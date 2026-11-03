# Study prose for Genesis 10 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

def same_list(received, explain, shared, know, note, entries=None, wisdom=None):
    v = {'received': received, 'explain': explain, 'shared': shared,
         'instructions': [ins(K, S, know)], 'entries': entries or [],
         'lost': [between(note)]}
    if wisdom: v['instructions'].append(ins(W, R, wisdom))
    return v

CHAPTER = {
 'slug': 'genesis', 'chapter': 10,
 'chapterNote': (
  "The table of nations lists the same three branches in the same order in every column, and most of its names are the same names in "
  "different spellings. What varies is the count and a handful of names. The Hebrew keeps seventy nations, Dodanim, Resen, Mash, Obal, "
  "Uzal, Nimrod as a mighty man, coastlands for the Japhethites, and families for the groupings. The Greek keeps seventy-two, with "
  "Elishah added among Japheth’s sons and Cainan added twice among Shem’s, Rhodians for Dodanim, Dasem, Meshech, Aizel, no Obal, Nimrod "
  "as a giant, islands, and tribes. The Latin and King James follow the Hebrew list; Luke’s genealogy of Jesus follows the Greek in "
  "including Cainan."),
 'verses': {

 '10:1': same_list(
  "These are the generations of Noah’s sons, Shem, Ham and Japheth, who had sons after the flood.",
  ("A new heading opens the table of nations. The seventy names that follow in the Hebrew, seventy-two in the Greek, are the peoples of "
   "the known world traced to Noah’s three sons. Copies of Luke likewise differ between seventy and seventy-two disciples sent out, "
   "a number often read against this chapter. All versions agree on the heading."),
  ["These are the generations of Noah’s sons.", "They are Shem, Ham and Japheth.", "Sons were born to them after the flood."],
  "The nations of the earth descend from Noah’s three sons.",
  "Hebrew, Greek, Latin and King James agree. Greek geneseis, “generations,” is the heading word of 2:4 and 6:9; Deuteronomy 32:8 and Luke 10:1 are read against the table’s count.",
  entries=['noah'], wisdom="A list of nations is placed under one family; the chapter teaches that the peoples are kin before they are strangers."),

 '10:2': {
  'received': "The sons of Japheth are Gomer, Magog, Madai, Javan, Tubal, Meshech and Tiras.",
  'explain': ("Japheth’s line comes first: the peoples of the north and the Aegean. Javan is the Hebrew name for the Ionian Greeks, "
   "Magog the land Ezekiel names with Gog. The Hebrew, Latin and King James give seven sons; the Greek gives eight, adding Elishah, "
   "whom all the versions list again as a son of Javan in verse 4. The Greek keeps both occurrences, and they should not be deleted to match."),
  'shared': ["These are the sons of Japheth.", "Gomer, Magog, Madai and Javan are named.", "Tubal, Meshech and Tiras are named."],
  'instructions': [ins(K, S, "Japheth’s sons are the peoples of the north and the Greek world.")],
  'entries': [],
  'lost': [
   keeps("An added Elisa, “Elishah,” between Javan and Tubal, making eight sons; the Hebrew has seven and lists Elishah only under Javan in 10:4. The Greek count of nations rises with this and the Cainans of 10:22 and 10:24 to seventy-two."),
   between("Latin and King James give the seven of the Hebrew. Ezekiel 38:2 and Revelation 20:8 take up Magog; Isaiah 66:19 sends messengers to Javan."),
  ]},

 '10:3': same_list(
  "The sons of Gomer are Ashkenaz, Riphath and Togarmah.",
  ("Gomer’s three sons are northern peoples. Togarmah returns in Ezekiel, trading horses with Tyre and marching with Gog from the far "
   "north; Ashkenaz was later attached to the Jews of Germany. All versions agree."),
  ["These are the sons of Gomer.", "Ashkenaz and Riphath are named.", "Togarmah is named."],
  "Gomer’s sons are Ashkenaz, Riphath and Togarmah.",
  "Hebrew, Greek, Latin and King James agree; Greek Thorgama is Hebrew Togarmah. Ezekiel 27:14 and 38:6 name Beth-togarmah."),

 '10:4': {
  'received': "The sons of Javan are Elishah, Tarshish, Kittim and Dodanim, or the Rhodians.",
  'explain': ("Javan’s sons are the peoples of the sea: Elishah, Tarshish, the far western port toward which Jonah flees, Kittim, "
   "usually Cyprus, and a fourth whose name divides the texts. The Hebrew reads Dodanim; 1 Chronicles reads Rodanim; the Greek reads "
   "Rhodians, the people of Rhodes. Hebrew d and r look alike, which explains the two forms without deciding which is older."),
  'shared': ["These are the sons of Javan.", "Elishah, Tarshish and Kittim are named.", "A fourth, Dodanim or the Rhodians, is named."],
  'instructions': [ins(K, S, "Javan’s sons are the peoples of the Mediterranean coasts and islands.")],
  'entries': [],
  'lost': [
   loses("Hebrew Dodanim becomes Greek Rhodioi, “Rhodians,” the reading of 1 Chronicles 1:7 (Rodanim). The Hebrew form with d is not in the Greek."),
   between("Latin and King James read Dodanim with the Hebrew. Jonah 1:3 and Isaiah 66:19 name Tarshish."),
  ]},

 '10:5': {
  'received': "From these the coastland peoples spread, each by its land, language, family and nation.",
  'explain': ("Japheth’s section closes with a formula that will recur: lands, languages, families and nations. The Hebrew calls them "
   "the coastlands of the nations, a maritime region; the Greek the islands of the nations, the coastlands of the Mediterranean to "
   "whom Isaiah’s Servant will call. Hebrew families are Greek tribes. The formula anticipates the division of languages at Babel."),
  'shared': ["From these the coastland or island peoples were divided.", "Each had its own land and language.", "They were grouped by families and nations."],
  'instructions': [ins(K, S, "The Japhethites spread as coastland peoples, divided by language and family."), ins(W, R, "Diversity of land and tongue is recorded as the ordinary spread of one family, before Babel gives it a darker cause.")],
  'entries': [],
  'lost': [
   loses("Hebrew iyye ha-goyim, “coastlands of the nations,” is broader than Greek nēsoi tōn ethnōn, “islands of the nations”; Hebrew mishpechot, “families,” is Greek phylai, “tribes.”"),
   between("Latin “islands … families” and King James “isles of the Gentiles … families” divide between the two. Isaiah 49:1 calls to the islands."),
  ]},

 '10:6': same_list(
  "The sons of Ham are Cush, Mizraim, Put and Canaan.",
  ("Ham’s line is the south: Cush, the land south of Egypt; Mizraim, the Hebrew name for Egypt in a dual form often read as its two "
   "lands; Put, usually Libya; and Canaan, whose land God will promise to Abram. All versions agree."),
  ["These are the sons of Ham.", "Cush and Mizraim are named.", "Put and Canaan are named."],
  "Ham’s sons are the peoples of Africa and Canaan.",
  "Hebrew, Greek, Latin and King James agree; Greek Mesraim is Hebrew Mitsrayim, Egypt, and King James Phut is Put. Exodus 12:12 and 3:8 take up Egypt and Canaan.",
  entries=['egypt', 'canaan']),

 '10:7': same_list(
  "The sons of Cush are Seba, Havilah, Sabtah, Raamah and Sabteca; Raamah’s sons are Sheba and Dedan.",
  ("Cush’s sons and grandsons are the peoples of Arabia and the Red Sea. Havilah was named in 2:11 as a land of gold; Sheba will send "
   "its queen to Solomon; Dedan traded with Tyre. All versions agree."),
  ["These are the sons of Cush.", "Seba, Havilah, Sabtah, Raamah and Sabteca are named.", "Raamah’s sons are Sheba and Dedan."],
  "Cush’s descendants are the peoples of Arabia.",
  "Hebrew, Greek, Latin and King James agree; King James Sabtechah is Sabteca."),

 '10:8': {
  'received': "Cush was the father of Nimrod, who began to be a mighty man on the earth.",
  'explain': ("The table pauses for one man. Nimrod, Cush’s son, begins to be mighty. The Hebrew calls him a mighty man, a gibbor; the "
   "Greek a giant, the same word it used for the Nephilim and the heroes of 6:4, so the Greek reader sees Nimrod among that company. "
   "His name is often linked to the Hebrew for rebel, a link that is debated. Neither text here calls him corrupt."),
  'shared': ["Cush begat Nimrod.", "Nimrod began to be mighty.", "His might was on the earth."],
  'instructions': [ins(K, S, "Nimrod, son of Cush, was the first mighty man after the flood."), ins(W, R, "The first great man after the flood is remembered for power, not for faith; the table notes him and moves on.")],
  'entries': ['nephilim'],
  'lost': [
   loses("Hebrew gibbor, “mighty man,” becomes Greek gigas, “giant,” the word of 6:4. The Hebrew distinction between a warrior and the giants is gone, as it was there."),
   between("Latin “mighty” and King James “a mighty one” follow the Hebrew. Greek Nebrōd is Hebrew Nimrod."),
  ]},

 '10:9': {
  'received': "Nimrod was a mighty hunter before the Lord, which became a saying.",
  'explain': ("Nimrod’s fame is as a hunter, and it became proverbial. “Before the Lord” has been read as in the Lord’s sight and as in "
   "defiance of the Lord; Josephus made Nimrod the rebel behind the tower of Babel. The Hebrew says a mighty hunter, the Greek a giant "
   "hunter, and the Greek adds God to Lord in the first clause. The Hebrew says it is said; the Greek they will say."),
  'shared': ["Nimrod was a mighty hunter.", "He was so before the Lord.", "A saying arose about him."],
  'instructions': [ins(K, S, "Nimrod’s prowess as a hunter became proverbial."), ins(W, R, "“Before the Lord” can mean under his eye or against his face; a reputation for might is read both ways.")],
  'entries': ['lord-translation'],
  'lost': [
   loses("Hebrew gibbor-tsayid, “mighty hunter,” is again Greek gigas kynēgos, “giant hunter,” twice. Hebrew lifne YHWH, “before YHWH,” becomes enantion kyriou tou theou, “before the Lord God,” in the first clause. Hebrew al-ken ye’amar, “therefore it is said,” becomes dia touto erousin, “therefore they will say.”"),
   between("Latin “mighty hunter before the Lord … hence the saying arose” and King James “mighty hunter before the LORD: wherefore it is said” follow the Hebrew."),
  ]},

 '10:10': {
  'received': "The beginning of Nimrod’s kingdom was Babylon, Erech, Akkad and Calneh in the land of Shinar.",
  'explain': ("Nimrod is the first king named in Scripture, and his first city is Babel, or Babylon, the same Hebrew name that will be "
   "explained in 11:9. Erech and Akkad are old cities of Mesopotamia; Shinar is the southern plain where the tower will be built. "
   "Babylon becomes Scripture’s great image of a proud world power, down to Revelation."),
  'shared': ["Nimrod had a kingdom.", "It began with Babylon, Erech, Akkad and Calneh.", "They were in the land of Shinar."],
  'instructions': [ins(K, S, "Nimrod’s kingdom began at Babylon in the land of Shinar."), ins(W, R, "The first kingdom and the first proud city share a founder; Babylon’s story begins with a hunter who became a king.")],
  'entries': ['babylon'],
  'lost': [between("Hebrew Bavel and Greek Babylōn are the same name, Babel in 11:9; Hebrew Shin‘ar is Greek Sennaar. Latin Babylon and King James Babel follow their own traditions. Daniel 1:2 and Revelation 17:5 carry the names on.")]},

 '10:11': {
  'received': "From that land Asshur went out and built Nineveh, Rehoboth-Ir and Calah.",
  'explain': ("Assyria enters. Both columns read Asshur as the builder who went out from Shinar and founded Nineveh, Jonah’s city, and "
   "Calah. The Hebrew can also be read as “he went out to Asshur,” making Nimrod the builder of Nineveh; no flight from tyranny is "
   "stated either way. The Hebrew Rehoboth-Ir is “the city of Rehoboth” in Greek and “the city’s streets” in Latin."),
  'shared': ["Someone went out from the land of Shinar.", "Nineveh and Calah were built.", "A third place, Rehoboth-Ir, was built."],
  'instructions': [ins(K, S, "Nineveh and the cities of Assyria were founded from the land of Shinar.")],
  'entries': ['nineveh'],
  'lost': [between("Hebrew Rechovot-Ir, “Rehoboth-Ir,” is Greek tēn Rhoōbōth polin, “the city of Rehoboth,” and Latin plateas civitatis, “the city’s streets,” translating the name. Both Hebrew and Greek take Asshur as subject; the Hebrew also allows “to Asshur.” Jonah 3:3 and Matthew 12:41 take up Nineveh.")]},

 '10:12': {
  'received': "He built Resen, between Nineveh and Calah; that is the great city.",
  'explain': ("A fourth city lies between the other two. The Hebrew calls it Resen; the Greek Dasem, again the look-alike Hebrew letters "
   "d and r. “That is the great city” is ambiguous in every version; Jonah calls Nineveh the great city three times, and the phrase "
   "is usually taken of Nineveh here, though the grammar does not settle it."),
  'shared': ["A city was built between Nineveh and Calah.", "It is named Resen or Dasem.", "One of these is called the great city."],
  'instructions': [ins(K, S, "The cities of Assyria included one between Nineveh and Calah.")],
  'entries': ['nineveh'],
  'lost': [
   loses("Hebrew Resen becomes Greek Dasem, by the confusion of d and r seen at 10:4. The Hebrew name is not in the Greek."),
   between("Latin and King James read Resen with the Hebrew; King James “a great city” drops the article. Jonah 1:2 and 3:2 call Nineveh “the great city.”"),
  ]},

 '10:13': {
  'received': "Mizraim was the father of the Ludim, Anamim, Lehabim and Naphtuhim.",
  'explain': ("Egypt’s descendants are peoples, not men: the -im ending is a Hebrew plural, and the table describes nations as one "
   "family. Two of the names differ substantially in Greek, Enemetiim for Anamim and Nephthaliim for Naphtuhim, more than ordinary "
   "spelling; they are kept as the Greek has them."),
  'shared': ["Mizraim had descendants.", "The Ludim and Lehabim are named.", "The Anamim and Naphtuhim, or Enemetiim and Nephthaliim, are named."],
  'instructions': [ins(K, S, "The peoples descended from Egypt are listed as one family.")],
  'entries': ['egypt'],
  'lost': [
   loses("Hebrew Anamim and Naphtuchim appear in Greek as Enemetieim and Nephthalieim, forms that differ beyond routine spelling."),
   between("Latin and King James keep the Hebrew forms. Greek Loudieim keeps the Hebrew plural ending; Acts 17:26 reads the nations as one family."),
  ]},

 '10:14': same_list(
  "Mizraim’s line continues with the Pathrusim, the Casluhim, from whom the Philistines came, and the Caphtorim.",
  ("Egypt’s list closes with the Philistines, Israel’s long enemies, traced here through the Casluhim; Amos says God brought them from "
   "Caphtor, usually identified with Crete. Elsewhere the Greek often calls the Philistines simply foreigners. All versions agree."),
  ["The Pathrusim and Casluhim are named.", "The Philistines came from the Casluhim.", "The Caphtorim are named."],
  "The Philistines are traced to the descendants of Egypt.",
  "Hebrew, Greek, Latin and King James agree. Greek Phylistieim keeps the Hebrew name here where other books have allophyloi. Amos 9:7 and Deuteronomy 2:23 name Caphtor."),

 '10:15': {
  'received': "Canaan was the father of Sidon, his firstborn, and of Heth, the Hittite.",
  'explain': ("Canaan’s line is the peoples of the promised land. Sidon, the Phoenician city, is his firstborn; then Heth, father of the "
   "Hittites from whom Abraham will buy Sarah’s tomb. The Hebrew names Heth as a man; the Greek and Latin give the people, the Hittite. "
   "The rest of the list will follow the Greek pattern of peoples."),
  'shared': ["Canaan had sons.", "Sidon was his firstborn.", "Heth, or the Hittite, is named."],
  'instructions': [ins(K, S, "Sidon and the Hittites descend from Canaan.")],
  'entries': ['canaan'],
  'lost': [
   loses("Hebrew Chet, “Heth,” a personal name, becomes Greek ton Chettaion, “the Hittite,” an ethnic term. The Hebrew name is not in the Greek."),
   between("Latin “the Hittite” follows the Greek; King James “Heth” the Hebrew. Matthew 15:21–28 brings Jesus to Sidon’s region; Genesis 23:10 and 2 Samuel 11:3 name Hittites."),
  ]},

 '10:16': same_list(
  "Canaan’s line includes the Jebusite, the Amorite and the Girgashite.",
  ("Three more peoples of the land. The Jebusites held Jerusalem, then called Jebus, until David took it; God tells Abram his "
   "descendants must wait because the Amorites’ iniquity is not yet full. All versions agree."),
  ["The Jebusite is named.", "The Amorite is named.", "The Girgashite is named."],
  "The Jebusites, Amorites and Girgashites descend from Canaan.",
  "Hebrew, Greek, Latin and King James agree; King James Girgasite is Girgashite. 2 Samuel 5:6–9 and Genesis 15:16 are the later points.",
  entries=['canaan', 'jerusalem']),

 '10:17': {
  'received': "Canaan’s line includes the Hivite, the Arkite and the Sinite.",
  'explain': ("The Hivites will appear as the Gibeonites who trick Joshua and as the family of Shechem; the Arkites and Sinites are "
   "northern Phoenician peoples. The third name differs: Hebrew Sinite, Greek Asennite. The Greek form is kept without claiming a "
   "separate, otherwise unknown tribe."),
  'shared': ["The Hivite is named.", "The Arkite is named.", "A third people, the Sinite or Asennite, is named."],
  'instructions': [ins(K, S, "The Hivites and their neighbours descend from Canaan.")],
  'entries': ['canaan'],
  'lost': [
   loses("Hebrew ha-Sini, “the Sinite,” appears as Greek ton Asennaion, “the Asennite,” a different form of the name."),
   between("Latin and King James read Sinite with the Hebrew. Joshua 9:7 and Genesis 34:2 name Hivites."),
  ]},

 '10:18': {
  'received': "Canaan’s line ends with the Arvadite, the Zemarite and the Hamathite, after which the Canaanite families spread.",
  'explain': ("The last three Canaanite peoples reach north to Hamath on the Orontes, which marks the northern edge of the promised land. "
   "The Hebrew Zemarite is the Greek Samarean, a form that should not be confused with the later Samaria. Then the families, or in "
   "Greek the tribes, of Canaan spread abroad, as Noah’s sons did in 9:19."),
  'shared': ["The Arvadite and Hamathite are named.", "A people called Zemarite or Samarean is named.", "Afterward the Canaanite families spread."],
  'instructions': [ins(K, S, "The Canaanite peoples spread through the land after their founding.")],
  'entries': ['canaan'],
  'lost': [
   loses("Hebrew ha-Tsemari, “the Zemarite,” becomes Greek ton Samaraion, “the Samarean”; Hebrew mishpechot, “families,” is Greek phylai, “tribes.”"),
   between("Latin “Zemarite … peoples” and King James “Zemarite … families” follow the Hebrew. Greek diesparēsan, “scattered,” is the verb of 9:19 and 10:32; Numbers 34:8 names the entrance of Hamath."),
  ]},

 '10:19': {
  'received': "The Canaanite territory ran from Sidon toward Gerar and Gaza, and toward Sodom, Gomorrah, Admah and Zeboiim as far as Lasha.",
  'explain': ("The borders of Canaan are drawn from Sidon in the north down the coast to Gaza, then across to the cities of the plain. "
   "Sodom appears here only as a border town; its fall in chapter 19 becomes the Bible’s example of sudden judgement. The named limits "
   "agree in all versions; only the boundary formula differs."),
  'shared': ["The Canaanite border began at Sidon.", "It ran toward Gerar and as far as Gaza.", "It reached toward Sodom, Gomorrah, Admah and Zeboiim, as far as Lasha."],
  'instructions': [ins(K, S, "The land of Canaan stretched from Sidon to Gaza and the cities of the plain.")],
  'entries': ['canaan'],
  'lost': [between("Hebrew bo’akhah, “as you go toward,” is Greek heōs elthein, “as far as”; the names are the same in all four. King James “as thou comest … as thou goest” keeps the Hebrew idiom. Genesis 19:24 and Hosea 11:8 take up Sodom and Admah.")]},

 '10:20': {
  'received': "These are the sons of Ham, by their families, languages, lands and nations.",
  'explain': ("Ham’s section closes with the formula of verse 5. The Hebrew says families, the Greek tribes; the Latin adds generations "
   "to the list. The difference is in how the groupings are named, not in any added or missing branch of Ham’s line."),
  'shared': ["These are the sons of Ham.", "They are grouped by families and languages.", "They are grouped by lands and nations."],
  'instructions': [ins(K, S, "Ham’s descendants are summed up by family, language, land and nation.")],
  'entries': [],
  'lost': [between("Hebrew mishpechot, “families,” is Greek phylai, “tribes”; Latin adds “generations”; King James “families … tongues … countries … nations” follows the Hebrew.")]},

 '10:21': {
  'received': "Sons were also born to Shem, the father of all the children of Eber and the brother of Japheth the elder.",
  'explain': ("Shem comes last, as the line the story will follow. He is honoured as the father of all the sons of Eber, from whose name "
   "the word Hebrew is traced. The Hebrew can be read as making Shem the elder brother of Japheth or Japheth the elder; the Greek and "
   "King James read Japheth as elder, the Latin Shem."),
  'shared': ["Sons were born to Shem.", "He is the father of all the sons of Eber.", "He is related to Japheth as brother, one of them the elder."],
  'instructions': [ins(K, S, "Shem is the ancestor of Eber and so of the Hebrews."), ins(W, R, "The chosen line is listed last and introduced by its descendant Eber; the table already leans toward Abraham.")],
  'entries': [],
  'lost': [between("Hebrew achi Yefet ha-gadol can mean “brother of Japheth the elder” or “elder brother of Japheth”; Greek adelphos Iapheth tou meizonos reads Japheth as elder, as King James does, while the Latin fratris Iapheth maior reads Shem as elder. Greek Eber is Hebrew Ever; Genesis 14:13 first calls Abram a Hebrew.")]},

 '10:22': {
  'received': "The sons of Shem are Elam, Asshur, Arpachshad, Lud and Aram.",
  'explain': ("Shem’s sons are the peoples of the east: Elam beyond Babylon, Asshur, Arpachshad, Lud and Aram, the Syrians. The Hebrew, "
   "Latin and King James give five; the Greek gives six, adding Cainan at this level, a different placement from the Cainan it also adds "
   "between Arpachshad and Shelah in verse 24. The Hebrew form of the third name is Arpachshad; Arphaxad is the Greek form."),
  'shared': ["These are the sons of Shem.", "Elam, Asshur and Arpachshad are named.", "Lud and Aram are named."],
  'instructions': [ins(K, S, "Shem’s sons are the peoples of the east, including Aram and Asshur.")],
  'entries': [],
  'lost': [
   keeps("An added kai Kainan, “and Cainan,” as a sixth son of Shem; the Hebrew has five. This Cainan is distinct from the one the Greek inserts in 10:24 and 11:12–13 between Arphaxad and Shelah."),
   between("Latin and King James give the five of the Hebrew. Acts 2:9 hears Elamites at Pentecost; Luke 3:36 includes Cainan from the Greek."),
  ]},

 '10:23': {
  'received': "The sons of Aram are Uz, Hul, Gether and Mash.",
  'explain': ("Aram’s four sons are the Aramean peoples; Job will live in the land of Uz. The fourth name differs: Hebrew Mash, Greek "
   "Meshech, the name also borne by a son of Japheth in verse 2. No particular scribal cause is established."),
  'shared': ["These are the sons of Aram.", "Uz, Hul and Gether are named.", "A fourth, Mash or Meshech, is named."],
  'instructions': [ins(K, S, "The Aramean peoples descend from Shem through Aram.")],
  'entries': [],
  'lost': [
   loses("Hebrew Mash becomes Greek Mosoch, “Meshech,” coinciding with the Japhethite name of 10:2; the Hebrew form is gone."),
   between("Latin and King James read Mash with the Hebrew. Job 1:1 places Job in Uz."),
  ]},

 '10:24': {
  'received': "Arpachshad was the ancestor of Shelah, and Shelah the father of Eber.",
  'explain': ("The line narrows toward Eber. The Hebrew, Latin and King James run Arpachshad, Shelah, Eber; the Greek inserts a generation, "
   "Arpachshad, Cainan, Shelah, Eber, as it does again with years in 11:12–13. This changes the genealogy, not only its wording. Luke’s "
   "genealogy of Jesus includes this Cainan, following the Greek."),
  'shared': ["Arpachshad is the ancestor of Shelah.", "Shelah begat Eber.", "The line runs toward the Hebrews."],
  'instructions': [ins(K, S, "The line from Shem to Eber runs through Arpachshad and Shelah.")],
  'entries': [],
  'lost': [
   keeps("An added egennēsen ton Kainan, kai Kainan egennēsen, “begat Cainan, and Cainan begat,” a generation absent from the Hebrew; the same Cainan appears with ages in 11:12–13 and in Luke 3:36."),
   between("Latin “Arpachshad fathered Shelah, from whom Eber was born” and King James “Arphaxad begat Salah; and Salah begat Eber” follow the Hebrew."),
  ]},

 '10:25': same_list(
  "Eber had two sons, Peleg, in whose days the earth was divided, and Joktan.",
  ("Eber’s two sons part the line. Peleg means division, and the verse explains it: in his days the earth was divided, read as the "
   "scattering at Babel or as a splitting of lands. Joktan’s sons will be the peoples of Arabia; Peleg’s line will lead to Abram. "
   "All versions agree."),
  ["Eber had two sons.", "Peleg was named for the division of the earth in his days.", "His brother was Joktan."],
  "Peleg’s name records the division of the earth.",
  "Hebrew, Greek, Latin and King James agree; Greek Phalek is Hebrew Peleg. Genesis 11:9 and Luke 3:35 carry the name on.",
  wisdom="A name can hold a whole event; Peleg’s does, and his line is the one that continues."),

 '10:26': same_list(
  "Joktan was the father of Almodad, Sheleph, Hazarmaveth and Jerah.",
  ("Joktan’s thirteen sons, beginning here, are peoples of Arabia; Arab genealogists later called him Qahtan, ancestor of the south "
   "Arabians. Hazarmaveth, “court of death,” survives as Hadramaut, a region of the south. All versions agree."),
  ["Joktan had sons.", "Almodad and Sheleph are named.", "Hazarmaveth and Jerah are named."],
  "Joktan’s sons are the peoples of Arabia.",
  "Hebrew, Greek, Latin and King James agree; Greek Asarmōth is Hebrew Chatsarmavet."),

 '10:27': {
  'received': "Joktan’s sons continue with Hadoram, Uzal and Diklah.",
  'explain': ("Three more Arabian peoples. Diklah is the Hebrew for a date palm, fitting a people of the oases. The middle name differs: "
   "Hebrew Uzal, Greek Aizel, a difference in the transmitted form that does not make two separate people."),
  'shared': ["Hadoram is named.", "A son called Uzal or Aizel is named.", "Diklah is named."],
  'instructions': [ins(K, S, "Joktan’s line continues among the peoples of Arabia.")],
  'entries': [],
  'lost': [
   loses("Hebrew Uzal appears in Greek as Aizēl, a different form of the name."),
   between("Latin and King James read Uzal with the Hebrew. Greek Dekla is Hebrew Diqlah, “date palm.”"),
  ]},

 '10:28': {
  'received': "Joktan’s sons continue with Obal, Abimael and Sheba.",
  'explain': ("Two or three names, depending on the column. The Hebrew, Latin and King James list Obal, Abimael and Sheba; the Greek main "
   "text has no name at Obal’s place and gives Abimael and Sheba only. The shorter list is noted as such, without guessing which name "
   "fell out or whether one was ever there. Abimael is often read as “my father is God.”"),
  'shared': ["Abimael is named.", "Sheba is named.", "These are Joktan’s sons."],
  'instructions': [ins(K, S, "Joktan’s sons include Abimael and Sheba.")],
  'entries': [],
  'lost': [
   loses("Hebrew Oval, “Obal” (Latin Ebal), has no counterpart in the Greek main text, which passes from 10:27 straight to Abimael. The Hebrew name is absent."),
   between("Latin Ebal and King James Obal keep a name at the head of the verse with the Hebrew. Greek Abimeēl is Hebrew Avima’el."),
  ]},

 '10:29': same_list(
  "Joktan’s sons end with Ophir, Havilah and Jobab.",
  ("The last three of Joktan’s sons. Ophir is the land famous for gold, from which Solomon’s fleets will bring it; Havilah shares its "
   "name with a son of Cush in verse 7 and the gold land of 2:11. All versions agree and close the list."),
  ["Ophir and Havilah are named.", "Jobab is named.", "All these are the sons of Joktan."],
  "Joktan’s thirteen sons are the Arabian peoples, among them Ophir of the gold.",
  "Hebrew, Greek, Latin and King James agree. 1 Kings 9:28 and 1 Chronicles 29:4 bring gold from Ophir."),

 '10:30': {
  'received': "Their dwelling stretched from Mesha toward Sephar, the mountain of the east.",
  'explain': ("Joktan’s peoples are placed from Mesha to Sephar, the eastern mountain; both places are in Arabia and neither is certainly "
   "identified. The Hebrew says toward Sephar, the Greek as far as Sephar; the range is the same."),
  'shared': ["Their dwelling began at Mesha.", "It extended toward Sephar.", "Sephar is the mountain of the east."],
  'instructions': [ins(K, S, "The Joktanite peoples lived between Mesha and Sephar in the east.")],
  'entries': [],
  'lost': [between("Hebrew bo’akhah Sefarah, “as you go toward Sephar,” is Greek heōs Sōphēra, “as far as Sephar”; Hebrew har ha-qedem, “the mountain of the east,” is Greek oros anatolōn, “a mountain of the east.” Latin and King James follow the Hebrew idiom.")]},

 '10:31': {
  'received': "These are the sons of Shem, by their families, languages, lands and nations.",
  'explain': ("Shem’s section closes with the formula of verses 5 and 20: families or tribes, languages, lands, nations. The Greek word for "
   "nations is the word the New Testament uses for Gentiles, the nations Jesus sends his disciples to. The Latin says regions among their "
   "nations."),
  'shared': ["These are the sons of Shem.", "They are grouped by families and languages.", "They are grouped by lands and nations."],
  'instructions': [ins(K, S, "Shem’s descendants are summed up by family, language, land and nation.")],
  'entries': [],
  'lost': [between("Hebrew mishpechot is again Greek phylai, “tribes”; Latin “regions” for lands. Greek ethnē, “nations,” is the word of Matthew 28:19 and Galatians 3:8.")]},

 '10:32': {
  'received': "These are the families of Noah’s sons by their generations and nations; from them the nations spread over the earth after the flood.",
  'explain': ("The table closes as it opened, with the families of Noah’s sons and their spreading after the flood. The Hebrew says the "
   "nations were separated on the earth; the Greek says the islands of the nations were dispersed, bringing back the islands of verse 5. "
   "From the Greek verb comes diaspora, the scattering of a people. The next chapter will tell how the scattering happened."),
  'shared': ["These are the families of Noah’s sons.", "They are listed by generations and nations.", "From them the nations spread over the earth after the flood."],
  'instructions': [ins(K, S, "All the nations spread from Noah’s sons after the flood."), ins(W, R, "The chapter ends with dispersal as a plain fact; Babel will show the pride behind it, and Pentecost will gather the languages again.")],
  'entries': ['noah'],
  'lost': [
   loses("Hebrew nifredu ha-goyim, “the nations were separated,” becomes Greek diesparēsan nēsoi tōn ethnōn, “the islands of the nations were dispersed”; the Greek adds “islands” and changes the verb. Hebrew mishpechot is phylai, “tribes.”"),
   keeps("Greek diesparēsan, “were dispersed,” is the root of diaspora, the word of James 1:1 and 1 Peter 1:1; the Greek ties the spread of the nations to the later scattering of Israel."),
   between("Latin “Noah’s families according to their peoples and nations … the nations were divided” and King James “families of the sons of Noah … the nations divided” follow the Hebrew."),
  ]},
 }
}
