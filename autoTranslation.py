# -*- coding: utf-8 -*-

# Translate Treasure:
# 	Translate names
#   Add translation for treasure type, rareness,
#	DONE: Add translations for spell names (lower case surrounded by '*')

# Shade: anysbryd
# Conjoure - arswyn
# Ability: Gallu
# Familiar: Cynhalydd
# Bardic order = achen
# Bardic circle: Urdd/ Radd / achen
# cylch yr abred: circle of transmigration, circle of inchoation


# Prevent the program from running and overwriting progress
if False:
	print("\n\nWARNING: Converstion is locked, quitting\n\n")
	quit()

# List of files we should not overwrite
completedFiles = ["Anturio.md","Galluoedd.md","Ymladd.md","_Nodweddion_Rhywogaethau.md"]

# Bite, claw, slam

import os,json,re,copy

spellNames = json.load(open("translationTables/spellNames.json"))

spellNameTranslationForMonsterStatBlock = {}
for k in spellNames:
	spellNameTranslationForMonsterStatBlock["*"+k.lower()+"*"] = "*" + spellNames[k].lower() + "*"

raceTranslations = json.load(open("translationTables/races.json"))
classTranslations = json.load(open("translationTables/classes.json"))
classDescriptionsTranslations = json.load(open("translationTables/classDescriptions.json"))
skillTranslations = json.load(open("translationTables/skills.json"))
spellDescriptionsTranslations = json.load(open("translationTables/spellDescriptionTranslations.json"))
spellDescriptionSoftTranslations = json.load(open("translationTables/spellDescriptionSoftTranslations.json"))
damageTypes = json.load(open("translationTables/damageTypes.json"))
sensesTranslations = json.load(open("translationTables/senses.json"))
conditionTranslations = json.load(open("translationTables/conditions.json"))
languageTranslations = json.load(open("translationTables/languages.json")) 
weaponTranslations = json.load(open("translationTables/weapons.json")) 
chapterTitleTranslations = json.load(open("translationTables/chapterTitles.json")) 
treasureTranslations = json.load(open("translationTables/treasure.json")) 
treasureNameTranslations = json.load(open("translationTables/treasureNames.json")) 

damageTypes2 = copy.deepcopy(damageTypes)
damageTypes2.pop(" and ")


# TODO: Some skills e.g. "Medicine", "Persuasion" (see Priest)
monsterTranslations = json.load(open("translationTables/statBlockTranslations.json")) 
monsterSizeTranslations = json.load(open("translationTables/sizes.json")) 
monsterTypeTranslations = json.load(open("translationTables/monsterTypes.json")) 
monsterAlignmentTranslations = json.load(open("translationTables/alignments.json")) 
monsterNameTranslations = json.load(open("translationTables/monsterNames.json")) 

# Only translate if line starts with key
monsterContextTranslations = {
	"**Languages**": languageTranslations,
	"**Skills**": skillTranslations,
	"**Damage Resistances**": damageTypes,
	"**Damage Immunities**": damageTypes,
	"**Condition Immunities**": conditionTranslations,
	"**Senses**": sensesTranslations,
	"*Melee Weapon Attack:*": {
		" to hit,": " i fwrw,",
		" reach ": " cyrraedd ",
		" ft.": " tr.",
		" plus ": " ac ",
		"one target.": "un targed.",
		"two targets.": "dau targed.",
		"three targets.": "tri targed.",
		"acid damage": "difrod asid",
		"bludgeoning damage": "difrod taro",
		"cold damage": "difrod oer",
		"fire damage": "difrod tân",
		"force damage": "difrod grym",
		"lightning damage": "difrod mellt",
		"necrotic damage": "difrod necrotig",
		"piercing damage": "difrod tyllu",
		"poison damage": "difrod gwenwyn",
		"psychic damage": "difrod seicic",
		"radiant damage": "difrod pelydrol",
		"slashing damage": "difrod slasio",
		"thunder damage": "difrod taran"
	},
	"**Speed**": {
		" fly ": " hedfan ",
		" swim ": " nofio ",
		" climb ": " dringo "
	}
}


