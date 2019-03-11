#!/usr/bin/env python3

import os, sys
import unittest, vcf

rootPath=os.path.dirname(os.path.abspath(sys.argv[0])) + "/.."
sourcePath=rootPath + "/scripts"
sys.path.append(sourcePath)

from snpCompare import Compare


class test_Compare(unittest.TestCase):

	test1 = rootPath + "/testfiles/test1.vcf"
	test2 = rootPath + "/testfiles/test2.vcf"
	test3 = rootPath + "/testfiles/test3.vcf"

	def test_compare(self):

		docompare = Compare([self.test1, self.test2, self.test3])


		self.assertEqual(docompare.compare(rootPath + "/testfiles"), None)



if __name__ == '__main__':
	unittest.main()
