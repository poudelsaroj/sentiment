from fastapi import APIRouter
from pydantic import BaseModel
from app.models.sentiment import analyze_sentiment

router = APIRouter()


class TextInput(BaseModel):
    text: str


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    sentiment: str


@router.post("/analyze", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):
    sentiment = analyze_sentiment(request.text)
    return {"sentiment": sentiment}
