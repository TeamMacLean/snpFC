import os, sys
from snpCompare import Compare

mycompare = Compare(sys.argv[1:-1])
mycompare.compare(sys.argv[4])
