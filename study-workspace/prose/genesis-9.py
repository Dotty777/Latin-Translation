# Study prose for Genesis 9 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 9,
 'chapterNote': (
  "The blessing of Noah, the law of blood, the covenant of the bow and the scene in the tent are told alike in every column. What "
  "varies is in the phrasing of the commands and the curse. The Hebrew keeps “swarm on the earth,” “by humans his blood shall be shed,” "
  "the repeated “every wild animal of the earth,” “the bow” and “between God and every living creature,” Noah uncovering himself in his "
  "tent, “a slave of slaves,” and the pun of Japheth’s name. The Greek keeps an added “exercise dominion over it” in 9:1, “I made” for "
  "“he made” in 9:6, “the Lord God said to Noah” in 9:12, “my bow” and “between me,” Noah uncovered in his house, Ham who “went out,” "
  "a “household slave,” and the houses of Shem. The Latin and King James follow the Hebrew; the Latin gives Canaan to Japheth alone in 9:27."),
 'verses': {

 '9:1': {
  'received': "God blessed Noah and his sons and told them to be fruitful, multiply and fill the earth.",
  'explain': ("The blessing of creation is spoken again. Be fruitful, multiply, fill the earth: the words of 1:28 to the new humanity. "
   "The Greek adds a fourth command, exercise dominion over it, completing the echo of 1:28; the Hebrew, Latin and King James have "
   "three. At Babel people will try not to be scattered, resisting this very charge."),
  'shared': ["God blessed Noah and his sons.", "He told them to be fruitful and multiply.", "He told them to fill the earth."],
  'instructions': [ins(C, S, "Be fruitful, multiply and fill the earth."), ins(W, R, "The blessing is renewed after judgement; the flood did not withdraw God’s first word to humankind.")],
  'entries': ['noah'],
  'lost': [
   keeps("An added kai katakyrieusate autēs, “and exercise dominion over it,” which the Hebrew does not have here; the Greek completes the fourfold charge of 1:28. The addition is a literary echo whose origin is not known."),
   between("Latin “increase and multiply, and fill the earth” and King James “be fruitful, and multiply, and replenish the earth” give three commands with the Hebrew."),
  ]},

 '9:2': {
  'received': "Every animal, bird and fish will fear humankind, for they are given into human hands.",
  'explain': ("Human rule is restated in harsher terms than in chapter 1: now the creatures fear. Wild animals, birds, everything "
   "that moves and the fish of the sea are handed over. The Hebrew says they have been given, a passive; the Greek says I have given, "
   "making God the giver. The Latin separates the fish into their own sentence."),
  'shared': ["The fear and dread of humankind will be on the animals and birds.", "Everything that moves and the fish of the sea are included.", "They are given into human hands."],
  'instructions': [ins(K, S, "The creatures were placed under human authority after the flood."), ins(W, R, "Dominion after the flood comes with fear on the creatures’ side; the relationship is no longer the peace of the garden.")],
  'entries': [],
  'lost': [between("Hebrew be-yedkhem nittanu, “into your hand they have been given,” is Greek hypo cheiras hymin dedōka, “I have given them under your hands.” Hebrew “fear and dread” is Greek “dread and fear.” Latin makes the fish a separate sentence; King James keeps the Hebrew passive.")]},

 '9:3': {
  'received': "Every living creature may now be food, as the green plants were given before.",
  'explain': ("Permission widens. In 1:29 the food was plants; now every moving thing that lives may be eaten, given as the plants were. "
   "The Hebrew says every moving thing, the Greek every creeping thing; both mean the animals at large. The gift is God’s."),
  'shared': ["Every living, moving creature may be food.", "The gift is compared with the green plants.", "God has given everything."],
  'instructions': [ins(K, S, "God permitted animals as food after the flood."), ins(W, R, "Food is received as given; the permission is a gift with a limit attached in the next verse.")],
  'entries': [],
  'lost': [between("Hebrew kol-remes, “every moving thing,” is Greek pan herpeton, “every creeping thing,” a broader use of the word. Latin “everything that moves and lives” and King James “every moving thing that liveth” follow the Hebrew.")]},

 '9:4': {
  'received': "Flesh must not be eaten with its blood, which is its life.",
  'explain': ("One limit on the new permission. The Hebrew puts blood in apposition to life, flesh with its life, its blood; the Greek says "
   "flesh with blood of life; the Latin simply flesh with blood. The principle that life is in the blood will run through the law and "
   "into the apostles’ letter in Acts 15."),
  'shared': ["Flesh with its blood is not to be eaten.", "Blood is identified with life.", "The limit stands inside the permission."],
  'instructions': [ins(C, S, "You shall not eat flesh with its blood."), ins(W, R, "Life belongs to God even when the animal is given for food; the blood is the sign of that reserve.")],
  'entries': [],
  'lost': [between("Hebrew basar be-nafsho damo, “flesh with its life, its blood,” is Greek kreas en haimati psychēs, “flesh with blood of life.” Latin “flesh with blood” drops the life; King James “flesh with the life thereof, which is the blood thereof” keeps the Hebrew apposition. Leviticus 17:11 and Acts 15:20 take it up.")]},

 '9:5': {
  'received': "God will require an account for human blood, from every animal and from every human brother.",
  'explain': ("Human life is placed under God’s own protection. He will demand a reckoning for blood shed, from animals and from people. "
   "The Hebrew says from a human, from each one’s brother; the Greek compresses it to a human brother; the Latin and King James spell it "
   "out at length. Jesus uses the Greek verb when he says the blood of the prophets will be required of his generation."),
  'shared': ["God will require the blood of human lives.", "He will require it from every animal.", "He will require it from humans, each one’s brother."],
  'instructions': [ins(K, S, "God holds animals and people accountable for human life."), ins(W, R, "Every person is someone’s brother; the taking of a life is answered to God, not only to the family.")],
  'entries': [],
  'lost': [
   loses("Hebrew u-mi-yad ha-adam mi-yad ish achiv, “and from a human, from the hand of each one’s brother,” two clauses, becomes Greek ek cheiros anthrōpou adelphou, “from a human brother,” one. The Hebrew’s doubling is gone."),
   keeps("Greek ekzētēsō, “I will require,” is the verb of Luke 11:50–51."),
   between("Latin “from the hand of man, from the hand of a man and his brother” and King James “at the hand of man; at the hand of every man’s brother” keep the Hebrew’s two clauses."),
  ]},

 '9:6': {
  'received': "Whoever sheds human blood will have his own blood shed, because humankind is made in the image of God.",
  'explain': ("The principle becomes a formula: blood for blood, and the reason is the image of God. The Hebrew says by humans his blood "
   "shall be shed, naming the agent; the Greek says in return for his blood it shall be shed, an exchange without a stated agent; the "
   "Latin names neither. The Hebrew says he made humankind; the Greek I made, in God’s own voice. James makes the same point about cursing people."),
  'shared': ["Whoever sheds human blood will have his blood shed.", "The reason is the image of God.", "Humankind was made in that image."],
  'instructions': [ins(K, S, "Murder is answered with death because the victim bears God’s image."), ins(W, R, "The value of a human life is not in the person’s worth but in whose image they carry.")],
  'entries': ['creator'],
  'lost': [
   loses("Hebrew ba-adam damo yishafekh, “by humans his blood shall be shed,” names human agency. Greek anti tou haimatos autou ekchythēsetai, “in return for his blood it shall be shed,” is an exchange formula with no agent; the compressed Greek is syntactically awkward. Hebrew asah, “he made,” becomes Greek epoiēsa, “I made.”"),
   between("Latin “his blood shall be shed; for the human being was made in the image of God” drops the agent like the Greek but keeps “was made”; King James “by man shall his blood be shed … made he man” follows the Hebrew. James 3:9 and 1:27 are the reference points."),
  ]},

 '9:7': {
  'received': "Noah and his sons are told again to be fruitful, multiply and fill the earth.",
  'explain': ("The blessing of verse 1 returns to close the law of blood: after a word about death, a word about life. The Hebrew says "
   "swarm on the earth, the verb of the teeming creatures in 1:20; the Greek says fill the earth and multiply upon it; the Latin adds go "
   "forth upon the earth."),
  'shared': ["Be fruitful and multiply.", "Spread over the earth.", "Multiply upon it."],
  'instructions': [ins(C, S, "Be fruitful and multiply on the earth."), ins(W, R, "The command to multiply frames the law against killing; life is the purpose, and the law protects it.")],
  'entries': [],
  'lost': [
   loses("Hebrew shirtsu va-arets, “swarm on the earth,” the verb of 1:20, becomes Greek plērōsate tēn gēn, “fill the earth.” The teeming image is gone."),
   between("Latin “go forth upon the earth and fill it” and King James “bring forth abundantly in the earth” each take a different path; King James keeps the Hebrew swarm."),
  ]},

 '9:8': {
  'received': "God spoke to Noah and his sons.",
  'explain': ("A new speech begins, addressed to Noah and his sons together. The covenant promised in 6:18 is about to be made. All "
   "versions agree on speaker and hearers."),
  'shared': ["God spoke.", "He spoke to Noah.", "He spoke to Noah’s sons with him."],
  'instructions': [ins(K, S, "God addressed the covenant to Noah and his sons together.")],
  'entries': ['noah'],
  'lost': [between("Hebrew, Greek, Latin and King James agree.")]},

 '9:9': {
  'received': "God establishes his covenant with Noah and his descendants.",
  'explain': ("The first covenant in Scripture is made. “As for me, behold” marks God’s own initiative; the partners are Noah, his "
   "household and their offspring after them. The Hebrew says I am establishing; the Greek I establish; the Latin I will establish. "
   "The sense is the same."),
  'shared': ["God himself establishes the covenant.", "It is with Noah and his household.", "It extends to their offspring after them."],
  'instructions': [ins(K, S, "God’s covenant was made with Noah and all his descendants."), ins(W, R, "A covenant is God’s binding of himself; here he binds himself first and asks nothing in return.")],
  'entries': ['term-covenant', 'noah'],
  'lost': [between("Hebrew hineni meqim, “behold, I am establishing,” is Greek idou egō anistēmi, “behold, I establish”; Latin “I will establish.” Hebrew zera and Greek sperma are both “offspring,” King James “seed.”")]},

 '9:10': {
  'received': "The covenant includes every living creature that came out of the ark.",
  'explain': ("The covenant reaches past humankind to every living creature: birds, livestock and wild animals, all that left the ark. "
   "The Hebrew ends with a repetition, every wild animal of the earth, which the Greek does not have; the Latin and King James keep "
   "it. The animals are partners in God’s promise."),
  'shared': ["The covenant is with every living creature with Noah.", "Birds, livestock and wild animals are named.", "All that came out of the ark are included."],
  'instructions': [ins(K, S, "The covenant after the flood includes the animals."), ins(W, R, "God’s promises are wider than the human family; the creatures are remembered in them.")],
  'entries': ['term-covenant', 'noahs-ark'],
  'lost': [
   loses("Hebrew closes with le-khol chayyat ha-arets, “to every wild animal of the earth,” a second mention after the list; the Greek has no corresponding clause."),
   between("Latin “and all the wild animals of the earth” and King James “to every beast of the earth” keep the Hebrew repetition."),
  ]},

 '9:11': {
  'received': "Never again will all flesh be destroyed by a flood, nor the earth ruined by one.",
  'explain': ("The content of the covenant is a promise of restraint: no more flood to destroy all flesh or the earth. The Hebrew says all "
   "flesh will not be cut off; the Greek that it will not die, and adds water to the flood and all to the earth. Isaiah recalls this oath "
   "as the pattern of God’s steadfast kindness."),
  'shared': ["God establishes his covenant.", "All flesh will never again be destroyed by a flood.", "There will never again be a flood to destroy the earth."],
  'instructions': [ins(K, S, "God promised never to send another flood to destroy all life."), ins(W, R, "The promise does not say there will be no more judgement, only no more of this one; its comfort is specific.")],
  'entries': ['term-covenant'],
  'lost': [
   loses("Hebrew yikkaret, “be cut off,” becomes Greek apothaneitai, “die”; the Hebrew idiom of cutting off is gone. The Greek adds hydatos, “of water,” and pasan, “all,” to the earth."),
   between("Latin “be killed by floodwaters” and King James “be cut off … by the waters of a flood” divide between the two. Isaiah 54:9–10 recalls the oath."),
  ]},

 '9:12': {
  'received': "God announced the sign of the covenant between himself, Noah’s household and every living creature, for all generations.",
  'explain': ("A covenant needs a sign, and God announces one. The Hebrew says God said; the Greek the Lord God said to Noah, naming "
   "both more fully. The partners are God, the humans and every living creature, and the term is perpetual. Circumcision and the "
   "Sabbath will later be called signs of the covenant too."),
  'shared': ["God gives a sign of the covenant.", "It is between him, the humans and every living creature.", "It is for perpetual generations."],
  'instructions': [ins(K, S, "The covenant with Noah was given a visible sign for all generations."), ins(W, R, "God attaches signs to his promises so that they can be seen; faith is given something to look at.")],
  'entries': ['term-covenant', 'noah', 'lord-translation'],
  'lost': [
   keeps("An added pros Nōe, “to Noah,” and expands Elohim to kyrios ho theos, “the Lord God”; the Hebrew has “God said.”"),
   between("Latin and King James have “God said” with the Hebrew. Greek sēmeion tēs diathēkēs, “sign of the covenant,” is the phrase of 17:11 and Exodus 31:13."),
  ]},

 '9:13': {
  'received': "God sets his bow in the cloud as a sign of the covenant between him and the earth.",
  'explain': ("The sign is the rainbow. The word in Hebrew and Greek is the ordinary word for a warrior’s bow, and the verse has often been "
   "read as God hanging up his weapon in the sky. The Hebrew says I have set, a completed act; the Greek I set, present; the Latin I will "
   "place. The covenant partner here is the earth itself."),
  'shared': ["God sets his bow in the cloud.", "It is a sign of a covenant.", "The covenant is between God and the earth."],
  'instructions': [ins(K, S, "The rainbow is the sign of God’s covenant with the earth."), ins(W, R, "A weapon turned into a sign of peace; the bow in the cloud points away from the earth.")],
  'entries': ['term-covenant'],
  'lost': [between("Hebrew natatti, “I have set,” is Greek tithēmi, “I set,” and Latin ponam, “I will place.” Hebrew qeshet and Greek toxon are both the warrior’s bow of Habakkuk 3:9. King James “I do set” follows the present sense.")]},

 '9:14': {
  'received': "When God brings clouds over the earth, the bow will be seen in them.",
  'explain': ("The sign appears whenever the clouds come, the very clouds that once brought the flood. The Hebrew says the bow is seen; "
   "the Greek says my bow shall be seen; the Latin has God cover heaven with clouds. Ezekiel sees God’s glory like the bow in the cloud "
   "on a rainy day, and John sees a rainbow around the throne."),
  'shared': ["God brings clouds over the earth.", "The bow appears in the cloud.", "The sign is seen with the clouds."],
  'instructions': [ins(K, S, "The rainbow appears with the clouds as the covenant sign."), ins(W, R, "The sign of mercy is set where the threat used to come; clouds now carry the promise.")],
  'entries': [],
  'lost': [
   keeps("Greek to toxon mou, “my bow,” adds the possessive where the Hebrew has “the bow,” and makes the appearance a main clause rather than part of the “when.”"),
   between("Latin “when I cover heaven with clouds, My bow shall appear” has the possessive and its own image; King James “the bow shall be seen in the cloud” follows the Hebrew. Ezekiel 1:28 and Revelation 4:3 see the bow again."),
  ]},

 '9:15': {
  'received': "God will remember his covenant, and the waters will never again become a flood to destroy all flesh.",
  'explain': ("The bow is for God’s remembering, not only ours. When he sees it he remembers the covenant with every living creature, "
   "and the waters will not become a flood again. The Hebrew says every living creature of all flesh; the Greek among all flesh; the "
   "Latin every living soul that gives life to flesh. Zechariah praises God for remembering his holy covenant."),
  'shared': ["God will remember his covenant.", "It is with every living creature of all flesh.", "The waters will never again become a flood to destroy all flesh."],
  'instructions': [ins(K, S, "God binds himself to remember the covenant whenever the bow appears."), ins(W, R, "God sets himself a reminder; the promise is kept by his looking, not by our deserving.")],
  'entries': ['term-covenant'],
  'lost': [between("Hebrew be-khol-basar, “of all flesh,” is Greek en pasē sarki, “among all flesh”; Latin “every living soul that gives life to flesh” is its own phrasing; King James follows the Hebrew. Greek mnēsthēsomai, “I will remember,” is the verb of 8:1 and Luke 1:72.")]},

 '9:16': {
  'received': "The bow will be in the cloud, and God will see it and remember the everlasting covenant with every living creature.",
  'explain': ("The sign is described a third time, now as everlasting. The Hebrew says the bow, and between God and every living "
   "creature, speaking of God in the third person inside his own speech; the Greek says my bow and between me. Hebrews speaks of the "
   "blood of the everlasting covenant."),
  'shared': ["The bow will be in the cloud.", "God will see it and remember.", "The covenant is everlasting, with every living creature on the earth."],
  'instructions': [ins(K, S, "The covenant of the bow is everlasting."), ins(W, R, "An everlasting covenant with all living things means the creatures’ future is promised, not merely permitted.")],
  'entries': ['term-covenant'],
  'lost': [
   loses("Hebrew ha-qeshet, “the bow,” and ben Elohim, “between God,” keep the third person inside God’s speech. Greek to toxon mou, “my bow,” and ana meson emou, “between me,” make it first person throughout; the Greek does not say “between me, God.”"),
   between("Latin “the bow … between God” and King James “the bow … between God” keep the Hebrew. Greek diathēkē aiōnios, “everlasting covenant,” is the phrase of Hebrews 13:20 and 17:7."),
  ]},

 '9:17': {
  'received': "God told Noah that this is the sign of the covenant he has established with all flesh on the earth.",
  'explain': ("The speech ends by naming the sign once more, now addressed to Noah alone and extended to all flesh on the earth. The "
   "Hebrew says established; the Greek made. The covenant section closes as it opened, with God speaking to Noah."),
  'shared': ["God spoke to Noah.", "This is the sign of the covenant.", "The covenant is between God and all flesh on the earth."],
  'instructions': [ins(K, S, "The rainbow seals God’s covenant with all flesh on the earth.")],
  'entries': ['term-covenant', 'noah'],
  'lost': [between("Hebrew haqimoti, “I have established,” is Greek diethemēn, “I have made.” Latin “This shall be the sign” and King James “This is the token” are wording.")]},

 '9:18': {
  'received': "Noah’s sons who left the ark were Shem, Ham and Japheth, and Ham was the father of Canaan.",
  'explain': ("The story turns to the sons, and Canaan is named in advance, preparing for Noah’s words in verse 25 and for the land Israel "
   "will be given. All four versions agree exactly."),
  'shared': ["Noah’s sons came out of the ark.", "They were Shem, Ham and Japheth.", "Ham was the father of Canaan."],
  'instructions': [ins(K, S, "Ham, one of Noah’s three sons, was the father of Canaan.")],
  'entries': ['noah', 'canaan'],
  'lost': [between("Hebrew, Greek, Latin and King James agree in every word. Canaan returns at 9:25, 10:15 and 12:5.")]},

 '9:19': {
  'received': "From Noah’s three sons the whole earth was peopled.",
  'explain': ("The three sons are the fathers of all. The Hebrew says from these the whole earth was dispersed, using earth for its "
   "population; the Greek says from these they dispersed over all the earth; the Latin spells it out, the whole human race spread over "
   "all the earth. The table of nations in chapter 10 will give the detail."),
  'shared': ["These three were Noah’s sons.", "From them people spread.", "They spread over the whole earth."],
  'instructions': [ins(K, S, "All the peoples of the earth descend from Noah’s three sons."), ins(W, R, "One family is the root of every nation; Acts 17:26 draws the lesson that all are kin.")],
  'entries': ['noah'],
  'lost': [between("Hebrew naftsah kol-ha-arets, “the whole earth was dispersed,” is Greek diesparēsan epi pasan tēn gēn, “they dispersed over all the earth.” Latin “the whole human race spread” and King James “was the whole earth overspread” divide.")]},

 '9:20': {
  'received': "Noah began to farm the ground and planted a vineyard.",
  'explain': ("The first vineyard in Scripture is Noah’s. The Hebrew calls him a man of the ground and says he began and planted; the "
   "Greek says he began to be a farmer of the earth; the Latin a cultivator who began to work the ground. Isaiah will picture Israel as "
   "God’s vineyard, and Jesus will call himself the true vine."),
  'shared': ["Noah worked the ground.", "He began something new.", "He planted a vineyard."],
  'instructions': [ins(K, S, "Noah planted the first vineyard."), ins(W, R, "The gift of the vine comes before its misuse; what follows is not the vineyard’s fault.")],
  'entries': ['noah', 'grapevine'],
  'lost': [between("Hebrew va-yachel Noach ish ha-adamah, “Noah, a man of the ground, began,” is compressed; Greek ērxato Nōe anthrōpos geōrgos gēs, “Noah began to be a farmer of the earth,” makes farming the thing begun. Latin “a cultivator, began to work the ground” and King James “began to be an husbandman” follow the Greek construction. Isaiah 5:1–7 and John 15:1 take up the vine.")]},

 '9:21': {
  'received': "Noah drank the wine, became drunk, and lay uncovered in his tent.",
  'explain': ("The righteous man falls. He drinks, is drunk, and is exposed. The Hebrew says he uncovered himself inside his tent, an act "
   "of his own; the Greek says he was uncovered in his house, a state in a dwelling. The Latin and King James keep the tent. No version "
   "excuses him, and none adds to the account."),
  'shared': ["Noah drank some of the wine.", "He became drunk.", "He was uncovered in his dwelling."],
  'instructions': [ins(K, S, "Noah became drunk and was uncovered."), ins(W, R, "The one man found righteous is the first to be drunk; the flood did not wash the heart described in 8:21.")],
  'entries': ['noah'],
  'lost': [
   loses("Hebrew va-yitgal be-tokh oholoh, “he uncovered himself inside his tent,” is reflexive and names a tent. Greek egymnōthē en tō oikō autou, “he was uncovered in his house,” gives the state and a house. The Hebrew’s agency and the tent are gone."),
   between("Latin “lay uncovered in his tent” and King James “was uncovered within his tent” keep the tent but, like the Greek, the state rather than the act."),
  ]},

 '9:22': {
  'received': "Ham saw his father’s nakedness and told his two brothers outside.",
  'explain': ("Ham, named again as Canaan’s father, sees and tells. The Hebrew word for nakedness is the word of the laws on uncovering "
   "nakedness, and Ham’s wrong has been read as mockery or as something worse; the text says only seeing and telling. The Greek adds that "
   "he went out before telling his brothers, making the movement explicit."),
  'shared': ["Ham, the father of Canaan, saw his father’s nakedness.", "He told his two brothers.", "The brothers were outside."],
  'instructions': [ins(K, S, "Ham saw his father exposed and spoke of it to his brothers."), ins(W, R, "To look and then to tell is to make another’s shame a story; the brothers’ response shows the other way.")],
  'entries': ['canaan'],
  'lost': [
   keeps("An added kai exelthōn, “and going out,” before the telling; the Hebrew has Ham see and tell with the brothers already outside."),
   between("Latin “saw that his father’s private parts were uncovered” paraphrases; King James “saw the nakedness of his father” follows the Hebrew. Hebrew ervah is the word of Leviticus 18:6–7."),
  ]},

 '9:23': {
  'received': "Shem and Japheth covered their father with a garment, walking backward so as not to see his nakedness.",
  'explain': ("The two brothers act with care. They carry the garment between them, walk backward, cover their father, and keep their "
   "faces turned away. The Hebrew puts the garment on their shoulders; the Greek on their backs. The scene is told slowly so that the "
   "contrast with Ham is felt."),
  'shared': ["Shem and Japheth took the garment.", "They walked backward and covered their father’s nakedness.", "Their faces were turned away and they did not see."],
  'instructions': [ins(K, S, "Shem and Japheth covered their father without looking at him."), ins(W, R, "Honour covers what shame exposes; the brothers teach how to treat a parent’s failure.")],
  'entries': [],
  'lost': [between("Hebrew al-shekhem sheneihem, “on both their shoulders,” is Greek epi ta dyo nōta autōn, “on both their backs.” Latin “upon their shoulders” and King James “upon both their shoulders” keep the Hebrew; the Latin has them lay a cloak without “took.”")]},

 '9:24': {
  'received': "When Noah recovered from his wine he learned what his younger son had done.",
  'explain': ("Noah comes to himself and knows. The Hebrew says he awoke from his wine; the Greek that he sobered up. Ham is called the "
   "younger son although he is listed second; the phrase is read as the youngest of three, or as pointing to Canaan, Noah’s grandson. "
   "No version says what more, if anything, was done."),
  'shared': ["Noah recovered from his wine.", "He knew what had been done to him.", "The one who did it is called his younger son."],
  'instructions': [ins(K, S, "Noah learned of his son’s act when he awoke.")],
  'entries': ['noah'],
  'lost': [between("Hebrew va-yiqets Noach mi-yeino, “Noah awoke from his wine,” is Greek exenēpsen Nōe apo tou oinou, “Noah sobered up from the wine.” Latin and King James “awoke” follow the Hebrew. Hebrew ha-qatan and Greek ho neōteros both mean “the younger.”")]},

 '9:25': {
  'received': "Noah cursed Canaan to be the lowest of slaves to his brothers.",
  'explain': ("The curse falls, and it falls on Canaan, not on Ham and not on all his descendants. The Hebrew intensifies: a slave of "
   "slaves; the Greek has a concrete status, a household slave. The Latin and King James keep the Hebrew superlative. Joshua will later "
   "place the Gibeonites, a Canaanite people, under service."),
  'shared': ["Noah pronounced a curse.", "The curse names Canaan.", "Canaan is to be a slave to his brothers."],
  'instructions': [ins(K, S, "Noah’s curse named Canaan as a servant to his brothers."), ins(W, R, "The curse is specific to Canaan and to the story of the land; it has been misused when stretched to peoples it does not name.")],
  'entries': ['canaan'],
  'lost': [
   loses("Hebrew eved avadim, “a slave of slaves,” is a superlative of servitude. Greek pais oiketēs, “a household slave,” is a concrete social term; the Hebrew intensifier is gone."),
   between("Latin “slave of slaves” and King James “servant of servants” keep the Hebrew. Greek epikataratos Chanaan names Canaan as the Hebrew does. Joshua 9:23 is the later echo."),
  ]},

 '9:26': {
  'received': "Noah blessed the Lord, the God of Shem, and made Canaan his slave.",
  'explain': ("Noah blesses God rather than Shem himself: blessed be the Lord, the God of Shem. It is the first time God is named as a "
   "particular man’s God, as he will be the God of Abraham. The Hebrew has YHWH; the Greek the Lord. The Hebrew ends with a poetic "
   "suffix, to them; the Greek his. Zechariah’s song opens with the same Greek words."),
  'shared': ["Noah blesses the Lord.", "The Lord is called the God of Shem.", "Canaan is to be a slave to Shem."],
  'instructions': [ins(K, S, "The Lord is named the God of Shem."), ins(W, R, "The best thing said of Shem is said about his God; to be blessed is to have the Lord as one’s own.")],
  'entries': ['yhwh-yahweh', 'lord-translation', 'canaan'],
  'lost': [
   loses("Hebrew barukh YHWH Elohe Shem, “blessed be YHWH, the God of Shem,” names YHWH; Greek eulogētos kyrios ho theos tou Sēm has “the Lord.” Hebrew lamo, a poetic suffix read “to them,” is Greek autou, “his.”"),
   keeps("Eulogētos kyrios, “blessed be the Lord,” is the opening of Luke 1:68 and the shape of Ephesians 1:3."),
   between("Latin “let Canaan be his slave” and King James “Canaan shall be his servant” read the Hebrew suffix as singular, with the Greek."),
  ]},

 '9:27': {
  'received': "Noah asked God to enlarge Japheth and let him dwell in the tents of Shem, with Canaan as slave.",
  'explain': ("The blessing of Japheth is a Hebrew pun: yaft, enlarge, sounds like Yefet, Japheth. His descendants will spread over the "
   "coastlands in chapter 10. The Hebrew says the tents of Shem; the Greek the houses of Shem. Whose slave Canaan is divides the columns: "
   "the Hebrew and Greek say their, the Latin and King James his. Who dwells in Shem’s tents is left open in all."),
  'shared': ["May God enlarge Japheth.", "May he dwell in the dwellings of Shem.", "Canaan is to be a slave."],
  'instructions': [ins(K, S, "Japheth is blessed with enlargement and a place among Shem’s dwellings."), ins(W, R, "Japheth’s blessing is to live near Shem’s God; Christian readers have heard the nations gathered to Israel’s tents.")],
  'entries': ['canaan'],
  'lost': [
   loses("Hebrew yaft Elohim le-Yefet, “may God enlarge Japheth,” is a pun on the name that Greek platynai ho theos tō Iapheth cannot carry. Hebrew ohole Shem, “the tents of Shem,” becomes Greek tois oikois tou Sēm, “the houses of Shem.”"),
   between("Latin “tents of Shem … let Canaan be his slave” and King James “tents of Shem … Canaan shall be his servant” keep the tents and make Canaan the slave of one; Hebrew lamo and Greek autōn, “their,” make him the slave of both. 10:2–5 gives Japheth’s coastlands."),
  ]},

 '9:28': {
  'received': "Noah lived three hundred and fifty years after the flood.",
  'explain': ("The genealogical formula of chapter 5 resumes for Noah. He lives three hundred and fifty years after the flood, agreed in "
   "every version. By the Hebrew figures of chapter 11 Noah is still alive when Abram is born; by the Greek, some seven centuries "
   "separate Noah’s death from Abram’s birth."),
  'shared': ["Noah lived after the flood.", "He lived three hundred and fifty more years.", "His life is counted from the flood."],
  'instructions': [ins(K, S, "Noah lived three hundred and fifty years after the flood.")],
  'entries': ['noah'],
  'lost': [between("Hebrew, Greek, Latin and King James agree. Greek meta ton kataklysmon, “after the flood,” is the chapter’s point of reckoning; 11:10–26 carries the two chronologies on.")]},

 '9:29': {
  'received': "Noah lived nine hundred and fifty years in all, and he died.",
  'explain': ("The entry begun in 5:32 is closed with the words of chapter 5: all the days, a total, and he died. Nine hundred and fifty "
   "years, agreed in all versions. The man who was carried over the flood dies like Adam and Seth before him."),
  'shared': ["All the days of Noah are summed.", "They came to nine hundred and fifty years.", "He died."],
  'instructions': [ins(K, S, "Noah died at nine hundred and fifty."), ins(W, R, "Even the man saved through the flood dies; the ark was a rescue, not an escape from the sentence of 3:19.")],
  'entries': ['noah'],
  'lost': [between("Hebrew, Greek, Latin and King James agree, the King James after normalising spelling. The formula is that of 5:5.")]},
 }
}
