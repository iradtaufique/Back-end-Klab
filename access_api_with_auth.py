import requests
# from requests.models import HTTPBasicAuth
from requests.auth import HTTPBasicAuth

resposne = requests.get('https://rapidapi.com/', auth=HTTPBasicAuth('username', 'passord'))
print(resposne.status_code)
# print(resposne.json())


# if resposne.status_code == 200:
#     print(resposne.json())