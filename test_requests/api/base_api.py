# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 8:16 下午
# @Author  : Saber
# @FileName: base_api.py
# @Software: PyCharm

import requests

class BASEAPI:

    def send_api(self, req: dict):
        return requests.request(**req).json()




