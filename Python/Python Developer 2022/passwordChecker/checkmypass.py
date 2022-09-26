import requests

url = 'https://api.pwnedpasswords.com/range/' + 'password12'
res = requests.get(url)
print(res)