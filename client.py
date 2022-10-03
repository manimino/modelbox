import requests

print('Model info:')
info = requests.get('http://127.0.0.1:8000/info')
print(info.json())


print('')
request = {'text': 'The quick brown fox jumps over the lazy dog.'}
print('Running encode of', request)
resp = requests.post(url='http://127.0.0.1:8000/vectorize', json=request)
print(resp)
vector = resp.json()['vec'][:10]
print('Result:')
print(str(vector) + '...')
