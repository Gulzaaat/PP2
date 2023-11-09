import re
f = open('raw.txt', 'r', encoding='utf-8')
file = f.read() 
x = re.findall('[a-z]+_[a-z]+', file)
print(x)