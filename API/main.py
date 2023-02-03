from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from app.model import predict_pipeline

app = FastAPI()


class TextIn(BaseModel):
    State : str
    NAICS :str
    Term : int
    NoEmp : int
    NewExist : str
    CreateJob : int
    RetainedJob : int
    UrbanRural :int
    RevLineCr : str
    LowDoc : str
    GrAppv : int

class PredictionOut(BaseModel):
    category: str

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    values = [x for x in payload.__dict__.values()]
    category_pred = predict_pipeline(
        values
    )
    return {'category': category_pred}

# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0", port=8000)