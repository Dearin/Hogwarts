from datetime import datetime

import pytest
from jsonpath import jsonpath

from Services.apis.tagApi import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    def tear_down(self):
        # 进行数据清理
        # 针对于新增的数据进行编辑操作等，用例结束后直接根据删除即可，达到数据清理的作用
        pass

    @pytest.mark.skip
    def test_token(self):
        self.tag.get_token()

    @pytest.mark.run(order=3)
    def test_get_corp_list(self):
       result = self.tag.get_corp_tag_list()
       print(result.json())


    @pytest.mark.run(order=1)
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

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("tag_id,tag_name", [
        ["etld41BgAAbzETHdaWvkGSZpIqwnEG-A", "tag1_new"],
        ["etld41BgAAbzETHdaWvkGSZpIqwnEG-A", "tag1_中文"],
        ["etld41BgAAbzETHdaWvkGSZpIqwnEG-A", "tag1[中文]"],
    ])
    def test_edit_corp_tag(self, tag_id, tag_name):
        self.tag.edit_corp_tag(tag_id, tag_name)
        # 返回的数据校验
        lists = self.tag.get_corp_tag_list()
        assert jsonpath(lists.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("group_name", ["New_Group"])
    def test_del_corp_tag(self, group_name):
        tag_id = self.tag.get_tag_id(group_name)
        print(tag_id)
        self.tag.del_corp_tag(tag_id)
        groups = self.tag.get_groups_names()
        assert group_name not in groups
