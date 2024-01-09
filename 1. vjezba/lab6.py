import requests

response = requests.get('http://ip.jsontest.com/')

if(response.headers.get('Content-Type')=='application/json'):
    print(response.json().get('ip'))