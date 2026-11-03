# Study prose for Genesis 43 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 43,
 'chapterNote': (
  "The second journey: Judah’s pledge, Jacob’s surrender of Benjamin, the gifts and double silver, the steward’s reassurance, Simeon restored, Joseph’s question "
  "about his father, his tears at the sight of Benjamin, and the feast where Benjamin’s portion is five times the others’. The columns agree; the Hebrew keeps “the "
  "famine was severe,” “your brother” without “youngest” in 43:3 and 5, “our little ones,” El Shaddai, “if I am bereaved, I am bereaved,” “peace to you,” “the God "
  "of your father,” “they would eat bread there,” “to the ground,” “asked them of their welfare,” and “God be gracious to you, my son.” The Greek keeps “prevailed,” "
  "“youngest” added twice, “our households,” “my God,” “as I have been bereaved, I have been bereaved,” Benjamin “his brother by the same mother” in 43:16, “may you "
  "find favour,” “the God of your fathers,” “Joseph was about to dine there,” “faces to the ground,” “How are you? Is your father healthy?”, an added “May that man be "
  "blessed by God,” and “mercy to you, child.” Six Hebrew-column renderings were corrected today. The Latin and King James follow the Hebrew."),
 'verses': {

 '43:1': {
  'received': "The famine was severe in the land.",
  'explain': ("Kaved, heavy, as in 12:10 and 41:31. The Greek says prevailed; the Latin pressed heavily upon the whole land. The Hebrew-column rendering was corrected today."),
  'shared': ["The famine.", "It was severe.", "It was in the land."],
  'instructions': [ins(K, S, "The famine continued to press on Canaan.")],
  'entries': [],
  'lost': [between("Hebrew kaved, “heavy,” is Greek enischysen, “prevailed”; Latin “pressed heavily upon the whole land,” King James “was sore.”")]},

 '43:2': {
  'received': "When the grain from Egypt was eaten, their father told them to go again and buy a little food.",
  'explain': ("Hunger decides what Jacob would not. A little food: the modesty of a frightened man. The versions agree."),
  'shared': ["They had finished the grain they brought from Egypt.", "Their father said to them, Go again.", "Buy us a little food."],
  'instructions': [ins(K, S, "Jacob sent the brothers back to Egypt."), ins(W, R, "Jacob says go again as if Benjamin were not the price; hunger lets him ask for food and leave the condition unspoken, and Judah will speak it.")],
  'entries': ['jacob', 'egypt'],
  'lost': [AGREE]},

 '43:3': {
  'received': "Judah said: the man solemnly warned us, You shall not see my face unless your brother is with you.",
  'explain': ("Judah now speaks for the brothers, as he will for the rest of the story. The Hebrew says your brother; the Greek your youngest brother; the Latin under oath."),
  'shared': ["Judah spoke to him.", "The man solemnly warned us.", "You shall not see my face unless your brother is with you."],
  'instructions': [ins(K, S, "Judah reminded Jacob of Joseph’s condition."), ins(W, R, "Judah takes the lead that Reuben lost; the brother who sold Joseph for profit is the one who will offer himself for Benjamin, and his rise begins with telling his father the hard truth.")],
  'entries': [],
  'lost': [keeps("An added ho neōteros, “the youngest,” after brother in the Greek."), between("Latin “solemnly warned us under oath … your youngest brother” adds both; King James “except your brother be with you.”")]},

 '43:4': {
  'received': "If you send our brother with us, we will go down and buy you food.",
  'explain': ("The versions agree."),
  'shared': ["If you will send our brother with us.", "We will go down.", "We will buy food for you."],
  'instructions': [ins(K, S, "Judah made Benjamin the condition of going.")],
  'entries': [],
  'lost': [AGREE]},

 '43:5': {
  'received': "If not, we will not go, for the man said, You shall not see my face unless your brother is with you.",
  'explain': ("The Greek adds youngest again; the Latin as we have often said."),
  'shared': ["If you will not send him, we will not go down.", "The man said to us.", "You shall not see my face unless your brother is with you."],
  'instructions': [ins(K, S, "Judah refused to go without Benjamin.")],
  'entries': [],
  'lost': [keeps("An added ho neōteros, “the youngest,” again in the Greek."), between("Latin “as we have often said … your youngest brother”; King James “except your brother be with you.”")]},

 '43:6': {
  'received': "Israel said: Why did you treat me so badly as to tell the man you had another brother?",
  'explain': ("Israel, the name of the man who strove with God, blaming his sons for honesty. The Latin says to my misery."),
  'shared': ["Israel said.", "Why did you treat me so badly?", "You told the man you had another brother."],
  'instructions': [ins(K, S, "Jacob blamed his sons for mentioning Benjamin."), ins(W, R, "Jacob reproaches his sons for telling the truth; the man who lived by deception now wishes they had deceived. Fear is making him ask for the family vice.")],
  'entries': ['jacob'],
  'lost': [between("Latin “You have done this to my misery” for Hebrew lammah hare‘otem li, “why have you done evil to me?”; Greek and King James keep the question.")]},

 '43:7': {
  'received': "They said: the man questioned us closely about our family: is your father alive, have you a brother? We answered him. How could we know he would say, Bring your brother down?",
  'explain': ("A fair defence; the questions were Joseph’s. The Hebrew says according to these words; the Greek according to his questioning. The Hebrew-column rendering was corrected today."),
  'shared': ["The man questioned us closely about ourselves and our family: Is your father alive? Have you another brother?", "We answered him according to these words.", "Could we know he would say, Bring your brother down?"],
  'instructions': [ins(K, S, "The brothers defended their honesty with Joseph.")],
  'entries': [],
  'lost': [between("Hebrew al-pi ha-devarim ha-elleh, “according to these words,” is Greek kata tēn eperōtēsin tautēn, “according to this questioning”; Latin “following his questions,” King James “according to the tenor of these words.”")]},

 '43:8': {
  'received': "Judah said: Send the boy with me and we will go, that we may live and not die, we, you and our little ones.",
  'explain': ("Judah’s plea, with the household’s life in it. The Hebrew says our little ones; the Greek our households; the Latin we and our little ones, omitting you."),
  'shared': ["Send the boy with me and we will arise and go.", "That we may live and not die.", "We, you, and our little ones."],
  'instructions': [ins(K, S, "Judah urged Jacob to send Benjamin for all their sakes."), ins(W, R, "“That we may live and not die, we, you, and our little ones”: Judah widens the question from one son to three generations. The famine is the argument, and it is a true one.")],
  'entries': [],
  'lost': [between("Hebrew tappenu, “our little ones,” is Greek hē aposkeuē hēmōn, “our households” or baggage; Latin “we and our little ones” drops “you”; King James “both we, and thou, and also our little ones.”")]},

 '43:9': {
  'received': "I will be his surety; require him from my hand. If I do not bring him back and set him before you, I will bear the blame forever.",
  'explain': ("Judah offers himself, not his sons; the pledge Reuben could not make. Arav, surety, the word of Proverbs. The versions agree."),
  'shared': ["I myself will be his guarantor; from my hand you shall require him.", "If I do not bring him back and set him before you.", "Let me bear the blame forever."],
  'instructions': [ins(K, S, "Judah pledged himself for Benjamin."), ins(W, R, "“Let me bear the blame forever”: Judah, who said “what profit” over the pit, now puts himself in pawn for Rachel’s son. The pledge is kept in 44:33, and David’s tribe is made in the keeping.")],
  'entries': [],
  'lost': [AGREE]},

 '43:10': {
  'received': "Had we not delayed, we could have been back twice by now.",
  'explain': ("A reproach to the father’s hesitation. The versions agree."),
  'shared': ["If we had not delayed.", "Surely by now.", "We could have returned twice."],
  'instructions': [ins(K, S, "Judah noted the cost of delay.")],
  'entries': [],
  'lost': [AGREE]},

 '43:11': {
  'received': "Israel said: If it must be, take the land’s best in your bags as a gift: a little balm, honey, spices, ladanum, pistachios and almonds.",
  'explain': ("Jacob yields, and manages the yielding with gifts, as he managed Esau. Balm and ladanum, the Ishmaelites’ goods of 37:25. The Hebrew says a little balm, a little honey; the Greek resin, aromatics, nuts; the Latin storax."),
  'shared': ["If it must be so, do this.", "Take some of the land’s choice produce in your bags as a gift for the man.", "A little balm, a little honey, spices, ladanum, pistachios and almonds."],
  'instructions': [ins(K, S, "Jacob agreed and sent gifts to the man."), ins(W, R, "Jacob sends the goods of the land to the governor of Egypt, as he sent flocks to Esau; the old man still believes a gift turns a face, and this time he is sending it to his son.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew me‘at tzori u-me‘at devash nekhot va-lot botnim u-shqedim, “a little balm and a little honey, spices and ladanum, pistachios and almonds,” is Greek rhētinēs kai meli, thymiama kai staktēn kai tereminthon kai karya, “resin and honey, aromatics and stacte and terebinth nuts and nuts”; Latin “a little resin, honey, storax, stacte, terebinth nuts, and almonds”; King James “balm … honey, spices, and myrrh, nuts, and almonds.”")]},

 '43:12': {
  'received': "Take double silver, and return the silver found in your sacks; perhaps it was a mistake.",
  'explain': ("Honesty as policy: the returned silver goes back. The Hebrew says in the mouths of your sacks; the Greek in your sacks."),
  'shared': ["Take twice the silver in your hands.", "Carry back the silver that was returned in your sacks.", "Perhaps it was an oversight."],
  'instructions': [ins(C, S, "Take double silver and return what was found in your sacks."), ins(W, R, "Jacob returns the silver his sons once took for a brother; he does not know the symmetry, and it is the first honest thing the family has done with silver.")],
  'entries': [],
  'lost': [between("Hebrew be-fi amtechotekhem, “in the mouth of your sacks,” is Greek en tois marsippois hymōn, “in your sacks”; Latin “in the sacks,” King James “in the mouth of your sacks.”")]},

 '43:13': {
  'received': "Take your brother too, and go back to the man.",
  'explain': ("Said at last, in a subordinate clause. The Hebrew says arise, return; the Greek go down again. The Hebrew-column rendering was corrected today."),
  'shared': ["Take your brother also.", "Arise.", "Return to the man."],
  'instructions': [ins(C, S, "Take your brother also and return to the man."), ins(W, R, "“Take your brother also”: Benjamin is surrendered in six words after a chapter of refusal. Jacob gives up Rachel’s son to hunger, as he gave up Joseph to his brothers, and this time God gives him back.")],
  'entries': [],
  'lost': [between("Hebrew qumu shuvu el-ha-ish, “arise, return to the man,” is Greek anastantes katabēte pros ton anthrōpon, “arise, go down to the man”; Latin and King James follow the Hebrew.")]},

 '43:14': {
  'received': "May El Shaddai grant you mercy before the man, that he release your other brother and Benjamin. As for me, if I am bereaved, I am bereaved.",
  'explain': ("Jacob’s prayer and his resignation. El Shaddai, the name of the Bethel blessing. The Hebrew says if I am bereaved; the Greek my God, as I have been bereaved, I have been bereaved; the Latin I shall be as one bereaved and childless."),
  'shared': ["May God Almighty grant you mercy before the man.", "May he release your other brother and Benjamin.", "As for me, if I am bereaved, I am bereaved."],
  'instructions': [ins(K, S, "Jacob prayed and resigned himself to loss."), ins(W, R, "“If I am bereaved, I am bereaved”: Jacob commits his sons to El Shaddai and braces for the worst. It is the nearest he comes to Abraham on Moriah, and he does not know the lost son is the one he is sending to.")],
  'entries': ['el-shaddai', 'jacob'],
  'lost': [loses("Hebrew El Shaddai becomes Greek ho theos mou, “my God”; Hebrew ka-asher shakholti shakhalti, “as I am bereaved, I am bereaved,” becomes Greek egō men gar katha ēteknōmai ēteknōmai, “as I have been bereaved, I have been bereaved.”"), between("Latin “my God Almighty … I shall be as one bereaved and childless” and King James “God Almighty … If I be bereaved of my children, I am bereaved” keep the name.")]},

 '43:15': {
  'received': "The men took the gift, double silver and Benjamin, went down to Egypt and stood before Joseph.",
  'explain': ("Eleven before Joseph: the eleven stars. The versions agree."),
  'shared': ["The men took the gift and double silver.", "They took Benjamin and went down to Egypt.", "They stood before Joseph."],
  'instructions': [ins(K, S, "All eleven brothers stood before Joseph."), ins(W, R, "Eleven brothers stand before Joseph; the second dream’s count is complete, and only the sun and moon are missing.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '43:16': {
  'received': "Joseph saw Benjamin with them and told his steward to bring the men home and prepare a meal: they will dine with me at noon.",
  'explain': ("Joseph sees Benjamin and changes course: hospitality. The Greek adds his brother by the same mother; the Latin a feast."),
  'shared': ["Joseph saw Benjamin with them.", "He said to his steward, Bring the men into the house, slaughter and prepare.", "The men will eat with me at noon."],
  'instructions': [ins(K, S, "Joseph ordered a meal for his brothers."), ins(W, R, "He sees Benjamin and orders dinner; the test is not over, but the sight of his mother’s son turns the governor into a host.")],
  'entries': [],
  'lost': [keeps("An added ton adelphon autou ton homomētrion, “his brother by the same mother,” after Benjamin in the Greek."), between("Latin “When he saw them and Benjamin together,” King James “when Joseph saw Benjamin with them.”")]},

 '43:17': {
  'received': "The steward did as Joseph said and brought the men into Joseph’s house.",
  'explain': ("The versions agree."),
  'shared': ["The man did as Joseph said.", "He brought the men.", "Into Joseph’s house."],
  'instructions': [ins(K, S, "The brothers were brought into Joseph’s house.")],
  'entries': [],
  'lost': [AGREE]},

 '43:18': {
  'received': "The men were afraid at being brought in: it is because of the silver, so he can find a pretext, fall on us and take us as slaves with our donkeys.",
  'explain': ("Fear reads hospitality as a trap. Slaves, the fate they gave Joseph. The Hebrew says were afraid, find a pretext; the Greek seeing, accuse us falsely; the Latin terrified."),
  'shared': ["The men were afraid because they were brought into Joseph’s house.", "It is because of the silver returned to our sacks the first time.", "He will find a pretext against us, attack us, and take us as slaves with our donkeys."],
  'instructions': [ins(K, S, "The brothers feared enslavement over the silver."), ins(W, R, "They fear being made slaves for silver; that is exactly what they did to Joseph, and the fear is the shape of their guilt. Joseph means them dinner.")],
  'entries': [],
  'lost': [between("Hebrew va-yir’u ha-anashim, “and the men were afraid,” is Greek idontes de hoi andres, “seeing, the men”; Hebrew le-hitgolel alenu, “to roll upon us,” is Greek tou sykophantēsai hēmas, “to accuse us falsely”; Latin “They were terrified there,” King James “the men were afraid.”")]},

 '43:19': {
  'received': "They went to the steward of Joseph’s house and spoke to him at the door.",
  'explain': ("Confession at the threshold, before entering. The Hebrew says doorway; the Greek gateway. The Hebrew-column rendering was corrected today."),
  'shared': ["They approached the man over Joseph’s house.", "They spoke to him.", "At the door of the house."],
  'instructions': [ins(K, S, "The brothers explained themselves to the steward.")],
  'entries': [],
  'lost': [between("Hebrew petach ha-bayit, “the opening of the house,” is Greek en tō pylōni tou oikou, “in the gateway of the house”; Latin “at the doorway itself,” King James “at the door of the house.”")]},

 '43:20': {
  'received': "Please, my lord, we came down the first time to buy food.",
  'explain': ("The versions agree; the Latin hear us."),
  'shared': ["Please, my lord.", "We came down the first time.", "To buy food."],
  'instructions': [ins(K, S, "The brothers began their explanation.")],
  'entries': [],
  'lost': [AGREE]},

 '43:21': {
  'received': "At the lodging place we opened our sacks and each man’s silver was there in full weight; we have brought it back.",
  'explain': ("Their retelling compresses the two discoveries of 42:27 and 35 into one. The Latin adds after buying it."),
  'shared': ["When we came to the lodging place and opened our sacks, each man’s silver was in the mouth of his sack.", "It was our silver at full weight.", "We have brought it back in our hands."],
  'instructions': [ins(K, S, "The brothers reported the returned silver.")],
  'entries': [],
  'lost': [between("Latin “After buying it, when we came to a lodging place” adds; Hebrew, Greek and King James “when we came to the inn.”")]},

 '43:22': {
  'received': "We have brought other silver to buy food; we do not know who put the silver in our sacks.",
  'explain': ("The versions agree."),
  'shared': ["We have brought other silver to buy food.", "We do not know.", "Who put the silver in our sacks."],
  'instructions': [ins(K, S, "The brothers offered to pay again."), ins(W, R, "“We do not know who put it there”: the brothers have become honest men with silver, and the steward knows who put it there, and so does the reader.")],
  'entries': [],
  'lost': [AGREE]},

 '43:23': {
  'received': "He said: Peace to you, do not fear; your God and your father’s God gave you treasure in your sacks; I had your silver. And he brought Simeon out.",
  'explain': ("The steward speaks Joseph’s theology: your father’s God put it there. Simeon returned. The Hebrew says peace to you, the God of your father, I received your silver; the Greek may you find favour, the God of your fathers, your good silver in full; the Latin the verified money."),
  'shared': ["Peace to you; do not fear.", "Your God and the God of your father has given you treasure in your sacks; I had your silver.", "He brought Simeon out to them."],
  'instructions': [ins(K, S, "The steward reassured the brothers and freed Simeon."), ins(W, R, "An Egyptian steward tells Hebrew shepherds that their father’s God gave them treasure; Joseph has taught his household his faith, and uses a servant to preach it to his brothers.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew shalom lakhem, “peace to you,” is Greek hileōs hymin, “favour to you”; Hebrew Elohe avikhem, “the God of your father,” is Greek ho theos tōn paterōn hymōn, “the God of your fathers”; Hebrew kaspekhem ba elai, “your silver came to me,” is Greek to de argyrion hymōn eudokimoun apechō, “your good silver I have received in full”; Latin “Peace to you … the verified money”; King James “Peace be to you … I had your money.”")]},

 '43:24': {
  'received': "He brought them into Joseph’s house, gave them water to wash their feet, and fed their donkeys.",
  'explain': ("Hospitality, as Abraham’s and Laban’s. The Greek lacks the second entry into the house."),
  'shared': ["He brought the men into Joseph’s house.", "He gave them water and they washed their feet.", "He gave their donkeys fodder."],
  'instructions': [ins(K, S, "The brothers were received as guests.")],
  'entries': [],
  'lost': [loses("Hebrew va-yave ha-ish et-ha-anashim betah Yosef, “and the man brought the men into Joseph’s house,” is absent from the Greek, which begins with the water."), between("Latin “He brought them into the house, supplied water” and King James keep it.")]},

 '43:25': {
  'received': "They prepared the gift for Joseph’s coming at noon, for they heard they would eat bread there.",
  'explain': ("The Hebrew says they would eat bread there; the Greek Joseph was about to dine there."),
  'shared': ["They prepared the gift.", "It was for Joseph’s arrival at noon.", "They had heard they would eat bread there."],
  'instructions': [ins(K, S, "The brothers readied Jacob’s gift for Joseph.")],
  'entries': [],
  'lost': [between("Hebrew ki-sham yokhlu lachem, “that there they would eat bread,” is Greek hoti ekei mellei aristan, “that he was about to dine there”; Latin and King James follow the Hebrew.")]},

 '43:26': {
  'received': "When Joseph came home they brought him the gift and bowed to the ground.",
  'explain': ("The second bowing, now eleven, with gifts: the dream again. The Greek adds faces. The Hebrew-column rendering was corrected today."),
  'shared': ["Joseph came into the house.", "They brought him the gift in their hands into the house.", "They bowed down to him to the ground."],
  'instructions': [ins(K, S, "The brothers presented gifts and bowed to Joseph."), ins(W, R, "Eleven bow with gifts: Jacob’s present to the man is Jacob’s homage to his son, carried by hands that once lowered him into a pit.")],
  'entries': [],
  'lost': [keeps("An added epi prosōpon, “with their faces,” in the Greek: “to the ground on their faces.”"), between("Hebrew, Latin and King James “bowed to the ground.”")]},

 '43:27': {
  'received': "He asked after their welfare and said: Is your father well, the old man you spoke of? Is he still alive?",
  'explain': ("The question Joseph most wants answered, asked in form. The Hebrew says asked of their welfare, is your father well; the Greek How are you? Is your father healthy?; the Latin greeted them kindly. The Hebrew-column rendering was corrected today."),
  'shared': ["He asked them about their welfare.", "Is your father well, the old man of whom you spoke?", "Is he still alive?"],
  'instructions': [ins(K, S, "Joseph asked after Jacob."), ins(W, R, "“Is your father still alive?” is the governor’s courtesy and the son’s ache; Joseph asks about Jacob as a stranger, and the reader hears the twenty-two years in it.")],
  'entries': [],
  'lost': [between("Hebrew va-yish’al lahem le-shalom va-yomer ha-shalom avikhem, “and he asked them of welfare and said, Is your father well,” is Greek ērōtēsen de autous, pōs echete … ei hygiainei ho patēr hymōn, “he asked them, How are you? … Is your father healthy?”; Latin “He greeted them kindly in return and asked,” King James “asked them of their welfare.”")]},

 '43:28': {
  'received': "Your servant our father is well, still alive. They bowed low in homage.",
  'explain': ("Your servant our father: Jacob called a servant to his son; the sun bows in the sons’ words. The Greek adds Joseph’s reply, May that man be blessed by God."),
  'shared': ["Your servant our father is well; he is still alive.", "They bowed their heads.", "They prostrated themselves."],
  'instructions': [ins(K, S, "The brothers reported Jacob alive and bowed."), ins(W, R, "“Your servant our father”: Jacob is named Joseph’s servant by his sons. The second dream, sun and moon bowing, is fulfilled in a phrase of court manners.")],
  'entries': [],
  'lost': [keeps("An added kai eipen, eulogētos ho anthrōpos ekeinos tō theō, “and he said, Blessed be that man by God,” in the Greek."), between("Hebrew, Latin and King James have only the answer and the bowing.")]},

 '43:29': {
  'received': "He saw Benjamin, his mother’s son: Is this your youngest brother you spoke of? God be gracious to you, my son.",
  'explain': ("His mother’s son: the narrator says what Joseph cannot. The blessing is in the Hebrew idiom of a father. The Greek says whom you said you would bring, mercy, child; the Latin little brother."),
  'shared': ["He saw Benjamin his brother, his mother’s son.", "Is this your youngest brother, of whom you spoke to me?", "God be gracious to you, my son."],
  'instructions': [ins(K, S, "Joseph blessed Benjamin without revealing himself."), ins(W, R, "“God be gracious to you, my son”: Joseph blesses his full brother as a stranger blesses a boy. The word gracious, chanan, is in Benjamin’s own name-giving, 33:5; Joseph speaks their father’s language without being known.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew asher amartem elai, “of whom you spoke to me,” is Greek hon eipate pros me agagein, “whom you said you would bring to me”; Hebrew Elohim yochnekha beni, “God be gracious to you, my son,” is Greek ho theos eleēsai se, teknon, “God have mercy on you, child”; Latin “little brother … May God have mercy on you, my son”; King James “younger brother … God be gracious unto thee, my son.”")]},

 '43:30': {
  'received': "Joseph hurried out, his heart yearning for his brother, and sought a place to weep; he went into his room and wept.",
  'explain': ("The second weeping. Nikhmeru rachamav, his compassion grew hot, the bowels of the King James. The Hebrew says hurried; the Greek was troubled; the Latin tears were breaking forth."),
  'shared': ["Joseph was deeply moved for his brother.", "He sought a place to weep.", "He went into his chamber and wept there."],
  'instructions': [ins(K, S, "Joseph wept privately at the sight of Benjamin."), ins(W, R, "He must leave the room to weep; the disguise costs Joseph more than the brothers, and the reader is let into the chamber they are not.")],
  'entries': [],
  'lost': [between("Hebrew va-yemaher Yosef, “and Joseph hurried,” is Greek etarachthē de Iōsēph, “and Joseph was troubled”; Hebrew nikhmeru rachamav, “his compassions grew warm,” Greek synestrepheto ta entera autou, “his innards were wrung”; Latin “He hurried away … tears were breaking forth,” King James “made haste; for his bowels did yearn.”")]},

 '43:31': {
  'received': "He washed his face, came out, controlled himself, and said, Serve the bread.",
  'explain': ("Vayitappaq, restrained himself, the verb of 45:1 when he can no longer. The versions agree."),
  'shared': ["He washed his face and came out.", "He restrained himself.", "Set on the bread."],
  'instructions': [ins(K, S, "Joseph composed himself and ordered the meal."), ins(W, R, "Washed face, restrained heart, dinner served: Joseph governs himself as he governs Egypt, and the restraint will break in two chapters.")],
  'entries': [],
  'lost': [AGREE]},

 '43:32': {
  'received': "They served him alone, the brothers alone, and the Egyptians alone, for Egyptians may not eat with Hebrews; it is an abomination to them.",
  'explain': ("Three tables: Joseph by rank, the Egyptians by caste, the Hebrews by foreignness. The Latin says regard such a meal as profane."),
  'shared': ["They served him by himself, them by themselves, and the Egyptians by themselves.", "The Egyptians could not eat bread with the Hebrews.", "That is an abomination to the Egyptians."],
  'instructions': [ins(K, S, "The meal was served at separate tables by custom."), ins(W, R, "Joseph eats alone, between his Egyptians and his Hebrews; the seating is the man’s life, belonging wholly to neither table.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew to‘evah, “abomination,” is Greek bdelygma; Latin “regard such a meal as profane,” King James “an abomination unto the Egyptians.”")]},

 '43:33': {
  'received': "They were seated before him by age, eldest to youngest, and looked at one another in amazement.",
  'explain': ("A stranger seats eleven brothers in birth order; the amazement is the clue they do not take. The versions agree in substance."),
  'shared': ["They sat before him in order of age.", "From the firstborn to the youngest.", "The men looked at one another in astonishment."],
  'instructions': [ins(K, S, "Joseph seated his brothers in exact birth order."), ins(W, R, "Seated by age by a man who could not know their ages: Joseph plays with the knowledge he has, and the brothers marvel and still do not see.")],
  'entries': [],
  'lost': [between("Hebrew ha-bekhor ki-vkhorato ve-ha-tza‘ir ki-tz‘irato, “the firstborn by his birthright and the youngest by his youth,” is Greek ho prōtotokos kata ta presbeia autou kai ho neōteros kata tēn neotēta autou; Latin “marvelled greatly,” King James “the men marvelled one at another.”")]},

 '43:34': {
  'received': "Portions came from his table, Benjamin’s five times the others’; they drank and were merry with him.",
  'explain': ("Five times: Joseph tests whether the brothers can bear a favourite now. They drink and are merry, shakhar, grow drunk. The versions agree."),
  'shared': ["Portions were brought to them from his table.", "Benjamin’s portion was five times any of theirs.", "They drank and were merry with him."],
  'instructions': [ins(K, S, "Joseph favoured Benjamin at the feast."), ins(W, R, "Benjamin gets five portions and no one hates him; the brothers who could not bear a coat can bear a favourite now. The test is passed at a table, and Joseph sees it.")],
  'entries': [],
  'lost': [AGREE]},
 }
}
