import requests

try:
    response = requests.get('http://sadasdasd.com')
    print(response.status_code)
except requests.exceptions.ConnectionError:
    print('Connection Error! you are trying to reach invalid link!')    

""" if you don't know the specific type of exception error you will get
    you can use 
    request.exceptions.RequestException in the except keyword.
 
 """    