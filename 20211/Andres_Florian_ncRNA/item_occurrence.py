from sys import stdin
from collections import Counter

data= ["_".join(x.replace("\n","").split("_")[:-1]) for x in stdin]
ocurrence_data=Counter(data)
item_number=len(data)

#print("item", "apariciones","proportion\n")

to_print=[]


for item in set(data):
	to_print.append((item,ocurrence_data[item],ocurrence_data[item]/item_number))
	#print(item+"\t"+str(ocurrence_data[item])+"\t"+str(ocurrence_data[item]/item_number))


to_print.sort(key=lambda x:x[1])


for item in to_print:
	print(*item,sep="\t")
