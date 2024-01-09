import requests

payload = {
"temperatura": 22
}

response = requests.post('http://192.168.8.100/temperatura',json=payload)

print(response.text)
print(response.status_code)
