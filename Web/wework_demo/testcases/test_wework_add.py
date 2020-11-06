import pytest

from Web.wework_demo.Pages.Main_Page import MainPage


class TestWeworkAdd:

    def setup(self):
        self.main = MainPage()

    @pytest.mark.parametrize("name, account, phonenum",
                             [('Hogwarts_041', 'Hogwarts_041', '13500000041')])
    def test_wework_add(self, name, account, phonenum):
        result = self.main.goto_MemberListAdd().goto_add_member().add_member(name, account, phonenum).get_member(name)
        print(result)
        assert name in result

    def test_get_member(self):
        name='Hogwarts_037'
        result = self.main.goto_MemberListAdd().get_member(name)
        print(result)