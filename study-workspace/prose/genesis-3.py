# Study prose for Genesis 3 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 3,
 'chapterNote': (
  "The story of the fall is the same in every column: the serpent’s question, the eating, the hiding, the three sentences "
  "and the expulsion. What varies is at the edges. The Hebrew keeps the name YHWH God, the sound-play between the naked pair "
  "and the crafty serpent, “he ate” at the end of verse 6, the striking of head and heel, the woman’s “desire,” the name Eve, "
  "and the guardians stationed east of the garden. The Greek keeps “gods” in the serpent’s promise, “they ate,” the plain "
  "statement that Adam was with her, “watching” for the enmity of 3:15, “groaning” and “turning” for the woman, “the only tree” "
  "twice, the name Life for Eve, and Adam settled opposite the garden. The Latin stands alone in verse 15 with “she shall crush "
  "your head,” and gives “garden of delight” for Eden throughout."),
 'verses': {

 '3:1': {
  'received': "The serpent, shrewdest of the creatures God had made, questioned the woman about God’s command.",
  'explain': ("The tempter enters as one of God’s creatures, not as a rival power. It is called shrewd or cunning, and that word "
   "describes skill, not goodness. Its first move is a question that bends the command: the Hebrew asks whether God really "
   "forbade any tree; the Greek asks why God said they must not eat from any tree; the Latin asks why God forbade every tree. The doubt is planted before the lie."),
  'shared': ["The serpent was the shrewdest of the animals God had made.", "It spoke to the woman.", "It questioned what God had said about eating from the trees."],
  'instructions': [ins(K, S, "The serpent was a creature God had made, and it questioned God’s word."), ins(W, R, "Temptation often begins by making God’s command sound narrower or harsher than it is.")],
  'entries': ['eden-serpent', 'eve', 'lord-translation'],
  'lost': [
   loses("Hebrew arum, “shrewd,” answers arummim, “naked,” in 2:25; Greek phronimōtatos cannot carry the echo. Hebrew “of the field” becomes Greek “upon the earth,” and the Hebrew question “did God really say” becomes a Greek “why did God say.”"),
   keeps("The Greek names the serpent again as speaker and sharpens the command into “by no means eat from any tree,” so the distortion is plainer in the Greek than in the Hebrew."),
   between("Latin “why has God commanded you not to eat from every tree” and King James “hath God said, Ye shall not eat of every tree” each shape the question differently. Revelation 12:9 identifies the ancient serpent with the devil; Genesis itself does not name him."),
  ]},

 '3:2': {
  'received': "The woman answered that they may eat the fruit of the trees of the garden.",
  'explain': ("The woman begins well. She knows the permission of 2:16 and states it: the fruit of the trees is theirs to eat. "
   "All four versions give the same reply, with only the Greek “paradise” and the Latin’s plain “we eat” as differences. "
   "The conversation that will end in disobedience starts from the truth."),
  'shared': ["The woman replied to the serpent.", "She affirmed that they may eat the fruit of the trees.", "The trees are those of the garden."],
  'instructions': [ins(K, S, "The permission to eat from the trees of the garden was known to the woman."), ins(W, R, "Knowing what God allows is the first defence against being told what he forbids.")],
  'entries': ['eve', 'eden'],
  'lost': [
   between("Hebrew gan, “garden,” is Greek paradeisos, “paradise,” as throughout. The Greek names the serpent as the one addressed and says “we may eat”; the Latin has simply “we eat.” The collective “fruit of the trees” is natural in both."),
  ]},

 '3:3': {
  'received': "She reported that God forbade eating or touching the fruit of the tree in the middle of the garden, lest they die.",
  'explain': ("The woman’s report adds something. God forbade eating; she says eating and touching. The command of 2:17 was "
   "addressed in the singular in Hebrew; here it is plural, as in the Greek of 2:17. The Hebrew “lest you die” and the Greek "
   "“so that you do not die” express the same warning. Whether the addition of touching is caution or exaggeration the text does not say."),
  'shared': ["God forbade the fruit of the tree in the middle of the garden.", "The woman says they may not eat or touch it.", "The reason given is death."],
  'instructions': [ins(K, S, "The woman knew the prohibition and the penalty."), ins(W, R, "Adding to God’s command is a step away from it, however pious the addition sounds.")],
  'entries': ['eve', 'eden'],
  'lost': [
   between("Hebrew pen-temutun, “lest you die,” and Greek hina mē apothanēte, “so that you do not die,” are the same warning in two grammatical shapes. Both columns include touching. Latin gives the command as reported speech, “God commanded us”; King James keeps direct speech."),
  ]},

 '3:4': {
  'received': "The serpent flatly denied that they would die.",
  'explain': ("The lie is direct. God said “you shall surely die”; the serpent says “you shall certainly not die,” taking "
   "God’s emphatic form and negating it. Every version has the same words. It is the serpent’s claim, and the narrator does "
   "not endorse it. Jesus later calls the devil a liar from the beginning."),
  'shared': ["The serpent spoke to the woman.", "It denied that they would die.", "The denial is emphatic."],
  'instructions': [ins(K, S, "The serpent denied God’s warning of death."), ins(W, R, "A confident denial of consequences is the oldest lie.")],
  'entries': ['eden-serpent'],
  'lost': [
   keeps("Hebrew lo-mot temutun and Greek ou thanatō apothaneisthe both echo and negate the doubled form of 2:17: not “by death shall you die.” The Greek keeps the Hebrew idiom exactly."),
   between("Latin and King James give the same denial; King James “Ye shall not surely die” keeps the old plural “ye.” John 8:44 calls the devil a liar from the beginning."),
  ]},

 '3:5': {
  'received': "The serpent claimed that eating would open their eyes and make them like God, knowing good and evil.",
  'explain': ("The serpent reinterprets the prohibition as God’s jealousy: God knows that eating would make them godlike. "
   "The Hebrew word can mean “like God” or “like divine beings”; the Greek, Latin and King James choose the plural “gods.” "
   "The promise of open eyes will come true in a bitter way in verse 7. This is still the serpent speaking, not the narrator."),
  'shared': ["The serpent says God knows what the fruit does.", "Eating will open their eyes.", "They will be like God, or gods, knowing good and evil."],
  'instructions': [ins(K, S, "The serpent promised godlike knowledge from the forbidden fruit."), ins(W, R, "The desire to be like God by taking rather than receiving is the shape of the first sin.")],
  'entries': ['eden-serpent', 'elohim', 'gods'],
  'lost': [
   loses("Hebrew ke-elohim can be read as “like God” or “like divine beings”; the Hebrew column reads “like God.” Greek theoi is unambiguously plural, “gods.” The Hebrew ambiguity is gone in the Greek."),
   between("Latin dii and King James “gods” follow the plural with the Greek. Latin “God knows” keeps the Hebrew present where the Greek has “God knew.” Elohim is the same word used of God throughout chapter 1."),
  ]},

 '3:6': {
  'received': "The woman saw the tree as good, desirable and attractive, ate from it, and gave to her husband, who ate too.",
  'explain': ("Three attractions are named: good for food, pleasing to the eye, and a third that the versions divide over. "
   "The Hebrew says the tree was desirable for gaining wisdom; the Greek says beautiful to contemplate. Then the eating, and "
   "the sharing. The Greek says Adam was “with her” and that “they ate”; the Hebrew ends with “he ate.” John’s triad of flesh, eyes and pride is often set beside this verse."),
  'shared': ["The woman saw the tree as good for food and pleasing to the eyes.", "She took its fruit and ate.", "She gave to her husband and he ate as well."],
  'instructions': [ins(K, S, "Both the woman and the man ate from the forbidden tree."), ins(W, R, "Sin travels by sharing; what one takes, another is offered.")],
  'entries': ['eve', 'adam'],
  'lost': [
   loses("Hebrew nechmad le-haskil, “desirable for gaining wisdom,” becomes Greek hōraion tou katanoēsai, “beautiful to contemplate.” The Hebrew looks to understanding; the Greek to looking. The two senses overlap, so this is a shift of emphasis rather than a contradiction."),
   keeps("Greek met’ autēs, “with her,” places the man beside the woman at the temptation, and ephagon, “they ate,” closes the verse with both. The Hebrew ends “and he ate.” Paul’s “Adam was not deceived, but the woman” (1 Timothy 2:14) reads the scene from the Hebrew side."),
   between("Latin “delightful to look upon” sides with the Greek on the third attraction but has “who ate” with the Hebrew; King James “to be desired to make one wise” keeps the Hebrew."),
  ]},

 '3:7': {
  'received': "Their eyes were opened, they knew they were naked, and they made coverings of fig leaves.",
  'explain': ("The serpent’s promise comes true and turns to shame. Eyes are opened, and what they see is their own "
   "nakedness, which in 2:25 caused no shame. Their first act of knowledge is to hide their bodies. Luke uses the same "
   "Greek words for the opening of the disciples’ eyes at Emmaus, where sight leads to joy instead."),
  'shared': ["The eyes of both were opened.", "They knew that they were naked.", "They sewed fig leaves into coverings."],
  'instructions': [ins(K, S, "The first result of the disobedience was shame at their nakedness."), ins(W, R, "Knowledge gained by disobedience shows us ourselves before it shows us anything else.")],
  'entries': ['adam', 'eve'],
  'lost': [
   keeps("Greek diēnoichthēsan hoi ophthalmoi, “the eyes were opened,” is the phrase Luke uses at Emmaus (Luke 24:31). Greek perizōmata, like Hebrew chagorot, means coverings worn around the body, not full garments."),
   between("Hebrew and Greek agree throughout; Latin “coverings” and King James “aprons” are English wording only."),
  ]},

 '3:8': {
  'received': "Hearing the Lord God walking in the garden, the man and his wife hid among the trees.",
  'explain': ("God comes as he evidently used to, walking in the garden, and for the first time the humans hide. The Hebrew "
   "sets the time as “the breeze of the day”; the Greek says “toward evening,” and the Latin “the afternoon breeze,” all "
   "pointing to the cool late afternoon. God walking among his people becomes a covenant promise in Leviticus, which Paul applies to the church."),
  'shared': ["They heard the sound of the Lord God walking in the garden.", "It was in the cool of the day.", "The man and his wife hid among the trees."],
  'instructions': [ins(K, S, "After sinning, the man and the woman hid from God."), ins(W, R, "Guilt hides from the presence it once enjoyed; the hiding, not God’s coming, is what is new.")],
  'entries': ['adam', 'eve', 'lord-translation', 'eden'],
  'lost': [
   loses("Hebrew le-ruach ha-yom, “at the breeze of the day,” is an image; Greek to deilinon, “toward evening,” names the time directly. The Hebrew “the human” is Adam in the Greek. Hebrew “sound” and King James “voice” are both possible for qol."),
   keeps("Greek peripatountos, “walking,” is the verb of Leviticus 26:12, “I will walk among you,” which Paul quotes in 2 Corinthians 6:16."),
   between("Latin “afternoon breeze” keeps both the breeze and the hour; King James “cool of the day” interprets the breeze. The Greek singular “tree” is collective and does not put them inside one tree."),
  ]},

 '3:9': {
  'received': "The Lord God called to the man and asked where he was.",
  'explain': ("God’s first question in Scripture is two words in Greek: where are you? It is not a request for information "
   "but a summons to come out. The Hebrew asks it of “the human” without a name; the Greek, Latin and King James say Adam, "
   "and the Greek puts the name into the question itself. God asks Cain a matching question in the next chapter."),
  'shared': ["The Lord God called to the man.", "He asked where the man was.", "God sought the one who was hiding."],
  'instructions': [ins(K, S, "God sought out the man after his sin."), ins(W, R, "God’s question invites confession; it is the beginning of being found.")],
  'entries': ['adam', 'lord-translation'],
  'lost': [
   loses("Hebrew YHWH God calls “the human”; the Greek has the Lord God call Adam and adds the name inside the question, “Adam, where are you?” The Hebrew question is bare."),
   between("Latin and King James name Adam in the narration but not in the question, standing between the Hebrew and the Greek. Luke 19:10 gives the answer to the search: the Son of Man came to seek and to save what was lost."),
  ]},

 '3:10': {
  'received': "The man said he heard God in the garden and hid because he was afraid of his nakedness.",
  'explain': ("The man answers with the first confession of fear in the Bible. He heard, he was afraid, he was naked, he "
   "hid. He does not yet mention the tree. The Greek adds that he heard God “walking,” carrying over the detail of verse 8. "
   "John will write that perfect love casts out fear; here fear has just arrived."),
  'shared': ["The man heard the sound of God in the garden.", "He was afraid because he was naked.", "He hid."],
  'instructions': [ins(K, S, "Fear of God’s presence followed the first sin."), ins(W, R, "Fear names the symptom and not the cause; the man speaks of nakedness, not disobedience.")],
  'entries': ['adam'],
  'lost': [
   keeps("“To Him” and “as You walked in paradise” are added, so Adam’s report repeats the narrator’s description. The participle describes God walking; it does not make the sound walk on its own."),
   between("Hebrew qol, “sound,” is rendered “voice” in Latin and King James; the Hebrew, Latin and King James all say simply “in the garden.” Hebrews 2:15 speaks of those held all their lives by the fear of death."),
  ]},

 '3:11': {
  'received': "God asked who told him he was naked and whether he had eaten from the forbidden tree.",
  'explain': ("God’s second question goes to the cause. The knowledge of nakedness must have come from somewhere, and the "
   "only source is the one tree. The Greek adds that it was “the only one” forbidden, underlining how wide the permission "
   "had been. The Latin turns the two questions into one, “unless you have eaten,” which the Greek-English does not do."),
  'shared': ["God asked who told the man he was naked.", "God asked whether he had eaten from the forbidden tree.", "The questioning moves from the symptom to the act."],
  'instructions': [ins(K, S, "God traced the man’s shame to his eating from the forbidden tree."), ins(W, R, "God’s questions lead from what we feel to what we did.")],
  'entries': ['adam'],
  'lost': [
   keeps("Greek hou monou, “the only one,” is added to the tree: the one tree from which eating was forbidden. The Hebrew says only “the tree from which I commanded you not to eat.” The Greek also adds “to him.”"),
   between("Latin “unless you have eaten” joins the two questions into a single inference; Hebrew, Greek and King James keep two questions."),
  ]},

 '3:12': {
  'received': "The man blamed the woman God had given him for giving him the fruit, and admitted eating it.",
  'explain': ("The man confesses in the last word, “I ate,” but spends the sentence shifting blame: to the woman, and, through "
   "“whom You gave,” toward God himself. The versions agree; only the name differs, Adam in Greek, Latin and King James, "
   "“the human” in the Hebrew. The Latin calls the woman his companion."),
  'shared': ["The man answered God.", "He said the woman God gave him had given him the fruit.", "He admitted that he ate."],
  'instructions': [ins(K, S, "The man admitted eating but blamed the woman and, indirectly, God."), ins(W, R, "Confession that ends in “I ate” but begins with blame is only half a confession.")],
  'entries': ['adam', 'eve'],
  'lost': [
   between("Hebrew “the human” is Adam in Greek, Latin and King James; the explanation itself is the same in all four. Latin “as a companion” renders the Hebrew and Greek “to be with me.”"),
  ]},

 '3:13': {
  'received': "The Lord God questioned the woman, who said the serpent deceived her and she ate.",
  'explain': ("The woman’s answer mirrors the man’s: a cause named, then “I ate.” Her cause is deception by the serpent. "
   "The versions agree completely apart from the shape of God’s question, “what is this you have done” or, in the Latin, "
   "“why have you done this.” Paul twice recalls the serpent’s deceiving of Eve as a warning to the church."),
  'shared': ["The Lord God questioned the woman.", "She said the serpent deceived her.", "She admitted that she ate."],
  'instructions': [ins(K, S, "The woman admitted eating and named the serpent’s deception."), ins(W, R, "Being deceived explains a sin without excusing it; she still says “I ate.”")],
  'entries': ['eve', 'eden-serpent', 'lord-translation'],
  'lost': [
   keeps("Greek ēpatēsen, “deceived,” is the verb Paul uses of the serpent and Eve in 2 Corinthians 11:3 and 1 Timothy 2:14. Hebrew and Greek agree throughout the verse."),
   between("Latin “why have you done this” and King James “beguiled” are wording only; the question and the appeal to deception stand in all four."),
  ]},

 '3:14': {
  'received': "The Lord God cursed the serpent above all animals, to crawl on its belly and eat dust all its life.",
  'explain': ("Judgement begins with the serpent, and the first curse in Scripture falls on it, not on the man or the woman. "
   "The Hebrew has it go on its belly and eat dust; the Greek adds the chest and says earth. The curse sets the serpent "
   "below all other creatures. Paul will say that Christ became a curse for us."),
  'shared': ["The Lord God pronounced a curse on the serpent.", "It is cursed above all livestock and wild animals.", "It will go on its belly and eat dust all its life."],
  'instructions': [ins(K, S, "The serpent was cursed above all creatures for what it had done."), ins(W, R, "Judgement answers the tempter first; the one who leads into sin is not spared.")],
  'entries': ['eden-serpent', 'lord-translation'],
  'lost': [
   loses("Hebrew gechonekha, “your belly,” becomes Greek “your chest and belly,” and Hebrew afar, “dust,” becomes gē, “earth.” Hebrew “of the field” becomes “of the earth.”"),
   keeps("Greek epikataratos, “cursed,” opens the sequence of curses that falls on the serpent and then on the ground (3:17), never directly on the man or woman; Galatians 3:13 uses the same word of Christ."),
   between("Latin “upon your breast” follows the Greek chest; King James “upon thy belly” and “dust” follow the Hebrew."),
  ]},

 '3:15': {
  'received': "God set lasting enmity between the serpent and the woman and between their offspring, each striking at the other.",
  'explain': ("The sentence on the serpent becomes a promise. God himself puts hostility between the serpent’s offspring and "
   "the woman’s, aimed at head and heel. The versions differ sharply in the last clause. The Hebrew has striking or bruising "
   "of head and heel; the Greek has “watching,” hostile vigilance; the Latin alone has “she shall crush your head.” The Greek pronoun is masculine, “he.” Christian reading has long heard a first promise of victory here."),
  'shared': ["God puts enmity between the serpent and the woman.", "The enmity extends to their offspring.", "Head and heel are the points of the conflict."],
  'instructions': [ins(K, S, "God himself placed enmity between the serpent and the woman’s offspring."), ins(W, R, "Hostility to the tempter is God’s gift, not a failure of peace.")],
  'entries': ['eden-serpent', 'eve'],
  'lost': [
   loses("Hebrew shuf, “strike” or “bruise,” governs both clauses: he will strike your head, you will strike his heel. Greek tērēsei, “will watch,” replaces it with hostile watching, and the striking is gone from the Greek verse."),
   keeps("Greek autos, “he,” is masculine although the offspring noun sperma is neuter; the Greek reader is pointed to a single male descendant. The pronoun alone does not name him."),
   between("Latin ipsa conteret, “she shall crush,” makes the woman the agent and changes the verb; King James “it shall bruise” keeps the Hebrew action with a neuter pronoun. Romans 16:20 promises Satan crushed underfoot; Revelation 12:17 continues the serpent’s war with the woman’s offspring."),
  ]},

 '3:16': {
  'received': "To the woman God announced pain in childbearing, longing toward her husband, and his rule over her.",
  'explain': ("The sentence on the woman touches the two closest things: bearing children and her bond with her husband. All "
   "versions keep painful childbirth and the husband’s rule. The Hebrew multiplies her pain and her pregnancy, and speaks "
   "of her desire turned toward her husband; the Greek has groaning instead of pregnancy and “turning” instead of desire. Neither English word is a full account of marriage."),
  'shared': ["The woman’s pain is multiplied.", "In pain she will bear children.", "Her husband will rule over her."],
  'instructions': [ins(K, S, "Pain in childbearing and the husband’s rule follow the fall."), ins(W, R, "The sentence describes a broken world; it is a judgement to be read, not a design to be admired.")],
  'entries': ['eve'],
  'lost': [
   loses("Hebrew heronekh, “your pregnancy,” becomes Greek stenagmon, “your groaning.” Hebrew teshuqah, “desire,” becomes apostrophē, “turning” or recourse. The Hebrew words for pregnancy and desire are not in the Greek."),
   keeps("Greek stenagmos is the word Paul uses when the whole creation groans in travail (Romans 8:22). The Greek lets the woman’s sentence sound with that later groaning."),
   between("Latin “hardships and pregnancies” and “under your husband’s power” take their own path; King James “sorrow and conception” and “thy desire” follow the Hebrew. John 16:21 and 1 Timothy 2:15 return to childbirth."),
  ]},

 '3:17': {
  'received': "To the man God said that because he listened to his wife and ate, the ground is cursed and he will eat from it in pain all his life.",
  'explain': ("The man’s sentence falls on the ground, not on him directly. Because he listened to his wife rather than to "
   "God, the soil becomes hard, and food will come with pain. The Hebrew says the ground is cursed “because of you”; the "
   "Greek says “in your works,” tying the curse to his labour. The Greek again calls it “the only tree” forbidden."),
  'shared': ["The man listened to his wife and ate from the forbidden tree.", "The ground is cursed as a result.", "He will eat from it in pain all his life."],
  'instructions': [ins(K, S, "The ground was cursed because of the man’s disobedience."), ins(W, R, "Listening to a loved voice over God’s command is still disobedience, and its cost spreads beyond the one who chose it.")],
  'entries': ['adam'],
  'lost': [
   loses("Hebrew ba‘avurekha, “because of you,” becomes Greek en tois ergois sou, “in your works.” The Hebrew makes the man the cause; the Greek names the sphere of his labour. The Hebrew quotes the command, “You shall not eat from it”; the Greek says “the only one” forbidden."),
   between("Latin “in your work” sits closer to the Greek; King James “for thy sake” follows the Hebrew. Both Latin “toil” and King James “sorrow” render the pain."),
  ]},

 '3:18': {
  'received': "The ground will yield thorns and thistles, and the man will eat the plants of the field.",
  'explain': ("The cursed ground answers labour with weeds. Thorns and thistles are the sign of resistant soil, and the man’s "
   "food is now the plants of the field, no longer the fruit of the garden. All versions agree. Hebrews uses the same pair "
   "of words for barren ground near to a curse, and Jesus is crowned with thorns."),
  'shared': ["The ground will bring forth thorns and thistles.", "The man will eat the plants of the field.", "Food now comes from resistant soil."],
  'instructions': [ins(K, S, "After the fall the ground resists and food comes from the field."), ins(W, R, "Work that meets resistance is the common lot; it is not a sign of God’s absence.")],
  'entries': ['adam'],
  'lost': [
   keeps("Greek akanthas kai tribolous, “thorns and thistles,” is the pair Hebrews 6:8 uses for land that is near to being cursed; Matthew 27:29 crowns Jesus with the first of them. Hebrew and Greek agree in sense."),
   between("Latin “plants of the earth” and Greek “plants of the field” differ only in the noun; King James “herb of the field” follows the Hebrew."),
  ]},

 '3:19': {
  'received': "By the sweat of his face the man will eat bread until he returns to the ground he was taken from, for he is dust.",
  'explain': ("The sentence ends in death. Labour will be sweat, and the end of labour is a return to the ground of 2:7. "
   "The Hebrew distinguishes the ground he returns to from the dust he is made of; the Greek says earth throughout and "
   "has him “depart” into it. Luke uses the Greek word for sweat of Jesus in Gethsemane."),
  'shared': ["The man will eat bread by the sweat of his face.", "He will return to the ground from which he was taken.", "He is dust and will return to dust."],
  'instructions': [ins(K, S, "Death, a return to the dust, is part of the sentence on the man."), ins(W, R, "Remember that you are dust; it is a truth to live by, not only a sentence to fear.")],
  'entries': ['adam'],
  'lost': [
   loses("Hebrew adamah, “ground,” and afar, “dust,” are two words; Greek gē, “earth,” stands for both, and the link between adam and adamah is again lost. Hebrew tashuv, “you shall return,” becomes Greek apeleusē, “you shall depart.” The Greek adds “your” to bread."),
   keeps("Greek hidrōs, “sweat,” is the word of Luke 22:44, where Jesus’ sweat falls like drops of blood."),
   between("Latin “you are dust, and to dust you shall return” and King James “dust thou art” keep the Hebrew dust; the Latin has “earth” for the ground."),
  ]},

 '3:20': {
  'received': "The man named his wife Eve, because she was the mother of all the living.",
  'explain': ("After judgement comes a name full of hope. The Hebrew name Chawwah sounds like the word for living, and the "
   "explanation says why: she is the mother of all who live. The Greek translates the name instead of spelling it, calling "
   "her Zōē, Life, so the Greek reader hears the meaning directly. Paul draws from the one ancestry of all people."),
  'shared': ["The man named his wife.", "Her name is explained by life.", "She is the mother of all the living."],
  'instructions': [ins(K, S, "Eve is named as the mother of all the living."), ins(W, R, "Even under the sentence of death the next word is life; the human story goes on through her.")],
  'entries': ['eve', 'adam'],
  'lost': [
   loses("Hebrew Chawwah is a name with an echo of chayah, “to live.” Greek Zōē, “Life,” translates the name outright, so the Greek has no name Eve in this verse, only its meaning. The Hebrew “the human” is Adam in the Greek."),
   keeps("The Greek reader hears the explanation inside the name: Life, mother of all the living. Acts 17:26 and 1 Corinthians 15:22 build on the one descent of all people."),
   between("Latin Heva and King James Eve keep the name with the Hebrew."),
  ]},

 '3:21': {
  'received': "The Lord God made garments of skin for the man and his wife and clothed them.",
  'explain': ("Before sending them out, God clothes them. Their own fig leaves are replaced by tunics of skin that God himself "
   "makes. All four versions say the same. It is an act of care inside the judgement, and the first clothing in Scripture "
   "comes from God’s hand."),
  'shared': ["The Lord God made tunics of skin.", "They were for the man and his wife.", "God clothed them."],
  'instructions': [ins(K, S, "God clothed the man and the woman before they left the garden."), ins(W, R, "God provides for those he judges; care and judgement are not opposites.")],
  'entries': ['adam', 'eve', 'lord-translation'],
  'lost': [
   between("Hebrew, Greek, Latin and King James agree: tunics or coats of skin, made by the Lord God, and the pair clothed. The Hebrew here uses the name Adam as the Greek does."),
  ]},

 '3:22': {
  'received': "God said the man had become like one of us, knowing good and evil, and must not also take from the tree of life.",
  'explain': ("God speaks in the plural again, as in 1:26. The man has gained the knowledge the serpent promised, and now the "
   "tree of life must be kept from him, lest he live forever in his fallen state. The sentence breaks off unfinished; the "
   "action of the next verse completes it. The Hebrew says “also take,” the Greek “take”; the Greek names Adam and has God without Lord."),
  'shared': ["God says the man has become like one of us, knowing good and evil.", "The tree of life must be kept from him.", "Eating from it would mean living forever."],
  'instructions': [ins(K, S, "Humanity gained the knowledge of good and evil and lost access to the tree of life."), ins(W, R, "Endless life in a fallen state would be no mercy; the barring of the tree is a protection as well as a loss.")],
  'entries': ['adam', 'god-theos', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew YHWH God is “God” in the Greek, and “the human” is Adam. Hebrew gam, “also,” before the taking is absent from the Greek."),
   keeps("Greek heis ex hēmōn, “one of us,” keeps the plural of 1:26 and 11:7. Early Christians read the plural of the Father with the Son and Spirit; others read God addressing the heavenly court. The Greek adds nothing to decide it."),
   between("Latin “He said” drops both names; King James keeps “the LORD God” and “also.”"),
  ]},

 '3:23': {
  'received': "The Lord God sent the man out of the garden to work the ground he was taken from.",
  'explain': ("The expulsion is stated plainly, and the man’s work is redirected from the garden to the ground of his own "
   "making. The Hebrew says the garden of Eden; the Greek and Latin translate Eden as “delight,” the paradise or garden of "
   "delight. The task, to work the ground, is the same in all four."),
  'shared': ["The Lord God sent the man out of the garden.", "He was to work the ground.", "It was the ground from which he had been taken."],
  'instructions': [ins(K, S, "The man was sent out of the garden to work the ground."), ins(W, R, "Work outside the garden is still the work given in it; the task survives the loss of the place.")],
  'entries': ['eden', 'adam', 'lord-translation'],
  'lost': [
   loses("Hebrew gan-Eden, “the garden of Eden,” becomes Greek paradeisos tēs tryphēs, “the paradise of delight.” The Greek translates the name it spelled at 2:8, so Eden is no longer a place name here."),
   between("Latin “garden of delight” translates as the Greek does; King James “garden of Eden” keeps the Hebrew name. The sending-out and the task agree in all."),
  ]},

 '3:24': {
  'received': "God drove the man out and set the cherubim with a flaming sword to guard the way to the tree of life.",
  'explain': ("The chapter closes with guardians. Cherubim and a turning, flaming sword keep the way to the tree of life. The "
   "Hebrew stations the guardians east of the garden; the Greek first settles Adam opposite the garden, then stations them. "
   "The verb for guarding is the one given to the man in 2:15: what he was to keep, the cherubim now keep from him. Gold cherubim will later spread their wings over the ark."),
  'shared': ["God drove the man out.", "Cherubim and a flaming turning sword were stationed.", "They guard the way to the tree of life."],
  'instructions': [ins(K, S, "The way to the tree of life was barred by cherubim and a flaming sword."), ins(W, R, "The way to life is guarded, not destroyed; the tree still stands for a return in Revelation 22.")],
  'entries': ['cherubim', 'adam', 'eden'],
  'lost': [
   loses("Hebrew va-yashken, “he stationed,” has the cherubim as its object, placed “east of the garden of Eden.” Greek katōkisen auton, “settled him,” makes Adam the object, placed opposite the paradise of delight; then the cherubim are stationed separately. The Hebrew’s “east” is gone."),
   keeps("Greek phylassein, “to guard,” is the verb of 2:15; the Greek lets the man’s lost task and the cherubim’s new one sound alike. Cheroubin are the winged guardians of Exodus 25:18–22 and Hebrews 9:5."),
   between("Latin “before the garden of delight” and King James “at the east of the garden of Eden” each take part of the picture; neither has Adam settled opposite the garden."),
  ]},
 }
}
