"""
使用正则表达式将网页Headers转化成python字典格式
"""
import re
header_str = """
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-Hans-CN, zh-Hans; q=0.5
Cache-Control: no-cache
Connection: Keep-Alive
Content-Length: 246
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: OUTFOX_SEARCH_USER_ID=620234973@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1891152210.750806; JSESSIONID=aaaUwTO7CHQG5gNIXKpTw; ___rl__test__cookies=1560408828769
Host: fanyi.youdao.com
Origin: http://fanyi.youdao.com
Referer: http://fanyi.youdao.com/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134
X-Requested-With: XMLHttpRequest
"""
pattern = '^(.*?):(.*)$'
for line in header_str.splitlines():  # 反向引用
    print(re.sub(pattern, '\'\\1\':\'\\2\',', line))
