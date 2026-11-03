# Study prose for Genesis 21 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 21,
 'chapterNote': (
  "Isaac’s birth, the casting out of Hagar and Ishmael, God’s hearing of the boy and the treaty at Beersheba are the same story in every column. "
  "What varies is small and telling. The Hebrew keeps “in his old age” twice, Sarah’s “who would have said,” Ishmael simply “laughing,” “a nation” for "
  "Ishmael in 21:13, Hagar weeping while the boy lies silent, a well of water, two Philistines at the treaty, “deal falsely” and “kindness,” one well, "
  "the name Beersheba, and a tamarisk. The Greek keeps “in old age” for Sarah, “who will announce,” Ishmael playing “with her son Isaac,” “a great nation,” "
  "the child crying and weeping, a well of living water, a third Philistine named Ahuzzath, “wrong” and “righteousness,” wells, the name translated "
  "“Well of Swearing” or “Well of the Oath,” and a field. The Latin and King James follow the Hebrew; the Latin divides 21:32–33 differently."),
 'verses': {

 '21:1': {
  'received': "The Lord visited Sarah and did for her as he had promised.",
  'explain': ("The promise of 17:21 and 18:14 is kept, and the verse says so twice: as he had said, as he had spoken. The Hebrew names YHWH twice; the "
   "Greek the Lord twice; the Latin once, and says promised. “Visited” is the Bible’s word for God coming to act, in judgement or in grace."),
  'shared': ["The Lord visited Sarah.", "He did so as he had said.", "He did for Sarah as he had spoken."],
  'instructions': [ins(K, S, "God kept his promise to Sarah."), ins(W, R, "Twenty-five years after the first word, the fulfilment is told as plainly as the promise; God’s speaking and doing are one.")],
  'entries': ['sarah', 'yhwh-yahweh'],
  'lost': [between("Hebrew paqad, “visited,” is Greek epeskepsato; both versions repeat the name. Latin “as He had promised, and fulfilled what He had spoken” compresses; King James follows the Hebrew.")]},

 '21:2': {
  'received': "Sarah conceived and bore Abraham a son in old age, at the time God had said.",
  'explain': ("The impossible birth is stated as a fact. The Hebrew says in his old age, Abraham’s, and that God had spoken to him; the Greek says in old "
   "age, without saying whose, and that the Lord had spoken; the Latin her old age and foretold to her. The appointed time is the time of 17:21."),
  'shared': ["Sarah conceived.", "She bore Abraham a son in old age.", "It was at the appointed time God had spoken."],
  'instructions': [ins(K, S, "Isaac was born at the time God had set."), ins(W, R, "Paul reads this verse as the resurrection of a body as good as dead; the birth is the first proof that God gives life where there is none.")],
  'entries': ['sarah', 'abraham', 'isaac'],
  'lost': [between("Hebrew li-zqunav, “in his old age,” is Greek eis to gēras, “in old age,” without the possessive; Hebrew Elohim is Greek kyrios. Latin “in her old age … foretold to her” shifts to Sarah; King James “in his old age … God had spoken to him” follows the Hebrew. Romans 4:19 and Hebrews 11:11–12 read the verse.")]},

 '21:3': {
  'received': "Abraham named the son Sarah bore him Isaac.",
  'explain': ("The name commanded in 17:19 is given. Isaac, he laughs, carries Abraham’s laugh of 17:17 and Sarah’s of 18:12 into the child’s name. "
   "The Hebrew and Greek say his son who was born to him, whom Sarah bore him; the Latin shortens. All agree."),
  'shared': ["Abraham named his son.", "Sarah had borne the son to him.", "The name was Isaac."],
  'instructions': [ins(K, S, "Abraham named the promised son Isaac as God had directed."), ins(W, R, "The laughter of doubt is made the name of the child; God lets the parents’ incredulity become their son’s identity.")],
  'entries': ['abraham', 'sarah', 'isaac'],
  'lost': [between("Hebrew and Greek agree, both repeating “born to him … bore him”; Latin “his son whom Sarah bore him” drops one clause; King James follows the Hebrew. Hebrew Yitschaq is Greek Isaak.")]},

 '21:4': {
  'received': "Abraham circumcised Isaac on the eighth day, as God had commanded.",
  'explain': ("The covenant of chapter 17 is kept on its first son born under it. The eighth day is the day of 17:12, on which John and Jesus will also "
   "be circumcised. The Hebrew says his son Isaac; the Greek Isaac; the Latin him. The obedience is as prompt as in 17:23."),
  'shared': ["Abraham circumcised Isaac.", "It was on the eighth day.", "It was as God had commanded him."],
  'instructions': [ins(K, S, "Isaac was circumcised on the eighth day in obedience to the covenant.")],
  'entries': ['abraham', 'isaac', 'term-covenant'],
  'lost': [between("Hebrew ben-shemonat yamim, “a son of eight days,” is Greek tē ogdoē hēmera, “on the eighth day”; the Greek omits “his son.” Latin “circumcised him on the eighth day” and King James “his son Isaac being eight days old” divide. Luke 2:21 is the echo.")]},

 '21:5': {
  'received': "Abraham was a hundred years old when Isaac was born.",
  'explain': ("The age of 17:17 is confirmed: a hundred. The versions agree; the Latin rearranges the sentence around the circumcision. The number "
   "will be set against Isaac’s age at the binding and Abraham’s at his death."),
  'shared': ["Abraham was a hundred years old.", "His son Isaac was born.", "The birth is dated by Abraham’s age."],
  'instructions': [ins(K, S, "Isaac was born when Abraham was a hundred.")],
  'entries': ['abraham', 'isaac'],
  'lost': [between("Hebrew, Greek and King James agree; the Latin says “when he was one hundred years old; for Isaac was born when his father was this age.”")]},

 '21:6': {
  'received': "Sarah said that God had made laughter for her, and all who heard would laugh with her.",
  'explain': ("Sarah’s laugh of 18:12 is redeemed. God has made laughter for her, and everyone who hears will laugh too, with her or at the wonder; the "
   "Hebrew phrase can carry both. The Hebrew says God and laugh; the Greek the Lord and rejoice; the Latin God and laugh with. The verse is a small psalm "
   "on the child’s name."),
  'shared': ["Sarah spoke.", "God has made laughter for her.", "Everyone who hears will laugh with her."],
  'instructions': [ins(K, S, "Sarah rejoiced that God had turned her laughter to joy."), ins(W, R, "The same word that was doubt in the tent door is joy in the nursery; God does not take away the laugh but changes what it means.")],
  'entries': ['sarah', 'isaac', 'god-theos', 'lord-translation'],
  'lost': [between("Hebrew Elohim, “God,” is Greek kyrios, “the Lord”; Hebrew yitschaq-li, “will laugh for/with me,” is Greek synchareitai moi, “will rejoice with me,” making the shared joy explicit. Latin “God … will laugh with me” and King James “God hath made me to laugh … will laugh with me” keep the laughter.")]},

 '21:7': {
  'received': "Sarah marvelled that anyone could have told Abraham she would nurse children, for she had borne a son in old age.",
  'explain': ("Sarah’s second saying is harder, and the columns part. The Hebrew asks who would have said to Abraham that Sarah nurses children, and "
   "ends, I have borne a son in his old age; the Greek asks who will announce to Abraham that Sarah nurses a child, and ends in my old age; the Latin "
   "asks who would have believed it. The wonder is the same; whose old age and how many children differ."),
  'shared': ["Sarah spoke again.", "She marvelled that she, Sarah, should nurse a child.", "She had borne a son in old age."],
  'instructions': [ins(K, S, "Sarah wondered aloud at nursing a child in old age."), ins(W, R, "The wonder is told from the mother’s side: not only a son, but milk; the body as good as dead feeds a child.")],
  'entries': ['sarah', 'abraham'],
  'lost': [
   loses("Hebrew mi millel le-Avraham, “who would have said to Abraham,” a past wonder, becomes Greek tis anangelei tō Abraam, “who will announce to Abraham,” future; Hebrew banim, “children,” plural, becomes Greek paidion, “a child,” singular; Hebrew li-zqunav, “in his old age,” becomes Greek en tō gērei mou, “in my old age.”"),
   between("Latin “who would have believed, on hearing it, that Abraham’s Sarah would nurse a son whom she bore him in his old age” recasts the sentence but keeps Abraham’s age; King James “who would have said unto Abraham, that Sarah should have given children suck? for I have born him a son in his old age” follows the Hebrew."),
  ]},

 '21:8': {
  'received': "Isaac grew and was weaned, and Abraham made a great feast on that day.",
  'explain': ("Weaning, at two or three years, was marked with a feast. The child has lived through infancy, the dangerous years, and the household "
   "celebrates. The Greek adds his son; the Latin says on the day of his weaning. The feast is the setting for the next scene."),
  'shared': ["The child grew.", "He was weaned.", "Abraham made a great feast on the day Isaac was weaned."],
  'instructions': [ins(K, S, "Abraham celebrated Isaac’s weaning with a feast."), ins(W, R, "A feast for a child who has survived infancy; the joy of the house is the occasion of its division.")],
  'entries': ['abraham', 'isaac'],
  'lost': [between("Greek adds ton huion autou, “his son,” before Isaac; Hebrew says “Isaac.” Latin “on the day of his weaning” drops the name; King James follows the Hebrew.")]},

 '21:9': {
  'received': "Sarah saw Hagar’s son playing, and it provoked her.",
  'explain': ("What Sarah saw is the crux. The Hebrew says she saw the son of Hagar the Egyptian, whom she had borne to Abraham, laughing, a participle "
   "from the root of Isaac’s name, with no object; mocking, playing and worse have all been read in it. The Greek and Latin say playing with her son "
   "Isaac, naming the companion and making the scene explicit. Paul will read it as persecution; the Hebrew leaves the act unspecified."),
  'shared': ["Sarah saw Hagar’s son.", "He was the son Hagar had borne to Abraham.", "He was laughing or playing."],
  'instructions': [ins(K, S, "Sarah saw Ishmael at play or in mockery and reacted."), ins(W, R, "A laugh begins the second expulsion as a laugh named the heir; what Ishmael did is left for the reader to weigh, and Sarah weighed it against her son.")],
  'entries': ['sarah', 'hagar', 'isaac'],
  'lost': [
   keeps("Greek adds meta Isaak tou huiou autēs, “with her son Isaac,” giving the laughter a companion and object; Hebrew metsacheq, “laughing” or “playing,” stands alone. The Greek makes the link to the inheritance dispute of 21:10 explicit."),
   between("Latin “playing with her son Isaac” follows the Greek, and moves “and said to Abraham” into this verse; King James “mocking” reads the Hebrew participle as hostile. Galatians 4:29 reads persecution."),
  ]},

 '21:10': {
  'received': "Sarah told Abraham to drive out the slave woman and her son, who must not inherit with Isaac.",
  'explain': ("Sarah does not name Hagar or Ishmael; they are this slave woman and her son. The demand is about inheritance: the slave’s son shall not "
   "share with Isaac. Paul quotes the verse in Galatians for the two covenants. The versions agree; the Hebrew ends “with my son, with Isaac,” "
   "repeating the preposition."),
  'shared': ["Sarah spoke to Abraham.", "She told him to cast out the slave woman and her son.", "The slave woman’s son must not inherit with Isaac."],
  'instructions': [ins(K, S, "Sarah demanded the expulsion of Hagar and Ishmael to secure Isaac’s inheritance."), ins(W, R, "Sarah protects the promise by cruelty; the text records her words and God will endorse the outcome without the tone.")],
  'entries': ['sarah', 'hagar', 'isaac', 'abraham'],
  'lost': [between("Hebrew garesh, “drive out,” is Greek ekbale, “cast out,” the word Galatians 4:30 quotes; Hebrew im-beni im-Yitschaq, “with my son, with Isaac,” is Greek meta tou huiou mou Isaak. Latin and King James agree in sense.")]},

 '21:11': {
  'received': "The demand grieved Abraham greatly because of his son.",
  'explain': ("Abraham’s distress is for Ishmael, his son, the boy he pleaded for in 17:18. The Hebrew says the matter was very evil in his eyes; the "
   "Greek the statement seemed very harsh; the Latin he took it hard. The father’s grief is recorded before God speaks."),
  'shared': ["The matter displeased Abraham.", "It displeased him greatly.", "It was because of his son."],
  'instructions': [ins(K, S, "Abraham was grieved at the thought of sending Ishmael away."), ins(W, R, "The father loves the son the promise passes over; Abraham’s grief is the text’s acknowledgement that Ishmael is wronged.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew va-yera ha-davar me’od be-eine Avraham, “the matter was very evil in Abraham’s eyes,” is Greek sklēron de ephanē to rhēma sphodra enantion Abraam, “the statement seemed very harsh before Abraham.” Latin “took this hard” and King James “very grievous in Abraham’s sight” agree in sense.")]},

 '21:12': {
  'received': "God told Abraham not to grieve but to listen to Sarah, for his offspring would be named through Isaac.",
  'explain': ("God settles the dispute on Sarah’s side, with a reason: the line runs through Isaac. Paul quotes the last clause for the children of "
   "promise. The Hebrew says do not be displeased concerning the boy and your slave woman; the Greek do not regard the statement as harsh concerning "
   "the child and the slave woman. Sarah’s voice is to be obeyed in everything."),
  'shared': ["God spoke to Abraham.", "He is not to grieve over the boy and the slave woman but to listen to Sarah.", "Through Isaac his offspring will be named."],
  'instructions': [ins(C, S, "Listen to Sarah in everything she tells you."), ins(K, S, "The covenant line was fixed through Isaac."), ins(W, R, "God confirms the outcome Sarah demanded and will provide for the boy she rejects; election and compassion are both his.")],
  'entries': ['abraham', 'sarah', 'isaac', 'hagar'],
  'lost': [between("Hebrew al-yera be-einekha, “let it not be evil in your eyes,” is Greek mē sklēron estō to rhēma, “let the statement not be harsh”; Hebrew ha-na‘ar, “the boy,” is Greek tou paidiou, “the child”; Hebrew amatekha, “your slave woman,” is Greek tēs paidiskēs without “your.” Latin and King James follow the Hebrew. Romans 9:7 and Hebrews 11:18 quote the last clause.")]},

 '21:13': {
  'received': "God promised to make the slave woman’s son a nation too, because he was Abraham’s offspring.",
  'explain': ("Ishmael is not abandoned. God will make him a nation, because he is Abraham’s seed. The Hebrew says a nation; the Greek and Latin a great "
   "nation, which the Hebrew says in verse 18 and said in 17:20. The promise to Hagar in chapter 16 is renewed to Abraham."),
  'shared': ["God will make the slave woman’s son a nation.", "The reason is that he is Abraham’s offspring.", "Ishmael has a future from God."],
  'instructions': [ins(K, S, "God promised Ishmael a nation for Abraham’s sake."), ins(W, R, "The boy cast out of the house is kept in God’s promise; being Abraham’s seed is enough to be remembered.")],
  'entries': ['hagar', 'abraham'],
  'lost': [
   keeps("Greek adds mega, “great,” to the nation, eis ethnos mega, matching 17:20 and 21:18; the Hebrew here says le-goy, “a nation.”"),
   between("Latin “a great nation” follows the Greek; King James “a nation” the Hebrew."),
  ]},

 '21:14': {
  'received': "Early next morning Abraham gave Hagar bread and water, sent her away with the child, and she wandered in the wilderness of Beersheba.",
  'explain': ("Abraham obeys with provisions that will not last: bread and a skin of water. The sentence that places them on her shoulder together with "
   "the child is compressed in both languages; the Greek more readily puts the child on the shoulder, the Hebrew lets him be entrusted to her, and "
   "Ishmael, at least fourteen, is not an infant in either. The Hebrew names the wilderness of Beersheba; the Greek translates it, the Well of the Oath."),
  'shared': ["Abraham rose early and gave Hagar bread and a skin of water.", "He sent her away with the child.", "She wandered in the wilderness of Beersheba."],
  'instructions': [ins(K, S, "Abraham sent Hagar and Ishmael into the wilderness with scant provisions."), ins(W, R, "Obedience here costs Abraham his son and costs Hagar nearly everything; the text does not soften what the promise required.")],
  'entries': ['abraham', 'hagar'],
  'lost': [
   loses("Hebrew Be’er Shava, “Beersheba,” a name, becomes Greek to phrear tou horkou, “the Well of the Oath,” a translation, here and throughout the chapter; Hebrew lechem, “bread,” is Greek artous, “loaves”; Hebrew va-yashkem, “rose early,” is Greek anestē to prōi, “rose in the morning.”"),
   between("Latin “placed them upon her shoulder, entrusted the boy to her” reads the Hebrew so that the child is entrusted, not carried; King James “putting it on her shoulder, and the child” keeps the compression. Both keep Beersheba."),
  ]},

 '21:15': {
  'received': "When the water was gone, Hagar put the child under a bush.",
  'explain': ("The skin runs dry and Hagar gives up. She casts or lays the boy under what shade there is. The Hebrew says one of the shrubs; the Greek a "
   "fir tree, naming a species; the Latin one of the trees there. The verb is strong, cast, in the Hebrew and Greek; the Latin softens to laid."),
  'shared': ["The water in the skin ran out.", "Hagar put the child down.", "She put him under a bush or tree."],
  'instructions': [ins(K, S, "Hagar abandoned hope when the water failed."), ins(W, R, "When provision ends, the mother lays the child down to die; the story goes as far as despair before God speaks.")],
  'entries': ['hagar'],
  'lost': [between("Hebrew tachat achad ha-sichim, “under one of the shrubs,” is Greek hypokatō mias elatēs, “beneath a fir tree,” a specific tree; Hebrew va-tashlekh, “she cast,” is Greek erripsen, the same, but Latin posuit, “she laid.” King James “cast the child under one of the shrubs” follows the Hebrew.")]},

 '21:16': {
  'received': "Hagar sat a bowshot away, unwilling to watch the child die, and there was weeping.",
  'explain': ("Hagar sits at a distance so as not to see the death, and the weeping begins. Who weeps divides the columns: the Hebrew, Latin and King James "
   "have Hagar raise her voice and weep; the Greek has the child cry out and weep, aligning with the next verse where God hears the boy. The Hebrew "
   "does not exclude the child’s crying, and the Greek does not exclude the mother’s."),
  'shared': ["Hagar sat opposite the child about a bowshot away.", "She said she would not watch the child die.", "There was loud weeping."],
  'instructions': [ins(K, S, "Hagar sat apart from the dying child and there was weeping."), ins(W, R, "The mother who cannot watch and the child who cannot be saved; the scene is written so that God’s hearing in the next verse answers both.")],
  'entries': ['hagar'],
  'lost': [
   loses("Hebrew va-tissa et-qolah va-tevk, “she raised her voice and wept,” with Hagar as subject, becomes Greek anaboēsan de to paidion eklausen, “the child cried out and wept”; the weeper changes. Hebrew al-er’eh, “let me not see,” is Greek ou mē idō, “I will not see.”"),
   between("Latin “sitting opposite him, she raised her voice and wept” and King James “lift up her voice, and wept” keep Hagar as the weeper with the Hebrew."),
  ]},

 '21:17': {
  'received': "God heard the boy’s voice, and his angel called from heaven telling Hagar not to fear, for God had heard the boy where he was.",
  'explain': ("Ishmael’s name, God hears, is fulfilled: God hears the boy. The angel of God calls from heaven, not from beside her as in chapter 16, and "
   "asks what is wrong, then repeats the hearing. The Greek adds “from the place where he was” to the first clause and “your” to the child; the Hebrew "
   "says the boy. The comfort is the same."),
  'shared': ["God heard the boy’s voice.", "The angel of God called to Hagar from heaven and told her not to fear.", "God has heard the boy’s voice where he is."],
  'instructions': [ins(K, S, "God heard Ishmael and sent his angel to Hagar."), ins(W, R, "God hears the boy before anyone prays for him; the name given before his birth is honoured in the wilderness.")],
  'entries': ['hagar', 'angel-of-the-lord', 'god-theos'],
  'lost': [
   keeps("Greek adds ek tou topou hou ēn, “from the place where he was,” to the first hearing and sou, “your,” to the second mention of the child; the Hebrew has “the boy’s voice” and “the boy’s voice where he is.”"),
   between("Latin and King James follow the Hebrew; Hebrew mal’akh Elohim and Greek angelos theou are both “angel of God.”"),
  ]},

 '21:18': {
  'received': "Hagar was told to lift the boy and hold him by the hand, for God would make him a great nation.",
  'explain': ("The command and the promise: get up, take him, hold him; I will make him a great nation. The promise of 17:20 and 21:13 is spoken to the "
   "mother. The Hebrew says lift up the boy and hold him firmly; the Greek take the child and hold him; the sense is the same."),
  'shared': ["Hagar is to get up and lift the boy.", "She is to hold him by the hand.", "God will make him a great nation."],
  'instructions': [ins(C, S, "Get up, lift the boy and hold him by your hand."), ins(K, S, "God promised to make Ishmael a great nation."), ins(W, R, "The mother who laid the child down is told to pick him up; despair is answered by a task and a promise.")],
  'entries': ['hagar'],
  'lost': [between("Hebrew se’i et-ha-na‘ar ve-hachaziqi et-yadekh bo, “lift up the boy and make your hand strong on him,” is Greek labe to paidion kai kratēson tē cheiri sou auto, “take the child and hold him with your hand.” Latin “lift the boy, and hold his hand” and King James “lift up the lad, and hold him in thine hand” agree in sense.")]},

 '21:19': {
  'received': "God opened Hagar’s eyes to a well, and she filled the skin and gave the boy a drink.",
  'explain': ("The well was there; what was lacking was sight. God opens her eyes and she sees water, fills the skin and gives the boy to drink. The "
   "Greek calls it a well of living water, fresh or flowing, a phrase that will carry much later meaning; the Hebrew and Latin a well of water. The "
   "practical result comes first in every column."),
  'shared': ["God opened Hagar’s eyes.", "She saw a well of water.", "She filled the skin and gave the boy a drink."],
  'instructions': [ins(K, S, "God showed Hagar a well and the boy was saved."), ins(W, R, "The water was near all along; God’s help is sometimes the opening of eyes to what is already given.")],
  'entries': ['hagar', 'god-theos'],
  'lost': [
   keeps("Greek adds zōntos, “living,” to the water, phrear hydatos zōntos, “a well of living water,” the phrase of 26:19 and Jeremiah 2:13; the Hebrew says be’er mayim, “a well of water.”"),
   between("Latin “a well of water” and King James “a well of water” follow the Hebrew. John 4:10–11 gives the phrase its later sense."),
  ]},

 '21:20': {
  'received': "God was with the boy as he grew up in the wilderness and became an archer.",
  'explain': ("Ishmael’s story is closed with a blessing: God was with him. He grows, lives in the wilderness and becomes an archer, a hunter and warrior "
   "of the desert, the wild man of 16:12. The Latin says a young archer. The versions agree."),
  'shared': ["God was with the boy.", "He grew and lived in the wilderness.", "He became an archer."],
  'instructions': [ins(K, S, "Ishmael grew up in the wilderness with God’s presence."), ins(W, R, "“God was with the boy” is said of the son outside the covenant; God’s presence is wider than the line of promise.")],
  'entries': [],
  'lost': [between("Hebrew roveh qashshat, “a shooter, a bowman,” is Greek toxotēs, “an archer”; Latin “a young archer” adds the age. King James follows the Hebrew.")]},

 '21:21': {
  'received': "Ishmael lived in the wilderness of Paran, and his mother found him a wife from Egypt.",
  'explain': ("The wilderness of Paran lies south toward Sinai. Hagar, the Egyptian, takes a wife for her son from her own people; the mother who was "
   "given to Abraham now arranges a marriage, acting as head of the family. The versions agree."),
  'shared': ["He lived in the wilderness of Paran.", "His mother took a wife for him.", "She was from the land of Egypt."],
  'instructions': [ins(K, S, "Ishmael settled in Paran and married an Egyptian."), ins(W, R, "The cast-out slave arranges her son’s marriage as a matriarch; Hagar ends the chapter with the authority Sarah denied her.")],
  'entries': ['hagar', 'egypt'],
  'lost': [between("Hebrew, Greek, Latin and King James agree. Hebrew Paran is Greek Pharan; Deuteronomy 33:2 and Numbers 13:3 name the wilderness.")]},

 '21:22': {
  'received': "Abimelech and Phicol his commander told Abraham that God was with him in all he did.",
  'explain': ("The Philistine king returns, with his general, to make a treaty. Their opening word is a confession: God is with you in everything you "
   "do. The Hebrew names two, Abimelech and Phicol; the Greek adds a third, Ahuzzath his groomsman or friend, who appears in the Hebrew only in 26:26 "
   "with Isaac. The Latin and King James have two."),
  'shared': ["Abimelech and Phicol, commander of his army, spoke to Abraham.", "They said God was with him.", "God was with him in everything he did."],
  'instructions': [ins(K, S, "The Philistine king acknowledged that God was with Abraham."), ins(W, R, "The outsider sees God’s presence in Abraham’s life; the treaty begins from a pagan’s testimony.")],
  'entries': ['abraham'],
  'lost': [
   keeps("Greek adds kai Ochozath ho nymphagōgos autou, “and Ahuzzath his groomsman,” to the delegation, here and in 21:32, matching the Hebrew of 26:26; the Hebrew here names Abimelech and Phicol only."),
   between("Latin and King James name two with the Hebrew. Hebrew sar-tseva’o, “commander of his army,” is Greek ho archistratēgos tēs dynameōs autou, “chief commander of his force.”"),
  ]},

 '21:23': {
  'received': "Abimelech asked Abraham to swear not to deal falsely with him or his descendants but to repay his kindness.",
  'explain': ("The terms: an oath by God not to deal falsely with Abimelech, his offspring or his descendants, and to treat him and his land with the "
   "kindness he showed. The Hebrew says deal falsely and kindness, chesed; the Greek wrong and righteousness, and names Abraham’s name rather than "
   "descendants; the same substitution as in 19:19 and 20:13. The sojourner is asked to bind himself to his host."),
  'shared': ["Abimelech asks Abraham to swear by God.", "Abraham is not to deal falsely with Abimelech or his line.", "He is to show the land the kindness Abimelech showed him."],
  'instructions': [ins(K, S, "Abimelech sought a sworn treaty of good faith with Abraham."), ins(W, R, "The host asks the guest for kindness in return; Abraham, enriched by Gerar twice, is bound to be a good neighbour.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew im-tishqor li, “that you will not deal falsely with me,” becomes Greek mē adikēsein me, “not to wrong me”; Hebrew u-le-nini u-le-nekhdi, “my offspring and my descendants,” becomes mēde to sperma mou mēde to onoma mou, “my offspring or my name”; Hebrew ka-chesed, “according to the kindness,” becomes kata tēn dikaiosynēn, “according to the righteousness.” Hebrew hennah, “here,” is dropped."),
   between("Latin “not harm me, my posterity, or my offspring … the same kindness” and King James “not deal falsely with me, nor with my son, nor with my son’s son … the kindness” keep the descendants and the kindness."),
  ]},

 '21:24': {
  'received': "Abraham agreed to swear.",
  'explain': ("Three words. Abraham accepts the terms without bargaining, as he did not with God over Sodom. All versions agree exactly."),
  'shared': ["Abraham answered.", "He agreed.", "He said, I will swear."],
  'instructions': [ins(K, S, "Abraham consented to the oath.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew, Greek, Latin and King James agree word for word.")]},

 '21:25': {
  'received': "Abraham complained to Abimelech about a well his servants had seized.",
  'explain': ("Before swearing, Abraham raises a grievance: Abimelech’s men have taken a well. Water rights are the substance of desert treaties. The Hebrew "
   "says one well, seized; the Greek wells, taken away; the Latin a well seized by force. The reproof is the sojourner’s only leverage."),
  'shared': ["Abraham reproved Abimelech.", "The matter was a well of water.", "Abimelech’s servants had seized it."],
  'instructions': [ins(K, S, "Abraham complained of a seized well before swearing."), ins(W, R, "A treaty of kindness begins by naming the wrong; Abraham’s reproof is the honest ground of the oath that follows.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew be’er ha-mayim, “the well of water,” singular, is Greek tōn phreatōn tou hydatos, “the wells of water,” plural; Hebrew gazelu, “seized,” is Greek apheilanto, “took away.” Latin “a well … seized by force” and King James “a well … violently taken away” follow the Hebrew.")]},

 '21:26': {
  'received': "Abimelech denied all knowledge: Abraham had not told him, and he had only now heard.",
  'explain': ("The king’s reply is a threefold denial: I do not know who did it, you did not tell me, I never heard until today. It is a plea of "
   "innocence like his plea in chapter 20. The versions agree."),
  'shared': ["Abimelech did not know who had done it.", "Abraham had not told him.", "He had heard nothing until today."],
  'instructions': [ins(K, S, "Abimelech disclaimed knowledge of the seized well.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James agree in the three clauses; the Greek adds “to him.” King James “I wot not” is old English for “I know not.”")]},

 '21:27': {
  'received': "Abraham gave Abimelech sheep and cattle, and the two made a covenant.",
  'explain': ("Abraham gives the gifts this time, and the two cut a covenant, the Hebrew idiom. The Hebrew says flocks and cattle; the Greek sheep and "
   "calves; the Latin and King James sheep and oxen. Nothing is said of slaughtering these animals for the rite."),
  'shared': ["Abraham took livestock.", "He gave them to Abimelech.", "The two of them made a covenant."],
  'instructions': [ins(K, S, "Abraham and Abimelech made a covenant sealed with gifts."), ins(W, R, "The first treaty between Abraham and a king is made on equal terms; the sojourner gives, and the two swear as peers.")],
  'entries': ['abraham', 'term-covenant'],
  'lost': [between("Hebrew tson u-vaqar, “flocks and cattle,” is Greek probata kai moschous, “sheep and calves”; Hebrew va-yikhretu berit, “they cut a covenant,” is Greek diethento diathēkēn. Latin and King James “sheep and oxen” follow the Hebrew categories.")]},

 '21:28': {
  'received': "Abraham set seven ewe lambs apart.",
  'explain': ("A detail that puzzles Abimelech: seven female lambs set by themselves. The number seven and the oath about to be sworn are both in the "
   "name of the place. The versions agree."),
  'shared': ["Abraham took seven ewe lambs.", "They were of the flock.", "He set them apart."],
  'instructions': [ins(K, S, "Abraham separated seven ewe lambs for a purpose.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew sheva kivsot, “seven ewe lambs,” is Greek hepta amnadas; Hebrew levaddehen, “by themselves,” is Greek monas. Latin and King James agree.")]},

 '21:29': {
  'received': "Abimelech asked what the seven ewe lambs meant.",
  'explain': ("The king asks the question the reader asks. The versions agree; the Latin says to him for to Abraham. The answer gives the lambs a legal "
   "function."),
  'shared': ["Abimelech spoke to Abraham.", "He asked about the seven ewe lambs.", "He asked why they were set apart."],
  'instructions': [ins(K, S, "Abimelech asked the meaning of the seven lambs.")],
  'entries': [],
  'lost': [between("Hebrew mah hennah, “what are these,” is Greek ti eisin; Latin “to him” drops Abraham’s name; King James follows the Hebrew.")]},

 '21:30': {
  'received': "Abraham said the lambs were to be a witness that he had dug the well.",
  'explain': ("The lambs are evidence. Abimelech’s acceptance of them will testify that the well is Abraham’s by his own digging. The Hebrew says it may be "
   "a witness for me, a singular; the Greek that they may be a testimony, the lambs themselves, and names Abraham. The dispute of verse 25 is settled "
   "by a gift that records a right."),
  'shared': ["Abimelech will take the seven ewe lambs from Abraham.", "They will be a witness for Abraham.", "The witness is that Abraham dug the well."],
  'instructions': [ins(K, S, "The seven lambs witnessed Abraham’s right to the well."), ins(W, R, "A right is secured by giving, not grasping; Abraham buys his well with lambs and leaves the king no cause.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew tihyeh-li le-edah, “that it may be a witness for me,” singular, is Greek esontai moi eis martyrion, “that they may be a testimony for me,” plural; the Greek adds Abraham’s name. Latin “as testimony” and King James “that they may be a witness” divide.")]},

 '21:31': {
  'received': "So the place was named Beersheba, because the two swore there.",
  'explain': ("The name is explained by the oath, sheva, which in Hebrew also sounds like seven, the lambs just given; the Hebrew hears both. The Greek "
   "translates the name, Well of Swearing, hearing the oath only; the Latin and King James keep Beersheba. The Hebrew and Greek have Abraham name "
   "it; the Latin says it was called."),
  'shared': ["The place was given a name.", "The name is explained by the oath.", "The two of them swore there."],
  'instructions': [ins(K, S, "Beersheba was named for the oath sworn there."), ins(W, R, "A well and an oath give the place its name; Beersheba will be the southern limit of the land, “from Dan to Beersheba.”")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew Be’er Shava, “Beersheba,” holds both shava, “oath,” and sheva, “seven”; Greek Phrear horkismou, “Well of Swearing,” translates the oath and loses the seven."),
   between("Latin “that place was called Beersheba” keeps the name but makes the naming passive; King James “he called that place Beersheba” follows the Hebrew."),
  ]},

 '21:32': {
  'received': "They made the covenant at Beersheba, and Abimelech and Phicol returned to Philistine country.",
  'explain': ("The covenant is concluded and the Philistines go home. The Hebrew says at Beersheba; the Greek at the Well of the Oath, and again includes "
   "Ahuzzath. The Latin ends the verse at the covenant and carries the departure into verse 33. This is the first mention of Philistines as a people "
   "with a land."),
  'shared': ["They made a covenant at Beersheba.", "Abimelech and Phicol rose.", "They returned to the land of the Philistines."],
  'instructions': [ins(K, S, "The treaty was concluded and the Philistines departed.")],
  'entries': ['term-covenant'],
  'lost': [
   keeps("Greek again adds Ochozath ho nymphagōgos autou, “Ahuzzath his groomsman,” and translates Beersheba as to phrear tou horkou, “the Well of the Oath.”"),
   between("Latin “they made a covenant concerning the Well of the Oath” translates the name and ends there; King James follows the Hebrew with two Philistines and the name."),
  ]},

 '21:33': {
  'received': "Abraham planted a tree at Beersheba and called there on the name of the Lord, the everlasting God.",
  'explain': ("Abraham marks the place with worship, as at Shechem and Bethel, and gives God a new title, El Olam, the everlasting God. The Hebrew says he "
   "planted a tamarisk, a desert tree; the Greek a field, reading the rare word as cultivated ground, and names Abraham; the Latin and King James a "
   "grove. The Latin also carries the Philistines’ departure into this verse."),
  'shared': ["Abraham planted something at Beersheba.", "He called there on the name of the Lord.", "He called God the everlasting God."],
  'instructions': [ins(K, S, "Abraham worshipped the everlasting God at Beersheba."), ins(W, R, "A tree planted and a name given: Abraham puts down roots in the land of the oath and names the God who outlasts every treaty.")],
  'entries': ['el-olam', 'abraham', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew eshel, “a tamarisk,” becomes Greek arouran, “a field”; Hebrew be-Ve’er Shava is Greek epi tō phreati tou horkou, “at the Well of the Oath”; Hebrew YHWH El Olam, “YHWH, the everlasting God,” is Greek kyrios theos aiōnios. The Greek adds Abraham’s name."),
   between("Latin “planted a grove in Beersheba … the Lord, the everlasting God,” with the Philistines’ return prefixed, and King James “planted a grove in Beersheba” read eshel as a grove. The title El Olam appears only here."),
  ]},

 '21:34': {
  'received': "Abraham sojourned in Philistine country for a long time.",
  'explain': ("The chapter ends with Abraham still a sojourner, now in the land of the Philistines, for many days. The promise of the land has advanced "
   "by one well and one treaty. The versions agree; the Latin says settler."),
  'shared': ["Abraham sojourned.", "He was in the land of the Philistines.", "He stayed many days."],
  'instructions': [ins(K, S, "Abraham remained a sojourner among the Philistines for a long time."), ins(W, R, "The heir of all the land owns a well; Hebrews says he lived in tents because he looked for a city God would build.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew va-yagor, “he sojourned,” is Greek parōkēsen; Latin “lived as a settler”; King James “sojourned.” Hebrews 11:9 reads the sojourning.")]},
 }
}
