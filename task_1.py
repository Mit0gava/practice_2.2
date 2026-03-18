import requests

urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

def check_status(code):
    if code == 200:
        return "доступен"
    elif code == 403:
        return "вход запрещен"
    elif code == 404:
        return "не найден"
    else:
        return "не доступен"

for url in urls:
    try:
        response = requests.get(url)
        status = check_status(response.status_code)

        print(f"{url} – {status} – {response.status_code}")

    except:
        print(f"{url} – ошибка соединения")