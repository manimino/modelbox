import json
import requests

from iris.main import PredInput


def test_iris_predict(server):
    p = PredInput(petal_length=1, id=10, petal_width=1, sepal_length=1, sepal_width=1)
    print(p.__dict__)
    payload = json.dumps(p.__dict__)
    print(payload)
    response = requests.post("http://127.0.0.1:7890/predict", data=payload)
    assert response.status_code == 200
    resp = json.loads(response.json())
    assert resp['prediction'] in [0, 1, 2]   # check match to some class label
