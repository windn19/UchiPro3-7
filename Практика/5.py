import requests

API_URL = 'https://api.kinopoisk.dev/v1.3/movie/random'
API_TOKEN = 'ВАШ API KEY'
HEADERS = {'X-API-KEY': API_TOKEN}

response = requests.get(url=API_URL, headers=HEADERS)
result = response.json()
print(f'Фильм: {result["names"][0]["name"]}')
print(f'Описание: {result["description"]}')
print(f'Рейтинг Кинопоиска: {result["rating"]["kp"]}')
genres = []
for genre in result['genres']:
    genres.append(genre['name'])
print(f'Жанры: {", ".join(genres)}')
