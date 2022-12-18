# DnD Cymraeg

A Welsh translation of the Systems Reference Document (SRD) for Dungeons & Dragons.

This uses markdown files from [D&D 5E SRD REmastered](https://github.com/OldManUmby/DND.SRD.Wiki) by [Old Man Umby](http://www.oldmanumby.com).

Running the `autoTranslation.py` copies the markdown files from this source, does some simple automatic translation, and copies the files to the `DND_SRD_CYM` folder. The automatic translation depends on files in the "translationTables" folder. These are in json format and are used in some simple automatic translation scripts.

The aim is to translate documents paragraph by paragraph, putting the original English into a markdown quote block. Running the `makeWebsite.py` program converts the quote blocks to hidden elements in html files, written to the `web/public` folder.

## Contributing

Anyone can contribute, details to follow. If you know Github, get stuck in!

## Translation principles

This translation of D&D concepts follows several principles:

### Transparency

Someone who is familiar with D&D should be able to recognise the concepts easily. Some strategies to facilitate this include:

-  Translating the concept instead of the words, e.g. "Cloudkill" -> "Cwmwl Gwenwyn".
-  Investigating the etymology of the word as a guide, e.g. "Bugbear" has its origins in Middle English "bugge" meaning "something frightening", perhaps similar to Welsh "bwgan" so may translate as "Brawarth" or "Bwgarth".
-  Use of cognates, e.g. "Commune" -> "Ymgomino" rather than "Chweddleuo"; "Darkmantle" -> "Mantell Ddu" rather than "Clogyn Ddu".
-  Borrowing and phonetic translation, particularly for concepts borrowed from non-English languages and cultures.
-  For acronyms, trying to find a translation that uses the same acronym. e.g. "HP" -> "Heini Presennol", "AC" -> "Anhawster Curo", "DC" -> "Dosbarth Caledrwydd".

### Embedding Folklore

Celtic culture has a deep and unique folklore, much of which has inspired concepts in D&D. Translations should draw on this e.g. A "flying snake" has a specific word in Welsh, "Gwiber".  Or, for "Eldritch Blast", "Eldritch" apparently comes from a meaning like "Elf Realm". In Celtic folklore, Annwn is the realm of otherworldy beings, so -> "Blast Annwn".

### Utilising Variation

The Welsh language has a range of dialects and registers. These should be used as resources to add flavour and contrast. For example, there are multiple words for Elf, including "Elff" and  "Ellyll". So "Elf" -> "Elff" and "Drow" -> "Ellyll".

### Non-Essentialism

Historically, some of D&D's concepts reflect essentialism (e.g. [NASAGA blog](https://nasaga.org/confronting-racial-essentialism-in-dungeons-dragons/), [Premont & Heine, 2021](https://dl.acm.org/doi/abs/10.1145/3472538.3472560)). Replicating these concepts in translation should be avoided where possible. The official rules have moved from describing "races" to describing "species", and some argue that names like "half-elf" have supremacy overtones. This translation takes an aspirational approach.

This includes making class and monster descriptions gender neutral where appropriate. This is more of a challenge in Welsh, which has masculine morphemes in standard usage for classes/creature names. Avoid -wr and -wraig, and use -ydd or -yn.

### Fluency

Translations should be chosen that assist playing D&D interactively in real time. This means avoiding archaic words (unless that effect is useful), and avoiding using compound morphemes. The [Cymraeg Clir Guidelines](https://www.bangor.ac.uk/canolfanbedwyr/cymraeg_clir.php.en) are a good guide.

### Prioritise player-facing materials

Prioritise manual translation of spell list, PC stat parts (class, race, characterisations, gameplay) over DM parts (monster abilities, treasure).

---

* Download the [Markdown version of the SRD](https://github.com/OldManUmby/DND.SRD.Wiki/releases).
* Download Wizard's official [SRD v5.1 in PDF format](http://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf)
* Download Wizard's official [Errata and Basic Rules](http://dnd.wizards.com/articles/features/basicrules).
* Download Wizard's official [Characters Sheets](http://dnd.wizards.com/articles/features/character_sheets).

© 2015 Wizards. All Rights Reserved. Dungeons & Dragons® is a trademark[s] of Wizards of the Coast. For more information about Wizards of the Coast or any of Wizards' trademarks or other intellectual property, please visit their website at [www.wizards.com](http://www.wizards.com).