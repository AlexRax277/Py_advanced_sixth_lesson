import unittest
from homework_2.main import YandexDisk


Token = ''
ya = YandexDisk(token=Token)


class TestCalculateUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    def setUp(self):
        print('setUp')

    def test_create_folder(self):
        print('test_create_folder')
        self.assertEqual(ya.create_folder(folder_name='test_API_ya'), 201)

    def test2_create_folder(self):
        print('test2_create_folder')
        self.assertEqual(ya.create_folder(folder_name='test_API_ya'), 201)

    def test3_create_folder(self):
        print('test3_create_folder')
        self.assertEqual(ya.create_folder(folder_name='test_API_ya'), 409)

    def test4_create_folder(self):
        print('test4_create_folder')
        self.assertEqual(ya.create_folder(folder_name='test_API_ya2'), 409)

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


if __name__ == '__main__':
    unittest.main()
