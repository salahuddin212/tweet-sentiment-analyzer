# 🧠 Tweet Sentiment Analyzer

This is a NLP project built in Python that analyzes the sentiment of tweets and classifies them as **Positive**, **Negative**, or **Neutral**. It also includes emojis for fun, summary statistics, and a chart visualization.

## 📦 Features

- Load tweets from a CSV file  
- Analyze sentiment using TextBlob  
- Append emoji labels to results  
- Display top positive/negative tweets  
- Count sentiment breakdown and plot a bar chart  
- Save results and chart to file  
- Input a custom tweet for instant analysis

## 🛠️ Technologies Used

- Python  
- Pandas  
- TextBlob  
- Matplotlib

## 📁 Project Structure
tweet_sentiment/ ├── tweets.csv # Sample tweets
├── sentiment_analysis.py # Main script
├── tweets_with_sentiment.csv # Output with sentiment and emoji
├── sentiment_plot.png # Saved chart image
├── requirements.txt # Dependencies
└── README.md # Project info


## 🚀 Getting Started

### 1. Install Dependencies
pip install -r requirements.txt python -m textblob.download_corpora

### 2. Run the Script
python sentiment_analysis.py

You’ll see the results printed in your terminal, a chart popup, and updated files saved in your folder.

### 3. Try a Custom Tweet!
After the script runs, you can type your own tweet and see how the analyzer classifies it.

## 📊 Example Output

| Tweet                             | Sentiment | Emoji |
|-----------------------------------|-----------|-------|
| I love this project!              | Positive  | 😊    |
| This is terrible and frustrating. | Negative  | 😞    |
| Not bad, not good either.         | Neutral   | 😐    |


## 📄 License

For learning purposes only. Built with open-source Python tools.
