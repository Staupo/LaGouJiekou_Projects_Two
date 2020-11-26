# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 10:15 上午
# @Author  : Saber
# @FileName: test_access.py
# @Software: PyCharm

import re
import pytest
from LaGouJiekou_Projects.test_requests.api.access import Access
from LaGouJiekou_Projects.test_requests.api.WeChat import wechat

class TestACCESS:

    @pytest.fixture(scope="session")
    def token(self):
        yield wechat().test_get_token()

    def setup(self):
        self.access = Access()

    def create_muti_data(self):
        data = [("jin2324jin" + str(x), "wangyu", "155%09d" % x) for x in range(20)]
        return data

    def test_get(self, token):
        print(self.access.test_get("wangyu", token))

    def test_add(self, token):
        print(self.access.test_add_resion("xin12345xin", "wangmingyu", "18511000000", token))

    @pytest.mark.parametrize("userid, name, mobile", create_muti_data("xx"))
    def test_all(self, userid, name, mobile, token):
        try:
            # 创建一个成员, 对结果断言
            assert "created" == self.access.test_add_resion(userid, name, mobile, token)['errmsg']
        except AssertionError as e:
            if "userid existed" in e.__str__():
                self.access.test_delete(userid, token)
            if "mobile existed" in e.__str__():
                delete_userid = re.findall(":(.*)'$", e.__str__())
                self.access.test_delete(delete_userid, token)
            assert "created" == self.access.test_add_resion(userid, name, mobile, token)['errmsg']
        # 查询成员信息，对结果断言
        assert name == self.access.test_get(userid, token)['name']
        # 更新一个成员
        assert "updated" == self.access.test_update(userid, "wangmingyu", token)['errmsg']
        assert "wangmingyu" == self.access.test_get(userid, token)['name']
        # 删除
        assert "deleted" == self.access.test_delete(userid, token)['errmsg']
        assert 60111 == self.access.test_get(userid, token)['errcode']
