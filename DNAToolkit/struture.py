
import collections
Nucleotides=["A","C","G","T"]
DNA_ReverseComplement={"A":"T","T":"A","G":"C","C":"G"}

def validateSeq(dna_seq):
    tmpseq=dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    tempfreqdict={"A":0,"C":0,"G":0,"T":0}
    for nuc in seq:
        tempfreqdict[nuc]+=1
    return tempfreqdict
    #return dict((collections.Counter(seq)))

#Transcription
def transcription(seq):
    return seq.replace("T","U")

#reverse complement
def reverse_complement(seq):
    return "".join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]