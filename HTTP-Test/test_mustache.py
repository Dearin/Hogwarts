import chevron


class TestMustache:

    def test_mustache(self):
        print(chevron.render('Hello,{{name}}', {'name': "World"}))

    def test_file_mustache(self):
        with open('test.mustache', 'r') as f:
            print(chevron.render(f, {'username': "Deerin",
                                     'password': "123456",
                                     'company': 'uxsino',
                                     'adj': 'asshole'
                                     }))

    def test_args(self):
        args = {
            'template': 'Hello, {{ mustache }}!',
            'data': {
                'mustache': 'World'
            }
        }
        print(chevron.render(**args))

    def test_partials_via_dict(self):
        args = {
            'template': 'Hello, {{> thing }}!',

            'partials_dict': {
                'thing': 'World'
            }
        }
        print(chevron.render(**args))

    def test_partials_via_file(self):
        args = {
            'template': 'Hello, {{> thing }}!',
            # defaults to .
            'partials_path': 'partials/',
            # defaults to mustache
            'partials_ext': 'txt',
        }
        # ./partials/thing.ms will be read and rendered
        print(chevron.render(**args))
        # Output: Hello, 在这里测试一下!



    def test_lambdas(self):
        '''暂时还没有搞懂这个'''
        def first(text, render):
            # return only first occurance of items
            result = render(text)
            return [x.strip() for x in result.split(" || ") if x.strip()][0]

        def inject_x(text, render):
            # inject data into scope
            return render(text, {'x': 'data'})

        args = {
            # {{#}}{{/}}的意思是以#号开始/结束表示区块，它会根据上下文的键值来对区块进行一次或者多次的渲染。
            'template': 'Hello, {{# first}} {{x}} || {{y}} || {{z}} {{/ first}}!  {{# inject_x}} {{x}} {{/ inject_x}}',

            'data': {
                'y': 'foo',
                'z': 'bar',
                'first': first,
                'inject_x': inject_x
            }
        }

        print(chevron.render(**args))