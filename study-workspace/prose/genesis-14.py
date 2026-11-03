# Study prose for Genesis 14 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 14,
 'chapterNote': (
  "The war of the kings, Lot’s capture and rescue, Melchizedek’s blessing and Abram’s refusal of the spoil are the same story in every "
  "column. What varies is names and the texture of the war. The Hebrew keeps Tidal king of Goiim, Bela, the valley of Siddim, the Rephaim, "
  "Zuzim and Emim as distinct peoples, El-paran, the territory of Amalek, “possessions” for the spoil, Abram the Hebrew, a force divided for "
  "the night attack, Aner, “possessor of heaven and earth,” and an oath already sworn to YHWH God Most High. The Greek keeps Thargal king of "
  "nations, Balak, the salt ravine, giants and strong nations and Ommaeans, the terebinth of Paran, the rulers of Amalek, “horses” for the spoil "
  "three times, Abram “the one from beyond,” a sudden fall upon the enemy, Aunan, “who created heaven and earth,” and a hand raised to God Most "
  "High alone. The Latin has Arioch king of Pontus and the Wooded Valley; the King James follows the Hebrew."),
 'verses': {

 '14:1': {
  'received': "In the days of Amraphel of Shinar, Arioch of Ellasar, Chedorlaomer of Elam and Tidal king of nations,",
  'explain': ("The first war in Scripture is introduced by four eastern kings, led out of the land of Babel against the cities of the plain. "
   "The Hebrew names Tidal king of Goiim, which may be a people’s name; the Greek calls him Thargal king of nations; the Latin makes Arioch "
   "king of Pontus and Chedorlaomer king of the Elamites. The Greek sets the events in Amraphel’s reign."),
  'shared': ["Four kings are named.", "They are Amraphel, Arioch, Chedorlaomer and Tidal.", "They rule Shinar, Ellasar, Elam and the nations."],
  'instructions': [ins(K, S, "Four eastern kings, led by Chedorlaomer of Elam, began the first war in Scripture.")],
  'entries': ['babylon'],
  'lost': [
   loses("Hebrew Tid‘al melekh Goyim, “Tidal king of Goiim,” becomes Greek Thargal basileus ethnōn, “Thargal king of nations”; the name changes form and Goiim is translated. Hebrew bi-yeme, “in the days of,” becomes Greek en tē basileia, “in the reign of.”"),
   between("Latin “Arioch king of Pontus … Chedorlaomer king of the Elamites … Tidal king of the nations” goes its own way on two names; King James follows the Hebrew. Tidal is often compared with the Hittite royal name Tudhaliya."),
  ]},

 '14:2': {
  'received': "they made war on the five kings of Sodom, Gomorrah, Admah, Zeboiim and Bela, which is Zoar.",
  'explain': ("The five kings of the plain are named with their cities. The names are spelled quite differently in Greek, Balla for Bera, "
   "Barsa for Birsha, Sennaar for Shinab, Symobor for Shemeber, Balak for Bela, and are kept as they stand. Zoar, the old Bela, is the one "
   "city of the five that will be spared for Lot’s sake."),
  'shared': ["The four kings made war.", "They fought the kings of Sodom, Gomorrah, Admah and Zeboiim.", "They fought the king of Bela, which is Zoar."],
  'instructions': [ins(K, S, "The five cities of the plain, Sodom among them, were attacked by the eastern kings.")],
  'entries': [],
  'lost': [
   loses("Hebrew Bera, Birsha, Shinab, Shemeber and Bela appear in Greek as Balla, Barsa, Sennaar, Symobor and Balak, forms that differ substantially; Sennaar coincides with the Greek for Shinar."),
   between("Latin and King James keep the Hebrew forms. Greek epoiēsan polemon, “made war,” is the phrase of Revelation 11:7 and 13:7; Hosea 11:8 recalls Admah and Zeboiim."),
  ]},

 '14:3': {
  'received': "All five joined forces in the valley of Siddim, which is the Salt Sea.",
  'explain': ("The five kings gather in a valley identified with the Salt Sea, the Dead Sea, usually taken to mean that the valley later lay "
   "under its southern waters. The Hebrew names the valley Siddim; the Greek calls it the salt ravine; the Latin the Wooded Valley. All "
   "identify it with the sea, so the differing names do not place the gathering at different sites."),
  'shared': ["All five kings joined together.", "They met in a valley.", "The valley is identified with the Salt Sea."],
  'instructions': [ins(K, S, "The five kings gathered in the valley that became the Salt Sea.")],
  'entries': [],
  'lost': [
   loses("Hebrew emeq ha-Siddim, “the valley of Siddim,” is a name; Greek tēn pharanga tēn halykēn, “the salt ravine,” is a description, and Hebrew chaveru, “joined together,” becomes Greek synephōnēsan, “agreed together.” The name Siddim is gone from the Greek."),
   between("Latin “the Wooded Valley” reads Siddim as a word for fields or woods; King James “the vale of Siddim” keeps the name. Greek thalassa tōn halōn is the Salt Sea of Numbers 34:12 and Ezekiel 47:8."),
  ]},

 '14:4': {
  'received': "They had served Chedorlaomer twelve years and rebelled in the thirteenth.",
  'explain': ("The cause of the war: twelve years of tribute as subject states, then revolt. The Greek verb for rebelling is the root of "
   "“apostasy,” standing away, here a political revolt against an overlord. All versions agree."),
  'shared': ["They served Chedorlaomer.", "They served for twelve years.", "In the thirteenth year they rebelled."],
  'instructions': [ins(K, S, "The cities of the plain rebelled against Chedorlaomer after twelve years of subjection.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James agree; the Latin adds “against him.” Greek apestēsan, “rebelled,” is the verb of Hebrews 3:12; 2 Kings 18:7 and 24:1 show the same pattern.")]},

 '14:5': {
  'received': "In the fourteenth year Chedorlaomer and his allies struck the peoples east of the Jordan: the Rephaim, the Zuzim and the Emim.",
  'explain': ("The punitive campaign sweeps down the east of the Jordan before reaching the plain. The Hebrew names three peoples, the "
   "Rephaim at Ashteroth-karnaim, the Zuzim in Ham, the Emim at Shaveh-kiriathaim; the Greek has giants, strong nations with them, and "
   "Ommaeans in the city of Shaveh, using for the Rephaim the word it chose for the Nephilim of 6:4. Og of Bashan was the last of the Rephaim."),
  'shared': ["In the fourteenth year Chedorlaomer and the kings with him came.", "They struck the Rephaim at Ashteroth-karnaim.", "They struck other peoples east of the Jordan."],
  'instructions': [ins(K, S, "The eastern kings first defeated the peoples of Transjordan, the Rephaim among them.")],
  'entries': ['rephaim', 'emim', 'giant-peoples-overview'],
  'lost': [
   loses("Hebrew Refa’im, “Rephaim,” becomes Greek gigantes, “giants”; Hebrew ha-Zuzim be-Ham, “the Zuzim in Ham,” becomes ethnē ischyra hama autois, “strong nations with them”; Hebrew Emim be-Shaveh Qiryatayim becomes Ommaious en Sauē tē polei, “Ommaeans in the city of Shaveh.” The three Hebrew names are reduced to one."),
   between("Latin “Rephaim … Zuzim with them … Emim in Shaveh-kiriathaim” and King James “Rephaims … Zuzims in Ham … Emims in Shaveh Kiriathaim” keep the Hebrew names; the Latin shares “with them.” Deuteronomy 3:11 names Og; Deuteronomy 1:4 names Ashtaroth."),
  ]},

 '14:6': {
  'received': "They struck the Horites in the mountains of Seir as far as El-paran by the wilderness.",
  'explain': ("The campaign reaches south to Seir, home of the Horites who will later be displaced by Esau’s descendants, and to the edge of the "
   "wilderness of Paran, where Ishmael will live and from which Israel will send the spies. The Hebrew names El-paran; the Greek translates "
   "the first element as a terebinth; the Latin as plains."),
  'shared': ["They struck the Horites.", "The Horites were in the mountains of Seir.", "The campaign reached Paran by the wilderness."],
  'instructions': [ins(K, S, "The campaign reached the Horites of Seir and the edge of the wilderness of Paran.")],
  'entries': [],
  'lost': [
   loses("Hebrew El-Paran, a place name, becomes Greek tēs terebinthou tēs Pharan, “the terebinth of Paran,” translating el as a tree; Hebrew al-ha-midbar, “beside the wilderness,” becomes Greek en tē erēmō, “in the wilderness.” Hebrew “their mountain of Seir” loses “their.”"),
   between("Latin “the Plains of Paran” takes el another way; King James “Elparan, which is by the wilderness” keeps the name and the Hebrew preposition. Genesis 36:20–30 lists the Horites; 21:21 and Numbers 13:3 return to Paran."),
  ]},

 '14:7': {
  'received': "They turned back to Kadesh and struck the country of the Amalekites and the Amorites of Hazezon-tamar.",
  'explain': ("The army swings back north through Kadesh, the spring of judgement where Israel will later camp, striking the Amalekite region "
   "and the Amorites of Hazezon-tamar. Amalek himself is born later, so the name points to the land his people held. The Hebrew says the "
   "whole territory of Amalek; the Greek all the rulers of Amalek. The Greek translates En-mishpat as Spring of Judgment."),
  'shared': ["They turned back and came to Kadesh.", "They struck the Amalekites.", "They struck the Amorites living in Hazezon-tamar."],
  'instructions': [ins(K, S, "The campaign returned through Kadesh and struck Amalek and the Amorites.")],
  'entries': [],
  'lost': [
   loses("Hebrew kol-sedeh ha-Amaleqi, “the whole territory of the Amalekite,” becomes Greek pantas tous archontas Amalēk, “all the rulers of Amalek”; land becomes leaders. Hebrew En Mishpat, a name, is Greek tēn pēgēn tēs kriseōs, “the Spring of Judgment,” a translation."),
   between("Latin “the spring of Mishpat … the whole region of the Amalekites” and King James “Enmishpat … all the country of the Amalekites” follow the Hebrew. Numbers 20:1 and Exodus 17:8 return to Kadesh and Amalek."),
  ]},

 '14:8': {
  'received': "The five kings of the plain went out and drew up for battle in the valley of Siddim",
  'explain': ("The five kings meet the four in the valley of verse 3. The names continue as before: Bela in the Hebrew, Balak in the Greek; "
   "Siddim in the Hebrew, the salt valley in the Greek, the Wooded Valley in the Latin. The lines are drawn."),
  'shared': ["The kings of Sodom, Gomorrah, Admah and Zeboiim went out.", "The king of Bela, which is Zoar, went out with them.", "They drew up battle lines in the valley."],
  'instructions': [ins(K, S, "The five kings met the invaders in battle in the valley of Siddim.")],
  'entries': [],
  'lost': [
   loses("Hebrew Bela and emeq ha-Siddim are again Greek Balak and tēn koilada tēn halykēn, “the salt valley.”"),
   between("Latin “the Wooded Valley … against them” and King James “the vale of Siddim … joined battle with them” follow the Hebrew; the Latin and King James repeat “the king of” five times as the Hebrew does."),
  ]},

 '14:9': {
  'received': "against Chedorlaomer, Tidal, Amraphel and Arioch, four kings against five.",
  'explain': ("The four are listed again, now with Chedorlaomer first as the real leader, and the odds are stated: four against five. The "
   "smaller alliance from the east will win, and Abram will later defeat these same four with his household and allies. Tidal and Goiim "
   "continue as Thargal and nations in the Greek."),
  'shared': ["They fought Chedorlaomer of Elam and Tidal king of nations.", "They fought Amraphel of Shinar and Arioch of Ellasar.", "It was four kings against five."],
  'instructions': [ins(K, S, "Four eastern kings fought the five of the plain and won.")],
  'entries': [],
  'lost': [
   loses("Hebrew Tid‘al melekh Goyim is Greek Thargal basileus ethnōn, as in 14:1."),
   between("Latin “king of the Elamites … king of Pontus” and King James “Elam … Ellasar” divide as in 14:1. Greek hoi tessares basileis pros tous pente, “the four kings against the five,” anticipates 14:15 and 14:17."),
  ]},

 '14:10': {
  'received': "The valley was full of bitumen pits; the kings of Sodom and Gomorrah fell there, and the rest fled to the hills.",
  'explain': ("The battlefield itself defeats the five. The valley is full of tar pits, the same bitumen that sealed the ark and bound the "
   "bricks of Babel; the Dead Sea was known for lumps of it floating up. The kings of Sodom and Gomorrah fall there, the Greek says fall "
   "into them, and the survivors flee to the hills where Lot will later be told to flee. The king of Sodom nonetheless reappears in verse 17."),
  'shared': ["The valley was full of bitumen pits.", "The kings of Sodom and Gomorrah fled and fell there.", "The remaining men fled to the hill country."],
  'instructions': [ins(K, S, "The kings of the plain were routed among the bitumen pits of their own valley.")],
  'entries': [],
  'lost': [
   keeps("Greek enepesan ekei, “fell into them there,” makes the pits the thing fallen into; Hebrew va-yippelu shammah, “fell there,” is less specific. Neither adds “some of them” to explain the king of Sodom’s survival."),
   between("Latin “the Wooded Valley” and King James “the vale of Siddim … slimepits” continue their names. Genesis 6:14 and 11:3 have the bitumen; 19:17 the flight to the hills."),
  ]},

 '14:11': {
  'received': "The victors took all the goods of Sodom and Gomorrah and their food, and left.",
  'explain': ("The spoil is carried off. The Hebrew says all the possessions of Sodom and Gomorrah; the Greek says all the horses, the first "
   "of three places where it reads the spoil as cavalry. Raiding armies lived on what they seized, so the food goes too. When it is all "
   "recovered Abram will accept nothing but what his young men have eaten."),
  'shared': ["They took the spoil of Sodom and Gomorrah.", "They took all their food.", "They went away."],
  'instructions': [ins(K, S, "The eastern kings plundered Sodom and Gomorrah and withdrew.")],
  'entries': [],
  'lost': [
   loses("Hebrew kol-rekhush, “all the possessions,” becomes Greek tēn hippon pasan, “all the horses,” here and in 14:16 and 14:21; the Greek narrows the goods to a military asset."),
   between("Latin “all the possessions … food supplies” and King James “all the goods … victuals” follow the Hebrew. Judges 6:4 shows raiders living off the land."),
  ]},

 '14:12': {
  'received': "They also took Lot, Abram’s nephew, and his goods, for he was living in Sodom.",
  'explain': ("Lot’s choice in chapter 13 catches up with him: he is now living in Sodom, and he is carried off with everything he chose. The "
   "Hebrew says his possessions; the Greek his baggage, a word that often includes a household’s dependents. The report will reach Abram."),
  'shared': ["They took Lot, Abram’s nephew.", "They took his possessions.", "Lot was living in Sodom."],
  'instructions': [ins(K, S, "Lot was captured with Sodom because he lived there."), ins(W, R, "Lot’s share of the plain is taken with the plain; what is chosen by sight is lost by force.")],
  'entries': [],
  'lost': [between("Hebrew rekhusho, “his possessions,” is Greek tēn aposkeuēn autou, “his baggage,” a household term; the Greek adds “and went away.” Latin “his possessions” and King James “his goods” follow the Hebrew; the Latin and King James put “who dwelt in Sodom” before the goods.")]},

 '14:13': {
  'received': "A survivor told Abram the Hebrew, who was living by the oaks of Mamre with his Amorite allies Eshcol and Aner.",
  'explain': ("Abram is called the Hebrew for the first time; the Greek renders the word as “the one from beyond,” taking it as one who "
   "crossed the river. He lives by Mamre, with Mamre’s brothers Eshcol and Aner as sworn allies, the first human covenant named in "
   "Scripture. The Hebrew says oaks, the Greek an oak, the Latin a valley; the Greek reads Aunan for Aner."),
  'shared': ["One who escaped reported to Abram.", "Abram was living by Mamre the Amorite.", "Mamre’s brothers Eshcol and Aner were Abram’s allies."],
  'instructions': [ins(K, S, "Abram, living at Mamre with Amorite allies, heard of Lot’s capture."), ins(W, R, "The patriarch has sworn allies among the Amorites; faith does not forbid friendship with neighbours.")],
  'entries': ['abraham', 'hebron'],
  'lost': [
   loses("Hebrew Avram ha-Ivri, “Abram the Hebrew,” becomes Greek Abram tō peratē, “Abram the one from beyond,” a descriptive rendering; Hebrew elone, “oaks,” is a singular oak; Hebrew Aner is Greek Aunan. Hebrew ba‘ale berit, “masters of a covenant,” is Greek synōmotai, “sworn allies.”"),
   between("Latin “Abram the Hebrew … the valley of Mamre … Aner … had made a covenant” and King James “Abram the Hebrew … the plain of Mamre … Aner … confederate” keep the Hebrew name and ally. Genesis 21:27 and Joshua 9:15 are later covenants between men."),
  ]},

 '14:14': {
  'received': "Hearing that Lot was captured, Abram mustered three hundred and eighteen men born in his house and pursued as far as Dan.",
  'explain': ("Abram goes to war for his nephew. Three hundred and eighteen fighting men, born in his own household, are enough to pursue four "
   "kings to Dan at the northern edge of the land, a city named here by the name it later bore. The Hebrew calls them trained men, a word "
   "found nowhere else; the Greek counts household-born men and names Lot."),
  'shared': ["Abram heard that his kinsman had been captured.", "He mustered three hundred and eighteen men born in his household.", "He pursued as far as Dan."],
  'instructions': [ins(K, S, "Abram pursued the eastern kings with 318 of his own men to rescue Lot."), ins(W, R, "The man who gave Lot first choice now risks everything to recover him; kinship outlasts a parting.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew va-yareq et-chanikhav, “he mustered his trained men,” uses a verb of drawing out and a noun found only here; Greek ērithmēsen tous idious oikogeneis, “he counted his own household-born men,” changes both. The Greek adds Lot’s name."),
   between("Latin “mustered his three hundred eighteen armed men” names Lot like the Greek but keeps the mustering; King James “armed his trained servants” follows the Hebrew. Judges 18:29 and 1 Kings 12:29 are Dan."),
  ]},

 '14:15': {
  'received': "Abram attacked them by night with his servants, struck them, and pursued them to Hobah, north of Damascus.",
  'explain': ("A night attack by a small force, as Gideon will make against Midian. The Hebrew says Abram divided his force against them; the "
   "Greek that he fell upon them. Facing east, left meant north, so Hobah lies north of Damascus, far beyond the borders of the land. The "
   "Greek word for his men is rendered from the military setting, not as children."),
  'shared': ["Abram and his servants attacked by night.", "They struck the enemy.", "They pursued as far as Hobah, left of Damascus."],
  'instructions': [ins(K, S, "Abram’s night attack routed the four kings and drove them past Damascus."), ins(W, R, "A household of herdsmen defeats an imperial army; the victory is credited in verse 20 to God, not to the tactics.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew va-yechaleq alehem, “he divided against them,” describes splitting the force; Greek epepesen ep’ autous, “he fell upon them,” describes a sudden assault; the division is gone from the Greek. Hebrew avadav, “his slaves,” is Greek hoi paides autou, “his attendants.”"),
   between("Latin “he divided his companions, fell upon the enemy” has both; King James “he divided himself against them” follows the Hebrew. Judges 7:16–19 is Gideon’s night attack."),
  ]},

 '14:16': {
  'received': "Abram brought back all the goods, his kinsman Lot and his possessions, and the women and the people.",
  'explain': ("Everything is recovered, and the verb is repeated: he brought back, he brought back. The kinsman who redeems the captive is a "
   "picture the Law will use. The Hebrew says all the possessions; the Greek again says all the horses, and ties them to Sodom. The women "
   "and the people are named last, the human spoil that mattered most."),
  'shared': ["Abram brought back all the goods.", "He brought back his kinsman Lot and Lot’s possessions.", "He brought back the women and the people."],
  'instructions': [ins(K, S, "Abram recovered Lot, the captives and all the spoil."), ins(W, R, "The rescue is complete and costs Abram nothing he keeps; the redeemer gives back what he has won.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew kol-ha-rekhush, “all the possessions,” is again Greek pasan tēn hippon Sodomōn, “all the horses of Sodom,” adding the city and narrowing the goods."),
   between("Latin “all the possessions” and King James “all the goods” follow the Hebrew. Leviticus 25:48–49 and 1 Samuel 30:18–19 are the redeemer and the recovery."),
  ]},

 '14:17': {
  'received': "The king of Sodom came out to meet Abram in the valley of Shaveh, the King’s Valley, on his return.",
  'explain': ("The king of Sodom, fallen among the pits in verse 10 and now alive again, comes to meet the victor. The meeting place is the "
   "valley of Shaveh, called the King’s Valley; the Greek calls it a plain. The scene is set for two kings to meet Abram, Sodom’s and "
   "Salem’s, and for Abram to answer each differently."),
  'shared': ["Abram returned from defeating Chedorlaomer and the kings with him.", "The king of Sodom went out to meet him.", "They met in the valley of Shaveh, the King’s Valley."],
  'instructions': [ins(K, S, "The king of Sodom met Abram on his return from the victory.")],
  'entries': [],
  'lost': [between("Hebrew emeq Shaveh hu emeq ha-melekh, “the valley of Shaveh, which is the King’s Valley,” is Greek tēn koilada tēn Sauē, touto ēn to pedion basileōs, “the valley of Shaveh, which was the King’s Plain”; valley becomes plain in the second name and “is” becomes “was.” Latin and King James keep “valley”; King James “the king’s dale.”")]},

 '14:18': {
  'received': "Melchizedek, king of Salem and priest of God Most High, brought out bread and wine.",
  'explain': ("A second king appears, unannounced: Melchizedek, king of Salem and the first priest named in Scripture, long before Aaron. "
   "Hebrews explains the name as king of righteousness and Salem as peace, and Psalm 110 names the coming Lord a priest after his order. He "
   "brings bread and wine, loaves in the Greek, which early Christian writers saw as a figure of the Lord’s Supper."),
  'shared': ["Melchizedek was king of Salem.", "He brought out bread and wine.", "He was priest of God Most High."],
  'instructions': [ins(K, S, "Melchizedek, priest-king of Salem, met Abram with bread and wine."), ins(W, R, "A priest of the true God stands outside Abram’s family; God has worshippers the covenant has not yet reached.")],
  'entries': ['el-elyon', 'high-priest', 'jerusalem'],
  'lost': [
   keeps("Greek artous, “loaves,” is plural where Hebrew lechem, “bread,” is collective; the Greek keeps the kingship, the priesthood and the wine. Hebrews 7:1–3 and Psalm 110:4 build on this verse."),
   between("Latin “bread and wine, for he was priest” and King James “bread and wine: and he was the priest” follow the Hebrew. Hebrew El Elyon and Greek theos hypsistos are “God Most High,” the title of Luke 1:32."),
  ]},

 '14:19': {
  'received': "Melchizedek blessed Abram by God Most High, maker and possessor of heaven and earth.",
  'explain': ("The priest blesses the patriarch, and Hebrews draws the conclusion: the lesser is blessed by the greater. The Hebrew calls God "
   "the possessor of heaven and earth, with a word that can mean possessor or maker; the Greek and Latin say who created them; the King "
   "James possessor. The two senses are not at odds. The Greek names Abram where the Hebrew says “him.”"),
  'shared': ["Melchizedek blessed Abram.", "The blessing is by God Most High.", "God Most High is the possessor and maker of heaven and earth."],
  'instructions': [ins(K, S, "Abram was blessed by Melchizedek in the name of God Most High."), ins(W, R, "Abram receives a blessing rather than giving one; the father of faith accepts that someone stands above him.")],
  'entries': ['el-elyon', 'creator', 'abraham'],
  'lost': [
   loses("Hebrew qoneh shamayim va-arets, “possessor of heaven and earth,” allows possessor or maker; Greek hos ektisen ton ouranon kai tēn gēn, “who created heaven and earth,” decides for creating. Hebrew “blessed him” is Greek “blessed Abram.”"),
   between("Latin “who created” follows the Greek; King James “possessor” the Hebrew. Hebrews 7:6–7 reads the direction of the blessing."),
  ]},

 '14:20': {
  'received': "Melchizedek blessed God Most High for the victory, and Abram gave him a tenth of everything.",
  'explain': ("The blessing turns from Abram to God, who delivered the enemies into Abram’s hand; the verb is the one used whenever God hands "
   "enemies over in battle. Then a tenth is given, the first tithe in Scripture, long before the Law. The Hebrew and Greek leave the giver "
   "as “he”; the Latin names Abram; Hebrews argues from the gift that Levi, in Abraham, paid tithes to Melchizedek."),
  'shared': ["Blessed be God Most High.", "He delivered the enemies into Abram’s hand.", "A tenth of everything was given."],
  'instructions': [ins(K, S, "Abram gave Melchizedek a tenth of all after the victory."), ins(W, R, "The first tithe is a thank-offering for a rescue; Abram gives to God’s priest before he refuses the king of Sodom.")],
  'entries': ['el-elyon', 'abraham'],
  'lost': [between("Hebrew paredōken and Greek paredōken, “delivered,” agree; Hebrew be-yadekha, “into your hand,” is Greek hypocheirious soi, “into your power.” Latin “by whose protection your enemies are in your hands … Abram gave” adds the name; King James “he gave him tithes of all” keeps the pronoun. Hebrews 7:4 and 7:9 draw the lesson.")]},

 '14:21': {
  'received': "The king of Sodom asked Abram for the people and offered him the goods.",
  'explain': ("The king of Sodom proposes the customary division: the rescued people to him, the spoil to the victor. The Hebrew says the "
   "people and the possessions; the Greek the men and the horses; the Latin the people and the rest. By custom everything would be Abram’s; "
   "the king asks only for the captives."),
  'shared': ["The king of Sodom spoke to Abram.", "He asked for the people.", "He offered Abram the goods."],
  'instructions': [ins(K, S, "The king of Sodom offered Abram the spoil in exchange for the captives.")],
  'entries': [],
  'lost': [
   loses("Hebrew ha-nefesh, “the people,” and ha-rekhush, “the possessions,” become Greek tous andras, “the men,” and tēn hippon, “the horses”; the third narrowing of the spoil to horses."),
   between("Latin “give me the people; take the rest” and King James “give me the persons, and take the goods” follow the Hebrew. Numbers 31:9–11 shows the custom."),
  ]},

 '14:22': {
  'received': "Abram answered with an oath to God Most High, possessor and maker of heaven and earth.",
  'explain': ("Abram refuses with an oath, swearing by the very title Melchizedek used and binding his refusal to the Creator. The Hebrew says "
   "he has already raised his hand to YHWH, God Most High, a completed gesture; the Greek says he will stretch out his hand to God Most High, "
   "a future one, and omits the name YHWH. The Hebrew possessor is again the Greek creator."),
  'shared': ["Abram answered the king of Sodom.", "He raised his hand in oath to God Most High.", "God Most High is possessor and maker of heaven and earth."],
  'instructions': [ins(K, S, "Abram swore by God Most High in refusing the king of Sodom."), ins(W, R, "An oath to the Creator frames a refusal of wealth; Abram will not let a king of Sodom be the source of his riches.")],
  'entries': ['el-elyon', 'yhwh-yahweh', 'abraham'],
  'lost': [
   loses("Hebrew harimoti yadi el-YHWH El Elyon, “I have raised my hand to YHWH, God Most High,” names YHWH and records a completed gesture; Greek ektenō tēn cheira mou pros ton theon ton hypsiston, “I will stretch out my hand to God Most High,” drops the name and makes the gesture future. Hebrew qoneh is again Greek ektisen."),
   between("Latin “I lift my hand to the Lord God Most High, possessor” and King James “I have lift up mine hand unto the LORD, the most high God, the possessor” keep the name and the Hebrew title. Greek names the king of Sodom where the Latin says “him.”"),
  ]},

 '14:23': {
  'received': "Abram would take nothing of the king’s, not even a thread or sandal strap, lest he say he had made Abram rich.",
  'explain': ("The oath formula refuses even the smallest item, a thread and a sandal strap, a saying for things of no value; John the Baptist "
   "speaks of being unworthy to loosen the strap of Christ’s sandal. Abram wants no one but God to have made him rich. The Greek says sandal "
   "fastening for strap; the versions otherwise agree."),
  'shared': ["Abram will take nothing of the king’s.", "Not even a thread or a sandal strap.", "The reason is that the king must not say he made Abram rich."],
  'instructions': [ins(K, S, "Abram refused all the spoil of Sodom for himself."), ins(W, R, "Wealth from the wrong hand is refused so that the right hand may be seen; Abram guards the credit for God.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew serokh-na‘al, “sandal strap,” is Greek sphairōtēr hypodēmatos, “sandal fastening”; the Hebrew has “nor anything of yours” as a third item, the Greek “from anything of yours.” Latin and King James follow the Hebrew. Mark 1:7 and Proverbs 10:22 are the echoes.")]},

 '14:24': {
  'received': "Abram excepted only what his young men had eaten and the share due to his allies Aner, Eshcol and Mamre.",
  'explain': ("Abram refuses for himself but will not impose his choice on others. The young men, a common word for soldiers, have eaten; the "
   "three Amorite allies may take their share. The Hebrew opens “nothing for me”; the Greek lacks the phrase and orders the names Eshcol, "
   "Aunan, Mamre. David will later rule the same way about those who went and those who stayed."),
  'shared': ["Abram excepts what the young men have eaten.", "He excepts the share of the men who went with him.", "They are Aner, Eshcol and Mamre, and they may take their share."],
  'instructions': [ins(K, S, "Abram let his allies take their share while taking none himself."), ins(W, R, "Generosity in refusing does not become a rule for others; Abram’s scruple is his own, and his allies are free.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew bil‘adai, “nothing for me,” opens the verse and is absent from the Greek; Hebrew Aner, Eshkol u-Mamre becomes Greek Eschōl, Aunan, Mambrē, reordered and respelled; Hebrew “let them take” becomes Greek “they shall take.”"),
   between("Latin “Aner, Eshcol, and Mamre. Let these take their shares” and King James “Aner, Eshcol, and Mamre; let them take their portion” follow the Hebrew order and mood. 1 Samuel 30:22–24 is David’s ruling."),
  ]},
 }
}
