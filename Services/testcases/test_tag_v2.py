import json

import pytest
from jsonpath import jsonpath

from Services.apis.tagApi import Tag


class TestTagV2:
    """
    实战课程后，对用例进行完善
    todo: 封装底层方法
    todo: 参数化
    """

    def setup_class(self):
        self.tag = Tag()

    #
    # def teardown(self):
    #     group_id = self.tag.get_group_id_by_name("Hogwarts")
    #     self.tag.delete_n_detect([group_id])

    def test_get_tag_id(self):
        group_name = "Hogwarts"
        tag_name = [{
            "name": "Tag_001"
        }]
        self.tag.add_corp_tag(group_name, tag_name)
        tag_id = self.tag.get_tag_id_by_name(group_name, tag_name="Tag_001")
        assert tag_id is not None

    @pytest.mark.skip
    def test_token(self):
        self.tag.get_token()

    @pytest.mark.skip
    def test_is_exist(self):
        group_id = self.tag.get_group_id_by_name("Tes")
        res = self.tag.is_group_id_exist(group_id)
        print(res)

    # 单个接口的基础测试用例 - 修改新增方法参数后需要同步修改传承
    # @pytest.mark.parametrize("group_name,tag_name",
    #                          [["Hogwarts", "tag1"]])
    def test_add(self):
        """测试基础新增"""
        group_name = "Hogwarts"
        tag_name = [{
            "name": "Tag_001"
        }]
        self.tag.add_corp_tag(group_name, tag_name)
        assert group_name in self.tag.get_groups_names()
        assert tag_name[0]["name"] in self.tag.get_tags_name(group_name)

    # @pytest.mark.skip
    def test_get_corp_list(self):
        """获取标签列表"""
        result = self.tag.get_corp_tag_list()
        print(json.dumps(result.json(), indent=2, ensure_ascii=False))

    @pytest.mark.parametrize("name", ["tag1_new", "tag1_中文", "tag1[中文]"])
    def test_edit_corp_tag(self, name, group_name="Hogwarts"):
        """修改标签"""
        # 先新增一个标签组
        tag_name = [{
            "name": f"{name}"
        }]
        self.tag.add_corp_tag(group_name, tag_name)
        # 获取标签id进行修改
        tag_id = self.tag.get_ids_by_group_name(group_name)
        print(f"tag_id是{tag_id}")
        res = self.tag.edit_corp_tag(tag_id, tag_name)
        # 数据校验
        tags = self.tag.get_tags_name(group_name)
        print(tags)
        assert tag_name[0]['name'] in tags

    # @pytest.mark.parametrize("tag_name,tag_name1", [["Tag_001", "Tag_002"]])
    def test_del_corp_tag(self):
        """
        删除某一标签组下的标签：
        1、新增一标签组及标签
        2、删除该标签组下的某一标签
        3、判断该组下该标签是否存在
        """
        group_name = "Hogwarts"
        tag_name = [{"name": "Tag_001"}, {"name": "Tag_002"}]
        self.tag.add_n_detect(group_name, tag_name)
        # 获取tags
        tags = self.tag.get_tags_by_group_name(group_name)
        tag_id = tags['Tag_001']
        # 删除tags
        self.tag.del_corp_tag(tag_id)
        # 进行验证
        tags_now = self.tag.get_tags_by_group_name(group_name)
        print(f"==========tags====={tags_now}")

    @pytest.mark.parametrize("group_name", ["Hogwarts"])
    def test_del_corp_group(self, group_name):
        # 新增一标签组及对应标签
        self.tag.add_n_detect(group_name, tag_name=[
            {"name": "TAG1"},
            {"name": "TAG2"},
            {"name": "TAG3"},
        ])
        group_ids = self.tag.get_group_id_by_name(group_name)
        # 删除标签组
        self.tag.delete_n_detect([group_ids])
        groups = self.tag.get_groups_names()
        assert group_name not in groups
