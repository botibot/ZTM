import requests

#!md5 5d41402abc4b2a76b9719d911017c592 = "hello"

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)
print(res)