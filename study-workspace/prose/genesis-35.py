# Study prose for Genesis 35 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 35,
 'chapterNote': (
  "Return to Bethel, the vow paid, the name Israel confirmed, Rachel’s death at Benjamin’s birth, Reuben’s sin, the twelve sons, and Isaac’s death. The columns "
  "agree on the events; the Hebrew keeps “I will make an altar,” the gods “hidden” under the terebinth, El-bethel, Allon-bacuth and Ben-oni as names, “so He named "
  "him Israel,” El Shaddai, “a nation and an assembly,” “I will give” the land, Migdal-eder after Rachel’s burial, and “Israel heard of it” without comment. The "
  "Greek keeps “let us make an altar … who preserved me,” the gods “destroyed to this day,” “Israel set out from Shechem,” Bethel without El, “Oak of Mourning” "
  "named by Jacob, Luz named at the second theophany, “Your name is Jacob” without the closing confirmation, “I am your God,” “nations and assemblies,” “I have "
  "given it; it shall be yours,” Chabratha, the Tower of Gader placed before Rachel’s labour, “it seemed evil to him” of Reuben, “the city of the plain,” and "
  "“in which he lived” of Isaac’s years. The Latin and King James follow the Hebrew; the Latin dates the journey to springtime and glosses both of Benjamin’s "
  "names. Two Hebrew-column renderings were corrected today."),
 'verses': {

 '35:1': {
  'received': "God told Jacob to go up to Bethel, settle there, and build an altar to the God who appeared to him when he fled from Esau.",
  'explain': ("After Shechem, God sends Jacob back to the beginning. The altar vowed in 28:22 is now commanded. The versions agree."),
  'shared': ["Arise, go up to Bethel and settle there.", "Make an altar there to God.", "He appeared to you when you fled from your brother Esau."],
  'instructions': [ins(C, S, "Go up to Bethel, dwell there, and make an altar to the God who appeared to you."), ins(W, R, "God reminds Jacob of the vow by reminding him of the flight; the unpaid promise is called in after the shame of Shechem, and Jacob goes.")],
  'entries': ['jacob', 'bethel', 'elohim', 'altar'],
  'lost': [AGREE]},

 '35:2': {
  'received': "Jacob told his household to put away their foreign gods, purify themselves and change their clothes.",
  'explain': ("Foreign gods: Laban’s teraphim, Shechem’s spoil. Purification and new garments before approaching God, as at Sinai. The Greek adds and all who were with him, the captives of 34:29."),
  'shared': ["Jacob spoke to his household and all with him.", "Put away the foreign gods among you.", "Purify yourselves and change your garments."],
  'instructions': [ins(C, S, "Put away the foreign gods, purify yourselves, and change your garments."), ins(W, R, "The first purification in Scripture: gods out, bodies washed, clothes changed. Jacob prepares his house to meet God as a priest would, and the chapter is the nearest Genesis comes to liturgy.")],
  'entries': ['jacob', 'gods'],
  'lost': [keeps("Greek kai pasin tois met’ autou, “and to all who were with him,” for Hebrew ve-el kol-asher immo, “and to all who were with him,” present in both; the Latin “called together his whole household” drops it."), between("King James “and to all that were with him.”")]},

 '35:3': {
  'received': "Let us go up to Bethel; I will make an altar to the God who answered me in my distress and was with me on my way.",
  'explain': ("Jacob confesses what God did: answered, was with me. The Hebrew says I will make; the Greek let us make, and adds preserved me; the Latin let us make, accompanied me."),
  'shared': ["Let us arise and go up to Bethel.", "I will make an altar there to God.", "He answered me in the day of my distress and was with me on the road I travelled."],
  'instructions': [ins(K, S, "Jacob led his household to Bethel to pay his vow."), ins(W, R, "“The God who answered me in the day of my distress”: twenty years later Jacob names the God of the stone pillow by what He did, which is how the vow is paid.")],
  'entries': ['jacob', 'bethel', 'elohim'],
  'lost': [keeps("Greek poiēsōmen, “let us make,” for Hebrew ve-e‘eseh, “and I will make,” and an added kai diesōsen me, “and preserved me.”"), between("Latin “so that we may make an altar … accompanied me” follows the Greek’s plural; King James “I will make there an altar.”")]},

 '35:4': {
  'received': "They gave Jacob their foreign gods and earrings, and he hid them under the terebinth near Shechem.",
  'explain': ("Earrings as amulets, buried with the gods under the oak of Shechem where Abraham built an altar. The Hebrew says hid; the Greek adds and destroyed them to this day; the Latin buried, behind the city."),
  'shared': ["They gave Jacob all the foreign gods they had.", "They gave the rings in their ears.", "Jacob hid them under the terebinth near Shechem."],
  'instructions': [ins(K, S, "The household’s idols were buried at Shechem."), ins(W, R, "Rachel’s stolen gods go into the ground under the tree; the family leaves Haran behind at last, twenty years after leaving it.")],
  'entries': ['jacob'],
  'lost': [keeps("An added kai apōlesen auta heōs tēs sēmeron hēmeras, “and destroyed them to this day,” in the Greek after hiding them."), between("Hebrew va-yitmon, “hid,” Latin “buried,” King James “hid” without the addition.")]},

 '35:5': {
  'received': "As they journeyed, the terror of God fell on the cities around, so none pursued Jacob’s sons.",
  'explain': ("The fear Jacob felt in 34:30 is answered: God’s terror protects the murderers’ family. The Greek names Israel setting out from Shechem and the sons of Israel; the Hebrew they, Jacob’s sons."),
  'shared': ["They set out.", "A terror from God fell on the surrounding cities.", "They did not pursue Jacob’s sons."],
  'instructions': [ins(K, S, "God’s terror protected Jacob’s household from reprisal."), ins(W, R, "Jacob feared the Canaanites would gather against him; God sends dread instead. Grace covers the family’s worst act without approving it.")],
  'entries': ['jacob', 'elohim'],
  'lost': [keeps("An added exēren de Israēl ek Sikimōn, “Israel set out from Shechem,” and tōn huiōn Israēl, “the sons of Israel,” for Hebrew bene Ya‘aqov, “the sons of Jacob.”"), between("Latin “When they set out … pursue them” and King James “they journeyed … the sons of Jacob” follow the Hebrew.")]},

 '35:6': {
  'received': "Jacob came to Luz, that is Bethel, in Canaan, with all his people.",
  'explain': ("The place of the stairway, named twice. The versions agree."),
  'shared': ["Jacob came to Luz, which is Bethel.", "It is in the land of Canaan.", "He and all the people with him came."],
  'instructions': [ins(K, S, "Jacob reached Bethel with his household.")],
  'entries': ['jacob', 'bethel', 'canaan'],
  'lost': [AGREE]},

 '35:7': {
  'received': "He built an altar and named the place El-bethel, because God had revealed Himself to him there when he fled from his brother.",
  'explain': ("El-bethel, God of Bethel, the altar named for the God of the place. The Hebrew says El-bethel, revealed Himself, a plural verb; the Greek Bethel, appeared, and names Esau; the Latin House of God."),
  'shared': ["He built an altar there.", "He named the place for God and Bethel.", "God had appeared to him there when he fled from his brother."],
  'instructions': [ins(K, S, "Jacob built the altar at Bethel and named it."), ins(W, R, "The vow of 28:22 is paid: an altar where the stone was. Twenty years between promise and payment, and God waited.")],
  'entries': ['jacob', 'bethel', 'altar', 'elohim'],
  'lost': [loses("Hebrew El Bet-El, “God of Bethel,” becomes Greek Baithēl, “Bethel,” without El; Hebrew niglu elav ha-Elohim, “God revealed Himself,” plural verb, is Greek ephanē autō ho theos; Greek adds Ēsau, “Esau.”"), between("Latin “House of God” translates; King James “Elbethel.”")]},

 '35:8': {
  'received': "Deborah, Rebekah’s nurse, died and was buried below Bethel under the oak, which was named Allon-bacuth.",
  'explain': ("Deborah, the nurse of 24:59 whom the Greek omitted there, dies in Jacob’s camp; Rebekah herself is never said to have died. The Hebrew says buried, Allon-bacuth; the Greek Jacob named it Oak of Mourning, without the burial verb; the Latin Oak of Weeping."),
  'shared': ["Deborah, Rebekah’s nurse, died.", "She was buried below Bethel under the oak.", "It was named Oak of Weeping."],
  'instructions': [ins(K, S, "Rebekah’s nurse Deborah died at Bethel."), ins(W, R, "The old nurse dies in the camp of the son her mistress never saw again; the mourning for Deborah is the only mourning Genesis gives Rebekah.")],
  'entries': ['rebekah', 'bethel'],
  'lost': [loses("Hebrew va-tiqqaver, “and was buried,” is absent from the Greek; Hebrew Allon Bakhut, a name, becomes Greek Balanos penthous, “Oak of Mourning,” with Iakōb added as namer."), between("Latin “was buried … Oak of Weeping” and King James “was buried … Allonbachuth” keep the burial.")]},

 '35:9': {
  'received': "God appeared to Jacob again on his return from Paddan-aram and blessed him.",
  'explain': ("The second Bethel theophany. The Greek adds in Luz and repeats God; the Latin Mesopotamia of Syria."),
  'shared': ["God appeared to Jacob again.", "He had come from Paddan-aram.", "God blessed him."],
  'instructions': [ins(K, S, "God appeared to Jacob a second time at Bethel.")],
  'entries': ['jacob', 'elohim', 'haran'],
  'lost': [keeps("An added en Louza, “in Luz,” and a repeated ho theos in the Greek."), between("Hebrew Paddan Aram is Latin and Greek “Mesopotamia of Syria,” King James “Padanaram.”")]},

 '35:10': {
  'received': "God said, Your name is Jacob; no longer Jacob but Israel shall be your name. So He named him Israel.",
  'explain': ("The Jabbok name confirmed by God in daylight. The Hebrew ends so He named him Israel; the Greek lacks that and opens your name is Jacob; the Latin lacks the opening and has He called him Israel."),
  'shared': ["Your name is Jacob.", "No longer shall your name be Jacob, but Israel.", "He named him Israel."],
  'instructions': [ins(K, S, "God confirmed the name Israel."), ins(W, R, "The name given by a stranger at night is ratified by God at Bethel; what Jacob won by wrestling is given again as gift.")],
  'entries': ['jacob', 'elohim'],
  'lost': [loses("Hebrew va-yiqra et-shemo Yisra’el, “and He called his name Israel,” is absent from the Greek, which keeps the opening to onoma sou Iakōb, “your name is Jacob.”"), between("Latin lacks “Your name is Jacob” and has “He called him Israel”; King James has both clauses.")]},

 '35:11': {
  'received': "I am El Shaddai: be fruitful and multiply; a nation and a company of nations shall come from you, and kings from your loins.",
  'explain': ("The blessing of 17:6 and 28:3 to Jacob, with kings. The Hebrew says El Shaddai, a nation and an assembly; the Greek I am your God, nations and assemblies; the Latin God Almighty, nations and peoples."),
  'shared': ["I am God Almighty.", "Be fruitful and multiply; a nation and an assembly of nations shall come from you.", "Kings shall come from your loins."],
  'instructions': [ins(K, S, "God promised Jacob nations and kings."), ins(W, R, "Kings from Jacob’s loins: the promise reaches past the tribes to David. The man who called his brother “my lord” is told he will father lords.")],
  'entries': ['el-shaddai', 'jacob'],
  'lost': [loses("Hebrew El Shaddai becomes Greek ho theos sou, “your God”; Hebrew goy u-qehal goyim, “a nation and an assembly of nations,” becomes ethnē kai synagōgai ethnōn, “nations and assemblies of nations.”"), between("Latin “God Almighty … nations and peoples of nations” and King James “God Almighty … a nation and a company of nations” keep the name.")]},

 '35:12': {
  'received': "The land I gave Abraham and Isaac I will give to you and your seed after you.",
  'explain': ("The land, third generation. The Hebrew says I will give to you; the Greek I have given to you; it shall be yours; the Latin and King James will give."),
  'shared': ["The land I gave to Abraham and Isaac.", "I will give it to you.", "I will give the land to your seed after you."],
  'instructions': [ins(K, S, "God confirmed the land to Jacob and his seed."), ins(W, R, "Abraham, Isaac, Jacob: the land is given three times to men who never possess it. The promise is the inheritance, and the inheritance waits.")],
  'entries': ['abraham', 'isaac', 'jacob'],
  'lost': [keeps("Greek soi dedōka autēn, soi estai, “to you I have given it, it shall be yours,” for Hebrew lekha ettenennah, “to you I will give it.”"), between("Latin and King James “I will give.”")]},

 '35:13': {
  'received': "God went up from him at the place where He had spoken.",
  'explain': ("The theophany ends. The Latin compresses to He departed from him."),
  'shared': ["God went up from him.", "It was at the place.", "There He had spoken with him."],
  'instructions': [ins(K, S, "The vision ended.")],
  'entries': ['elohim'],
  'lost': [between("Latin “And He departed from him” drops the place; Hebrew, Greek and King James “went up from him in the place where he talked with him.”")]},

 '35:14': {
  'received': "Jacob set up a stone pillar where God had spoken, and poured a drink offering and oil on it.",
  'explain': ("A second pillar at Bethel, with a libation, the first drink offering in Scripture, and oil as in 28:18. The versions agree."),
  'shared': ["Jacob set up a pillar of stone where God had spoken with him.", "He poured out a drink offering on it.", "He poured oil on it."],
  'instructions': [ins(K, S, "Jacob consecrated a pillar with wine and oil."), ins(W, R, "Oil as before and now wine as well: Jacob has more to pour than he had with a stone for a pillow, and gives it.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '35:15': {
  'received': "Jacob named the place where God spoke to him Bethel.",
  'explain': ("The name confirmed. The versions agree."),
  'shared': ["Jacob named the place.", "God had spoken with him there.", "He named it Bethel."],
  'instructions': [ins(K, S, "Bethel was named again.")],
  'entries': ['jacob', 'bethel'],
  'lost': [AGREE]},

 '35:16': {
  'received': "They left Bethel, and some way short of Ephrath Rachel went into hard labour.",
  'explain': ("Rachel’s prayer for another son is answered on the road. The Hebrew says a stretch of land still to Ephrath; the Greek Chabratha, reading the Hebrew word as a place; the Latin in springtime. The Greek verse is split for alignment, its first half standing at the reader’s 35:21."),
  'shared': ["They journeyed from Bethel.", "There was still some distance to Ephrath.", "Rachel went into labour, and it was hard."],
  'instructions': [ins(K, S, "Rachel’s labour began on the road to Ephrath."), ins(W, R, "“May the Lord add to me another son,” she said at Joseph’s birth; the addition comes on a road, and costs her everything.")],
  'entries': [],
  'lost': [loses("Hebrew kivrat-ha-aretz, “a stretch of the land,” a measure of distance, becomes Greek Chabratha, a place name."), between("Latin “in springtime came to the land leading to Ephrath” reads the word as a season; King James “but a little way to come to Ephrath.”")]},

 '35:17': {
  'received': "In her hard labour the midwife said, Do not fear, you have another son.",
  'explain': ("The midwife’s comfort: another son, as Rachel asked. The Hebrew says do not fear; the Greek take courage; the Latin adds she began to be in danger."),
  'shared': ["Her labour was difficult.", "The midwife spoke to her.", "Do not fear, for this is also a son for you."],
  'instructions': [ins(K, S, "The midwife told Rachel she had a second son.")],
  'entries': [],
  'lost': [between("Hebrew al-tir’i, “do not fear,” is Greek tharsei, “take courage”; Latin “Do not fear … she began to be in danger”; King James “Fear not.”")]},

 '35:18': {
  'received': "As she died she named him Ben-oni, but his father called him Benjamin.",
  'explain': ("Ben-oni, son of my sorrow; Benjamin, son of the right hand, or of the south. The Hebrew keeps Ben-oni; the Greek translates Son of My Sorrow; the Latin gives both names with both meanings."),
  'shared': ["Her life was departing, for she was dying.", "She named him Ben-oni.", "His father named him Benjamin."],
  'instructions': [ins(K, S, "Rachel died naming Benjamin."), ins(W, R, "Two names for one child: the mother’s grief and the father’s hope. Jacob overrules the dying name, and the son of sorrow grows up as the son of the right hand.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew Ben-Oni, a name, becomes Greek Huios odynēs mou, “Son of my sorrow,” a translation; Benjamin is kept as Beniamin."), between("Latin “Benoni, that is, Son of My Sorrow … Benjamin, that is, Son of the Right Hand” glosses both; King James “Benoni … Benjamin.”")]},

 '35:19': {
  'received': "Rachel died and was buried on the way to Ephrath, that is, Bethlehem.",
  'explain': ("Not at Machpelah with the family but by the road, where her tomb is still shown. Bethlehem, named for the first time. The versions agree."),
  'shared': ["Rachel died.", "She was buried on the way to Ephrath.", "That is Bethlehem."],
  'instructions': [ins(K, S, "Rachel was buried near Bethlehem."), ins(W, R, "The beloved wife is buried by the roadside at Bethlehem, where Jeremiah will hear her weeping for her children and Matthew will hear it again.")],
  'entries': [],
  'lost': [AGREE]},

 '35:20': {
  'received': "Jacob set a pillar on her grave, which stands to this day.",
  'explain': ("A third pillar, this one a grave marker. The Hebrew says Rachel’s grave; the Greek Rachel’s monument. The Hebrew-column rendering was corrected today."),
  'shared': ["Jacob set up a pillar over her grave.", "It is the pillar of Rachel’s grave.", "It stands to this day."],
  'instructions': [ins(K, S, "Jacob marked Rachel’s grave with a pillar.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew matzevet qevurat-Rachel, “the pillar of Rachel’s grave,” is Greek stēlē mnēmeiou Rhachēl, “the pillar of Rachel’s monument”; Latin “Rachel’s tomb,” King James “Rachel’s grave.”")]},

 '35:21': {
  'received': "Israel journeyed on and pitched his tent beyond Migdal-eder.",
  'explain': ("Migdal-eder, the tower of the flock, near Bethlehem. The Hebrew places this after Rachel’s burial and calls him Israel; the Greek has it before her labour, at its 35:16a, and says Jacob departed from Bethel, the Tower of Gader; the Latin the Tower of the Flock."),
  'shared': ["Israel journeyed.", "He pitched his tent.", "It was beyond the tower of the flock."],
  'instructions': [ins(K, S, "Israel camped beyond Migdal-eder.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew Yisra’el … Migdal-Eder, “Israel … Tower of the Flock,” becomes Greek Iakōb … pyrgou Gader, “Jacob … Tower of Gader,” placed before Rachel’s labour as 35:16a."), between("Latin “the Tower of the Flock” translates; King James “Israel … the tower of Edar.”")]},

 '35:22a': {
  'received': "While Israel lived there, Reuben lay with Bilhah, his father’s concubine, and Israel heard of it.",
  'explain': ("The firstborn’s crime, told in one sentence; 49:4 is the verdict. The Hebrew says only Israel heard; the Greek adds and it seemed evil to him; the Latin did not escape his father’s knowledge. The Hebrew text has a break here, as if something were left unsaid."),
  'shared': ["Israel was living in that land.", "Reuben went and lay with Bilhah, his father’s concubine.", "Israel heard of it."],
  'instructions': [ins(K, S, "Reuben lay with Bilhah and Israel heard."), ins(W, R, "“And Israel heard”: the Hebrew stops there, and the silence is Jacob’s again. The Greek supplies the judgment the Hebrew withholds until the deathbed.")],
  'entries': ['jacob'],
  'lost': [keeps("An added kai ponēron ephanē enantion autou, “and it seemed evil before him,” in the Greek after Israel heard."), between("Latin “this did not escape his father’s knowledge” paraphrases; King James “and Israel heard it.”")]},

 '35:22b': {
  'received': "Now Jacob’s sons were twelve.",
  'explain': ("The list begins; the a/b division is editorial, for alignment. The versions agree."),
  'shared': ["Jacob’s sons.", "They were twelve.", "The list follows."],
  'instructions': [ins(K, S, "Jacob had twelve sons.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '35:23': {
  'received': "Leah’s sons: Reuben the firstborn, Simeon, Levi, Judah, Issachar and Zebulun.",
  'explain': ("Six by Leah. The versions agree."),
  'shared': ["The sons of Leah.", "Reuben, Jacob’s firstborn.", "Simeon, Levi, Judah, Issachar and Zebulun."],
  'instructions': [ins(K, S, "Leah bore six sons.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '35:24': {
  'received': "Rachel’s sons: Joseph and Benjamin.",
  'explain': ("Two by Rachel. The versions agree."),
  'shared': ["The sons of Rachel.", "Joseph.", "Benjamin."],
  'instructions': [ins(K, S, "Rachel bore Joseph and Benjamin.")],
  'entries': [],
  'lost': [AGREE]},

 '35:25': {
  'received': "Bilhah’s sons: Dan and Naphtali.",
  'explain': ("Two by Rachel’s maid. The versions agree."),
  'shared': ["The sons of Bilhah, Rachel’s maid.", "Dan.", "Naphtali."],
  'instructions': [ins(K, S, "Bilhah bore Dan and Naphtali.")],
  'entries': [],
  'lost': [AGREE]},

 '35:26': {
  'received': "Zilpah’s sons: Gad and Asher. These are Jacob’s sons born in Paddan-aram.",
  'explain': ("Two by Leah’s maid; twelve. Born in Paddan-aram is a summary that overlooks Benjamin, born in Canaan. The Greek and Latin say Mesopotamia of Syria."),
  'shared': ["The sons of Zilpah, Leah’s maid: Gad and Asher.", "These are the sons of Jacob.", "They were born to him in Paddan-aram."],
  'instructions': [ins(K, S, "The twelve sons are listed by their mothers."), ins(W, R, "Twelve sons by four women, listed by mother; the tribes carry the rivalries of the tents into their very order.")],
  'entries': ['jacob', 'haran'],
  'lost': [between("Hebrew Paddan Aram is Greek Mesopotamia tēs Syrias, Latin “Mesopotamia of Syria,” King James “Padanaram.”")]},

 '35:27': {
  'received': "Jacob came to his father Isaac at Mamre, Kiriath-arba, that is Hebron, where Abraham and Isaac had sojourned.",
  'explain': ("Home at last, to the blind father who thought he was dying in chapter 27. The Hebrew says Kiriath-arba; the Greek the city of the plain, in the land of Canaan; the Latin the city of Arba."),
  'shared': ["Jacob came to Isaac his father at Mamre.", "That is Hebron.", "Abraham and Isaac had sojourned there."],
  'instructions': [ins(K, S, "Jacob returned to Isaac at Hebron."), ins(W, R, "Isaac, who did not know the day of his death, has lived to see the son he blessed by mistake come home with twelve sons; the return is told in a verse.")],
  'entries': ['jacob', 'isaac', 'hebron', 'abraham', 'canaan'],
  'lost': [loses("Hebrew Qiryat ha-Arba, “Kiriath-arba,” becomes Greek polin tou pediou, “the city of the plain,” and the Greek adds en gē Chanaan, “in the land of Canaan.”"), between("Latin “the city of Arba” and King James “the city of Arbah” keep the name.")]},

 '35:28': {
  'received': "Isaac lived a hundred and eighty years.",
  'explain': ("Longer than Abraham or Jacob. The Greek adds in which he lived; the Latin completed. The Hebrew-column rendering was corrected today."),
  'shared': ["The days of Isaac.", "They were a hundred and eighty years.", "His life is summed up."],
  'instructions': [ins(K, S, "Isaac died at a hundred and eighty.")],
  'entries': ['isaac'],
  'lost': [keeps("An added has ezēsen, “which he lived,” in the Greek."), between("Hebrew va-yihyu yeme Yitzchaq, “the days of Isaac were”; Latin “Isaac’s days were completed”; King James “the days of Isaac were.”")]},

 '35:29': {
  'received': "Isaac breathed his last, old and full of days, and was gathered to his people; Esau and Jacob buried him.",
  'explain': ("The formula of Abraham’s death. Esau and Jacob together at the grave, as Isaac and Ishmael were; Isaac’s death is told here though he lives, by the dates, into Joseph’s Egyptian years. The Greek says his strength failed, added to his family; the Latin worn out with age."),
  'shared': ["Isaac breathed his last and died.", "He was gathered to his people, old and full of days.", "His sons Esau and Jacob buried him."],
  'instructions': [ins(K, S, "Esau and Jacob buried Isaac."), ins(W, R, "Esau first, then Jacob, at their father’s grave: the brothers who fought from the womb stand together once more, and the story of Isaac ends in peace between his sons.")],
  'entries': ['isaac', 'jacob'],
  'lost': [between("Hebrew va-yigva, “he expired,” is Greek eklipōn, “failing”; Hebrew el-ammav, “to his peoples,” is Greek pros to genos autou, “to his family”; Latin “worn out with age … joined to his people”; King James “gave up the ghost … gathered unto his people.”")]},
 }
}
