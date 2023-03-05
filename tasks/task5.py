import re


pattern = r'[-_\.\,!*\s]+'

string = input()
print(*re.split(pattern, string), sep='\n')

# привет   дом-кот__время.место,дверь***.дерево вечер_--рука!!поэт*два