spellNameContextTranslations = {
	"**Components:**": {
		"Verbal": "Geiriol",
		" V": " G",
		"Somatic": "Somatig",
		" S": " S",
		"Material": "Materol",
		" M": " M"
	},
	"**Range:**": {
		"feet": "troedfedd",
		"Touch": "cyffwrdd",
		"Self": "Hunain",
		"Sight": "Golwg",
		"-foot radius sphere": "-troedfedd, sffêr",
		"-foot radius cylinder": "-troedfedd, sffêr",
		"-foot cone": "-troedfedd, côn",
		"-mile radius": "-milltir radiws",
		"-foot radius": "-troedfedd radiws",
		"-foot line": "-troedfedd, llinell",
		"-foot cube": "-troedfedd, ciwb",
		"miles": "millturoedd",
		"mile": "milltur",
		" and ": "ac",
		"Special": "Arbennig"
	},
	"**Duration:**": {
		"Concentration, up to ": "Canolbwyntio, hyd at ",
		" one ": " 1 ",
		" 1 hour": " 1 awr",
		"hours": "awr",
		" 1 minutes": " 1 munud",
		"minutes": " munud",
		" 1 round": " 1 rownd",
		"rounds": " rownd",
		"Instantaneous": "Ar unwaith",
		"Until dispelled": "Nes gwrthswyno",
		"or triggered": "neu actifadu"
	},
	"**Casting Time:**": {
		"bonus action": "acsiwn bonws",
		"action": "acsiwn",
		"minutes": "munud",
		"minute": "munud",
		"hours": "awr",
		"days": "dydd",
		"day": "dydd"
	}
}

def applyOneTranslation(txt,targ,repl,softTranslate=False):
	if softTranslate:
		return(re.sub(re.escape(targ),targ + " (" + repl + ")",txt))
	else:
		return(txt.replace(targ,repl))
	

def softTranslate(txt,softTranslations):
	# don't soft translate title
	header = txt[:txt.index("\n")]
	txt = txt[txt.index("\n"):]
	for tx in softTranslations:
		for k in tx:
			repl = tx[k]
			if type(repl) is str:
				# Simple string replace
				txt = applyOneTranslation(txt,k,repl,True)
	txt = header + txt
	return(txt)

def translateParts(filepath,translations,translateType=False,titleTranslations=None):
	with open(filepath) as o:
		txt = o.read()
	
	if translateType:
		txt = txt.split("\n")
		txt[2] = convertSizeAndType(txt[2])
		txt = "\n".join(txt)
		txt = monsterExtraTranslations(txt)

	if (not titleTranslations is None) and (filepath.count("#")==0 or any([x for x in ["Statistics","Spellcasting","Artifacts","Magic_Items","Sentient_Magic"]])):
		txt = translateTitle(txt, titleTranslations)
		
	txt = convertThrows(txt)

	for dDict in translations:
		for k in dDict:
			repl = dDict[k]
			if type(repl) is str:
				# Simple string replace
				txt = applyOneTranslation(txt,k,repl)
			else:
				# contextual replace (only replace based on matching k)
				txt = txt.split("\n")
				for i in range(len(txt)):
					if txt[i].count(k)>0:
						for rep in repl:
							txt[i] = txt[i].replace(rep,repl[rep])
				# Join back together
				txt = "\n".join(txt)
	# Previously, wrote to md file to convert to latex
	#with open("tmp.md",'w') as o:
	#	o.write(txt)
	return(txt)

def md2tex(filepath,destFilepath):
	pandocCommand = 'pandoc tmp.md -o "'+destFilepath+'"'
	#print(pandocCommand)
	os.system(pandocCommand)

