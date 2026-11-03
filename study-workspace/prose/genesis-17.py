# Study prose for Genesis 17 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 17,
 'chapterNote': (
  "The covenant of circumcision, the new names and the promise of Isaac are the same in every column; the word covenant comes thirteen times in "
  "all of them. What varies is in the titles, the pronouns and the legal detail. The Hebrew keeps El Shaddai, “walk before me,” “I will make you "
  "fruitful,” Sarah as the one blessed and the mother of nations in 17:16, twelve princes for Ishmael, a passive circumcision for Abraham, and no "
  "deadline in the sanction of 17:14. The Greek keeps “I am your God,” “be pleasing before me,” “increase,” “throughout their generations” added "
  "to the command, the eighth day added to the sanction with “destroyed” and “scattered,” the promised child as the one blessed in 17:16, twelve "
  "nations for Ishmael, and Abraham circumcising himself and his household actively. The Latin and King James follow the Hebrew; the Latin lacks "
  "the first clause of 17:13."),
 'verses': {

 '17:1': {
  'received': "When Abram was ninety-nine the Lord appeared and said, I am God Almighty; walk before me and be blameless.",
  'explain': ("Thirteen years of silence end. Abram is ninety-nine, his body as good as dead in Paul’s phrase, and God appears with a new name and "
   "a demand. The Hebrew name is El Shaddai, traditionally God Almighty; the Greek says I am your God. The Hebrew asks Abram to walk before "
   "God, the Greek to be pleasing before him, the rendering it used of Enoch and Noah. Blameless is the Hebrew word for a whole, unblemished sacrifice."),
  'shared': ["Abram was ninety-nine when the Lord appeared to him.", "God declared who he is.", "Abram is to live before God and be blameless."],
  'instructions': [ins(C, S, "Walk before me and be blameless."), ins(K, S, "God revealed himself to Abram as God Almighty."), ins(W, R, "After thirteen silent years the first word is a name and a command; God’s self-disclosure and his claim on a life come together.")],
  'entries': ['el-shaddai', 'abraham', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew ani El Shaddai, “I am El Shaddai,” a divine title, becomes Greek egō eimi ho theos sou, “I am your God,” without the title. Hebrew hithallekh lefanai, “walk before me,” becomes Greek euarestei enantion emou, “be pleasing before me,” as at 5:22 and 6:9. Hebrew YHWH appeared is Greek kyrios."),
   keeps("Greek euarestei is the verb of Hebrews 11:5–6; amemptos, “blameless,” is the word Luke 1:6 uses of Zechariah and Elizabeth."),
   between("Latin “I am God Almighty. Walk before Me” and King James “I am the Almighty God; walk before me, and be thou perfect” keep the title and the walk. Romans 4:19 reads the age."),
  ]},

 '17:2': {
  'received': "God will set his covenant between himself and Abram and multiply him greatly.",
  'explain': ("The covenant of chapter 15 is renewed and the promise of many descendants repeated. God sets the covenant as a gift from his side; "
   "it is not a bargain between equals. The Hebrew doubles the intensifier, very very greatly; the Greek has it once here. The versions agree."),
  'shared': ["God will set his covenant between himself and Abram.", "He will multiply Abram.", "The multiplication will be great."],
  'instructions': [ins(K, S, "God renewed his covenant with Abram and the promise of multiplication."), ins(W, R, "God sets the covenant; Abram does not negotiate it. The initiative stays where it was in chapter 15.")],
  'entries': ['term-covenant', 'abraham'],
  'lost': [between("Hebrew bi-me’od me’od, “very very,” is Greek sphodra, once; Hebrew ve-ettenah, “I will give” or “set,” is Greek thēsomai, “I will set.” Latin “establish … exceedingly” and King James “make … exceedingly” agree in sense. Luke 1:72–73 remembers the covenant.")]},

 '17:3': {
  'received': "Abram fell on his face, and God spoke to him.",
  'explain': ("Abram answers the appearance with prostration, the posture he will take again in verse 17. God speaks. The Hebrew and Greek "
   "include the speaking here; the Latin ends the verse with the falling and carries God’s speaking into verse 4."),
  'shared': ["Abram fell on his face.", "God spoke.", "What follows is God’s word to him."],
  'instructions': [ins(K, S, "Abram bowed to the ground before God’s word."), ins(W, R, "The body speaks before the mouth; prostration is Abram’s answer to the name he has just heard.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew va-yedabber itto Elohim, “God spoke with him,” is Greek elalēsen autō ho theos, “spoke to him”; the Latin has only “Abram fell facedown,” moving the speech to 17:4. King James follows the Hebrew.")]},

 '17:4': {
  'received': "God declared that his covenant was with Abram and that he would be the father of a multitude of nations.",
  'explain': ("God’s side comes first: as for me. Abram’s side will begin at verse 9, as for you. The promise is fatherhood of a multitude of "
   "nations, which Paul reads as Abraham fathering all who believe, Gentile and Jew. The Latin begins “God said to him, It is I.”"),
  'shared': ["God sets out his own side of the covenant.", "His covenant is with Abram.", "Abram will be the father of a multitude of nations."],
  'instructions': [ins(K, S, "God’s covenant made Abram father of many nations."), ins(W, R, "“As for me” before “as for you”: the covenant is stated as God’s undertaking before it becomes Abram’s duty.")],
  'entries': ['term-covenant', 'abraham'],
  'lost': [between("Hebrew ani hinneh, “I, behold,” is Greek kai egō idou, “and I, behold”; Latin Ego sum, “It is I,” with “God said to him” carried from 17:3. Hebrew hamon goyim and Greek plēthous ethnōn are “multitude of nations”; Latin and King James “many nations.” Romans 4:16–17 and Galatians 3:7–9 are Paul’s reading.")]},

 '17:5': {
  'received': "Abram’s name becomes Abraham, because God has made him the father of a multitude of nations.",
  'explain': ("The first renaming by God in Scripture. Abram means exalted father; Abraham is explained by sound as father of a multitude, "
   "av-hamon. The Hebrew says I have made you; the Greek and Latin I have appointed you. The new name is a promise carried in every greeting."),
  'shared': ["His name will no longer be Abram.", "His name will be Abraham.", "The reason is that God has made him father of many nations."],
  'instructions': [ins(K, S, "God renamed Abram as Abraham, father of a multitude."), ins(W, R, "A name is changed before the thing it names exists; Abraham must answer to “father of a multitude” while he has one son by a slave.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew netattikha, “I have made you,” is Greek tetheika se, “I have appointed you”; Latin constitui, “appointed,” King James “have I made thee.” Hebrew Avraham and Greek Abraam are the same name. Nehemiah 9:7 and Romans 4:17 recall it.")]},

 '17:6': {
  'received': "God will make Abraham exceedingly fruitful, with nations and kings coming from him.",
  'explain': ("The promise widens from descendants to nations and kings. The Hebrew uses fruitfulness language, the verb of 1:28, with the "
   "doubled intensifier; the Greek says increase and keeps the double “very very” here where it dropped it in verse 2. Kings will come from "
   "a man with no land and one son."),
  'shared': ["God will make Abraham exceedingly fruitful.", "He will make nations of him.", "Kings will come from him."],
  'instructions': [ins(K, S, "Nations and kings were promised to come from Abraham.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew ve-hifreti, “I will make fruitful,” is Greek auxanō, “I will increase”; the Hebrew bi-me’od me’od is matched by Greek sphodra sphodra here. Latin “increase exceedingly” and King James “exceeding fruitful” divide.")]},

 '17:7': {
  'received': "God establishes an everlasting covenant with Abraham and his offspring through their generations, to be their God.",
  'explain': ("The heart of the chapter: an everlasting covenant with Abraham and his line, whose content is a relationship, to be God to you and "
   "to your offspring. The covenant passes down the family as the Passover and the Sabbath will. The phrase everlasting covenant was first used "
   "of the rainbow; Hebrews uses it of the blood of Christ. All versions agree."),
  'shared': ["God establishes his covenant with Abraham and his offspring through their generations.", "It is an everlasting covenant.", "Its content is that God will be God to them."],
  'instructions': [ins(K, S, "God bound himself to be the God of Abraham and his descendants forever."), ins(W, R, "The gift inside the covenant is God himself; land and children follow from “to be God to you,” not the other way round.")],
  'entries': ['term-covenant', 'abraham'],
  'lost': [between("Hebrew, Greek, Latin and King James agree in every clause; the Latin phrases the end “to be your God and the God of your offspring.” Greek diathēkē aiōnios is the phrase of 9:16 and Hebrews 13:20; Exodus 12:14 and 31:16 carry “throughout their generations.”")]},

 '17:8': {
  'received': "God gives Abraham and his offspring the land of his sojourning, all Canaan, as an everlasting possession, and will be their God.",
  'explain': ("The land is added to the relationship: all Canaan, where Abraham is now a stranger, as an everlasting holding. The Greek word "
   "means land kept firmly, and Jacob will recall the promise in these words to Joseph in Egypt. The clause “I will be their God” closes God’s "
   "side of the covenant as it opened it."),
  'shared': ["God gives Abraham and his offspring the land where he sojourns.", "It is all the land of Canaan, an everlasting possession.", "God will be their God."],
  'instructions': [ins(K, S, "All Canaan was given to Abraham’s line as an everlasting possession."), ins(W, R, "The land of his wandering becomes the land of his heirs; the stranger is promised the place he is passing through.")],
  'entries': ['canaan', 'abraham'],
  'lost': [between("Hebrew erets megurekha, “the land of your sojournings,” is Greek tēn gēn hēn paroikeis, “the land where you sojourn”; Latin “the land of your sojourning,” King James “the land wherein thou art a stranger.” Greek kataschesin aiōnion, “everlasting possession,” recurs in 48:4 and Acts 7:5.")]},

 '17:9': {
  'received': "God told Abraham that he and his offspring must keep the covenant through their generations.",
  'explain': ("Now Abraham’s side: as for you, keep my covenant. The Greek verb means to watch over carefully, as Mary kept all these things in "
   "her heart. The obligation falls on Abraham and on every generation after him. The versions agree; the Latin says God spoke again."),
  'shared': ["God spoke to Abraham.", "Abraham is to keep God’s covenant.", "His offspring are to keep it through their generations."],
  'instructions': [ins(C, S, "Keep my covenant, you and your offspring through their generations."), ins(W, R, "God has set the covenant; Abraham’s part is to keep it. The order is grace, then obedience.")],
  'entries': ['term-covenant', 'abraham'],
  'lost': [between("Hebrew ve-attah, “and as for you,” is Greek sy de; Hebrew tishmor, “you shall keep,” is Greek diatērēseis, the verb of Luke 2:51 and Acts 15:29. Latin “God said again” and King James “therefore” are connective wording.")]},

 '17:10': {
  'received': "The covenant Abraham must keep is this: every male among his people shall be circumcised.",
  'explain': ("The covenant is given a sign in the flesh. Every male is to be circumcised; the promise includes Sarah by name, but the sign is "
   "placed on the males. The Greek adds “throughout their generations” to the command and drops “my” before covenant; the Hebrew addresses a "
   "plural “you shall keep,” the Greek a singular. Moses and Jeremiah will call for circumcised hearts."),
  'shared': ["This is the covenant to be kept.", "It is between God and Abraham and his offspring.", "Every male among them shall be circumcised."],
  'instructions': [ins(C, S, "Every male among you shall be circumcised."), ins(K, S, "Circumcision was given as the covenant to be kept."), ins(W, R, "The sign cuts the flesh that carries the promised seed; the covenant is marked where the future is made.")],
  'entries': ['term-covenant'],
  'lost': [
   keeps("Greek adds eis tas geneas autōn, “throughout their generations,” to the covenant command, and reads hē diathēkē, “the covenant,” for Hebrew beriti, “my covenant.” Hebrew tishmeru, “you (plural) shall keep,” is Greek diatērēseis, singular."),
   between("Latin “My covenant that you shall observe” and King James “my covenant, which ye shall keep” follow the Hebrew, King James keeping the plural. Deuteronomy 10:16 and Romans 4:11 take up circumcision."),
  ]},

 '17:11': {
  'received': "They shall be circumcised in the flesh of the foreskin, as a sign of the covenant between God and them.",
  'explain': ("The rite is specified and named a sign, like the rainbow and later the Sabbath. Paul calls Abraham’s circumcision a sign and "
   "seal of the righteousness he already had by faith in chapter 15. The Greek word for the foreskin is Paul’s word for the uncircumcised, "
   "the Gentiles. The versions agree; the Latin and King James make the verb active."),
  'shared': ["They are to be circumcised in the flesh of the foreskin.", "It shall be a sign.", "It is a sign of the covenant between God and them."],
  'instructions': [ins(C, S, "Circumcise the flesh of the foreskin as a sign of the covenant."), ins(W, R, "A sign is something to look at and remember by; the covenant is written on the body so that it cannot be forgotten.")],
  'entries': ['term-covenant'],
  'lost': [between("Hebrew u-nemaltem, “you shall be circumcised,” is Greek peritmēthēsesthe, passive, as the Hebrew; Latin circumcidetis and King James “ye shall circumcise” make it active. Greek akrobystia is Paul’s word in Romans 2:25–26; sēmeion diathēkēs is the sign of 9:13 and Exodus 31:13.")]},

 '17:12': {
  'received': "Every male is to be circumcised at eight days old, through the generations, whether born in the house or bought from a foreigner.",
  'explain': ("The rule is made precise: the eighth day, which the Law will confirm and on which John and Jesus were circumcised, and the scope "
   "widened to every male of the household, slaves bought from foreigners included. From the start people outside Abraham’s blood are brought "
   "into the covenant household. The Greek calls the eight-day-old a child; the Latin rearranges the clauses."),
  'shared': ["Every male is to be circumcised at eight days old.", "This holds throughout the generations.", "It includes those born in the house and those bought from foreigners."],
  'instructions': [ins(C, S, "Circumcise every male at eight days old, including servants born or bought."), ins(W, R, "The sign of the promise is given to infants who cannot choose and to slaves who were not born to it; the covenant is wider than its blood.")],
  'entries': ['term-covenant'],
  'lost': [between("Hebrew ben-shemonat yamim, “a son of eight days,” is Greek paidion oktō hēmerōn, “a child of eight days”; Hebrew yelid bayit, “born in the house,” is Greek oikogenēs. Latin “every male infant … both those born in your household and those purchased … including whoever is not of your lineage” reorders; King James follows the Hebrew. Leviticus 12:3, Luke 1:59 and 2:21 are the eighth day.")]},

 '17:13': {
  'received': "Those born in the house and those bought must be circumcised, so that God’s covenant is in their flesh as an everlasting covenant.",
  'explain': ("The requirement is repeated with emphasis, must surely be circumcised, and the sign is called the covenant itself, in your flesh. "
   "The Hebrew and Greek have both clauses; the Latin has only the second, lacking the repeated requirement. The Greek says the covenant is upon "
   "the flesh, the Hebrew in it. Ezekiel and Paul will look for a covenant written on hearts of flesh."),
  'shared': ["Those born in the house and those bought must be circumcised.", "God’s covenant is in their flesh.", "It is an everlasting covenant."],
  'instructions': [ins(C, S, "The household-born and the purchased alike must be circumcised."), ins(K, S, "The covenant is carried in the flesh as an everlasting covenant.")],
  'entries': ['term-covenant'],
  'lost': [
   loses("Hebrew bi-vsarkhem, “in your flesh,” is Greek epi tēs sarkos hymōn, “upon your flesh”; Hebrew miqnat kaspekha, “bought with your money,” loses “your” in Greek. The Hebrew emphatic himmol yimmol, “must surely be circumcised,” is matched by Greek peritomē peritmēthēsetai."),
   between("Latin has only “My covenant shall be in your flesh as an everlasting covenant,” without the first clause; King James has both with the Hebrew. Ezekiel 36:26 and Romans 2:28–29 are the echoes."),
  ]},

 '17:14': {
  'received': "An uncircumcised male is cut off from his people, for he has broken the covenant.",
  'explain': ("The sanction: the uncircumcised male is cut off from his people. The Hebrew states it without a deadline; the Greek adds “on the "
   "eighth day,” aligning the penalty with the rule of verse 12, and says the person shall be destroyed and has scattered the covenant where the "
   "Hebrew says cut off and broken. Early Christian writers saw the eighth day as a figure of the resurrection."),
  'shared': ["An uncircumcised male is in view.", "That person shall be cut off from his people.", "He has broken God’s covenant."],
  'instructions': [ins(K, S, "Neglect of circumcision broke the covenant and cut a man off from his people."), ins(W, R, "To refuse the sign is to refuse the covenant; the body’s mark and the people’s membership stand or fall together.")],
  'entries': ['term-covenant'],
  'lost': [
   keeps("Greek adds tē hēmera tē ogdoē, “on the eighth day,” to the sanction; the Hebrew has the deadline only in 17:12. Hebrew ve-nikhretah, “shall be cut off,” becomes Greek exolethreuthēsetai, “shall be destroyed,” and Hebrew hefar, “has broken,” becomes dieskedasen, “has scattered.”"),
   between("Latin “cut off from his people, because he has broken My covenant” and King James “cut off from his people; he hath broken my covenant” follow the Hebrew without the eighth day. John 20:26 is the eighth day of the fathers’ reading."),
  ]},

 '17:15': {
  'received': "God told Abraham that Sarai’s name would now be Sarah.",
  'explain': ("Sarah is renamed as Abraham was, the only woman in Scripture to receive a new name from God. Both forms mean princess; the "
   "change is in the ending, and kings of peoples will come from her. The Hebrew commands Abraham, you shall not call her Sarai; the Greek "
   "states it passively, her name shall not be called Sarai. The English keeps Sarai and Sarah so the change is visible."),
  'shared': ["God spoke to Abraham about his wife Sarai.", "Her name is no longer Sarai.", "Her name is Sarah."],
  'instructions': [ins(K, S, "God renamed Sarai as Sarah."), ins(W, R, "Sarah is renamed before she is told she will bear; the promise reaches her through her husband but is about her.")],
  'entries': ['sarah', 'abraham'],
  'lost': [between("Hebrew lo-tiqra, “you shall not call,” a command to Abraham, is Greek ou klēthēsetai, “shall not be called,” passive. Greek Sara and Sarra mark the change by doubling the consonant where Hebrew changes the ending. Latin and King James keep the command. Isaiah 51:2 and 1 Peter 3:6 remember Sarah.")]},

 '17:16': {
  'received': "God will bless Sarah and give Abraham a son by her, and from that line nations and kings will come.",
  'explain': ("Sarah is blessed in her own right, and the barren wife is promised a son at ninety. Then the versions part. The Hebrew keeps Sarah "
   "as the subject: I will bless her, she shall become nations, kings of peoples from her. The Greek shifts to the child: I will bless him, he "
   "shall become nations, kings of nations from him; the Latin follows the Greek. The Greek says child, not son."),
  'shared': ["God will bless Sarah.", "He will give Abraham a son by her.", "Nations and kings of peoples will come from that line."],
  'instructions': [ins(K, S, "Sarah was promised a son and a line of nations and kings."), ins(W, R, "Whether the blessing rests on the mother or the child, it rests on a birth no one expects; the barren woman is the chosen channel.")],
  'entries': ['sarah', 'abraham'],
  'lost': [
   loses("Hebrew u-verakhtiha ve-hayetah le-goyim, malkhe ammim mimmennah yihyu, “I will bless her, and she shall become nations; kings of peoples shall be from her,” keeps Sarah as subject three times. Greek eulogēsō auton kai estai eis ethnē, kai basileis ethnōn ex autou esontai, “I will bless him, and he shall become nations, and kings of nations shall be from him,” shifts to the child. Hebrew ben, “son,” is Greek teknon, “child,” in the first clause."),
   between("Latin “a son by her, whom I will bless. He shall become nations … from him” follows the Greek; King James “yea, I will bless her, and she shall be a mother of nations; kings of people shall be of her” follows the Hebrew. Genesis 35:11 and 36:31 bring the kings."),
  ]},

 '17:17': {
  'received': "Abraham fell on his face and laughed, asking himself whether a man of a hundred and a woman of ninety could have a child.",
  'explain': ("Abraham laughs, and the Hebrew verb will give Isaac his name. He falls on his face as in verse 3, but this time with laughter and "
   "two inward questions about his age and Sarah’s. The Hebrew says he spoke in his heart, the Greek in his mind; the laughter itself is not "
   "located. Sarah will laugh next, and at the birth will say God has made laughter for her."),
  'shared': ["Abraham fell on his face and laughed.", "He asked inwardly whether a man of a hundred could have a child.", "He asked whether Sarah at ninety could bear."],
  'instructions': [ins(K, S, "Abraham laughed at the promise of a son in his and Sarah’s old age."), ins(W, R, "The laughter is recorded without rebuke here; faith and incredulity share one face, and God names the child after the laugh.")],
  'entries': ['abraham', 'sarah', 'isaac'],
  'lost': [between("Hebrew be-libbo, “in his heart,” is Greek en tē dianoia autou, “in his mind”; Hebrew yitschaq, “he laughed,” is the sound of Yitschaq, Isaac, which Greek egelasen cannot carry. Latin and King James say heart. Genesis 18:12 and 21:6 continue the laughter.")]},

 '17:18': {
  'received': "Abraham asked that Ishmael might live before God.",
  'explain': ("Abraham’s plea is for the son he already has. The Hebrew is a wish, if only Ishmael might live before you; the Greek a direct "
   "appeal, let this Ishmael live before you. Both ask for Ishmael’s life and standing, and God will answer in verse 20 while keeping the covenant "
   "line for Isaac."),
  'shared': ["Abraham spoke to God.", "His plea concerned Ishmael.", "He asked that Ishmael might live before God."],
  'instructions': [ins(K, S, "Abraham pleaded for Ishmael’s life and standing before God."), ins(W, R, "The father asks for the son he can see rather than the one he is promised; God grants the first without surrendering the second.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew lu Yishma‘el yichyeh, “if only Ishmael might live,” a wish, is Greek Ismaēl houtos zētō, “let this Ishmael live,” an appeal with a demonstrative. Latin utinam and King James “O that” keep the wish. Genesis 21:13 is the answer.")]},

 '17:19': {
  'received': "God replied that Sarah would indeed bear Abraham a son, to be named Isaac, with whom he would establish an everlasting covenant.",
  'explain': ("God answers the laugh and the plea at once: yes, Sarah will bear a son, and his name will be Isaac, from the laughter. The covenant "
   "is to run through him and his offspring. The Greek opens with an emphatic “yes, behold” and addresses Abraham by name; the Hebrew says "
   "“indeed.” Paul calls believers children of promise, like Isaac."),
  'shared': ["Sarah will bear Abraham a son.", "He is to be named Isaac.", "God will establish an everlasting covenant with him and his offspring."],
  'instructions': [ins(K, S, "God named Isaac before his conception and fixed the covenant on him."), ins(W, R, "The child is named for the father’s laugh; God turns incredulity into the name of the promise.")],
  'entries': ['isaac', 'sarah', 'term-covenant', 'abraham'],
  'lost': [between("Hebrew aval, “indeed,” is Greek nai, idou, “yes, behold”; the Greek adds “to Abraham” and “with his offspring” where the Hebrew has “for his offspring.” Latin follows the Greek address and the Hebrew sense; King James “a son indeed” follows the Hebrew. Galatians 4:28 and Romans 9:7 read Isaac.")]},

 '17:20': {
  'received': "God had heard Abraham about Ishmael: he would bless him, multiply him, make him father of twelve rulers and a great nation.",
  'explain': ("Ishmael is not forgotten. God has heard, and the name means that; he will bless and multiply him and make him a great nation, "
   "the words given to Abram in 12:2. The Hebrew promises twelve princes, the tribal chiefs listed in chapter 25; the Greek says twelve nations, "
   "the peoples they lead. The Hebrew has fruitfulness and a doubled intensifier; the Greek increase and one."),
  'shared': ["God has heard Abraham concerning Ishmael.", "God has blessed him and will multiply him greatly.", "He will father twelve rulers and become a great nation."],
  'instructions': [ins(K, S, "Ishmael was blessed with twelve rulers and a great nation, though not the covenant."), ins(W, R, "Blessing and covenant are not the same; Ishmael receives the one and not the other, and both are God’s gifts.")],
  'entries': ['abraham', 'hagar'],
  'lost': [
   loses("Hebrew shenem-asar nesi’im, “twelve princes,” becomes Greek dōdeka ethnē, “twelve nations”; the chiefs become their peoples. Hebrew ve-hifreti, “I will make him fruitful,” is Greek auxanō, “increase,” and bi-me’od me’od is sphodra once."),
   between("Latin “twelve princes (duces) … I will bless him” and King James “twelve princes … I have blessed him” keep the princes; the Latin makes the blessing future. Genesis 25:16 lists the twelve; 21:13 and 21:18 repeat the great nation."),
  ]},

 '17:21': {
  'received': "But the covenant would be established with Isaac, whom Sarah would bear at this time next year.",
  'explain': ("The line is drawn: the covenant goes to Isaac, and a date is set, this appointed time next year. Ishmael is blessed; Isaac is the "
   "heir. All versions agree; the Greek phrase “in the other year” means the following year."),
  'shared': ["God will establish his covenant with Isaac.", "Sarah will bear him.", "It will be at this time next year."],
  'instructions': [ins(K, S, "The covenant was fixed on Isaac, to be born within a year."), ins(W, R, "A date is given to the impossible; faith is asked to wait one year, not forever.")],
  'entries': ['isaac', 'sarah', 'term-covenant'],
  'lost': [between("Hebrew la-mo‘ed ha-zeh ba-shanah ha-acheret, “at this appointed time in the next year,” is Greek eis ton kairon touton en tō eniautō tō heterō, “at this time in the other year,” meaning next. Latin “at this time next year” and King James “at this set time in the next year” agree.")]},

 '17:22': {
  'received': "When God had finished speaking, he went up from Abraham.",
  'explain': ("The audience ends and God goes up, the same word used after he speaks with Jacob at Bethel and of the angel at Manoah’s altar. "
   "The chapter turns from word to deed. The versions agree."),
  'shared': ["God finished speaking with Abraham.", "God went up.", "He went up from Abraham."],
  'instructions': [ins(K, S, "God departed when the covenant speech was complete.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew va-yekhal le-dabber itto, “he finished speaking with him,” is Greek synetelesen de lalōn pros auton; Hebrew va-ya‘al, “went up,” is Greek anebē. Latin and King James agree. Genesis 35:13 and Judges 13:20 use the same going up.")]},

 '17:23': {
  'received': "That very day Abraham circumcised Ishmael and every male of his household, as God had said.",
  'explain': ("Obedience is immediate and complete: Ishmael, the household-born, the purchased, every male, on that very day. The Hebrew stresses "
   "the same day and says the flesh of their foreskin; the Greek says at the time of that day and their foreskins. The Latin adds “immediately.” "
   "The sign is given to the whole household before the promised son exists."),
  'shared': ["Abraham took Ishmael and every male of his household.", "He circumcised them on that very day.", "He did as God had spoken to him."],
  'instructions': [ins(K, S, "Abraham circumcised his whole household the same day God commanded it."), ins(W, R, "The command of the morning is kept before night; Abraham’s obedience is measured in hours.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew be-etsem ha-yom ha-zeh, “on that very day,” is Greek en tō kairō tēs hēmeras ekeinēs, “at the time of that day,” which names no hour; Hebrew besar orlatam, “the flesh of their foreskin,” is Greek tas akrobystias autōn, “their foreskins.” Latin “immediately, on that very day … as God had commanded” and King James “in the selfsame day, as God had said” follow the Hebrew.")]},

 '17:24': {
  'received': "Abraham was ninety-nine when he was circumcised.",
  'explain': ("Abraham’s own circumcision is dated: ninety-nine, the age of verse 1. The Hebrew says he was circumcised, a passive or reflexive "
   "form; the Greek and Latin that he circumcised his own flesh, making him the agent. The old man takes the sign on himself."),
  'shared': ["Abraham was ninety-nine years old.", "He was circumcised.", "The sign was in his own flesh."],
  'instructions': [ins(K, S, "Abraham himself was circumcised at ninety-nine."), ins(W, R, "The father of the covenant receives its sign at the same age as its promise; he is marked as he is renamed.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew be-himmolo, “in his being circumcised,” passive or reflexive, becomes Greek hēnika perieteme, “when he circumcised,” active, with Abraham performing the act."),
   between("Latin “when he circumcised the flesh of his foreskin” follows the Greek; King James “when he was circumcised” the Hebrew."),
  ]},

 '17:25': {
  'received': "Ishmael was thirteen when he was circumcised.",
  'explain': ("Ishmael’s age is thirteen, which fits the dates of 16:16 and 17:1. The passive form is kept in all versions. Later Arab custom "
   "circumcised at about this age, and Jewish tradition set the bar mitzvah at thirteen."),
  'shared': ["Ishmael was Abraham’s son.", "He was thirteen years old.", "He was circumcised."],
  'instructions': [ins(K, S, "Ishmael was circumcised at thirteen.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James agree; the Latin phrases it “had reached thirteen years at the time of his circumcision.”")]},

 '17:26': {
  'received': "Abraham and Ishmael were circumcised on the same day.",
  'explain': ("Father and son receive the sign together. The Hebrew says on that very day; the Greek at the time of that day, as in verse 23, "
   "without naming an hour. The Latin runs the sentence on into verse 27."),
  'shared': ["Abraham was circumcised.", "His son Ishmael was circumcised.", "It was on the same day."],
  'instructions': [ins(K, S, "Abraham and Ishmael were circumcised together.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew be-etsem ha-yom ha-zeh is again Greek en tō kairō tēs hēmeras ekeinēs. Latin “on that same day” and King James “in the selfsame day” follow the Hebrew.")]},

 '17:27': {
  'received': "All the men of his household, born there or bought from foreigners, were circumcised with him.",
  'explain': ("The chapter ends with the whole household marked. The Hebrew says all the men were circumcised with him, including those bought "
   "from a foreigner; the Greek makes Abraham the one who circumcised them and speaks of foreign nations; the Latin counts the foreigners as a "
   "third group circumcised together. The Greek word for foreign is the one used of the Samaritan who returned to give thanks."),
  'shared': ["All the men of Abraham’s household are included.", "Those born in the house and those bought are included.", "They were circumcised with Abraham."],
  'instructions': [ins(K, S, "Every man of Abraham’s household, foreign-born included, received the covenant sign."), ins(W, R, "The covenant household is larger than the family; slaves of foreign birth carry the same mark as the heir.")],
  'entries': ['abraham', 'term-covenant'],
  'lost': [
   loses("Hebrew nimmolu itto, “were circumcised with him,” passive, becomes Greek perietemen autous, “he circumcised them,” active; Hebrew me’et ben-nekhar, “from a foreigner,” becomes Greek ek allogenōn ethnōn, “from foreign nations.”"),
   between("Latin “those born there as well as those purchased and foreigners, were circumcised together” makes foreigners a separate group; King James “bought with money of the stranger, were circumcised with him” follows the Hebrew. Greek allogenēs is the word of Luke 17:18."),
  ]},
 }
}
