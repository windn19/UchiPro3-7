import re

string = input()
pattern = r'\d{1,2}\.\d{1,2}\.\d{4}'
result = re.findall(pattern, string)
print(*result)

# 4.10.1957: запуск Спутник-1. 03.11.1957 запуск Спутник-2 с собакой Лайка.
