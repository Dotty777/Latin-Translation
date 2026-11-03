# Study prose for Genesis 22 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 22,
 'chapterNote': (
  "The testing of Abraham, the binding of Isaac, the ram and the oath are the same story in every column. What varies is in the words for the son and "
  "the place. The Hebrew keeps “your only one,” the land of Moriah, “here I am, my son,” a sheep or goat for the offering, a ram “behind him” in the thicket, "
  "the name “YHWH will see” with a difficult proverb, “the gate of their enemies,” and “bless themselves.” The Greek keeps “your beloved,” the “high land,” "
  "“what is it, child,” a sheep, Isaac’s feet bound together, “one ram” in a sabek plant with Isaac named at the offering, “the Lord saw … on the mountain the "
  "Lord appeared,” “the cities of their adversaries,” “be blessed,” and Beersheba translated as the Well of the Oath. The Latin has “only-begotten,” the “land "
  "of vision,” and Abraham rising in the night; the King James follows the Hebrew."),
 'verses': {

 '22:1': {
  'received': "After these things God tested Abraham, calling his name, and Abraham answered, Here I am.",
  'explain': ("The chapter announces itself as a test, so the reader knows what Abraham does not. God calls and Abraham answers with the word of a "
   "servant ready to be sent, which he will say again to Isaac and to the angel. The Hebrew has God call once; the Greek and Latin twice, as all the "
   "versions do in verse 11. The King James “tempt” is old English for test."),
  'shared': ["After these things God tested Abraham.", "God called him by name.", "Abraham answered, Here I am."],
  'instructions': [ins(K, S, "God put Abraham to the test."), ins(W, R, "“Here I am” is said before the command is heard; readiness precedes knowledge of the cost.")],
  'entries': ['abraham', 'god-theos'],
  'lost': [
   keeps("Greek doubles the call, Abraam, Abraam, where the Hebrew has it once; the Hebrew doubles it only at 22:11. Hebrew nissah, “tested,” is Greek epeirazen."),
   between("Latin “Abraham, Abraham” follows the Greek; King James “Abraham” follows the Hebrew and renders the verb “tempt.” Hebrews 11:17 and James 2:21 read the test."),
  ]},

 '22:2': {
  'received': "God told Abraham to take his beloved only son Isaac to the land of Moriah and offer him as a burnt offering on a mountain he would show him.",
  'explain': ("The command is built to wound: your son, your only one, whom you love, Isaac, each word closer than the last, as in 12:1. The Hebrew says "
   "your only one; the Greek your beloved, the word the Gospels use at the baptism; the Latin only-begotten. The place is the land of Moriah in the "
   "Hebrew, the high land in the Greek, the land of vision in the Latin. The offering is to be wholly burned."),
  'shared': ["God told Abraham to take his son Isaac, whom he loves.", "He was to go to a land God named.", "He was to offer him as a burnt offering on a mountain God would show."],
  'instructions': [ins(C, S, "Take your son Isaac and offer him as a burnt offering on the mountain I will show you."), ins(W, R, "The promise and the command stand against each other; Abraham is asked to give back the only thing the promise had given.")],
  'entries': ['abraham', 'isaac'],
  'lost': [
   loses("Hebrew yechidekha, “your only one,” becomes Greek ton agapēton, “your beloved”; Hebrew erets ha-Moriyah, “the land of Moriah,” a name, becomes Greek tēn gēn tēn hypsēlēn, “the high land,” a description; Hebrew lekh-lekha, “go for yourself,” is Greek poreuthēti. The name Moriah is gone."),
   keeps("Greek agapētos, “beloved,” is the word of Matthew 3:17 and Mark 12:6; the Greek reader hears the beloved son of the Gospels on the mountain. The Greek also keeps “whom you love.”"),
   between("Latin “your only-begotten son … the land of vision” reads Moriah from the root of seeing; King James “thine only son Isaac … the land of Moriah” follows the Hebrew. 2 Chronicles 3:1 places the temple on Moriah."),
  ]},

 '22:3': {
  'received': "Abraham rose early, saddled his donkey, took two servants and Isaac, split the wood, and set out for the place God had named.",
  'explain': ("Obedience is told in verbs, without a word of feeling: rose, saddled, took, split, went. The Hebrew says early in the morning; the Latin "
   "in the night; the Greek in the morning and adds that he came to the place, anticipating verse 9. The Greek marks the donkey as female; the two "
   "servants are young men in the Hebrew, attendants in the Greek."),
  'shared': ["Abraham rose early and saddled his donkey.", "He took two servants and his son Isaac.", "He split wood for the offering and set out for the place God had told him."],
  'instructions': [ins(K, S, "Abraham obeyed at once, preparing everything for the sacrifice himself."), ins(W, R, "He splits the wood with his own hands; the obedience is told in chores, and the silence about his heart is the loudest thing in the verse.")],
  'entries': ['abraham', 'isaac'],
  'lost': [
   keeps("Greek adds kai ēlthen, “and came,” to the setting out, and marks the donkey as tēn onon, feminine; Hebrew va-yelekh el-ha-maqom, “went toward the place.” Hebrew ne‘arav, “his young men,” is Greek paidas, “attendants.”"),
   between("Latin “rose in the night” differs from Hebrew ba-boqer, “in the morning”; King James “rose up early in the morning … two of his young men” follows the Hebrew."),
  ]},

 '22:4': {
  'received': "On the third day Abraham saw the place in the distance.",
  'explain': ("Three days of travel, unrecorded, and then the sight of the mountain. The third day will become the Bible’s day of deliverance. The "
   "versions agree; the Latin says he for Abraham."),
  'shared': ["It was the third day.", "Abraham raised his eyes.", "He saw the place from a distance."],
  'instructions': [ins(K, S, "Abraham reached sight of the mountain on the third day."), ins(W, R, "Three days of walking toward the unthinkable; the test is as much the journey as the knife.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew, Greek and King James agree; the Latin says “he raised his eyes.” Hebrew me-rachoq, “from afar,” is Greek makrothen.")]},

 '22:5': {
  'received': "Abraham told the servants to wait with the donkey while he and the boy went to worship and return.",
  'explain': ("Abraham speaks of return in the plural: we will worship and come back to you. Whether faith or concealment, the words are kept in every "
   "version; Hebrews reads them as faith in resurrection. The Hebrew says young men and the boy; the Greek attendants and the boy; the Latin servants "
   "and after we have worshipped."),
  'shared': ["Abraham told his servants to stay with the donkey.", "He and the boy would go on to worship.", "They would return to the servants."],
  'instructions': [ins(K, S, "Abraham left the servants and went on alone with Isaac, speaking of return."), ins(W, R, "“We will return” is either faith or a father’s evasion; Hebrews chooses faith, and the plural stands in every text.")],
  'entries': ['abraham', 'isaac'],
  'lost': [between("Hebrew ne‘arav, “his young men,” is Greek tois paisin autou, “his attendants”; Hebrew ha-na‘ar, “the boy,” is Greek to paidarion. The plural “we will return” is in all four. Hebrews 11:19 reads it.")]},

 '22:6': {
  'received': "Abraham laid the wood on Isaac, carried the fire and knife himself, and the two walked on together.",
  'explain': ("The son carries the wood of his own sacrifice; the father carries the fire and the knife. The two go together, a phrase repeated in verse 8 "
   "that became the hinge of Christian reading of the chapter. The versions agree; the Latin runs the sentence into the next verse."),
  'shared': ["Abraham laid the wood on his son Isaac.", "He took the fire and the knife in his hand.", "The two went together."],
  'instructions': [ins(K, S, "Isaac carried the wood and Abraham the fire and knife."), ins(W, R, "The son bearing the wood up the hill is the picture the church saw of another Son; the text gives the picture without comment.")],
  'entries': ['abraham', 'isaac'],
  'lost': [between("Hebrew va-yelekhu sheneihem yachdav, “and the two of them went together,” is Greek kai eporeuthēsan hoi dyo hama; Latin “as the two walked together” continues into 22:7. King James follows the Hebrew.")]},

 '22:7': {
  'received': "Isaac asked his father where the animal for the offering was, since they had fire and wood.",
  'explain': ("The only words Isaac speaks. He calls, my father; Abraham answers, here I am, my son, the same words he gave God; Isaac asks where the "
   "animal is. The Hebrew word covers sheep or goat; the Greek says sheep; the Latin victim. The Greek answer is what is it, child, instead of here I am."),
  'shared': ["Isaac spoke to his father.", "Abraham answered him.", "Isaac asked where the animal for the burnt offering was, since they had fire and wood."],
  'instructions': [ins(K, S, "Isaac noticed that no animal had been brought."), ins(W, R, "The child sees what is missing and asks; the father’s “here I am” to his son is the same word he gave to God, and it costs more.")],
  'entries': ['isaac', 'abraham'],
  'lost': [
   loses("Hebrew hinneni veni, “here I am, my son,” becomes Greek ti estin, teknon, “what is it, child”; Hebrew ha-seh, “the sheep or goat,” becomes Greek to probaton, “the sheep.” Hebrew avi, “my father,” is Greek pater, “father.”"),
   between("Latin “what is it, son? … the victim” follows the Greek question and its own noun; King James “here am I, my son … the lamb” follows the Hebrew answer and reads the animal as a lamb."),
  ]},

 '22:8': {
  'received': "Abraham answered that God would provide the animal, and the two went on together.",
  'explain': ("Abraham’s answer is true in a way he cannot know: God will see to it, provide for himself, the animal. The Hebrew verb is see, used of "
   "provision, and it gives the place its name in verse 14. The Hebrew and Greek do not say God will provide himself as the animal, though Christian "
   "readers heard it. The refrain returns: the two went together."),
  'shared': ["Abraham said God would provide the animal for the offering.", "He called Isaac his son.", "The two went on together."],
  'instructions': [ins(K, S, "Abraham trusted God to provide the sacrifice."), ins(W, R, "“God will provide” is faith speaking without knowing how; the sentence is truer than the speaker intends.")],
  'entries': ['abraham', 'isaac', 'yhwh-jireh'],
  'lost': [between("Hebrew Elohim yir’eh-lo ha-seh, “God will see for himself the sheep,” is Greek ho theos opsetai heautō probaton, “God will see for himself a sheep”; both use see for provide. Hebrew beni, “my son,” is Greek teknon, “child.” Latin “victim” and King James “a lamb” keep their nouns from 22:7.")]},

 '22:9': {
  'received': "At the place God had named, Abraham built an altar, laid the wood, bound Isaac and laid him on it.",
  'explain': ("The preparations are told slowly: altar, wood, binding, laying. Isaac does not resist; the Hebrew verb for binding gives the event its "
   "Jewish name, the Akedah. The Greek says he bound his son Isaac’s feet together, naming the limbs; the Hebrew says bound. The Latin says the place "
   "God had shown him; the Hebrew and Greek told him."),
  'shared': ["They came to the place God had told him.", "Abraham built an altar and arranged the wood.", "He bound his son Isaac and laid him on the altar on the wood."],
  'instructions': [ins(K, S, "Abraham bound Isaac and laid him on the altar."), ins(W, R, "The binding is told without a word from the son; Isaac’s silence has been read as consent, and the chapter does not contradict it.")],
  'entries': ['abraham', 'isaac', 'altar'],
  'lost': [between("Hebrew va-ya‘aqod, “he bound,” the root of Akedah, is Greek sympodisas, “having bound the feet together,” naming the limbs; Hebrew ha-mizbeach, “the altar,” with the article, is Greek thysiastērion without it. Latin “God had shown him” and “placed him upon the altar on the pile of wood” paraphrase; King James follows the Hebrew.")]},

 '22:10': {
  'received': "Abraham reached for the knife to slay his son.",
  'explain': ("The act is at its last stage. The Hebrew says Abraham stretched out his hand and took the knife to slaughter his son, two completed acts "
   "and a purpose; the Greek says he stretched out his hand to take the knife to slaughter, so the taking is still intention when the voice comes. The "
   "Latin says grasped. The difference is where the intervention finds him."),
  'shared': ["Abraham stretched out his hand.", "He took, or reached for, the knife.", "His purpose was to slay his son."],
  'instructions': [ins(K, S, "Abraham went as far as the knife."), ins(W, R, "Nothing is left of the test but the stroke; whatever Abraham believed about return, he did not hold back the hand.")],
  'entries': ['abraham', 'isaac'],
  'lost': [
   loses("Hebrew va-yiqqach et-ha-ma’akhelet, “and he took the knife,” a completed act, becomes Greek labein tēn machairan, “to take the knife,” the purpose of the reaching; the knife is not yet in hand in the Greek."),
   between("Latin “grasped the knife to sacrifice” and King James “took the knife to slay” follow the Hebrew’s completed taking."),
  ]},

 '22:11': {
  'received': "The angel of the Lord called from heaven, Abraham, Abraham, and he answered, Here I am.",
  'explain': ("The voice comes from heaven, doubled, and Abraham answers for the third time, here I am. The angel of the Lord speaks as God in the "
   "verses that follow. The Hebrew says messenger of YHWH; the Greek angel of the Lord; the article in English does not settle who the figure is. "
   "All versions agree."),
  'shared': ["The angel of the Lord called from heaven.", "He called Abraham’s name twice.", "Abraham answered, Here I am."],
  'instructions': [ins(K, S, "The angel of the Lord stopped Abraham at the last moment."), ins(W, R, "The same “here I am” that began the test ends it; Abraham is as ready to be stopped as he was to be sent.")],
  'entries': ['angel-of-the-lord', 'abraham'],
  'lost': [between("Hebrew mal’akh YHWH and Greek angelos kyriou agree, both doubling the name here; Latin and King James likewise. The Hebrew says “from the heavens,” plural; the Greek “from heaven.”")]},

 '22:12': {
  'received': "The angel forbade Abraham to harm the boy, for now he knew Abraham feared God, not having withheld his only son.",
  'explain': ("The test is over and its result stated: now I know that you fear God. The Hebrew says you have not withheld your son, your only one, "
   "from me; the Greek you did not spare your beloved son for my sake; the Latin your only-begotten son. The words for the son and for the giving "
   "differ as in verse 2. The boy is unharmed."),
  'shared': ["Abraham is not to lay a hand on the boy or do anything to him.", "Now God knows that Abraham fears him.", "Abraham did not withhold his son."],
  'instructions': [ins(C, S, "Do not lay your hand on the boy."), ins(K, S, "Abraham’s fear of God was proved by his willingness to give up Isaac."), ins(W, R, "God asks for the son and refuses the sacrifice; what he wanted was the hand that did not hold back, not the blood.")],
  'entries': ['abraham', 'isaac'],
  'lost': [
   loses("Hebrew ve-lo chasakhta et-binkha et-yechidekha mimmenni, “and you have not withheld your son, your only one, from me,” becomes Greek kai ouk epheisō tou huiou sou tou agapētou di’ eme, “and you did not spare your beloved son for my sake”; withhold becomes spare, only becomes beloved, from me becomes for my sake."),
   between("Latin “have not spared your only-begotten son for My sake” mixes the two; King James “hast not withheld thy son, thine only son from me” follows the Hebrew. Romans 8:32 echoes the Greek “did not spare.”"),
  ]},

 '22:13': {
  'received': "Abraham saw a ram caught by its horns in a thicket, and offered it in place of his son.",
  'explain': ("God provides, as Abraham said. A ram is caught by its horns and is offered instead of Isaac, the first substitute sacrifice in Scripture. "
   "The Hebrew says a ram behind him in the thicket; the Greek one ram in a sabek plant, keeping the Hebrew word for thicket as if it were a species, "
   "and names Isaac at the offering; the Latin says among the thorns behind him."),
  'shared': ["Abraham raised his eyes and saw a ram.", "It was caught by its horns.", "He took it and offered it as a burnt offering in place of his son."],
  'instructions': [ins(K, S, "A ram was provided and offered instead of Isaac."), ins(W, R, "The substitute is caught, not chosen; God’s provision is already in the thicket before Abraham looks up.")],
  'entries': ['abraham', 'isaac', 'lamb-of-god'],
  'lost': [
   loses("Hebrew ayil achar, “a ram behind him,” becomes Greek krios heis, “one ram,” reading achar as echad, “one”; Hebrew ba-sevakh, “in the thicket,” becomes Greek en phytō sabek, “in a sabek plant,” transliterating the Hebrew noun as a plant name. The Greek adds Isaak at the offering."),
   between("Latin “behind him … among the thorns” and King James “behind him … in a thicket” follow the Hebrew; the Latin drops “went.” John 1:29 and 1 Peter 1:19 are the later lamb."),
  ]},

 '22:14': {
  'received': "Abraham named the place for the Lord’s seeing, and the saying arose, On the mountain of the Lord it will be seen.",
  'explain': ("The place is named from verse 8: the Lord sees, or provides. The Hebrew name is YHWH yir’eh, the Lord will see, and the proverb that "
   "follows is difficult, on the mountain of YHWH it will be seen; the Greek says the Lord saw, past, and on the mountain the Lord appeared, making God "
   "the one seen; the Latin the Lord sees and will see. Later tradition placed the temple on this mountain."),
  'shared': ["Abraham named the place.", "The name speaks of the Lord’s seeing.", "A saying about the mountain of the Lord arose from it."],
  'instructions': [ins(K, S, "The mountain was named for the Lord who sees and provides."), ins(W, R, "“The Lord sees” and “the Lord is seen” are one name in two tenses; on this mountain God both provides and appears.")],
  'entries': ['yhwh-jireh', 'abraham', 'jerusalem'],
  'lost': [
   loses("Hebrew YHWH yir’eh, “YHWH will see,” future, becomes Greek Kyrios eiden, “the Lord saw,” past; Hebrew be-har YHWH yera’eh, “on the mountain of YHWH it will be seen,” passive and difficult, becomes Greek en tō orei kyrios ōphthē, “on the mountain the Lord appeared,” with the Lord as the one seen; Hebrew asher ye’amer ha-yom, “as it is said today,” becomes hina eipōsin sēmeron, “so that they might say today.”"),
   between("Latin “The Lord Sees … on the mountain the Lord will see” keeps God as the seer in both; King James “Jehovahjireh … in the mount of the LORD it shall be seen” follows the Hebrew. 2 Chronicles 3:1 is the temple mount."),
  ]},

 '22:15': {
  'received': "The angel of the Lord called to Abraham a second time from heaven.",
  'explain': ("A second call, this time not to stop but to bless. The angel speaks in the next verse as the Lord swearing by himself. The versions agree; "
   "the Hebrew says messenger of YHWH, from the heavens."),
  'shared': ["The angel of the Lord called again.", "It was the second time.", "He called from heaven."],
  'instructions': [ins(K, S, "The angel spoke to Abraham a second time to bless him.")],
  'entries': ['angel-of-the-lord', 'abraham'],
  'lost': [between("Hebrew, Greek, Latin and King James agree; the Latin adds “saying.”")]},

 '22:16': {
  'received': "The Lord swore by himself, because Abraham had not withheld his only son,",
  'explain': ("God swears by himself, having nothing greater to swear by, as Hebrews observes. The ground is Abraham’s act. The Hebrew says you have not "
   "withheld your son, your only one; the Greek you did not spare your beloved son for my sake, adding for my sake which the Hebrew has only in verse 12; "
   "the Latin only-begotten, for my sake."),
  'shared': ["The Lord swore by himself.", "The reason is what Abraham has done.", "Abraham did not withhold his only son."],
  'instructions': [ins(K, S, "God bound himself by oath because of Abraham’s obedience."), ins(W, R, "God’s oath answers Abraham’s surrender; the promise that was gift becomes oath, and Hebrews says it is the anchor of hope.")],
  'entries': ['abraham', 'isaac'],
  'lost': [
   loses("Hebrew ve-lo chasakhta et-binkha et-yechidekha, “and you have not withheld your son, your only one,” is again Greek kai ouk epheisō tou huiou sou tou agapētou di’ eme, “and did not spare your beloved son for my sake”; the Greek adds di’ eme here, which the Hebrew has only in 22:12."),
   between("Latin “have not spared your only-begotten son for My sake” has the Greek phrase with its own noun; King James “hast not withheld thy son, thine only son” follows the Hebrew. Hebrews 6:13–14 quotes the oath."),
  ]},

 '22:17': {
  'received': "God will bless Abraham and multiply his offspring like the stars and the sand, and they will possess the gate of their enemies.",
  'explain': ("The promise is renewed in its fullest form: stars and sand together, and victory. The Hebrew says your offspring shall possess the gate of "
   "their enemies, the gate standing for the city; the Greek shall inherit the cities of their adversaries, spelling out the image. The Hebrew doubles "
   "the verbs, blessing I will bless, multiplying I will multiply, which the King James keeps."),
  'shared': ["God will surely bless Abraham.", "He will multiply his offspring like the stars of heaven and the sand of the seashore.", "His offspring will possess the gate of their enemies."],
  'instructions': [ins(K, S, "God confirmed innumerable offspring and victory to Abraham by oath."), ins(W, R, "Stars and sand are promised to a man who nearly lost his one son; the promise is restored larger than before.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew sha‘ar oyvav, “the gate of his enemies,” a concentrated image of a city’s control, becomes Greek tas poleis tōn hypenantiōn, “the cities of their adversaries,” the thing the image stands for; Hebrew yirash, “possess,” becomes klēronomēsei, “inherit.”"),
   between("Latin “the gates of their enemies” keeps the gate, plural; King James “the gate of his enemies” and “in blessing I will bless … in multiplying I will multiply” follow the Hebrew doubling. Hebrews 11:12 recalls the stars and sand."),
  ]},

 '22:18': {
  'received': "All the nations of the earth will be blessed through Abraham’s offspring, because he obeyed.",
  'explain': ("The blessing of 12:3 and 18:18 is sworn, now attached to the offspring and to obedience. The Hebrew verb is reflexive, shall bless themselves "
   "by your offspring, though passive and reciprocal readings are also argued; the Greek is passive, shall be blessed, the form Paul and Peter quote. The "
   "ground is you listened to my voice."),
  'shared': ["All the nations of the earth will be blessed in Abraham’s offspring.", "The reason is that Abraham obeyed God’s voice.", "The promise is sworn, not only spoken."],
  'instructions': [ins(K, S, "The blessing of all nations through Abraham’s seed was sealed by oath."), ins(W, R, "Obedience in the hardest thing becomes the ground of blessing for everyone; one man’s surrender is sworn into the future of the nations.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew ve-hitbarakhu, “and they shall bless themselves,” reflexive (or reciprocal), becomes Greek eneulogēthēsontai, “they shall be blessed,” passive; Hebrew shama‘ta be-qoli, “you listened to my voice,” is Greek hypēkousas tēs emēs phōnēs, “you obeyed my voice.”"),
   between("Latin “shall be blessed … you obeyed” and King James “be blessed … hast obeyed” follow the Greek passive. Acts 3:25 and Galatians 3:8 quote it."),
  ]},

 '22:19': {
  'received': "Abraham returned to his servants, and they went together to Beersheba, where he lived.",
  'explain': ("The descent is told briefly. Abraham rejoins the servants and they go to Beersheba. Isaac is not named in the return, which some ancient "
   "readers made much of; the omission says nothing about his fate. The Hebrew says Beersheba; the Greek the Well of the Oath; the Latin shortens."),
  'shared': ["Abraham returned to his servants.", "They went together to Beersheba.", "Abraham settled there."],
  'instructions': [ins(K, S, "Abraham returned to Beersheba after the sacrifice."), ins(W, R, "The silence about Isaac on the way down matches the silence about his words on the way up; the son is given back and the text does not say what passed between them.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew Be’er Shava is again Greek to phrear tou horkou, “the Well of the Oath,” twice; Hebrew ne‘arav is Greek paides. Latin “and they went together to Beersheba, where he lived” compresses; King James follows the Hebrew.")]},

 '22:20': {
  'received': "Abraham was told that Milcah had borne sons to his brother Nahor.",
  'explain': ("The chapter ends with news from Haran: Nahor’s family has grown. The list that follows exists for one name, Rebekah, Isaac’s future wife. "
   "The versions agree; the Latin makes the report indirect."),
  'shared': ["After these things Abraham was told news.", "Milcah had borne sons.", "They were sons of his brother Nahor."],
  'instructions': [ins(K, S, "Abraham learned of his brother Nahor’s sons."), ins(W, R, "After the mountain, a genealogy; the promise of offspring is already being prepared in a family far away.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew hinneh yaledah Milkah gam-hi, “behold, Milcah too has borne,” is Greek idou tetoken Melcha kai autē; the Latin reports indirectly. King James follows the Hebrew.")]},

 '22:21': {
  'received': "Uz the firstborn, Buz his brother, and Kemuel the father of Aram.",
  'explain': ("Three of Nahor’s eight sons. Uz shares his name with Job’s land, Buz with Elihu’s clan. The Hebrew says Kemuel the father of Aram; the "
   "Greek and Latin the father of the Syrians, giving the people for the ancestor."),
  'shared': ["Uz was the firstborn.", "Buz was his brother.", "Kemuel was the father of Aram."],
  'instructions': [ins(K, S, "Nahor’s first sons were Uz, Buz and Kemuel.")],
  'entries': [],
  'lost': [between("Hebrew avi Aram, “the father of Aram,” is Greek patera Syrōn, “the father of the Syrians”; Latin likewise; King James “the father of Aram” with the Hebrew. Job 1:1 and 32:2 recall Uz and Buz.")]},

 '22:22': {
  'received': "Chesed, Hazo, Pildash, Jidlaph and Bethuel.",
  'explain': ("Five more names, completing the eight. The Hebrew reads Hazo; the Greek Azau. The Greek and Hebrew include Bethuel here; the Latin keeps "
   "him for the next verse. Chesed may be the ancestor of the Chaldeans, Kasdim."),
  'shared': ["Chesed and Pildash are named.", "Hazo or Azau and Jidlaph are named.", "Bethuel is named."],
  'instructions': [ins(K, S, "Nahor’s sons included Bethuel, the father of Rebekah.")],
  'entries': [],
  'lost': [between("Hebrew Chazo is Greek Azau, a different form; the Latin verse ends at Jidlaph and gives Bethuel in 22:23. King James follows the Hebrew.")]},

 '22:23': {
  'received': "Bethuel was the father of Rebekah; these eight Milcah bore to Nahor, Abraham’s brother.",
  'explain': ("The list reaches its point: Rebekah, granddaughter of Nahor and Milcah, who will marry Isaac in chapter 24. The Hebrew says Bethuel begat "
   "Rebekah and these eight; the Greek these eight sons; the Latin of whom Rebekah was born. Rebekah is the only woman named among the grandchildren."),
  'shared': ["Bethuel begat Rebekah.", "Milcah bore eight to Nahor.", "Nahor was Abraham’s brother."],
  'instructions': [ins(K, S, "Rebekah, Isaac’s future wife, was Nahor’s granddaughter."), ins(W, R, "The genealogy is told for one girl’s sake; the next generation of the promise is already born in Nahor’s house.")],
  'entries': ['rebekah'],
  'lost': [between("Greek adds huioi, “sons,” to the eight; Hebrew shemonah elleh, “these eight.” Latin “and Bethuel, of whom Rebekah was born” makes the birth passive; King James follows the Hebrew.")]},

 '22:24': {
  'received': "Nahor’s concubine Reumah bore him Tebah, Gaham, Tahash and Maacah.",
  'explain': ("Four more sons by a concubine complete Nahor’s twelve, matching Ishmael’s twelve and Jacob’s. The Greek name forms differ, Tabek, Tochos, "
   "Mocha for Tebah, Tahash, Maacah; the number and the concubine agree. Maacah is also the name of a small Aramean kingdom."),
  'shared': ["Nahor had a concubine named Reumah.", "She also bore sons.", "They were Tebah, Gaham, Tahash and Maacah."],
  'instructions': [ins(K, S, "Nahor had four more sons by his concubine Reumah.")],
  'entries': [],
  'lost': [between("Hebrew Tevach, Tachash and Ma‘akhah appear in Greek as Tabek, Tochos and Mocha; Gaham and Reumah are close. Latin and King James keep the Hebrew forms.")]},
 }
}
