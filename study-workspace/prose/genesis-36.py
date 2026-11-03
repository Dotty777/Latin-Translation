# Study prose for Genesis 36 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of names and small turns of phrase differ.")
NAMES = between("The lists agree in persons; the Greek spells the names differently, and the Latin and King James follow the Hebrew forms.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 36,
 'chapterNote': (
  "The generations of Esau: his wives and sons, his move to Seir, the chiefs of Edom, the Horite clans, the kings of Edom before Israel had one, and the chiefs by "
  "their places. A genealogy’s differences are differences of spelling and of kinship terms. The Hebrew keeps Anah as “daughter of Zibeon” (36:2, 14), Zepho, "
  "Hemam, Alvan, Ebal, Shepho, Onam, Ezer, Dishan, “the hot springs” that Anah found, three sons of Ezer, Bela, Dinhabah, Bedad, Avith, Hadar, Pau, “the land of "
  "Seir” for the Horite chiefs, and Me-zahab as a daughter. The Greek keeps Anah as “son of Zibeon,” “out of the land of Canaan,” Sophar, Aiman, Golon, Gaibel, "
  "Soph, Oman, Asar, Rison, “Iamin” transliterated for the springs, four sons of Ezer, Balak, Dennaba, Barad, Geththaim, Arad son of Barad, Phogor, “the land of "
  "Edom,” “tribes, places, regions and nations,” Gola, Jether, Megediel, Zaphoim, and Me-zahab as a son. The Latin and King James follow the Hebrew; the King James "
  "says “dukes” for chiefs and “mules” for the springs."),
 'verses': {

 '36:1': {
  'received': "These are the generations of Esau, that is, Edom.",
  'explain': ("Esau receives his toledot, as Ishmael did, before Jacob’s story continues: the rejected line is recorded in full. The versions agree."),
  'shared': ["These are the generations of Esau.", "Esau is Edom.", "The record of his line begins."],
  'instructions': [ins(K, S, "Esau’s generations are recorded."), ins(W, R, "Esau is given a chapter; the brother who lost the blessing is not lost to the record, and his nation is counted before Jacob’s sons are.")],
  'entries': [],
  'lost': [AGREE]},

 '36:2': {
  'received': "Esau took Canaanite wives: Adah daughter of Elon the Hittite, and Oholibamah daughter of Anah, daughter of Zibeon the Hivite,",
  'explain': ("The wives’ names differ from 26:34 and 28:9; Adah here for Basemath there, and Basemath here for Mahalath. The Hebrew says daughter of Anah, daughter of Zibeon; the Greek son of Zibeon, which 36:24 supports; the Latin and King James daughter."),
  'shared': ["Esau took his wives from the daughters of Canaan.", "Adah, daughter of Elon the Hittite.", "Oholibamah, daughter of Anah, of Zibeon the Hivite."],
  'instructions': [ins(K, S, "Esau’s wives Adah and Oholibamah were Canaanite.")],
  'entries': ['canaan'],
  'lost': [loses("Hebrew bat-Tziv‘on, “daughter of Zibeon,” of Anah, becomes Greek tou huiou Sebegōn, “the son of Zibeon”; the kinship changes gender."), between("Latin “the daughter of Zibeon” and King James “the daughter of Zibeon” follow the Hebrew.")]},

 '36:3': {
  'received': "and Basemath, Ishmael’s daughter, sister of Nebaioth.",
  'explain': ("Mahalath of 28:9 under another name. The versions agree."),
  'shared': ["Basemath.", "She was Ishmael’s daughter.", "She was the sister of Nebaioth."],
  'instructions': [ins(K, S, "Basemath was Esau’s Ishmaelite wife.")],
  'entries': [],
  'lost': [AGREE]},

 '36:4': {
  'received': "Adah bore Eliphaz; Basemath bore Reuel.",
  'explain': ("Eliphaz is the name of Job’s Temanite friend; Reuel of Moses’ father-in-law. The versions agree."),
  'shared': ["Adah bore Eliphaz to Esau.", "Basemath bore Reuel.", "Two sons are named."],
  'instructions': [ins(K, S, "Eliphaz and Reuel were born to Esau.")],
  'entries': [],
  'lost': [AGREE]},

 '36:5': {
  'received': "Oholibamah bore Jeush, Jalam and Korah; these are Esau’s sons born in Canaan.",
  'explain': ("Five sons in all, born before the move to Seir. The versions agree."),
  'shared': ["Oholibamah bore Jeush, Jalam and Korah.", "These are the sons of Esau.", "They were born in the land of Canaan."],
  'instructions': [ins(K, S, "Esau had five sons in Canaan.")],
  'entries': ['canaan'],
  'lost': [AGREE]},

 '36:6': {
  'received': "Esau took his family, household and all his goods from Canaan and went to another land, away from Jacob.",
  'explain': ("Esau leaves Canaan to Jacob, as Lot left it to Abraham and Ishmael to Isaac. The Hebrew says went to another land; the Greek went out of the land of Canaan, with a fuller inventory; the Latin another region."),
  'shared': ["Esau took his wives, sons, daughters, household, livestock and all he had acquired in Canaan.", "He went to another land.", "He went away from his brother Jacob."],
  'instructions': [ins(K, S, "Esau left Canaan to Jacob."), ins(W, R, "Esau departs without being told to; the land settles on Jacob by the elder brother’s leaving, and the oracle is fulfilled by a move, not a war.")],
  'entries': ['jacob', 'canaan'],
  'lost': [keeps("Greek ek tēs gēs Chanaan, “out of the land of Canaan,” for Hebrew el-eretz, “to a land,” and a fuller list, panta ta hyparchonta kai panta ta ktēnē kai panta hosa ektēsato kai hosa periepoiēsato, “all possessions and all livestock and all he acquired and accumulated.”"), between("Latin “went to another region” and King James “went into the country” follow the Hebrew.")]},

 '36:7': {
  'received': "Their possessions were too great to dwell together; the land could not support them for their livestock.",
  'explain': ("The reason of 13:6 again. The Hebrew says because of their livestock; the Greek the multitude of their belongings; the Latin the multitude of their flocks."),
  'shared': ["Their possessions were too great for them to dwell together.", "The land of their sojourning could not support them.", "It was because of their livestock."],
  'instructions': [ins(K, S, "The brothers’ wealth required separate lands."), ins(W, R, "Abraham and Lot parted for the same reason; blessing in Genesis is measured in herds and resolved by distance.")],
  'entries': [],
  'lost': [between("Hebrew mi-pene miqnehem, “because of their livestock,” is Greek apo tou plēthous tōn hyparchontōn autōn, “from the multitude of their belongings”; Latin “the multitude of their flocks”; King James “because of their cattle.”")]},

 '36:8': {
  'received': "Esau settled in the hill country of Seir; Esau is Edom.",
  'explain': ("Seir, the red sandstone country south-east of the Dead Sea, named for its hairy, se‘ar, aspect or for the Horite Seir. The versions agree."),
  'shared': ["Esau dwelt in the hill country of Seir.", "Esau.", "He is Edom."],
  'instructions': [ins(K, S, "Esau settled in Seir.")],
  'entries': [],
  'lost': [AGREE]},

 '36:9': {
  'received': "These are the generations of Esau, father of Edom, in the hill country of Seir.",
  'explain': ("A second heading, for the Seir generation. The versions agree; the King James father of the Edomites."),
  'shared': ["These are the generations of Esau.", "He is the father of Edom.", "They are in the hill country of Seir."],
  'instructions': [ins(K, S, "The Seir generations of Esau begin.")],
  'entries': [],
  'lost': [AGREE]},

 '36:10': {
  'received': "Esau’s sons: Eliphaz, son of Adah, and Reuel, son of Basemath.",
  'explain': ("The two principal sons restated. The versions agree."),
  'shared': ["These are the names of Esau’s sons.", "Eliphaz, son of Esau’s wife Adah.", "Reuel, son of Esau’s wife Basemath."],
  'instructions': [ins(K, S, "Eliphaz and Reuel head the Edomite clans.")],
  'entries': [],
  'lost': [AGREE]},

 '36:11': {
  'received': "Eliphaz’s sons: Teman, Omar, Zepho, Gatam and Kenaz.",
  'explain': ("Teman gives its name to a district of Edom and to Job’s Eliphaz the Temanite. The Greek says Sophar for Zepho."),
  'shared': ["The sons of Eliphaz.", "Teman, Omar, Zepho.", "Gatam and Kenaz."],
  'instructions': [ins(K, S, "Eliphaz had five sons, including Teman.")],
  'entries': [],
  'lost': [between("Hebrew Tzefo, “Zepho,” is Greek Sōphar; Latin and King James “Zepho.”")]},

 '36:12': {
  'received': "Timna, Eliphaz’s concubine, bore Amalek; these are Adah’s descendants.",
  'explain': ("Amalek, Israel’s hereditary enemy, is Esau’s grandson by a concubine. The versions agree."),
  'shared': ["Timna was a concubine of Eliphaz, Esau’s son.", "She bore Amalek to Eliphaz.", "These are the descendants of Esau’s wife Adah."],
  'instructions': [ins(K, S, "Amalek descended from Esau through Eliphaz."), ins(W, R, "Amalek, who will attack Israel in the wilderness and whom Saul will fail to destroy, is a cousin; the longest enmity in Israel’s history is a family one.")],
  'entries': [],
  'lost': [AGREE]},

 '36:13': {
  'received': "Reuel’s sons: Nahath, Zerah, Shammah and Mizzah; these are Basemath’s descendants.",
  'explain': ("Four clans of Reuel. The versions agree."),
  'shared': ["The sons of Reuel.", "Nahath, Zerah, Shammah and Mizzah.", "These are the descendants of Esau’s wife Basemath."],
  'instructions': [ins(K, S, "Reuel had four sons.")],
  'entries': [],
  'lost': [AGREE]},

 '36:14': {
  'received': "The sons of Oholibamah, daughter of Anah, daughter of Zibeon: Jeush, Jalam and Korah.",
  'explain': ("The Hebrew again says daughter of Zibeon; the Greek son, as in verse 2."),
  'shared': ["These are the sons of Esau’s wife Oholibamah, daughter of Anah, of Zibeon.", "She bore to Esau.", "Jeush, Jalam and Korah."],
  'instructions': [ins(K, S, "Oholibamah’s three sons are restated.")],
  'entries': [],
  'lost': [loses("Hebrew bat-Tziv‘on, “daughter of Zibeon,” again becomes Greek huiou Sebegōn, “son of Zibeon.”"), between("Latin and King James “daughter of Zibeon.”")]},

 '36:15': {
  'received': "The chiefs of Esau’s sons: of Eliphaz the firstborn, chiefs Teman, Omar, Zepho, Kenaz,",
  'explain': ("Alluf, chief, perhaps leader of a thousand; the King James dukes. The Greek says Sophar."),
  'shared': ["These are the chiefs of the sons of Esau.", "The sons of Eliphaz, Esau’s firstborn.", "Chief Teman, chief Omar, chief Zepho, chief Kenaz."],
  'instructions': [ins(K, S, "Eliphaz’s sons became Edomite chiefs.")],
  'entries': [],
  'lost': [between("Hebrew Tzefo is Greek Sōphar; Hebrew allufe, “chiefs,” is Greek hēgemones, Latin duces, King James “dukes.”")]},

 '36:16': {
  'received': "chief Korah, chief Gatam, chief Amalek: the chiefs of Eliphaz in Edom, Adah’s descendants.",
  'explain': ("Korah appears among Eliphaz’s sons here and Oholibamah’s in verse 14; the lists are clan rosters, not strict pedigrees. The Latin says Eliphaz’s sons, Adah’s sons."),
  'shared': ["Chief Korah, chief Gatam, chief Amalek.", "These are the chiefs of Eliphaz in the land of Edom.", "These are the descendants of Adah."],
  'instructions': [ins(K, S, "Seven chiefs descend from Eliphaz.")],
  'entries': [],
  'lost': [between("Latin “These are Eliphaz’s sons in the land of Edom, and these are Adah’s sons” for Hebrew allufe Elifaz … bene Adah, “chiefs of Eliphaz … sons of Adah”; Greek and King James follow the Hebrew.")]},

 '36:17': {
  'received': "Reuel’s sons: chiefs Nahath, Zerah, Shammah, Mizzah; the chiefs of Reuel in Edom, Basemath’s descendants.",
  'explain': ("Four chiefs of Reuel. The versions agree."),
  'shared': ["These are the sons of Reuel, Esau’s son.", "Chief Nahath, chief Zerah, chief Shammah, chief Mizzah.", "These are the chiefs of Reuel in Edom, descendants of Basemath."],
  'instructions': [ins(K, S, "Four chiefs descend from Reuel.")],
  'entries': [],
  'lost': [AGREE]},

 '36:18': {
  'received': "Oholibamah’s sons: chiefs Jeush, Jalam, Korah; the chiefs of Oholibamah, daughter of Anah, Esau’s wife.",
  'explain': ("Three chiefs of Oholibamah. The Greek ends the chiefs of Oholibamah, without daughter of Anah, Esau’s wife."),
  'shared': ["These are the sons of Oholibamah, Esau’s wife.", "Chief Jeush, chief Jalam, chief Korah.", "These are the chiefs of Oholibamah."],
  'instructions': [ins(K, S, "Three chiefs descend from Oholibamah.")],
  'entries': [],
  'lost': [loses("Hebrew bat-Anah eshet Esav, “daughter of Anah, Esau’s wife,” at the close is absent from the Greek."), between("Latin and King James keep it.")]},

 '36:19': {
  'received': "These are Esau’s sons and their chiefs; he is Edom.",
  'explain': ("The close of the family roster. The Hebrew says he is Edom; the Greek these are the sons of Edom."),
  'shared': ["These are Esau’s sons.", "These are their chiefs.", "Esau is Edom."],
  'instructions': [ins(K, S, "Esau’s sons and chiefs are summed up.")],
  'entries': [],
  'lost': [between("Hebrew hu Edom, “he is Edom,” is Greek houtoi eisin huioi Edōm, “these are the sons of Edom”; Latin “he is Edom,” King James “who is Edom.”")]},

 '36:20': {
  'received': "The sons of Seir the Horite, inhabitants of the land: Lotan, Shobal, Zibeon, Anah,",
  'explain': ("The Horites, the earlier people of Seir, whom Esau’s line displaced and absorbed by marriage, Deuteronomy 2:12. The Hebrew says inhabitants, plural; the Greek who inhabited, of Seir."),
  'shared': ["These are the sons of Seir the Horite.", "They inhabited the land.", "Lotan, Shobal, Zibeon and Anah."],
  'instructions': [ins(K, S, "The Horite clans of Seir are listed."), ins(W, R, "The displaced people are recorded alongside their displacers; Scripture keeps the names of the Horites as carefully as the Edomites.")],
  'entries': [],
  'lost': [between("Hebrew yoshve ha-aretz, “inhabitants of the land,” plural, is Greek tou katoikountos tēn gēn, “who inhabited the land,” singular, of Seir; Latin and King James follow the Hebrew.")]},

 '36:21': {
  'received': "Dishon, Ezer and Dishan: the Horite chiefs, sons of Seir, in Edom.",
  'explain': ("Seven Horite clans. The Greek says Asar and Rison for Ezer and Dishan, and the Horite, the son of Seir, singular."),
  'shared': ["Dishon, Ezer and Dishan.", "These are the chiefs of the Horites.", "They are the sons of Seir in the land of Edom."],
  'instructions': [ins(K, S, "Seven Horite chiefs descend from Seir.")],
  'entries': [],
  'lost': [between("Hebrew Etzer ve-Dishan, “Ezer and Dishan,” is Greek Asar kai Risōn; Hebrew bene Se‘ir, “sons of Seir,” plural, is Greek tou huiou Sēir, singular; Latin and King James follow the Hebrew.")]},

 '36:22': {
  'received': "Lotan’s sons: Hori and Hemam; Lotan’s sister was Timna.",
  'explain': ("Timna, Eliphaz’s concubine of verse 12, is a Horite; the lines intermarry. The Greek says Aiman."),
  'shared': ["The sons of Lotan.", "Hori and Hemam.", "Lotan’s sister was Timna."],
  'instructions': [ins(K, S, "Lotan’s sons and sister Timna are named.")],
  'entries': [],
  'lost': [between("Hebrew Hemam is Greek Aiman; Latin “Heman,” King James “Hemam.”")]},

 '36:23': {
  'received': "Shobal’s sons: Alvan, Manahath, Ebal, Shepho and Onam.",
  'explain': ("The Greek forms are Golon, Manahath, Gaibel, Soph, Oman; the persons are the same."),
  'shared': ["These are the sons of Shobal.", "Alvan, Manahath, Ebal.", "Shepho and Onam."],
  'instructions': [ins(K, S, "Shobal had five sons.")],
  'entries': [],
  'lost': [NAMES]},

 '36:24': {
  'received': "Zibeon’s sons: Aiah and Anah, the Anah who found the hot springs in the wilderness while pasturing his father’s donkeys.",
  'explain': ("The one anecdote in the chapter. Yemim is a word found only here: hot springs by the Vulgate, mules by the rabbis and King James; the Greek transliterates Iamin and spells the finder Onas. This Anah is Zibeon’s son, as the Greek has it in verses 2 and 14."),
  'shared': ["Zibeon’s sons were Aiah and Anah.", "This is the Anah who found something in the wilderness.", "He was tending his father Zibeon’s donkeys."],
  'instructions': [ins(K, S, "Anah son of Zibeon made a discovery while herding."), ins(W, R, "One Horite herdsman is remembered for finding water, or breeding mules, in the desert; the genealogy pauses for a shepherd’s luck, and no one knows what he found.")],
  'entries': [],
  'lost': [loses("Hebrew ha-yemim, an unknown noun, becomes Greek ton Iamin, a transliteration; Hebrew Anah becomes Greek Onan and Onas within the verse."), between("Latin “hot springs,” King James “the mules.”")]},

 '36:25': {
  'received': "Anah’s children: Dishon and Oholibamah, daughter of Anah.",
  'explain': ("Oholibamah, Esau’s wife, is Horite on both sides. The Latin says a son Dishon and a daughter Oholibamah."),
  'shared': ["These are the children of Anah.", "Dishon.", "Oholibamah, the daughter of Anah."],
  'instructions': [ins(K, S, "Anah fathered Dishon and Oholibamah.")],
  'entries': [],
  'lost': [between("Latin “He had a son Dishon and a daughter Oholibamah” paraphrases; Hebrew, Greek and King James “the children of Anah: Dishon and Oholibamah.”")]},

 '36:26': {
  'received': "Dishon’s sons: Hemdan, Eshban, Ithran and Cheran.",
  'explain': ("The Hebrew spells the father Dishan here, as in verse 28; most translations read Dishon with the Greek and Samaritan. The Greek says Amada for Hemdan."),
  'shared': ["These are the sons of Dishon.", "Hemdan, Eshban.", "Ithran and Cheran."],
  'instructions': [ins(K, S, "Dishon had four sons.")],
  'entries': [],
  'lost': [between("Hebrew Dishan here, read Dishon by Greek, Latin and King James; Hebrew Chemdan is Greek Amada.")]},

 '36:27': {
  'received': "Ezer’s sons: Bilhan, Zaavan and Akan.",
  'explain': ("Three in the Hebrew; the Greek has four, Balaan, Zoukam, Ioukam and Oukan, the second name doubled."),
  'shared': ["These are the sons of Ezer.", "Bilhan and Zaavan.", "Akan."],
  'instructions': [ins(K, S, "Ezer had three sons.")],
  'entries': [],
  'lost': [keeps("The Greek lists four sons of Asar, Balaan kai Zoukam kai Ioukam kai Oukan, where the Hebrew has three, Bilhan va-Za‘avan va-Aqan."), between("Latin and King James give three.")]},

 '36:28': {
  'received': "Dishan’s sons: Uz and Aran.",
  'explain': ("Uz, the name of Job’s country. The Greek says Rison and Aram."),
  'shared': ["These are the sons of Dishan.", "Uz.", "Aran."],
  'instructions': [ins(K, S, "Dishan had two sons.")],
  'entries': [],
  'lost': [between("Hebrew Dishan … Aran is Greek Risōn … Aram; Latin and King James follow the Hebrew.")]},

 '36:29': {
  'received': "The Horite chiefs: Lotan, Shobal, Zibeon, Anah,",
  'explain': ("The seven Horite clans as chiefdoms. The versions agree."),
  'shared': ["These are the chiefs of the Horites.", "Chief Lotan, chief Shobal.", "Chief Zibeon, chief Anah."],
  'instructions': [ins(K, S, "The Horite chiefs are listed.")],
  'entries': [],
  'lost': [AGREE]},

 '36:30': {
  'received': "Dishon, Ezer, Dishan: the Horite chiefs by their clans in the land of Seir.",
  'explain': ("The Hebrew says in the land of Seir; the Greek in the land of Edom, with Asar and Rison."),
  'shared': ["Chief Dishon, chief Ezer, chief Dishan.", "These are the chiefs of the Horites.", "They are according to their chiefdoms in the land."],
  'instructions': [ins(K, S, "Seven Horite chiefdoms held Seir.")],
  'entries': [],
  'lost': [loses("Hebrew be-eretz Se‘ir, “in the land of Seir,” becomes Greek en gē Edōm, “in the land of Edom”; Hebrew Etzer, Dishan are Greek Asar, Risōn."), between("Latin and King James “in the land of Seir.”")]},

 '36:31': {
  'received': "These are the kings who reigned in Edom before any king reigned over Israel.",
  'explain': ("A note written from a time when Israel had kings, or anticipating 17:6. The Hebrew says over the sons of Israel; the Greek in Israel."),
  'shared': ["These are the kings who reigned in the land of Edom.", "It was before.", "Any king reigned over Israel."],
  'instructions': [ins(K, S, "Edom had kings before Israel."), ins(W, R, "Edom has kings while Israel is still a family; the elder brother comes first in this too, and the promise to Jacob of kings from his loins waits centuries.")],
  'entries': [],
  'lost': [between("Hebrew li-vne Yisra’el, “over the sons of Israel,” is Greek en Israēl, “in Israel”; Latin “before the children of Israel had a king,” King James “over the children of Israel.”")]},

 '36:32': {
  'received': "Bela son of Beor reigned in Edom; his city was Dinhabah.",
  'explain': ("Not a dynasty: each king is from a different city. The Greek says Balak and Dennaba; this Balak is not Balaam’s king, though Beor is Balaam’s father’s name."),
  'shared': ["Bela, son of Beor, reigned in Edom.", "His city.", "It was named Dinhabah."],
  'instructions': [ins(K, S, "Bela was Edom’s first king.")],
  'entries': [],
  'lost': [between("Hebrew Bela … Dinhavah is Greek Balak … Dennaba; Latin and King James “Bela … Dinhabah.”")]},

 '36:33': {
  'received': "Bela died, and Jobab son of Zerah of Bozrah reigned.",
  'explain': ("Bozrah, Edom’s chief city, named by the prophets. The Greek says Balak."),
  'shared': ["Bela died.", "Jobab, son of Zerah of Bozrah.", "He reigned in his place."],
  'instructions': [ins(K, S, "Jobab succeeded Bela.")],
  'entries': [],
  'lost': [between("Greek Balak for Hebrew Bela; the rest agrees.")]},

 '36:34': {
  'received': "Jobab died, and Husham of the Temanites reigned.",
  'explain': ("The Greek says Asom."),
  'shared': ["Jobab died.", "Husham of the land of the Temanites.", "He reigned in his place."],
  'instructions': [ins(K, S, "Husham succeeded Jobab.")],
  'entries': [],
  'lost': [between("Hebrew Chusham is Greek Asom; Latin and King James “Husham.”")]},

 '36:35': {
  'received': "Husham died, and Hadad son of Bedad, who defeated Midian in Moab, reigned; his city was Avith.",
  'explain': ("The one king with a deed: a victory over Midian in Moab’s territory. The Greek says Barad and Geththaim."),
  'shared': ["Husham died.", "Hadad, son of Bedad, who defeated Midian in the field of Moab, reigned.", "His city was named Avith."],
  'instructions': [ins(K, S, "Hadad defeated Midian and reigned in Edom.")],
  'entries': [],
  'lost': [between("Hebrew Bedad … Avit is Greek Barad … Geththaim; Latin and King James “Bedad … Avith.”")]},

 '36:36': {
  'received': "Hadad died, and Samlah of Masrekah reigned.",
  'explain': ("The versions agree."),
  'shared': ["Hadad died.", "Samlah of Masrekah.", "He reigned in his place."],
  'instructions': [ins(K, S, "Samlah succeeded Hadad.")],
  'entries': [],
  'lost': [AGREE]},

 '36:37': {
  'received': "Samlah died, and Shaul of Rehoboth-on-the-River reigned.",
  'explain': ("Rehoboth by the River, perhaps the Euphrates, a foreign king. The versions agree; the King James Saul."),
  'shared': ["Samlah died.", "Shaul of Rehoboth by the River.", "He reigned in his place."],
  'instructions': [ins(K, S, "Shaul succeeded Samlah.")],
  'entries': [],
  'lost': [AGREE]},

 '36:38': {
  'received': "Shaul died, and Baal-hanan son of Achbor reigned.",
  'explain': ("Baal-hanan, Baal is gracious, a Canaanite name. The versions agree."),
  'shared': ["Shaul died.", "Baal-hanan, son of Achbor.", "He reigned in his place."],
  'instructions': [ins(K, S, "Baal-hanan succeeded Shaul.")],
  'entries': [],
  'lost': [AGREE]},

 '36:39': {
  'received': "Baal-hanan died, and Hadar reigned; his city was Pau, and his wife Mehetabel, daughter of Matred, daughter of Me-zahab.",
  'explain': ("The eighth and last king, the only one whose wife is named. The Hebrew says Hadar, Pau, daughter of Me-zahab; the Greek Arad son of Barad, Phogor, son of Me-zahab; 1 Chronicles 1:50 reads Hadad and Pai."),
  'shared': ["Baal-hanan son of Achbor died.", "Hadar reigned in his place and his city was named Pau.", "His wife was Mehetabel, daughter of Matred, of Me-zahab."],
  'instructions': [ins(K, S, "Hadar was Edom’s eighth king.")],
  'entries': [],
  'lost': [loses("Hebrew Hadar … Pa‘u … bat Me-zahav, “Hadar … Pau … daughter of Me-zahab,” becomes Greek Arad huios Barad … Phogōr … huiou Maizoob, “Arad son of Barad … Phogor … son of Me-zahab.”"), between("Latin and King James “Hadar … Pau … the daughter of Mezahab.”")]},

 '36:40': {
  'received': "The chiefs of Esau by their clans and places, by name: Timna, Alvah, Jetheth,",
  'explain': ("A final list, of chiefs by territory, some bearing place-names. The Greek says tribes, places, regions and nations, Gola, Jether."),
  'shared': ["These are the names of the chiefs of Esau.", "They are by their families and places, by their names.", "Chief Timna, chief Alvah, chief Jetheth."],
  'instructions': [ins(K, S, "Esau’s territorial chiefs are listed.")],
  'entries': [],
  'lost': [keeps("Greek kata tas phylas autōn, kata topon autōn, en tais chōrais autōn kai en tois ethnesin autōn, “by their tribes, by their places, in their regions and in their nations,” expands Hebrew le-mishpechotam li-mqomotam bi-shmotam, “by their families, by their places, by their names”; Hebrew Alvah, Yetet are Greek Gōla, Iether."), between("Latin and King James follow the Hebrew.")]},

 '36:41': {
  'received': "Oholibamah, Elah, Pinon,",
  'explain': ("Oholibamah as a chief, a clan named for the wife or a place. Elah is Elath on the Red Sea. The versions agree."),
  'shared': ["Chief Oholibamah.", "Chief Elah.", "Chief Pinon."],
  'instructions': [ins(K, S, "The list continues with Oholibamah, Elah and Pinon.")],
  'entries': [],
  'lost': [AGREE]},

 '36:42': {
  'received': "Kenaz, Teman, Mibzar,",
  'explain': ("The versions agree."),
  'shared': ["Chief Kenaz.", "Chief Teman.", "Chief Mibzar."],
  'instructions': [ins(K, S, "The list continues with Kenaz, Teman and Mibzar.")],
  'entries': [],
  'lost': [AGREE]},

 '36:43': {
  'received': "Magdiel and Iram: the chiefs of Edom by their dwellings in the land they held. This is Esau, father of Edom.",
  'explain': ("Eleven territorial chiefs, and the closing formula. The Greek says Megediel and Zaphoim; the Latin father of the Edomites."),
  'shared': ["Chief Magdiel, chief Iram.", "These are the chiefs of Edom by their dwellings in the land of their possession.", "This is Esau, the father of Edom."],
  'instructions': [ins(K, S, "The chapter closes with Esau as father of Edom."), ins(W, R, "“The land of their possession”: Esau has a land and holds it while Jacob’s sons are still tenting in Canaan. The blessing withheld from Esau was not land or kings, and the chapter is honest about what he had.")],
  'entries': [],
  'lost': [between("Hebrew Magdi’el … Iram is Greek Megediēl … Zaphōim; Latin “father of the Edomites,” Greek and Hebrew “father of Edom,” King James “the father of the Edomites.”")]},
 }
}
