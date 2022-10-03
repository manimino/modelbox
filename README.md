# modelbox

Really basic model serving template. Uses FastAPI in a Docker.

This API vectorizes sentences. Send it some text, get a vector back.

### Usage 

Run it (not in docker):

```
pip install -r requirements.txt
python server.py
python client.py
```

`client.py` will print the model info and a sample encoding. 

You can also browse [the docs endpoint](http://127.0.0.1:8000/docs) and try things interactively there.

Run in docker:
```
docker build . -t modelbox
docker run -p 8000:8000 modelbox
python client.py
```

### Batch operations

In practice you'd probably want to batch the encodings, doing one sentence at a time is inefficient. Either
add an endpoint that accepts a list of texts or run it in a queue and have it pull many items off the queue at once.
