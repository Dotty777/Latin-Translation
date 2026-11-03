# Study prose for Genesis 7 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 7,
 'chapterNote': (
  "The entry into the ark and the rising of the waters are told alike in every column; the forty days, the hundred and fifty days, "
  "the fifteen cubits and Noah’s six hundred years agree. What varies is small but real. The Hebrew keeps the seventeenth day of the "
  "second month, sevens of all birds without a clean and unclean division, the great deep, the breath in the nostrils of 7:22, and "
  "YHWH shutting Noah in. The Greek keeps the twenty-seventh day, clean and unclean birds, “everything that rises up” for every living "
  "thing, the birds first in the list of 7:8, “forty nights” added at 7:17, and the Lord God closing the ark from outside. The Latin "
  "and King James follow the Hebrew date and lists."),
 'verses': {

 '7:1': {
  'received': "The Lord told Noah to enter the ark with his household, because he had seen him righteous in his generation.",
  'explain': ("The command to enter comes with its reason: God has seen Noah righteous. It repeats the judgement of 6:9 in God’s own "
   "voice. The Hebrew YHWH is the Greek Lord God; the Latin says only “the Lord said to him.” The invitation and the assessment "
   "agree in all four."),
  'shared': ["The Lord told Noah to enter the ark.", "His whole household was to go with him.", "God had seen Noah righteous in this generation."],
  'instructions': [ins(C, S, "Enter the ark, you and all your household."), ins(K, S, "God counted Noah righteous before him.")],
  'entries': ['noah', 'noahs-ark', 'lord-translation'],
  'lost': [
   loses("Hebrew YHWH becomes Greek kyrios ho theos, “the Lord God.”"),
   between("Latin “the Lord said to him” drops Noah’s name; King James “Come thou and all thy house into the ark” keeps the Hebrew. The reason, “I have seen you righteous,” is the same in all."),
  ]},

 '7:2': {
  'received': "Noah was to take seven pairs of every clean animal and one pair of every unclean animal, male and female.",
  'explain': ("The pairs of 6:19 are refined. Clean animals come by sevens, unclean by twos, each male with female. The Hebrew "
   "describes the pair with the words for a man and his wife; the Greek says male and female. Whether “seven by seven” means seven "
   "animals or seven pairs is left as the texts leave it. The clean and unclean distinction appears before the law names it."),
  'shared': ["Seven of every clean animal are to be taken.", "Two of every unclean animal are to be taken.", "Each kind is to come male and female."],
  'instructions': [ins(C, S, "Take seven of the clean animals and two of the unclean, male and female."), ins(W, R, "Clean animals are taken in greater number; provision is being made for sacrifice and food as well as survival.")],
  'entries': ['noahs-ark'],
  'lost': [
   between("Hebrew ish ve-ishto, “a male and its mate,” literally “a man and his wife,” is Greek arsen kai thēly, “male and female.” Latin and King James keep “male and female” and “the male and his female.” The sevens are the same in all."),
  ]},

 '7:3': {
  'received': "Noah was also to take the birds of the sky by sevens, to keep their offspring alive on the earth.",
  'explain': ("The birds are added to the instruction. The Hebrew, Latin and King James take seven of the birds, with no clean and "
   "unclean division; the Greek divides the birds too, seven of the clean and two of the unclean, extending the rule of verse 2. The "
   "purpose is the same in all: to keep seed alive on the face of the earth."),
  'shared': ["Birds of the sky are to be taken by sevens.", "They come male and female.", "The purpose is to keep offspring alive on all the earth."],
  'instructions': [ins(C, S, "Take the birds by sevens, male and female, to preserve their offspring."), ins(W, R, "Even the birds are gathered for the sake of what comes after; the flood is survived with the future in mind.")],
  'entries': ['noahs-ark'],
  'lost': [
   keeps("An added tōn katharōn, “of the clean,” to the birds, and a second clause, “two by two of the birds that are not clean,” which the Hebrew does not have. The clean and unclean division of verse 2 is carried to the birds in Greek alone."),
   between("Latin “of the birds of heaven take seven and seven” and King James “of fowls also of the air by sevens” follow the Hebrew’s undivided sevens."),
  ]},

 '7:4': {
  'received': "In seven days God would send rain for forty days and nights and wipe every living thing he had made from the earth.",
  'explain': ("The timetable is given: seven days of waiting, then forty days and nights of rain. The Hebrew says God will wipe "
   "away every living thing; the Greek says everything that rises up, an unusual rendering of the Hebrew word for existing things "
   "that does not refer to resurrection or to the newborn. Forty becomes Scripture’s number of testing."),
  'shared': ["Rain will begin in seven days.", "It will fall for forty days and forty nights.", "God will wipe out every living thing he made from the earth."],
  'instructions': [ins(K, S, "God announced seven days’ warning and forty days of rain."), ins(W, R, "Seven days are given between the word and the water; judgement announced is a space for obedience.")],
  'entries': [],
  'lost': [
   loses("Hebrew kol-ha-yequm, “every living thing” or “all that exists,” becomes Greek pan to anastēma, “everything that rises up,” a different image. Hebrew “face of the ground” is Greek “face of the earth.” Hebrew “I will send rain” is Greek “I am bringing rain.”"),
   keeps("Greek tesserakonta hēmeras kai tesserakonta nyktas, “forty days and forty nights,” is the span of Exodus 24:18 and Matthew 4:2."),
   between("Latin “every being I have made” and King James “every living substance” follow the Hebrew sense."),
  ]},

 '7:5': {
  'received': "Noah did all that the Lord commanded him.",
  'explain': ("The obedience formula of 6:22 returns before the entry, framing the whole preparation. Noah did all that was "
   "commanded. The Hebrew says YHWH, the Greek the Lord God. Nothing is recorded of Noah’s words; only his doing."),
  'shared': ["Noah did what the Lord commanded.", "He did all of it.", "The obedience is stated again before the flood."],
  'instructions': [ins(K, S, "Noah obeyed the Lord’s command about the animals and the timetable."), ins(W, R, "Obedience is told twice so that the reader does not miss it; the ark is faith in the form of work.")],
  'entries': ['noah'],
  'lost': [
   loses("Hebrew YHWH is again Greek “the Lord God.”"),
   between("Latin and King James say “the Lord” with the Hebrew. Greek epoiēsen … panta, “did all,” repeats 6:22 and anticipates 7:16."),
  ]},

 '7:6': {
  'received': "Noah was six hundred years old when the flood came upon the earth.",
  'explain': ("Noah’s age dates the flood. All versions give six hundred. By the Greek figures of chapter 5, Methuselah would "
   "still be alive in this year, a problem the Hebrew numbers do not have. The verse is a hinge between the command and the entry."),
  'shared': ["Noah was six hundred years old.", "The flood of water came upon the earth.", "The two facts are tied together."],
  'instructions': [ins(K, S, "The flood came in Noah’s six hundredth year.")],
  'entries': ['noah'],
  'lost': [between("Hebrew, Greek, Latin and King James all give six hundred. The Latin says “he,” the others name Noah; Latin “inundated” is wording only.")]},

 '7:7': {
  'received': "Noah entered the ark with his sons, his wife and his sons’ wives because of the flood.",
  'explain': ("The entry itself. Eight people go in, named as in 6:18, and the reason is the water. The Hebrew says waters in the "
   "plural, the Greek water in the singular, ordinary idiom in each language. The household is the same in every version."),
  'shared': ["Noah entered the ark.", "His sons, his wife and his sons’ wives entered with him.", "They entered because of the flood."],
  'instructions': [ins(K, S, "Noah’s household of eight entered the ark."), ins(W, R, "They entered before the rain; faith moves on the word, not on the weather.")],
  'entries': ['noah', 'noahs-ark'],
  'lost': [between("Hebrew mei ha-mabbul, “waters of the flood,” plural, is Greek to hydōr tou kataklysmou, singular; idiom only. Latin and King James agree. 1 Peter 3:20 counts the eight.")]},

 '7:8': {
  'received': "Clean and unclean animals, birds and everything that creeps on the ground came with them.",
  'explain': ("The animals are listed as they come. The Hebrew order is clean animals, unclean animals, birds, creeping things; "
   "the Greek puts the birds first. Both keep the clean and unclean groups. The lists should be compared as they stand rather than "
   "rearranged to match."),
  'shared': ["Clean animals came.", "Unclean animals came.", "Birds and creeping things came."],
  'instructions': [ins(K, S, "Animals of every class came to the ark.")],
  'entries': ['noahs-ark'],
  'lost': [
   loses("Hebrew lists clean animals, unclean animals, birds, and everything that moves on the ground. Greek lists birds, clean livestock, unclean livestock, creeping things; the Hebrew order is changed and “ground” becomes “earth.”"),
   between("Latin and King James keep the Hebrew order."),
  ]},

 '7:9': {
  'received': "They came to Noah into the ark two by two, male and female, as God had commanded.",
  'explain': ("The creatures enter in pairs, as God commanded. “Two by two” describes paired entry and does not cancel the sevens of "
   "verse 2. The Hebrew repeats Noah’s name at the end; the Greek uses a pronoun. The Latin says the Lord commanded where the others say God."),
  'shared': ["The animals entered two by two.", "They were male and female.", "They came as God commanded Noah."],
  'instructions': [ins(K, S, "The animals came in pairs as God commanded."), ins(W, R, "The creatures obey the command given to Noah; creation keeps step with the man who keeps step with God.")],
  'entries': ['noahs-ark'],
  'lost': [between("Hebrew “as God commanded Noah” is Greek “as God commanded him”; Latin has “the Lord,” King James “God … Noah.” Hebrew ba’u, “came,” is Greek eisēlthon, “entered.”")]},

 '7:10': {
  'received': "After the seven days the waters of the flood came upon the earth.",
  'explain': ("The waiting of verse 4 ends. Seven days pass and the water comes. The verse is brief and the versions agree, with "
   "the Latin’s “inundated” as the only flourish. Everything announced now begins."),
  'shared': ["Seven days passed.", "The flood came.", "The water was upon the earth."],
  'instructions': [ins(K, S, "The flood came as announced after seven days.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James agree; plural and singular water are idiom.")]},

 '7:11': {
  'received': "In Noah’s six hundredth year, in the second month, the springs of the deep burst and the windows of heaven opened.",
  'explain': ("The flood is dated to the day and described from two directions: water from below, as the springs of the deep burst, "
   "and water from above, as the windows or floodgates of heaven open. The Hebrew, Latin and King James date it to the seventeenth "
   "day; the Greek to the twenty-seventh. The Hebrew says the great deep; the Greek the abyss, without “great.” Malachi uses the Greek floodgates for a blessing."),
  'shared': ["The date is Noah’s six hundredth year, second month.", "The springs of the deep burst open.", "The windows of heaven were opened."],
  'instructions': [ins(K, S, "The flood came from the deep below and the heavens above on a recorded day."), ins(W, R, "The waters separated at creation are let loose together; the flood is an undoing of the order of Genesis 1.")],
  'entries': [],
  'lost': [
   loses("Hebrew be-shiv‘ah-asar yom, “on the seventeenth day,” becomes Greek hebdomē kai eikadi, “on the twenty-seventh.” Hebrew tehom rabbah, “the great deep,” becomes Greek abyssos without “great”; Hebrew arubbot, “windows,” becomes katarraktai, “floodgates.” The Greek adds “on that day.”"),
   keeps("Katarraktai, “floodgates,” is the word of Malachi 3:10 and 2 Kings 7:2; the Greek date forms a pattern with 8:4 and 8:14 that invites study as a flood calendar."),
   between("Latin “seventeenth … great deep … floodgates” and King James “seventeenth … great deep … windows” keep the Hebrew date."),
  ]},

 '7:12': {
  'received': "Rain fell on the earth for forty days and forty nights.",
  'explain': ("The rain announced in verse 4 falls. All versions agree, and all include the nights. At creation God had not yet "
   "sent rain; the first rain told in Scripture is the rain of judgement."),
  'shared': ["Rain fell on the earth.", "It fell for forty days.", "It fell for forty nights."],
  'instructions': [ins(K, S, "The rain lasted forty days and forty nights.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James agree word for word in sense. Greek hyetos, “rain,” answers the rain God had not yet sent in 2:5.")]},

 '7:13': {
  'received': "On that very day Noah entered the ark with Shem, Ham and Japheth, his wife and his sons’ three wives.",
  'explain': ("The entry is told again, now dated to the day the water came and with the sons named. The Hebrew’s emphatic “on that "
   "very day” is the Greek’s “on that day.” The Hebrew ends “with them,” the Greek “with him.” The household is the same eight."),
  'shared': ["Noah entered the ark on that day.", "Shem, Ham and Japheth entered with him.", "Noah’s wife and his sons’ three wives entered."],
  'instructions': [ins(K, S, "Noah’s household entered the ark on the day the flood began.")],
  'entries': ['noah'],
  'lost': [between("Hebrew be-etsem ha-yom ha-zeh, “on that very day,” is Greek en tē hēmera tautē, “on that day”; Hebrew ittam, “with them,” is Greek met’ autou, “with him.” Latin and King James keep the emphasis and the plural.")]},

 '7:14': {
  'received': "Every wild animal, all livestock, every creeping thing and every bird entered according to its kind.",
  'explain': ("The animals are listed by kind, in the words of Genesis 1. The Hebrew begins “they,” picking up the household, and "
   "closes with an extra phrase, “every bird of every wing”; the Greek drops both and runs its list straight into the verb of the next "
   "verse. The Latin expands the birds to “all birds and all flying creatures.”"),
  'shared': ["Wild animals entered according to kind.", "Livestock and creeping things entered according to kind.", "Every bird entered according to kind."],
  'instructions': [ins(K, S, "Every kind of land animal and bird entered the ark.")],
  'entries': ['noahs-ark'],
  'lost': [
   loses("Hebrew hemmah, “they,” at the head and kol tsippor kol-kanaf, “every bird of every wing,” at the end are both absent from the Greek, which gives the bare list and continues into 7:15."),
   between("Latin “they … all birds and all flying creatures” and King James “they … every bird of every sort” keep the Hebrew frame."),
  ]},

 '7:15': {
  'received': "They came to Noah into the ark, two by two of all flesh that had the breath of life.",
  'explain': ("The sentence that began in verse 14 ends: all these came in pairs. “All flesh in which is a spirit of life” gathers "
   "every creature that breathes. The versions agree; in the Greek the long inventory of verse 14 is the subject of this verb."),
  'shared': ["They came to Noah into the ark.", "They came two by two.", "They were of all flesh that has the breath of life."],
  'instructions': [ins(K, S, "The breathing creatures entered the ark in pairs.")],
  'entries': ['noahs-ark'],
  'lost': [between("Hebrew ruach chayyim and Greek pneuma zōēs are “spirit of life”; Latin and King James say “breath of life.” The Hebrew starts a new sentence, “they came”; the Greek continues the one begun in 7:14.")]},

 '7:16': {
  'received': "Male and female of all flesh entered as God commanded, and the Lord shut Noah in.",
  'explain': ("The entry ends with God’s own hand. The animals have come as commanded; then the Lord closes the door. The Hebrew says "
   "YHWH shut him in, or shut behind him; the Greek says the Lord God closed the ark from outside him. Both make God the one who "
   "shuts, and neither leaves Noah outside. The chapter uses God for the command and the Lord for the closing."),
  'shared': ["Male and female of all flesh entered.", "They entered as God commanded Noah.", "The Lord shut the ark."],
  'instructions': [ins(K, S, "God himself shut the ark once Noah and the creatures were inside."), ins(W, R, "The door is closed from outside; the safety of those within is God’s doing, not their own.")],
  'entries': ['noah', 'noahs-ark', 'yhwh-yahweh', 'lord-translation'],
  'lost': [
   loses("Hebrew va-yisgor YHWH ba‘ado, “YHWH shut behind him,” has no object but Noah. Greek ekleisen kyrios ho theos tēn kibōton exōthen autou, “the Lord God closed the ark from outside him,” names the ark and the outside. Hebrew “commanded him” becomes Greek “commanded Noah.”"),
   between("Latin “the Lord shut him in from outside” stands between the two; King James “the LORD shut him in” follows the Hebrew."),
  ]},

 '7:17': {
  'received': "The flood lasted forty days, and the waters rose and lifted the ark above the earth.",
  'explain': ("The water does what it was built for: it lifts the ark. The Hebrew says the flood was on the earth forty days; the "
   "Greek adds “and forty nights,” repeating the phrase of verse 12. The addition does not lengthen the flood. The ark rises; "
   "the Latin says high above the earth."),
  'shared': ["The flood was on the earth forty days.", "The waters increased.", "They lifted the ark above the earth."],
  'instructions': [ins(K, S, "The rising waters lifted the ark from the earth."), ins(W, R, "The same water that destroys carries the ark; judgement and rescue are one event seen from two places.")],
  'entries': ['noahs-ark'],
  'lost': [
   keeps("An added kai tesserakonta nyktas, “and forty nights,” which this Hebrew verse lacks though 7:12 has it. The Greek repeats a duration already in the story; it does not make the flood longer."),
   between("Latin “for forty days … lifted the ark high above the earth” and King James “forty days … bare up the ark” follow the Hebrew."),
  ]},

 '7:18': {
  'received': "The waters prevailed and increased greatly, and the ark floated on them.",
  'explain': ("The Hebrew verb for the water’s strength, gavar, to grow mighty, is used four times from here to verse 24; the Greek "
   "says the water held power. The ark moves on the face of the waters in the Hebrew; the Greek says it was carried. No one steers. "
   "The Latin adds that the water filled everything on the surface."),
  'shared': ["The waters prevailed.", "They increased greatly upon the earth.", "The ark was borne on the waters."],
  'instructions': [ins(K, S, "The ark floated on the prevailing waters without human steering."), ins(W, R, "The ark has no rudder; those inside can only be carried.")],
  'entries': ['noahs-ark'],
  'lost': [between("Hebrew va-telekh ha-tevah, “the ark moved,” is Greek epephereto hē kibōtos, “the ark was carried,” the verb of the Spirit over the water in 1:2. Hebrew gavar is Greek ekratei, “held power.” Latin “floated … filled everything” and King James “went upon the face of the waters” are wording.")]},

 '7:19': {
  'received': "The waters prevailed exceedingly and covered all the high mountains under heaven.",
  'explain': ("The intensifier is doubled, very very greatly, in Hebrew and Greek alike. The high mountains under all the heavens "
   "go under. The Hebrew has the mountains covered, a passive; the Greek has the water cover them, an active. Peter describes the "
   "world of that time as overflowed with water and perishing."),
  'shared': ["The waters prevailed exceedingly.", "All the high mountains were covered.", "They were the mountains under the whole heaven."],
  'instructions': [ins(K, S, "The flood covered the high mountains under heaven.")],
  'entries': [],
  'lost': [between("Hebrew me’od me’od, “very very,” is Greek sphodra sphodrōs; Hebrew “were covered” is Greek “covered,” with the water as subject; Hebrew “under all the heavens” is Greek “under heaven.” Latin and King James follow the Hebrew passive. 2 Peter 3:6 and Psalm 104:6 recall the scene.")]},

 '7:20': {
  'received': "The water rose fifteen cubits above the mountains and covered them.",
  'explain': ("A measure is given: fifteen cubits over the highest peaks, half the ark’s own height of thirty cubits. The Hebrew says "
   "the mountains were covered; the Greek repeats “all the high mountains.” The Latin reads the fifteen cubits as above the mountains "
   "it covered. A modern conversion would need a stated cubit."),
  'shared': ["The water rose fifteen cubits.", "It rose above the mountains.", "The mountains were covered."],
  'instructions': [ins(K, S, "The water stood fifteen cubits above the mountains.")],
  'entries': [],
  'lost': [
   keeps("Greek repeats panta ta orē ta hypsēla, “all the high mountains,” from 7:19; the Hebrew says only “the mountains.”"),
   between("Latin “above the mountains it covered” and King James “fifteen cubits upward … the mountains were covered” follow the Hebrew. Fifteen cubits is half the ark’s height in 6:15."),
  ]},

 '7:21': {
  'received': "All flesh that moved on the earth died: birds, livestock, wild animals, creeping things and all humankind.",
  'explain': ("The death of all land life is stated plainly, class by class, ending with humankind. The Hebrew says swarming "
   "things that swarm and all humankind; the Greek says creeping things that move and every human. The refrain of chapter 5, “and he "
   "died,” now falls on all flesh at once."),
  'shared': ["All flesh moving upon the earth died.", "Birds, livestock, wild animals and creeping things died.", "All humankind died."],
  'instructions': [ins(K, S, "All land life outside the ark died in the flood."), ins(W, R, "The judgement announced in 6:7 is carried out to the letter; God’s warnings are not figures of speech.")],
  'entries': [],
  'lost': [between("Hebrew kol-ha-sherets ha-shorets, “every swarming thing that swarms,” is Greek “every creeping thing moving”; Hebrew kol-ha-adam, “all humankind,” is Greek pas anthrōpos, “every human.” Hebrew yigva, “perished,” is Greek apethanen, “died,” the refrain of chapter 5. Latin and King James agree in sense.")]},

 '7:22': {
  'received': "Everything on the dry land that had the breath of life died.",
  'explain': ("The scope is restated by breath and by place. The Hebrew says everything on dry land in whose nostrils was the breath "
   "of the spirit of life; the Greek drops nostrils and spirit and coordinates the clauses, everything that had a breath of life, and "
   "all that was on the dry land. The dry land called up on the third day is where death falls; sea creatures are not named."),
  'shared': ["Everything with the breath of life died.", "The dead were on the dry land.", "The sea creatures are not named."],
  'instructions': [ins(K, S, "Death fell on all that breathed on the dry land.")],
  'entries': [],
  'lost': [
   loses("Hebrew nishmat-ruach chayyim be-appav, “the breath of the spirit of life in its nostrils,” is condensed to Greek pnoē zōēs, “a breath of life”; nostrils and spirit are gone, and the Hebrew’s single qualified clause becomes two coordinated ones."),
   between("Latin “everything upon the land that had the breath of life” also drops the nostrils; King James “all in whose nostrils was the breath of life” keeps the Hebrew. Greek tēs xēras, “the dry land,” is the word of 1:9–10."),
  ]},

 '7:23': {
  'received': "God wiped out every living thing on the earth; only Noah and those with him in the ark remained.",
  'explain': ("The destruction is summed up and the remnant named. Everything from humans to birds is wiped away; only Noah remains, "
   "and those with him. The Hebrew says every living thing on the face of the ground; the Greek everything standing on the face of all "
   "the earth. From the Greek verb for remaining comes the Bible’s word for the remnant."),
  'shared': ["God wiped out every living thing from the face of the earth.", "Humans, livestock, creeping things and birds were wiped away.", "Only Noah and those with him in the ark remained."],
  'instructions': [ins(K, S, "Only Noah and those in the ark survived the flood."), ins(W, R, "A remnant is left; from here on the story of salvation is the story of the few who remain.")],
  'entries': ['noah', 'noahs-ark'],
  'lost': [
   loses("Hebrew kol-ha-yequm, “every living thing,” is again Greek pan to anastēma, “everything standing”; Hebrew “face of the ground” becomes Greek “face of all the earth.”"),
   keeps("Greek kateleiphthē, “remained,” is the root of the remnant of Isaiah 10:22 and Romans 9:27 and 11:5."),
   between("Latin “every being upon the earth” and King James “every living substance … upon the face of the ground” render the Hebrew sense; King James makes the verb passive, “was destroyed.”"),
  ]},

 '7:24': {
  'received': "The waters prevailed on the earth for a hundred and fifty days.",
  'explain': ("The chapter closes with a count: a hundred and fifty days of the water’s power. The Hebrew says the waters prevailed; "
   "the Greek that the water remained high, a description of height, not of honour. The Latin says the waters held the earth. "
   "The duration agrees in all."),
  'shared': ["The waters prevailed on the earth.", "They did so for a hundred and fifty days.", "The flood held before it began to recede."],
  'instructions': [ins(K, S, "The flood prevailed for a hundred and fifty days.")],
  'entries': [],
  'lost': [between("Hebrew va-yigberu, “prevailed,” the fourth use of gavar, is Greek hypsōthē, “was raised high.” Latin “held the earth” and King James “prevailed” follow the Hebrew. All give a hundred and fifty days.")]},
 }
}
