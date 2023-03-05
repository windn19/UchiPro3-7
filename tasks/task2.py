import re

string = input()
# pattern = r'[А-Я][а-я]+\s[А-Я][а-я]+\s[А-Я][а-я]+'
pattern = re.compile(r'([А-Я][а-я]+\s?){3}')
# result = re.sub(pattern, 'Неизвестный ', string)
result =pattern.sub('Неизвестный ', string)
print(result)


# Иванов Иван Иванович столкнулся с Петровым Петром Петровичем и за этим наблюдал Михайлов Михаил Михайлович
