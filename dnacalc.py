#! /usr/bin/env python

# This program takes a DNA sequence and shows its length and the nucleotide composition

DNASeq = raw_input("Enter a DNA sequence: ")
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ","")
print 'Sequence:', DNASeq

SeqLength = float(len(DNASeq))
print 'Sequence Length:', int(SeqLength)

NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberG = DNASeq.count('G')
NumberC = DNASeq.count('C')

# Old way to output the Numbers, now removed
# print 'A:", NumberA/SeqLength

# Calculate percentage and out put to 1 decimal
print 'There are %d A base(s) out of %d (%.1f%%)' % (NumberA, SeqLength, 100*NumberA/SeqLength)
print 'There are %d T base(s) out of %d (%.1f%%)' % (NumberT, SeqLength, 100*NumberT/SeqLength)
print 'There are %d G base(s) out of %d (%.1f%%)' % (NumberG, SeqLength, 100*NumberG/SeqLength)
print 'There are %d C base(s) out of %d (%.1f%%)' % (NumberC, SeqLength, 100*NumberC/SeqLength)