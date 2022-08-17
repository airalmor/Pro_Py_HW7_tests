import unittest

from parameterized import parameterized

from yandex_make_dir import make_dir

class TestYaFoo(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp ===> Test START')

    def test_unitest_make_dir(self):
        foo_result = make_dir('unitest')
        self.assertEqual(foo_result.status_code, 201)

    def tearDown(self) -> None:
        print('tearDown ===> Test STOP')
