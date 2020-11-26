# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 10:18 上午
# @Author  : Saber
# @FileName: access.py
# @Software: PyCharm


from LaGouJiekou_Projects.test_requests.api.base_api import BASEAPI

class Access(BASEAPI):

    def test_add_resion(self, userid, mobile, name, token, department=None):
        if department is None:
            department = [1]
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
            "json": {
                "userid": userid,
                "name": name,
                "mobile":mobile,
                "department": department
            }
        }
        r = self.send_api(data)
        return r

    def test_get(self, userid, token):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": token,
                "userid": userid
            }
        }
        r = self.send_api(data)
        return r

    def test_update(self, userid, token, name):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
            "json": {
                "userid": userid,
                "name": name
            }
        }
        r = self.send_api(data)
        return r


    def test_delete(self, userid, token):
        data = {
            "methon": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": token,
                "userid": userid
            }
        }
        r = self.send_api(data)
        return r

