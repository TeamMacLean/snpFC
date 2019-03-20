import os
import vcf


class snpcompare():

	"class to compare SNPs from multiple VCFs"

	def __init__(self, vcffiles):

		self.vcffilenames = vcffiles
		self.snpsites = {}
		self.snp_positions = {}

	def record_all_snp_positions(self, chromosome, position):
		"""
			records all chromosome and positions in global variable (dictionary data structure) and initializes with an array of False boolean values for each vcf input file
			Each boolean value is a positional value of a snp in input vcf files in an array.
			E.g. if input vcf files are ["test1.vcf", "test2.vcf", "test3.vcf"]
			snpsites["chr1"]["1"] = [False, False, False]
			snpsites["chr1"]["10"] = [False, False, False]
			snpsites["chr2"]["1"] = [False, False, False]

			:type chromosome: string
			:param chromosome: name of the chromosome

			:type position: int
			:param position: position of SNP call in the chromosome

			return:
				None
		"""
		if  chromosome in self.snpsites.keys():
			if str(position) in self.snpsites[chromosome].keys():
				return
			else:
				self.snpsites[chromosome][str(position)] = [False] * len(self.vcffilenames)
		else:
			self.snpsites.update({chromosome:{str(position): [False] * len(self.vcffilenames) }})

	def record_all_snps(self, filename, chromosome, position, ref, alt):
		"""
			append the snp records to the dictionary data structure once they passed the filter

			:type filename: string
			:param filename: vcf filename

			:type chromosome: string
			:param chromosome: chromosome name on which SNP was call

			:type position: int
			:param position: base position in the chromosome

			:type ref: String
			:param ref: reference base in SNP call

			:type alt: String
			:param alt: alternate base in SNP call

			return:
				None

		"""

		if filename in self.snp_positions.keys():
			if chromosome in self.snp_positions[filename].keys():
				self.snp_positions[filename][chromosome].update({str(position):{"ref":ref, "alt":str(alt).replace("[","").replace("]", "").replace(" ", "")}} )
			else:
				self.snp_positions[filename].update({chromosome:{str(position):{"ref":ref, "alt":str(alt).replace("[","").replace("]", "").replace(" ", "")}}})
		else:
			self.snp_positions.update({filename:{chromosome:{str(position) : {"ref": ref, "alt":str(alt).replace("[","").replace("]", "").replace(" ", "")}}}})


	def get_snp_data(self):

		''' reads chromosome, position, reference and alternative columns for SNPs and store in dict data structure'''

		vcf_counter = 0
		for filename in  self.vcffilenames:
			vcf_reader=vcf.Reader(open(filename), "rb")
			samplename= vcf_reader.samples[0]
			for record in vcf_reader:
				chromosome, position, ref, alt = record.CHROM, record.POS, record.REF, record.ALT
				position=str(position)

				## code to build all snps position
				self.record_all_snp_positions(chromosome, position)

				self.record_all_snps(filename, chromosome, position, ref, alt)
				#self.snp_positions.update({str(vcf_counter) + "_" + chromosome + "_" + str(position):{"ref": str(ref), "alt":str(alt).replace("[","").replace("]", "")}})
				self.snpsites[chromosome][str(position)][vcf_counter] = True

			vcf_counter+=1

	def count_list_elements_occurrences(self, alt_bases):
		"""
			counts number of each element of input array

			:type alt_bases: Array
			:param alt_bases: alternate bases from all VCF files for same chromosome and position. e.g. ["A", "T", "A", "T,C"]

			return:
				array with count of each element in the input array. e.g for above array it retuns [2, 1, 2, 1]

		"""
		counts=[]
		for x in alt_bases:
			counts.append(alt_bases.count(x))
		return counts

	def get_unique_snps(self):
		""" records a unique snps in a vcf file """



		for chromosome in self.snpsites.keys():

			for position in self.snpsites[chromosome].keys():
				for filenumber in range(len(self.vcffilenames)):

					if self.snpsites[chromosome][position][filenumber] == True and sum(self.snpsites[chromosome][position]) == 1:  # First any(array) finds
						self.snp_positions[self.vcffilenames[filenumber]][chromosome][position].update({"unique":True})
					elif sum(self.snpsites[chromosome][position]) >=2:		# there might be snp at same position but with different alt base

						snp_index = [i for i, j in enumerate(self.snpsites[chromosome][position]) if j==True]

						totalindex = len(snp_index)
						# Lets check the alt base in these vcf files using index
						# lets get array of alt bases from each file
						alt_snps=[]
						for index in snp_index:
							alt_snps.append(self.snp_positions[self.vcffilenames[index]][chromosome][position]["alt"])

						# get the counts of the elements

						counts = self.count_list_elements_occurrences(alt_snps)

						for index in range(len(counts)):
							if counts[index] == 1:
								# this is unique, so occurred once
								self.snp_positions[self.vcffilenames[snp_index[index]]][chromosome][position].update({"unique":True}) # vcffilenames[snp_index[index]] =  this will be the filename
								#print("this is unique", vcffilenames[snp_index[index]], chromosome, position, self.snp_positions[vcffilenames[snp_index[index]]][chromosome][position])


					#else:
					#	vcf_database["self.snp_positions"][chromosome + "_" + position].update({"unique":False})


		return

	def get_common_snps(self):

		""" records SNPs common to all VCF input files """

		for chromosome in self.snpsites.keys():
			for position in self.snpsites[chromosome].keys():
				if all(self.snpsites[chromosome][position]) == True:
					#lets check if all alt bases are same
					alt_snps=[]
					for index in range(len(self.snpsites[chromosome][position])):
						alt_snps.append(self.snp_positions[self.vcffilenames[index]][chromosome][position]["alt"])

					counts = self.count_list_elements_occurrences(alt_snps)

					for countindex in range(len(counts)):
						if counts[countindex] == len(self.vcffilenames):
								self.snp_positions[self.vcffilenames[countindex]][chromosome][position].update({"common" : True})


	def compare(self, outdir, save=True, display=False):
		"""
			save the common/unique snps to files and/or display the results

			:type outdir: string
			:param outdir: output directory to save the output files

			:type save: boolean
			:param save: save the results to output files. Default True

			:type display: boolean
			:param display: display the results on the screen. Default False

			returns:
				None
		"""

		self.get_snp_data()
		self.get_unique_snps()
		self.get_common_snps()

		outfiles=[]
		for filename in self.vcffilenames:
			outfile=outdir + "/" + os.path.basename(filename).replace(".vcf", "") + "_snpcompare.txt"
			outfh=open(outfile, "w"); outfiles.append(outfile)
			if display == True:
				print("Common and Unique SNPS in vcf File : ", filename)
			else:
				print("Common and Unique SNPs from file ", filename , " are saved in :", outfile)
			for chromosome in self.snp_positions[filename].keys():
				for position in self.snp_positions[filename][chromosome].keys():
					if "common" in self.snp_positions[filename][chromosome][position].keys() and self.snp_positions[filename][chromosome][position]["common"] == True:
						if save == True:
							outfh.write(" ".join([chromosome,position, self.snp_positions[filename][chromosome][position]["ref"], self.snp_positions[filename][chromosome][position]["alt"], "common"]) + "\n")
						if display == True:
							print(" ".join([chromosome,position, self.snp_positions[filename][chromosome][position]["ref"], self.snp_positions[filename][chromosome][position]["alt"], "common"]))
					elif "unique" in self.snp_positions[filename][chromosome][position].keys() and self.snp_positions[filename][chromosome][position]["unique"] == True:
						if save == True:
							outfh.write(" ".join([chromosome,position, self.snp_positions[filename][chromosome][position]["ref"], self.snp_positions[filename][chromosome][position]["alt"], "unique"]) + "\n")
						if display == True:
							print(" ".join([chromosome, position, self.snp_positions[filename][chromosome][position]["ref"], self.snp_positions[filename][chromosome][position]["alt"], "unique"]))

			outfh.close()
		if display==True:
			print("The outputs are saved in these files :", " ".join(outfiles))

		return
