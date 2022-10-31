# -*- coding:utf-8 -*-

import requests
import json

endpoint = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"
params = {
    "date": "2019-05-13",
    "type":2
}
res = requests.get(endpoint, params=params)

# json形式が返り値なので辞書型に変換する
res_dict = json.loads(res.text)

print(res_dict)