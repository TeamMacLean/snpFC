#!/usr/bin/env python3
import os, sys
import argparse
import vcf

rootPath=os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(rootPath)

from snpFilter import snpfilter
from snpCompare import snpcompare

parser=argparse.ArgumentParser(description="Script to filter the SNPs using user threshold values and compare the SNPs from multiple VCF files")

parser.add_argument("--vcf", action="store", dest="vcf", nargs="+", help="Space separated vcf input files")
parser.add_argument("--filter", action="store_true", dest="filter", default=False, help="Filter the SNPs")
parser.add_argument("--compare", action="store_true", dest="compare", default=False, help="Compare the SNPs")
parser.add_argument("--frequency", action="store", dest="frequency", default=70, type=int, help="Frequency of SNP call. Default: 70 [int]")
parser.add_argument("--pvalue", action="store", dest="pvalue", default=0.05, type=float, help="Pvalue of the SNP call. Default: 0.05 [float]" )
parser.add_argument("--genotype", action="store", dest="genotype", default="heterozygous", type=str, help="Genotype of the SNP call - heterozygous/homozygous/both. Default: heterozygous")
parser.add_argument("--quality", action="store", dest="genotype_quality", default=10, type=int, help="Genotype quality of the SNP call. Default: 10")
parser.add_argument("--rawreaddepth", action="store", dest="raw_read_depth", default=5, type=int, help="Raw read depth of the SNP call. Default: 5")
parser.add_argument("--qualityreaddepth", action="store", dest="quality_read_depth", default=5, type=int, help="Quality read depth of the SNP call. Default: 5")
parser.add_argument("--depthreference", action="store", dest="depth_in_reference", default=5, type=int, help="Depth in reference of the SNP call. Default: 5")
parser.add_argument("--depthvariant", action="store", dest="depth_in_variant", default=5, type=int, help="Depth in variant of the SNP call. Default: 5")
parser.add_argument("--show", action="store_true", dest="display", default=False, help="Display the results on the screen")
parser.add_argument("--outdir", action="store", dest="outdir", default=os.path.abspath("."), help="Path to the output folder. Default: Current working directory")

options=parser.parse_args()


if  __name__ == "__main__":


	options=parser.parse_args()
	if not options.vcf:
		print("Input VCF file/s not provided. Use option --vcf to provde the input VCF files (mutliple vcf files should be space separated)")
		exit(1)
	if len(options.vcf) ==1 and options.compare == True:
		print("Number of VCF files provided : ", len(options.vcf))
		print("SNP compare will not be done.")
		options.compare=False



	vcffilenames  = options.vcf
	print("VCF files provided ", vcffilenames)
	if options.filter == True:
		filtered_files = []
		for vcffilename in options.vcf:
			outfilename = options.outdir + "/filter_"  + os.path.basename(os.path.abspath(vcffilename))
			doFilter = snpfilter(vcffilename, outfilename)
			doFilter.filter()
			filtered_files.append(outfilename)
			#print("VCF filtering done for ", vcffilename, " Filtered output vcf file is ", outfilename)

	if options.compare == True and options.filter == True:
		print("Filter :", True, ", Compare: ", True)
		print("Files to compare ", filtered_files)
		doCompare = snpcompare(filtered_files)
		doCompare.compare(options.outdir)
	elif options.compare == True:
		print("Filter :", False, ", Compare: ", True)
		print("Files to compare ", options.vcf)
		doCompare = snpcompare(options.vcf)
		doCompare.compare(options.outdir)
	else:
		pass


	#print("SNPs comparison completed. Files are output in ", options.outdir)

	exit(0)
