import requests

def get_username(username: str) -> dict:
    url = f'https://api.github.com/users/{username}'
    r = requests.get(url)
    return r.json()

class User:

    def __init__(self, login, id, avatar_url, html_url) -> None:
        self.login = login
        self.id = id
        self.avatar_url = avatar_url
        self.html_url = html_url

    def get_login (self):
        return self.login
