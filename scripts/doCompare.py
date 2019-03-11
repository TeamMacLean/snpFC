import os, sys
from snpCompare import Compare

mycompare= Compare(sys.argv[1], sys.argv[2], sys.argv[3])
mycompare.compare(sys.argv[4])
