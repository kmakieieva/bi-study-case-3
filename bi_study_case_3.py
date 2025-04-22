import os
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from mongodb import get_database

nltk.download('vader_lexicon')

# Data ingestion and preparation
db = get_database(os.environ.get("MONGODB_CONNECTION_STRING"))
collection = db["product_reviews"]

reviews = list(collection.find())

data = {
    'review': list(map(lambda review: review["Text"], reviews)),
    'product': list(map(lambda review: review["ProductName"], reviews))
}
df = pd.DataFrame(data)

# Sentiment analysis via VADER
sia = SentimentIntensityAnalyzer()


def get_sentiment(review):
    sentiment = sia.polarity_scores(review)
    return sentiment['compound']


df['sentiment_score'] = df['review'].apply(get_sentiment)
print("Data with Sentiment Scores")
print(df)

# Scatter plot visualization of VADER Sentiment Score per Product
plt.figure(figsize=(8, 10))
plt.scatter(df['product'], df['sentiment_score'], color='blue')
plt.xticks(rotation=90)
plt.title('VADER Sentiment Score per Product')
plt.xlabel('Product')
plt.ylabel('Sentiment Score')
plt.grid(True)
plt.tight_layout()
plt.show()
