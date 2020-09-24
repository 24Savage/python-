import unittest
from html_test_report import HTMLTestRunner
from test_mergesort import TestMergeSort
'''
生成HTML报告文档
'''

suite = unittest.makeSuite(TestMergeSort)
f = open(r"C:\Users\jiao\desktop\report.html", 'wb')
HTMLTestRunner(stream=f,title="mergeSort Test",description="test").run(suite)
f.close()