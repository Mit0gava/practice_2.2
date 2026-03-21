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
        json.dump(groups, f, indent=4, ensure_ascii=False)


def get_rates():
    try:
        response = requests.get(URL, timeout=5)
        data = response.json()
        return data["Valute"]
    except:
        print("Ошибка загрузки курсов валют")
        return {}


def show_all_rates(rates):
    for code, info in rates.items():
        print(f"{code} — {info['Value']}")


def find_currency(rates):
    code = input("Введите код валюты: ").upper()
    if code in rates:
        print(f"{code} — {rates[code]['Value']}")
    else:
        print("Валюта не найдена")


def create_group(groups, rates):
    name = input("Название группы: ")

    if name in groups:
        print("Такая группа уже существует")
        return

    groups[name] = []

    while True:
        code = input("Добавить валюту (или stop): ").upper()
        if code == "STOP":
            break

        if code not in rates:
            print("Такой валюты нет")
            continue

        if code in groups[name]:
            print("Уже добавлена")
            continue

        groups[name].append(code)

    save_groups(groups)
    print("Группа сохранена")


def show_groups(groups):
    if not groups:
        print("Групп пока нет")
        return

    for name, codes in groups.items():
        print(f"{name}: {', '.join(codes) if codes else 'пусто'}")


def edit_group(groups, rates):
    name = input("Название группы: ")

    if name not in groups:
        print("Группа не найдена")
        return

    print("1 Добавить валюту")
    print("2 Удалить валюту")

    choice = input("Выбор: ")

    if choice == "1":
        code = input("Код валюты: ").upper()

        if code not in rates:
            print("Такой валюты нет")
            return

        if code in groups[name]:
            print("Уже есть в группе")
            return

        groups[name].append(code)
        print("Добавлено")

    elif choice == "2":
        code = input("Код валюты: ").upper()

        if code in groups[name]:
            groups[name].remove(code)
            print("Удалено")
        else:
            print("Такой валюты нет в группе")

    save_groups(groups)


# --- основной код ---

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
    if not rates:
        continue

    if choice == "1":
        show_all_rates(rates)

    elif choice == "2":
        find_currency(rates)

    elif choice == "3":
        create_group(groups, rates)

    elif choice == "4":
        show_groups(groups)

    elif choice == "5":
        edit_group(groups, rates)

    elif choice == "6":
        print("Выход...")
        break

    else:
        print("Неверный выбор")