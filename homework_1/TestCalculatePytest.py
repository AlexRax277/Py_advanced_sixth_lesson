import unittest
import pytest
from homework_1.source import documents, directories, check_document_existance, get_doc_owner_name, \
     get_all_doc_owners_names, show_all_docs_info, get_doc_shelf, add_new_shelf, add_new_doc, delete_doc, \
     move_doc_to_shelf
from unittest import mock


class TestCalculatePytest:

    @classmethod
    def setup_class(cls):
        print('setup_class')

    def setup(self):
        print('setup')

    @pytest.mark.parametrize('doc_number', [doc['number'] for doc in documents])
    def test_check_document_existance(self, doc_number):
        assert check_document_existance(doc_number) is True

    def test_get_doc_owner_name(self):
        with unittest.mock.patch('builtins.input', return_value='2207 876234'):
            assert get_doc_owner_name() == 'Василий Гупкин'

    def test_get_all_doc_owners_names(self):
        assert get_all_doc_owners_names() == set([doc['name'] for doc in documents])

    def test_show_all_docs_info(self):
        def foo(data):
            for doc in data:
                print(' '.join(list(doc.values())))
        assert show_all_docs_info() == foo(documents)

    def test_get_doc_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='11-2'):
            assert get_doc_shelf() == '1'

    @pytest.mark.parametrize('shelf_number, result', [
        ('1', False),
        ('2', False),
        ('3', False),
        ('4', '4'),
        ('5', '5')
    ])
    def test_add_new_shelf(self, shelf_number, result):
        assert add_new_shelf(shelf_number) == result

    def test_add_new_doc(self):
        assert add_new_doc('12', 'pass', 'Tom', '2') == print(documents, directories)

    def test_delete_doc(self):
        with unittest.mock.patch('builtins.input', return_value="11-2"):
            assert delete_doc() == ("11-2", True)

    def test_move_doc_to_shelf(self):
        assert move_doc_to_shelf("11-2", "2") == print('Документ номер "11-2" был перемещен на полку номер "2"')

    def teardown(self):
        print('teardown')

    def teardown_class(cls):
        print('teardown_class')
