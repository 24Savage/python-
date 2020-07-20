import unittest
import random

from merge_sort import merge_sort

def setUpModule():
    print('Module %s up'%__name__)

def tearDownModule():
    print('Module %s down'%__name__)

class TestMergeSort(unittest.TestCase):
    '''
    unittest提供了丰富的断言,如assertEqual assertIs assertIsNot assertGreater assertIn等
    以及用例包裹方法
    '''
    def test_empty(self):
        self.assertEqual(merge_sort([]),[])

    def test_reverse_array(self):
        reverse_arr = [i for i in range(99,-1,-1)]
        self.assertEqual(merge_sort(reverse_arr), [i for i in range(100)])

    def test_random(self):
        test_arr = [random.randint(0,100) for _ in range(random.randint(0,100))]
        res_arr = merge_sort(test_arr)
        self.assertEqual(res_arr, sorted(test_arr))

    @classmethod
    def setUpClass(cls):
        print('Cls %s up'%str(cls))

    @classmethod
    def tearDownClass(cls):
        print('Cls %s down'%str(cls))

    def setUp(self):
        print('Method %s up'%str(self))
    
    def tearDown(self):
        print('Mothed %s down'%str(self))


if __name__ == '__main__':
    unittest.main()