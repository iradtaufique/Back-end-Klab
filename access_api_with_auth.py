import requests
# from requests.auth import HTTPBasicAuth

resposne = requests.get('https://api.github.com/users', auth=('username', 'yourpassword'))
print(resposne.status_code)
if resposne.status_code == 200:
    print(resposne.json())