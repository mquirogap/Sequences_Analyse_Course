from sys import stdin
from collections import Counter

data= [x.replace("\n","").split("_") for x in stdin]
data= [["_".join(x[:-1]),x[-1]] for x in data]

AAlist= [x[0] for x in data]
#print(AAlist,"\n")

for AA in set(AAlist):
	
	print(AA+":")	
	AA_codons=[x[1] for x in data if x[0] == AA]
	#print(AA_codons)
	codon_ocurrence=Counter(AA_codons)
	codon_number=len(AA_codons)

	to_print=[]

	for codon in set(AA_codons):
		to_print.append((codon,codon_ocurrence[codon],codon_ocurrence[codon]/codon_number))


	to_print.sort(key=lambda x:x[1])


	for codon in to_print:
		print(" ",*codon,sep="\t")
	print("-----------------------------------------")
