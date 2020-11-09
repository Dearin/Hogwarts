import yaml


class TestConfig:
    def test_conf(self):
        # 这样的话会需要去连接环境，为啥类？
        conf = yaml.safe_load(open('../yamls/conf.yml'))
        print(conf)