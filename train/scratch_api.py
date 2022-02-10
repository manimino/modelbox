import json
import uvicorn

from typing import Optional, List

from pydantic import BaseModel
from fastapi import FastAPI, Response


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


app = FastAPI()


@app.post("/predict")
async def predict(item: Item):
    yhat = 1/item.price
    return Response(json.dumps({'prediction': yhat, 'info': ''}), status_code=200, media_type='application/json')


@app.post('/predict-many')
async def predict_many(items: List[Item]):
    ret = []
    for item in items:
        yhat = 1/item.price
        ret.append({'prediction': yhat, 'info': ''})
    return Response(json.dumps(ret), status_code=200, media_type='application/json')


if __name__ == '__main__':
    uvicorn.run(app)