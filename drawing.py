  
from Bio import SeqIO
import pylab

sizes = [len(rec) for rec in SeqIO.parse("*.fasta", "fasta")]


pylab.hist(sizes, bins=20)
pylab.title(
"%i sequences\nLengths %i to %i" % (len(sizes), min(sizes), max(sizes))
)

pylab.xlabel("Sequence length (bp)")
pylab.ylabel("Count")
pylab.show()
