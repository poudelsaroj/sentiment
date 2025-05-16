from app.models.sentiment import analyze_sentiment


def test_positive_sentiment():
    text = "I love this product!"
    assert analyze_sentiment(text) == "positive"


def test_negative_sentiment():
    text = "This is terrible."
    assert analyze_sentiment(text) == "negative"


def test_neutral_sentiment():
    text = "It is acceptable."
    assert analyze_sentiment(text) == "neutral"