def convertThrows(txt):
	# DC 18 Constitution saving throw
	# must make a DC 23 Dexterity saving throw
	for skillType in skillTranslations:
		tx = skillTranslations[skillType]
		txt = re.sub("must make a DC ([0-9]+) "+skillType+" saving throw", "llwyddo ar cais achub " + tx + " DC \\1",txt)
		txt = re.sub("must succeed on a DC ([0-9]+) "+skillType+" saving throw", "llwyddo ar cais achub " + tx + " DC \\1",txt)
	#taking 40 (9d8) acid damage on a failed save, or half as much damage on a successful one
	for damageType in damageTypes:
		txt = re.sub("taking ([0-9+]) (\\([0-9d]\\)) "+ damageType+" damage on a failed save, or half as much damage on a successful one", 
			"cymryd \\1 \\2 difrod "+ damageTypes[damageType]+" ar fethiant a hanner y difrod ar lwyddiant.",txt)
	
	txt = txt.replace("The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.", "Gall creadur ailadrodd y cais achub ar diwedd pob un o'i tro, gyda llwyddiant yn diweddu yr effaith ar ei hun.")
	
	for cond in conditionTranslations:
		txt = txt.replace("or be "+cond, "neu cael ei "+conditionTranslations[cond])
		
	txt = txt.replace("for 1 minute", "am un munud")
	txt = txt.replace("for 1 hour", "am un awr")
	txt = txt.replace("for 24 hours", "am 24 awr")
	
	return(txt)
		
	
	
	
def convertSizeAndType(line):
	#*Small elemental, neutral evil*
	#*Medium monstrosity, neutral*
	#*Huge beast, unaligned*
	#*Medium monstrosity (shapechanger), neutral*
	#*Tiny dragon, neutral good*
	#*Medium swarm of Tiny beasts, unaligned*
	if not line.startswith("*"):
		return(line)
	divPos = line.rindex(",")
	part1 = line[:divPos]
	part2 = line[divPos+1:]
	
	mSize,mType = part1.split(" ",1)
	mSize = mSize.replace("*","")
	mAlignment = part2.replace("*","")
	
	cSize = monsterSizeTranslations[mSize].lower()
	cType = mType
	for r in monsterTypeTranslations:
		repl = monsterTypeTranslations[r]
		cType = cType.replace(r,repl)
	cAlignment = mAlignment
	for r in monsterAlignmentTranslations:
		repl = monsterAlignmentTranslations[r]
		cAlignment = cAlignment.replace(r,repl)
	
	ret = "*" + cType + " " + cSize + ", " + cAlignment + "*"
	ret = re.sub(" +"," ",ret)
	#print(line)
	#print(ret)
	#print("-------------")
	return(ret)

