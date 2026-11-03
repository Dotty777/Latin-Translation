# Study prose for Genesis 11 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

def birth(name, son, heb, grk, extra=''):
    return {
     'received': f"{name} lived {heb} years in the Hebrew, {grk} in the Greek, and became the father of {son}.",
     'explain': (f"The formula of chapter 5 continues for Shem’s line, now without totals. The Hebrew, Latin and King James give {heb} years before {son}; "
       f"the Greek gives {grk}, adding a hundred as it did for most of the fathers before the flood, so that its chronology from the flood to Abram "
       f"runs several centuries longer. {extra}").strip(),
     'shared': [f"{name} lived a set number of years.", f"He begat {son}.", "The line from Shem continues."],
     'instructions': [ins(K, S, f"{son} was born to {name}; the age differs between the Hebrew and Greek texts.")],
     'entries': [],
     'lost': [
      loses(f"Hebrew {heb} years becomes Greek {grk}; the Hebrew interval is replaced and the cumulative chronology shifts by a century here."),
      between(f"Latin and King James give {heb} with the Hebrew.")]}

def after(name, son, heb, grk, extra=''):
    same = heb == grk
    return {
     'received': (f"After {son}’s birth {name} lived {heb} more years and had other sons and daughters." if same else
                  f"After {son}’s birth {name} lived on, {heb} years in the Hebrew and {grk} in the Greek, and had other sons and daughters."),
     'explain': ((f"The years after the named son agree in every version, {heb}. " if same else
                  f"The Hebrew, Latin and King James give {heb} years after {son}; the Greek gives {grk}. ") +
                 "Unlike chapter 5, no total is given for these fathers, and the Hebrew does not say that they died; the Greek adds “and he died” to each entry, "
                 f"completing the pattern of the earlier chapter. {extra}").strip(),
     'shared': [f"{name} lived on after {son} was born.", "He had other sons and daughters.", "Only the one son in the line is named."],
     'instructions': [ins(K, S, f"{name} had further children after {son}.")],
     'entries': [],
     'lost': ([] if same else [loses(f"Hebrew {heb} years after {son} becomes Greek {grk}.")]) + [
      keeps("An added kai apethanen, “and he died,” which the Hebrew omits throughout this genealogy; the Greek carries the refrain of chapter 5 into chapter 11."),
      between(f"Latin and King James give {heb} with the Hebrew and, like it, no death notice.")]}

