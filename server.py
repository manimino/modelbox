import dataclasses

from fastapi import FastAPI, APIRouter
import uvicorn
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel, validator


# don't use dataclasses decorator when inheriting from BaseModel, it's an either / or thing
class Sentence(BaseModel):
    text: str

    @validator('text')
    def text_non_empty(cls, v):
        if not v:
            raise ValueError('string must not be empty')
        return v


@dataclasses.dataclass
class Vector:
    vec: list


class ModelBox:

    def __init__(self, model):
        self.model = model
        self.router = APIRouter()
        self.router.add_api_route("/info", self.hello, methods=["GET"])
        self.router.add_api_route("/vectorize", self.vectorize, methods=["POST"])

    def hello(self):
        return {"Hello": str(self.model)}

    def vectorize(self, sentence: Sentence):
        vecs = self.model.encode(sentence.text)
        print(vecs)
        print(type(vecs))
        return Vector(vec=vecs.tolist())


app = FastAPI()
tformer = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
hello = ModelBox(tformer)
app.include_router(hello.router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