def monsterExtraTranslations(txt):
	txt = re.sub("If .+? fails a saving throw, it can choose to succeed instead.", "Os yw'n methu cais achub, gall dewis i lwyddo yn lle hynny.", txt)
	txt = re.sub("\\*\\*\\*Frightful Presence\\*\\*\\*. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC ([0-9]+) Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.", 
	"***Presenoldeb Arswydus***. Mae rhaid i pob creadur o fewn 120 o'r ddraig ac sy'n ymwybodol o'r ddraig llwyddo ar cais achub Doethder DC \\1 neu ddod yn ofnus am 1 mumud. Gall creadur ailadrodd y cais achub ar diwedd pob un o'i tro, gyda llwyddiant yn diweddu yr effaith ar ei hun. Os yw cais achub y creadur yn llwyddianus neu mae'r effaith yn diweddu, mae'r creadur yn imiwn i Presenoldeb Arswydus y ddraig am 24 awr.", txt)
	txt = re.sub("The .+? can take ([1-9]) legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The .+? regains spent legendary actions at the start of its turn.", "Gall cymryd \\1 acsiwn chwedleuol o'r dewis islaw. Gall defnyddio dim ond un opsiwn ar y tro a dim ond ar ddiwedd tro creadur arall. Mae'n adennill unrhyw acsiwn chwedleuol wedi ei wario ar ddechrau ei tro.", txt)
	txt = re.sub ("\\*\\*Wing Attack \\(Costs 2 Actions\\)\\*\\*\\. The dragon beats its wings\\. Each creature within ([0-9]+) feet of the dragon must succeed on a DC ([0-9]+) Dexterity saving throw or take (.+?) bludgeoning damage and be knocked prone\\. The dragon can then fly up to half its flying speed\\.", 
	"**Ymosodiad Adain (Costio 2 Acsiwn)**. Mae'r draig yn curo ei adeiniau. Mae rhaid i bob creadur o fewn \\1 troedfedd o'r draig llwyddo ar cais achub Chwimder DC \\2 neu cymrud \\3 difrod taro a cael ei llorio. Gall y draig hedfan hyd at hanner ei cyflymder hedfan.", txt)
	txt = txt.replace("**Tail Attack**. The dragon makes a tail attack.", "**Ymosodiad Cynffon**. Mae'r draig yn gwneud ymosodiad cynffon.")
	txt = txt.replace("**Detect**. The dragon makes a Wisdom (Perception) check.", "**Canfod**. Mae'r draig yn gwneud cais Doethder (Canfyddiad).")
	# Amphibious
	txt = re.sub("The .+? can breathe air and water","Gall anadlu aer a dŵr",txt)
	txt = re.sub("and the target is grappled \\(escape DC ([0-9]+)\\)", "ac mae'r targed wedi ei afael (DC dianc \\1)",txt)
	return(txt)

def translateTitle2(currentTitle,translationTable):
	currentTitle = currentTitle.replace("#","").strip()
	if not currentTitle in translationTable:
		currentTitle += " (Creature)"
	if not currentTitle in translationTable:
		currentTitle = currentTitle[:currentTitle.rindex(" ")]+ " (NPC)"
	if not currentTitle in translationTable:
		currentTitle = currentTitle[:currentTitle.rindex(" ")]+ " (Devil)"
	if not currentTitle in translationTable:
		currentTitle = currentTitle[:currentTitle.rindex(" ")]+ " (Giant)"
	return(currentTitle)

def translateTitle(txt, translationTable):
	lines = txt.split("\n")
	currentTitle = translateTitle2(lines[0],translationTable)
	# Header actually varies in original, but should be just one "#"
	# header = currentTitle[:currentTitle.rindex("#")].strip()
	if currentTitle in translationTable:
		trans = translationTable[currentTitle]
		lines[0] = "# " + trans + " (" + currentTitle + ")"
	else:
		print("WARNING: Cannot find translation for title: "+ lines[0])
	txt = "\n".join(lines)
	return(txt)

	
def convertFolder(folder,destFolderName, translations=[], destBaseFolder="DND_SRD_CYM", translateType=False, titleTranslations=None,softTranslations=[]):
	files = os.listdir(folder)
	files = [x for x in files if x.endswith(".md")]
	# remove files that we've translated already
	files = [x for x in files if not x in completedFiles]
	
	for f in files:
		if f in ["## Spell Lists (Wikilinked).md","## Spell Lists.md"]:
			continue
		filepath = os.path.join(folder,f)
		
		# Translate
		txt = translateParts(filepath,translations,translateType,titleTranslations)
		txt = softTranslate(txt,softTranslations)
		txt = txt.replace("fff","ff")
		
		folder,filename = os.path.split(filepath)
		#destFilename = filename.replace(" ","_").replace("#","")
		# Take filename from translated title
		destFilename = txt.split("\n")[0].replace("#","").strip()
		if destFilename.count("(")>0:
			destFilename = destFilename[:destFilename.index("(")].strip()
		destFilename = destFilename.replace(" ","_")
		destFilename = destFilename.replace("'","")
		destFilename = destFilename + ".md"
		if filename.startswith("#"):
			destFilename = "_" + destFilename
		
		#lowerFolder = os.path.split(folder)[1]
		destFolder = os.path.join(destBaseFolder,destFolderName)
		if not os.path.isdir(destFolder):
			os.mkdir(destFolder)
		destFilepath = os.path.join(destFolder,destFilename)
		print("> "+destFilepath)
		
		with open(destFilepath,"w") as o:
			o.write(txt)

	

