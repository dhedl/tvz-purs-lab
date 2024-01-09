import requests

payload = {
"username": 'PURS',
"password": '1234'
}
response = requests.post('http://192.168.8.100/login',
json=payload)

print(response.text)
print(response.status_code)


