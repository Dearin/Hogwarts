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
        # 获取添加前的标签组名
        pre_groups = self.tag.get_groups_names()
        print(pre_groups)
        # 针对添加的数据进行校验
        if group_name in pre_groups:
            tags = self.tag.get_tags_name(group_name)
            # 若group_name在添加前就存在，则判断新增的tag名称是否存在
            if tag_name in tags:
                # 若存在，则进行添加操作后，返回数据中tag_name是不会重复的。
                self.tag.add_corp_tag(group_name, tag_name)
                new_tags = self.tag.get_tags_name(group_name)
                assert len(tags) == len(new_tags)

            else:
                # 若需新增的tag在已有组中不存在，则添加成功，返回数据中应有对应的tag
                self.tag.add_corp_tag(group_name, tag_name)
                new_tags = self.tag.get_tags_name(group_name)
                assert tag_name in new_tags
        # 当标签组名不存在时，则直接进行组和tag的新增
        else:
            self.tag.add_corp_tag(group_name, tag_name)
            assert group_name in self.tag.get_groups_names()
            assert tag_name in self.tag.get_tags_name(group_name)
