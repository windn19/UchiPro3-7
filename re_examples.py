import re

pattern1 = r'\d\d\.\d\d'
pattern2 = r'\d\d\.\d\d\.\d{4}'
string = '01.12 должно было произойти что-то, но произойдет 02.12.2023'
p1 = r'\d{2}\.\d{2}'
p2 = r'(\d{2}\.){2}\d{4}'

p1 = re.compile(p1)
p2 = re.compile(p2)

match1 = re.search(pattern1, string)
match2 = re.search(pattern2, string)
print(match1)  # <re.Match object; span=(0, 5), match='01.12'>
print(match2.group())  # <re.Match object; span=(50, 60), match='02.12.2023'>

match1 = p1.search(string)
match2 = p2.search(string)
print(match1.group())
print(match2[0], match2.start(), match2.end(), match2.span(), match2.re, match2.string)
#
#
match3 = re.match(pattern1, string)
match4 = re.match(pattern2, string)
print(match3)  # <re.Match object; span=(0, 5), match='01.12'>
print(match4)  # None
# #
# #
match = re.findall(pattern1, string)
print(match)  # ['01.12', '02.12']
# #
result = re.split(pattern1, string)
print(result)  # ['', ' должно было произойти что-то, но произойдет ', '.2023']
# # # #
new_string = re.sub(pattern1, '-удалено-', string)
print(new_string)  # -удалено- должно было произойти что-то, но произойдет -удалено-.2023
match1 = re.search(pattern1, string, re.IGNORECASE)
print(match1)
