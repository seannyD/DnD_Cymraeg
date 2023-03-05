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
	x = x.replace("*","").replace("#","").replace(":","").strip()
	if x.count("(")==0 or x.count(")")==0:
		x = x.replace("(","").replace(")","")
	if x.startswith("(") and x.endswith(")"):
		x = x[1:-1]
	x = x.title()
	if x=="Dc":
		x = "DC"
	if x=="AC":
		x = "AC"
	if x == "Hp":
		x = "HP"
	x = x.replace("Npc","NPC")
	return(x)
	
def includeWord(eng):
	if eng.lower() == "nodyn":
		return(False)
	if eng.lower().count("level")>0:
		return(False)
	if eng.startswith("Any"):
		return(False)
	if eng in ["And","Any","Armor Class Alt","Hp_Alt","Ranger Alt","Constitution_Alt"]:
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
				cat = cat.replace("Race","Species")
				entries.append({"English": eng, "Cymraeg":cym,"Category":cat})
			
with open('web/public/Geiriadur/geiriadur.json', 'w') as f:
    json.dump({"data":entries}, f)
