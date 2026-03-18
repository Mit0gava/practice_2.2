import requests

BASE_URL = "https://api.github.com"


def show_profile():
    username = input("Введите username: ")

    url = f"{BASE_URL}/users/{username}"
    data = requests.get(url).json()

    print("\nИмя:", data.get("name"))
    print("Профиль:", data.get("html_url"))
    print("Репозитории:", data.get("public_repos"))
    print("Подписки:", data.get("following"))
    print("Подписчики:", data.get("followers"))


def show_repos():
    username = input("Введите username: ")

    url = f"{BASE_URL}/users/{username}/repos"
    repos = requests.get(url).json()

    for repo in repos:
        print("\nНазвание:", repo["name"])
        print("Ссылка:", repo["html_url"])
        print("Язык:", repo["language"])
        print("Видимость:", "private" if repo["private"] else "public")
        print("Основная ветка:", repo["default_branch"])


def search_repo():
    name = input("Название репозитория: ")

    url = f"{BASE_URL}/search/repositories?q={name}"
    data = requests.get(url).json()

    for repo in data["items"][:5]:
        print(repo["name"], "-", repo["html_url"])


while True:
    print("\n1 Профиль пользователя")
    print("2 Репозитории пользователя")
    print("3 Поиск репозитория")
    print("4 Выход")

    choice = input("Выбор: ")

    if choice == "1":
        show_profile()

    elif choice == "2":
        show_repos()

    elif choice == "3":
        search_repo()

    elif choice == "4":
        break