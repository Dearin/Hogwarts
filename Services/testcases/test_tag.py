import json
from datetime import datetime

import pytest
from jsonpath import jsonpath

from Services.apis.tagApi import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    def teardown_class(self):
        # 一次操作下来遗留的数据只有：Hogwarts组下的tag_new标签和tag1更新后的数据
        lists = self.tag.get_corp_tag_list()
        group_id = jsonpath(lists.json(), '$.tag_group[?(@.group_name=="Hogwarts")]')[0]['group_id']
        self.tag.del_corp_group(group_id)

    def test_token(self):
        self.tag.get_token()

    @pytest.mark.run(order=1)
    def test_get_corp_list(self):
        result = self.tag.get_corp_tag_list()
        print(result.json())

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("group_name,tag_name",
                             [["Hogwarts", "tag1"], ["New_Group", "tag_new"]])
    def test_add_group_and_tag(self, group_name, tag_name):
        """
        新增标签组和组下的tag
        """
        # 获取添加前的标签组名
        pre_groups = self.tag.get_groups_names()
        print(pre_groups)
        # 针对添加的数据进行校验,若group不存在，则直接新增
        if group_name not in pre_groups:
            self.tag.add_corp_tag(group_name, tag_name)
            assert group_name in self.tag.get_groups_names()
            assert tag_name in self.tag.get_tags_name(group_name)
        else:
            tags = self.tag.get_tags_name(group_name)
            # 若group_name在添加前就存在，则判断新增的tag名称是否存在
            if tag_name in tags:
                # 若存在，则进行添加操作后，返回数据中tag_name是不会重复的。
                self.tag.add_corp_tag(group_name, tag_name)
                new_tags = self.tag.get_tags_name(group_name)
                assert len(tags) == len(new_tags)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("group_name,tag_name", [["Hogwarts", "tag2"]])
    def test_add_tag_name(self, group_name, tag_name):
        """在已存在的标签组下新增tag"""
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

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("group_name,tag_name", [["Hogwarts", "tag2"]])
    def test_add_tag_fail(self, group_name, tag_name):
        """重复添加1次标签和标签组"""
        pre_tags = self.tag.get_tags_name(group_name)
        self.tag.add_corp_tag(group_name, tag_name)
        new_tags = self.tag.get_tags_name(group_name)
        assert len(pre_tags) == len(new_tags)

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("tag_name", ["tag1_new", "tag1_中文", "tag1[中文]"])
    def test_edit_corp_tag(self, tag_name, group_name="Hogwarts"):
        tag_id = self.tag.get_tag_id_by_group_name(group_name)[0]
        print(f"tag_id是{tag_id}")
        res = self.tag.edit_corp_tag(tag_id, tag_name)
        print(res)
        # 返回的数据校验
        tags = self.tag.get_tags_name(group_name)
        print(tags)
        assert tag_name in tags

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize("group_name", ["New_Group"])
    def test_del_corp_tag(self, group_name):
        tag_id = self.tag.get_tag_id(group_name)
        print(tag_id)
        self.tag.del_corp_tag(tag_id)
        groups = self.tag.get_groups_names()
        assert group_name not in groups
