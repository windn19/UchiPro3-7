import requests

response = requests.get('https://swapi.dev/api/planets/10/')
print(response)
text = response.text
print(type(text), text)
json = response.json()
print(type(json), json)
