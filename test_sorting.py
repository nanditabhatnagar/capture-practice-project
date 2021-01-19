import unittest
from main import sort_files

class TestSorting(unittest.TestCase):

    def test_sort_by_file_count(self):
        barcodeList = ['1','2','3','4','5']
        file_count = [10,9,8,7,6]
        sortedFileList = sort_files(barcodeList, 1)
        expected = ['5','4','3','2','1']
        self.assertIsInstance(sortedFileList, tuple)
        self.assertEqual(sortedFileList, expected)
 
    def test_sort_by_file_count2(self):
        barcodeList = ['1','2','3','4','5']
        file_count = [100,19,58,78,16]
        sortedFileList = sort_files(barcodeList, file_count)
        expected = ['5','2','3','4','1']
        self.assertIsInstance(sortedFileList, tuple)
        self.assertEqual(sortedFileList, expected)
 
    def test_sort_by_file_count3(self):
        barcodeList = ['1','2','3','4','5']
        file_count = [10,9,8,7,6]
        sortedFileList = sort_files(barcodeList, file_count)
        expected = ['5','4','3','2','1']
        self.assertIsInstance(sortedFileList, tuple)
        self.assertEqual(sortedFileList, expected)

if __name__ == '__main__':
    unittest.main()
