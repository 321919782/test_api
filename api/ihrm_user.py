import requests


def user_login():
    header = {
        "Content-Type": "application/json"
    }
    url = "http://localhost:8080/api/sys/login"
    data = {
        "mobile": "13800000002",
        "password": "123456"
    }

    res = requests.post(url=url, headers=header, json=data)
    # print(res.json())

    token = res.json()["data"]
    return token


def user_get_all():
    token = "Bearer " + user_login()
    print(token)
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    url = "http://localhost:8080/api/sys/user"
    data = {
        "page": 1,
        "size": 10
    }
    res_data = requests.get(url=url, params=data, headers=header)
    data = res_data.json()
    print(data)
    return data


if __name__ == '__main__':
    print(user_login())
    print(user_get_all())
