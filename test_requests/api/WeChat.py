# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 10:19 上午
# @Author  : Saber
# @FileName: WeChat.py
# @Software: PyCharm


from LaGouJiekou_Projects.test_requests.api.base_api import BASEAPI

class wechat(BASEAPI):
    def test_get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwe653983e4c732493",
                "corpsecret": "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
            }
        }
        r = self.send_api(data)
        try:
            return r['access_token']
        except Exception as e:
            raise ValueError("requests token error")