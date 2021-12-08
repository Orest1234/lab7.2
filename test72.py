import unittest
import lab72 as code

class TestProgramm(unittest.TestCase):
    def test_calc(self):
        matrix_test = code.create((8,6))
        for i in range(len(matrix_test)):
            list1 = matrix_test[i + 1]
            list2 = sorted(list1)
            n_min = list2[0]
            n_max = list2[len(list2) - 1]
            index_min = list1.index(n_min)
            index_max = list1.index(n_max)
            list1[index_min] = n_max
            list1[index_max] = n_min
            matrix_test.update({i + 1: list1})
        return matrix_test
        matrix = code.create((8,6))
        matrix = code.change(matrix)
        
        self.assertEqual(matrix, matrix_test)