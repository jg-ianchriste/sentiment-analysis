from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity


# Sample text for sentiment analysis
text = "I love using AI tools. They make life so much easier!"

# Get sentiment polarity and subjectivity
polarity, subjectivity = analyze_sentiment(text)

# Print the results
print(f"Text: {text}")
print(f"Sentiment Polarity: {polarity}")
print(f"Sentiment Subjectivity: {subjectivity}")