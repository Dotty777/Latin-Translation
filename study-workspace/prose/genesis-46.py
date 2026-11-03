# Study prose for Genesis 46 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
NAMES = between("The lists agree in persons; the Greek spells the names differently, and the Latin and King James follow the Hebrew forms.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 46,
 'chapterNote': (
  "Israel goes down to Egypt: the night vision at Beersheba, the wagons, the roll of the seventy who came, and the meeting with Joseph. The columns agree on the "
  "journey and differ most in the genealogy. The Hebrew keeps Beersheba, “Here I am,” “I am God, the God of your father,” “his hand,” Pharaoh as sender of the wagons, "
  "“little ones,” Hamul, the Hebrew name-forms, Joseph’s two sons only, ten sons of Benjamin in one generation, fourteen for Rachel, two for Joseph, seventy in all, "
  "Goshen for the meeting, “his chariot,” and the brothers and the father’s house both addressed in 46:31. The Greek keeps the Well of the Oath, “What is it?”, “the God "
  "of your fathers,” “his hands,” Joseph as sender, “households,” Jemuel, its own spellings, five added descendants of Joseph (Machir, Gilead, Soutalaam, Taam, Edem), "
  "Benjamin’s sons in three generations, eighteen for Rachel, nine for Joseph, seventy-five in all, the figure Acts 7:14 follows, Heroopolis “in the land of Rameses,” "
  "“his chariots,” and Gesem of Arabia. The Latin and King James follow the Hebrew; the Latin has Jacob “die happy.”"),
 'verses': {

 '46:1': {
  'received': "Israel set out with all he had, came to Beersheba, and sacrificed to the God of his father Isaac.",
  'explain': ("The last station in Canaan, where Isaac built an altar; Jacob sacrifices to his father’s God before leaving the land. The Hebrew says Beersheba, sacrifices; the Greek the Well of the Oath, a sacrifice."),
  'shared': ["Israel set out with all that he had.", "He came to Beersheba.", "He offered sacrifices to the God of his father Isaac."],
  'instructions': [ins(K, S, "Jacob sacrificed at Beersheba before leaving Canaan."), ins(W, R, "He stops at his father’s altar on the way out of the land; the God of Isaac is consulted before Israel leaves Isaac’s country, and answers that night.")],
  'entries': ['jacob', 'isaac', 'altar'],
  'lost': [between("Hebrew Be’erah Shava, “to Beersheba,” is Greek epi to phrear tou horkou, “to the Well of the Oath”; Hebrew zevachim, “sacrifices,” is Greek thysian, “a sacrifice”; Latin “the Well of the Oath … sacrifices,” King James “Beersheba … sacrifices.”")]},

 '46:2': {
  'received': "God spoke to Israel in visions of the night: Jacob, Jacob! He said, Here I am.",
  'explain': ("The last theophany to a patriarch. Jacob, Jacob, doubled like Abraham, Abraham at Moriah and Moses, Moses at the bush. The Hebrew says visions, Here I am; the Greek a vision, What is it?"),
  'shared': ["God spoke to Israel in visions of the night.", "Jacob, Jacob!", "He said, Here I am."],
  'instructions': [ins(K, S, "God called Jacob by night at Beersheba."), ins(W, R, "God calls him Jacob, not Israel, the old name for the old man; and Jacob answers “Here I am,” the word of Abraham, which he gives to God at last without a bargain.")],
  'entries': ['jacob', 'elohim'],
  'lost': [between("Hebrew be-mar’ot ha-laylah, “in visions of the night,” plural, is Greek en horamati tēs nyktos, singular; Hebrew hinneni, “here I am,” is Greek ti estin, “what is it?”; Latin “in a vision of the night … Here I am,” King James “in the visions of the night … Here am I.”")]},

 '46:3': {
  'received': "I am God, the God of your father; do not fear to go down to Egypt, for I will make you a great nation there.",
  'explain': ("Isaac was told not to go to Egypt; Jacob is told not to fear going. The Hebrew says I am God, the God of your father; the Greek the God of your fathers; the Latin the most mighty God of your father."),
  'shared': ["I am the God of your father.", "Do not fear to go down to Egypt.", "I will make you a great nation there."],
  'instructions': [ins(K, S, "God authorised the descent into Egypt."), ins(W, R, "“Do not fear to go down”: the promise of a great nation is to be kept in Egypt, not Canaan. God sends Israel into the land of its slavery with a blessing, and 15:13 is remembered.")],
  'entries': ['elohim', 'egypt'],
  'lost': [loses("Hebrew anokhi ha-El Elohe avikha, “I am the God, the God of your father,” becomes Greek egō eimi ho theos tōn paterōn sou, “I am the God of your fathers,” the first clause absorbed and the father made plural."), between("Latin “the most mighty God of your father” and King James “God, the God of thy father” keep the singular.")]},

 '46:4': {
  'received': "I will go down with you to Egypt and surely bring you up again, and Joseph will close your eyes.",
  'explain': ("God goes down too, and will bring him up: Jacob’s body in 50:13, Israel in the exodus. Joseph will close his eyes: he will die with Joseph by him. The Hebrew says hand; the Greek hands, at last."),
  'shared': ["I will go down with you to Egypt.", "I will surely bring you up again.", "Joseph will put his hand on your eyes."],
  'instructions': [ins(K, S, "God promised to accompany Jacob and bring him back."), ins(W, R, "“I will go down with you”: the God of Bethel goes to Egypt. The promise to Jacob at the ladder, I am with you wherever you go, is kept to the border and past it.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew anokhi a‘alkha gam-aloh, “I will surely bring you up,” is Greek egō anabibasō se eis telos, “I will bring you up at last”; Hebrew yado, “his hand,” is Greek tas cheiras, “his hands”; Latin “bring you back from there … his hands,” King James “surely bring thee up again … his hand.”")]},

 '46:5': {
  'received': "Jacob left Beersheba; the sons of Israel carried their father, children and wives in the wagons Pharaoh sent.",
  'explain': ("The Hebrew says Pharaoh sent the wagons, little ones; the Greek Joseph sent, households; 45:21 allows both."),
  'shared': ["Jacob arose from Beersheba.", "The sons of Israel carried Jacob their father, their little ones and their wives.", "They rode in the wagons sent to carry him."],
  'instructions': [ins(K, S, "The family left Beersheba in the wagons.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew asher-shalach Par‘oh, “which Pharaoh sent,” becomes Greek has apesteilen Iōsēph, “which Joseph sent”; Hebrew tappam, “their little ones,” is Greek tēn aposkeuēn, “their households.”"), between("Latin and King James “which Pharaoh had sent … their little ones.”")]},

 '46:6': {
  'received': "They took their livestock and goods from Canaan and came to Egypt, Jacob and all his seed.",
  'explain': ("The Greek says possessions; the Latin he took."),
  'shared': ["They took their livestock and the goods acquired in Canaan.", "They came to Egypt.", "Jacob and all his seed with him."],
  'instructions': [ins(K, S, "Jacob entered Egypt with all his household.")],
  'entries': ['jacob', 'canaan', 'egypt'],
  'lost': [between("Hebrew miqnehem, “their livestock,” is Greek ta hyparchonta, “their possessions”; Latin “took everything he had possessed,” King James “their cattle, and their goods.”")]},

 '46:7': {
  'received': "His sons and grandsons, daughters and granddaughters, all his seed, he brought with him to Egypt.",
  'explain': ("The versions agree; the Latin compresses."),
  'shared': ["His sons and his sons’ sons.", "His daughters and his sons’ daughters.", "All his seed he brought with him into Egypt."],
  'instructions': [ins(K, S, "Four generations went down together.")],
  'entries': ['egypt'],
  'lost': [between("Latin “his sons and grandsons, daughters, and all his descendants together” compresses; Hebrew, Greek and King James list “his sons’ daughters.”")]},

 '46:8': {
  'received': "These are the names of the sons of Israel who came to Egypt, Jacob and his sons: Reuben, Jacob’s firstborn.",
  'explain': ("The roll begins; Exodus 1:1 opens with the same words. The versions agree."),
  'shared': ["These are the names of the sons of Israel who entered Egypt.", "Jacob and his sons.", "Jacob’s firstborn was Reuben."],
  'instructions': [ins(K, S, "The roll of those who entered Egypt begins."), ins(W, R, "“These are the names”: Exodus will begin with the same words. The list of seventy is the hinge between the family and the nation.")],
  'entries': ['jacob', 'egypt'],
  'lost': [AGREE]},

 '46:9': {
  'received': "Reuben’s sons: Hanoch, Pallu, Hezron and Carmi.",
  'explain': ("The Greek spells Enoch, Phallous. The versions agree."),
  'shared': ["The sons of Reuben.", "Hanoch and Pallu.", "Hezron and Carmi."],
  'instructions': [ins(K, S, "Reuben had four sons.")],
  'entries': [],
  'lost': [NAMES]},

 '46:10': {
  'received': "Simeon’s sons: Jemuel, Jamin, Ohad, Jachin, Zohar, and Shaul the son of a Canaanite woman.",
  'explain': ("Shaul’s Canaanite mother noted, perhaps the one disapproved marriage. The Greek spells Aod, Saar."),
  'shared': ["The sons of Simeon.", "Jemuel, Jamin, Ohad, Jachin, Zohar.", "Shaul, the son of a Canaanite woman."],
  'instructions': [ins(K, S, "Simeon had six sons.")],
  'entries': ['canaan'],
  'lost': [NAMES]},

 '46:11': {
  'received': "Levi’s sons: Gershon, Kohath and Merari.",
  'explain': ("The three Levite clans. The versions agree."),
  'shared': ["The sons of Levi.", "Gershon and Kohath.", "Merari."],
  'instructions': [ins(K, S, "Levi had three sons.")],
  'entries': [],
  'lost': [AGREE]},

 '46:12': {
  'received': "Judah’s sons: Er, Onan, Shelah, Perez and Zerah; Er and Onan died in Canaan. Perez’s sons: Hezron and Hamul.",
  'explain': ("Chapter 38 summarised, with Perez’s sons, David’s line. The Hebrew says Hamul; the Greek Jemuel."),
  'shared': ["The sons of Judah: Er, Onan, Shelah, Perez and Zerah.", "Er and Onan died in Canaan.", "The sons of Perez were Hezron and Hamul."],
  'instructions': [ins(K, S, "Judah’s line through Perez is recorded."), ins(W, R, "Er and Onan dead, Perez counted with sons: the Tamar story is folded into the roll, and the king’s line is already two generations deep when Israel enters Egypt.")],
  'entries': ['canaan'],
  'lost': [between("Hebrew Chamul is Greek Iemouēl, “Jemuel”; Latin and King James “Hamul.”")]},

 '46:13': {
  'received': "Issachar’s sons: Tola, Puvah, Iob and Shimron.",
  'explain': ("Iob, spelled Jashub in Numbers 26; the Greek Jasoub, Zambram."),
  'shared': ["The sons of Issachar.", "Tola and Puvah.", "Iob and Shimron."],
  'instructions': [ins(K, S, "Issachar had four sons.")],
  'entries': [],
  'lost': [NAMES]},

 '46:14': {
  'received': "Zebulun’s sons: Sered, Elon and Jahleel.",
  'explain': ("The Greek spells Allon, Aloel."),
  'shared': ["The sons of Zebulun.", "Sered and Elon.", "Jahleel."],
  'instructions': [ins(K, S, "Zebulun had three sons.")],
  'entries': [],
  'lost': [NAMES]},

 '46:15': {
  'received': "These are Leah’s sons, born in Paddan-aram, with his daughter Dinah: thirty-three souls.",
  'explain': ("Thirty-three, counting Jacob or Dinah by one reckoning. The Greek and Latin say Mesopotamia of Syria."),
  'shared': ["These are the sons of Leah, whom she bore to Jacob in Paddan-aram.", "With his daughter Dinah.", "All the souls, sons and daughters, were thirty-three."],
  'instructions': [ins(K, S, "Leah’s line numbered thirty-three.")],
  'entries': ['haran'],
  'lost': [between("Hebrew Paddan Aram is Greek Mesopotamia tēs Syrias; Latin “Mesopotamia of Syria … her daughter Dinah,” King James “Padanaram … his daughter Dinah.”")]},

 '46:16': {
  'received': "Gad’s sons: Ziphion, Haggi, Shuni, Ezbon, Eri, Arodi and Areli.",
  'explain': ("The Greek spells Saphon, Haggis, Saunis, Thasoban, Aedis, Aroedis, Aroeleis."),
  'shared': ["The sons of Gad.", "Ziphion, Haggi, Shuni, Ezbon.", "Eri, Arodi and Areli."],
  'instructions': [ins(K, S, "Gad had seven sons.")],
  'entries': [],
  'lost': [NAMES]},

 '46:17': {
  'received': "Asher’s sons: Imnah, Ishvah, Ishvi and Beriah, with their sister Serah; Beriah’s sons: Heber and Malchiel.",
  'explain': ("Serah, one of two daughters named in the roll. The Greek spells Jemna, Jesoua, Jeul, Baria, Sara, Chobor, Melchiel."),
  'shared': ["The sons of Asher: Imnah, Ishvah, Ishvi and Beriah.", "Serah was their sister.", "The sons of Beriah were Heber and Malchiel."],
  'instructions': [ins(K, S, "Asher’s line, with the daughter Serah, is recorded.")],
  'entries': [],
  'lost': [NAMES]},

 '46:18': {
  'received': "These are Zilpah’s sons, whom Laban gave to Leah; she bore Jacob sixteen souls.",
  'explain': ("The versions agree."),
  'shared': ["These are the sons of Zilpah, whom Laban gave to his daughter Leah.", "She bore these to Jacob.", "Sixteen souls."],
  'instructions': [ins(K, S, "Zilpah’s line numbered sixteen.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '46:19': {
  'received': "The sons of Rachel, Jacob’s wife: Joseph and Benjamin.",
  'explain': ("Jacob’s wife: Rachel alone is given the title in the roll. The versions agree."),
  'shared': ["The sons of Rachel.", "She was Jacob’s wife.", "Joseph and Benjamin."],
  'instructions': [ins(K, S, "Rachel’s sons were Joseph and Benjamin."), ins(W, R, "Only Rachel is called Jacob’s wife in the list; the roll of the nation keeps the old man’s heart on record.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '46:20': {
  'received': "Joseph’s sons born in Egypt, by Asenath daughter of Potiphera priest of On: Manasseh and Ephraim.",
  'explain': ("The Hebrew stops at two. The Greek adds five descendants from Numbers 26: Machir and Gilead of Manasseh, Soutalaam, Taam and Edem of Ephraim, which raises its totals below."),
  'shared': ["Sons were born to Joseph in Egypt.", "Asenath, daughter of Potiphera, priest of On, bore them.", "Manasseh and Ephraim."],
  'instructions': [ins(K, S, "Joseph’s sons Manasseh and Ephraim are counted.")],
  'entries': ['egypt'],
  'lost': [keeps("An added genealogy in the Greek: egenonto de huioi Manassē … Machir, Machir de egennēsen ton Galaad; huioi de Ephraim … Soutalaam kai Taam; huioi de Soutalaam Edem, “sons of Manasseh by his Syrian concubine: Machir; Machir begat Gilead; the sons of Ephraim: Soutalaam and Taam; Soutalaam’s son Edem,” five persons the Hebrew lacks."), between("Latin and King James end with Manasseh and Ephraim; the Greek’s On is Heliopolis.")]},

 '46:21': {
  'received': "Benjamin’s sons: Bela, Becher, Ashbel, Gera, Naaman, Ehi, Rosh, Muppim, Huppim and Ard.",
  'explain': ("Ten sons for Benjamin, the youngest, in the Hebrew; the Greek makes three sons, six grandsons by Bela, and Ard a great-grandson by Gera, matching Numbers 26 and 1 Chronicles 8."),
  'shared': ["The sons of Benjamin.", "Bela, Becher, Ashbel, Gera, Naaman.", "Ehi, Rosh, Muppim, Huppim and Ard."],
  'instructions': [ins(K, S, "Benjamin’s ten descendants are listed."), ins(W, R, "Benjamin the lad has ten sons in the list; the roll counts what will be, and the Greek quietly spreads them over three generations to make the arithmetic of a family into the arithmetic of a tribe.")],
  'entries': [],
  'lost': [loses("Hebrew lists ten as bene Binyamin, “sons of Benjamin,” in one generation; the Greek reads huioi de Beniamin: Bala kai Chobōr kai Asbēl; egenonto de huioi Bala: Gēra kai Noeman kai Ancheis kai Rhōs kai Mamphin kai Hophimin; Gēra de egennēsen ton Arad, three generations."), between("Latin and King James list ten sons with the Hebrew.")]},

 '46:22': {
  'received': "These are Rachel’s sons born to Jacob: fourteen souls.",
  'explain': ("Two plus two plus ten. The Greek says eighteen, having added Joseph’s descendants."),
  'shared': ["These were Rachel’s sons.", "They were born to Jacob.", "The souls were counted."],
  'instructions': [ins(K, S, "Rachel’s line numbered fourteen.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew arba‘ah asar, “fourteen,” becomes Greek deka oktō, “eighteen,” the four added descendants of 46:20 counted."), between("Latin and King James “fourteen.”")]},

 '46:23': {
  'received': "Dan’s son: Hushim.",
  'explain': ("Sons, plural, with one name; the Greek Asom."),
  'shared': ["The sons of Dan.", "Hushim.", "One is named."],
  'instructions': [ins(K, S, "Dan had one son.")],
  'entries': [],
  'lost': [NAMES]},

 '46:24': {
  'received': "Naphtali’s sons: Jahzeel, Guni, Jezer and Shillem.",
  'explain': ("The Greek spells Hasiel, Gouni, Issaar, Syllem."),
  'shared': ["The sons of Naphtali.", "Jahzeel and Guni.", "Jezer and Shillem."],
  'instructions': [ins(K, S, "Naphtali had four sons.")],
  'entries': [],
  'lost': [NAMES]},

 '46:25': {
  'received': "These are Bilhah’s sons, whom Laban gave to Rachel; she bore Jacob seven souls.",
  'explain': ("The versions agree."),
  'shared': ["These are the sons of Bilhah, whom Laban gave to his daughter Rachel.", "She bore these to Jacob.", "Seven souls."],
  'instructions': [ins(K, S, "Bilhah’s line numbered seven.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '46:26': {
  'received': "All who came to Egypt with Jacob, his own descendants, not counting his sons’ wives: sixty-six.",
  'explain': ("Sixty-six from his loins, excluding Joseph and his two sons in Egypt and, by one count, Jacob himself. The versions agree."),
  'shared': ["All the souls who came to Egypt with Jacob, who came from his loins.", "Not counting the wives of Jacob’s sons.", "Sixty-six souls."],
  'instructions': [ins(K, S, "Sixty-six of Jacob’s descendants entered Egypt.")],
  'entries': ['jacob', 'egypt'],
  'lost': [AGREE]},

 '46:27': {
  'received': "Joseph’s sons born in Egypt were two; all the souls of Jacob’s house that came to Egypt were seventy.",
  'explain': ("Seventy: sixty-six, Joseph and his two sons, and Jacob. The Greek says nine and seventy-five, with the added descendants; Acts 7:14 and the Dead Sea Exodus 1:5 have seventy-five, Deuteronomy 10:22 seventy."),
  'shared': ["Joseph’s sons born to him in Egypt are counted.", "All the souls of Jacob’s house who came to Egypt.", "The total is given."],
  'instructions': [ins(K, S, "Seventy souls of Jacob’s house came to Egypt."), ins(W, R, "Seventy, or seventy-five: the Hebrew and Greek count the same family by different rules, and Stephen in Acts follows the Greek. The number is the seed of a nation either way, and the nations of Genesis 10 were seventy too.")],
  'entries': ['jacob', 'egypt'],
  'lost': [loses("Hebrew nefesh shenayim … shiv‘im, “two souls … seventy,” becomes Greek psychai ennea … hebdomēkonta pente, “nine souls … seventy-five,” with the five added in 46:20 counted twice over in the method."), between("Latin and King James “two … seventy.”")]},

 '46:28': {
  'received': "He sent Judah ahead to Joseph to show the way to Goshen, and they came to Goshen.",
  'explain': ("Judah leads again. The Hebrew says to show the way before him to Goshen; the Greek to meet him near Heroopolis in the land of Rameses, the Greek names for the eastern delta; the Latin to announce his coming."),
  'shared': ["He sent Judah ahead of him to Joseph.", "He was to prepare the way to Goshen.", "They came to the land of Goshen."],
  'instructions': [ins(K, S, "Judah went ahead to arrange the meeting."), ins(W, R, "Judah is sent ahead to Joseph; the brother who proposed the sale now prepares the reunion, and his tribe will lead Israel’s march in Numbers.")],
  'entries': [],
  'lost': [loses("Hebrew le-horot lefanav Goshnah va-yavo’u artzah Goshen, “to direct before him to Goshen, and they came to the land of Goshen,” becomes Greek synantēsai autō kath’ Hērōōn polin eis gēn Rhamessē, “to meet him near Heroopolis in the land of Rameses”; Goshen is replaced by Greek-era names."), between("Latin “have him meet him in Goshen” and King James “to direct his face unto Goshen” keep Goshen.")]},

 '46:29': {
  'received': "Joseph harnessed his chariot and went up to meet his father Israel in Goshen; he presented himself, fell on his neck and wept a long while.",
  'explain': ("The fifth weeping, the longest. The Hebrew says his chariot, Goshen, wept on his neck a good while; the Greek his chariots, Heroopolis, wept abundantly; the Latin wept as he embraced him."),
  'shared': ["Joseph made ready his chariot and went up to meet Israel his father.", "He presented himself to him.", "He fell on his neck and wept a long while."],
  'instructions': [ins(K, S, "Joseph and Jacob were reunited."), ins(W, R, "He fell on his neck and wept a good while: the father who said he would go down to Sheol mourning is wept over alive by the son he mourned. Twenty-two years are in the length of the weeping.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew merkavto, “his chariot,” is Greek ta harmata autou, “his chariots”; Hebrew Goshnah is Greek kath’ Hērōōn polin, “near Heroopolis”; Hebrew va-yevk al-tzavvarav od, “and wept on his neck still,” is Greek eklausen klauthmō pleioni, “wept with much weeping”; Latin “in that same place … wept as he embraced him,” King James “to Goshen … wept on his neck a good while.”")]},

 '46:30': {
  'received': "Israel said to Joseph: Now let me die, since I have seen your face and you are alive.",
  'explain': ("Let me die: the wish of 45:28 fulfilled; he will live seventeen more years. The Latin says die happy."),
  'shared': ["Israel said to Joseph.", "Now let me die.", "I have seen your face, and you are still alive."],
  'instructions': [ins(K, S, "Jacob was content to die having seen Joseph."), ins(W, R, "“Now let me die”: Simeon will say the same with the child in his arms. The sight of the lost son alive is enough for a life; Jacob asks nothing more of God.")],
  'entries': ['jacob'],
  'lost': [between("Latin “Now I shall die happy, because I have seen your face and leave you still alive” expands; Hebrew, Greek and King James “Now let me die, since I have seen thy face, because thou art yet alive.”")]},

 '46:31': {
  'received': "Joseph told his brothers and his father’s house: I will go up and tell Pharaoh my brothers and my father’s house from Canaan have come.",
  'explain': ("Joseph manages the court. The Greek addresses the brothers only."),
  'shared': ["Joseph said to his brothers and his father’s household.", "I will go up and report to Pharaoh.", "My brothers and my father’s household from Canaan have come to me."],
  'instructions': [ins(K, S, "Joseph prepared to present the family to Pharaoh.")],
  'entries': ['canaan'],
  'lost': [loses("Hebrew ve-el-bet aviv, “and to his father’s house,” as addressees is absent from the Greek, which has only pros tous adelphous autou, “to his brothers.”"), between("Latin and King James “to his brothers and all his father’s household.”")]},

 '46:32': {
  'received': "The men are shepherds, keepers of livestock, and have brought their flocks, herds and all they have.",
  'explain': ("Shepherds, which 46:34 says Egyptians despise: Joseph tells Pharaoh plainly. The Greek says livestock, oxen."),
  'shared': ["The men are shepherds.", "They have been keepers of livestock.", "They have brought their flocks and herds and all they have."],
  'instructions': [ins(K, S, "Joseph would present his family as shepherds.")],
  'entries': [],
  'lost': [between("Hebrew tzonam u-veqaram, “their flocks and their herds,” is Greek ta ktēnē kai tous boas, “their livestock and oxen”; Latin “livestock, herds,” King James “flocks, and herds.”")]},

 '46:33': {
  'received': "When Pharaoh calls you and asks your occupation,",
  'explain': ("The versions agree."),
  'shared': ["Pharaoh will call you.", "He will say.", "What is your occupation?"],
  'instructions': [ins(K, S, "Joseph anticipated Pharaoh’s question.")],
  'entries': [],
  'lost': [AGREE]},

 '46:34': {
  'received': "say, Your servants have kept livestock from youth, we and our fathers, so you may live in Goshen; for every shepherd is an abomination to Egyptians.",
  'explain': ("Joseph wants them despised into Goshen: the shepherds’ stigma secures the pasture and keeps the family apart. The Greek says Gesem of Arabia; the Latin detest."),
  'shared': ["Your servants have been herdsmen from our youth until now, we and our fathers.", "So that you may dwell in the land of Goshen.", "Every shepherd is an abomination to the Egyptians."],
  'instructions': [ins(C, S, "Tell Pharaoh you have been herdsmen from your youth."), ins(W, R, "Joseph uses Egypt’s contempt to keep Israel separate; the shepherds are given Goshen because the Egyptians will not have them nearer, and the distance preserves a people.")],
  'entries': ['egypt'],
  'lost': [keeps("Greek en gē Gesem Arabias, “in the land of Gesem of Arabia,” for Hebrew be-eretz Goshen."), between("Latin “the Egyptians detest all shepherds” and King James “every shepherd is an abomination unto the Egyptians” follow the Hebrew.")]},
 }
}