CHAPTER = {
 'slug': 'genesis', 'chapter': 11,
 'chapterNote': (
  "Babel, the line of Shem and the household of Terah are told alike in every column. What varies is the frame of the tower story and "
  "the years of the genealogy. The Hebrew keeps “lest we be scattered” as the builders’ motive, the name Babel with its pun on confusion, "
  "a city only in 11:8, the short ages at fatherhood (Arpachshad 35, Shelah 30, Eber 34 …), no death notices, Ur of the Chaldeans, and "
  "“they went out” in 11:31. The Greek keeps “before we are scattered” as a sequence, the name translated as Confusion, “the city and the "
  "tower,” a hundred more years before most births with Cainan inserted between Arpachshad and Shelah, “and he died” for each father, "
  "“the country of the Chaldeans” without Ur, Terah as the one who led them out, and Terah’s years “in Haran.” The Latin and King James "
  "follow the Hebrew; Luke’s genealogy and Stephen’s speech in Acts follow the Greek."),
 'verses': {

 '11:1': {
  'received': "The whole earth had one language and the same speech.",
  'explain': ("Before the scattering, unity: one language for everyone. The Hebrew says one language and the same words; the Greek one "
   "language and one voice for all, an image of collective speech. Both set up the confusion that follows. The one tongue is not yet "
   "called a blessing or a danger; it is simply the state of things."),
  'shared': ["The whole earth had one language.", "All people shared the same speech.", "This was the state before Babel."],
  'instructions': [ins(K, S, "Humankind once shared a single language.")],
  'entries': [],
  'lost': [between("Hebrew devarim achadim, “the same words,” is Greek phōnē mia pasin, “one voice to all”; Latin “the same words” and King James “one speech” follow the Hebrew. Both describe shared speech, not identical sound.")]},

 '11:2': {
  'received': "Journeying from the east, the people found a plain in the land of Shinar and settled there.",
  'explain': ("The migration ends on the plain of Shinar, the southern Mesopotamia of Nimrod’s kingdom in 10:10, where Daniel will later "
   "see the temple vessels carried and Zechariah will see wickedness housed. They settle rather than spread. All versions agree."),
  'shared': ["The people journeyed from the east.", "They found a plain in the land of Shinar.", "They settled there."],
  'instructions': [ins(K, S, "Humankind settled on the plain of Shinar."), ins(W, R, "Settling in one place against the command to fill the earth is the quiet beginning of the tower.")],
  'entries': ['babylon'],
  'lost': [between("Hebrew, Greek, Latin and King James agree word for word in sense; Hebrew mi-qedem, “from the east,” is Greek apo anatolōn. Zechariah 5:11 and Daniel 1:2 return to Shinar.")]},

 '11:3': {
  'received': "They resolved to make bricks and bake them, using brick for stone and bitumen for mortar.",
  'explain': ("The first step is technology. With no stone on the alluvial plain, they make bricks and bind them with bitumen. The Hebrew "
   "says burn them thoroughly; the Greek bake them with fire. Israel will later be forced to make bricks in Egypt. The materials are the "
   "same in all versions."),
  'shared': ["They said to one another, Come, let us make bricks.", "They baked the bricks.", "They used brick for stone and bitumen for mortar."],
  'instructions': [ins(K, S, "The builders of Babel used baked brick and bitumen."), ins(W, R, "Human invention is not the sin; the bricks are neutral until the next verse says what they are for.")],
  'entries': [],
  'lost': [between("Hebrew nisrefah li-serefah, “let us burn them to a burning,” an emphatic doubling, is Greek optēsōmen autas pyri, “let us bake them with fire.” Latin follows the Greek fire; King James “burn them thoroughly” the Hebrew. Hebrew chemar, “bitumen,” is King James “slime.” Exodus 1:14 recalls the bricks.")]},

 '11:4': {
  'received': "They planned a city and a tower reaching to heaven, to make a name for themselves and avoid being scattered.",
  'explain': ("The purpose is spoken: a city, a tower with its top in the heavens, and a name. Babylon’s stepped temple towers were meant "
   "as meeting points of heaven and earth. The Hebrew gives the motive as prevention, lest we be scattered; the Greek and Latin as "
   "sequence, before we are scattered. In the next chapter God will promise Abram the great name these builders tried to make for themselves."),
  'shared': ["They said, Come, let us build a city and a tower.", "The tower was to reach to heaven.", "They wanted to make a name for themselves, with scattering in view."],
  'instructions': [ins(K, S, "The builders of Babel sought a name for themselves and a tower to heaven."), ins(W, R, "A name made for oneself and a name given by God are the two roads out of this verse; Abram will take the second.")],
  'entries': ['babylon'],
  'lost': [
   loses("Hebrew pen-nafuts, “lest we be scattered,” gives the builders a defensive motive. Greek pro tou diasparēnai hēmas, “before we are scattered,” turns the motive into a point in time, as if the scattering were expected. The Hebrew’s purpose clause is gone."),
   between("Latin “before we are scattered throughout all lands” follows the Greek; King James “lest we be scattered abroad” the Hebrew. Greek pyrgos, “tower,” and onoma, “name,” point to 28:12 and 12:2."),
  ]},

 '11:5': {
  'received': "The Lord came down to see the city and the tower the people had built.",
  'explain': ("The tower meant to reach heaven is so small that God must come down to see it; the irony is in every version. The Hebrew says "
   "YHWH came down; the Greek the Lord; the Latin names the builders Adam’s children. God will come down again to rescue Israel from Egypt."),
  'shared': ["The Lord came down.", "He came to see the city and the tower.", "The human beings had built them."],
  'instructions': [ins(K, S, "God came down to inspect the tower of Babel."), ins(W, R, "What looks tall from below is small from above; the verse measures human pride by God’s descent.")],
  'entries': ['yhwh-yahweh', 'lord-translation'],
  'lost': [between("Hebrew bene ha-adam, “the sons of man,” is Greek hoi huioi tōn anthrōpōn, “the human beings,” and Latin filii Adam, “Adam’s children”; King James “children of men.” Hebrew YHWH is Greek kyrios. Exodus 3:8 and 19:20 bring God down again.")]},

 '11:6': {
  'received': "The Lord observed that one people with one language had begun this, and nothing they planned would be beyond them.",
  'explain': ("God names the danger: unity of people and language has made this possible, and nothing they plan will be out of reach. The "
   "Hebrew says nothing will be withheld from them; the Greek nothing they undertake will fail them; the Latin that they will not abandon "
   "their plans until done. The word for people, Hebrew am and Greek genos, carries no modern racial sense."),
  'shared': ["They are one people with one language.", "This is what they have begun to do.", "Nothing they plan will be beyond them."],
  'instructions': [ins(K, S, "God saw that united humankind could accomplish whatever it planned."), ins(W, R, "Unity is a power, and power without God’s purpose is the thing God moves to limit.")],
  'entries': ['yhwh-yahweh', 'lord-translation'],
  'lost': [between("Hebrew lo-yibbatser mehem, “will not be withheld from them,” is Greek ouk ekleipsei ex autōn, “will not fail them”; Latin “they will not abandon their plans until they accomplish them” paraphrases; King James “nothing will be restrained from them” follows the Hebrew. Greek genos hen, “one people,” is the word of 1 Peter 2:9.")]},

 '11:7': {
  'received': "God resolved to go down and confuse their language so that they would not understand one another.",
  'explain': ("God answers the builders’ “Come, let us” with his own. The plural deliberation echoes 1:26 and 3:22. The remedy is "
   "confusion of language: the Hebrew says they will not understand one another’s language; the Greek each will not understand his "
   "neighbour’s voice. The verb in both is “hear,” which here means understand."),
  'shared': ["God says, Come, let us go down.", "He will confuse their language there.", "They will not understand one another."],
  'instructions': [ins(K, S, "God confused the language of Babel so that the builders could not understand each other."), ins(W, R, "The remedy for a proud unity is a confusion that forces dispersal; the scattering the builders feared is the cure.")],
  'entries': [],
  'lost': [between("Hebrew sefat re‘ehu, “his neighbour’s language,” is Greek tēn phōnēn tou plēsion, “the neighbour’s voice”; Hebrew lo yishme‘u and Greek mē akousōsin are both “not hear,” meaning not understand. Latin and King James agree. The plural “let us” is in all four, as at 1:26 and 3:22.")]},

 '11:8': {
  'received': "The Lord scattered them over all the earth, and they stopped building.",
  'explain': ("What the builders feared in verse 4 happens: the Lord scatters them. They leave the work unfinished. The Hebrew says they "
   "stopped building the city; the Greek adds the tower, naming both parts of the project from verse 4. The addition does not mean the "
   "Hebrew story lacked a tower. Mary sings that God has scattered the proud."),
  'shared': ["The Lord scattered them from there.", "They were scattered over all the earth.", "They stopped building."],
  'instructions': [ins(K, S, "God scattered the builders and ended the work at Babel."), ins(W, R, "An unfinished tower is the monument of Babel; what is built against God is left half-made.")],
  'entries': ['yhwh-yahweh', 'lord-translation'],
  'lost': [
   keeps("An added kai ton pyrgon, “and the tower,” to the abandoned work; the Hebrew says “the city” only. The Greek names both parts of the project of 11:4."),
   between("Latin “stopped building the city” and King James “left off to build the city” follow the Hebrew. Luke 1:51 and Deuteronomy 32:8 look back on the scattering."),
  ]},

 '11:9': {
  'received': "The place was named Babel, because there the Lord confused the language of all the earth and scattered the people.",
  'explain': ("The name is explained by a Hebrew pun: Bavel sounds like balal, to confuse. The Greek translates the name outright, "
   "Confusion, so that the Greek reader hears the meaning and not the name; the Hebrew, Latin and King James keep Babel. The Babylonians "
   "themselves explained the name as “gate of god.” The Greek has the Lord God in the final clause where the Hebrew repeats YHWH."),
  'shared': ["The place was given a name.", "The name is explained by the confusion of language there.", "From there the Lord scattered them over all the earth."],
  'instructions': [ins(K, S, "Babel is named for the confusion of languages."), ins(W, R, "The city of the great name is remembered by a name that means confusion; pride renames itself.")],
  'entries': ['babylon', 'yhwh-yahweh', 'lord-translation'],
  'lost': [
   loses("Hebrew Bavel, with its echo of balal, “confused,” is a name and a pun. Greek Synchysis, “Confusion,” is a translation; the name Babel is not in the Greek verse. Hebrew YHWH … YHWH becomes Greek kyrios … kyrios ho theos."),
   between("Latin Babel and King James Babel keep the name; the Latin makes the confusing passive, “was confused.” Genesis 10:10 and Revelation 18:2 carry Babylon on."),
  ]},

 '11:10': {
  'received': "Shem was a hundred years old when he became the father of Arpachshad, two years after the flood.",
  'explain': ("A new heading begins Shem’s line, which will lead to Abram. Shem is a hundred two years after the flood, although Noah was "
   "five hundred at 5:32 and six hundred at the flood; 5:32 most likely marks when Noah began to have sons. The Hebrew says two years "
   "after the flood, the Greek in the second year. Arpachshad is the Hebrew form; Arphaxad the Greek."),
  'shared': ["These are the generations of Shem.", "Shem was a hundred years old when he begat Arpachshad.", "It was two years after the flood."],
  'instructions': [ins(K, S, "Shem’s line, which leads to Abram, began two years after the flood.")],
  'entries': [],
  'lost': [between("Hebrew shenatayim achar ha-mabbul, “two years after the flood,” is Greek deuterou etous meta ton kataklysmon, “in the second year after the flood.” Hebrew Arpakhshad is Greek Arphaxad. Latin and King James follow the Hebrew phrasing.")]},

 '11:11': after('Shem', 'Arpachshad', '500', '500', extra="Shem’s is the one entry in this list whose figures agree in every column."),

 '11:12': {
  'received': "Arpachshad lived 35 years in the Hebrew, 135 in the Greek, and became the father of Shelah, or, in the Greek, of Cainan.",
  'explain': ("Here the two texts part most sharply. The Hebrew, Latin and King James have Arpachshad father Shelah at thirty-five. The "
   "Greek has him father Cainan at a hundred and thirty-five, adding both a century and a generation, the Cainan already seen in 10:24. "
   "Luke’s genealogy of Jesus includes Cainan, son of Arphaxad, following the Greek."),
  'shared': ["Arpachshad lived a set number of years.", "He begat a son.", "The line continues toward Eber."],
  'instructions': [ins(K, S, "The line from Arpachshad continues; the Greek adds a generation, Cainan, that the Hebrew lacks.")],
  'entries': [],
  'lost': [
   loses("Hebrew chamesh u-sheloshim, “thirty-five,” and Shelach, “Shelah,” become Greek hekaton triakonta pente, “a hundred and thirty-five,” and Kainan, “Cainan.” The Hebrew number and the Hebrew son are both replaced in this verse."),
   keeps("The Greek Cainan is the generation of Luke 3:36, “Shelah, son of Cainan, son of Arphaxad”; the New Testament genealogy follows the Greek here."),
   between("Latin and King James give thirty-five and Shelah with the Hebrew."),
  ]},

 '11:13': {
  'received': "Arpachshad lived on after his son’s birth and had other sons and daughters; in the Greek, Cainan’s whole entry follows.",
  'explain': ("The Hebrew gives Arpachshad 403 years after Shelah, with sons and daughters; the Latin 303. The Greek gives him 430 years "
   "after Cainan, adds his death, and then supplies Cainan’s complete entry: 130 years to Shelah, 330 after, sons and daughters, and "
   "death. Cainan’s entry exists only in the Greek, and from there in Luke."),
  'shared': ["Arpachshad lived on after his named son.", "He had other sons and daughters.", "The line continues to Shelah."],
  'instructions': [ins(K, S, "Arpachshad had further children; the Greek inserts Cainan’s generation between him and Shelah.")],
  'entries': [],
  'lost': [
   loses("Hebrew 403 years after Shelah becomes Greek 430 years after Cainan. The Hebrew verse is one sentence; the Greek is three, with “and he died” twice."),
   keeps("An added Kainan ezēsen hekaton triakonta etē kai egennēsen ton Sala … triakosia triakonta etē … kai apethanen, Cainan’s full entry, which the Hebrew does not have anywhere. Luke 3:36 includes him."),
   between("Latin gives 303 years, differing from both Hebrew 403 and Greek 430; King James gives 403 with the Hebrew. Neither has Cainan."),
  ]},

 '11:14': birth('Shelah', 'Eber', '30', '130'),
 '11:15': after('Shelah', 'Eber', '403', '330', extra="Here the two texts differ by more than the usual hundred."),
 '11:16': birth('Eber', 'Peleg', '34', '134', extra="Eber is the ancestor from whom the Hebrews take their name."),
 '11:17': after('Eber', 'Peleg', '430', '370', extra="Greek copies themselves vary at this number."),
 '11:18': birth('Peleg', 'Reu', '30', '130', extra="Peleg’s name, “division,” was explained in 10:25."),
 '11:19': after('Peleg', 'Reu', '209', '209', extra="For Peleg, Reu and Serug the years after the son’s birth match the Hebrew exactly."),
 '11:20': birth('Reu', 'Serug', '32', '132', extra="Luke lists Serug in the line of Jesus; a town called Sarugi near Haran appears in Assyrian records."),
 '11:21': after('Reu', 'Serug', '207', '207', extra="Reu’s whole life is 339 years in the Greek and 239 in the Hebrew; spans shorten sharply after the flood."),
 '11:22': birth('Serug', 'Nahor', '30', '130', extra="Nahor is Abram’s grandfather; the name will pass to Abram’s brother in 11:26."),
 '11:23': after('Serug', 'Nahor', '200', '200', extra="Serug’s whole life is 330 years in the Greek and 230 in the Hebrew."),

 '11:24': {
  'received': "Nahor lived 29 years in the Hebrew, 79 in the Greek, and became the father of Terah.",
  'explain': ("The last father before Terah. The Hebrew, Latin and King James give Nahor twenty-nine years at Terah’s birth; the Greek "
   "seventy-nine, adding fifty rather than the usual hundred. Nahor’s is the shortest life in the list in either text."),
  'shared': ["Nahor lived a set number of years.", "He begat Terah.", "The line reaches Abram’s father."],
  'instructions': [ins(K, S, "Terah, Abram’s father, was born to Nahor; the age differs between the texts.")],
  'entries': [],
  'lost': [
   loses("Hebrew tesha ve-esrim, “twenty-nine,” becomes Greek hebdomēkonta ennea, “seventy-nine,” fifty years more."),
   between("Latin and King James give twenty-nine with the Hebrew."),
  ]},

 '11:25': {
  'received': "After Terah’s birth Nahor lived on, 119 years in the Hebrew and 129 in the Greek, and had other sons and daughters.",
  'explain': ("The Hebrew, Latin and King James give Nahor 119 years after Terah; the Greek 129, and adds his death. Nahor lives 148 years "
   "in the Hebrew and 208 in the Greek, a third of Shem’s six hundred. The long lives are ending."),
  'shared': ["Nahor lived on after Terah was born.", "He had other sons and daughters.", "His life was far shorter than Shem’s."],
  'instructions': [ins(K, S, "Nahor had further children after Terah.")],
  'entries': [],
  'lost': [
   loses("Hebrew 119 years becomes Greek 129."),
   keeps("An added kai apethanen, “and he died,” as throughout this list."),
   between("Latin and King James give 119 with the Hebrew and no death notice."),
  ]},

 '11:26': {
  'received': "Terah lived seventy years and became the father of Abram, Nahor and Haran.",
  'explain': ("The list ends with three sons, as chapter 5 ended with Noah’s three. Abram’s name means exalted father; God will rename "
   "him Abraham, father of many nations. All versions agree exactly. As at 5:32, the age need not mean all three were born in one year."),
  'shared': ["Terah lived seventy years.", "He begat Abram, Nahor and Haran.", "The genealogy of Shem ends with Abram."],
  'instructions': [ins(K, S, "Abram was one of the three sons of Terah."), ins(W, R, "The line that began with Shem’s blessing arrives at Abram; the story is about to narrow to one man.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew, Greek, Latin and King James agree, the King James after normalising spelling. Greek Abram is Hebrew Avram; Genesis 17:5 and Romans 4:17 give the new name.")]},

 '11:27': {
  'received': "These are the generations of Terah: he had Abram, Nahor and Haran, and Haran had Lot.",
  'explain': ("A new heading opens the story of Abraham, which runs to his death in 25:11. The three sons are named again and Lot is "
   "introduced, the nephew who will travel with Abram and be rescued from Sodom. All versions agree."),
  'shared': ["These are the generations of Terah.", "Terah begat Abram, Nahor and Haran.", "Haran begat Lot."],
  'instructions': [ins(K, S, "Lot was Abram’s nephew, the son of his brother Haran.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew, Greek, Latin and King James agree. Greek geneseis Thara, “generations of Terah,” is the heading word of 6:9; 2 Peter 2:7 calls Lot righteous.")]},

 '11:28': {
  'received': "Haran died during his father Terah’s lifetime, in his native land of the Chaldeans.",
  'explain': ("Haran dies before his father, in the land of his birth. The Hebrew, Latin and King James name the city, Ur of the Chaldeans; "
   "the Greek says the country of the Chaldeans without naming Ur, the wording Stephen uses in Acts. “In the presence of his father” "
   "means during his father’s lifetime."),
  'shared': ["Haran died.", "He died during his father Terah’s lifetime.", "He died in the land of his birth, among the Chaldeans."],
  'instructions': [ins(K, S, "Haran died young, in his father’s lifetime, in the land of the Chaldeans."), ins(W, R, "The family story begins with a death out of order; Lot is fatherless before the journey starts.")],
  'entries': ['ur'],
  'lost': [
   loses("Hebrew be-Ur Kasdim, “in Ur of the Chaldeans,” names the city; Greek en tē chōra tōn Chaldaiōn, “in the country of the Chaldeans,” does not. The name Ur is absent from the Greek here and in 11:31."),
   keeps("The Greek wording is the one Stephen uses in Acts 7:4, “the land of the Chaldeans.”"),
   between("Latin and King James name Ur with the Hebrew. Genesis 15:7 and Nehemiah 9:7 recall the bringing out."),
  ]},

 '11:29': {
  'received': "Abram and Nahor married: Abram’s wife was Sarai, and Nahor’s was Milcah, daughter of Haran, who was also father of Iscah.",
  'explain': ("The two surviving brothers marry. Sarai is introduced without parentage; Milcah is Haran’s daughter, so Nahor married his "
   "niece, and through her will come Rebekah. Milcah’s name means queen. Iscah is named and never heard of again; later tradition "
   "identified her with Sarai. All versions agree."),
  'shared': ["Abram and Nahor took wives.", "Abram’s wife was Sarai.", "Nahor’s wife was Milcah, daughter of Haran, who was also the father of Iscah."],
  'instructions': [ins(K, S, "Sarai was Abram’s wife and Milcah was Nahor’s.")],
  'entries': ['abraham', 'sarah'],
  'lost': [between("Hebrew, Greek, Latin and King James agree. Greek Melcha is Hebrew Milkah; Genesis 22:23 and 24:15 bring Rebekah from her line.")]},

 '11:30': {
  'received': "Sarai was barren and had no child.",
  'explain': ("One sentence that shapes the next fourteen chapters. Sarai is the first of the barren wives whose children are gifts of "
   "God: Sarah, Rebekah, Rachel, Hannah, Elizabeth. The Hebrew says she had no child; the Greek that she bore none. The promise to "
   "Abram will be made to a man whose wife cannot conceive."),
  'shared': ["Sarai was barren.", "She had no child.", "Her childlessness is stated before the promise."],
  'instructions': [ins(K, S, "Sarai was barren when the story of Abram began."), ins(W, R, "God’s promise begins where human possibility ends; the barren wife is the first condition of the covenant.")],
  'entries': ['sarah'],
  'lost': [between("Hebrew ein lah valad, “she had no child,” is Greek ouk eteknopoiei, “she bore no children.” Latin and King James follow the Hebrew. Greek steira, “barren,” is the word of Luke 1:7 and Galatians 4:27.")]},

 '11:31': {
  'received': "Terah took Abram, Lot and Sarai out of the land of the Chaldeans toward Canaan, and they settled at Haran.",
  'explain': ("The family leaves for Canaan but stops halfway. The Hebrew says they went out from Ur of the Chaldeans with a difficult "
   "“with them,” and uses plural verbs; the Greek makes Terah the leader, “he led them out,” and continues in the singular, “he came as "
   "far as Haran and settled.” The Greek again says the country of the Chaldeans without Ur. Haran the city shares its name in English, not in Hebrew, with Haran the brother."),
  'shared': ["Terah took Abram, Lot and Sarai.", "They left the land of the Chaldeans to go to Canaan.", "They came to Haran and settled there."],
  'instructions': [ins(K, S, "Terah led his family from Ur toward Canaan and settled at Haran."), ins(W, R, "A journey begun toward the promised land stops short; Terah settles where Abram will have to be called again.")],
  'entries': ['abraham', 'sarah', 'ur', 'haran', 'canaan'],
  'lost': [
   loses("Hebrew va-yetse’u ittam me-Ur Kasdim, “they went out with them from Ur of the Chaldeans,” names Ur and has plural verbs; Greek exēgagen autous ek tēs chōras tōn Chaldaiōn, “he led them out of the country of the Chaldeans,” drops Ur and makes Terah the subject, continuing “he came … he settled.”"),
   keeps("The Greek clears up the difficult Hebrew “with them” by keeping Terah as leader throughout; the Hebrew leaves the relationships implicit."),
   between("Latin “led them out of Ur of the Chaldeans … they came as far as Haran” stands between, Terah leading but Ur named and the arrival plural; King James follows the Hebrew."),
  ]},

 '11:32': {
  'received': "Terah lived two hundred and five years and died in Haran.",
  'explain': ("Terah’s entry closes in Haran. All versions give two hundred and five years; the Greek attaches “in Haran” to the days as "
   "well as to the death. The Samaritan text gives 145, which fits Stephen’s statement in Acts that Abram left Haran after his father’s "
   "death (70 plus 75). The way is clear for the call of chapter 12."),
  'shared': ["Terah’s days were two hundred and five years.", "He died.", "He died in Haran."],
  'instructions': [ins(K, S, "Terah died in Haran at two hundred and five."), ins(W, R, "The father dies in the halfway place; the son will be the one to finish the journey.")],
  'entries': ['haran'],
  'lost': [
   keeps("Greek hai hēmerai Thara en Charran, “the days of Terah in Haran,” adds the place to the lifespan; the Hebrew says only “the days of Terah were two hundred and five years.”"),
   between("Latin and King James follow the Hebrew. Acts 7:4 and Genesis 12:4 raise the chronological question the Samaritan 145 would answer."),
  ]},
 }
}
