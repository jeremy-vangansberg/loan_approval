from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from app.model import predict_pipeline

app = FastAPI()

['Term', 'NoEmp', 'NewExist', 'CreateJob', 'RetainedJob', 'UrbanRural',
       'RevLineCr', 'LowDoc', 'DisbursementGross', 'BalanceGross', 'GrAppv',
       'SBA_Appv']

class TextIn(BaseModel):
    Term : int
    NoEmp :int
    NewExist : float
    CreateJob : int
    RetainedJob : float
    UrbanRural : int
    RevLineCr : str
    LowDoc :str
    DisbursementGross : int
    BalanceGross : int
    GrAppv : int

class PredictionOut(BaseModel):
    category: str

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    category_pred = predict_pipeline(
        [
            payload.Term,
            payload.NoEmp,
            payload.NewExist,
            payload.CreateJob,
            payload.RetainedJob,
            payload.UrbanRural,
            payload.RevLineCr,
            payload.LowDoc,
            payload.DisbursementGross,
            payload.BalanceGross,
            payload.GrAppv
        ]
    )
    return {'category': category_pred}

# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0", port=8000)