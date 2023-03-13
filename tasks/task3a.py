import re


pat = r"8\(\d{3}\)\d{3}-(\d{2}-?){2}"
pat1 = r'8\(\d{3}\)\d{3}(-\d{2}){2}'
# s = input()

s = "8(912)654-84-12, телефон 7(987)456-45-45 \n или 8(456)1212123 8(456)123-45-45 "

print(re.findall(pat1, s))

for it in re.finditer(pat1, s):
    print(it[0])
