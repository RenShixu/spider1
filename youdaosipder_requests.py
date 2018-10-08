import requests
import json

# 定义请求URL地址和参数
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rules"
data = {'i': '中国',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1538809813781',  # 每次翻译都会改变 需要根据每次翻译生成的值设定
        'sign': '736deab5735d42b056b0a6091b0a7cd3',  # 每次翻译都会改变 需要根据每次翻译生成的值设定
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'}

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': len(data),
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # cookie每次翻译都会改变 需要根据每次翻译生成的值设定
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=666990059.4513776; OUTFOX_SEARCH_USER_ID=752452795@10.169.0.83; JSESSIONID=aaatGHo2PeZzrfuH14hzw; ___rl__test__cookies=1538809813768',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3452.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

#发送请求，爬取信息
res = requests.post(url,data = data)
response = requests.post(url,data=data)
print(response.content.decode('utf-8'))


# 解析结果
str_json = res.content.decode("utf-8")
#print(str_json)
myjson = json.loads(str_json)

print(myjson)

