import re
f = open('raw.txt', 'r', encoding='utf-8')
file = f.read()
x = re.sub("[ ,.]", ":", file)
print(x)