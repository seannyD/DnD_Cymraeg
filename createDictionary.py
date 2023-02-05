import os,json

def camel_case_split(str):
	words = [[str[0]]]
	for c in str[1:]:
		if words[-1][-1].islower() and c.isupper():
			words.append(list(c))
		else:
			words[-1].append(c)
	return [''.join(word) for word in words]
	
def clean(x):
	x = x.replace("(","").replace(")","").replace("*","").replace("#","").strip()
	x = x.title()
	return(x)
	
def includeWord(eng):
	if eng.lower() == "nodyn":
		return(False)
	if eng.lower().count("level")>0:
		return(False)
	if eng.startswith("Any"):
		return(False)
	if eng in ["And","Any"]:
		return(False)
	return(True)

seenEng = []
entries = []
for file in [x for x in os.listdir("translationTables/") if x.endswith("json")]:
	print(file)
	js = json.load(open("translationTables/"+file))
	cat = " ".join(camel_case_split(file.replace(".json",""))).title()
	for key in js:
		print(key)
		eng = clean(key)
		cym = js[key]
		if not type(cym) is dict:
			cym = clean(cym)
			if (not eng+cat in seenEng) and includeWord(eng):
				seenEng.append(eng+cat)
				entries.append({"English": eng, "Cymraeg":cym,"Category":cat})
			
with open('web/public/Geiriadur/geiriadur.json', 'w') as f:
    json.dump({"data":entries}, f)
