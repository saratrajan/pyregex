import re

nameAge = '''
Tom is 8 and Joe is 34
Mary is 33
'''

ages = re.findall(r'\d{1,3}', nameAge)
names = re.findall(r'[A-Z][a-z]*', nameAge)

x = 0
ageDict = {}

for eachname in names:
    ageDict[eachname] = ages[x]
    x += 1

print(ageDict)