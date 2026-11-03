# Study prose for Genesis 33 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 33,
 'chapterNote': (
  "Jacob meets Esau and is embraced, the brothers part, and Jacob settles at Succoth and then Shechem, where he buys a field and builds an altar. The columns "
  "agree on the reconciliation; the Hebrew keeps Jacob’s “No, please” in 33:10, “I will go beside you,” Succoth as a name, “arrived safely” for shalem, “the sons "
  "of Hamor,” a hundred kesitahs, and the altar named El-Elohe-Israel. The Greek keeps Esau “his brother” and the maids “two” added, both brothers weeping, "
  "“companies” in the plural, “you will accept me,” “go straight ahead,” “Booths” and “houses,” Salem as a city, Hamor alone as seller, a hundred lambs, and "
  "the altar used to invoke rather than named. The Latin and King James follow the Hebrew; the Latin also reads Salem and a hundred lambs, and has only Esau weep."),
 'verses': {

 '33:1': {
  'received': "Jacob looked up and saw Esau coming with four hundred men, and divided the children among Leah, Rachel and the two maids.",
  'explain': ("The morning after Peniel, the limping man sees the army. He arranges the children by their mothers. The Greek adds his brother after Esau."),
  'shared': ["Jacob looked up and saw Esau coming.", "Four hundred men were with him.", "He divided the children among Leah, Rachel and the two maids."],
  'instructions': [ins(K, S, "Jacob saw Esau’s approach and arranged his family."), ins(W, R, "Blessed and lamed, Jacob still arranges; the night with God has not made him careless of the morning.")],
  'entries': ['jacob'],
  'lost': [keeps("An added ho adelphos autou, “his brother,” after Esau in the Greek."), between("Hebrew, Latin and King James “Esau was coming.”")]},

 '33:2': {
  'received': "He put the maids and their children first, Leah and hers next, and Rachel and Joseph last.",
  'explain': ("The order is the order of his love, the most precious furthest from danger. The Greek adds two to the maids and says sons for their children."),
  'shared': ["The maids and their children in front.", "Leah and her children next.", "Rachel and Joseph last."],
  'instructions': [ins(K, S, "Jacob placed Rachel and Joseph safest, at the rear."), ins(W, R, "The order of the march is the order of the heart; Joseph’s brothers will have seen where they stood, and chapter 37 begins here.")],
  'entries': ['jacob'],
  'lost': [keeps("An added dyo, “two,” before the maids and huious, “sons,” for their children in the Greek; Hebrew ha-shefachot ve-yaldehen, “the maids and their children.”"), between("Latin “the two maidservants and their children” adds the number too; King James “the handmaids and their children.”")]},

 '33:3': {
  'received': "He went ahead of them and bowed to the ground seven times as he approached his brother.",
  'explain': ("Seven bows, the homage of a vassal to a king in the letters of the age. Jacob goes first, between his family and the danger. The versions agree."),
  'shared': ["He himself went on before them.", "He bowed to the ground seven times.", "He came near to his brother."],
  'instructions': [ins(K, S, "Jacob bowed seven times before Esau."), ins(W, R, "“Let your mother’s sons bow down to you,” said Isaac; Jacob bows seven times to Esau. The blessing is reversed in act, and God’s purpose is served by the reversal.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '33:4': {
  'received': "Esau ran to him, embraced him, fell on his neck and kissed him, and they wept.",
  'explain': ("Esau runs, as Laban ran and as the father runs in Luke 15. The Hebrew order is embraced, fell on his neck, kissed; the Greek embraced, kissed, fell on his neck, both wept; the Latin has only Esau weep."),
  'shared': ["Esau ran to meet him.", "He embraced him, fell on his neck and kissed him.", "They wept."],
  'instructions': [ins(K, S, "Esau embraced Jacob and the brothers wept."), ins(W, R, "The four hundred men were an escort, not an army; Esau runs where Jacob crawled, and the forgiveness Jacob bought with camels was already free.")],
  'entries': [],
  'lost': [between("Hebrew va-yechabbeqehu va-yippol al-tzavvarav va-yishshaqehu va-yivku, “embraced him, fell on his neck, kissed him, and they wept,” is Greek periēlaben auton kai … katephilēsen auton, kai epepesen epi ton trachēlon autou, kai eklausan amphoteroi, “embraced and kissed, fell on his neck, and both wept”; Latin “kissed him, and wept,” Esau alone; King James follows the Hebrew.")]},

 '33:5': {
  'received': "Esau saw the women and children and asked who they were; Jacob said, The children God has graciously given your servant.",
  'explain': ("Jacob credits God for the children, as he did not credit the rods. The Hebrew says graciously given, chanan; the Greek had mercy; the Latin do they belong to you?"),
  'shared': ["Esau looked up and saw the women and children.", "Who are these with you?", "The children God has graciously given your servant."],
  'instructions': [ins(K, S, "Jacob presented his children as God’s gift."), ins(W, R, "“Your servant” again; even embraced, Jacob keeps the bow in his speech. Humility learned in fear becomes habit in safety.")],
  'entries': ['jacob', 'elohim'],
  'lost': [between("Hebrew asher-chanan Elohim, “whom God has graciously given,” is Greek hois ēleēsen ho theos, “with whom God has had mercy on”; Latin adds “Do they belong to you?”; King James “graciously given.”")]},

 '33:6': {
  'received': "The maids and their children came and bowed.",
  'explain': ("The presentation begins, in the order of the march. The versions agree."),
  'shared': ["The maids drew near.", "Their children came too.", "They bowed down."],
  'instructions': [ins(K, S, "The maids and children bowed to Esau.")],
  'entries': [],
  'lost': [AGREE]},

 '33:7': {
  'received': "Leah and her children came and bowed; afterward Joseph and Rachel came and bowed.",
  'explain': ("Joseph before Rachel in the Hebrew, perhaps shielding her; the Greek Rachel and Joseph, after these things. The versions agree in substance."),
  'shared': ["Leah and her children drew near and bowed.", "Afterward Joseph and Rachel drew near.", "They bowed."],
  'instructions': [ins(K, S, "Leah, then Rachel and Joseph, bowed to Esau.")],
  'entries': [],
  'lost': [between("Hebrew ve-achar niggash Yosef ve-Rachel, “and afterward Joseph and Rachel drew near,” is Greek kai meta tauta prosēngisen Rhachēl kai Iōsēph, “and after these things Rachel and Joseph drew near”; Latin “Joseph and Rachel,” King James “Joseph near and Rachel.”")]},

 '33:8': {
  'received': "Esau asked what all the company he met was for; Jacob said, To find favour in my lord’s sight.",
  'explain': ("The droves explained. The Hebrew says all this camp, singular; the Greek companies, and repeats your servant; the Latin those companies."),
  'shared': ["What did you mean by all this company I met?", "Jacob answered.", "To find favour in the sight of my lord."],
  'instructions': [ins(K, S, "Jacob explained the gifts as a bid for favour.")],
  'entries': ['jacob'],
  'lost': [keeps("Greek pasai hai parembolai hautai, “all these companies,” plural, for Hebrew kol-ha-machaneh ha-zeh, “all this camp,” and an added ho pais sou, “your servant.”"), between("Latin “those companies” plural; King James “all this drove.”")]},

 '33:9': {
  'received': "Esau said, I have plenty, my brother; keep what is yours.",
  'explain': ("My brother: Esau answers my lord and your servant with the word Jacob has avoided. The versions agree."),
  'shared': ["I have plenty.", "My brother.", "Keep what is yours for yourself."],
  'instructions': [ins(K, S, "Esau declined the gift as a brother."), ins(W, R, "Jacob says “my lord” and Esau says “my brother”; the one who was wronged uses the warmer word, and the chapter turns on it.")],
  'entries': [],
  'lost': [AGREE]},

 '33:10': {
  'received': "Jacob begged him to accept the gift, for seeing Esau’s face was like seeing the face of God, and Esau had received him.",
  'explain': ("Peniel the night before, and now Esau’s face like God’s face: the brother’s welcome is a second theophany. The Hebrew begins No, please and says you have accepted me; the Greek omits the plea and says you will accept me; the Latin please, not so, this little gift, be favourable."),
  'shared': ["If I have found favour in your sight, accept my gift from my hand.", "I have seen your face as one sees the face of God.", "You have accepted me."],
  'instructions': [ins(K, S, "Jacob pressed the gift, comparing Esau’s face to God’s."), ins(W, R, "Having seen God face to face and lived, Jacob sees his brother’s face and says it is the same; forgiveness from a man is where God’s face is seen by day.")],
  'entries': ['jacob', 'elohim'],
  'lost': [loses("Hebrew al-na, “no, please,” opening Jacob’s reply, is absent from the Greek; Hebrew va-tirtzeni, “and you have accepted me,” becomes Greek kai eudokēseis me, “and you will accept me.”"), between("Latin “Please, not so … this little gift … Be favourable to me” and King James “Nay, I pray thee … thou wast pleased with me” follow the Hebrew.")]},

 '33:11': {
  'received': "Take my blessing that was brought to you, for God has been gracious to me and I have everything. He urged him, and Esau accepted.",
  'explain': ("Jacob calls the gift my blessing, berakhah: the word he stole is the word he now gives back. The Hebrew says I have enough, kol, all; the Greek I have everything, blessings; the Latin God gave me by granting me everything."),
  'shared': ["Accept my blessing that has been brought to you.", "God has dealt graciously with me and I have all.", "He urged him and Esau accepted it."],
  'instructions': [ins(K, S, "Esau accepted Jacob’s gift under urging."), ins(W, R, "“Take my blessing”: Jacob returns the word he took in chapter 27, and Esau takes it. The feud ends in a transfer of the thing it began with.")],
  'entries': ['jacob', 'elohim'],
  'lost': [between("Hebrew birkhati, “my blessing,” singular, is Greek tas eulogias mou, “my blessings”; Hebrew yesh-li-khol, “I have all,” is Greek esti moi panta; Latin “which God gave me by granting me everything”; King James “my blessing … I have enough.”")]},

 '33:12': {
  'received': "Esau said, Let us journey on, and I will go beside you.",
  'explain': ("Esau offers escort. The Hebrew says I will go before you, or alongside; the Greek let us set out and go straight ahead, without the clause; the Latin I will accompany you."),
  'shared': ["Esau spoke.", "Let us set out and go.", "He offers to travel with Jacob."],
  'instructions': [ins(K, S, "Esau offered to travel with Jacob.")],
  'entries': [],
  'lost': [loses("Hebrew ve-elekhah le-negdekha, “and I will go beside you,” is absent from the Greek, which has aparantes poreusometha ep’ eutheian, “setting out let us go straight ahead.”"), between("Latin “I will accompany you on your journey” and King James “I will go before thee” keep the clause.")]},

 '33:13': {
  'received': "Jacob said the children were tender and the flocks nursing; one hard day’s drive would kill them all.",
  'explain': ("A true reason and a polite refusal. The Greek makes Jacob the driver; the Hebrew passive. The versions agree in substance."),
  'shared': ["My lord knows the children are tender.", "The nursing flocks and herds are with me.", "If driven hard one day, all the flock will die."],
  'instructions': [ins(K, S, "Jacob declined to travel at Esau’s pace.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew u-defaqum yom echad, “and if they are driven one day,” impersonal, is Greek ean oun katadiōxō autous hēmeran mian, “if then I drive them one day”; Latin “if I make them work too hard”; King James “if men should overdrive them.”")]},

 '33:14': {
  'received': "Let my lord go ahead; I will follow slowly at the pace of the herds and children until I reach you in Seir.",
  'explain': ("Jacob promises Seir and goes to Succoth; the brothers meet again only at Isaac’s burial. The Hebrew says at the pace of the work before me, the livestock; the Greek according to the journey before me; the Latin as my little ones are able."),
  'shared': ["Let my lord go ahead of his servant.", "I will lead on gently at the pace of the livestock and the children.", "Until I come to my lord in Seir."],
  'instructions': [ins(K, S, "Jacob promised to follow Esau to Seir at his own pace."), ins(W, R, "“Until I come to my lord in Seir”: he does not go. Reconciled, Jacob still keeps his distance from Esau, and the narrator records the promise without the arrival.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew le-regel ha-melakhah asher-lefanai, “at the foot of the work before me,” the livestock, is Greek kata scholēn tēs poreuseōs tēs enantion mou, “at the leisure of the journey before me”; Latin “as I see that my little ones are able”; King James “according as the cattle that goeth before me and the children be able to endure.”")]},

 '33:15': {
  'received': "Esau offered to leave some men with him; Jacob said there was no need, only to find his lord’s favour.",
  'explain': ("A second offer, a second refusal. The Greek says it is enough that I have found favour; the Hebrew let me find favour; the Latin I need only this."),
  'shared': ["Let me leave with you some of my people.", "Why is this necessary?", "Let me find favour in my lord’s sight."],
  'instructions': [ins(K, S, "Jacob declined Esau’s escort.")],
  'entries': ['jacob'],
  'lost': [keeps("Greek hikanon hoti heuron charin, “it is enough that I have found favour,” for Hebrew emtza-chen, “let me find favour.”"), between("Latin “There is no need. I need only this” and King James “What needeth it? let me find grace” follow the Hebrew.")]},

 '33:16': {
  'received': "Esau returned that day to Seir.",
  'explain': ("Esau goes home. He is not seen again until 35:29. The versions agree."),
  'shared': ["Esau returned.", "It was that day.", "He went on his way to Seir."],
  'instructions': [ins(K, S, "Esau went back to Seir.")],
  'entries': [],
  'lost': [AGREE]},

 '33:17': {
  'received': "Jacob went to Succoth, built a house and made booths for his cattle, and named the place Succoth.",
  'explain': ("Succoth, booths, east of Jordan, not Seir. The Hebrew keeps the name and says a house; the Greek translates Booths and says houses; the Latin Succoth, that is, Tents."),
  'shared': ["Jacob travelled to Succoth.", "He built a house and made booths for his livestock.", "He named the place Succoth."],
  'instructions': [ins(K, S, "Jacob settled at Succoth, not Seir."), ins(W, R, "A house, for the first time: Jacob the tent-dweller builds. The man who vowed a house for God at Bethel builds one for himself at Succoth first.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew Sukkot, a name, becomes Greek Skēnai, “Booths,” a translation, and Hebrew bayit, “a house,” becomes oikias, “houses.”"), between("Latin “Succoth, that is, Tents” and King James “Succoth … an house” keep the name.")]},

 '33:18': {
  'received': "Jacob came safely to the city of Shechem in Canaan, from Paddan-aram, and camped before the city.",
  'explain': ("Back in Canaan. The Hebrew shalem can be read safely, whole, or as a place, Salem; the Greek, Latin and King James take it as Salem, a city of Shechem. The vow at Bethel asked for a return in peace, shalom; shalem answers it."),
  'shared': ["Jacob came to the city of Shechem in the land of Canaan.", "He came from Paddan-aram.", "He camped in front of the city."],
  'instructions': [ins(K, S, "Jacob returned to Canaan at Shechem."), ins(W, R, "“Jacob came shalem”: whole, safe, in peace, as he asked at Bethel. The vow’s condition is met in a single word, and the vow itself is still unpaid.")],
  'entries': ['jacob', 'canaan', 'haran'],
  'lost': [between("Hebrew shalem, “whole” or “safe,” is Greek Salēm, a city name, as in Latin Salem and King James “Shalem”; Hebrew Paddan Aram is Greek “Mesopotamia of Syria.”")]},

 '33:19': {
  'received': "He bought the plot where he camped from the sons of Hamor, Shechem’s father, for a hundred kesitahs.",
  'explain': ("The second purchase of land in Canaan, after Machpelah; Joseph will be buried here. The kesitah is an unknown unit; the Greek and Latin render it a hundred lambs; the Hebrew says the sons of Hamor, the Greek Hamor alone."),
  'shared': ["He bought the plot of ground where he had pitched his tent.", "The seller was Hamor’s house, Shechem’s father.", "He paid a hundred units."],
  'instructions': [ins(K, S, "Jacob bought a field at Shechem."), ins(W, R, "Abraham bought a grave and Jacob buys a camp; the land is acquired one plot at a time, by purchase, long before it is possessed.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew me-yad bene-Chamor, “from the hand of the sons of Hamor,” becomes Greek para Emmōr, “from Hamor,” and Hebrew me’ah qesitah, “a hundred kesitahs,” becomes hekaton amnōn, “a hundred lambs.”"), between("Latin “from the sons of Hamor … for one hundred lambs” mixes; King James “the children of Hamor … an hundred pieces of money.”")]},

 '33:20': {
  'received': "He set up an altar there and called it El-Elohe-Israel, God, the God of Israel.",
  'explain': ("Jacob’s first altar, named with his new name: God, the God of Israel. The Hebrew names the altar; the Greek invoked the God of Israel, describing the act; the Latin called upon the most mighty God of Israel."),
  'shared': ["He erected an altar there.", "He called on God.", "The God of Israel."],
  'instructions': [ins(K, S, "Jacob built an altar to the God of Israel."), ins(W, R, "At Bethel he vowed “the Lord shall be my God”; at Shechem the altar is named “the God of Israel.” The vow is paid in a name, and Israel is Jacob.")],
  'entries': ['jacob', 'altar', 'elohim'],
  'lost': [loses("Hebrew va-yiqra-lo El Elohe Yisra’el, “and he called it El, the God of Israel,” a name for the altar, becomes Greek kai epekalesato ton theon Israēl, “and he called upon the God of Israel,” an act of prayer."), between("Latin “called upon the most mighty God of Israel” follows the Greek’s sense; King James “called it EleloheIsrael” keeps the name.")]},
 }
}
