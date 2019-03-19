import vcf


class snpfilter():
	'''	A class for filtering SNPs with threshold values in VCF files	'''
	def __init__(self, vcffilename, vcfoutfile, frequency=70, pvalue=0.05, genotype='any', genotype_quality=20, raw_read_depth=5, quality_read_depth=5, depth_in_reference=5, depth_in_variant=5):
		"""
		Initializes the filter threshold values
		"""
		self.vcffilename = vcffilename
		self.vcfoutfile = vcfoutfile
		self.frequency=frequency
		self.pvalue=pvalue
		self.genotype=genotype
		self.genotype_quality=genotype_quality
		self.raw_read_depth=raw_read_depth
		self.quality_read_depth=quality_read_depth
		self.depth_in_reference=depth_in_reference
		self.depth_in_variant=depth_in_variant

	def open_vcf(self):
		self.vcf_reader = vcf.Reader(filename=self.vcffilename)

	def write_vcf(self):
		self.vcf_writer = vcf.Writer(open(self.vcfoutfile, 'w'), self.vcf_reader)

	def write_snp_records(self, record):
		self.vcf_writer.write_record(record)

	def get_samplename(self):
		""" returns the samplename of the snp record """
		return self.vcf_reader.samples[0]

	def get_frequency(self, record, sample):
		'return frequency of SNP genotype'
		call = record.genotype(sample)
		return float(call.data.FREQ.replace('%', ''))

	def get_pvalue(self,record, sample):
		'return pvalue of a SNP record'
		call = record.genotype(sample)
		return call.data.PVAL
	def get_genotype(self,record, sample):
		'return the genotype of a snp record - heterozygous or homozygous'
		call=record.genotype(sample)
		genotype=call.data.GT
		array=genotype.split('/')
		if array[0] == array[1]:
			return 'homozygous'
		else:
			return 'heterozygous'

	def get_quality_read_depth(self,record, sample):
		'return the quality read depth for snp record'
		call=record.genotype(sample)
		return int(call.data.DP)
	def get_genotype_quality(self, record, sample):
		'return genotype quality'
		call=record.genotype(sample)
		return int(call.data.GQ)
	def get_raw_read_depth(self, record, sample):
		""" returns raw read depth of the snp record"""
		call=record.genotype(sample)
		return int(call.data.SDP)
	def get_depth_in_reference(self, record, sample):
		""" returns depth in reference data for the snp record"""
		call=record.genotype(sample)
		return int(call.data.RD)
	def get_depth_in_variant(self, record, sample):
		""" returns depth in variant data for the snp record """
		call=record.genotype(sample)
		return int(call.data.AD)
	def check_threshold_value(self, recordvalue, testvalue):
		""" function to test snp record value to threshold value
		args:
		recordvalue - value in a snp record
		testvalue - threshold value to test

		returns:
		True - if condition is True
		False - if condition is False
		"""

		if recordvalue >= testvalue:
			return True
		else:
			return False

	def check_frequency(self,record, sample, testvalue):
		""" function to check frequency of a base in snp call"""

		return self.check_threshold_value(self.get_frequency(record,sample), testvalue)
	def check_pvalue(self, record, sample,testvalue):
		""" function to check pvalue of alt base call in a snp call"""
		record_pvalue=float(self.get_pvalue(record, sample))
		if record_pvalue <= float(testvalue):
			return True
		else:
			return False
		#return (not self.check_threshold_value(float(self.get_pvalue(record, sample)), np.float32(testvalue)))		# here we are testing pvalue less or equal to, so we have to return the opposite result
	def check_genotype(self,record, sample, testvalue):
		""" function to check genotype of alt base in the snp call"""
		#return self.check_threshold_value(self.get_genotype(record, sample), testvalue)
		if self.genotype == 'any':
			return True
		elif self.get_genotype(record, sample) == testvalue:
			return True
	def check_genotype_quality(self,record, sample,testvalue):
		""" function to check genotype quality of alt base in the snp call"""
		return self.check_threshold_value(self.get_genotype_quality(record, sample), testvalue)
	def check_quality_read_depth(self, record, sample,testvalue):
		""" function to call read depth quality of alt base in the snp call"""
		return self.check_threshold_value(self.get_quality_read_depth(record, sample), testvalue)
	def check_raw_read_depth(self,record, sample,testvalue):
		""" function to check raw read depth of alt base in the snp call"""
		return self.check_threshold_value(self.get_raw_read_depth(record,sample), testvalue)
	def check_depth_in_reference(self,record, sample,testvalue):
		""" function to check dpeth in reference for alt base call in the snp call"""
		return self.check_threshold_value(self.get_depth_in_reference(record, sample), testvalue)
	def check_depth_in_variant(self,record, sample,testvalue):
		""" function to check depth in variant for alt base in the snp call"""
		return self.check_threshold_value(self.get_depth_in_variant(record, sample), testvalue)


	def passed_filter(self, record, samplename):
		"""
		function to test if a snp record passed the filter or not
		args:
			record - pyVCF SNP record object
			samplename - samplename in the SNP record

		"""
		results=[
				self.check_frequency(record, samplename, self.frequency),
				self.check_pvalue(record, samplename, self.pvalue),
				self.check_genotype(record,samplename, self.genotype),
				self.check_genotype_quality(record,samplename, self.genotype_quality),
				self.check_quality_read_depth(record, samplename, self.quality_read_depth),
				self.check_raw_read_depth(record,samplename, self.raw_read_depth),
				self.check_depth_in_reference(record, samplename, self.depth_in_reference),
				self.check_depth_in_variant(record, samplename, self.depth_in_variant)
				]

		if all(results):      # also can be used if results.count(True) == 8
			return True
		else:
			return False

	def filter(self):
		"""
			function to filter all SNP records from a VCF file
		"""
		self.open_vcf()
		self.write_vcf()
		samplename=self.get_samplename()
		for record in self.vcf_reader:
			if self.passed_filter(record, samplename) == True:
				self.write_snp_records(record)
		self.vcf_writer.close()
		return
