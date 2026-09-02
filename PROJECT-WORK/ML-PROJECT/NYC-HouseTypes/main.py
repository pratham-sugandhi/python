
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

COLUMNS = ["price", "minimum_nights", "number_of_reviews", "reviews_per_month",
                  "calculated_host_listings_count", "availability_365", "latitude", "longitude", "neighbourhood_group", "neighbourhood"]

# Load model
model = joblib.load("Model_Pipeline.pkl")

# Pydantic Model 
class Features(BaseModel):
    latitude: float = Field(..., ge=-90, le=90, description="Latitude Cordinates"),
    longitude: float = Field(..., ge=-180, le=180, description="Longitude Cordinates"),
    price: float = Field(..., ge=0, description="Price Per Night"),
    minimum_nights: int = Field(..., ge=1, description="Minimum_nights"),
    number_of_reviews: int = Field(..., ge=0, description="number_of_reviews"),
    reviews_per_month: float = Field(..., ge=0, description="reviews_per_month"),
    calculated_host_listings_count: int = Field(..., ge=0, description="calculated_host_listings_count"),
    availability_365 : int = Field(..., ge=0, le=365, description="availability_365"),
    neighbourhood_group: str = Field(..., min_length=1, description="neighbourhood_group")
    neighbourhood: str = Field(..., min_length=1, description="neighbourhood"),



@app.get("/")
def greet():
    return "Hello Guyss"


@app.post("/predict")
def predict(features: Features):
    row = pd.DataFrame([features.dict()], columns=COLUMNS)
    prediction = model.predict(row)
    probability = model.predict_proba(row)
    return {
        "Prediction_room_type": prediction[0],
        "Probability": probability.tolist()[0]
    }
