# -*- coding: utf-8 -*-
import unittest
from data_masking_methods import test_mask_the_info, test_null_the_info

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# will probably need a loop here
suite.addTests(loader.loadTestsFromModule(test_mask_the_info))
suite.addTests(loader.loadTestsFromModule(test_null_the_info))

runner = unittest.TextTestRunner(verbosity=3)
test_result = runner.run(suite)
print(test_result)
