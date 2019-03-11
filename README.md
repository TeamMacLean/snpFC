## Introduction

snpFC - a python tool for filtering and comparing SNPs from multiple VCF files

## Requirement

1) python v3.6.1+
2) pyvcf

## Usage

1) python3 scripts/snpfc.py --vcf testfiles/test1.vcf testfiles/test2.vcf testfiles/test3.vcf --filter --outdir ./
2) python3 scripts/snpfc.py --vcf testfiles/test1.vcf testfiles/test2.vcf testfiles/test3.vcf --filter --compare --outdir ./
3) python3 scripts/snpfc.py --vcf testfiles/test1.vcf testfiles/test2.vcf testfiles/test3.vcf --filter --outdir ./ --genotype homozygous --frequency 80
4) python3 scripts/snpfc.py --vcf testfiles/test1.vcf testfiles/test2.vcf testfiles/test3.vcf --filter --outdir ./ --genotype_quality 20
