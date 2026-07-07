from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

app = FastAPI(title="House Price Prediction API")

# Request Body
class House(BaseModel):
    area: float


@app.get("/")
def home():
    return {
        "message": "Welcome to House Price Prediction API"
    }


@app.post("/predict")
def predict(data: House):
    prediction = model.predict([[data.area]])

    return {
        "predicted_price": round(prediction[0], 2)
    }