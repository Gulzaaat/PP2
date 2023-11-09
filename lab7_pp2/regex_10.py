import re
f = open('raw.txt', 'r', encoding='utf-8')
file = f.read()
# camel to snake
# txt2 = "TheRainInSpain"
x2 = re.sub(r"([a-z])([A-Z])", r"\1_\2", file) #txt2
print(x2.lower())