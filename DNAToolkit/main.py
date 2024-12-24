from DNAToolkit import *

import random

Nucleotides=["A","C","G","T"]

randDNAstr="".join([random.choice(Nucleotides) for nuc in range(20)])


DNAstr=validateSeq(randDNAstr)
print(countNucFrequency(DNAstr))