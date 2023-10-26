import json

with open('sample-data.json') as json_file:
	data = json.load(json_file)

print('Interface Status')
print('='*84)
names = ['DN', 'Description', 'Speed', 'MTU']
form = "{:<47}  {:<15}  {:<10}  {:<6}"
print(form.format(*names))
print('-'*47 + '  ' + '-'*15 + '  ' + '-'*10 + '  ' + '-'*6)
n = data["totalCount"]

for i in data['imdata']:
	dat = i['l1PhysIf']['attributes']
	print(form.format(*(dat['dn'], '' if dat.get('description') == None else dat['description'], dat['speed'], dat['mtu'])))