################
# Races
if False:
	convertFolder("DND.SRD.Wiki-0.5.1/Races/","Rhywogaethau",[raceTranslations],titleTranslations={"Racial Traits": "# Nodweddion Rhywogaethau"})

################
# Monsters
convertFolder("DND.SRD.Wiki-0.5.1/Monsters/", "Anghenfilod",
	[monsterContextTranslations,
		monsterTranslations,
		spellNameTranslationForMonsterStatBlock],
	translateType=True,
	titleTranslations=monsterNameTranslations, softTranslations=[conditionTranslations,damageTypes2])

	
	
################
# Spells xxx
convertFolder("DND.SRD.Wiki-0.5.1/Spells/","Swynau", [spellNameContextTranslations, spellDescriptionsTranslations], titleTranslations=spellNames, softTranslations=[spellDescriptionSoftTranslations, conditionTranslations])
# Spell list

################
# Classes
# Add case variants
weaponTranslations2 = {}
for wp in weaponTranslations:
	weaponTranslations2[wp] = weaponTranslations[wp]
	weaponTranslations2[wp.lower()] = weaponTranslations[wp].lower()
	weaponTranslations2[wp.capitalize()] = weaponTranslations[wp].capitalize()
classContextTranslations = {
	"**Weapons:**": weaponTranslations2,
	"**Skills:**": skillTranslations,
	"**Saving Throws:**": skillTranslations
}

spellNamesLower = {}
for s in spellNames:
	spellNamesLower[s.lower()] = spellNames[s].lower()

# (now skipped because we've translated by hand)
if False:
	convertFolder("DND.SRD.Wiki-0.5.1/Classes/","Dosbarthau",[classContextTranslations,classDescriptionsTranslations], titleTranslations=classTranslations, softTranslations = [spellNamesLower,skillTranslations])

##################
# Treasure

treasureNameTranslations["Magic Items"] = "Gwrthrychau Hud"
treasureNameTranslations["Artifacts"] = "Artiffactau"
treasureNameTranslations["Sentient Magic"] = "Hudolaeth Synhwyrol"

treasureTranslations2 = {"*":{}}
for k in treasureTranslations:
	treasureTranslations2["*"][k] = treasureTranslations[k]

convertFolder("DND.SRD.Wiki-0.5.1/Treasure","Trysor",[treasureTranslations2],titleTranslations=treasureNameTranslations,softTranslations = [spellNameTranslationForMonsterStatBlock,damageTypes2])


##################
# Other chapters
convertFolder("DND.SRD.Wiki-0.5.1/Characterizations","Cymeriadaeth",titleTranslations=chapterTitleTranslations)
convertFolder("DND.SRD.Wiki-0.5.1/Equipment","Cyfarpar",titleTranslations=chapterTitleTranslations, softTranslations = [weaponTranslations2, conditionTranslations, damageTypes2])
convertFolder("DND.SRD.Wiki-0.5.1/Gamemastering","Meistrolaethy y Gêm",titleTranslations=chapterTitleTranslations, softTranslations = [spellNameTranslationForMonsterStatBlock, conditionTranslations, ])

if False:
	convertFolder("DND.SRD.Wiki-0.5.1/Gameplay","Chwarae y Gêm",titleTranslations=chapterTitleTranslations,softTranslations= [spellNameTranslationForMonsterStatBlock, skillTranslations])




