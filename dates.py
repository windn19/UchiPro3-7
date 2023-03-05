import re


pattern = r'(\d{4})/(\d{1,2})/(\d{1,2})'
string = "1999/12/31 2022/1/1 1987/12/7"
new_string = re.sub(pattern, r'\3.\2.\1', string)
print(new_string)
