#!/usr/bin/env python3

## unittest for filter_vcf.py functions

import os, sys
import unittest, vcf

rootPath=os.path.dirname(os.path.abspath(sys.argv[0])) + "/.."
sourcePath=rootPath + "/snpfc"
sys.path.append(sourcePath)

from snpFilter import SnpFilter


class test_snpfilter(unittest.TestCase):

	''' class to test snpfilter '''
	testfile = rootPath + "/testfiles/test1.vcf"
	outfile = rootPath + "/testfiles/test_test1_filtered.vcf"

	dofilter = SnpFilter(testfile, outfile)

	def test_open_vcf(self):
		self.assertEqual(self.dofilter._open_vcf(), None)
	def test_write_vcf(self):
		self.assertEqual(self.dofilter._write_vcf(), None)
	def test_get_samplename(self):
		self.dofilter._open_vcf()
		self.assertEqual(self.dofilter.get_samplename(), 'Sample1')
	def test_values(self):
		self.dofilter._open_vcf()
		record=next(self.dofilter.vcf_reader)
		sample=self.dofilter.vcf_reader.samples[0]
		self.assertEqual(self.dofilter.get_frequency(record, sample), 75)
		self.assertEqual(float(self.dofilter.get_pvalue(record, sample)), 0.0034965)
		self.assertEqual(self.dofilter.get_genotype(record, sample), 'homozygous')
		self.assertEqual(self.dofilter.get_quality_read_depth(record, sample), 8)
		self.assertEqual(self.dofilter.get_genotype_quality(record, sample), 24)
		self.assertEqual(self.dofilter.get_raw_read_depth(record, sample), 8)
		self.assertEqual(self.dofilter.get_depth_in_reference(record, sample), 20)
		self.assertEqual(self.dofilter.get_depth_in_variant(record, sample), 6)

	def test_check_threshold_value(self):
		self.assertTrue(self.dofilter.check_threshold_value(10, 1))
	def test_check_frequency(self):
		self.dofilter._open_vcf()
		record=next(self.dofilter.vcf_reader)
		sample=self.dofilter.vcf_reader.samples[0]
		self.assertTrue(self.dofilter.check_frequency(record, sample, 75))
		self.assertTrue(self.dofilter.check_pvalue(record, sample, 0.0034965))
		self.assertTrue(self.dofilter.check_genotype(record, sample, 'homozygous'))
		self.assertTrue(self.dofilter.check_genotype_quality(record, sample, 24))
		self.assertTrue(self.dofilter.check_quality_read_depth(record, sample, 8))
		self.assertTrue(self.dofilter.check_raw_read_depth(record, sample, 8))
		self.assertTrue(self.dofilter.check_depth_in_reference(record,sample, 20))
		self.assertTrue(self.dofilter.check_depth_in_variant(record, sample, 6))

	# vcf_reader = vcf.Reader(open(testfile), 'r')
	# record = next(vcf_reader)
	# sample = vcf_reader.samples[0]
	#
	# def test_snpfilter(self):
	# 	" test initialization of snpfilter class"
	#
	#
	# 	self.assertEqual(self.dofilter.pvalue , 0.05)
	# 	self.assertEqual(self.dofilter.genotype, 'any')
	# 	self.assertEqual(self.dofilter.genotype_quality, 20)
	# 	self.assertEqual(self.dofilter.raw_read_depth, 5)
	# 	self.assertEqual(self.dofilter.quality_read_depth, 5)
	# 	self.assertEqual(self.dofilter.depth_in_reference,5)
	# 	self.assertEqual(self.dofilter.depth_in_variant,5)
	#
	#
	#
	# def test_get_record_calldata(self):
	# 	print(self.dofilter.get_record_calldata(self.record))
	#
	# def test_filter(self):
	#
	# 	" test filter function "
	# 	self.assertEqual(self.dofilter.filter(), None)








if __name__ == '__main__':
	unittest.main()
