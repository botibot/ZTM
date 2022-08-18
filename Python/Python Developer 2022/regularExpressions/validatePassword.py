import re


password = '1asdgf$#@90'

passwordPattern = re.compile(r'[A-Za-z0-9$%#@]{8,}\d')
check = passwordPattern.fullmatch(password)

print(check)