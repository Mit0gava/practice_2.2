import requests
import json

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
SAVE_FILE = "save.json"


def load_groups():
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_groups(groups):
    with open(SAVE_FILE, "w") as f:
        json.dump(groups, f, indent=4)


def get_rates():
    data = requests.get(URL).json()
    return data["Valute"]


groups = load_groups()

while True:
    print("\n1 Показать все валюты")
    print("2 Найти валюту по коду")
    print("3 Создать группу")
    print("4 Показать группы")
    print("5 Изменить группу")
    print("6 Выход")

    choice = input("Выбор: ")

    rates = get_rates()

    if choice == "1":
        for code in rates:
            print(code, "-", rates[code]["Value"])

    elif choice == "2":
        code = input("Введите код валюты: ").upper()
        if code in rates:
            print(code, "-", rates[code]["Value"])
        else:
            print("Валюта не найдена")

    elif choice == "3":
        name = input("Название группы: ")
        groups[name] = []

        while True:
            code = input("Добавить валюту (или stop): ").upper()
            if code == "STOP":
                break
            groups[name].append(code)

        save_groups(groups)

    elif choice == "4":
        print(groups)

    elif choice == "5":
        name = input("Название группы: ")

        if name in groups:
            print("1 Добавить валюту")
            print("2 Удалить валюту")

            c = input("Выбор: ")

            if c == "1":
                code = input("Код валюты: ").upper()
                groups[name].append(code)

            elif c == "2":
                code = input("Код валюты: ").upper()
                if code in groups[name]:
                    groups[name].remove(code)

            save_groups(groups)

    elif choice == "6":
        break