# Study prose for Genesis 5 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

def birth(name, son, heb, grk, extra_explain='', extra_lost=None, wisdom=None):
    """A 'lived N years and begat' verse where Hebrew and Greek give different ages."""
    v = {
     'received': f"{name} lived {heb} years in the Hebrew, {grk} in the Greek, and became the father of {son}.",
     'explain': (f"The formula repeats: a man lives so many years and begets a son. All versions agree on the father and the son. "
       f"They differ on the age. The Hebrew, Latin and King James give {heb} years; the Greek gives {grk}, adding a hundred as it does "
       f"for most fathers in this chapter, and taking the same hundred from the years after the birth, so the total life stays the same. {extra_explain}").strip(),
     'shared': [f"{name} lived a set number of years before this son.", f"He begat {son}.", "The generation passes from father to son."],
     'instructions': [ins(K, S, f"{son} was born to {name}; the age at the birth differs between the Hebrew and Greek texts.")],
     'entries': [],
     'lost': [
      loses(f"Hebrew gives {heb} years before {son}; Greek gives {grk}. The Hebrew interval is replaced, and with it the elapsed chronology from Adam shifts by a century at this generation."),
      keeps(f"The Greek keeps the total lifespan by shortening the years after {son}’s birth. Repeated increases before fatherhood balanced by decreases after it look like a patterned chronology rather than slips; which chronology is older is not settled."),
      between(f"Latin and King James give {heb} with the Hebrew.")]}
    if wisdom: v['instructions'].append(ins(W, R, wisdom))
    if extra_lost: v['lost'].extend(extra_lost)
    return v

def after(name, son, heb, grk, total, extra=''):
    return {
     'received': f"After {son}’s birth {name} lived on, {heb} years in the Hebrew and {grk} in the Greek, and had other sons and daughters.",
     'explain': (f"The second line of the formula counts the years after the named son and notes the rest of the family only as sons and daughters. "
       f"The Hebrew, Latin and King James give {heb}; the Greek gives {grk}, the mirror image of the change in the verse before, so that {name}’s total of {total} is the same in both. {extra}").strip(),
     'shared': [f"{name} lived on after {son} was born.", "He had other sons and daughters.", "Only the one son in the line is named."],
     'instructions': [ins(K, S, f"{name} had further children after {son}; the years given differ between Hebrew and Greek.")],
     'entries': [],
     'lost': [
      loses(f"Hebrew {heb} years after {son} becomes Greek {grk}. The hundred years moved before the birth in the previous verse are taken away here."),
      between(f"Latin and King James give {heb} with the Hebrew. Greek huious kai thygateras, “sons and daughters,” is the formula of 5:4 and 11:11.")]}

def total(name, years, note, extra_lost=None, see=''):
    v = {
     'received': f"{name} lived {years} years in all, and he died.",
     'explain': (f"The third line closes a life: all the days, a total, and death. {note} The words “and he died” close eight of the nine lives in this chapter; only Enoch’s entry ends differently."),
     'shared': [f"All the days of {name} are summed.", f"They came to {years} years.", "He died."],
     'instructions': [ins(K, S, f"{name} died after {years} years."), ins(W, R, "Every long life in the list ends the same way; the count of days is a reminder to number our own.")],
     'entries': [],
     'lost': [between(f"Hebrew, Greek, Latin and King James all give {years}, and all say “and he died.” {see}".strip())]}
    if extra_lost: v['lost'] = extra_lost + v['lost']
    return v

