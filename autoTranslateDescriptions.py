from deep_translator import GoogleTranslator
import os, time,re, hashlib

adjusts = {
	"swynion": "swynau",
	"cyfnod": "swyn",
	"cyfnodau": "swynau",
	"slot sillafu": "slot swyno",
	"slotiau sillafu": "slotiau swyno",
	"sillafu": "swyn", # (sometimes 'swyno')
	"tafliad arbed": "cais achub",
	"dafliad arbed": "cais achub",
	"bwrw'r swyn": "llunio'r swyn",
	"bwrw swyn": "llunio swyn",
	"fwrw": "llunio",
	" gweithred[,\\. ]": "acsiwn",
	"camau gweithredu": "acsiynnau",
	"cam gweithredu": "acsiwn",
	"arbediad llwyddiannus": "cais achyb llwyddiannus",
	"CC": "DM",
	"melee": "sgarmes",
	"seibiant": "saib",
	"gorffwys": "saib",
	"pwynt taro": "pwynt heini",
	"pwyntiau taro": "pwyntiau heini",
	"Ar darllen uwch:": "Ar lefelau uwch:",
	
	"aberiad": "gwyriant",
	"nefol": "nefolydd",
	"fiend": "diawl",
	"dieflig": "diawliaid",
	" fei[,\\. ]": "tylwyth teg",
	"diferu": "llaid",
	"unmarw": "anfarwol",
	"goblin": "coblyn"
}

def getHash(txt):
	return(hashlib.md5(txt.encode()).hexdigest())
	
def translateText(txt):
	hx = getHash(txt)
	filepath = "tmp/R_"+str(hx)+".txt"
	resp = ""
	if os.path.isfile(filepath):
		resp = open(filepath).read()
	else:
		resp = translator.translate(txt)
		time.sleep(2)
		open(filepath,'w').write(resp)
	resp = makeAdjusts(resp)
	return(resp)
	
def makeAdjusts(txt):
	for trg in adjusts:
		txt = re.sub(trg, adjusts[trg], txt)
	return(txt)

def translateEntry(filepath):
	entry = open(filepath).read()
	if entry.count("Cyfieithiad Awtomatig")>0:
		return(None)
	lastAsterisk = entry.rindex("\n**Parhad")
	descSep = entry.index("\n",lastAsterisk+2)
	header = entry[:descSep]
	description_eng = entry[descSep+1:].strip()
	description_cym = translateText(description_eng)
	final = header + "\n\n### Cyfieithiad Awtomatig\n\n"  
	final += description_cym
	final += "\n\n>  " + description_eng.replace("\n","\n>  ")
	open(filepath,'w').write(final)
	return("OK")


translator = GoogleTranslator(source='en', target='cy')

folder = "DND_SRD_CYM/Swynau/"
files = os.listdir(folder)
files = [f for f in files if f.endswith(".md")]
files = [f for f in files if not f.startswith("_")]
files.sort()
print("Translating ...")
for file in files:
	print("   "+file)
	translateEntry(folder+file)





