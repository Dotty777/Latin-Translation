# Study prose for Genesis 30 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 30,
 'chapterNote': (
  "The contest of the sisters, eight more children, Joseph’s birth, and Jacob’s wage of speckled sheep. The columns agree on the children and their names; "
  "they diverge in the small explanatory clauses and, in the breeding account, in the colour words. The Hebrew keeps “I may be built up through her,” “with "
  "mighty wrestlings I have wrestled,” “may YHWH add” in Joseph’s naming, Laban who “learned by divination,” “speckled, spotted, dark,” poplar, almond and "
  "plane rods, “the stronger animals,” and the division by weak and strong. The Greek keeps Jacob and the maids named in the birth notices, “God has helped me” "
  "for Naphtali, “Issachar, which means Reward,” “God” for YHWH in 30:24, Laban who “would divine by signs,” “gray, white-marked, spotted,” styrax, walnut and "
  "plane, a “white-marked ram,” and a division by marked and unmarked. The Latin and King James follow the Hebrew; the Latin reads the final division as early "
  "and late season. One Hebrew-column rendering was corrected today."),
 'verses': {

 '30:1': {
  'received': "Rachel, childless, envied her sister and told Jacob to give her children or she would die.",
  'explain': ("Rachel’s barrenness after Leah’s four sons becomes envy, and envy becomes a demand Jacob cannot meet. Give me children, or I die: the Hebrew is as abrupt as the English. The versions agree."),
  'shared': ["Rachel saw that she bore Jacob no children.", "She envied her sister.", "Give me children, or else I die."],
  'instructions': [ins(K, S, "Rachel demanded children of Jacob in her envy."), ins(W, R, "The loved wife envies the unloved for her sons; each sister has what the other wants, and neither has peace.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '30:2': {
  'received': "Jacob angrily asked if he were in God’s place, who had withheld the fruit of the womb.",
  'explain': ("Jacob’s one recorded anger at Rachel, and a true word in it: the womb is God’s to open. The versions agree."),
  'shared': ["Jacob’s anger was kindled against Rachel.", "Am I in the place of God?", "He has withheld from you the fruit of the womb."],
  'instructions': [ins(K, S, "Jacob disclaimed power over Rachel’s barrenness."), ins(W, R, "Isaac prayed for barren Rebekah; Jacob is angry with barren Rachel. The son does not do what the father did, and the narrator lets the contrast stand.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '30:3': {
  'received': "Rachel offered her maid Bilhah, that she might bear on Rachel’s knees and build her up.",
  'explain': ("Sarah’s expedient with Hagar. To bear on my knees is adoption; the Hebrew says I may be built up through her, the pun on son and build from 16:2; the Greek and Latin I may have children."),
  'shared': ["Here is my maid Bilhah.", "Go in to her, that she may bear on my knees.", "I too may have children through her."],
  'instructions': [ins(K, S, "Rachel gave Bilhah to Jacob as a surrogate."), ins(W, R, "Rachel repeats Sarah’s plan and will reap Sarah’s rivalry; the surrogate’s sons are counted hers, but the envy is not cured by counting.")],
  'entries': ['sarah', 'hagar'],
  'lost': [between("Hebrew ve-ibbaneh gam-anokhi mimmennah, “that I too may be built up from her,” the ben/banah wordplay, is Greek kai teknopoiēsomai kagō ex autēs, “and I too will have children from her”; Latin “have children,” King James “have children by her.”")]},

 '30:4': {
  'received': "She gave him Bilhah as wife, and Jacob went in to her.",
  'explain': ("Bilhah becomes a wife of secondary rank. The Latin breaks the verse and carries the going in to verse 5. The versions agree."),
  'shared': ["She gave him her maid Bilhah.", "She was to be his wife.", "Jacob went in to her."],
  'instructions': [ins(K, S, "Bilhah became Jacob’s wife.")],
  'entries': ['jacob'],
  'lost': [between("Latin “she gave him Bilhah in marriage, and she” runs into 30:5; Hebrew, Greek and King James complete the verse here.")]},

 '30:5': {
  'received': "Bilhah conceived and bore Jacob a son.",
  'explain': ("The first of the maids’ four sons. The Greek says Bilhah, Rachel’s slave woman; the Hebrew Bilhah; the Latin she."),
  'shared': ["Bilhah conceived.", "She bore a son.", "He was Jacob’s."],
  'instructions': [ins(K, S, "Bilhah bore Jacob a son.")],
  'entries': ['jacob'],
  'lost': [keeps("An added hē paidiskē Rhachēl, “Rachel’s slave woman,” after Bilhah in the Greek."), between("Hebrew, Latin and King James without it.")]},

 '30:6': {
  'received': "Rachel said God had vindicated her and heard her, and named him Dan.",
  'explain': ("Dan, from din, to judge: God has judged in my favour. The Hebrew and Greek say God; the Latin the Lord; the King James God hath judged me."),
  'shared': ["God has judged me and heard my voice.", "He has given me a son.", "She named him Dan."],
  'instructions': [ins(K, S, "Rachel named Dan for God’s judgment in her favour."), ins(W, R, "Rachel reads a surrogate’s son as a verdict in her case against Leah; the children are counted as points in a quarrel, and the names keep score.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew dananni Elohim, “God has judged me,” is Greek ekrinen moi ho theos, “God has judged for me”; Latin “the Lord has judged in my favour,” King James “God hath judged me.”")]},

 '30:7': {
  'received': "Bilhah bore Jacob a second son.",
  'explain': ("The versions agree; the Latin another son."),
  'shared': ["Bilhah, Rachel’s maid, conceived again.", "She bore a second son.", "He was Jacob’s."],
  'instructions': [ins(K, S, "Bilhah bore a second son.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '30:8': {
  'received': "Rachel said she had wrestled mightily with her sister and prevailed, and named him Naphtali.",
  'explain': ("Naphtali, from a root of wrestling. The Hebrew says with wrestlings of God I have wrestled with my sister, God used as an intensive; the Greek God has helped me, I have contended with my sister; the Latin God has matched me with my sister; the King James great wrestlings."),
  'shared': ["Rachel spoke of her struggle with her sister.", "She has prevailed.", "She named him Naphtali."],
  'instructions': [ins(K, S, "Rachel named Naphtali for her struggle with Leah."), ins(W, R, "Rachel wrestles her sister as Jacob will wrestle God; the household is a ring, and the names of the tribes are the bouts.")],
  'entries': [],
  'lost': [loses("Hebrew naftule Elohim niftalti im-achoti, “wrestlings of God I have wrestled with my sister,” an intensive idiom, becomes Greek synelabeto moi ho theos kai synanestraphēn tē adelphē mou, “God has helped me and I have contended with my sister”; the wrestling becomes help."), between("Latin “God has matched me with my sister” and King James “great wrestlings have I wrestled” render the idiom differently.")]},

 '30:9': {
  'received': "Leah, having stopped bearing, gave her maid Zilpah to Jacob as wife.",
  'explain': ("Leah answers surrogate with surrogate. The versions agree."),
  'shared': ["Leah saw that she had ceased bearing.", "She took her maid Zilpah.", "She gave her to Jacob as wife."],
  'instructions': [ins(K, S, "Leah gave Zilpah to Jacob."), ins(W, R, "Leah, who stopped asking to be loved when Judah was born, is drawn back into the contest; rivalry is harder to leave than to enter.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '30:10': {
  'received': "Zilpah bore Jacob a son.",
  'explain': ("The Greek adds Jacob went in to her and she conceived; the Hebrew says only Zilpah bore; the Latin when she conceived and bore."),
  'shared': ["Zilpah, Leah’s maid.", "She bore a son.", "He was Jacob’s."],
  'instructions': [ins(K, S, "Zilpah bore Jacob a son.")],
  'entries': ['jacob'],
  'lost': [keeps("An added eisēlthen de pros autēn Iakōb, kai synelaben, “Jacob went in to her, and she conceived,” in the Greek."), between("Hebrew and King James “Zilpah Leah’s maid bare Jacob a son”; Latin “when she conceived and bore a son.”")]},

 '30:11': {
  'received': "Leah said, Good fortune, and named him Gad.",
  'explain': ("Gad, fortune. The Hebrew written form ba-gad can be read as a troop comes, the King James rendering, or as fortune has come, with the Greek and Latin. The versions divide on the pun, not the name."),
  'shared': ["Leah spoke at the birth.", "Good fortune!", "She named him Gad."],
  'instructions': [ins(K, S, "Leah named Gad for good fortune.")],
  'entries': [],
  'lost': [between("Hebrew ba-gad, read ba gad, “fortune has come,” or be-gad, “with a troop,” is Greek en tychē, “in fortune,” Latin feliciter, “good fortune,” King James “a troop cometh.”")]},

 '30:12': {
  'received': "Zilpah bore Jacob a second son.",
  'explain': ("The Greek adds conceived again. The versions agree."),
  'shared': ["Zilpah, Leah’s maid.", "She bore a second son.", "He was Jacob’s."],
  'instructions': [ins(K, S, "Zilpah bore a second son.")],
  'entries': ['jacob'],
  'lost': [keeps("An added kai synelaben eti, “and conceived again,” in the Greek."), between("Hebrew, Latin and King James without it.")]},

 '30:13': {
  'received': "Leah said, Happy am I, for women will call me happy, and named him Asher.",
  'explain': ("Asher, happy. The Hebrew says happy am I, women will call me happy; the Greek blessed am I, women will call me blessed; the Latin this is for my happiness. Mary’s all generations will call me blessed echoes it."),
  'shared': ["Leah spoke.", "Happy am I, for women will call me happy.", "She named him Asher."],
  'instructions': [ins(K, S, "Leah named Asher for her happiness."), ins(W, R, "Leah counts herself happy by other women’s reckoning; the unloved wife has become, by her sons, the envied one.")],
  'entries': [],
  'lost': [between("Hebrew be-oshri ki ishsheruni banot, “in my happiness, for daughters call me happy,” is Greek makaria egō, hoti makarizousin me hai gynaikes, “blessed am I, for the women call me blessed”; Latin “this is for my happiness,” King James “Happy am I, for the daughters will call me blessed.”")]},

 '30:14': {
  'received': "Reuben found mandrakes at wheat harvest and brought them to Leah; Rachel asked for some.",
  'explain': ("Mandrakes, duda’im, love-apples, thought to aid conception. Reuben is perhaps five. The Greek says mandrake apples; the Latin omits to Leah in Rachel’s request."),
  'shared': ["Reuben went out at wheat harvest and found mandrakes in the field.", "He brought them to his mother Leah.", "Rachel said to Leah, Give me some of your son’s mandrakes."],
  'instructions': [ins(K, S, "Rachel asked Leah for Reuben’s mandrakes."), ins(W, R, "Rachel, who has Jacob’s love, asks Leah for a fertility charm; Leah, who has sons, wants a night with Jacob. The trade reveals what each lacks.")],
  'entries': [],
  'lost': [between("Greek mēla mandragorōn, “apples of mandrakes,” for Hebrew duda’im, “mandrakes”; Latin and King James “mandrakes.”")]},

 '30:15': {
  'received': "Leah protested that Rachel had taken her husband and now wanted the mandrakes; Rachel offered Jacob for the night in exchange.",
  'explain': ("The bargain. The Hebrew begins Rachel’s reply therefore; the Greek not so, let him; the Latin let him sleep with you. Jacob is traded like the stew that bought a birthright."),
  'shared': ["Is it a small matter that you have taken my husband? Would you take my son’s mandrakes too?", "Rachel answered.", "He shall lie with you tonight in exchange for your son’s mandrakes."],
  'instructions': [ins(K, S, "Rachel traded a night with Jacob for the mandrakes."), ins(W, R, "“You have taken my husband”: Leah speaks as if Rachel were the intruder, though Rachel was the one promised. Each sister is the other’s usurper.")],
  'entries': ['jacob'],
  'lost': [keeps("An added ouch houtōs, “not so,” opening Rachel’s reply in the Greek, where the Hebrew has lakhen, “therefore.”"), between("Latin “Let him sleep with you tonight” drops the connective; King James “Therefore he shall lie with thee.”")]},

 '30:16': {
  'received': "Leah met Jacob at evening and told him she had hired him with the mandrakes; he lay with her that night.",
  'explain': ("Hired, sakhar, the root of Issachar. The Greek adds today; the versions otherwise agree."),
  'shared': ["Jacob came from the field in the evening and Leah went out to meet him.", "You must come in to me, for I have hired you with my son’s mandrakes.", "He lay with her that night."],
  'instructions': [ins(K, S, "Leah claimed her hired night with Jacob."), ins(W, R, "Jacob is hired like a labourer by the wife he did not choose; the man who worked fourteen years for Rachel is bought for a night with weeds.")],
  'entries': ['jacob'],
  'lost': [keeps("An added sēmeron, “today,” in the Greek after come in to me."), between("Hebrew, Latin and King James without it.")]},

 '30:17': {
  'received': "God heard Leah and she bore Jacob a fifth son.",
  'explain': ("God heard Leah: the narrator credits God, not the mandrakes, which Rachel has and which do not help her. The Latin says her prayers."),
  'shared': ["God heard Leah.", "She conceived.", "She bore Jacob a fifth son."],
  'instructions': [ins(K, S, "Leah conceived a fifth son by God’s hearing."), ins(W, R, "The mandrakes go to Rachel and the child to Leah; the narrator quietly discredits the charm.")],
  'entries': ['jacob', 'elohim'],
  'lost': [between("Latin “God heard her prayers” adds the object; Hebrew, Greek and King James “God heard Leah.”")]},

 '30:18': {
  'received': "Leah said God had given her wages for giving her maid to her husband, and named him Issachar.",
  'explain': ("Issachar, there is wages, or man of wages. The Greek adds which means Reward; the Hebrew and Latin give the name alone."),
  'shared': ["God has given me my wages.", "Because I gave my maid to my husband.", "She named him Issachar."],
  'instructions': [ins(K, S, "Leah named Issachar for her reward."), ins(W, R, "Leah calls the child her wages for lending Zilpah, as if God were settling an account; the theology is a tired wife’s, and the narrator does not correct her.")],
  'entries': ['elohim'],
  'lost': [keeps("An added ho estin Misthos, “which is Reward,” after Issachar in the Greek."), between("Hebrew, Latin and King James give the name without the gloss.")]},

 '30:19': {
  'received': "Leah bore Jacob a sixth son.",
  'explain': ("The versions agree."),
  'shared': ["Leah conceived again.", "She bore a sixth son.", "He was Jacob’s."],
  'instructions': [ins(K, S, "Leah bore a sixth son.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '30:20': {
  'received': "Leah said God had endowed her with a good gift and now her husband would honour her, and named him Zebulun.",
  'explain': ("Zebulun, from zavad, endow, and zaval, a rare verb, honour or dwell with. The Hebrew says honour me, provisionally; the Greek choose me; the Latin be with me; the King James dwell with me."),
  'shared': ["God has endowed me with a good gift.", "Now my husband will honour me, for I have borne him six sons.", "She named him Zebulun."],
  'instructions': [ins(K, S, "Leah named Zebulun hoping for her husband’s regard."), ins(W, R, "Six sons, and Leah still hopes her husband will dwell with her; the hope of Reuben’s name is unchanged five births later.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew yizbeleni ishi, “my husband will honour” or “dwell with me,” a rare verb, is Greek hairetiei me ho anēr mou, “my husband will choose me”; Latin “will be with me,” King James “will my husband dwell with me.”")]},

 '30:21': {
  'received': "Afterward she bore a daughter, Dinah.",
  'explain': ("Dinah, judgment, the feminine of Dan; her story is chapter 34. No explanation is given for her name. The versions agree."),
  'shared': ["Afterward.", "She bore a daughter.", "She named her Dinah."],
  'instructions': [ins(K, S, "Leah bore Dinah.")],
  'entries': [],
  'lost': [AGREE]},

 '30:22': {
  'received': "God remembered Rachel, heard her and opened her womb.",
  'explain': ("Remembered, as God remembered Noah and will remember Israel: acted on His purpose. The versions agree; the Latin the Lord."),
  'shared': ["God remembered Rachel.", "God heard her.", "He opened her womb."],
  'instructions': [ins(K, S, "God opened Rachel’s womb at last."), ins(W, R, "After maids and mandrakes and bargains, the sentence is simply “God remembered Rachel”; what the contest could not do, remembrance does.")],
  'entries': ['elohim'],
  'lost': [AGREE]},

 '30:23': {
  'received': "She bore a son and said God had taken away her reproach.",
  'explain': ("Reproach, cherpah, the shame of barrenness, which Elizabeth will echo. The Greek adds to Jacob."),
  'shared': ["She conceived and bore a son.", "She said.", "God has taken away my reproach."],
  'instructions': [ins(K, S, "Rachel bore a son and her reproach was removed.")],
  'entries': ['elohim'],
  'lost': [keeps("An added tō Iakōb, “to Jacob,” after bore a son in the Greek."), between("Hebrew, Latin and King James without it.")]},

 '30:24': {
  'received': "She named him Joseph, saying, May the Lord add to me another son.",
  'explain': ("Joseph, from yasaf, add, with a play on asaf, take away, in the previous verse. The Hebrew says YHWH; the Greek God; the Latin the Lord. The prayer is answered in Benjamin, at the cost of her life."),
  'shared': ["She named him Joseph.", "She said.", "May the Lord add to me another son."],
  'instructions': [ins(K, S, "Rachel named Joseph and prayed for another son."), ins(W, R, "Rachel’s first son is named for the second she wants; even in joy she is asking for more, and the asking will be granted at Bethlehem.")],
  'entries': ['yhwh-yahweh'],
  'lost': [loses("Hebrew yosef YHWH li, “may YHWH add to me,” becomes Greek prosthetō ho theos moi, “may God add to me.”"), between("Latin “may the Lord add” and King James “The LORD shall add” keep the name.")]},

 '30:25': {
  'received': "After Joseph’s birth Jacob asked Laban to send him home to his own country.",
  'explain': ("Fourteen years are up with Joseph’s birth; Jacob asks leave. The versions agree; the Latin his father-in-law."),
  'shared': ["Rachel had borne Joseph.", "Jacob said to Laban, Send me away.", "Let me go to my own place and country."],
  'instructions': [ins(K, S, "Jacob asked to return home after fourteen years."), ins(W, R, "With Rachel’s son born, Jacob thinks of home; the promise of return at Bethel stirs when the beloved wife has a child.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '30:26': {
  'received': "Give me my wives and children for whom I served you, and let me go; you know my service.",
  'explain': ("Wives and children as wages earned. The versions agree."),
  'shared': ["Give me my wives and my children, for whom I have served you.", "Let me depart.", "You know the service I have rendered you."],
  'instructions': [ins(K, S, "Jacob claimed his family as earned wages.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '30:27': {
  'received': "Laban asked for favour, saying he had learned by divination that the Lord blessed him for Jacob’s sake.",
  'explain': ("Laban wants to keep his lucky herdsman. The Hebrew says I have learned by divination, nichashti, that YHWH blessed me because of you; the Greek I would divine by signs, for God blessed me at your arrival, a difficult sentence; the Latin learned by experience; the King James adds tarry."),
  'shared': ["If I have found favour in your sight.", "I have learned that the Lord has blessed me.", "It is because of you."],
  'instructions': [ins(K, S, "Laban admitted God blessed him through Jacob."), ins(W, R, "Laban learns by omens what Abimelech learned by looking: the Lord is with this man. The pagan’s divination arrives at the truth by the wrong road.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew nichashti, “I have divined,” is Greek oiōnisaimēn an, “I would divine by signs,” and Hebrew YHWH is Greek ho theos; Latin “learned by experience” softens the divination; King James “learned by experience … tarry.”")]},

 '30:28': {
  'received': "Name your wages and I will pay them.",
  'explain': ("The offer of 29:15 again, from the man who turned the last one into fourteen years. The versions agree."),
  'shared': ["Laban said.", "Name your wages.", "I will pay them."],
  'instructions': [ins(K, S, "Laban invited Jacob to set new wages.")],
  'entries': [],
  'lost': [AGREE]},

 '30:29': {
  'received': "Jacob said Laban knew how he had served and how the livestock had fared under him.",
  'explain': ("Jacob’s record. The Hebrew says your cattle with me; the Latin how great your possessions have become in my hands."),
  'shared': ["You know how I have served you.", "You know how your livestock have fared with me.", "Jacob states his case."],
  'instructions': [ins(K, S, "Jacob reminded Laban of his faithful service.")],
  'entries': ['jacob'],
  'lost': [between("Latin “how great your possessions have become in my hands” expands Hebrew et asher-hayah miqnekha itti, “how your cattle was with me”; Greek and King James follow the Hebrew.")]},

 '30:30': {
  'received': "You had little before I came and it has grown to much; the Lord blessed you by my coming. When shall I provide for my own house?",
  'explain': ("Jacob attributes the increase to the Lord’s blessing at his feet, le-ragli; the question when is a demand. The Latin turns the question into a statement, it is right."),
  'shared': ["You had little before I came, and it has increased to abundance.", "The Lord blessed you at my coming.", "Now when shall I also provide for my own house?"],
  'instructions': [ins(K, S, "Jacob asked when he might provide for his own household."), ins(W, R, "Twenty years of blessing have gone to Laban’s account; Jacob asks when the blessing he carries will be his to keep.")],
  'entries': ['jacob', 'yhwh-yahweh'],
  'lost': [between("Latin “It is right, then, that at last I should provide for my own household also” makes the Hebrew question u-mattai e‘eseh gam-anokhi le-veti, “and when shall I also do for my house?” a statement; Greek and King James keep the question.")]},

 '30:31': {
  'received': "Laban asked what to give; Jacob said nothing, if Laban would do one thing, and he would keep the flock again.",
  'explain': ("Jacob wants no gift from Laban, as Abraham wanted none from Ephron; he wants a deal. The versions agree."),
  'shared': ["What shall I give you?", "You shall give me nothing.", "If you will do this thing for me, I will again tend and guard your flock."],
  'instructions': [ins(K, S, "Jacob refused a gift and proposed terms.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '30:32': {
  'received': "Let me go through your flock today and remove every speckled, spotted and dark sheep and every spotted goat; those shall be my wages.",
  'explain': ("The marked animals, a minority in flocks of white sheep and dark goats. The Hebrew says I will pass through, speckled, spotted, dark; the Greek let all your sheep pass, gray lambs, white-marked and spotted goats; the Latin variegated, speckled, dark. The colour vocabulary is uncertain in both languages."),
  'shared': ["Pass through all your flock today.", "Separate the speckled and spotted, the dark among the sheep and the spotted among the goats.", "These shall be my wages."],
  'instructions': [ins(K, S, "Jacob proposed the marked animals as his wages."), ins(W, R, "Jacob asks for the odd and off-coloured; the wage looks modest to Laban and is a trap, because Jacob knows sheep better than his uncle does.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew naqod ve-talu … chum, “speckled and spotted … dark,” becomes Greek phaion … dialeukon kai rhanton, “gray … white-marked and spotted,” with Hebrew e‘evor, “I will pass through,” as Greek parelthatō panta ta probata sou, “let all your sheep pass.”"), between("Latin “variegated … speckled … dark, spotted, or variegated” and King James “speckled and spotted … brown … spotted and speckled” follow the Hebrew’s terms.")]},

 '30:33': {
  'received': "My honesty will answer for me when you inspect my wages: any unmarked animal with me shall count as stolen.",
  'explain': ("Jacob offers an audit. Righteousness, tzedaqah, is honest dealing. The Hebrew says in time to come, when you come upon my wages; the Greek tomorrow, my wages are before you; the Latin tomorrow, when the agreed time comes."),
  'shared': ["My righteousness will answer for me in time to come.", "When you inspect my wages.", "Every goat not speckled or spotted and every sheep not dark with me shall be counted stolen."],
  'instructions': [ins(K, S, "Jacob proposed an inspection to prove his honesty."), ins(W, R, "“My righteousness will answer for me”: Jacob stakes his honesty before the man who cheated him. His honesty is real as far as the count goes; the rods are another matter.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew be-yom machar ki-tavo al-sekhari, “in the day to come, when you come upon my wages,” is Greek tē aurion, hoti estin ho misthos mou enōpion sou, “tomorrow, for my wages are before you”; Latin “tomorrow, when the agreed time comes”; King James “in time to come, when it shall come for my hire.”")]},

 '30:34': {
  'received': "Laban said, Very well, let it be as you say.",
  'explain': ("Laban agrees, thinking he has the better of it. The Hebrew begins hen, very well, which the Greek lacks; the Latin I accept. The Hebrew-column rendering was corrected today."),
  'shared': ["Laban said.", "Let it be.", "According to your word."],
  'instructions': [ins(K, S, "Laban accepted Jacob’s terms.")],
  'entries': [],
  'lost': [between("Hebrew hen lu yehi khi-dvarekha, “behold, would it be according to your word,” is Greek estō kata to rhēma sou, “let it be according to your word,” without hen; Latin “I accept what you ask”; King James “Behold, I would it might be according to thy word.”")]},

 '30:35': {
  'received': "That day Laban removed the striped and spotted goats, everything with white on it, and all the dark lambs, and gave them to his sons.",
  'explain': ("Laban removes the marked animals and puts them three days off under his sons, so Jacob’s flock starts with none. The Hebrew says striped, speckled, spotted, dark; the Greek spotted, white-marked, gray; the Latin reverses the arrangement, the single-coloured flock entrusted to his sons."),
  'shared': ["That day he separated the marked male and female goats.", "He separated everything with white on it and all the dark lambs.", "He gave them into the hands of his sons."],
  'instructions': [ins(K, S, "Laban removed the marked animals from Jacob’s care."), ins(W, R, "Laban stacks the deck: Jacob is to breed marked lambs from a flock with no marked parents. The trickster trusts arithmetic, and Jacob trusts something else.")],
  'entries': [],
  'lost': [between("Hebrew aquddim u-tlu’im … nequddot u-tlu’ot … chum, “striped and spotted … speckled and spotted … dark,” is Greek rhantous kai dialeukous … phaion; Latin “variegated and spotted; but the whole flock of a single colour … he entrusted to his sons” reverses which animals go to the sons; King James “ringstraked and spotted … speckled and spotted … brown.”")]},

 '30:36': {
  'received': "He put three days’ journey between them, and Jacob kept the rest of Laban’s flock.",
  'explain': ("Separation to prevent mixing. The Hebrew says between himself and Jacob; the Greek between them and Jacob; the Latin his son-in-law."),
  'shared': ["He set a three days’ journey between himself and Jacob.", "Jacob pastured the rest of Laban’s flock.", "The flocks were apart."],
  'instructions': [ins(K, S, "Jacob was left with Laban’s unmarked flock.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew beno u-ven Ya‘aqov, “between himself and Jacob,” is Greek ana meson autōn kai ana meson Iakōb, “between them and Jacob”; Latin “between himself and his son-in-law”; King James “betwixt himself and Jacob.”")]},

 '30:37': {
  'received': "Jacob took fresh rods of poplar, almond and plane, and peeled white streaks in them.",
  'explain': ("The folk method: striped rods at the trough. The Hebrew trees are livneh, luz, armon, poplar, almond, plane; the Greek styrax, walnut, plane; the King James poplar, hazel, chestnut. The Greek and Latin elaborate the peeling."),
  'shared': ["Jacob took fresh rods of three kinds of tree.", "He peeled white streaks in them.", "The white of the rods showed."],
  'instructions': [ins(K, S, "Jacob prepared peeled rods for the breeding season."), ins(W, R, "Jacob uses the husbandry of his day; the narrator reports the method without endorsing its science, and 31:9 will say who really gave the flocks.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew livneh … luz … armon, “poplar, almond, plane,” is Greek styrakinēn kai karyinēn kai platanou, “styrax, walnut, plane”; Latin “poplar, almond, and plane”; King James “poplar … hazel … chestnut.” Greek and Latin add that the pattern became variegated.")]},

 '30:38': {
  'received': "He set the rods in the troughs where the flock came to drink, so they bred before the rods.",
  'explain': ("The rods before the eyes at mating time. The Hebrew completes the sentence here, they mated when they came to drink; the Greek runs it on into verse 39; the Latin conceive while looking at them."),
  'shared': ["He set the peeled rods in the channels of the watering troughs.", "The flock came there to drink.", "They mated when they came to drink."],
  'instructions': [ins(K, S, "The rods were placed where the flock mated.")],
  'entries': [],
  'lost': [between("Hebrew va-yechamnah be-vo’an lishtot, “and they were in heat when they came to drink,” completes the verse; the Greek hina … enkissēsōsin, “so that they might conceive,” continues into 30:39; Latin and King James follow the Hebrew.")]},

 '30:39': {
  'received': "The flock bred before the rods and bore striped, speckled and spotted young.",
  'explain': ("The result. The Hebrew says striped, speckled, spotted; the Greek white-marked, variegated, ash-gray with spots; the Latin in the heat of mating, spotted, variegated, marked with different colours."),
  'shared': ["The flock bred before the rods.", "They brought forth young.", "The young were striped, speckled and spotted."],
  'instructions': [ins(K, S, "Marked lambs were born in Jacob’s flock.")],
  'entries': [],
  'lost': [between("Hebrew aquddim nequddim u-tlu’im, “striped, speckled, spotted,” is Greek dialeuka kai poikila kai spodoeidē rhanta, “white-marked, variegated, ash-gray spotted”; Latin “spotted, variegated, and marked with different colours” and adds “in the very heat of mating”; King James “ringstraked, speckled, and spotted.”")]},

 '30:40': {
  'received': "Jacob separated the lambs and faced the flock toward the striped and dark animals in Laban’s flock, keeping his own droves apart.",
  'explain': ("A second method: facing the breeding ewes toward marked animals. The Hebrew says turned the flock toward the striped and all the dark in Laban’s flock; the Greek set a white-marked ram and every variegated lamb before the sheep; the Latin placed the branches before the rams, white and black to Laban."),
  'shared': ["Jacob separated the lambs.", "He set the flock facing the marked animals.", "He kept his own flocks apart and did not mix them with Laban’s."],
  'instructions': [ins(K, S, "Jacob kept his growing flock separate from Laban’s."), ins(W, R, "Jacob’s separate droves are the first property he has held in his own name; the man who left with a staff is becoming a house.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew va-yitten pene ha-tzon el-aqod ve-khol-chum be-tzon Lavan, “and he set the faces of the flock toward the striped and all the dark in Laban’s flock,” becomes Greek kai estēsen enantion tōn probatōn krion dialeukon kai pan poikilon en tois amnois, “he set before the sheep a white-marked ram and every variegated one among the lambs”; a ram appears."), between("Latin “placed the branches in the troughs before the rams’ eyes. All the white and black animals belonged to Laban” rewrites; King James “set the faces of the flocks toward the ringstraked, and all the brown.”")]},

 '30:41': {
  'received': "Whenever the stronger animals mated, Jacob set the rods before them, that they might breed among the rods.",
  'explain': ("Selective breeding: the rods for the strong. The Hebrew says the stronger animals, mequshsharot; the Greek when the sheep were mating and conceiving, without strong; the Latin in the early season, rams and ewes."),
  'shared': ["The animals mated.", "Jacob placed the rods before their eyes in the troughs.", "They would mate among the rods."],
  'instructions': [ins(K, S, "Jacob used the rods for the stronger animals.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew ha-tzon ha-mequshsharot, “the bound-up,” that is vigorous, animals, becomes Greek en tō kairō hō enekissēsan ta probata en gastri lambanonta, “at the time the sheep were in heat and conceiving,” without the strength."), between("Latin “when the sheep mated in the early season” and King James “whensoever the stronger cattle did conceive” keep a selection.")]},

 '30:42': {
  'received': "For the feebler animals he did not set the rods; so the feeble were Laban’s and the strong Jacob’s.",
  'explain': ("The result of selection. The Hebrew contrasts weak and strong; the Greek unmarked and marked, when the sheep gave birth; the Latin late-born and early-season; the King James feebler and stronger. The division is by different criteria in each column."),
  'shared': ["In the other case he did not put the rods there.", "One class of animals belonged to Laban.", "The other class belonged to Jacob."],
  'instructions': [ins(K, S, "Jacob’s flock was the stronger, Laban’s the weaker."), ins(W, R, "The weak to Laban and the strong to Jacob: the man who was given the younger-for-elder trick repays it in sheep, and the narrator keeps his own counsel.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew be-ha‘atif ha-tzon … ha-atufim le-Lavan ve-ha-qeshurim le-Ya‘aqov, “when the flock was feeble … the feeble to Laban and the strong to Jacob,” becomes Greek hēnika d’ an eteken ta probata … ta asēma tou Laban, ta de episēma tou Iakōb, “when the sheep gave birth … the unmarked Laban’s, the marked Jacob’s”; strength becomes marking."), between("Latin “the late-born became Laban’s, and those of the early season Jacob’s” reads the seasons; King James “the feebler were Laban’s, and the stronger Jacob’s.”")]},

 '30:43': {
  'received': "Jacob grew exceedingly rich, with large flocks, servants, camels and donkeys.",
  'explain': ("The inventory of a patriarch, as for Abraham in 12:16 and 24:35. The Greek adds oxen; the Hebrew flocks, female and male slaves, camels, donkeys."),
  'shared': ["The man became exceedingly prosperous.", "He had large flocks.", "He had female and male servants, camels and donkeys."],
  'instructions': [ins(K, S, "Jacob became very wealthy in Laban’s service."), ins(W, R, "“The man became exceedingly great” was said of Isaac in Gerar and now of Jacob in Haran; the blessing of Abraham is counted in the same coin in each generation.")],
  'entries': ['jacob'],
  'lost': [keeps("An added ktēnē kai boes, “livestock and oxen,” in the Greek inventory; Hebrew tzon rabbot, “many flocks.”"), between("Latin “many flocks, maidservants, male servants, camels, and donkeys” and King James “much cattle, and maidservants, and menservants, and camels, and asses” follow the Hebrew.")]},
 }
}
