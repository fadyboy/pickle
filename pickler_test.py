import unittest
from pickler import list_pickler, unpickler
# declare a class for my pickle unit tests
class PickleTests(unittest.TestCase):

    # create a setUp method to always use the following components
    def setUp(self):
        # create a file object for writing to a file in binary
        self.file_obj = open('testfile', 'wb')

    # create a teardown method to close the open file object
    def tearDown(self):
        self.file_obj.close()

    # test that an object that is pickled and unpickled have the same data
    def pickle_unpickle_equal_test(self):

        my_list = [1, 2, "sherman Wosely"]
        list_pickler(my_list, self.file_obj)
        another_list = unpickler(self.file_obj)

        # check that my_list and another list are equal
        self.assertEqual(True, my_list == another_list)
