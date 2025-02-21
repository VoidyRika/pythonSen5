import requests

response = requests.get("https://fake-json-api.mock.beeceptor.com/users")

try:
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Ошибка при выполнении запроса:", e)
