import os,re
from operator import itemgetter, attrgetter

words= {}

sizes = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]


folder = "DND.SRD.Wiki-0.5.1/Treasure/"
files = os.listdir(folder)
files = [x for x in files if x.endswith(".md")]
for f in files:
	filepath = os.path.join(folder,f)
	o = open(filepath)
	t = o.read()
	o.close()
	t = re.sub("[\\.,;:\\?!\"]"," ",t)
	lines = t.split("\n")
	#lines = [line for line in lines if any([line.startswith("*"+x) for x in sizes])]
	#lines = [line for line in lines if line.count("any")>0]
	#lines = [line for line in lines if line.count("**Languages")>0]
	#lines = [line[:line.rindex("*")] for line in lines if line.startswith("*")]
	#lines = [line for line in lines if line.count("**Duration")]
	lines = [line for line in lines if line.startswith("*")]
	t = " ".join(lines)
	t = [x for x in t.split(" ") if len(x.strip())>0]
	for w in t:
		try:
			words[w] += 1
		except:
			words[w] = 1
				

words2 = sorted([x for x in words.items()], key=itemgetter(1))

for word in words2:
	print(word)