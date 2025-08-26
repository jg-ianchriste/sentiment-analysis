import pytest
from sentiment2 import analyze_sentiment


def test_analyze_sentiment_positive():
    text = "I love using AI tools. They make life so much easier!"
    polarity, subjectivity = analyze_sentiment(text)
    assert polarity > 0
    assert 0 <= subjectivity <= 1


def test_analyze_sentiment_negative():
    text = "I hate bugs in the code. They make life so much harder!"
    polarity, subjectivity = analyze_sentiment(text)
    assert polarity < 0
    assert 0 <= subjectivity <= 1


def test_analyze_sentiment_neutral():
    text = "The sky is blue."
    polarity, subjectivity = analyze_sentiment(text)
    assert polarity == 0
    assert 0 <= subjectivity <= 1
