# Study prose for Genesis 28 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 28,
 'chapterNote': (
  "Jacob is sent to Haran with a blessing he did not steal, Esau takes a third wife from Ishmael, and at Bethel the fugitive sees the stairway and hears the "
  "promise in his own name. The Hebrew keeps El Shaddai, “an assembly of peoples,” “your seed with you,” Paddan-aram, Beersheba, YHWH standing “above it,” "
  "“the dust of the earth,” the four directions in the order west, east, north, south, Luz, “if God will be with me,” and “I return in peace.” The Greek keeps "
  "“my God” for El Shaddai, “assemblies of nations,” Abraham called “my father,” “flee” for “go,” Mesopotamia and “Mesopotamia of Syria,” the Well of the Oath, "
  "the Lord standing “firm upon it,” an added “fear not,” “the sand of the earth,” the directions sea, south, north, east, “House of God” for Bethel, Oulamlous "
  "for Luz, “the Lord God” in the vow, and God as the agent of the return. The Latin and King James follow the Hebrew; the Latin has the Lord “leaning upon the ladder.”"),
 'verses': {

 '28:1': {
  'received': "Isaac called Jacob, blessed him, and charged him not to marry a Canaanite.",
  'explain': ("Isaac, now knowing whom he blessed, blesses Jacob again, openly, and repeats Abraham’s rule of chapter 24. The Latin says the people of Canaan; the others the daughters."),
  'shared': ["Isaac called Jacob and blessed him.", "He charged him.", "You shall not take a wife from the daughters of Canaan."],
  'instructions': [ins(C, S, "You shall not take a wife from the daughters of Canaan."), ins(K, S, "Isaac knowingly blessed Jacob and sent him for a wife."), ins(W, R, "The blessing given blind is now given with open eyes; Isaac accepts the oracle and makes Jacob’s departure a mission rather than a flight.")],
  'entries': ['isaac', 'jacob', 'canaan'],
  'lost': [between("Latin “from the people of Canaan” for Hebrew mi-benot Kena‘an, “from the daughters of Canaan”; Greek and King James “daughters.”")]},

 '28:2': {
  'received': "Go to Paddan-aram, to Bethuel’s house, and take a wife from Laban’s daughters.",
  'explain': ("The destination and the bride’s family, as in Rebekah’s own story. The Hebrew says go to Paddan-aram; the Greek flee to Mesopotamia, importing Rebekah’s word from 27:43; the Latin journey to Mesopotamia of Syria."),
  'shared': ["Arise and go to Paddan-aram.", "Go to the house of Bethuel, your mother’s father.", "Take a wife from the daughters of Laban, your mother’s brother."],
  'instructions': [ins(C, S, "Go to Paddan-aram and take a wife from the daughters of Laban."), ins(W, R, "Isaac sends Jacob where Abraham sent a servant; this time the heir goes himself, with nothing but a staff.")],
  'entries': ['haran'],
  'lost': [loses("Hebrew lekh Paddenah Aram, “go to Paddan-aram,” becomes Greek apodrathi eis tēn Mesopotamian, “flee to Mesopotamia”; the flight is Rebekah’s word, not Isaac’s."), between("Latin “go and journey to Mesopotamia of Syria” and King James “go to Padanaram” keep the going.")]},

 '28:3': {
  'received': "May El Shaddai bless you and make you fruitful, that you become an assembly of peoples.",
  'explain': ("The blessing proper, in the name God used to Abraham in 17:1. The Hebrew says El Shaddai, an assembly of peoples, qehal ammim; the Greek my God, assemblies of nations; the Latin God Almighty, a multitude of peoples."),
  'shared': ["May God Almighty bless you.", "May He make you fruitful and multiply you.", "May you become an assembly of peoples."],
  'instructions': [ins(K, S, "Isaac blessed Jacob with fruitfulness in El Shaddai’s name."), ins(W, R, "The name of the covenant of circumcision is invoked over the son who goes out alone; the people begin in one man on a road.")],
  'entries': ['jacob', 'el-shaddai'],
  'lost': [loses("Hebrew El Shaddai becomes Greek ho theos mou, “my God”; Hebrew qehal ammim, “an assembly of peoples,” singular, becomes synagōgas ethnōn, “assemblies of nations,” plural."), between("Latin “God Almighty … a multitude of peoples” and King James “God Almighty … a multitude of people” follow the Hebrew.")]},

 '28:4': {
  'received': "May He give you Abraham’s blessing, to you and your seed, to inherit the land of your sojourning that God gave Abraham.",
  'explain': ("The Abrahamic blessing formally transferred. The Hebrew says the blessing of Abraham, your seed with you, God gave; the Greek Abraham my father, your seed after you; the Latin He promised your grandfather."),
  'shared': ["May He give you the blessing of Abraham.", "To you and your seed.", "To inherit the land of your sojourning, which God gave to Abraham."],
  'instructions': [ins(K, S, "Isaac passed the blessing of Abraham to Jacob."), ins(W, R, "The land of your sojourning: Jacob is to inherit a land he is leaving and in which he has only ever been a guest.")],
  'entries': ['abraham', 'jacob'],
  'lost': [keeps("An added tou patros mou, “my father,” after Abraham in the Greek; Hebrew u-le-zar‘akha ittakh, “and to your seed with you,” becomes tō spermati sou meta se, “to your seed after you.”"), between("Latin “which He promised your grandfather” varies; King James “to thy seed with thee … which God gave unto Abraham.”")]},

 '28:5': {
  'received': "Isaac sent Jacob to Paddan-aram, to Laban the Aramean, brother of Rebekah, mother of Jacob and Esau.",
  'explain': ("The departure, with a full genealogical tag. The Hebrew says Paddan-aram, Aramean; the Greek Mesopotamia, Syrian; the Latin Mesopotamia of Syria, and drops Esau."),
  'shared': ["Isaac sent Jacob away.", "He went to Laban son of Bethuel the Aramean.", "Laban was Rebekah’s brother, the mother of Jacob and Esau."],
  'instructions': [ins(K, S, "Jacob left for Laban’s house.")],
  'entries': ['isaac', 'jacob', 'rebekah', 'haran'],
  'lost': [between("Hebrew Paddenah Aram … ha-Arammi is Greek Mesopotamian … tou Syrou; Latin “Mesopotamia of Syria … the Syrian” and drops “the mother of Jacob and Esau” to “his mother Rebekah”; King James “Padanaram … the Syrian.”")]},

 '28:6': {
  'received': "Esau saw that Isaac had blessed Jacob and sent him to Paddan-aram for a wife, charging him against Canaanite women.",
  'explain': ("Esau watches and draws a conclusion. The Hebrew and King James say Paddan-aram; the Greek Mesopotamia of Syria and Jacob had gone; the Latin Mesopotamia of Syria, Isaac sent him."),
  'shared': ["Esau saw that Isaac had blessed Jacob.", "Jacob was sent to Paddan-aram to take a wife.", "Isaac had charged him not to take a Canaanite wife."],
  'instructions': [ins(K, S, "Esau noted the blessing and the marriage charge.")],
  'entries': ['isaac', 'jacob'],
  'lost': [between("Hebrew ve-shillach oto Paddenah Aram, “and sent him to Paddan-aram,” is Greek apōcheto eis tēn Mesopotamian Syrias, “he went to Mesopotamia of Syria”; Latin “sent him to Mesopotamia of Syria”; King James “sent him away to Padanaram.”")]},

 '28:7': {
  'received': "and that Jacob had obeyed his parents and gone to Paddan-aram.",
  'explain': ("Jacob obeyed, the narrator says, the first wholly creditable thing said of him. The Greek says Mesopotamia of Syria; the Latin Syria, his parents."),
  'shared': ["Jacob obeyed his father.", "He obeyed his mother.", "He went to Paddan-aram."],
  'instructions': [ins(K, S, "Jacob obeyed his parents in going.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew Paddenah Aram is Greek Mesopotamian Syrias, Latin “Syria,” King James “Padanaram”; Latin “his parents” for “his father and his mother.”")]},

 '28:8': {
  'received': "Esau saw that the Canaanite women displeased his father.",
  'explain': ("Esau learns late what his marriages cost him. The versions agree."),
  'shared': ["Esau saw.", "The daughters of Canaan displeased Isaac.", "Isaac was his father."],
  'instructions': [ins(K, S, "Esau realised his father disapproved of Canaanite wives."), ins(W, R, "Esau wants his father’s approval after the blessing is gone; he reads Isaac’s wishes a chapter too late.")],
  'entries': ['isaac', 'canaan'],
  'lost': [AGREE]},

 '28:9': {
  'received': "So Esau went to Ishmael and married Mahalath, Ishmael’s daughter, Nebaioth’s sister, besides his other wives.",
  'explain': ("A wife from Abraham’s line, but the rejected branch: Ishmael’s daughter, a cousin. The two sons outside the promise join their houses. The versions agree; Mahalath is called Basemath in 36:3."),
  'shared': ["Esau went to Ishmael.", "He took Mahalath, daughter of Ishmael, Abraham’s son, sister of Nebaioth.", "He added her to the wives he already had."],
  'instructions': [ins(K, S, "Esau married Ishmael’s daughter."), ins(W, R, "Esau mends his marriages by marrying into Ishmael; the two displaced sons of Abraham’s house make common cause, and Edom and Ishmael are kin ever after.")],
  'entries': ['abraham'],
  'lost': [AGREE]},

 '28:10': {
  'received': "Jacob left Beersheba and went toward Haran.",
  'explain': ("The journey begins, from his father’s home to his mother’s. The Hebrew says Beersheba; the Greek the Well of the Oath; the Latin Beersheba."),
  'shared': ["Jacob went out from Beersheba.", "He journeyed.", "He went toward Haran."],
  'instructions': [ins(K, S, "Jacob set out from Beersheba for Haran."), ins(W, R, "Abraham’s road run backwards: the heir leaves the land to find a wife, alone where his father’s servant had ten camels.")],
  'entries': ['jacob', 'haran'],
  'lost': [loses("Hebrew Be’er Sheva becomes Greek tou phreatos tou horkou, “the Well of the Oath.”"), between("Latin and King James “Beersheba.”")]},

 '28:11': {
  'received': "He came to a place, stopped for the night at sunset, put a stone under his head and slept.",
  'explain': ("A certain place, ha-maqom, the place, as if already known; a stone for a pillow. The Latin says wished to rest; the King James stones, pillows, plural, though verse 18 has one."),
  'shared': ["He came to a certain place and stayed the night, for the sun had set.", "He took one of the stones of the place and put it under his head.", "He lay down to sleep there."],
  'instructions': [ins(K, S, "Jacob slept in the open with a stone for a pillow."), ins(W, R, "The heir of Abraham lies on the ground with a rock under his head; the promise is about to be renewed to a man with nothing.")],
  'entries': ['jacob'],
  'lost': [between("Latin “wished to rest there after sunset” varies; King James “took of the stones of that place, and put them for his pillows” pluralises; Hebrew and Greek “one of the stones … under his head.”")]},

 '28:12': {
  'received': "He dreamed of a stairway from earth to heaven with the angels of God going up and down on it.",
  'explain': ("The dream. Sullam, found only here, a ladder or stairway, perhaps a ramp like a ziggurat’s. Angels ascend first, then descend. The versions agree; John 1:51 reads the Son of Man as the ladder."),
  'shared': ["He dreamed.", "A stairway stood on the earth and its top reached heaven.", "The angels of God were ascending and descending on it."],
  'instructions': [ins(K, S, "Jacob dreamed of the stairway to heaven."), ins(W, R, "Heaven and earth are joined above a sleeping fugitive; the traffic of angels goes on whether or not he knows it, and he is about to learn that he did not know.")],
  'entries': ['jacob', 'angels'],
  'lost': [AGREE]},

 '28:13': {
  'received': "The Lord stood above it and said, I am the Lord, God of Abraham and Isaac; the land you lie on I give to you and your seed.",
  'explain': ("The Lord speaks in His own name to Jacob for the first time. The Hebrew says stood above it, or beside him; the Greek stood firm upon it and adds fear not; the Latin leaned upon the ladder."),
  'shared': ["The Lord stood above it.", "I am the Lord, the God of Abraham your father and the God of Isaac.", "The land on which you lie I will give to you and your seed."],
  'instructions': [ins(K, S, "God renewed the land promise to Jacob at Bethel."), ins(W, R, "The ground under the fugitive is the first ground promised to him; the land is given to a man lying on it with a stone for a pillow.")],
  'entries': ['jacob', 'abraham', 'isaac', 'yhwh-yahweh'],
  'lost': [keeps("An added mē phobou, “fear not,” in the Greek; Hebrew nitzav alav, “standing over it” or “him,” is Greek epestērikto ep’ autēs, “stood firm upon it.”"), between("Latin “leaned upon the ladder” and King James “stood above it” follow the Hebrew without the fear not.")]},

 '28:14': {
  'received': "Your seed shall be like the dust of the earth, spreading in every direction, and all families of the earth shall be blessed in you and your seed.",
  'explain': ("The promise of 13:16 and 12:3 to Jacob. The Hebrew says dust of the earth, west, east, north, south, families; the Greek sand of the earth, toward the sea, south, north, east, tribes; the Latin dust, tribes."),
  'shared': ["Your seed shall be like the dust of the earth.", "You shall spread west, east, north and south.", "All the families of the earth shall be blessed in you and your seed."],
  'instructions': [ins(K, S, "God promised Jacob innumerable seed and blessing for all nations."), ins(W, R, "The deceiver receives the blessing of the nations unasked and unearned; grace at Bethel is given to the man least able to claim it.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew ka-afar ha-aretz, “as the dust of the earth,” becomes Greek hōs hē ammos tēs gēs, “as the sand of the earth”; Hebrew yammah va-qedmah ve-tzafonah va-negbah, “seaward, eastward, northward, southward,” becomes epi thalassan kai liba kai borran kai anatolas, “to the sea and the south and the north and the east”; Hebrew mishpechot, “families,” becomes phylai, “tribes.”"), between("Latin “dust of the earth … west and east, north and south … tribes” and King James “dust … west … east … north … south … families” follow the Hebrew.")]},

 '28:15': {
  'received': "I am with you and will keep you wherever you go and bring you back to this land; I will not leave you until I have done what I promised.",
  'explain': ("Presence, protection, return, completion. The Hebrew says I am with you, guard you wherever you go; the Greek I am with you, guarding you on every road, never abandon; the Latin I will be your guardian, without I am with you."),
  'shared': ["I am with you and will guard you wherever you go.", "I will bring you back to this land.", "I will not leave you until I have done what I have spoken."],
  'instructions': [ins(K, S, "God promised Jacob His presence and return."), ins(W, R, "“I am with you” was said to Isaac in Gerar and is now said to Jacob on the road; the promise travels with the man, which is what a promise of land to a wanderer must mean.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ve-hinneh anokhi immakh, “and behold I am with you,” is Greek kai idou egō meta sou; Latin “I will be your guardian wherever you go” drops the clause; Hebrew be-khol asher-telekh, “in all that you go,” is Greek en tē hodō pasē hou ean poreuthēs, “on every road you travel.”")]},

 '28:16': {
  'received': "Jacob awoke and said, Surely the Lord is in this place and I did not know it.",
  'explain': ("The waking confession. The versions agree."),
  'shared': ["Jacob awoke from his sleep.", "Surely the Lord is in this place.", "I did not know it."],
  'instructions': [ins(K, S, "Jacob recognised God’s presence at the place."), ins(W, R, "“I did not know it” is the truest thing Jacob has said; the place was holy before he noticed, and God was with him before he asked.")],
  'entries': ['jacob', 'yhwh-yahweh'],
  'lost': [AGREE]},

 '28:17': {
  'received': "He was afraid and said, How fearful is this place; it is the house of God, the gate of heaven.",
  'explain': ("Fear and the two names: Beth-El, house of God, and gate of heaven. The versions agree."),
  'shared': ["He was afraid.", "How fearful is this place!", "This is the house of God and the gate of heaven."],
  'instructions': [ins(K, S, "Jacob called the place God’s house and heaven’s gate."), ins(W, R, "The gate of heaven is a stony hillside where a runaway slept; holiness, Jacob learns, is where God is, not where men build.")],
  'entries': ['jacob', 'bethel'],
  'lost': [AGREE]},

 '28:18': {
  'received': "In the morning he set up his pillow-stone as a pillar and poured oil on it.",
  'explain': ("A matzevah, standing stone, anointed with oil; the first anointing in Scripture. The versions agree."),
  'shared': ["Jacob rose early in the morning.", "He took the stone from under his head and set it up as a pillar.", "He poured oil on top of it."],
  'instructions': [ins(K, S, "Jacob consecrated the stone as a pillar."), ins(W, R, "The pillow becomes a pillar; what served Jacob’s head is made to mark God’s presence. Oil on a stone is the first consecration in Genesis.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '28:19': {
  'received': "He named the place Bethel; the city had been called Luz.",
  'explain': ("Bethel, house of God, replacing Luz, almond tree. The Hebrew keeps both names; the Greek translates Bethel as House of God and gives the old name as Oulamlous, a run-together of the Hebrew ulam Luz, formerly Luz; the Latin Bethel, Luz."),
  'shared': ["He named that place.", "He named it Bethel.", "Previously the city had been called Luz."],
  'instructions': [ins(K, S, "Jacob renamed Luz as Bethel.")],
  'entries': ['bethel', 'jacob'],
  'lost': [loses("Hebrew Bet-El, a name, becomes Greek Oikos theou, “House of God,” a translation; Hebrew ulam Luz, “but formerly Luz,” becomes Oulamlous, the adverb and the name read as one word."), between("Latin “Bethel … Luz” and King James “Bethel … Luz” keep the names.")]},

 '28:20': {
  'received': "Jacob vowed: if God will be with me and keep me on this road and give me bread and clothing,",
  'explain': ("The vow begins with conditions: presence, protection, bread, clothing, the needs of a man on the road. The Hebrew says God; the Greek the Lord God; the Latin if God is with me."),
  'shared': ["Jacob vowed a vow.", "If God will be with me and guard me on this way.", "If He gives me bread to eat and clothing to put on."],
  'instructions': [ins(K, S, "Jacob’s vow set conditions for his allegiance."), ins(W, R, "Jacob bargains even with God, asking for bread and clothes; the vow is a trader’s, and God will keep His side before Jacob fully keeps his.")],
  'entries': ['jacob'],
  'lost': [keeps("An added kyrios, “Lord,” before God in the Greek: kyrios ho theos."), between("Latin and King James “God.”")]},

 '28:21': {
  'received': "and I return safely to my father’s house, then the Lord shall be my God.",
  'explain': ("The condition ends and the vow begins, or the vow begins here; interpreters divide. The Hebrew says I return in peace; the Greek He brings me back safely, making God the agent; the Latin I return safely."),
  'shared': ["I return in peace to my father’s house.", "Then.", "The Lord shall be my God."],
  'instructions': [ins(K, S, "Jacob vowed to take the Lord as his God on his safe return."), ins(W, R, "“The Lord shall be my God” is conditional on a homecoming; the God of Abraham and Isaac is not yet, in Jacob’s mouth, the God of Jacob.")],
  'entries': ['jacob', 'yhwh-yahweh'],
  'lost': [between("Hebrew ve-shavti ve-shalom, “and I return in peace,” is Greek kai apostrepsē me meta sōtērias, “and He brings me back with safety”; Latin “I return safely,” King James “I come again … in peace.”")]},

 '28:22': {
  'received': "This stone pillar shall be God’s house, and of all You give me I will give a tenth.",
  'explain': ("The vow proper: a shrine and a tithe, the second tithe in Genesis after Abraham’s to Melchizedek. The Greek adds to me; the Latin shall be called."),
  'shared': ["This stone I have set up as a pillar shall be the house of God.", "Of all You give me.", "I will surely give a tenth to You."],
  'instructions': [ins(K, S, "Jacob vowed a shrine and a tithe at Bethel."), ins(W, R, "A tenth of everything is promised by a man who owns a staff; the tithe is faith’s arithmetic, counting on what has not yet been given.")],
  'entries': ['jacob', 'bethel'],
  'lost': [keeps("An added moi, “to me,” in the Greek: “shall be to me the house of God.”"), between("Latin “shall be called the House of God” and King James “shall be God’s house” follow the Hebrew.")]},
 }
}
