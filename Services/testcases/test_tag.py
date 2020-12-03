from datetime import datetime

import pytest
from jsonpath import jsonpath

from Services.apis.tagApi import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    def test_token(self):
        self.tag.get_token()

    def test_get_corp_list(self):
        self.tag.get_corp_tag_list()

    @pytest.mark.parametrize("group_name,tag_name", [
        ["Hogwarts", "tag_new"], ["New_Group", "tag1"], ["Hogwarts", "tag1"]
    ])
    def test_add_tag_name(self, group_name, tag_name):
        """
        新增tag标签的测试
        :param group_name: 指定标签组，如组名不存在则新增一组；若组名已存在则在该组下添加tag
        :param tag_name: 标签名称，同一标签组下tag_name不可以重复
        :return:
        """
        pre_lists = self.tag.get_corp_tag_list()
        pre_groups = jsonpath(pre_lists.json(), "$.tag_group..group_name")
        print(f"当前所有的组名为：{pre_groups}")
        pre_tags = []
        self.tag.add_corp_tag(group_name, tag_name)
        now_lists = self.tag.get_corp_tag_list()
        print(f"添加后的列表{now_lists.json()}")
        now_tags = jsonpath(now_lists.json(), '$.tag_group[?(@group_name=="Hogwarts")]')
        print(f"当前所有的tags是{now_tags}")
        # 针对添加的数据进行校验(成功和不成功)
        # 当group_name存在时：
