import json
from pprint import pprint

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N960F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.12.1620(0x27000C34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm32',
    'Referer': 'https://servicewechat.com/wx4554c1e6dfadc8ed/93/page-frame.html'
}

# url = 'https://www.xiaohongshu.com/api/store/ps/products/v1?sid=session.1589005728496063078399&keyword=%E6%89%8B%E6%8C%81%E5%90%B8%E5%B0%98%E5%99%A8&page=1&per_page=20'
url = 'https://www.xiaohongshu.com/api/store/ps/products/v1?sid=session.1589005728496063078399&keyword=手持吸尘器&page=1&per_page=20'


response = requests.get(url, headers=headers)
res = response.text
pprint(json.loads(res))

