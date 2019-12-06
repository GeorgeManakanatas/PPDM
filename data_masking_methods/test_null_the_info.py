# -*- coding: utf-8 -*-
'''
'''
import numpy as np
import pandas as pd
import unittest
from . import null_the_info


class TestNullTheProperColumns(unittest.TestCase):
    '''
    Test the function that nulls specific columns in a dataset
    '''

    def test_null_one_column(self):
        '''
        Test nulling one column
        '''
        # create dataframe for the stesting and mull the first column
        df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11, 12]]))
        new_data_frame = null_the_info.null_the_proper_columns(df, [0])
        # get the coluumn apply set so there are no individual values
        # get the length and verify that it is 1
        self.result = set(new_data_frame[[0]])
        self.assertEqual(len(self.result), 1)

    def test_null_many_columns(self):
        '''
        Test nulling multiple columns
        '''
        # create dataframe for the stesting and mull the first and third column
        df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11, 12]]))
        new_data_frame = null_the_info.null_the_proper_columns(df, [0,2])
        # get the coluumn apply set so there are no individual values
        # get the length and verify that it is 1
        self.temp_result1 = len(set(new_data_frame[0]))
        self.temp_result2 = len(set(new_data_frame[2]))
        self.assertTrue((self.temp_result1==1) & (self.temp_result2==1))

if __name__ == '__main__':
    unittest.main()
