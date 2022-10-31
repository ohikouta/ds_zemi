# -*- coding:utf-8 -*-

import requests

docid = "S100FIZV"
endpoint = f"https://disclosure.edinet-fsa.go.jp/api/v1/documents/{docid}"
params = {
    "type": 1
}
res = requests.get(endpoint, params=params).content

print(type(res))

res.decode("utf-8")

with open(res, 'wb') as f:
    print(f)

# 返ってくるバイナリデータをzip形式のファイルとして保存

import zipfile

zip = zipfile.ZipFile("sample.zip", 'w', zipfile.ZIP_DEFLATED)

zip.close()

with zipfile.ZipFile('sample.zip') as zf:
    print(zf.namelist())
    
