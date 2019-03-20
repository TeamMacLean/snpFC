import setuptools
from distutils.core import setup

setup(
    name='snpfc',
    version='0.2.4',
    packages=setuptools.find_packages(),
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
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        # Pick your license as you wish
        'License :: OSI Approved :: Python Software Foundation License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.

        'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.0',
		'Programming Language :: Python :: 3.1',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		],
	keywords='snp, filter, compare, vcf',
	python_requires='>=3',
	install_requires=['pyvcf'],


)
