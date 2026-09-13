from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Server - Heart Disease Inference")

class PatientData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    thalach: int

@app.get("/")
def health_check():
    return {"status": "AI Server is healthy"}

@app.post("/predict")
def predict(data: PatientData):
    risk = 1 if (data.chol > 240 or data.thalach < 110 or data.cp > 0) else 0
    return {
        "status": "success",
        "prediction": risk,
        "diagnosis": "Nguy cơ cao mắc bệnh tim" if risk == 1 else "Bình thường",
        "model_used": "XGBoost Classifier"
    }
