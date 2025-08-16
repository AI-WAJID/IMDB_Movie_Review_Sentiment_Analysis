# 🎬 IMDB Movie Review Sentiment Analysis

A **real-time sentiment analysis web application** that classifies movie reviews as **Positive** or **Negative** using a pre-trained Simple RNN model. Built with Streamlit for an interactive user experience.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🚀 Live Demo

[**Try the App Live →**](#) *(https://imdb-movie-review-sentiment-analysis-d4pc.onrender.com/)*

## ✨ Features

- 🎯 **Real-time Sentiment Analysis** - Instant classification of movie reviews
- 📊 **Confidence Scoring** - Shows prediction probability (0-1 scale)
- 🎨 **Modern UI Design** - Clean, responsive interface with custom styling
- ⚡ **Fast Performance** - Optimized with Streamlit caching
- 🧠 **Pre-trained Model** - Trained on 25,000 IMDB movie reviews
- 📱 **Mobile Friendly** - Works seamlessly across devices

## 🏗️ Architecture

### Model Specifications
- **Architecture**: Simple RNN (Recurrent Neural Network)
- **Input**: Text reviews (max 500 tokens)
- **Output**: Binary sentiment classification
- **Parameters**: ~1.3M trainable parameters
- **Dataset**: IMDB Movie Reviews (25k samples)

### Tech Stack
```
Frontend:    Streamlit
Backend:     Python 3.8+
ML Framework: TensorFlow/Keras
Model:       Simple RNN
Deployment:  Render
```

## 📦 Installation

### 1. Clone Repository
```bash
git clone https://github.com/AI-WAJID/IMDB_Movie_Review_Sentiment_Analysis.git
cd imdb-sentiment-analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📁 Project Structure

```
imdb-sentiment-analysis/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── simple_rnn_imdb.h5    # Pre-trained model file
├── Procfile              # Render deployment config
├── imdb.ipynb            # Model training notebook
├── prediction.ipynb      # Model testing/prediction examples
└── README.md             # Project documentation
```

## 🔧 Usage

1. **Launch the App**: Run `streamlit run app.py`
2. **Enter Review**: Type or paste a movie review in the text area
3. **Get Prediction**: Click "🔍 Classify Sentiment"
4. **View Results**: See sentiment classification and confidence score

### Example Reviews to Try:
```
✅ Positive: "This movie was absolutely fantastic! Great acting and amazing plot."
❌ Negative: "Terrible movie, boring plot and poor acting. Complete waste of time."
```

## 🧠 Model Details

### Neural Network Architecture
```python
Model: Sequential
├── Embedding(10000, 128)     # Word embeddings
├── SimpleRNN(128)            # RNN layer
└── Dense(1, sigmoid)         # Output layer
```

### Performance Metrics
- **Training Accuracy**: ~85%
- **Validation Accuracy**: ~83%
- **Model Size**: 5.01 MB
- **Inference Time**: <100ms

## 🚀 Deployment

### Deploy on Render
1. Push code to GitHub
2. Connect repository to [Render](https://render.com)
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `streamlit run app.py`

### Deploy on Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku main
```

## 🛠️ Development

### Model Training
The model was trained using:
- **Dataset**: IMDB Movie Reviews (50k reviews)
- **Split**: 25k training, 25k validation
- **Epochs**: Multiple epochs with early stopping
- **Optimizer**: Adam
- **Loss**: Binary crossentropy

### Code Structure
- `load_resources()`: Loads model and word indices with caching
- `preprocess_text()`: Tokenizes and pads input text
- `predict_sentiment()`: Runs inference and returns results
- Custom CSS styling for enhanced UI

## 📊 Sample Predictions

| Review Text | Predicted Sentiment | Confidence |
|------------|-------------------|------------|
| "Amazing movie!" | Positive 😊 | 0.89 |
| "Worst film ever" | Negative 😞 | 0.92 |
| "It was okay" | Positive 😊 | 0.54 |

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## 📝 Requirements

```txt
tensorflow>=2.8.0
streamlit>=1.28.0
numpy>=1.21.0
pandas>=1.3.0
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **IMDB Dataset**: Stanford AI Lab
- **TensorFlow**: Google Brain Team
- **Streamlit**: Streamlit Inc.

## 📧 Contact

**Your Name** - [wajidthephenom@gmai.com]

**Project Link**: https://github.com/AI-WAJID/IMDB_Movie_Review_Sentiment_Analysis.git 

---

⭐ **Star this repository if you found it helpful!**
