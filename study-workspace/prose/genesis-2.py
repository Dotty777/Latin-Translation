# Study prose for Genesis 2 — Saints Parallel Reader Study Workspace. Draft for review.
# Grounded in the site's Hebrew–Greek, Latin–Greek and King James–Greek studies for each verse.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 2,
 'chapterNote': (
  "The chapter turns from the week of creation to the garden. What varies is the frame around the story. "
  "The Hebrew keeps the name YHWH God through most of the chapter, the seventh day as the day of completion, "
  "the breath in the nostrils, the human settled in the garden with an overtone of rest, and the sound-plays of "
  "woman and man, naked and crafty. The Greek keeps the sixth day for completion, a “book of origin,” a paradise, "
  "“let us make” for the helper, a plural prohibition, “the two” who become one flesh, and the name Adam from "
  "verse 16. The Latin and King James mostly follow the Hebrew frame; the Latin alone reads “garden of delight” "
  "for Eden and “from the beginning” for the east."),
 'verses': {

 '2:1': {
  'received': "Heaven and earth were finished, together with everything that fills and orders them.",
  'explain': ("The sentence closes the six days. Nothing is left half-made: the sky, the land and all that belongs to them are "
   "complete. The Hebrew pictures that fullness as a host, an ordered company like the stars; the Greek pictures it as "
   "order and adornment, the word that later means the world itself. Either way the point is the same: creation is whole."),
  'shared': ["Heaven and earth were completed.", "Everything belonging to them was completed with them.", "The work of the six days is finished before the seventh is described."],
  'instructions': [ins(K, S, "God brought the whole of heaven and earth to completion."), ins(W, R, "A finished work can be rested from; completion comes before rest.")],
  'entries': ['creator'],
  'lost': [
   loses("Hebrew tseva’am, “their host,” is the word for an army or an ordered company, often used of the stars. The Greek kosmos, “order” or “adornment,” drops the military picture. King James “host” keeps it; Latin ornatus follows the Greek side."),
   keeps("Kosmos is the root of “cosmos,” and the same Greek word renders the host of heaven again in Deuteronomy 4:19. The Greek reader hears the created order as a single adorned whole."),
   between("The two images describe the same completed creation; neither adds or removes a creature."),
  ]},

 '2:2': {
  'received': "God completed his work and on the seventh day ceased from all of it.",
  'explain': ("Every version agrees that God stopped on the seventh day. They differ on the day of completion. The Hebrew, Latin and "
   "King James say the work was completed on the seventh day; the Greek says the sixth. Readers have long explained how "
   "completion and rest can belong to one day, and the Greek wording removes the need for that explanation."),
  'shared': ["God completed the work he had made.", "On the seventh day he ceased from all of it.", "Rest follows a finished work."],
  'instructions': [ins(K, S, "God ceased from his work on the seventh day."), ins(W, R, "Ceasing from work is part of the pattern God set, not a failure to keep going.")],
  'entries': ['creator'],
  'lost': [
   loses("Hebrew ha-shevi‘i, “the seventh,” dates the completion to the seventh day. Greek hektē, “sixth,” moves it to the sixth. Latin and King James stay with the Hebrew. This is a real numerical difference, not a shade of wording."),
   keeps("Hektē makes the week tidy: completion on the sixth day, cessation on the seventh. A rabbinic tradition (Megillah 9a) remembers a sixth-day wording among the translators, so the reading is old, though its origin is not settled."),
   between("Hebrew shavat is “ceased”; Latin requievit and King James “rested” add the sense of repose. The Saints English keeps “ceased.”"),
  ]},

 '2:3': {
  'received': "God blessed the seventh day and made it holy, because on it he ceased from his work.",
  'explain': ("The seventh day is the first thing in the Bible to be called holy. All four versions agree on the blessing and the "
   "sanctifying, and on the reason: God ceased. They part over how the preceding work is described. The Hebrew has the hard "
   "phrase “created to make”; the Greek says the work God “had begun to make.” The holiness of the day is not in dispute."),
  'shared': ["God blessed the seventh day.", "God made the seventh day holy.", "The reason is that on it he ceased from his work."],
  'instructions': [ins(K, S, "The seventh day is blessed and holy because God ceased from his work on it."), ins(W, R, "Holiness is first attached to time, not to a place or an object.")],
  'entries': ['creator'],
  'lost': [
   loses("Hebrew bara, “created,” stands in the closing clause: work “that God created to make.” Greek ērxato, “began,” replaces it: work “that God had begun to make.” The Hebrew verb of creation is gone from the Greek verse."),
   keeps("Ērxato, “began,” smooths a difficult Hebrew construction and ties the work back to its beginning in 1:1. Whether this is the translator’s rephrasing or a different Hebrew source cannot be decided from the wording."),
   between("Latin “created to be made” and King James “created and made” each find their own way through the Hebrew phrase; Latin has “work” in the singular where the Greek has “works.”"),
  ]},

 '2:4': {
  'received': "This is the account of the origin of heaven and earth, from the day God made them.",
  'explain': ("A heading stands between the week and the garden. The Hebrew calls what follows the “generations” of heaven and "
   "earth; the Greek calls it a “book of origin,” the phrase Matthew later uses to open his Gospel. The Hebrew also names "
   "YHWH God here for the first time, while the Greek has only God. The verse looks back to the finished world and forward to the story of the man."),
  'shared': ["What follows is an account of the origin of heaven and earth.", "It is dated to the day God made them.", "The creation already told is the starting point of the new story."],
  'instructions': [ins(K, S, "The story of the garden belongs to the same creation as the six days."), ins(W, R, "Read what follows as the origin of the human story, not as a second and rival creation.")],
  'entries': ['yhwh-yahweh', 'elohim', 'god-theos'],
  'lost': [
   loses("Hebrew toledot, “generations,” becomes Greek biblos geneseōs, “book of origin.” The Greek adds a book-image the Hebrew does not have. The Hebrew YHWH Elohim is reduced to “God,” and the Hebrew order “earth and heavens” becomes “heaven and earth.”"),
   keeps("Biblos geneseōs is the formula of Genesis 5:1 and the opening words of Matthew 1:1. The Greek heading lets the reader hear the chain from the first origin to the genealogy of Jesus Christ. The Greek word genesis also gave the book its name."),
   between("Latin and King James follow the Hebrew in naming the Lord God; the Latin has “origins,” the King James “generations.”"),
  ]},

 '2:5': {
  'received': "Before any plant had grown there was no rain and no human to work the ground.",
  'explain': ("The scene is set by what is missing. There are no shrubs or plants yet, no rain from God, and no one to work the "
   "soil. The Hebrew says the plants were “not yet” there; the Greek runs the sentence on from the heading, making the "
   "plants part of what God made “before” they came to be. Either way the earth waits on two things, water and a worker."),
  'shared': ["No plant of the field had yet grown.", "God had not yet sent rain on the earth.", "There was no human to work the ground."],
  'instructions': [ins(K, S, "Rain comes from God, and the ground is given to be worked."), ins(W, R, "Growth waits on gifts from above and labour from below.")],
  'entries': ['yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew terem, “not yet,” describes an earth without plants. Greek pro tou genesthai, “before it came to be,” turns the plants into further objects of “God made” in 2:4. The Greek again has “God” where the Hebrew names YHWH God."),
   between("Latin and King James keep the Lord God; the Latin has “shrub” and “plant of the countryside,” the Greek “green thing” and “plant of the field.”"),
  ]},

 '2:6': {
  'received': "Water rose from the earth and watered the whole face of the ground.",
  'explain': ("Before rain there was water from below. The Hebrew word for it is rare and disputed: a mist, a flow, a rising "
   "stream. The Greek and Latin choose a spring; the King James chooses a mist. The Hebrew also calls the ground adamah, "
   "the word the man’s name will come from in the next verse, a link the Greek does not carry."),
  'shared': ["Water rose from the earth.", "It watered the whole face of the ground.", "The earth was watered before any rain fell."],
  'instructions': [ins(K, S, "The ground was watered from within before rain came."), ins(W, R, "Provision can come by a way no one would have asked for.")],
  'entries': [],
  'lost': [
   loses("Hebrew ed appears only here and in Job 36:27 and may mean mist, flow or rising water. Greek pēgē is plainly “spring.” Hebrew adamah, “ground,” becomes Greek gē, “earth,” so the echo between adamah and adam in 2:7 is lost."),
   between("Latin fons follows the Greek spring; King James “mist” follows one reading of the Hebrew. The disputed word means neither can be called the wrong account."),
  ]},

 '2:7': {
  'received': "God formed the human from the dust of the ground, breathed life into him, and he became a living soul.",
  'explain': ("The making of the human is told as a potter’s work and a breath. God shapes dust, then breathes life into it, and "
   "a living soul results. The Hebrew places the breath in the nostrils, the Greek in the face; the Latin has clay where "
   "the others have dust. Paul quotes the closing words when he sets the first Adam beside the last."),
  'shared': ["God formed the human from the earth.", "God breathed the breath of life into him.", "The human became a living soul."],
  'instructions': [ins(K, S, "Human life comes from God’s forming and God’s breath."), ins(W, R, "Remember what you are made of and where your breath comes from.")],
  'entries': ['adam', 'yhwh-yahweh', 'last-adam'],
  'lost': [
   loses("Hebrew be-appav, “into his nostrils,” is a precise bodily picture. Greek prosōpon, “face,” is broader. The Hebrew YHWH God is again “God” in the Greek. Both keep the forming, the breath and the living soul, so neither text is less bodily than the other."),
   keeps("Greek eplasen is the potter’s verb, and enephysēsen, “breathed in,” is the verb John uses once, when the risen Jesus breathes on the disciples (John 20:22). Psychēn zōsan, “a living soul,” is the phrase Paul quotes in 1 Corinthians 15:45."),
   between("Latin de limo terrae, “from the clay of the ground,” changes the image from dust to clay; King James keeps dust and nostrils with the Hebrew."),
  ]},

 '2:8': {
  'received': "The Lord God planted a garden in Eden and placed the human he had formed in it.",
  'explain': ("The human is given a home before he is given a task. God plants, then places. The Hebrew garden becomes a "
   "“paradise” in Greek, a borrowed word for an enclosed royal park that will later name the life to come. Eden lies "
   "toward the east in the Hebrew and Greek; the Latin instead reads “of delight” and “from the beginning.”"),
  'shared': ["The Lord God planted a garden.", "The garden was in Eden.", "God placed the human he had formed there."],
  'instructions': [ins(K, S, "The human’s first home was planted by God."), ins(W, R, "A place prepared for you is a gift before it is a responsibility.")],
  'entries': ['eden', 'adam', 'lord-translation'],
  'lost': [
   keeps("Greek paradeisos, a loanword for an enclosed park, is the word that later carries the hope of paradise (Luke 23:43; Revelation 2:7). Here it is simply the planted garden. The Greek also has kyrios ho theos, “the Lord God,” for the first time in the chapter."),
   between("Hebrew mi-qedem can mean “in the east” or “from of old.” Hebrew, Greek and King James take the direction; the Latin takes the time, “from the beginning,” and translates Eden as “delight.” The Greek spells the name here and translates it at 3:23."),
  ]},

 '2:9': {
  'received': "God made every pleasant and fruitful tree grow, with the tree of life and the tree of the knowledge of good and evil in the middle.",
  'explain': ("The garden is full of trees that are good to look at and good to eat, and two are singled out: the tree of life "
   "and the tree of knowledge. The Greek names the second tree awkwardly, “knowing what is knowable of good and evil,” an "
   "over-literal rendering of the Hebrew. The tree of life, lost in chapter 3, returns in the last chapter of Revelation."),
  'shared': ["God made the trees of the garden grow.", "They were beautiful to see and good for food.", "The tree of life and the tree of the knowledge of good and evil stood among them."],
  'instructions': [ins(K, S, "God provided trees for beauty and for food."), ins(W, R, "Beauty and nourishment are both God’s provision, and both stand near a choice.")],
  'entries': ['eden', 'god-theos'],
  'lost': [
   loses("Hebrew nechmad le-mar’eh, “desirable to see,” becomes “beautiful to see.” The Hebrew “tree of the knowledge of good and evil” becomes a doubled “tree of knowing the knowable of good and evil.” The Greek adds eti, “further,” and has “God” for YHWH God."),
   keeps("Greek xylon tēs zōēs, “tree of life,” is the phrase Revelation uses for the tree beside the river of the city of God (Revelation 2:7; 22:2)."),
   between("Latin and King James name the Lord God and keep the plain “tree of knowledge of good and evil”; the Latin has “pleasant to eat from.”"),
  ]},

 '2:10': {
  'received': "A river flowed out of Eden to water the garden and divided into four.",
  'explain': ("Water now comes as a river, not a spring. It rises in Eden, waters the garden and then parts into four. The Hebrew "
   "calls the four “heads”; the Greek calls them “beginnings,” using the word of Genesis 1:1. Ezekiel and Revelation both "
   "later see a river of life flowing from God’s presence."),
  'shared': ["A river flowed out of Eden.", "It watered the garden.", "It divided into four."],
  'instructions': [ins(K, S, "The garden was watered by a river from Eden."), ins(W, R, "What begins as one gift can reach many places.")],
  'entries': ['eden'],
  'lost': [
   between("Hebrew rashim, “heads,” and Greek archas, “beginnings,” are both ways of naming a river’s source or branch; archē is the word of 1:1 and 1:16. Latin “branches” and King James “heads” divide the same way. The picture of one river becoming four is the same in all."),
   between("The Latin has the river flow “from the place of delight,” its rendering of Eden, where Greek and King James keep the name."),
  ]},

 '2:11': {
  'received': "The first river is Pishon, which circles the land of Havilah, where there is gold.",
  'explain': ("The first river is named and placed. Hebrew and Greek write the same two names in their own letters, and both "
   "say the river circles a land of gold. Where that land lies has been argued since antiquity, but the verse itself only "
   "names it. Havilah returns in the table of nations."),
  'shared': ["The first river is Pishon.", "It circles the land of Havilah.", "There is gold in that land."],
  'instructions': [ins(K, S, "The first river of Eden is Pishon, in a land of gold.")],
  'entries': ['eden'],
  'lost': [
   keeps("Hebrew Pishon and Chavilah, Greek Phisōn and Heuilat: the names are transliterated, and the verb “circles” and the gold agree. The Hebrew and Greek say the same thing. Rashi and Augustine disagree about geography, not about the words."),
   between("Latin “winds through” and King James “compasseth” are wording only."),
  ]},

 '2:12': {
  'received': "The gold of that land is good, and precious stones are found there.",
  'explain': ("The land of the first river is rich. All versions agree the gold is good; they differ on the stones. The Hebrew "
   "names bdellium, often taken as a fragrant resin, and the shoham stone, usually rendered onyx, the stone engraved with the "
   "tribes’ names on the high priest’s shoulders. The Greek names a red carbuncle and a green stone. No modern mineral can be assigned with certainty."),
  'shared': ["The gold of that land is good.", "Precious things are found there.", "The land is described as rich before anyone owns it."],
  'instructions': [ins(K, S, "The land of Pishon held good gold and precious stones."), ins(W, R, "Riches are part of the created world before they are part of anyone’s wealth.")],
  'entries': [],
  'lost': [
   loses("Hebrew ha-bedolach ve-even ha-shoham, “bdellium and the shoham stone,” becomes Greek anthrax and lithos prasinos, “carbuncle and green stone.” Bdellium may be a resin; anthrax is a glowing red gem; prasinos is leek-green. The Hebrew names, including the priestly shoham of Exodus 28:9, are not in the Greek."),
   between("Latin and King James keep bdellium and onyx with the Hebrew. The Greek may be giving contextual equivalents; that is a possibility, not a proof that the translator misunderstood."),
  ]},

 '2:13': {
  'received': "The second river is Gihon, which circles the land of Cush.",
  'explain': ("The second river is named and placed like the first. Hebrew calls its land Cush; the Greek, Latin and King "
   "James call it Ethiopia, the usual Greek name for Cush, the country south of Egypt along the upper Nile. Ancient Ethiopia "
   "is not the modern state, and some place this Cush elsewhere; the verse does not settle it."),
  'shared': ["The second river is Gihon.", "It circles a whole land.", "That land is called Cush or Ethiopia."],
  'instructions': [ins(K, S, "The second river of Eden is Gihon.")],
  'entries': ['eden'],
  'lost': [
   loses("Hebrew erets Kush, “the land of Cush,” becomes Greek gē Aithiopias, “the land of Ethiopia.” The Greek Bible regularly makes this substitution, so the Greek reader sees a familiar name where the Hebrew keeps the older one."),
   between("Latin and King James follow the Greek with Ethiopia. Acts 8:27 names an official of its queen."),
  ]},

 '2:14': {
  'received': "The third river is the Tigris, running by Assyria, and the fourth is the Euphrates.",
  'explain': ("The last two rivers are the great rivers of Mesopotamia. The Hebrew gives their native names, Chiddeqel and "
   "Perat; the Greek and Latin give Tigris and Euphrates, which the Saints English uses for both. The Hebrew places the "
   "Tigris east of Asshur, a city or land; the Greek says “opposite the Assyrians,” a people. The Euphrates will later mark the far border of the promised land."),
  'shared': ["The third river is the Tigris.", "It runs beside Assyria.", "The fourth river is the Euphrates."],
  'instructions': [ins(K, S, "The third and fourth rivers of Eden are the Tigris and the Euphrates.")],
  'entries': ['eden'],
  'lost': [
   loses("Hebrew Chiddeqel and Perat, with qidmat Ashshur, “east of Asshur,” become Greek Tigris and Euphratēs, katenanti Assyriōn, “opposite the Assyrians.” A place name becomes a people name, and “east of” becomes “in front of,” both legitimate senses of the Hebrew."),
   between("King James keeps the Hebrew name Hiddekel and “east of Assyria”; Latin has Tigris “toward the Assyrians” with the Greek. Daniel receives his last vision on the Tigris (Daniel 10:4), and Genesis 15:18 makes the Euphrates a border of the promise."),
  ]},

 '2:15': {
  'received': "The Lord God put the human in the garden to work it and guard it.",
  'explain': ("Now the task is given. The human is set in the garden with two duties, to work it and to keep it. The Hebrew "
   "verb for placing him comes from the word for rest, so he is settled there; the Greek uses a plain word of position and "
   "adds “whom He had formed,” echoing verse 8. Work belongs to the garden before the fall, not only after it."),
  'shared': ["The Lord God placed the human in the garden.", "He was to work it.", "He was to guard it."],
  'instructions': [ins(K, S, "The human was placed in the garden to work and keep it."), ins(W, R, "Work and care for a place are part of a good life, not a punishment.")],
  'entries': ['eden', 'adam', 'lord-translation'],
  'lost': [
   loses("Hebrew va-yannichehu, “settled him,” comes from nuach, the verb of rest. Greek etheto, “placed,” is the verb of 2:8 and has no overtone of rest. The Hebrew also names “the garden of Eden” here; the Greek says only “paradise.”"),
   keeps("“Whom He had formed” is added, repeating 2:8 so that the two verses echo. The placement is tied back to the forming."),
   between("Latin “garden of delight” and King James “garden of Eden” both name the place; the Latin “cultivate and keep” and King James “dress and keep” give the two duties."),
  ]},

 '2:16': {
  'received': "The Lord God commanded the human and gave him every tree of the garden to eat from.",
  'explain': ("The first command in Scripture opens with permission. Before any limit is named, the human is told he may "
   "eat freely of every tree. The Hebrew still calls him “the human”; the Greek begins here to use Adam as a name, at the "
   "point where a person is first addressed. The Hebrew’s doubled verb, “you may surely eat,” is imitated in the Greek."),
  'shared': ["The Lord God gave a command.", "It was addressed to the human.", "He may eat from every tree of the garden."],
  'instructions': [ins(C, S, "From every tree of the garden you may freely eat."), ins(W, R, "God’s first word of command is a wide permission; limits come inside generosity.")],
  'entries': ['adam', 'lord-translation'],
  'lost': [
   loses("Hebrew al ha-adam keeps the article, “the human.” The Greek treats Adam as a personal name from this verse on. The Hebrew intensifier akhol tokhel, “you may surely eat,” is carried into Greek as brōsei phagē, a Hebrew-style construction."),
   between("Latin has only “He commanded him, saying, Eat”; it names neither the Lord God nor Adam here and drops “freely.” King James keeps the Lord God and “the man.”"),
  ]},

 '2:17': {
  'received': "The tree of the knowledge of good and evil is forbidden, on pain of death.",
  'explain': ("One tree is withheld, and the penalty is stated plainly: in the day of eating, death. The Hebrew addresses one "
   "person throughout; the Greek shifts to the plural, “you shall not eat … you shall surely die,” as if the pair who will "
   "break the command were already in view. English “you” hides the difference. Paul traces the entry of death to this one disobedience."),
  'shared': ["The tree of the knowledge of good and evil is not to be eaten from.", "Death is the consequence of eating from it.", "The warning is emphatic."],
  'instructions': [ins(C, S, "You shall not eat from the tree of the knowledge of good and evil."), ins(K, S, "Eating from it brings death."), ins(W, R, "A single limit inside great freedom is still a limit, and it is given with its consequence.")],
  'entries': ['adam'],
  'lost': [
   loses("Hebrew tokhal, “you shall eat,” and the verbs that follow are singular. Greek phagesthe and apothaneisthe are plural: the prohibition and the death are addressed to more than one. The Greek may anticipate the pair of chapter 3, where the woman reports the command in the plural (3:3)."),
   keeps("Greek thanatō apothaneisthe, “by death you shall die,” doubles the idea as the Hebrew does. Romans 5:12 and 6:23 read death as the wage of this disobedience."),
   between("Latin and King James keep the singular with the Hebrew and give the same emphatic warning."),
  ]},

 '2:18': {
  'received': "The Lord God said it was not good for the human to be alone and resolved to make him a fitting helper.",
  'explain': ("For the first time something in the garden is called not good: solitude. God resolves to make a helper who "
   "corresponds to the human. The Hebrew has God speak in the singular, “I will make”; the Greek has “let us make,” the "
   "form of Genesis 1:26. The Hebrew word for helper is most often used of God himself coming to help his people."),
  'shared': ["It is not good for the human to be alone.", "God resolved to make him a helper.", "The helper was to correspond to him."],
  'instructions': [ins(K, S, "Being alone was judged not good by God."), ins(W, R, "Companionship is God’s remedy, planned before the human knew the need.")],
  'entries': ['adam', 'eve', 'lord-translation'],
  'lost': [
   loses("Hebrew e‘eseh, “I will make,” is singular. Greek poiēsōmen, “let us make,” is plural, repeating the deliberation of 1:26. The plural names no addressee and settles no doctrine on its own; the Hebrew has no plural here."),
   keeps("Poiēsōmen lets the two scenes of human creation, 1:26 and 2:18, sound alike. Whether that is the translator’s harmonising or an inherited reading is not known."),
   between("Latin “let Us make” follows the Greek; King James “I will make” follows the Hebrew. Hebrew ezer, “helper,” is the word of Psalm 121:2, “my help comes from the LORD.”"),
  ]},

 '2:19': {
  'received': "God formed the animals and birds and brought them to the human, who gave each its name.",
  'explain': ("The creatures are brought to the human for naming, and his names stand. In chapter 1 God named the day, the "
   "night and the sky; now that authority is shared. The Hebrew uses the same forming verb as in 2:7 and the same phrase, "
   "“living creature,” for animals and human alike. The Greek adds “further,” presenting this forming as an additional act, and calls the man Adam."),
  'shared': ["God formed the animals of the field and the birds of the sky.", "He brought them to the human.", "Whatever the human called each creature became its name."],
  'instructions': [ins(K, S, "The human named the living creatures, and God let the names stand."), ins(W, R, "To name is to take responsibility; God entrusts his creatures to human care.")],
  'entries': ['adam', 'god-theos'],
  'lost': [
   loses("Hebrew YHWH God becomes “God”; “the human” becomes Adam. Hebrew va-yitser min ha-adamah, “formed from the ground,” repeats the verb of 2:7, and nefesh chayah, “living creature,” is the phrase used of the human there."),
   keeps("Greek eti, “further,” presents the forming of the animals as an additional act rather than a first making, which eases the order of chapter 1. It is a Greek connective, not a different Hebrew word."),
   between("Latin and King James keep the Lord God; Latin has “animals of the earth” and “birds of heaven,” Greek “wild animals of the field” and “birds of the sky.”"),
  ]},

 '2:20': {
  'received': "The human named all the creatures, but no helper fit for him was found among them.",
  'explain': ("The naming is completed, and the search fails. Livestock, birds and wild animals all receive names, and none "
   "is a partner for the human. The Hebrew describes the missing helper as one “over against him,” a counterpart who faces "
   "him; the Greek here says “like him,” having said “corresponding to him” in verse 18. Both parts of the Hebrew sense are kept across the two verses."),
  'shared': ["The human gave names to all the creatures.", "He named livestock, birds and wild animals.", "No fitting helper was found for him."],
  'instructions': [ins(K, S, "None of the animals was a fitting helper for the human."), ins(W, R, "Dominion over creatures does not answer the need for a companion.")],
  'entries': ['adam', 'eve'],
  'lost': [
   between("Hebrew ezer ke-negdo, “a helper as over against him,” has no exact Greek equivalent. Greek boēthos homoios autōi, “a helper like him,” stresses likeness; in 2:18 the Greek had kat’ auton, “corresponding to him.” Latin “like himself” and King James “help meet for him” each take one side."),
   between("The Greek, Latin and King James name Adam; the Hebrew still says “the human.” Latin lists “all the animals,” Greek “all the livestock.”"),
  ]},

 '2:21': {
  'received': "God put the human into a deep sleep, took one of his ribs and closed the flesh over the place.",
  'explain': ("The helper is made from the human himself. God sends sleep, takes a rib, or side, and closes the flesh. The "
   "Hebrew calls the sleep a deep sleep; the Greek calls it an ecstasy, a trance, the word it also uses for Abraham’s sleep "
   "in Genesis 15:12. The Hebrew word for rib is also used for the sides of the Tabernacle. John uses the Greek word for the pierced side of Jesus."),
  'shared': ["God caused the human to sleep.", "God took one of his ribs.", "God closed up the flesh in its place."],
  'instructions': [ins(K, S, "The woman was taken from the human’s own body while he slept."), ins(W, R, "The deepest gifts may be given while we are not awake to see them.")],
  'entries': ['adam', 'eve'],
  'lost': [
   loses("Hebrew tardemah, “deep sleep,” becomes Greek ekstasis, a trance or displaced state. Hebrew “closed up flesh” becomes Greek “filled up flesh” (aneplērōsen). YHWH God is “God,” and the human is Adam."),
   keeps("Ekstasis also renders Abraham’s deep sleep in 15:12, so the Greek links the two God-sent sleeps. Greek pleura, “rib” or “side,” is the word John uses for the side of Jesus (John 19:34), which Augustine set beside this verse."),
   between("Hebrew tsela and Greek pleura both mean rib or side; Latin and King James say rib. The Latin keeps “the Lord God” and “deep sleep” with the Hebrew."),
  ]},

 '2:22': {
  'received': "The Lord God built the rib into a woman and brought her to the human.",
  'explain': ("The woman is “built,” an architectural word in both Hebrew and Greek, where the man was “formed” like clay. "
   "The verb is unexpected, and the translator kept it. Then God brings her to the human, as he brought the animals, but "
   "this time the meeting is different. The Greek continues to call the man Adam."),
  'shared': ["The Lord God made the rib into a woman.", "The verb is “built.”", "God brought her to the human."],
  'instructions': [ins(K, S, "God made the woman from the human and brought her to him."), ins(W, R, "The partner is God’s gift, brought rather than found.")],
  'entries': ['eve', 'adam', 'lord-translation'],
  'lost': [
   keeps("Hebrew va-yiven and Greek ōkodomēsen are the same building verb; the Greek did not substitute a plainer word of making. Both traditions could develop the image of the woman built."),
   between("The Greek, Latin and King James name Adam; the Hebrew has “the human.” Latin “fashioned” is wording only."),
  ]},

 '2:23': {
  'received': "The human recognised the woman as his own bone and flesh and named her Woman because she was taken from Man.",
  'explain': ("The first human words in the Bible are a recognition. “Bone of my bones and flesh of my flesh” becomes the "
   "Bible’s phrase for close kinship. The Hebrew then plays on sound: ishah, woman, from ish, man. Greek, Latin and English "
   "cannot keep the pun; the Greek instead says she was taken “from her husband,” making the marriage explicit."),
  'shared': ["The woman is bone of his bones and flesh of his flesh.", "She is called Woman.", "She was taken from Man."],
  'instructions': [ins(K, S, "The woman is of the same bone and flesh as the man."), ins(W, R, "Kinship is recognised and spoken before it is commanded.")],
  'entries': ['eve', 'adam'],
  'lost': [
   loses("Hebrew ishah and ish sound alike: Woman because taken from Man. Greek gynē and anēr cannot carry it, and Latin and English cannot either. Hebrew zot ha-pa‘am, “this at last,” becomes Greek touto nyn, “this now.”"),
   keeps("Autēs, “her” man, is added: she was taken from her husband. The relationship is spelled out as marriage, perhaps to make up for the lost wordplay, though that is an inference."),
   between("Latin de viro, “from man,” and King James “out of Man” keep the Hebrew sense without the sound. “Bone of my bones” recurs for Laban and Jacob (29:14) and for the tribes and David (2 Samuel 5:1)."),
  ]},

 '2:24': {
  'received': "A man leaves his father and mother, is joined to his wife, and they become one flesh.",
  'explain': ("The narrator draws the lesson. Marriage means leaving one household and holding fast in a new one, and the "
   "two become one flesh. The Hebrew verb is “cling,” the Greek “be glued,” both strong. The Greek adds “the two,” the "
   "wording Jesus and Paul quote. Paul applies the verse to marriage and then to Christ and the church."),
  'shared': ["A man leaves his father and mother.", "He is joined to his wife.", "They become one flesh."],
  'instructions': [ins(K, S, "Marriage joins a man and his wife as one flesh."), ins(W, R, "Leaving and joining belong together; a new bond asks for a loosening of the old.")],
  'entries': ['eve', 'adam'],
  'lost': [
   keeps("Greek hoi dyo, “the two,” is not in the Hebrew of this verse. It is the form quoted in Matthew 19:5, Mark 10:8, 1 Corinthians 6:16 and Ephesians 5:31. The Greek also puts the verbs in the future, “shall leave … shall become.”"),
   between("Hebrew davaq, “clings,” and Greek proskollēthēsetai, “shall be glued,” are equally firm; Latin “cling” and King James “cleave” match them. The Latin has “the two” with the Greek; the King James does not."),
  ]},

 '2:25': {
  'received': "The human and his wife were both naked and felt no shame.",
  'explain': ("The chapter ends in innocence. The pair are naked and unashamed, a state the next chapter will end. The Hebrew "
   "plants a sound-play here: arummim, naked, is almost arum, the crafty serpent of 3:1. No translation can carry it. The "
   "Greek says “the two,” as in verse 24, and continues to name Adam."),
  'shared': ["Both were naked.", "They were the human and his wife.", "They were not ashamed."],
  'instructions': [ins(K, S, "Before the fall the pair were naked and unashamed."), ins(W, R, "Shame is not original to human life; it enters with what follows.")],
  'entries': ['adam', 'eve', 'eden-serpent'],
  'lost': [
   loses("Hebrew arummim, “naked,” echoes arum, “crafty,” the serpent’s word in 3:1. Greek gymnoi and phronimōtatos cannot keep the link, and neither can Latin or English. The Hebrew “the human” is Adam in the Greek."),
   between("Greek “the two” matches its own wording of 2:24; Latin and King James say “both.” All agree they were not ashamed."),
  ]},
 }
}
