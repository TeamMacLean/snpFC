from distutils.core import setup

setup(
    name='snpfc',
    version='0.1',
    packages=['snpfc',],
    license='Open Software License',
    long_description=open('README.md').read(),
	url="https://github.com/TeamMacLean/snpFC",
	author="Ram Krishna Shrestha",
	author_email="ram_krishna.shrestha@tsl.ac.uk",
	classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 0.0.1-beta',

        # Indicate who your project is intended for
        'Intended Audience :: Bioinformatics',
        'Topic :: SNP Filter and Compare :: SNP Analysis',

        # Pick your license as you wish
        'License :: Open Software License 3.0 :: osl-3.0',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
		],
	keywords='snp, filter, compare, vcf',
	python_requires='3.6+',
	install_requires=['pyvcf'],


)
