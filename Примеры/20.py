import requests

response = requests.get('https://uchi.ru/')
response.encoding = 'utf-8'
print(type(response), response)
print(response.text)

