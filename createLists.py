# -*- coding: utf-8 -*-
import os,json,re

spellNames = json.load(open("translationTables/spellNames.json"))
classTranslations = json.load(open("translationTables/classes.json"))


# Monster List
monsterList = {}
monsterFiles = os.listdir("DND_SRD_CYM/Anghenfilod/")
monsterFiles = [x for x in monsterFiles if x.endswith(".md")]
monsterFiles = [x for x in monsterFiles if not x.startswith("_")]
for f in monsterFiles:
	o = open("DND_SRD_CYM/Anghenfilod/"+f)
	d = o.read()
	monsterName = d[1:d.index("\n")].strip()
	monsterType = "Arall"
	if monsterName.count("(")>1:
		monsterType = monsterName[monsterName.index("(")+1:monsterName.index(")")]
	if monsterType in ["Metalaidd","Cromatig"]:
		monsterType = "Draig "+monsterType
	if monsterType.count("Svirfneblin"):
		monsterType = "Arall"
	if not monsterType in monsterList:
		monsterList[monsterType] = []
	monsterList[monsterType].append((monsterName,f))

monsterListTxt = "# Rhestr Anghenfilod\n\n"
mTypes = [x for x in monsterList.keys()]
mTypes.sort()
for mType in mTypes:
	monsterListTxt += "\n## " + mType + "\n\n"
	monsterList[mType].sort()
	for mName,mURL in monsterList[mType]:
		mURL = mName
		if mURL.count("(")>0:
			mURL = mURL[:mURL.index("(")].strip()
		mURL = mURL.replace(" ","_")
		mURL = mURL.replace("'","")
		mURL = mURL + ".html"
		mName = mName.replace("(","(*",1)
		mName = "*)".join(mName.rsplit(')',1))
		monsterListTxt += "-  [" + mName + "]("+mURL+")\n"
with(open("DND_SRD_CYM/Anghenfilod/_Rhestr_Anghenfilod.md",'w')) as o:
	o.write(monsterListTxt)


##############
# Spell List
with open("DND.SRD.Wiki-0.5.1/Spells/## Spell Lists.md") as o:
	spellList = o.read()
uniqueSpells = []
translatedSpellList = ""
for line in spellList.split("\n"):
	if line.startswith("- "):
		eng = line[2:].strip()
		cym = spellNames[eng]
		spellNameX = cym + " (" + eng + ")"
		url = cym
		if url.count("(")>0:
			url = url[:url.index("(")].strip()
		url = url.replace(" ","_") + ".html"
		url = url.replace("'","")
		line = "-  [" + spellNameX.replace("(","(*").replace(")","*)") + "]("+ url +")"
		if not line in uniqueSpells:
			uniqueSpells.append(line)
	elif line.startswith("## "):
		eng_class = line[line.index(" ")+1:line.index("Spells")].strip()
		cym_class = classTranslations[eng_class]
		line = "## Swynau " + cym_class + " ("+ eng_class +" Spells)"
	elif line.startswith("#### "):
		if line.count("Cantrip")>0:
			line = "#### Swyngyfaredd (Cantrip, lefel 0)"
		else:
			line = "#### Lefel " + line[5]
	elif line == "# SPELL LISTS":
		line = "# Rhestr Swynau\n\n"
		for clx in classTranslations:
			if clx.count("ALT")==0:
				cym_class = classTranslations[clx]
				linkTitle = "-  [Swynau " + cym_class + " ("+ clx +" Spells)]"
				linkURL = "(#swynau-" + cym_class.lower() + "-"+ clx.lower() +"-spells)"
				line += linkTitle+linkURL + "\n"
	# Add line back to translation
	translatedSpellList += line + "\n"
with open("DND_SRD_CYM/Swynau/_Rhestr_Swynau_Dosbarthau.md", 'w') as o:
	o.write(translatedSpellList)

uniqueSpells.sort()
with open("DND_SRD_CYM/Swynau/_Rhestr_Swynau.md",'w') as o:
	o.write("# Rhestr Swynau\n\n" + "\n".join(uniqueSpells))


#######################
# Treasure List
treasureList = {}
treasureFiles = os.listdir("DND_SRD_CYM/Trysor/")
treasureFiles = [x for x in treasureFiles if x.endswith(".md")]
treasureFiles = [x for x in treasureFiles if not x.startswith("_")]
for f in treasureFiles:
	o = open("DND_SRD_CYM/Trysor/"+f)
	d = o.read()
	treasureName = d[1:d.index("\n")].strip()
	treasureType = d[d.index("*")+1:].strip()
	if treasureType.count("(")>0 and not treasureType.endswith(")"):
		treasureType += ")"
	treasureType = treasureType[:treasureType.index(",")].strip()
	if not treasureType in treasureList:
		treasureList[treasureType] = [] 
	treasureList[treasureType].append((treasureName,f))

treasureListTxt = "# Rhestr Trysorau\n\n"
mTypes = [x for x in treasureList.keys()]
mTypes.sort()
for mType in mTypes:
	treasureListTxt += "\n## " + mType + "\n\n"
	treasureList[mType].sort()
	for mName,mURL in treasureList[mType]:
		mURL = mName
		if mURL.count("(")>0:
			mURL = mURL[:mURL.index("(")].strip()
		mURL = mURL.replace(" ","_")
		mURL = mURL.replace("'","")
		mURL = mURL + ".html"
		mName = mName.replace("(","(*",1)
		mName = "*)".join(mName.rsplit(')',1))
		mName = mName.replace("#","").strip()
		mURL = mURL.replace("#","").strip()
		if mURL.startswith("_"):
			mURL = mURL[1:]
		treasureListTxt += "-  [" + mName + "]("+mURL+")\n"
with(open("DND_SRD_CYM/Trysor/_Rhestr_Trysorau.md",'w')) as o:
	o.write(treasureListTxt)