# 使用yaml来读取配置环境
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize('env', yaml.safe_load(open('env.yml')))
    def test_demo(self, env):
        if 'test' in env:
            print('这是测试环境')
            print(type(env))
            print('测试环境的ip地址：',env['test'])
        elif 'dev' in env:
            print('这是开发环境')
            print('测试环境的ip地址：',env['dev'])

    def test_yaml(self):
        print(yaml.safe_load(open('env.yml')))
