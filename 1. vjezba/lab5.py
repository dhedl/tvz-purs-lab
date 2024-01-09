import requests

params = {
    "temperatura": 21
}
response = requests.delete('http://192.168.8.100/temperatura', params=params)

print(response.text)
print(response.status_code)
