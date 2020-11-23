
import requests
import chevron
from jsonpath import jsonpath
from jsonschema import validate
import json

from schema import Schema


class TestDemo:


    def test_demo_1(self):
        url = 'https://httpbin.testing-studio.com/get'
        res = requests.get(url)
        print(res.status_code)
        print(res.json())
        assert res.status_code == 200

    def test_demo_2(self):
        url = 'https://api.github.com/events'
        res = requests.get(url)
        print(res.json())
        assert res.status_code == 200

    def test_query(self):
        payload = {
            "level":1,
            "name":"ceshiren"
        }
        res = requests.get("https://httpbin.testing-studio.com/get",params=payload)
        print(res.text)
        assert res.status_code == 200


    def test_form(self):
        payload ={
            "name":"ceshiren",
            "age":18
        }
        res = requests.post("https://httpbin.testing-studio.com/post",data = payload)
        print(res.text)
        assert res.status_code == 200


    def test_headers(self):
        payload = {
            "name": "ceshiren",
            "age": 18
        }
        headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        res = requests.post("https://httpbin.testing-studio.com/post", data=payload, headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_post_json(self):
        payload = {
            "name": "ceshiren",
            "age": 18
        }
        headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        res = requests.post("https://httpbin.testing-studio.com/post", json=payload, headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_jsonpath(self):
        headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        url = 'https://home.testing-studio.com/categories.json'
        res = requests.get(url= url,headers=headers)
        # 使用jsonpath进行断言
        # 从根元素开始查找，查找第一个name
        assert jsonpath(res.json(), '$..name')[0] == '开源项目'


    def test_schema(self):
        headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        url = "https://testerhome.com/api/v3/topics.json"
        res = requests.get(url= url, headers=headers)
        schema_json = json.load(open('schema.json'))
        Schema(int).validate(10)
        # 弱
        validate(res.json(), schema_json)

    def test_cookie_manul(self):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                   "Cookie":"dengshuyue"
                   }
        url = "http://httpbin.ceshiren.com/cookies"
        res = requests.get(url=url, headers=headers)
        print(res.request.headers)

    def test_cookie_dict(self):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        headers['Cookie'] = 'dengshuyue'
        url = "http://httpbin.ceshiren.com/cookies"
        res = requests.get(url=url, headers=headers)
        print(res.request.headers)

    def test_cookie_params(self):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        url = "http://httpbin.ceshiren.com/cookies"

        cookie_data = {"dengshuyue": "always win",
                       "aisosad": "aiyasosand"
                       }
        res = requests.get(url=url, headers=headers,cookies = cookie_data)
        print(res.request.headers)


