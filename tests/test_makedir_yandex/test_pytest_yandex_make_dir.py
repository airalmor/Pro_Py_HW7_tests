import pytest
from yandex_make_dir import make_dir
from parameterized import parameterized

fixture = [('pytest_yandex_make_dir', 201)]

@pytest.mark.parametrize('dir_name,code',fixture)
def test_make_dir(dir_name, code):
    result = make_dir(dir_name)
    assert code == result.status_code
