import sys, requests


def login():
    data = {
        "email": "root@dasith.works",
        "password": "Kekc8swFgD6zU"
    }
    headers = {"Content-Type": "application/json"}

    r = requests.post("http://10.10.11.120:3000/api/user/login", data=data)
    print(r.text)

def register():
    data = {"name": "dasith", "email": "root@dasith.works", "password": "Kekc8swFgD6zU"}

    r = requests.post("http://10.10.11.120:3000/api/user/register", data=data)
    print(r.text)

register()
