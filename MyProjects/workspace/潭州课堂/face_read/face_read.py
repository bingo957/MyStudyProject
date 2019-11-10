# coding: utf-8 #
#  author:李斌  #

import json
import base64
import requests

# 1、读取第一张图片数据
with open('1.png', 'rb') as f:
    pic_1 = f.read()
# 2、读取第二张图片数据
with open('2.png', 'rb') as f:
    pic_2 = f.read()
# 3、图片数据整合
image_data = json.dumps(
    [
        {'image': str(base64.b64encode(pic_1), 'utf-8'),
         'image_type': 'BASE64',
         'face_type': 'IDCARD',
         'quality_control': 'LOW'
         },
        {'image': str(base64.b64encode(pic_2), 'utf-8'),
         'image_type': 'BASE64',
         'face_type': 'IDCARD',
         'quality_control': 'LOW'
         }
    ]
)
# 4、拼接api接口
get_token = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lVfov6E1oaWZR9f4qIhd9Hjy&client_secret=Gubrc6RnMTdA3Eb8WumHIGrz4vHgCTdy"
API_url = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token="
access_token = json.loads(requests.get(get_token).text)['access_token']
url = API_url + access_token
# 5、请求api结果
response = json.loads(requests.post(url, image_data).text)['result']['score']
if response > 80:
    print('\n相似度:%d' % response + ' %,认证成功，是同一个人。')
else:
    print('\n认证失败,不是同一个人')