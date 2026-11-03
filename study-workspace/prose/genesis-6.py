# Study prose for Genesis 6 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 6,
 'chapterNote': (
  "The corruption of the earth, God’s decision, Noah’s favour and the building of the ark are told alike. What varies is how "
  "God’s inner response is described and how the Hebrew’s rarer words are handled. The Hebrew keeps YHWH’s regret and grief of "
  "heart, the disputed verb of 6:3, the Nephilim as a distinct name, violence filling the earth, gopher wood, the tsohar of the ark, "
  "and Noah walking with God. The Greek keeps God considering and reflecting in 6:6 and growing angry in 6:7, “My Spirit shall "
  "not remain in these human beings,” giants for Nephilim and mighty men alike, injustice for violence, squared timber, a "
  "construction instruction in place of the window, a fuller inventory of creatures to be “nourished,” and Noah pleasing God. "
  "The Latin and King James follow the Hebrew in nearly every one of these; the Latin alone has a window in 6:16."),
 'verses': {

 '6:1': {
  'received': "As people multiplied on the earth, daughters were born to them.",
  'explain': ("The chapter opens with growth. Humankind spreads, and the mention of daughters prepares for what the sons of God "
   "will do. The Hebrew speaks of humankind collectively on the face of the ground; the Greek of human beings in the plural on the "
   "earth. The sense is the same."),
  'shared': ["Human beings began to multiply on the earth.", "Daughters were born to them.", "The scene is set for the next verse."],
  'instructions': [ins(K, S, "Humankind multiplied on the earth after the first generations.")],
  'entries': [],
  'lost': [between("Hebrew ha-adam, “humankind,” collective, is Greek hoi anthrōpoi, plural; Hebrew “face of the ground” is Greek “the earth.” Latin and King James say the same.")]},

 '6:2': {
  'received': "The sons of God saw that the daughters of men were beautiful and took wives from among them as they chose.",
  'explain': ("A famous and disputed verse, but the dispute is not between the texts. Hebrew and Greek both read “sons of God.” "
   "Who they are, angels, rulers or the line of Seth, is a question of interpretation that the printed texts do not decide. "
   "What the verse states is desire, choice and marriage across a boundary."),
  'shared': ["The sons of God saw the daughters of men.", "They found them beautiful.", "They took wives from among all they chose."],
  'instructions': [ins(K, S, "The sons of God took wives from the daughters of men."), ins(W, R, "Choosing by beauty alone, from all one wishes, is the shape of the disorder the chapter goes on to describe.")],
  'entries': ['sons-of-god'],
  'lost': [
   keeps("Hebrew bene ha-Elohim and Greek hoi huioi tou theou agree: sons of God. Some Greek witnesses read “angels of God,” but the main text printed here does not; the Greek keeps the Hebrew phrase."),
   between("Latin filii Dei and King James “sons of God” agree. Jewish writings and many early Christians read angels (Jude 6; 2 Peter 2:4); Augustine and Chrysostom read Seth’s descendants; others read rulers."),
  ]},

 '6:3': {
  'received': "The Lord declared that his spirit would not stay with humankind forever, for they are flesh, and set their days at a hundred and twenty years.",
  'explain': ("God responds with a limit. The Hebrew verb is rare and disputed, contend, judge or remain; the Greek reads “remain,” "
   "my Spirit shall not remain in these human beings. The Hebrew speaks of humankind in the singular, the Greek in the plural. "
   "Both end with a hundred and twenty years, whether as the span of a life or the time left before the flood."),
  'shared': ["God’s spirit will not stay with humankind forever.", "The reason is that humankind is flesh.", "Their days are set at a hundred and twenty years."],
  'instructions': [ins(K, S, "God limited the days of humankind because they are flesh."), ins(W, R, "Breath is lent, not owned; the limit is a judgement and a mercy at once.")],
  'entries': ['spirit-god-lord', 'lord-translation'],
  'lost': [
   loses("Hebrew lo-yadon ruchi va-adam, with the rare yadon, is uncertain: “shall not contend,” “shall not judge,” or “shall not remain.” Greek ou mē katameinē to pneuma mou en tois anthrōpois toutois chooses “remain” and makes the humans plural and demonstrative, “these.” Hebrew YHWH becomes “the Lord God.”"),
   between("Latin “shall not remain in the human being” follows the Greek verb with the Hebrew singular; King James “shall not always strive with man” follows the other reading of the Hebrew. All give a hundred and twenty years."),
  ]},

 '6:4': {
  'received': "In those days, and afterward, the giants were on the earth, born when the sons of God went in to the daughters of men; they were the renowned men of old.",
  'explain': ("The offspring are described. The Hebrew uses two terms, Nephilim for the beings on the earth and “mighty men” for "
   "the renowned heroes of old; the Greek uses “giants” for both, so the distinction is lost. The Hebrew Nephilim is often linked "
   "to a verb for falling, and the spies in Numbers use the same word for the people of Canaan. None of the texts gives a full account of what these beings were."),
  'shared': ["Giants were on the earth in those days.", "The sons of God went in to the daughters of men and children were born.", "These were the renowned men of old."],
  'instructions': [ins(K, S, "The giants of old were born in the days when the sons of God took human wives."), ins(W, R, "Fame and might are not the same as goodness; the men of renown belong to the generation of the flood.")],
  'entries': ['nephilim', 'sons-of-god', 'giant-peoples-overview'],
  'lost': [
   loses("Hebrew ha-nefilim, “the Nephilim,” and ha-gibborim, “the mighty men,” are two words; Greek gigantes, “giants,” stands for both, and the Hebrew distinction between the beings and the heroes is gone. Hebrew “they bore children to them” becomes Greek “begat children for themselves.”"),
   between("Latin gigantes for the first and “mighty men of old” for the second keeps the two apart, as does King James “giants … mighty men.” Numbers 13:33 and Wisdom of Solomon 14:6 take up the words."),
  ]},

 '6:5': {
  'received': "The Lord saw that human wickedness was great on the earth and that every inclination of the heart was bent on evil continually.",
  'explain': ("God looks and sees. The verdict is total: not some evil, but every inclination, all the time. The Hebrew says every "
   "inclination of the thoughts of the heart was only evil; the Greek says each person intently considered evil things in his heart "
   "all the days. The Hebrew YHWH is the Greek Lord God. The Greek sentence runs on into the next verse."),
  'shared': ["The Lord saw human wickedness.", "It was great upon the earth.", "The thoughts of the heart were set on evil continually."],
  'instructions': [ins(K, S, "God judged the human heart to be set on evil before the flood."), ins(W, R, "The flood answers a disorder of the heart, not only of deeds; the inner life is where God looks first.")],
  'entries': ['yhwh-yahweh', 'lord-translation'],
  'lost': [
   loses("Hebrew kol-yetser machshevot libbo raq ra, “every inclination of the thoughts of his heart only evil,” names the yetser, the formed inclination. Greek pas tis dianoeitai en tē kardia autou epimelōs epi ta ponēra, “everyone intently considers evil things in his heart,” describes the act of considering. Hebrew “was great” becomes Greek “had multiplied.”"),
   between("Latin “every thought of the heart was intent upon evil” leans toward the Greek; King James “every imagination of the thoughts of his heart was only evil continually” follows the Hebrew."),
  ]},

 '6:6': {
  'received': "God was sorry he had made humankind on the earth, and it pained him.",
  'explain': ("The versions differ most sharply here. The Hebrew says YHWH regretted making humankind and was grieved to his "
   "heart; the Latin and King James follow it. The Greek says God considered that he had made humankind and reflected on it, "
   "avoiding the language of regret and grief. Neither text should be made to settle later questions about whether God changes."),
  'shared': ["God looked back on his making of humankind.", "He responded with sorrow or deliberation.", "The response leads to the decision of the next verse."],
  'instructions': [ins(K, S, "God responded with grief, or deliberation, to the wickedness of humankind."), ins(W, R, "Scripture is willing to speak of God’s grief in human words; the Greek is more reserved, and both ways of speaking have their place.")],
  'entries': ['yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew va-yinnachem YHWH, “YHWH regretted,” and va-yit‘atsev el-libbo, “he was grieved to his heart,” give regret and heartfelt grief. Greek enethymēthē ho theos, “God considered,” and dienoēthē, “reflected,” give deliberation. The Hebrew’s grief is gone from the Greek verse."),
   keeps("The Greek treats the human language about God differently in two neighbouring verses, reflection here and anger in 6:7, which suggests interpretive handling rather than a different text."),
   between("Latin “He regretted … touched with grief deep within His heart” and King James “it repented the LORD … it grieved him at his heart” keep the Hebrew."),
  ]},

 '6:7': {
  'received': "The Lord resolved to wipe humankind and the animals from the earth, because he was sorry, or angry, that he had made them.",
  'explain': ("The decision is spoken. Everything that breathes on the land, from humans to birds, will be wiped away. The reason "
   "closes the verse: in the Hebrew, Latin and King James, God regrets having made them; in the Greek, he has become angry that "
   "he made them. The Hebrew says “created,” the Greek “made.” Both go straight on to Noah, so neither excludes mercy."),
  'shared': ["God will wipe humankind from the face of the earth.", "Livestock, creeping things and birds will go with them.", "God’s reason is his response to having made them."],
  'instructions': [ins(K, S, "God resolved to destroy the living things of the earth with humankind."), ins(W, R, "The creatures share the judgement on the people who ruled them; human sin is never private.")],
  'entries': ['yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew ki nichamti ki asitim, “for I regret that I made them,” becomes Greek hoti ethymōthēn hoti epoiēsa autous, “for I have become angry that I made them.” Regret becomes anger. Hebrew bara, “created,” is Greek “made,” and YHWH is “God.”"),
   between("Latin “for I regret having made them” and King James “for it repenteth me that I have made them” follow the Hebrew; Latin and King James keep “created.”"),
  ]},

 '6:8': {
  'received': "But Noah found favour with the Lord.",
  'explain': ("One word turns the chapter: but. Against the whole earth stands one man who finds favour. The Hebrew says in the "
   "eyes of YHWH; the Greek before the Lord God. The Greek word can also be rendered grace, as the King James does; the choice "
   "does not create a difference between the sources."),
  'shared': ["Noah is set apart from the corruption.", "He found favour.", "The favour was with the Lord."],
  'instructions': [ins(K, S, "Noah found favour with God in a corrupt generation."), ins(W, R, "Favour comes before the ark; Noah is chosen before he builds.")],
  'entries': ['noah', 'yhwh-yahweh', 'lord-translation'],
  'lost': [
   between("Hebrew matsa chen be-eine YHWH, “found favour in the eyes of YHWH,” is Greek heuren charin enantion kyriou tou theou, “found favour before the Lord God.” Greek charis is also “grace,” as King James has it; Latin gratiam coram Domino. Only the divine title is longer in Greek."),
  ]},

 '6:9': {
  'received': "Noah was a righteous man, blameless in his generation, who walked with God.",
  'explain': ("A new heading, and the first person in Scripture to be called righteous. Noah is righteous, blameless or complete, "
   "and in close fellowship with God. As with Enoch in 5:22–24, the Hebrew says he walked with God and the Greek says he pleased "
   "God. The evaluation is the same in both. Hebrews says Noah became heir of the righteousness that is by faith."),
  'shared': ["These are the generations of Noah.", "Noah was righteous and blameless in his generation.", "He lived in fellowship with God."],
  'instructions': [ins(K, S, "Noah was righteous and walked with God."), ins(W, R, "Righteousness is possible in a corrupt age; Noah’s generation is named so that his integrity stands out against it.")],
  'entries': ['noah'],
  'lost': [
   loses("Hebrew et-ha-Elohim hithallekh Noach, “Noah walked with God,” becomes Greek tō theō euērestēsen Noe, “Noah pleased God,” as at 5:22 and 5:24. Hebrew tamim, “blameless,” is Greek teleios, “complete”; Hebrew “generations” is plural, Greek singular."),
   keeps("Greek dikaios, “righteous,” is the word Hebrews 11:7 and 2 Peter 2:5 use of Noah. Greek geneseis, “generations,” is the heading word that divides Genesis (2:4; 10:1; 11:27)."),
   between("Latin “righteous and blameless … he walked with God” and King James “just … perfect … walked with God” keep the Hebrew image."),
  ]},

 '6:10': {
  'received': "Noah had three sons: Shem, Ham and Japheth.",
  'explain': ("The three sons of 5:32 are named again as the household the flood will spare. All versions agree exactly, the "
   "Greek this time matching the Hebrew’s “three sons.” Ham will be the father of Canaan and of Egypt, which the Psalms call the land of Ham."),
  'shared': ["Noah begat three sons.", "They were Shem, Ham and Japheth.", "The household of the ark is named."],
  'instructions': [ins(K, S, "Noah’s three sons were Shem, Ham and Japheth.")],
  'entries': ['noah'],
  'lost': [between("Hebrew, Greek, Latin and King James agree on the count and the names. Greek Cham is Hebrew Cham, father of Canaan (9:18) and Mizraim (10:6).")]},

 '6:11': {
  'received': "The earth was corrupt before God and filled with violence.",
  'explain': ("The narrator restates the state of things. Corruption before God, and the earth filled: in the Hebrew with "
   "violence, wrongful harm; in the Greek with injustice, the broader word. The Greek verb for corruption means to spoil or rot, "
   "the word Paul uses when he speaks of creation freed from its bondage to corruption."),
  'shared': ["The earth was corrupt.", "The corruption was before God.", "The earth was filled with wrongdoing."],
  'instructions': [ins(K, S, "The earth before the flood was corrupt and full of violence."), ins(W, R, "Violence is how corruption of heart becomes visible; a world full of it is a world ready for judgement.")],
  'entries': [],
  'lost': [
   loses("Hebrew chamas, “violence,” is specific; Greek adikia, “injustice,” is general. The Hebrew’s picture of bloodshed and harm becomes a moral category in Greek."),
   keeps("Greek ephtharē, “was corrupted,” from phtheirō, to spoil or rot, is the word of Romans 8:21."),
   between("Latin iniquitate, “wickedness,” sits nearer the Greek; King James “violence” follows the Hebrew."),
  ]},

 '6:12': {
  'received': "God saw that the earth was corrupt, for all flesh had corrupted its way upon it.",
  'explain': ("God sees what the narrator has said. The corruption is universal, “all flesh,” and it is a matter of conduct, "
   "its “way.” The Greek adds Lord to God and uses a stronger verb, ruined. Joel will promise the reverse: God’s Spirit poured out on all flesh."),
  'shared': ["God saw the earth.", "It was corrupt.", "All flesh had corrupted its way upon the earth."],
  'instructions': [ins(K, S, "God saw that all flesh had corrupted its way."), ins(W, R, "A “way” can be corrupted; conduct is a path, and the whole earth had left it.")],
  'entries': ['god-theos', 'lord-translation'],
  'lost': [
   loses("Hebrew Elohim, “God,” becomes Greek kyrios ho theos, “the Lord God.” Hebrew nishchatah, “was corrupt,” and hishchit, “had corrupted,” become Greek katephtharmenē and katephtheiren, intensified forms, “ruined.” Hebrew hinneh, “behold,” is dropped."),
   between("Latin and King James keep “God” and “corrupt”; the Latin sentence runs on into 6:13. Greek pasa sarx, “all flesh,” is the phrase of Joel 3:1 (2:28) and Acts 2:17."),
  ]},

 '6:13': {
  'received': "God told Noah that the end of all flesh had come, for the earth was full of violence, and he would destroy them with the earth.",
  'explain': ("God speaks to Noah for the first time, and the first word is judgement. The Hebrew says the end of all flesh has come "
   "before me; the Greek the time of every human. The Hebrew earth is full of violence, the Greek of injustice. The Hebrew destroys "
   "them with the earth; the Greek destroys them and the earth. Amos and Ezekiel take up the Hebrew words for later judgements."),
  'shared': ["God spoke to Noah.", "An end has come before God because the earth is filled with wrongdoing.", "God will destroy them and the earth."],
  'instructions': [ins(K, S, "God announced the coming destruction to Noah before it came."), ins(W, R, "Judgement is announced to the righteous before it falls; Noah is told so that he can act.")],
  'entries': ['noah'],
  'lost': [
   loses("Hebrew qets kol-basar, “the end of all flesh,” becomes Greek kairos pantos anthrōpou, “the time of every human”; the end becomes an appointed time and all flesh becomes humanity. Hebrew chamas is again adikia. Hebrew et-ha-arets, “with the earth,” becomes Greek kai tēn gēn, “and the earth.”"),
   between("Latin “the end of all flesh … destroy them with the earth” and King James “the end of all flesh … destroy them with the earth” keep the Hebrew. Amos 8:2 and Ezekiel 7:2–3 echo “the end has come.”"),
  ]},

 '6:14': {
  'received': "God commanded Noah to build an ark of timber, with compartments, coated inside and out with pitch.",
  'explain': ("The command to build. The Hebrew names gopher wood, a term never identified; the Greek says squared, worked timber; "
   "the Latin smooth timbers. Compartments in the Hebrew are nests in the Greek. The Hebrew word for the ark is used elsewhere only "
   "of the basket that carried Moses; the Greek uses the word later used for the ark of the covenant. The Hebrew word for pitch shares its root with atonement."),
  'shared': ["Noah is to make an ark.", "It is to have compartments.", "It is to be coated inside and out with pitch."],
  'instructions': [ins(C, S, "Make an ark of timber with rooms, and coat it inside and outside with pitch."), ins(W, R, "Salvation here takes the form of a building project; faith does what it is told with timber and pitch.")],
  'entries': ['noahs-ark', 'noah'],
  'lost': [
   loses("Hebrew atse-gofer, “gopher wood,” is an unidentified material; Greek xylōn tetragōnōn, “squared timber,” describes prepared wood instead. Hebrew qinnim, “compartments,” is Greek nossias, “nests.” The Greek adds oun, “therefore.”"),
   keeps("Greek kibōtos, “ark,” is the word for the ark of the covenant (Exodus 25:10) and of 1 Peter 3:20, so the Greek ties the two arks together; Hebrew tevah is used only here and of Moses’ basket (Exodus 2:3)."),
   between("Latin “smooth timbers” and “bitumen” and King James “gopher wood” and “pitch” divide; Hebrew kofer, “pitch,” shares its root with kippur, atonement (Leviticus 17:11)."),
  ]},

 '6:15': {
  'received': "The ark was to be three hundred cubits long, fifty wide and thirty high.",
  'explain': ("The dimensions are given and agree in every version: 300 by 50 by 30 cubits. The Greek repeats “the ark” where the "
   "Hebrew says “it.” No exact modern length of the cubit is assumed. The proportions are those of a vessel built to float, not to sail."),
  'shared': ["This is how the ark is to be made.", "It is three hundred cubits long and fifty wide.", "It is thirty cubits high."],
  'instructions': [ins(C, S, "Make the ark three hundred cubits long, fifty wide and thirty high.")],
  'entries': ['noahs-ark'],
  'lost': [between("Hebrew, Greek, Latin and King James give the same three numbers; the Greek names the ark twice where the Hebrew has “it.”")]},

 '6:16': {
  'received': "The ark was to be finished at the top, with a door in its side and three decks.",
  'explain': ("The hardest verse of the instructions. The Hebrew begins with a rare word, tsohar, read as an opening, a window or "
   "a roof; the Latin and King James say window. The Greek has no window at all but a construction instruction, “make the ark by "
   "bringing it together,” often understood as narrowing it upward. All agree on finishing to a cubit at the top, the door in the side and the three levels. No modern roof plan can be drawn from any of them."),
  'shared': ["The ark is finished to a cubit at the top.", "Its door is set in its side.", "It has lower, second and third levels."],
  'instructions': [ins(C, S, "Set the door in the ark’s side and make it with three levels."), ins(W, R, "One door and three decks: the ark is remembered for how it was entered, not for how it looked.")],
  'entries': ['noahs-ark'],
  'lost': [
   loses("Hebrew tsohar ta‘aseh la-tevah, “make a tsohar for the ark,” names something, an opening, window or roof, that the Greek does not have. Greek episynagōn poiēseis tēn kibōton, “make the ark by bringing it together,” is a construction action instead of a thing."),
   keeps("Greek thyra, “door,” is the word of John 10:9, “I am the door,” which Augustine set beside the ark’s single door."),
   between("Latin fenestram, “window,” and King James “window” choose one reading of the Hebrew word; Rashi records both window and precious stone. The door and the three stories agree everywhere."),
  ]},

 '6:17': {
  'received': "God would bring the flood on the earth to destroy all flesh that breathes, and everything on the earth would perish.",
  'explain': ("The flood is named for the first time. God himself brings it, water upon the earth, and its scope is everything "
   "under heaven that has the breath or spirit of life. The versions agree on the extent. The Greek word for flood is the one "
   "Jesus uses for the days of Noah as a warning for his coming."),
  'shared': ["God is bringing the flood on the earth.", "It will destroy all flesh that has the breath of life.", "Everything on the earth will perish."],
  'instructions': [ins(K, S, "God announced a flood that would destroy all life on the land."), ins(W, R, "The flood is God’s act, not a natural accident; the one who made the waters sends them.")],
  'entries': [],
  'lost': [
   keeps("Greek kataklysmos, “flood,” is the word of Matthew 24:38–39, Luke 17:27 and 2 Peter 2:5. Hebrew mabbul is used only of this flood."),
   between("Hebrew “flood of water” and Greek “the flood, water upon the earth” differ in construction only; Hebrew ruach chayyim and Greek pneuma zōēs are “spirit of life,” Latin and King James “breath of life.” Hebrew yigva, “perish,” is Greek teleutēsei, “die.”"),
  ]},

 '6:18': {
  'received': "God promised to establish his covenant with Noah, who would enter the ark with his wife, his sons and their wives.",
  'explain': ("The first covenant in Scripture is promised here and made after the flood in chapter 9. Alongside the promise comes "
   "the command: Noah and his household, eight people, are to enter the ark. All versions agree. The Greek word for covenant is the "
   "one that later names the new covenant."),
  'shared': ["God will establish his covenant with Noah.", "Noah will enter the ark.", "His sons, his wife and his sons’ wives will go with him."],
  'instructions': [ins(K, S, "God’s first covenant was promised to Noah before the flood."), ins(C, S, "Enter the ark with your household.")],
  'entries': ['term-covenant', 'noah', 'noahs-ark'],
  'lost': [
   keeps("Greek diathēkē, “covenant,” renders Hebrew berit and is the word of Luke 22:20 and Hebrews 8:8, so the Greek reader hears the first covenant in the vocabulary of the last."),
   between("Hebrew, Greek, Latin and King James name the same household in the same order."),
  ]},

 '6:19': {
  'received': "Noah was to bring two of every living kind into the ark, male and female, to keep them alive.",
  'explain': ("The animals come in pairs. The Hebrew says two of every living thing, of all flesh, to keep them alive; the Greek "
   "gives a fuller list, livestock, creeping things, wild animals and all flesh, two by two, and says they are to be nourished "
   "with Noah. Male and female pairs are in all four."),
  'shared': ["Two of every kind are to come into the ark.", "They are to be kept alive with Noah.", "They are to be male and female."],
  'instructions': [ins(C, S, "Bring two of every living kind, male and female, into the ark to keep them alive."), ins(W, R, "The creatures are preserved in pairs so that life can begin again; the ark is a seed as well as a shelter.")],
  'entries': ['noahs-ark'],
  'lost': [
   keeps("An added an inventory the Hebrew does not have here, “all the livestock, all the creeping things, all the wild animals,” and says dyo dyo, “two by two,” and trephein, “to nourish,” where the Hebrew has lehachayot, “to keep alive.”"),
   between("Latin “every living creature of all flesh … to live with you” and King James “every living thing of all flesh … to keep them alive” keep the Hebrew’s shorter form."),
  ]},

 '6:20': {
  'received': "Two of every kind of bird, livestock and creeping thing were to come to Noah to be kept alive.",
  'explain': ("The list is spelled out by kind: birds, livestock, creeping things, each according to its kind, the phrase of "
   "chapter 1. The creatures themselves come to Noah. The Greek adds “with you” and repeats “male and female,” and again says "
   "“nourished” where the Hebrew says “kept alive.”"),
  'shared': ["Birds, livestock and creeping things come according to their kinds.", "Two of each come to Noah.", "They are to be kept alive."],
  'instructions': [ins(K, S, "Two of every kind of creature came to Noah to be preserved."), ins(W, R, "The animals come to Noah; the gathering is God’s work as much as the man’s.")],
  'entries': ['noahs-ark'],
  'lost': [
   keeps("An added meta sou, “with you,” and arsen kai thēly, “male and female,” which the Hebrew does not repeat in this verse; “to be nourished” again stands for “to be kept alive.”"),
   between("Latin “so that they may live” and King James “to keep them alive” follow the Hebrew; the creatures are the subject of “come” in all four."),
  ]},

 '6:21': {
  'received': "Noah was to gather every kind of food as provision for himself and the animals.",
  'explain': ("The last instruction is practical: food for a long voyage, for the people and the animals alike. The Hebrew uses an "
   "impersonal passive, food that is eaten; the Greek addresses a plural you, the foods that you eat, inside instructions "
   "otherwise addressed to Noah alone."),
  'shared': ["Noah is to take food of every kind.", "He is to gather it to himself.", "It is for him and for the animals."],
  'instructions': [ins(C, S, "Gather every kind of food for yourself and for the animals."), ins(W, R, "Faith provisions the ship; trusting God does not excuse Noah from counting the stores.")],
  'entries': [],
  'lost': [between("Hebrew mi-kol-ma’akhal asher ye’akhel, “of every food that is eaten,” is Greek apo pantōn tōn brōmatōn ha edesthe, “of all the foods that you (plural) eat.” Latin and King James keep the impersonal form.")]},

 '6:22': {
  'received': "Noah did everything God commanded him.",
  'explain': ("The chapter ends with obedience stated twice over: Noah did according to all that God commanded; so he did. The "
   "Greek has the Lord God where the Hebrew has God. The same words close Moses’ work on the tabernacle, and Hebrews counts "
   "Noah’s building among the acts of faith."),
  'shared': ["Noah did what God commanded.", "He did all of it.", "The obedience is complete."],
  'instructions': [ins(K, S, "Noah obeyed God’s command in full."), ins(W, R, "Faith is seen in the finished ark; obedience is the shape faith takes in a workshop.")],
  'entries': ['noah'],
  'lost': [
   loses("Hebrew Elohim, “God,” is Greek kyrios ho theos, “the Lord God.”"),
   keeps("Greek houtōs epoiēsen, “so he did,” is the phrase that closes Exodus 40:16; Hebrews 11:7 reads Noah’s building as faith."),
   between("Latin “Noah did everything God had commanded him” drops the repeated “so he did”; King James keeps it."),
  ]},
 }
}
