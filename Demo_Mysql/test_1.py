import requests
import json


def get_token():
    url1="https://www.baidu.com"
    content={'jsom'}
    web=requests.get(url=url1,params=content)
    print(web.url)
    