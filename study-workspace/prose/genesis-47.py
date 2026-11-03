# Study prose for Genesis 47 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 47,
 'chapterNote': (
  "Jacob before Pharaoh, Israel settled in Goshen, Joseph’s famine administration that makes Egypt Pharaoh’s, Israel’s growth, and Jacob’s oath from Joseph to be "
  "buried in Canaan. The columns agree; the Hebrew keeps Goshen, “Pharaoh said to his brothers,” the settlement as a request (“please let your servants live in Goshen”), "
  "Pharaoh’s grant and the livestock appointment in 47:6, “according to their little ones,” “we will not hide from my lord,” “he moved them into the cities,” “here is seed,” "
  "“for your little ones’ food,” “may we find favour,” and Israel bowing “at the head of the bed.” The Greek keeps Gesem, Joseph named in 47:3, the settlement as a "
  "statement, Pharaoh’s grant moved into 47:5 with an added arrival notice, “measured for each person,” an added “do not let us be wiped out,” “he enslaved them,” "
  "“all the Egyptians,” “we have found favour,” and Israel bowing “upon the top of his staff,” the reading Hebrews 11:21 follows. One Hebrew-column rendering was "
  "corrected today. The Latin and King James follow the Hebrew; the Latin presents “five of his youngest brothers” and has the Egyptians “gladly serve the king.”"),
 'verses': {

 '47:1': {
  'received': "Joseph told Pharaoh his father and brothers had come from Canaan with their flocks and herds and were in Goshen.",
  'explain': ("The report, as planned in 46:31. The Hebrew says flocks and herds, Goshen; the Greek livestock and oxen, Gesem."),
  'shared': ["Joseph came and told Pharaoh.", "My father and brothers, their flocks and herds and all they have, have come from Canaan.", "They are in the land of Goshen."],
  'instructions': [ins(K, S, "Joseph announced his family’s arrival to Pharaoh.")],
  'entries': ['canaan', 'egypt'],
  'lost': [between("Hebrew tzonam u-veqaram, “their flocks and herds,” is Greek ta ktēnē autōn kai hoi boes autōn, “their livestock and oxen”; Hebrew Goshen is Greek Gesem; Latin and King James “Goshen.”")]},

 '47:2': {
  'received': "He took five of his brothers and presented them to Pharaoh.",
  'explain': ("Five, a round Egyptian number, as in 43:34 and 45:22. The Latin says the youngest five; the Greek from among his brothers."),
  'shared': ["From among his brothers he took five men.", "He presented them.", "Before Pharaoh."],
  'instructions': [ins(K, S, "Five brothers were presented to Pharaoh.")],
  'entries': [],
  'lost': [between("Hebrew u-miqtzeh echav, “from the end of his brothers,” is Greek apo de tōn adelphōn autou, “from among his brothers”; Latin “five of his youngest brothers” reads qatzeh as the lesser; King James “some of his brethren, even five men.”")]},

 '47:3': {
  'received': "Pharaoh asked their occupation; they said, Your servants are shepherds, we and our fathers.",
  'explain': ("The rehearsed answer, 46:34. The Greek names Joseph’s brothers. The Hebrew-column rendering was corrected today."),
  'shared': ["Pharaoh said to his brothers, What is your occupation?", "They answered Pharaoh.", "Your servants are shepherds, both we and our fathers."],
  'instructions': [ins(K, S, "The brothers declared themselves shepherds."), ins(W, R, "They say the despised word, shepherds, to the king who despises it, because Joseph told them to; the family’s separateness in Egypt is chosen on the first day.")],
  'entries': [],
  'lost': [between("Hebrew el-echav, “to his brothers,” is Greek tois adelphois Iōsēph, “to Joseph’s brothers”; Latin “He asked them,” King James “unto his brethren.”")]},

 '47:4': {
  'received': "We have come to sojourn, for there is no pasture for our flocks in Canaan’s famine; please let your servants live in Goshen.",
  'explain': ("Sojourn, gur: temporary, they think. The Hebrew says please let your servants live; the Greek now we will live; the Latin we ask you to grant."),
  'shared': ["We have come to sojourn in the land.", "There is no pasture for your servants’ flocks, for the famine is severe in Canaan.", "Let your servants live in the land of Goshen."],
  'instructions': [ins(K, S, "The brothers asked to settle in Goshen."), ins(W, R, "“To sojourn”: they intend a visit and will stay four hundred years. Israel enters Egypt as Abraham entered Canaan, a sojourner, and the word has a long future.")],
  'entries': ['canaan'],
  'lost': [between("Hebrew ve-attah yeshvu-na avadekha, “and now please let your servants dwell,” a request, is Greek nyn oun katoikēsomen hoi paides sou, “now then we your servants will dwell,” a statement; Latin “We ask you to grant,” King James “we pray thee, let thy servants dwell.”")]},

 '47:5': {
  'received': "Pharaoh said to Joseph: Your father and brothers have come to you.",
  'explain': ("The Hebrew and Latin have one sentence. The Greek here carries Pharaoh’s grant of Gesem and the livestock appointment from the Hebrew’s verse 6, and adds a narrative sentence, Jacob and his sons came to Joseph in Egypt, and Pharaoh heard of it, before the Hebrew words."),
  'shared': ["Pharaoh spoke to Joseph.", "Your father and your brothers.", "They have come to you."],
  'instructions': [ins(K, S, "Pharaoh acknowledged the family’s arrival.")],
  'entries': [],
  'lost': [keeps("The Greek reads katoikeitōsan en gē Gesem; ei de epistē hoti eisin en autois andres dynatoi, katastēson autous archontas tōn emōn ktēnōn, “let them dwell in Gesem; if you know capable men among them, set them over my livestock,” and ēlthon de eis Aigypton pros Iōsēph Iakōb kai hoi huioi autou, kai ēkousen Pharaō basileus Aigyptou, “Jacob and his sons came to Joseph in Egypt, and Pharaoh king of Egypt heard,” before the Hebrew’s sentence; the grant is the Hebrew’s 47:6."), between("Latin and King James have only “Your father and brothers have come to you.”")]},

 '47:6': {
  'received': "Egypt is before you; settle them in the best of the land, in Goshen; and if any are capable, set them over my livestock.",
  'explain': ("Pharaoh’s grant, and an offer of office to the shepherds. The Greek has only the first clause here, the rest having been placed in verse 5."),
  'shared': ["The land of Egypt is before you.", "Settle your father and brothers in the best of the land; let them live in Goshen.", "If you know capable men among them, put them in charge of my livestock."],
  'instructions': [ins(K, S, "Pharaoh granted Goshen and offered posts."), ins(W, R, "“The land of Egypt is before you”: Pharaoh gives Israel what God gave Abraham in words, a land before him. The gift is real and the giver is a king, and the difference will show in four hundred years.")],
  'entries': ['egypt'],
  'lost': [loses("Hebrew yeshvu be-eretz Goshen ve-im-yadata … sare miqneh al-asher-li, “let them dwell in Goshen, and if you know … chiefs of livestock over what is mine,” is absent here in the Greek, which placed it in 47:5 and keeps only hē gē Aigyptou enantion sou estin; en tē beltistē gē katoikison, “the land of Egypt is before you; settle them in the best land.”"), between("Latin and King James have the full verse here.")]},

 '47:7': {
  'received': "Joseph brought in his father Jacob and presented him; Jacob blessed Pharaoh.",
  'explain': ("The shepherd blesses the king; Hebrews 7:7 says the lesser is blessed by the greater. The versions agree."),
  'shared': ["Joseph brought in his father Jacob.", "He presented him before Pharaoh.", "Jacob blessed Pharaoh."],
  'instructions': [ins(K, S, "Jacob blessed Pharaoh."), ins(W, R, "Jacob blesses Pharaoh: the old sojourner with a staff gives, the lord of Egypt receives. The dream of sun and moon is turned inside out, and the blessing of Abraham reaches a throne.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '47:8': {
  'received': "Pharaoh asked Jacob how old he was.",
  'explain': ("The days of the years of your life: Pharaoh is struck by his age. The versions agree."),
  'shared': ["Pharaoh asked Jacob.", "How many are the days?", "Of the years of your life."],
  'instructions': [ins(K, S, "Pharaoh asked Jacob’s age.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '47:9': {
  'received': "Jacob said: My sojourning has been a hundred and thirty years, few and hard, short of my fathers’ years of sojourning.",
  'explain': ("Jacob calls his life a sojourning, as Hebrews 11:13 will say of all the patriarchs, and his years few and evil. He will reach 147, short of Abraham’s 175 and Isaac’s 180."),
  'shared': ["The years of my sojourning are a hundred and thirty.", "Few and hard have been the years of my life.", "They have not reached my fathers’ years in their sojourning."],
  'instructions': [ins(K, S, "Jacob summed up his life as a hard sojourn."), ins(W, R, "“Few and evil”: a hundred and thirty years, counted as a pilgrimage and judged short and hard by the man who lived them. The blessed life, from inside, felt like this.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew me‘at ve-ra‘im, “few and evil,” is Greek mikrai kai ponērai, “few and difficult”; Latin “few and troubled,” King James “few and evil.”")]},

 '47:10': {
  'received': "Jacob blessed Pharaoh and left his presence.",
  'explain': ("A second blessing, on leaving. The versions agree."),
  'shared': ["Jacob blessed Pharaoh.", "He went out.", "He left Pharaoh’s presence."],
  'instructions': [ins(K, S, "Jacob blessed Pharaoh again and withdrew.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '47:11': {
  'received': "Joseph settled his father and brothers with a holding in the best of Egypt, the land of Rameses, as Pharaoh commanded.",
  'explain': ("Achuzzah, a holding, the word of Machpelah; Rameses, the later name of the Goshen district, from which the exodus will set out. The versions agree."),
  'shared': ["Joseph settled his father and his brothers.", "He gave them a holding in the best of the land of Egypt, the land of Rameses.", "As Pharaoh had commanded."],
  'instructions': [ins(K, S, "Israel received a holding in Rameses."), ins(W, R, "A holding in Rameses: the name of the exodus’s starting point is given to the place where Israel first settles. The land they are given is the land they will leave.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '47:12': {
  'received': "Joseph provided bread for his father, brothers and all the household, according to their little ones.",
  'explain': ("According to the mouths of the children: rations by family size. The Greek says grain measured for each person; the Latin food for each one."),
  'shared': ["Joseph provided bread for his father, his brothers and all his father’s household.", "He provided according to need.", "According to their little ones."],
  'instructions': [ins(K, S, "Joseph fed the whole family."), ins(W, R, "He feeds them by the mouths of the children; the brother who was told in a dream that sheaves would bow to him distributes sheaves to his brothers’ babies.")],
  'entries': [],
  'lost': [between("Hebrew lechem le-fi ha-taf, “bread according to the mouth of the little ones,” is Greek siton kata sōma, “grain according to the body,” per person; Latin “food for each one,” King James “bread, according to their families.”")]},

 '47:13': {
  'received': "There was no bread anywhere, so severe was the famine; Egypt and Canaan languished.",
  'explain': ("The narrative returns to the famine’s administration. The Greek says grain; the Latin throughout the whole world."),
  'shared': ["There was no bread in all the land.", "The famine was very severe.", "Egypt and Canaan languished because of it."],
  'instructions': [ins(K, S, "The famine exhausted Egypt and Canaan.")],
  'entries': ['egypt', 'canaan'],
  'lost': [between("Hebrew lechem, “bread,” is Greek sitos, “grain”; Latin “throughout the whole world … especially Egypt and Canaan,” King James “no bread in all the land.”")]},

 '47:14': {
  'received': "Joseph gathered all the silver in Egypt and Canaan for the grain bought and brought it into Pharaoh’s house.",
  'explain': ("The money runs out first. The Greek adds he allotted grain to them; the Latin the king’s treasury."),
  'shared': ["Joseph gathered all the silver found in Egypt and Canaan.", "It was for the grain they bought.", "Joseph brought the silver into Pharaoh’s house."],
  'instructions': [ins(K, S, "Joseph collected Egypt’s silver for Pharaoh.")],
  'entries': ['egypt', 'canaan'],
  'lost': [keeps("An added kai esitometrei autois, “and he allotted grain to them,” in the Greek."), between("Latin “brought it into the king’s treasury,” King James “brought the money into Pharaoh’s house.”")]},

 '47:15': {
  'received': "When the silver was gone in Egypt and Canaan, the Egyptians came to Joseph: Give us bread; why should we die before you?",
  'explain': ("The versions agree."),
  'shared': ["All the silver was spent in Egypt and Canaan.", "All the Egyptians came to Joseph, saying, Give us bread!", "Why should we die before your eyes? Our silver is gone."],
  'instructions': [ins(K, S, "The Egyptians begged Joseph for bread."), ins(W, R, "“Why should we die before your eyes”: Jacob’s words to his sons, now Egypt’s to Joseph. The whole land has become the family in famine, and Joseph its provider.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '47:16': {
  'received': "Joseph said: Bring your livestock, and I will give you bread for it since your silver is gone.",
  'explain': ("Second stage: livestock. The versions agree."),
  'shared': ["Bring your livestock.", "I will give you bread in exchange for your livestock.", "If your silver is gone."],
  'instructions': [ins(K, S, "Joseph took livestock in payment for bread.")],
  'entries': [],
  'lost': [AGREE]},

 '47:17': {
  'received': "They brought their livestock, and Joseph gave bread for horses, flocks, herds and donkeys, feeding them that year.",
  'explain': ("Horses, first mentioned in Genesis. The versions agree."),
  'shared': ["They brought their livestock to Joseph.", "Joseph gave them bread for their horses, flocks, herds and donkeys.", "He nourished them with bread for all their livestock that year."],
  'instructions': [ins(K, S, "Egypt’s livestock passed to Pharaoh for bread.")],
  'entries': [],
  'lost': [AGREE]},

 '47:18': {
  'received': "The next year they came: we will not hide from my lord that our silver and livestock are gone; nothing is left but our bodies and land.",
  'explain': ("Third stage: persons and land. The Hebrew says we will not hide; the Greek do not let us be wiped out, our possessions; the Latin you know."),
  'shared': ["That year ended and they came the next year.", "Our silver is spent and our livestock belongs to my lord.", "Nothing is left before my lord but our bodies and our land."],
  'instructions': [ins(K, S, "The Egyptians offered themselves and their land."), ins(W, R, "Silver, then cattle, then bodies and land: the famine strips Egypt in three years down to the people themselves, and the people ask to be bought.")],
  'entries': [],
  'lost': [keeps("An added mēpote ektribōmen apo tou kyriou hēmōn, “lest we be wiped out before our lord,” and ta hyparchonta, “our possessions,” in the Greek; Hebrew lo-nekhached me-adoni, “we will not hide from my lord,” is lost."), between("Latin “We will not conceal from our lord” and King James “We will not hide it from my lord” follow the Hebrew.")]},

 '47:19': {
  'received': "Why should we die, we and our land? Buy us and our land for bread; we will be Pharaoh’s slaves. Give seed that we may live and the land not be desolate.",
  'explain': ("Slavery for seed. The Greek adds sow; the Latin into the king’s service, when its cultivator perishes."),
  'shared': ["Why should we die before your eyes, we and our land?", "Buy us and our land for bread, and we and our land will be slaves to Pharaoh.", "Give us seed, that we may live and not die and the land not become desolate."],
  'instructions': [ins(K, S, "Egypt sold itself to Pharaoh for food and seed."), ins(W, R, "Egypt makes itself Pharaoh’s slave to live, through Joseph; the people who will enslave Israel are enslaved first by their own hunger, and the irony is left for Exodus to pick up.")],
  'entries': [],
  'lost': [keeps("An added speirōmen, “that we may sow,” and a restructured opening, hina oun mē apothanōmen enantion sou, “so that we do not die before you,” in the Greek."), between("Latin “Buy us into the king’s service … lest the land be reduced to a wilderness when its cultivator perishes” varies; King James “buy us and our land for bread … servants unto Pharaoh.”")]},

 '47:20': {
  'received': "Joseph bought all Egypt for Pharaoh, each man selling his field because the famine was too much; the land became Pharaoh’s.",
  'explain': ("The Greek says sold their land, the land became Pharaoh’s; the Latin each person sold his property, he subjected it."),
  'shared': ["Joseph bought all the land of Egypt for Pharaoh.", "The Egyptians sold their fields because the famine bore heavily on them.", "The land became Pharaoh’s."],
  'instructions': [ins(K, S, "All Egypt’s land passed to Pharaoh through Joseph."), ins(W, R, "The famine Joseph foresaw makes Pharaoh owner of Egypt; the dreamer serves his king completely and his own family generously, and the narrator reports both without a verdict.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew ish sadehu, “each his field,” is Greek tēn gēn autōn, “their land”; Latin “each person sold his property … He subjected it to Pharaoh,” King James “the Egyptians sold every man his field.”")]},

 '47:21': {
  'received': "As for the people, he moved them into the cities from one end of Egypt to the other.",
  'explain': ("The Hebrew says he moved them to cities, he‘evir le-arim; the Greek and Samaritan read he‘evid la-avadim, enslaved them for him; the Latin runs the clause into verse 20’s sentence."),
  'shared': ["As for the people.", "He acted upon them.", "From one end of Egypt’s territory to the other."],
  'instructions': [ins(K, S, "Joseph reorganised the population of Egypt."), ins(W, R, "Moved to cities or made slaves: one letter divides the readings. Either way Egypt is remade under a Hebrew vizier, and the text shows a state’s whole power in a famine.")],
  'entries': ['egypt'],
  'lost': [loses("Hebrew he‘evir oto le-arim, “he moved them to the cities,” becomes Greek katedoulōsato autō eis paidas, “he enslaved them to him as slaves,” reading avadim for arim."), between("Latin “and all its peoples, from Egypt’s farthest boundaries to its remotest borders” continues 47:20; King James “he removed them to cities.”")]},

 '47:22': {
  'received': "Only the priests’ land he did not buy, for they had an allowance from Pharaoh and lived on it, so did not sell.",
  'explain': ("The priesthood exempt, as in Egyptian records. The Latin says which the king had given them, from the public storehouses."),
  'shared': ["Only the priests’ land he did not buy.", "The priests had an allowance from Pharaoh and ate it.", "Therefore they did not sell their land."],
  'instructions': [ins(K, S, "The priests’ land was exempt.")],
  'entries': [],
  'lost': [between("Latin “which the king had given them … fixed rations from the public storehouses … not compelled to sell” expands; Hebrew, Greek and King James “a portion assigned them of Pharaoh.”")]},

 '47:23': {
  'received': "Joseph told the people: I have bought you and your land today for Pharaoh; here is seed, sow the land.",
  'explain': ("The Greek says all the Egyptians, take seed; the Latin Pharaoh owns you."),
  'shared': ["Joseph said to the people.", "I have bought you and your land today for Pharaoh.", "Here is seed for you; sow the land."],
  'instructions': [ins(C, S, "Here is seed; sow the land."), ins(W, R, "Bought today, and sowing tomorrow; the sale is followed at once by seed. Joseph’s Egypt is a hard bargain that keeps people alive, and the narrator leaves the judgment to the reader.")],
  'entries': [],
  'lost': [keeps("Greek pasi tois Aigyptiois, “to all the Egyptians,” for Hebrew el-ha-am, “to the people,” and labete heautois sperma, “take seed for yourselves,” for he-lakhem zera, “here is seed for you.”"), between("Latin “Pharaoh owns you and your land. Take seed” varies; King James “I have bought you this day … lo, here is seed for you.”")]},

 '47:24': {
  'received': "At harvest give Pharaoh a fifth; four parts are yours for seed and food for your households and little ones.",
  'explain': ("A twenty per cent tax, Joseph’s own figure from 41:34, now permanent. The Greek lacks the little ones’ clause; the Latin so that you may have produce."),
  'shared': ["At harvest, give a fifth to Pharaoh.", "Four parts shall be yours for seed and your food.", "For your households and your little ones."],
  'instructions': [ins(C, S, "Give a fifth of the harvest to Pharaoh."), ins(W, R, "A fifth to the crown and four-fifths to the farmer: the terms are better than slavery in most ages, and the Egyptians will call them salvation. Joseph’s rule is severe and survivable.")],
  'entries': [],
  'lost': [loses("Hebrew u-le-ekhol le-tappekhem, “and for food for your little ones,” is absent from the Greek, which ends pasin tois en tois oikois hymōn, “for everyone in your households.”"), between("Latin “for your households and children” and King James “for food for your little ones” keep it.")]},

 '47:25': {
  'received': "They said: You have saved our lives; may we find favour with my lord, and we will be Pharaoh’s slaves.",
  'explain': ("Gratitude for servitude. The Hebrew says may we find favour; the Greek we have found favour; the Latin gladly serve the king."),
  'shared': ["You have saved our lives.", "May we find favour before my lord.", "We will be Pharaoh’s slaves."],
  'instructions': [ins(K, S, "The Egyptians accepted servitude with thanks."), ins(W, R, "“You have saved our lives”: Egypt says to Joseph what Joseph said God did through him. The saviour of Egypt is a Hebrew slave; Exodus will begin where this gratitude has been forgotten.")],
  'entries': [],
  'lost': [between("Hebrew nimtza-chen, “may we find favour,” is Greek heurēkamen charin, “we have found favour”; Latin “Only let our lord look favourably upon us, and we shall gladly serve the king”; King James “let us find grace in the sight of my lord.”")]},

 '47:26': {
  'received': "Joseph made it a law in Egypt to this day that Pharaoh has a fifth; only the priests’ land was not Pharaoh’s.",
  'explain': ("A standing statute. The Latin says paid to the kings, free of this obligation."),
  'shared': ["Joseph made it a law over the land of Egypt to this day.", "Pharaoh has a fifth.", "Only the priests’ land did not become Pharaoh’s."],
  'instructions': [ins(K, S, "The fifth became permanent Egyptian law.")],
  'entries': ['egypt'],
  'lost': [between("Latin “a fifth part has been paid to the kings throughout the whole land of Egypt, established as a law” paraphrases; Hebrew, Greek and King James “Joseph made it a law … unto this day.”")]},

 '47:27': {
  'received': "Israel lived in Egypt, in Goshen; they got holdings there and were fruitful and multiplied greatly.",
  'explain': ("While Egypt sells itself, Israel acquires and multiplies: the blessing of 1:28 and the promise to Abraham, in Goshen. The Greek says Gesem, inherited; the Latin he possessed."),
  'shared': ["Israel lived in Egypt, in the land of Goshen.", "They acquired holdings there.", "They were fruitful and multiplied greatly."],
  'instructions': [ins(K, S, "Israel prospered and multiplied in Goshen."), ins(W, R, "Egypt is impoverished and Israel multiplies; the famine that bought a nation for Pharaoh makes Jacob’s house a people. Exodus 1:7 will repeat the sentence and Pharaoh will take fright.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew va-ye’achazu vah, “and they got holdings in it,” is Greek kai eklēronomēsan ep’ autēs, “and they inherited on it”; Hebrew va-yifru, “and were fruitful,” Greek kai ēuxēthēsan, “and increased”; Latin “possessed it. He increased,” King James “had possessions therein, and grew.”")]},

 '47:28': {
  'received': "Jacob lived seventeen years in Egypt; his years were a hundred and forty-seven.",
  'explain': ("Seventeen years with Joseph in Egypt, as Joseph had seventeen with him in Canaan. The versions agree."),
  'shared': ["Jacob lived in Egypt seventeen years.", "The years of Jacob’s life.", "They were a hundred and forty-seven."],
  'instructions': [ins(K, S, "Jacob lived seventeen years in Egypt and died at 147."), ins(W, R, "Seventeen years: Joseph was seventeen when he was lost, and his father has him seventeen years at the end. The account is balanced, as Genesis likes its accounts.")],
  'entries': ['jacob', 'egypt'],
  'lost': [AGREE]},

 '47:29': {
  'received': "As Israel’s death neared he called Joseph: If I have found favour, put your hand under my thigh and deal kindly and truly with me; do not bury me in Egypt.",
  'explain': ("The oath by the thigh, Abraham’s gesture in 24:2; chesed and emet, kindness and truth. The Greek says mercy and truth."),
  'shared': ["Israel’s time to die drew near and he called his son Joseph.", "If I have found favour in your sight, put your hand under my thigh and deal kindly and truly with me.", "Please do not bury me in Egypt."],
  'instructions': [ins(K, S, "Jacob made Joseph swear not to bury him in Egypt."), ins(W, R, "Jacob asks of Joseph what Abraham asked of his servant, with the same oath; the last patriarch binds the viceroy of Egypt by the custom of the tents, and asks for Canaan dead if not alive.")],
  'entries': ['jacob', 'egypt'],
  'lost': [between("Hebrew chesed ve-emet, “kindness and faithfulness,” is Greek eleēmosynēn kai alētheian, “mercy and truth”; Latin “kindness and faithfulness,” King James “kindly and truly.”")]},

 '47:30': {
  'received': "Let me lie with my fathers; carry me out of Egypt and bury me in their tomb. Joseph said, I will do as you say.",
  'explain': ("Machpelah, with Abraham and Isaac. The Latin says from this land, my ancestors’ tomb."),
  'shared': ["I will lie with my fathers.", "Carry me out of Egypt and bury me in their tomb.", "Joseph said, I will do as you have said."],
  'instructions': [ins(K, S, "Joseph promised to bury Jacob in Canaan."), ins(W, R, "“Carry me out of Egypt”: Jacob will not stay even dead. The promise of land is kept for him in a grave, as for Abraham, and the carrying out of Egypt is rehearsed in a coffin.")],
  'entries': ['jacob', 'egypt', 'hebron'],
  'lost': [between("Latin “carry me from this land and bury me in my ancestors’ tomb … as you have commanded” varies; Hebrew, Greek and King James “out of Egypt … in their buryingplace … as thou hast said.”")]},

 '47:31': {
  'received': "Swear to me, he said; Joseph swore, and Israel bowed at the head of the bed.",
  'explain': ("The Hebrew consonants mth read as mittah, bed, by the Masoretes, and matteh, staff, by the Greek; Hebrews 11:21 follows the Greek, worshipped leaning on the top of his staff. The Latin worshipped God toward the head of his bed."),
  'shared': ["He said, Swear to me.", "He swore to him.", "Israel bowed in worship."],
  'instructions': [ins(K, S, "Joseph swore, and Jacob bowed in worship."), ins(W, R, "Bed or staff, the old man bows: in thanks for the oath, or to the God who kept him. One unpointed word, read two ways, gives two pictures of a dying man’s worship, and both are true of him.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew al-rosh ha-mittah, “upon the head of the bed,” becomes Greek epi to akron tēs rhabdou autou, “upon the top of his staff,” reading matteh for mittah; Hebrews 11:21 cites the Greek."), between("Latin “worshipped God, turning toward the head of his bed” and King James “bowed himself upon the bed’s head” follow the Hebrew.")]},
 }
}
