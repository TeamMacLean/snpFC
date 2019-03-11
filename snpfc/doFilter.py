import os, sys
from snpFilter import snpfilter

myfilter = snpfilter(sys.argv[1], sys.argv[2])
myfilter.filter()
