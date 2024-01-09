import requests

response = requests.get('http://192.168.8.100/login')

print(response.text)
print(response.status_code)

for k, v in response.headers.items():
    print(f'{k}: {v}')


