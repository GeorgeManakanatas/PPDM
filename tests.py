# -*- coding: utf-8 -*-
import unittest
from data_masking_methods import test_mask_the_info, test_null_the_info

# create loader and suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()
# will probably need a loop here after a wile
suite.addTests(loader.loadTestsFromModule(test_mask_the_info))
suite.addTests(loader.loadTestsFromModule(test_null_the_info))
# set runner and run tests
runner = unittest.TextTestRunner(verbosity=3)
test_result = runner.run(suite)