CHAPTER = {
 'slug': 'genesis', 'chapter': 5,
 'chapterNote': (
  "The ten generations from Adam to Noah are the same men in the same order in every column, and the totals of their lives "
  "agree almost everywhere. What varies is the division of the years. The Hebrew keeps the shorter ages at fatherhood (Adam 130, "
  "Seth 105, Enosh 90 and so on), Enoch walking with God for three hundred years, Methuselah 187 at Lamech’s birth, and Lamech’s "
  "777. The Greek keeps a hundred more years before most births and a hundred fewer after, so that the flood falls later in its "
  "reckoning; it has Enoch pleasing God for two hundred years and “not found” because God transferred him, Methuselah 167, Lamech "
  "753, Noah’s “three sons,” and “book of the origin of human beings” for the heading. The Latin and King James follow the Hebrew "
  "numbers throughout; Hebrews 11:5 follows the Greek wording about Enoch."),
 'verses': {

 '5:1': {
  'received': "This is the record of Adam’s descendants, made in the likeness of God on the day God created humankind.",
  'explain': ("A new heading opens the first genealogy. The Hebrew calls it the book of the generations of Adam; the Greek the "
   "book of the origin of human beings, the phrase it used in 2:4 and that Matthew uses of Jesus. The verse looks back to 1:26–27: "
   "humankind was made in the likeness, or image, of God. The Hebrew says likeness here, the Greek image; the Hebrew distinguishes “created” from “made,” the Greek says made twice."),
  'shared': ["This is the book of Adam’s generations.", "God created humankind.", "He made them in his likeness or image."],
  'instructions': [ins(K, S, "The human line descends from Adam, who was made in the likeness of God."), ins(W, R, "A list of births and deaths begins by recalling what every person in it is: made in God’s likeness.")],
  'entries': ['adam', 'god-theos'],
  'lost': [
   loses("Hebrew toledot adam, “generations of Adam,” becomes Greek biblos geneseōs anthrōpōn, “book of the origin of human beings”; Greek then names Adam separately. Hebrew demut, “likeness,” becomes Greek eikōn, “image,” and Hebrew bara, “created,” becomes “made.”"),
   keeps("Biblos geneseōs repeats 2:4 and anticipates Matthew 1:1, so the Greek reader hears the same heading over creation, Adam’s line and the Messiah’s."),
   between("Latin “book of Adam’s generations … in the likeness of God” and King James “generations of Adam … in the likeness of God” follow the Hebrew."),
  ]},

 '5:2': {
  'received': "God made them male and female, blessed them, and named them Adam on the day they were created.",
  'explain': ("The naming of 1:27–28 is recalled: male and female together are blessed and called Adam, the Hebrew word for "
   "humankind as well as the first man’s name. The plural “their name” shows the pair is meant. The versions agree, with the "
   "Greek saying “made” where the Hebrew says “created.”"),
  'shared': ["God made them male and female.", "He blessed them.", "He called their name Adam on the day of their creation."],
  'instructions': [ins(K, S, "Male and female together bear the name Adam and the blessing."), ins(W, R, "The blessing and the name belong to both; neither is given to the man alone.")],
  'entries': ['adam'],
  'lost': [
   between("Hebrew bara, “created,” is Greek epoiēsen, “made,” twice. Hebrew adam serves as both humankind and the name; Greek Adam is a name, so the plural “their name Adam” is more striking in Greek. Latin and King James keep “created.”"),
  ]},

 '5:3': birth('Adam', 'Seth', '130', '230',
   extra_explain="The son is begotten in Adam’s likeness and image, the words of verse 1 and of 1:26 turned toward a human father. The Hebrew says likeness and image; the Greek form and image.",
   extra_lost=[loses("Hebrew bi-demuto ke-tsalmo, “in his likeness, according to his image,” becomes Greek kata tēn idean autou kai kata tēn eikona autou, “according to his form and image.” Latin and King James keep likeness and image.")],
   wisdom="What God gave to Adam, Adam passes to his son; the image is inherited as well as given."),

 '5:4': after('Adam', 'Seth', '800', '700', '930'),

 '5:5': total('Adam', '930', "Adam’s 930 years are the same in every version, though the Greek divides them differently around Seth’s birth. The death first threatened in 2:17 is now recorded; Paul says death reigned from Adam.",
   extra_lost=[keeps("Greek kai apethanen, “and he died,” is the word of Romans 5:14. Justin Martyr noted that Adam died within a thousand years, reading 2:17 with Psalm 90:4.")]),

 '5:6': birth('Seth', 'Enosh', '105', '205'),
 '5:7': after('Seth', 'Enosh', '807', '707', '912'),
 '5:8': total('Seth', '912', "Seth’s total is the same in Greek and Hebrew; the differences of 5:6–7 lie in how the years are divided, and equal totals do not make the chronologies identical.", see="The King James also agrees after spelling is normalised."),

 '5:9': birth('Enosh', 'Kenan', '90', '190'),
 '5:10': after('Enosh', 'Kenan', '815', '715', '905'),
 '5:11': total('Enosh', '905', "Each life is summed as a count of days and then closed. The psalm of Moses measures ordinary human days at seventy or eighty years."),

 '5:12': birth('Kenan', 'Mahalalel', '70', '170',
   extra_explain="Mahalalel’s name is usually read as “praise of God”; Luke lists him in the line of Jesus."),
 '5:13': after('Kenan', 'Mahalalel', '840', '740', '910'),
 '5:14': total('Kenan', '910', "Kenan’s total agrees in all versions."),

 '5:15': birth('Mahalalel', 'Jared', '65', '165',
   extra_explain="Jared’s name is linked to the Hebrew verb for going down; the book of Jubilees ties it to heavenly watchers who came down in his days."),
 '5:16': after('Mahalalel', 'Jared', '830', '730', '895'),
 '5:17': total('Mahalalel', '895', "Mahalalel’s 895 years are the shortest of the long lives before Enoch, and the same in Greek and Hebrew."),

 '5:18': {
  'received': "Jared lived 162 years and became the father of Enoch.",
  'explain': ("For once the numbers agree. Jared is the one father in this list whose three figures are the same in Greek and "
   "Hebrew. His son is Enoch, the seventh from Adam in Seth’s line, as Jude notes, sharing his name with Cain’s son in 4:17."),
  'shared': ["Jared lived 162 years.", "He begat Enoch.", "Hebrew and Greek agree on the number."],
  'instructions': [ins(K, S, "Enoch, the seventh from Adam, was born to Jared.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James all give 162. Latin “fathered” and King James “begat” are English register only.")]},

 '5:19': {
  'received': "After Enoch’s birth Jared lived 800 years and had other sons and daughters.",
  'explain': ("The second line of Jared’s entry also agrees across the versions: 800 years after Enoch, with sons and daughters. "
   "Jared is the one father whose three figures, 162, 800 and 962, the Greek did not alter."),
  'shared': ["Jared lived on after Enoch was born.", "He lived 800 more years.", "He had other sons and daughters."],
  'instructions': [ins(K, S, "Jared had further children after Enoch.")],
  'entries': [],
  'lost': [between("All four versions give 800 years and the sons and daughters; there is no difference to record.")]},

 '5:20': total('Jared', '962', "Jared’s is the second longest life in Scripture, after his grandson Methuselah’s."),

 '5:21': birth('Enoch', 'Methuselah', '65', '165',
   extra_explain="Methuselah’s name is often read as “man of the dart,” or “man of Shelah”; Luke lists him in the line of Jesus."),

 '5:22': {
  'received': "After Methuselah’s birth Enoch lived in close fellowship with God for centuries and had other sons and daughters.",
  'explain': ("Enoch’s entry breaks the pattern. Where the others simply lived, Enoch “walked with God” in the Hebrew, Latin and "
   "King James, or “pleased God” in the Greek. The years differ too: three hundred in the Hebrew, two hundred in the Greek, "
   "fitting the chapter’s offsets. Hebrews follows the Greek wording when it says Enoch was attested to have pleased God."),
  'shared': ["Enoch lived in fellowship with God after Methuselah’s birth.", "He did so for hundreds of years.", "He had other sons and daughters."],
  'instructions': [ins(K, S, "Enoch walked with, or pleased, God for the rest of his life."), ins(W, R, "Walking with God and pleasing God are two names for one life; the Greek and Hebrew together describe it.")],
  'entries': [],
  'lost': [
   loses("Hebrew va-yithallekh Chanokh et-ha-Elohim, “Enoch walked with God,” is an image of companionship. Greek euērestēsen tō theō, “he pleased God,” gives the meaning without the walk. Hebrew 300 years becomes Greek 200."),
   keeps("Euērestēsen is the word of Hebrews 11:5–6, “he was attested to have pleased God … without faith it is impossible to please him.” The New Testament reads Enoch through the Greek."),
   between("Latin and King James keep “walked with God” and three hundred years with the Hebrew."),
  ]},

 '5:23': {
  'received': "All the days of Enoch were 365 years.",
  'explain': ("Enoch’s total is short by the chapter’s standards and the same in every version: 365, the number of days in a solar "
   "year. Later writings under his name dwell on the sun, moon and calendar. The formula stops here without “and he died,” the "
   "only entry in the chapter to do so."),
  'shared': ["Enoch’s days are summed.", "They came to 365 years.", "The verse does not say that he died."],
  'instructions': [ins(K, S, "Enoch’s life on earth was 365 years, and the usual notice of death is absent.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James all give 365 and all omit “and he died.”")]},

 '5:24': {
  'received': "Enoch walked with God and was no more, because God took him.",
  'explain': ("Enoch does not die; he is taken. The Hebrew says he walked with God and “was not,” for God took him. The Greek "
   "says he pleased God and “was not found,” because God transferred him. Neither names a destination. Hebrews quotes the "
   "Greek wording, and Sirach and Wisdom praise Enoch as taken up for pleasing God."),
  'shared': ["Enoch lived in fellowship with God.", "He disappeared from the earth.", "God took him."],
  'instructions': [ins(K, S, "Enoch was taken by God without the recorded death of the others."), ins(W, R, "A life that pleases God can end otherwise than the list expects; Enoch is the chapter’s sign of hope.")],
  'entries': [],
  'lost': [
   loses("Hebrew “walked with God” is again Greek “pleased God.” Hebrew ve-enennu, “and he was not,” becomes Greek ouch hēurisketo, “he was not found,” and Hebrew laqach, “took,” becomes metethēken, “transferred.”"),
   keeps("Ouch hēurisketo and metethēken are the words Hebrews 11:5 quotes: “he was not found, because God had translated him.” Sirach 44:16 and Wisdom of Solomon 4:10 praise Enoch in the same terms."),
   between("Latin “walked with God and was seen no more, because God took him” and King James “he was not; for God took him” keep the Hebrew."),
  ]},

 '5:25': {
  'received': "Methuselah lived 187 years in the Hebrew, 167 in the Greek, and became the father of Lamech.",
  'explain': ("Here the Greek goes the other way. Instead of adding a hundred years, it gives twenty fewer: 167 against the Hebrew "
   "187. With that figure Methuselah outlives the flood by fourteen years in the Greek reckoning, a problem Augustine discussed; "
   "the Hebrew and some Greek copies read 187. This Lamech, Noah’s father, shares his name with the boaster of Cain’s line."),
  'shared': ["Methuselah lived a set number of years before this son.", "He begat Lamech.", "The age given differs between the texts."],
  'instructions': [ins(K, S, "Lamech, Noah’s father, was born to Methuselah; the Greek and Hebrew ages differ.")],
  'entries': [],
  'lost': [
   loses("Hebrew 187 becomes Greek 167 in the main text consulted, twenty years fewer rather than a hundred more. The Hebrew figure keeps Methuselah’s death in the flood year; the Greek figure places it fourteen years after the flood."),
   keeps("The Greek 167 is the reading of the main text checked; other Greek witnesses read 187, so no agreement of all Greek copies is claimed."),
   between("Latin and King James give 187 with the Hebrew. Luke 3:36–37 lists Methuselah and this Lamech in the line of Jesus."),
  ]},

 '5:26': {
  'received': "After Lamech’s birth Methuselah lived on, 782 years in the Hebrew and 802 in the Greek, and had other sons and daughters.",
  'explain': ("The second line answers the first: the Hebrew 782 and the Greek 802 both bring Methuselah to 969. The chronological "
   "placement of his death still differs by twenty years. Sons and daughters close the formula as usual."),
  'shared': ["Methuselah lived on after Lamech was born.", "He had other sons and daughters.", "The years given differ between the texts."],
  'instructions': [ins(K, S, "Methuselah had further children after Lamech.")],
  'entries': [],
  'lost': [
   loses("Hebrew 782 years becomes Greek 802, twenty years more after the birth rather than a hundred fewer. Each pair sums to 969."),
   between("Latin and King James give 782 with the Hebrew."),
  ]},

 '5:27': total('Methuselah', '969', "Methuselah’s is the longest life recorded in Scripture, and the total is the same in Greek and Hebrew, though the twenty-year shift of 5:25–26 still moves his death relative to the flood. The Greek adds “which he lived.”"),

 '5:28': {
  'received': "Lamech lived 182 years in the Hebrew, 188 in the Greek, and became the father of a son.",
  'explain': ("The last father before Noah. The son is not yet named; the next verse names him with an explanation. The Hebrew, "
   "Latin and King James give Lamech 182 years at the birth; the Greek 188, a difference of six years rather than the chapter’s "
   "usual hundred."),
  'shared': ["Lamech lived a set number of years.", "He begat a son.", "The son is named in the next verse."],
  'instructions': [ins(K, S, "Noah was born to Lamech; the age given differs between the texts.")],
  'entries': ['noah'],
  'lost': [
   loses("Hebrew 182 years becomes Greek 188, six years more."),
   between("Latin and King James give 182 with the Hebrew."),
  ]},

 '5:29': {
  'received': "Lamech named him Noah, hoping he would bring relief from the toil of the cursed ground.",
  'explain': ("Noah’s name is explained by a hope. His father looks back to the curse of 3:17 and forward to relief. The Hebrew "
   "says Noah will comfort us in our work and painful toil; the Greek says he will give us rest from our works, from the pains "
   "of our hands and from the cursed earth. The Hebrew name sounds like the word for rest, and the Greek “rest” keeps closer to that sound than the Hebrew’s own “comfort.” Neither says Noah removes human sin."),
  'shared': ["Lamech named his son Noah.", "He expected relief from toil through him.", "He recalls the ground the Lord cursed."],
  'instructions': [ins(K, S, "Noah was named in hope of relief from the curse on the ground."), ins(W, R, "A child can be named for a hope the parents will not live to see fulfilled; Lamech’s hope reaches past the flood to Matthew 11:28.")],
  'entries': ['noah', 'yhwh-yahweh', 'lord-translation'],
  'lost': [
   loses("Hebrew yenachamenu, “he will comfort us,” explains Noach by a different root than nuach, “rest.” Greek dianapausei hēmas, “he will give us rest,” uses the rest word, and divides the sources of toil with a repeated apo, “from.” Hebrew YHWH is Greek “the Lord God.”"),
   keeps("The Greek reader hears Noah’s name explained by rest, which is what the name sounds like; the Hebrew hears comfort. Dianapausei anticipates the rest of 8:4 and the invitation of Matthew 11:28."),
   between("Latin “comfort us in our work and the toil of our hands upon the ground the Lord has cursed” and King James “comfort us concerning our work” follow the Hebrew."),
  ]},

 '5:30': {
  'received': "After Noah’s birth Lamech lived on, 595 years in the Hebrew and 565 in the Greek, and had other sons and daughters.",
  'explain': ("Unlike the earlier offsets, Lamech’s figures do not balance. The Hebrew 595 and the Greek 565 after Noah produce "
   "different totals in the next verse. Sons and daughters close the formula."),
  'shared': ["Lamech lived on after Noah was born.", "He had other sons and daughters.", "The years given differ between the texts."],
  'instructions': [ins(K, S, "Lamech had further children after Noah.")],
  'entries': [],
  'lost': [
   loses("Hebrew 595 years becomes Greek 565; with the six years of 5:28 the totals no longer agree."),
   between("Latin and King James give 595 with the Hebrew."),
  ]},

 '5:31': {
  'received': "All the days of Lamech were 777 years in the Hebrew, 753 in the Greek, and he died.",
  'explain': ("The one total in the chapter that differs. The Hebrew gives 777, a number built of sevens often set beside the "
   "seventy-sevenfold vengeance of the other Lamech in 4:24; the Greek gives 753. Each total matches its own preceding "
   "intervals. The Latin column runs Noah’s verse together with this one."),
  'shared': ["Lamech’s days are summed.", "He died.", "The total differs between the Hebrew and Greek texts."],
  'instructions': [ins(K, S, "Lamech died; his total differs between the Hebrew and the Greek.")],
  'entries': [],
  'lost': [
   loses("Hebrew 777 becomes Greek 753; the Hebrew’s pattern of sevens, which invites comparison with 4:24, is not in the Greek number."),
   between("Latin and King James give 777 with the Hebrew. The Latin column prints 5:31 and 5:32 as one passage."),
  ]},

 '5:32': {
  'received': "When Noah was five hundred years old he became the father of Shem, Ham and Japheth.",
  'explain': ("The chapter ends with Noah and the three sons through whom the world will be repeopled. Noah is five hundred, "
   "the oldest father in the list by far. The Greek adds “three sons” before the names. The summary does not require all three "
   "to be born in one year; compare 11:10. Shem means “name,” a word Babel’s builders will seek and God will promise to Abram."),
  'shared': ["Noah was five hundred years old.", "He begat Shem, Ham and Japheth.", "The line of Adam reaches the generation of the flood."],
  'instructions': [ins(K, S, "Noah’s three sons were born when he was five hundred."), ins(W, R, "The long list ends not with a death but with three births; the story of the flood opens from here.")],
  'entries': ['noah'],
  'lost': [
   keeps("Greek treis huious, “three sons,” is added before the names; the Hebrew gives the names only. The Greek makes the count explicit for the flood story and the table of nations."),
   between("Latin and King James give the names without the count; the Latin joins this verse to 5:31. Luke 3:36 lists Shem in the line of Jesus."),
  ]},
 }
}
