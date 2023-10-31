# TODO: move quotes to hidden 'eng'
# surround with: <details><summary>eng</summary>CONTENT</details>

import os


def md2tex(filepath,destFilepath,pageTitle):
	pandocCommand = 'pandoc --toc --metadata title="' + pageTitle  +'" -s '+filepath.replace(" ","\\ ")+' -o "'+destFilepath+'"'
	os.system(pandocCommand)
	html = open(destFilepath).read()
	html = html.replace('<blockquote>','<details><summary>eng</summary><blockquote>')
	html = html.replace('</blockquote>','</blockquote></details>')
	if(filepath.endswith("tmp.txt")):
		# Top level index
		html = html.replace("</head>",headerTextMain)#"<html>\n"+headerTextMain+'\n<div class="info">'+ html+"\n</div></html>"
	else:
		html = html.replace("</head>",headerText)#"<html>\n"+headerText+'\n<div class="info">'+ html+"\n</div></html>"
	with open(destFilepath,'w') as o:
		o.write(html)


# convert index
cdir = "DND_SRD_CYM"

headerText = open("web/header.html").read()
headerTextMain = headerText.replace("../","")

ix = open("DND_SRD_CYM/index.md").read()
indexText = ""
currChapter = ""
# -  [Ty hwnt i Lefel 1](Cymeriadaeth/Ty_hwnt_i_Lefel_1.html)
for line in ix.split("\n"):
	if line.startswith("#"):
		currChapter = line[1:].strip()
	if line.strip().endswith("]"):
		lab = line[line.index("[")+1:line.index("]")]
		url = currChapter+"/"+lab.replace(" ","_")+".html"
		indexText += "-  ["+lab+"]"+"("+url+")\n"
	else:
		indexText += line + "\n"

with open("tmp.txt","w") as o:
	o.write(indexText)
	
md2tex("tmp.txt","web/public/index.html","Daeargelloedd & Dreigiau")

folders = [x for x in os.listdir(cdir) if os.path.isdir(os.path.join(cdir, x))]

for folder in folders:
	print("   "+folder)
	dfolder = "web/public/"+folder
	#dfolder = dfolder.replace(" ","_")
	if not os.path.exists(dfolder):
		os.mkdir(dfolder)
	files = os.listdir(os.path.join(cdir,folder))
	files = [x for x in files if x.endswith(".md")]
	for f in files:
		dest = dfolder +"/"+ f.replace(".md",".html")
		pageTitle = f.replace("_cy.html",".html").replace("_"," ")
		md2tex(cdir+"/"+folder+"/"+f,dest,pageTitle)