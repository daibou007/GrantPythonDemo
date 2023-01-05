# -*- encoding=utf8 -*-
__author__ = "yangpengliang"


import base64
import json
import requests


def test():
    APP_ID = 9167
    APP_SECRET = "1VZjzl643IT2glwUOb3QbksMA9b5bsRv"
    uid = 333
    userName = "aaabbb"
    url = "https://api.gobelieve.io/v2/auth/grant"
    obj = {"uid":uid, "user_name":userName}
    auth = str(APP_ID) + ":" + APP_SECRET
    basic = base64.b64encode(auth.encode())
    headers = {'Content-Type': 'application/json; charset=UTF-8','Authorization': 'Basic ' + str(basic)}

    res = requests.post(url, data=json.dumps(obj), headers=headers)
    if res.status_code == 200:
        obj = json.loads(res.text)
        print(obj)
        token = obj["data"]["token"]
        print(token)

test()