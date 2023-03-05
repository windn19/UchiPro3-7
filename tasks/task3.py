import re

#
pat = re.compile(r"(кот.*){2,}")
n = int(input())
for _ in range(n):
    s = input()
    match = pat.search(s)
    if match:
        print(match[0])

# pat = r'кот'
# n = int(input())
# for _ in range(n):
#     s = input()
#     if len(re.findall(pat, s)) > 1:
#         print(s)
#     else:
#         print('Нет нужного числа повторений')

# кот-кот
# кот и кофе
# кот картошка
# котик играет с котом
# ток кот тко отк
