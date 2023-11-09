import re
f = open('raw.txt', 'r', encoding='utf-8')
file = f.read()
# txt = "The_rain_in_Spain"
x = re.sub(r"(_)([a-zA-Z])", lambda a: a.group(2).capitalize(), file)  #txt
print(x)