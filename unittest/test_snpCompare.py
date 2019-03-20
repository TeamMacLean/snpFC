#!/usr/bin/env python3

import os, sys
import unittest, vcf

rootPath=os.path.dirname(os.path.abspath(sys.argv[0])) + "/.."
sourcePath=rootPath + "/snpfc"
sys.path.append(sourcePath)

from snpCompare import snpcompare


class test_Compare(unittest.TestCase):

	test1 = rootPath + "/testfiles/unittest1.vcf"
	test2 = rootPath + "/testfiles/unittest2.vcf"
	docompare = snpcompare([test1, test2])

	def test_record_all_snp_positions(self):
		self.docompare.record_all_snp_positions('chr1', 100)
		self.assertEqual(self.docompare.snpsites, {'chr1': {'775': [True, True], '776': [False, True], '100': [False, False]}})

	def test_record_all_snps(self):
		self.docompare.record_all_snps(self.test1, 'chr1', 100, 'A', 'G')
		self.assertIn('100', list(self.docompare.snp_positions[self.test1]['chr1'].keys()))

	def test_get_snp_data(self):
		self.assertEqual(self.docompare.get_snp_data(), None)
	def test_count_list_elements_occurrences(self):
		self.assertEqual(self.docompare.count_list_elements_occurrences(['A', 'T','A','C','G', 'G']), [2,1,2,1,2,2])
	def test_get_unique_snps(self):
		self.docompare.get_snp_data()
		self.docompare.get_unique_snps()
		self.assertEqual(self.docompare.snp_positions, {
				self.test1: {'chr1': {'775': {'ref': 'A', 'alt': 'G'}}},
				self.test2: {'chr1': {'775': {'ref':'A', 'alt':'G'},  '776': {'ref': 'T', 'alt': 'C', 'unique':True} } }
				}  )
	def test_get_common_snps(self):
		self.docompare.get_snp_data()
		self.docompare.get_common_snps()
		self.assertDictEqual(self.docompare.snp_positions, {
				self.test1: {'chr1': {'775': {'ref': 'A', 'alt': 'G', 'common':True}}},
				self.test2: {'chr1': {'775': {'ref':'A', 'alt':'G', 'common':True},  '776': {'ref': 'T', 'alt': 'C'} } }
				})


	#
	# def test_compare(self):
	#
	# 	docompare = Compare([self.test1, self.test2, self.test3])
	#
	#
	# 	self.assertEqual(docompare.compare(rootPath + "/testfiles"), None)



if __name__ == '__main__':
	unittest.main()
