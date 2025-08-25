#!/usr/bin/env python
# coding: utf-8

import nltk

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment


sample_text = "I absolutely adore this new phone! It's fast and the camera is amazing."
result = analyze_sentiment(sample_text)
print(f"Sentiment polarity: {result.polarity}, subjectivity: {result.subjectivity}")
