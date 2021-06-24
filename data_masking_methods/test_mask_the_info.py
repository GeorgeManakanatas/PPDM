# -*- coding: utf-8 -*-
'''
'''
import numpy as np
import pandas as pd
import unittest
from . import mask_the_info


class TestMaskingMethodSelection(unittest.TestCase):
    '''
    Test the function selects the masking method to be used
    '''

    def test_improper_method(self):
        '''
        Test providing an improper method
        '''
        df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.result = mask_the_info.masking_method_selection(df, [0],
                                                             'wrongMethod',
                                                             False,
                                                             'filename')
        self.assertFalse(self.result)

    def test_proper_method(self):
        '''
        Test providing an proper method
        '''
        df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.result = mask_the_info.masking_method_selection(df, [0],
                                                             'replace',
                                                             False,
                                                             'filename')
        self.assertTrue(isinstance(self.result, pd.DataFrame))


if __name__ == '__main__':
    unittest.main()

    