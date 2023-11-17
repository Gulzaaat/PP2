list = ['abc', 'xaaxa', 'Gulzat', 'fileee']
a = open('xaxa.txt', 'w')
for i in list:
    a.write('\n' + i)

a.close()