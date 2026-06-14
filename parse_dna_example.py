import os

from Bio import SeqIO

os.chdir(r"C:\Users\jibri\Desktop\bioinformatics-dna-toolkit")

for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
