import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

# ------------------------------
# Streamlit Page Config (MUST be first Streamlit call)
# ------------------------------
st.set_page_config(page_title="IMDB Sentiment Analysis", page_icon="🎬", layout="centered")

# ------------------------------
# Load Dataset Word Index & Model
# ------------------------------
@st.cache_resource
def load_resources():
    word_index = imdb.get_word_index()
    reverse_word_index = {value: key for key, value in word_index.items()}
    model = load_model('simple_rnn_imdb.h5')
    return word_index, reverse_word_index, model

word_index, reverse_word_index, model = load_resources()

# ------------------------------
# Helper Functions
# ------------------------------
def decode_review(encoded_review):
    """Convert encoded review back to words"""
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

def preprocess_text(text):
    """Preprocess user input for the model"""
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

def predict_sentiment(review):
    """Run sentiment prediction"""
    preprocessed_input = preprocess_text(review)
    prediction = model.predict(preprocessed_input, verbose=0)
    sentiment = 'Positive 😊' if prediction[0][0] > 0.5 else 'Negative 😞'
    return sentiment, float(prediction[0][0])

# ------------------------------
# Streamlit App UI
# ------------------------------
st.markdown(
    """
    <style>
    .stTextArea textarea {
    background-color: #ffffff;   /* white background */
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
    color: #1a1a1a;              /* deep gray text */
    border: 1px solid #d0d7de;   /* light gray border */
}

.result-box {
    background-color: #e8f0fe;   /* very light blue highlight */
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: #202124;              /* strong dark gray text */
}

    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎬 IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review below, and the model will classify it as **Positive** or **Negative**.")

# User input
user_input = st.text_area("✍️ Movie Review", placeholder="Type your review here...")

if st.button("🔍 Classify Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a movie review before classifying.")
    else:
        sentiment, score = predict_sentiment(user_input)

        st.markdown(
            f"""
            <div class="result-box">
                Sentiment: {sentiment}  
                <br><br>
                Prediction Confidence: **{score:.2f}**
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("ℹ️ Enter a movie review above and click **Classify Sentiment**.")
