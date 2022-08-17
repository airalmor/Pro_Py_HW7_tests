import builtins
from src import *
import mock
import pytest
from parameterized import parameterized

fixture_check_document_existance = [('2207 876234', True),('1234', False)]
fixture_get_doc_owner_name = [('2207 876234', 'Василий Гупкин'),('1234',False)]
fixture_get_all_doc_owners_names = [('2207 876234,11-2,10006', {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'})]


@pytest.mark.parametrize('data,answer', fixture_check_document_existance)
def test_check_document_existance(data, answer):
    result = check_document_existance(data)
    assert result == answer


def test_get_doc_owner_name():
    with mock.patch.object(builtins, 'input', lambda _: '2207 876234'):
        result = get_doc_owner_name()
        assert result == 'Василий Гупкин'


@pytest.mark.parametrize('data,answer', fixture_get_all_doc_owners_names)
def test_get_all_doc_owners_names(data, answer):
    result = get_all_doc_owners_names()
    assert result == answer


def test_add_new_shelf():
    with mock.patch.object(builtins, 'input', lambda _: '10'):
        result = add_new_shelf()
        assert result == ('10',True)

