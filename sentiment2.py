from textblob import TextBlob

# Sample text for sentiment analysis
text = "I love using AI tools. They make life so much easier!"

# Create a TextBlob object
blob = TextBlob(text)

# Get sentiment polarity and subjectivity
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

# Print the results
print(f"Text: {text}")
print(f"Sentiment Polarity: {polarity}")
print(f"Sentiment Subjectivity: {subjectivity}")