import requests

params = {
    'lang': 'ru',
    'format': 'j1'
}

response = requests.get(
    'https://wttr.in/Moscow',
    params=params
)
response.encoding = 'utf-8'
print(response.url)
print(response.text)
