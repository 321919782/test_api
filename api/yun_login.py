import json
import requests


# 1.使用request去完成 请求的接口任务，并将JSON结果返回


def yun_login_api(username, password):
    url = "http://yun.zenm.vip/iot/account/login/"
    header = {
        "Content-Type":"application/json"
    }

    data = {
        "username": username,
        "password": password
    }
    json_data = json.dumps(data)
    res = requests.post(url=url, data=json_data,headers=header )
    json_data = res.json()
    return json_data