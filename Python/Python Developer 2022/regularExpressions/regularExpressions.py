import re

pattern = re.compile('this')
string = 'search inside of this text please!'

a = (re.search('this', string))
print(a.span())
print(a.end())
print(a.start())
print(a.group())

b = pattern.search(string)
print(b)