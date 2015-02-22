__author__ = 'victor'

import unittest
from tests.store.controller.BSTControllerTestCase import BSTControllerTestCase


def suite():
    suites = unittest.TestSuite()
    suites.addTests(unittest.TestLoader().loadTestsFromTestCase(BSTControllerTestCase))
    return suites