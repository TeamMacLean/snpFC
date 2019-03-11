#!/usr/bin/env python3

## unittest for filter_vcf.py functions

import os, sys
import unittest, vcf

rootPath=os.path.dirname(os.path.abspath(sys.argv[0])) + "/.."
sourcePath=rootPath + "/scripts"
sys.path.append(sourcePath)

from snpFilter import snpfilter


class test_snpfilter(unittest.TestCase):

	''' class to test snpfilter '''
	testfile = rootPath + "/testfiles/test1.vcf"
	outfile = rootPath + "/testfiles/test_test1_filtered.vcf"

	dofilter = snpfilter(testfile, outfile)
	vcf_reader = vcf.Reader(open(testfile), 'r')
	record = next(vcf_reader)
	sample = vcf_reader.samples[0]

	def test_snpfilter(self):
		" test initialization of snpfilter class"


		self.assertEqual(self.dofilter.pvalue , 0.05)
		self.assertEqual(self.dofilter.genotype, 'any')
		self.assertEqual(self.dofilter.genotype_quality, 20)
		self.assertEqual(self.dofilter.raw_read_depth, 5)
		self.assertEqual(self.dofilter.quality_read_depth, 5)
		self.assertEqual(self.dofilter.depth_in_reference,5)
		self.assertEqual(self.dofilter.depth_in_variant,5)



	def test_get_record_calldata(self):
		print(self.dofilter.get_record_calldata(self.record))

	def test_filter(self):

		" test filter function "
		self.assertEqual(self.dofilter.filter(), None)








if __name__ == '__main__':
	unittest.main()
