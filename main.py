import requests

def get_username(username: str) -> dict:
    url = f'https://api.github.com/users/{username}'
    r = requests.get(url)
    if r.status_code == 200:
        return print(r.json())
    else:
        return print(r.status_code)

class User: ...

