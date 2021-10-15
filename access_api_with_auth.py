import requests
# from requests.models import HTTPBasicAuth
from requests.auth import HTTPBasicAuth

resposne = requests.get('https://api.github.com/users', auth=HTTPBasicAuth('iradtaufique', 'irad1423'))
print(resposne.status_code)
# print(resposne.json())


# if resposne.status_code == 200:
#     print(resposne.json())