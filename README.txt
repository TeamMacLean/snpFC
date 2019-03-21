Introduction

snpFC - a python tool for filtering and comparing SNPs from multiple VCF files

Requirement

1) python v3.0+
2) pyvcf

Command line Usage

1) snpfc.py --help

	usage: snpfc.py [-h] [--vcf VCF [VCF ...]] [--filter] [--compare]
	                [--frequency FREQUENCY] [--pvalue PVALUE]
	                [--genotype GENOTYPE] [--quality GENOTYPE_QUALITY]
	                [--rawreaddepth RAW_READ_DEPTH]
	                [--qualityreaddepth QUALITY_READ_DEPTH]
	                [--depthreference DEPTH_IN_REFERENCE]
	                [--depthvariant DEPTH_IN_VARIANT] [--show] [--outdir OUTDIR]

	Script to filter the SNPs using user threshold values and compare the SNPs
	from multiple VCF files

	optional arguments:
	  -h, --help            show this help message and exit
	  --vcf VCF [VCF ...]   Space separated vcf input files
	  --filter              Filter the SNPs
	  --compare             Compare the SNPs
	  --frequency FREQUENCY
	                        Frequency of SNP call. Default: 70 [int]
	  --pvalue PVALUE       Pvalue of the SNP call. Default: 0.05 [float]
	  --genotype GENOTYPE   Genotype of the SNP call -
	                        heterozygous/homozygous/both. Default: heterozygous
	  --quality GENOTYPE_QUALITY
	                        Genotype quality of the SNP call. Default: 10
	  --rawreaddepth RAW_READ_DEPTH
	                        Raw read depth of the SNP call. Default: 5
	  --qualityreaddepth QUALITY_READ_DEPTH
	                        Quality read depth of the SNP call. Default: 5
	  --depthreference DEPTH_IN_REFERENCE
	                        Depth in reference of the SNP call. Default: 5
	  --depthvariant DEPTH_IN_VARIANT
	                        Depth in variant of the SNP call. Default: 5
	  --show                Display the results on the screen
	  --outdir OUTDIR       Path to the output folder. Default: Current working
                        directory


2) python3 scripts/snpfc.py --vcf testfiles/test1.vcf testfiles/test2.vcf testfiles/test3.vcf --filter --outdir ./
3) python3 scripts/snpfc.py --vcf testfiles/test1.vcf testfiles/test2.vcf testfiles/test3.vcf --filter --compare --outdir ./
4) python3 scripts/snpfc.py --vcf testfiles/test1.vcf testfiles/test2.vcf testfiles/test3.vcf --filter --outdir ./ --genotype homozygous --frequency 80
5) python3 scripts/snpfc.py --vcf testfiles/test1.vcf testfiles/test2.vcf testfiles/test3.vcf --filter --outdir ./ --genotype_quality 20

Usage as python module


import snpfc
from snpfc.snpFilter import snpfilter
dofilter = snpfilter(input.vcf, output.vcf, frequency=70, pvalue=0.05, genotype='any', genotype_quality=20, raw_read_depth=5, quality_read_depth=5, depth_in_reference=5, depth_in_variant=5)
dofilter.filter()

This will filter the SNPs and save in output.vcf file.


from snpCompare import snpcompare
docompare = snpcompare(input1.vcf, input2.vcf, input3.vcf)
docompare.compare()


This will compare the SNPs in the input files and save the output in the files - input1_snpcompare.txt, input2_snpcompare.txt and input3_snpcompare.txt in the current working directory.

docompare.compare(output_directory)

This will save the output files in the output directory specified.
