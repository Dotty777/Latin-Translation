# Study prose for Genesis 12 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 12,
 'chapterNote': (
  "The call, the journey, the altars and the episode in Egypt are the same story in every column. What varies is at the edges of the "
  "promise and in the Egyptian scene. The Hebrew keeps “go for yourself,” the command “be a blessing,” two different verbs for treating "
  "Abram lightly and cursing him, the oak of Moreh, the journey toward the Negev, “the woman was taken,” a single benefactor in Egypt, "
  "female donkeys, and YHWH striking Pharaoh with plagues. The Greek keeps a plain “go out,” the promise “you shall be blessed,” one verb "
  "for cursing, “the high oak,” an encampment in the wilderness, the officials who bring her to Pharaoh, plural benefactors, calves and "
  "mules, God afflicting Pharaoh with grievous afflictions, “hurry away,” and Lot named in Pharaoh’s order. The Latin and King James follow "
  "the Hebrew; the Latin alone has “the renowned valley” at Shechem."),
 'verses': {

 '12:1': {
  'received': "The Lord told Abram to leave his land, his kindred and his father’s house for a land he would show him.",
  'explain': ("The call moves outward in three circles, land, wider kin, the father’s own household, each closer and harder to leave, and "
   "the destination is withheld. The Hebrew says lekh lekha, go for yourself; the Greek a plain “go out,” the word Stephen quotes in "
   "Acts. Hebrews says Abraham went out not knowing where he was going."),
  'shared': ["The Lord spoke to Abram.", "He is to leave his land, his kindred and his father’s house.", "He is to go to a land God will show him."],
  'instructions': [ins(C, S, "Go out from your land, your kindred and your father’s house to the land I will show you."), ins(W, R, "Obedience here means leaving before knowing; the land is shown only to the one already on the way.")],
  'entries': ['abraham', 'haran', 'lord-translation'],
  'lost': [
   loses("Hebrew lekh-lekha, “go for yourself,” adds a personal pronoun to the command that Rashi and others read closely; Greek exelthe, “go out,” has no equivalent for lekha. The Hebrew YHWH is “the Lord.”"),
   keeps("Exelthe is the word Stephen quotes in Acts 7:3; Hebrews 11:8 reads the going-out as faith."),
   between("Latin “go out … and come into the land” and King James “get thee out of thy country” both render the command without the Hebrew’s pronoun."),
  ]},

 '12:2': {
  'received': "God promised to make Abram a great nation, to bless him and make his name great, so that blessing would attach to him.",
  'explain': ("The first of the promises: a nation, a blessing, a name. The name the builders of Babel wanted to make for themselves is here "
   "given as a gift. The last clause divides the texts. The Hebrew is an imperative, “be a blessing”; the Greek, Latin and King James "
   "give a promise, “you shall be blessed” or “thou shalt be a blessing.” The promise is repeated to Ishmael and to Jacob and fulfilled in Egypt."),
  'shared': ["God will make Abram a great nation.", "God will bless him.", "God will make his name great."],
  'instructions': [ins(K, S, "God promised Abram nationhood, blessing and a great name."), ins(W, R, "The great name refused to Babel is granted to the man who left his own; a name is received, not built.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew ve-heyeh berakhah, “and be a blessing,” is an imperative giving Abram a role. Greek kai esē eulogētos, “and you shall be blessed,” is a promise of blessing received. The command is gone from the Greek."),
   keeps("Greek megalynō to onoma sou, “I will make your name great,” answers the “let us make a name for ourselves” of 11:4 and anticipates 2 Samuel 7:9."),
   between("Latin “and you shall be blessed” follows the Greek; King James “thou shalt be a blessing” keeps the Hebrew noun but as a promise. Deuteronomy 26:5 sees the great nation in Egypt."),
  ]},

 '12:3': {
  'received': "God will bless those who bless Abram and curse those who curse him, and through him all the families of the earth will be blessed.",
  'explain': ("The promise widens from Abram to everyone who meets him and then to the whole earth. The Hebrew uses two different verbs, "
   "the one who treats you lightly I will curse, with a singular offender; the Greek uses one verb for both and plural offenders. The "
   "Hebrew says the families of the ground, the Greek the tribes of the earth. Peter and Paul both quote the last clause for the nations."),
  'shared': ["God will bless those who bless Abram.", "God will curse those who curse him.", "In him all the families of the earth will be blessed."],
  'instructions': [ins(K, S, "Through Abram all the families of the earth will be blessed."), ins(W, R, "The blessing of one man is for everyone; the particular choice serves the universal promise.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew meqallelkha a’or, “the one who treats you lightly I will curse,” uses two verbs, qalal and arar, and a singular offender. Greek tous kataromenous se katarasomai, “those who curse you I will curse,” uses one verb twice and a plural. Hebrew mishpechot ha-adamah, “families of the ground,” is Greek phylai tēs gēs, “tribes of the earth.”"),
   between("Latin “curse those who curse you … families of the earth” sits nearer the Greek; King James “curse him that curseth thee … families of the earth” keeps the singular. Acts 3:25 and Galatians 3:8 quote the promise; Numbers 24:9 repeats the pairing."),
  ]},

 '12:4': {
  'received': "Abram went as the Lord had told him, with Lot, at seventy-five years old.",
  'explain': ("The obedience is one verb: Abram went. Lot goes with him, and his age is given, seventy-five, already old and childless; "
   "twenty-five years will pass before Isaac is born. All versions agree, with the Latin saying commanded where the others say spoken."),
  'shared': ["Abram went as the Lord had spoken to him.", "Lot went with him.", "Abram was seventy-five when he left Haran."],
  'instructions': [ins(K, S, "Abram obeyed the call at seventy-five, taking Lot with him."), ins(W, R, "Age is no bar to the call; the promise is given to a man past the time of hope.")],
  'entries': ['abraham', 'haran'],
  'lost': [between("Hebrew YHWH is Greek kyrios; Latin “as the Lord had commanded him” for “spoken.” The age is the same in all four. Genesis 17:17, 21:5 and Romans 4:19 measure the wait.")]},

 '12:5': {
  'received': "Abram took Sarai, Lot, their possessions and the people gained in Haran, and came to the land of Canaan.",
  'explain': ("Abram does not leave as a poor wanderer; he travels as the head of a household with flocks, goods and people. The Hebrew says "
   "the persons they had “made” in Haran, an idiom for acquiring servants; the Greek says acquired, the same verb as for the possessions. "
   "The land is named Canaan, after Ham’s son on whom the curse fell, and they arrive."),
  'shared': ["Abram took Sarai, Lot and all their possessions.", "He took the people gained in Haran.", "They set out for Canaan and arrived there."],
  'instructions': [ins(K, S, "Abram’s household travelled from Haran and arrived in Canaan.")],
  'entries': ['abraham', 'sarah', 'canaan', 'haran'],
  'lost': [
   loses("Hebrew ha-nefesh asher asu, “the persons they had made,” is an idiom the Greek renders pasan psychēn hēn ektēsanto, “every person they had acquired,” repeating the verb of the possessions. The Hebrew’s odd “made” is smoothed away."),
   between("Latin “the people they had gathered” and King James “the souls that they had gotten” render the sense; the Latin runs the arrival into 12:6. Greek Chanaan is Hebrew Kena‘an."),
  ]},

 '12:6': {
  'received': "Abram passed through the land to Shechem and the oak there, while the Canaanites still held the land.",
  'explain': ("The first stop in the land is Shechem, where Jacob will buy ground, Joseph’s bones will be buried and Joshua will renew the "
   "covenant. The Hebrew names the oak of Moreh; the Greek calls it the high oak; the Latin the renowned valley. The note that the "
   "Canaanites were in the land makes the promise a hope: Abram receives it while others hold it."),
  'shared': ["Abram passed through the land.", "He came to the place of Shechem and its oak.", "The Canaanites were then in the land."],
  'instructions': [ins(K, S, "Abram’s first station in the land was Shechem, held by the Canaanites."), ins(W, R, "The land is promised while others possess it; faith lives in tents among the present owners.")],
  'entries': ['abraham', 'canaan'],
  'lost': [
   loses("Hebrew elon Moreh, “the oak of Moreh,” is a named tree; Greek tēn dryn tēn hypsēlēn, “the high oak,” describes it and drops the name. Hebrew “passed through the land” is Greek “travelled through the length of the land.” The two tree-names should not be combined into one."),
   between("Latin “the renowned valley” takes Moreh as a word for teaching or fame and the oak as a valley; King James “the plain of Moreh” keeps the name with another noun. Joshua 24:1 and John 4:5 return to Shechem."),
  ]},

 '12:7': {
  'received': "The Lord appeared to Abram, promised the land to his offspring, and Abram built an altar there.",
  'explain': ("The first time Scripture says the Lord was seen by Abram, and the first time the land is promised to his offspring. Abram "
   "answers with an altar, as he will at Bethel, Hebron and Moriah. The Hebrew says YHWH; the Greek the Lord, and names Abram as the "
   "builder where the Hebrew continues with “he.” The Greek word for appeared is used of the risen Christ."),
  'shared': ["The Lord appeared to Abram.", "He promised the land to Abram’s offspring.", "Abram built an altar there to the Lord."],
  'instructions': [ins(K, S, "God promised the land to Abram’s offspring and Abram worshipped in response."), ins(W, R, "An altar is the right answer to a promise; Abram claims the land first by worship, not by conquest.")],
  'entries': ['abraham', 'altar', 'yhwh-yahweh', 'lord-translation'],
  'lost': [
   loses("Hebrew YHWH twice becomes Greek kyrios twice; Hebrew “he built” becomes Greek “Abram built,” supplying the name."),
   keeps("Greek ōphthē, “appeared,” is the form of Luke 24:34 and 1 Corinthians 15:5, and of Acts 7:2; the Greek reader hears the same word for God seen by Abram and Christ seen by the apostles."),
   between("Latin and King James keep “he built” with the Hebrew. Genesis 8:20 had the first altar; 13:18 and 22:9 are the next."),
  ]},

 '12:8': {
  'received': "Abram moved to the hills east of Bethel, pitched his tent between Bethel and Ai, built an altar and called on the Lord’s name.",
  'explain': ("The second station is between Bethel, “house of God,” a name the place will receive from Jacob, and Ai, “the ruin,” where Joshua "
   "will suffer his first defeat. The Hebrew places Bethel “toward the sea,” which the Hebrew column gives as west and the Greek keeps "
   "literally; both mean the same. Abram builds a second altar and calls on the name of the Lord, the phrase of 4:26."),
  'shared': ["Abram moved to the hill country east of Bethel and pitched his tent.", "Bethel lay west and Ai east.", "He built an altar and called on the name of the Lord."],
  'instructions': [ins(K, S, "Abram worshipped at a second altar between Bethel and Ai."), ins(W, R, "Each stage of the journey is marked by prayer; the tent moves, the altars remain.")],
  'entries': ['abraham', 'bethel', 'altar'],
  'lost': [between("Hebrew mi-yam, “from the sea,” is Greek kata thalassan, “toward the sea,” both meaning west in this land; the Hebrew column prints “west.” Latin “called upon His name” drops the repeated Lord; King James keeps both. Genesis 28:19 gives Bethel its name; Joshua 7:2–5 is Ai.")]},

 '12:9': {
  'received': "Abram journeyed on, southward.",
  'explain': ("The versions part over a short verse. The Hebrew, Latin and King James have Abram continuing his journey toward the Negev, "
   "the south; the Greek has him depart, travel on and encamp in the wilderness. The Hebrew describes direction, the Greek a stopping "
   "place. Neither should be filled in from the other."),
  'shared': ["Abram journeyed on.", "He kept moving by stages.", "His way lay to the south."],
  'instructions': [ins(K, S, "Abram continued southward through the land by stages.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew halokh ve-nasoa ha-negbah, “going on and journeying toward the Negev,” gives continued movement south. Greek aparas … eporeuthē kai parenebalen en tē erēmō, “having departed he travelled and encamped in the wilderness,” names a camp and a wilderness and drops the south. The Negev is gone from the Greek."),
   between("Latin “advancing farther toward the south” and King James “going on still toward the south” follow the Hebrew."),
  ]},

 '12:10': {
  'received': "A severe famine drove Abram down to Egypt to live there as a stranger.",
  'explain': ("The promised land fails to feed him, and Abram goes down to Egypt. Famine tests each of the fathers in turn; Isaac faces one, "
   "and Jacob’s whole family goes down to Egypt because of another. The versions agree; the Greek says the famine grew strong, the "
   "Hebrew that it was severe."),
  'shared': ["There was a famine in the land.", "Abram went down to Egypt to sojourn there.", "The famine was severe."],
  'instructions': [ins(K, S, "Famine took Abram from the promised land to Egypt."), ins(W, R, "The land of promise can be a land of hunger; the promise does not exempt Abram from need.")],
  'entries': ['abraham', 'egypt'],
  'lost': [between("Hebrew kaved, “heavy,” is Greek enischysen, “grew strong”; Latin “had become severe,” King James “grievous.” Hebrew lagur and Greek paroikēsai are both “to sojourn,” to live as a resident alien. Genesis 26:1 and 47:4 bring the next famines.")]},

 '12:11': {
  'received': "Nearing Egypt, Abram told Sarai that he knew she was a beautiful woman.",
  'explain': ("The scheme begins with a compliment. The Hebrew has Abram say “Look, I know,” with an appeal before the fact; the Greek "
   "drops the appeal, repeats Abram’s name and says beautiful in face where the Hebrew says in appearance. The fear behind the words comes in the next verse."),
  'shared': ["Abram was about to enter Egypt.", "He spoke to his wife Sarai.", "He said he knew she was a beautiful woman."],
  'instructions': [ins(K, S, "Abram knew Sarai’s beauty would be noticed in Egypt.")],
  'entries': ['abraham', 'sarah'],
  'lost': [between("Hebrew hinneh-na, “look now,” an appeal, is absent from the Greek, which names Abram twice. Hebrew yefat-mar’eh, “beautiful of appearance,” is Greek euprosōpos, “beautiful in face.” Latin “I know you are a beautiful woman” and King James “Behold now, I know that thou art a fair woman” divide.")]},

 '12:12': {
  'received': "Abram feared that the Egyptians would see Sarai, call her his wife, kill him and keep her.",
  'explain': ("The fear is stated plainly: they will kill me and keep you alive. It is the fear of a man who thinks his life depends on his "
   "wits rather than on the promise just given. The Hebrew says keep you alive; the Greek preserve you. The versions agree."),
  'shared': ["The Egyptians will see Sarai.", "They will say she is his wife.", "They will kill Abram and keep her alive."],
  'instructions': [ins(K, S, "Abram feared for his life because of Sarai’s beauty."), ins(W, R, "The man with a promise of descendants fears death in Egypt; fear forgets what faith has just heard.")],
  'entries': ['abraham', 'sarah'],
  'lost': [between("Hebrew yechayyu, “they will keep alive,” is Greek peripoiēsontai, “they will preserve”; neither implies a legal status. Latin and King James agree with the Hebrew.")]},

 '12:13': {
  'received': "Abram asked Sarai to say she was his sister, so that he would be treated well and live because of her.",
  'explain': ("The request is a half-truth; Abraham will later explain that Sarah is his father’s daughter though not his mother’s, and "
   "Isaac will tell the same story of Rebekah. The Hebrew gives the request in the second person, say that you are my sister; the Greek "
   "supplies the words Sarai is to speak, I am his sister. The motive is stated without disguise: that it may go well with me."),
  'shared': ["Abram asked Sarai to say she was his sister.", "He wanted it to go well with him because of her.", "He wanted his life preserved on her account."],
  'instructions': [ins(K, S, "Abram asked Sarai to pass as his sister in Egypt."), ins(W, R, "The father of faith protects himself at his wife’s expense; Scripture records it without excuse.")],
  'entries': ['abraham', 'sarah'],
  'lost': [between("Hebrew imri-na achoti at, “please say, you are my sister,” is Greek eipon oun hoti adelphē autou eimi, “therefore say, I am his sister,” supplying her first-person words. Hebrew nafshi and Greek psychē mou are “my life.” Latin and King James keep the Hebrew form. Genesis 20:12 and 26:7 are the sequels.")]},

 '12:14': {
  'received': "When Abram entered Egypt the Egyptians saw that Sarai was very beautiful.",
  'explain': ("What Abram foresaw happens. Sarai, ten years his junior and so about sixty-five, is noticed. All versions agree; the Greek "
   "sentence runs on into the next verse."),
  'shared': ["Abram entered Egypt.", "The Egyptians saw the woman.", "She was very beautiful."],
  'instructions': [ins(K, S, "Sarai’s beauty was noticed as soon as they entered Egypt.")],
  'entries': ['sarah', 'egypt'],
  'lost': [between("Hebrew, Greek, Latin and King James agree. The Greek does not add “his wife” here; its syntax continues into 12:15. Genesis 17:17 gives the ages.")]},

 '12:15': {
  'received': "Pharaoh’s officials praised Sarai to Pharaoh, and she was taken into his house.",
  'explain': ("The court does what courts did: it reports a beautiful woman to the king, and she is brought to the royal house. Pharaoh is a "
   "title, from the Egyptian for great house, and this Pharaoh is never named. The Hebrew says the woman was taken, without naming who "
   "took her; the Greek has the officials bring her; the Latin has them report her rather than see her."),
  'shared': ["Pharaoh’s officials praised Sarai to Pharaoh.", "She was taken into Pharaoh’s house.", "Abram’s scheme has cost him his wife."],
  'instructions': [ins(K, S, "Sarai was taken into Pharaoh’s house on the officials’ report."), ins(W, R, "The lie that was meant to save Abram’s life delivers his wife to another man; self-protection has its own cost.")],
  'entries': ['sarah', 'egypt'],
  'lost': [
   keeps("Greek kai eisēgagon autēn, “and they brought her,” makes the officials the agents; Hebrew va-tuqqach ha-ishah, “and the woman was taken,” leaves the agent unstated."),
   between("Latin “the princes reported her to Pharaoh … the woman was taken” and King James “the princes also of Pharaoh saw her … the woman was taken” keep the Hebrew passive. 1 Kings 1:2–3 shows the custom."),
  ]},

 '12:16': {
  'received': "Abram was treated well for Sarai’s sake and acquired flocks, cattle, donkeys, servants and camels.",
  'explain': ("Abram prospers by his wife’s loss. The Hebrew has a single benefactor, Pharaoh, and lists flocks, cattle, male donkeys, "
   "slaves male and female, female donkeys and camels; the Greek has plural benefactors and lists sheep, calves, donkeys, slaves and "
   "mules. The word for female slaves is the one that will name Hagar; she may well have joined the household here."),
  'shared': ["Abram was treated well because of Sarai.", "He acquired livestock.", "He acquired male and female servants and camels."],
  'instructions': [ins(K, S, "Abram grew rich in Egypt because of Sarai."), ins(W, R, "Wealth gained at this price is part of the story’s shame, not its reward; Egypt enriches Abram as it later enriches Israel on the way out.")],
  'entries': ['abraham', 'egypt', 'hagar'],
  'lost': [
   loses("Hebrew le-Avram hetiv, “he treated Abram well,” has Pharaoh as the single benefactor; Greek tō Abram eu echrēsanto, “they treated Abram well,” is plural. Hebrew atonot, “female donkeys,” becomes Greek hēmionoi, “mules,” and Hebrew tson u-vaqar, “flocks and cattle,” becomes probata kai moschoi, “sheep and calves.”"),
   between("Latin “they treated Abram well … oxen … female donkeys” sits between; King James “he entreated Abram well … oxen … she asses” follows the Hebrew. Greek paidiskai is the word of 16:1 and Galatians 4:22."),
  ]},

 '12:17': {
  'received': "The Lord struck Pharaoh and his house with great plagues because of Sarai.",
  'explain': ("God intervenes where Abram has failed. The Hebrew says YHWH struck Pharaoh with plagues, using the word Exodus will use for "
   "the last plague on Egypt; the Greek says God afflicted him with great and grievous afflictions, a verb that means to examine closely, "
   "often under pain. The protection promised in verse 3 works even when Abram has not earned it."),
  'shared': ["God struck Pharaoh and his household.", "The blows were great.", "They came because of Sarai, Abram’s wife."],
  'instructions': [ins(K, S, "God protected Sarai by afflicting Pharaoh’s house."), ins(W, R, "God keeps the promise to Abram when Abram does not; the plagues on Pharaoh are grace to a man who has not deserved it.")],
  'entries': ['sarah', 'egypt', 'yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew va-yenagga YHWH … nega‘im gedolim, “YHWH struck … with great plagues,” uses the plague word of Exodus 11:1. Greek ētasen ho theos … etasmois megalois kai ponērois, “God afflicted … with great and grievous afflictions,” changes the name, the verb and adds “grievous.”"),
   between("Latin “the Lord struck … with very great plagues” and King James “the LORD plagued … with great plagues” follow the Hebrew. Genesis 20:18 repeats the pattern."),
  ]},

 '12:18': {
  'received': "Pharaoh summoned Abram and asked what he had done and why he had not said Sarai was his wife.",
  'explain': ("The pagan king puts to the man of promise the question God put to Eve in the garden: what is this you have done? Abimelech "
   "will ask it again. Pharaoh’s complaint is just, and Abram makes no reply. The Hebrew asks two questions; the Greek joins the second to the first."),
  'shared': ["Pharaoh called Abram.", "He asked what Abram had done to him.", "He asked why Abram had not said she was his wife."],
  'instructions': [ins(K, S, "Pharaoh rebuked Abram for concealing that Sarai was his wife."), ins(W, R, "The rebuke comes from outside the covenant; a pagan king sees the wrong the patriarch would not name.")],
  'entries': ['abraham', 'egypt'],
  'lost': [between("Hebrew lammah lo-higgadta li, “why did you not tell me,” is a second question; Greek hoti ouk apēngeilas moi, “that you did not tell me,” makes it depend on the first. Latin and King James keep two questions. Greek ti touto epoiēsas is the question of 3:13 and 20:9.")]},

 '12:19': {
  'received': "Pharaoh asked why Abram had called her his sister, so that he took her as wife, and told him to take her and go.",
  'explain': ("Pharaoh restores Sarai and dismisses Abram. The Hebrew says take her and go; the Greek adds “before you” and uses an urgent "
   "verb, hurry away, the pattern that returns at the exodus when the Egyptians urge Israel to leave quickly. Whether Pharaoh had made "
   "her his wife in fact or only in intention the Hebrew leaves open; King James reads “so I might have taken her.”"),
  'shared': ["Pharaoh asked why Abram said she was his sister.", "Pharaoh had taken her as his wife.", "He returned her and told Abram to go."],
  'instructions': [ins(K, S, "Pharaoh returned Sarai and sent Abram away."), ins(W, R, "Abram leaves Egypt rebuked and enriched, a pattern Israel will repeat; God brings his people out even through their failures.")],
  'entries': ['abraham', 'sarah', 'egypt'],
  'lost': [
   keeps("Greek adds enantion sou, “before you,” and apotreche, “hurry away,” where the Hebrew has qach va-lekh, “take and go.” The Greek urgency anticipates Exodus 12:31–33."),
   between("Latin “take her and go” and King James “take her, and go thy way” follow the Hebrew; King James “so I might have taken her” reads the Hebrew as intention."),
  ]},

 '12:20': {
  'received': "Pharaoh ordered his men to escort Abram away with his wife and all he had.",
  'explain': ("The chapter ends with an escort out of Egypt. The Hebrew says the men sent Abram away with his wife and possessions; the Greek "
   "and Latin say they escorted him; the Greek adds Lot, who was with Abram since Haran and is named again here before the quarrel of the "
   "next chapter. Neither text means Lot first joined Abram in Egypt."),
  'shared': ["Pharaoh gave his men orders concerning Abram.", "They sent him away with his wife.", "All that he had went with him."],
  'instructions': [ins(K, S, "Abram was escorted out of Egypt with his household."), ins(W, R, "The first stay in Egypt ends under escort; the shape of the exodus is drawn in small.")],
  'entries': ['abraham', 'egypt'],
  'lost': [
   keeps("Greek adds kai Lōt met’ autou, “and Lot with him,” to the party, and gives the escorting as the content of the order, sympropempsai; the Hebrew says va-yeshallechu, “they sent away,” without Lot."),
   between("Latin “his men … escorted him away with his wife and everything he had” has the escort without Lot; King James “they sent him away, and his wife, and all that he had” follows the Hebrew."),
  ]},
 }
}
