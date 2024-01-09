import requests


response = requests.get('http://192.168.8.100/temperatura')

if(response.headers.get('Content-Type')=='application/json'):
    print(response.json().get('temperatura'))
