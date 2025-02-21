import requests

try:
    response = requests.get("https://fake-json-api.mock.beeceptor.com/users")
    response.raise_for_status()
    data = response.json()

    for user in data:
        print(user)
except requests.exceptions.RequestException:
    print("Ошибка при запросе данных")
