import re
f = open('raw.txt', 'r', encoding='utf-8')
file = f.read()
x = re.findall('ab{2,3}', file)
print(x)