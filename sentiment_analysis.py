import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Analyze polarity and classify sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"


# Add emoji based on sentiment
def get_emoji(sentiment):
    return {
        "Positive": "😊",
        "Negative": "😞",
        "Neutral": "😐"
    }.get(sentiment, "")


# Load tweets
df = pd.read_csv("tweets.csv", quotechar='"')

# Apply sentiment analysis and emoji
df["Sentiment"] = df["tweet"].apply(analyze_sentiment)
df["Emoji"] = df["Sentiment"].apply(get_emoji)

# Print full table
print("\n--- Analyzed Tweets ---")
print(df[["tweet", "Sentiment", "Emoji"]])

# Save to new CSV
df.to_csv("tweets_with_sentiment.csv", index=False)

# Print summary stats
print("\n--- Sentiment Counts ---")
print(df["Sentiment"].value_counts())

# Show top tweets
print("\nTop Positive Tweets:")
print(df[df["Sentiment"] == "Positive"]["tweet"].head(3))

print("\nTop Negative Tweets:")
print(df[df["Sentiment"] == "Negative"]["tweet"].head(3))

# Plot sentiment distribution
df["Sentiment"].value_counts().plot(kind="bar", title="Sentiment Breakdown")
plt.xlabel("Sentiment")
plt.ylabel("Tweet Count")
plt.tight_layout()
plt.savefig("sentiment_plot.png")
plt.show()

# Optional: analyze a single tweet from the user
user_input = input("\nType your own tweet to analyze: ")
result = analyze_sentiment(user_input)
emoji = get_emoji(result)
print(f"Sentiment: {result} {emoji}")
