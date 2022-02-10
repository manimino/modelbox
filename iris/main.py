import json
import uvicorn

import numpy as np

from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator

from iris.model import get_model


class PredInput(BaseModel):
    id: int
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    @validator('id')
    def validate_id(cls, v):
        assert v > 0
        return v


app = FastAPI()


@app.post('/predict')
async def app_predict(p: PredInput):
    model, model_id = get_model()
    x = np.array([p.sepal_length, p.sepal_width, p.petal_length, p.petal_width])
    x = x.reshape([1, len(x)])
    yhat = model.predict(x)
    return json.dumps({'prediction': float(yhat[0]), 'model': model_id})


def run_api(port=7890):
    uvicorn.run(app, port=port)


if __name__ == '__main__':
    run_api()