##############################################################################
#
# Copyright (c) 2008 Zope Corporation and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Test Products.CMFDefault.browser.folder

$Id$
"""

import unittest
from Testing import ZopeTestCase
from zope.testing import doctest

from Products.CMFDefault.testing import FunctionalLayer


utest_suite = doctest.DocFileSuite( 'folder_utest.txt'
                                  , optionflags=doctest.NORMALIZE_WHITESPACE
                                  )
ftest_suite = ZopeTestCase.FunctionalDocFileSuite('folder.txt')
ftest_suite.layer = FunctionalLayer

def test_suite():
    return unittest.TestSuite((
        utest_suite,
        ftest_suite,
    ))
