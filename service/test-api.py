import requests

# x = requests.get('http://localhost:8000/').json()
# print(x)

x = requests.post('http://localhost:8000/',json={
    "username:" : "Hello World",
    "password": "asdddddddddddd"
}).json()

print("DONE")
print(x)