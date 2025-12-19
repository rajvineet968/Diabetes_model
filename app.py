from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Diabetes Prediction API")

# Load pipeline model
model = joblib.load("models/random_forest_model.pkl")

# ---- Input schema (MATCH TRAINING COLUMNS) ----
class DiabetesInput(BaseModel):
    Age: float
    BMI: float
    BloodPressure: float
    Glucose: float
    Insulin: float
    SkinThickness: float
    DiabetesPedigree: float
    Pregnancies: float

@app.get("/")
def home():
    return {"message": "Random Forest Diabetes API is running"}

@app.post("/predict")
def predict(data: DiabetesInput):
    # Convert JSON → DataFrame (THIS IS THE FIX)
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
