# Study prose for Genesis 19 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 19,
 'chapterNote': (
  "The night at Sodom, the rescue of Lot, the fire from heaven, the pillar of salt and the cave are the same story in every column. What "
  "varies is in the verbs and the explanations. The Hebrew keeps “that we may know them,” “this one came to sojourn,” a singular son-in-law, "
  "men who were taking the daughters, Lot lingering, a single speaker at the escape, “no, please, Lord,” favour and kindness, smoke rising, "
  "Moab and Ben-ammi without gloss. The Greek keeps “that we may have intercourse with them,” the crowd addressing Lot as “you,” sons-in-law "
  "who had taken the daughters, a family “troubled,” the angels named as rescuers, plural speakers, “I beg you, Lord,” mercy and righteousness, "
  "a flame rising, and the names explained: Moab “from my father,” Amman “son of my kin.” The Latin and King James follow the Hebrew; the "
  "Latin glosses Ammon too."),
 'verses': {

 '19:1': {
  'received': "The two angels reached Sodom at evening, and Lot, sitting in the gate, rose to meet them and bowed.",
  'explain': ("Two of the three visitors of chapter 18 arrive at Sodom at the hour when the day’s travel ends. Lot is in the gate, where a city’s "
   "elders sat, and he does what Abraham did: rises, meets them, bows to the ground. The Hebrew calls them messengers, the Greek angels, the "
   "same word. Lot’s welcome is as warm as his uncle’s; the city’s will not be."),
  'shared': ["The two angels came to Sodom in the evening.", "Lot was sitting in the gate of Sodom.", "He rose to meet them and bowed to the ground."],
  'instructions': [ins(K, S, "Lot received the two angels at Sodom’s gate with honour."), ins(W, R, "Lot has learned Abraham’s hospitality; the man who chose Sodom still keeps the manners of the tents.")],
  'entries': ['angels'],
  'lost': [between("Hebrew mal’akhim and Greek angeloi are both “messengers”; Hebrew be-sha‘ar, “in the gate,” is Greek para tēn pylēn, “beside the gate.” Latin “at the city gates” and King James “in the gate of Sodom” agree in sense.")]},

 '19:2': {
  'received': "Lot urged the visitors to lodge at his house and wash their feet, but they said they would spend the night in the square.",
  'explain': ("The invitation repeats Abraham’s offer: a house, a night’s rest, water for the feet, an early start. The guests refuse at first and "
   "propose the open square, a refusal that tests the host and, in Sodom, would have been dangerous. Lot addresses them as lords in the plural. "
   "The versions agree; the Hebrew adds “please.”"),
  'shared': ["Lot invited them to his house for the night.", "He offered to wash their feet so they could leave early.", "They said they would spend the night in the square."],
  'instructions': [ins(K, S, "Lot offered the angels lodging, which they at first declined."), ins(W, R, "A guest’s first refusal is a courtesy that lets the host prove his welcome; Lot passes the test that Sodom will fail.")],
  'entries': ['angels'],
  'lost': [between("Hebrew hinneh na-adonai, “please, my lords,” is Greek idou, kyrioi, “look, lords,” without “please” or “my”; Hebrew ba-rechov, “in the square,” is Greek en tē plateia. Latin and King James keep the entreaty.")]},

 '19:3': {
  'received': "Lot pressed them until they came in, and he made them a feast with unleavened bread.",
  'explain': ("Lot insists and the guests yield. He makes them a feast, the Hebrew and Greek words both suggesting drink, and bakes unleavened bread "
   "because there is no time to let dough rise. The Greek says a drinking feast and repeats “for them”; the bread is not a festival observance here. "
   "The guests eat, as at Mamre."),
  'shared': ["Lot pressed them and they came into his house.", "He prepared a feast and baked unleavened bread.", "They ate."],
  'instructions': [ins(K, S, "Lot persuaded the angels to lodge with him and fed them."), ins(W, R, "Unleavened bread is the bread of haste; even Lot’s hospitality is hurried by the city around it.")],
  'entries': ['angels'],
  'lost': [between("Hebrew mishteh, “feast,” from the verb to drink, is Greek poton, “a drinking feast”; Hebrew matsot and Greek azymous are both “unleavened bread.” The Greek repeats autois, “for them,” with the bread. Latin and King James agree in sense.")]},

 '19:4': {
  'received': "Before they lay down, the men of Sodom, young and old, surrounded the house.",
  'explain': ("The city shows itself. Before the guests can sleep the men of Sodom, from young to old, every one, surround the house. The Hebrew "
   "stresses extent, all the people from every quarter; the Greek says together, and adds the name Sodomites. No one in the city is exempted."),
  'shared': ["The guests had not yet lain down.", "The men of the city surrounded the house.", "They came young and old, all the people."],
  'instructions': [ins(K, S, "The whole male population of Sodom besieged Lot’s house."), ins(W, R, "“From young to old, all the people” is the narrator’s answer to Abraham’s question; there were not ten.")],
  'entries': [],
  'lost': [between("Hebrew kol-ha-am mi-qatseh, “all the people from the extremity,” that is from every quarter, is Greek pas ho laos hama, “all the people together”; the Greek adds hoi Sodomitai, “the Sodomites.” Latin “all the people together” follows the Greek; King James “from every quarter” the Hebrew.")]},

 '19:5': {
  'received': "They called for Lot to bring out his visitors so that they might abuse them.",
  'explain': ("The demand is stated. The Hebrew uses know as a euphemism for sexual relations, as in 4:1; the Greek verb can mean associate with or "
   "have intercourse with, and the context, especially verse 8, makes the meaning plain. The Latin and King James keep “know.” The crowd wants "
   "the strangers for rape."),
  'shared': ["The men called to Lot.", "They asked for the men who had come to him that night.", "They demanded them for sexual abuse."],
  'instructions': [ins(K, S, "The men of Sodom demanded Lot’s guests for sexual violence."), ins(W, R, "Hospitality and its violation are the measure of Sodom; the stranger under a roof is the test the city fails.")],
  'entries': [],
  'lost': [between("Hebrew ve-ned‘ah otam, “that we may know them,” a euphemism, is Greek hina syngenōmetha autois, “that we may have intercourse with them,” a verb that also means associate with; the context fixes the sense. Latin cognoscamus and King James “know” keep the euphemism. Judges 19:22 repeats the scene.")]},

 '19:6': {
  'received': "Lot went out to them and shut the door behind him.",
  'explain': ("Lot steps outside to face the crowd and closes the door to protect his guests, putting himself between them and the mob. The Greek "
   "says he stood at the vestibule; the Hebrew at the entrance. The Latin carries his “he said” into this verse."),
  'shared': ["Lot went out to the men.", "He stood at the entrance.", "He shut the door behind him."],
  'instructions': [ins(K, S, "Lot went out alone to confront the crowd and protect his guests."), ins(W, R, "Lot shuts the door on his own safety; whatever follows, this is the act of a host.")],
  'entries': [],
  'lost': [between("Hebrew ha-petchah, “to the entrance,” is Greek pros to prothyron, “to the vestibule”; Latin has no threshold word and adds “and said.” King James “at the door” follows the Hebrew.")]},

 '19:7': {
  'received': "Lot begged the men not to act wickedly.",
  'explain': ("Lot calls the mob brothers and pleads with them. The Hebrew begins “please, my brothers”; the Greek with a forceful refusal, “by no "
   "means, brothers.” It is the plea of a man who has lived among them and still hopes to be heard."),
  'shared': ["Lot addressed the men as brothers.", "He pleaded with them.", "He asked them not to act wickedly."],
  'instructions': [ins(K, S, "Lot pleaded with the men of Sodom to do no evil."), ins(W, R, "Calling the mob “brothers” is Lot’s whole position in Sodom: inside it, pleading, and unheard.")],
  'entries': [],
  'lost': [between("Hebrew al-na achai, “please, my brothers,” is Greek mēdamōs, adelphoi, “by no means, brothers”; the Greek replaces the entreaty with a refusal and drops “my.” Latin “please, my brothers” and King James “I pray you, brethren” follow the Hebrew.")]},

 '19:8': {
  'received': "Lot offered the mob his two virgin daughters instead, asking only that his guests be left alone.",
  'explain': ("Lot’s offer is monstrous and the text reports it without approving it. He offers his daughters to protect the men under his roof; the "
   "law of the guest outweighs the daughters in his mind. The Hebrew says do to them what seems good to you; the Greek use them as you please, "
   "and calls the forbidden act unjust. The Hebrew says the shadow of my roof, the Greek my roof beams."),
  'shared': ["Lot has two daughters who have not known a man.", "He offers to bring them out to the mob.", "He asks that nothing be done to the men under his roof."],
  'instructions': [ins(K, S, "Lot offered his daughters to the mob to protect his guests."), ins(W, R, "The text records Lot’s offer and nowhere approves it; a host’s duty has become a father’s crime, and Scripture lets the reader see both.")],
  'entries': [],
  'lost': [between("Hebrew va-asu lahen ka-tov be-eineikhem, “do to them what seems good in your eyes,” is Greek chrasthe autais katha an areskē hymin, “use them as you please”; Hebrew al-ta‘asu davar, “do nothing,” is Greek mē poiēsēte mēden adikon, “do nothing unjust”; Hebrew be-tsel qorati, “in the shadow of my roof,” is Greek hypo tēn skepēn tōn dokōn mou, “under the shelter of my roof beams.” Latin and King James follow the Hebrew.")]},

 '19:9': {
  'received': "The mob turned on Lot as a meddling foreigner, threatened him with worse, and pressed on the door.",
  'explain': ("Lot’s plea provokes them. He is a sojourner, and now he judges them; they will treat him worse than his guests. The Hebrew has the "
   "crowd speak of Lot in the third person, this one came to sojourn; the Greek addresses him directly, you came alone to sojourn, and makes the "
   "judging a question. They press on Lot and move to break the door."),
  'shared': ["The men told Lot to stand back.", "They mocked him as a sojourner who presumes to judge.", "They threatened to treat him worse than his guests and pressed against the door."],
  'instructions': [ins(K, S, "The mob rejected Lot’s intervention and threatened him."), ins(W, R, "The sojourner who protests is told he has no standing; the righteous man in Sodom is tolerated only while he is silent.")],
  'entries': [],
  'lost': [
   loses("Hebrew ha-echad ba lagur va-yishpot shafot, “this one came to sojourn, and he judges indeed,” a third-person sneer with a doubled verb, becomes Greek eisēlthes paroikein, mē kai krisin krinein, “you came to sojourn; will you also judge?”, second person and a question. The Hebrew’s two “they said” become one."),
   between("Latin “you came as a stranger; did you come to judge?” shares the Greek second person; King James “this one fellow came in to sojourn, and he will needs be a judge” follows the Hebrew."),
  ]},

 '19:10': {
  'received': "The visitors pulled Lot inside and shut the door.",
  'explain': ("The rescue reverses roles: the guests save the host. They reach out, pull Lot in and shut the door he had shut on himself. The Greek "
   "spells out “into the house” and “the door of the house”; the Hebrew is briefer. The men are still called men here."),
  'shared': ["The men reached out their hands.", "They pulled Lot into the house.", "They shut the door."],
  'instructions': [ins(K, S, "The angels rescued Lot from the mob."), ins(W, R, "The host is saved by his guests; Lot’s protection of the strangers becomes their protection of him.")],
  'entries': ['angels'],
  'lost': [between("Hebrew va-yavi’u, “brought in,” is Greek eisespasanto, “pulled in”; the Greek adds eis ton oikon and tēn thyran tou oikou. Latin and King James agree in sense.")]},

 '19:11': {
  'received': "They struck the men outside with blindness, so that they wore themselves out looking for the door.",
  'explain': ("The mob is struck blind, small and great, and gropes for the door in vain. The Hebrew says they wearied themselves to find it; the "
   "Greek that they became helpless seeking it; the Latin simply that they could not find it. The same word for blindness is used of the Syrian "
   "army struck at Elisha’s prayer."),
  'shared': ["The men at the door were struck with blindness.", "Small and great alike were struck.", "They could not find the door."],
  'instructions': [ins(K, S, "The angels blinded the men of Sodom."), ins(W, R, "Blind men still grope for the door of the house they meant to violate; judgement here does not end the desire, only the power.")],
  'entries': ['angels'],
  'lost': [between("Hebrew va-yil’u, “they wore themselves out,” is Greek pareluthēsan, “they were weakened” or “disabled”; Hebrew sanverim, “blindness,” the word of 2 Kings 6:18, is Greek aorasia. Latin “could not find the door” drops the weariness; King James “wearied themselves” keeps it.")]},

 '19:12': {
  'received': "The visitors told Lot to gather any family he had in the city and bring them out.",
  'explain': ("The angels declare their purpose by a question: who else is yours here? Son-in-law, sons, daughters, anyone in the city, bring them "
   "out. The Hebrew has a singular son-in-law and a command to bring out all who belong to him; the Greek plural sons-in-law and a condition, if you "
   "have anyone else. The rescue is offered to Lot’s whole household."),
  'shared': ["The men asked Lot who else belonged to him in the city.", "They named sons-in-law, sons and daughters.", "He was to bring them out of the place."],
  'instructions': [ins(C, S, "Bring everyone who belongs to you out of this place."), ins(W, R, "The rescue is wider than Lot deserves; whoever he can gather may come, and the limit will be set by those who refuse.")],
  'entries': ['angels'],
  'lost': [between("Hebrew chatan, “son-in-law,” singular, is Greek gambroi, plural; Hebrew ve-khol asher-lekha ba-ir hotse, “and all who are yours in the city, bring out,” a command, is Greek ē ei tis soi allos estin en tē polei, exagage, “or if you have anyone else in the city, bring out,” conditional. Latin and King James follow the Hebrew.")]},

 '19:13': {
  'received': "They would destroy the place because its outcry had risen before the Lord, who had sent them.",
  'explain': ("The angels state the sentence and its ground: the outcry of 18:20 has grown great before the Lord, and the Lord has sent them. The "
   "Hebrew says YHWH twice; the Greek the Lord twice; the Latin says destroy them where the others say destroy it. Lot now knows what Abraham knew."),
  'shared': ["The men are about to destroy the place.", "The outcry has grown great before the Lord.", "The Lord sent them to destroy it."],
  'instructions': [ins(K, S, "The angels revealed that the Lord had sent them to destroy Sodom."), ins(W, R, "The messengers who ate at Lot’s table are the executioners of his city; mercy and judgement come through the same door.")],
  'entries': ['angels', 'yhwh-yahweh'],
  'lost': [between("Hebrew gadelah, “has grown great,” is Greek hypsōthē, “has risen”; Hebrew le-shachatah, “to destroy it,” is Greek ektripsai autēn, “to wipe it out.” Latin “destroy them” changes the object; King James follows the Hebrew.")]},

 '19:14': {
  'received': "Lot warned his sons-in-law to flee, but they thought he was joking.",
  'explain': ("Lot goes out to the men engaged or married to his daughters and warns them; they laugh. The Hebrew participle can mean men who were "
   "marrying the daughters, so betrothed; the Greek says who had taken them, completed marriages; the Latin says who were to marry them. The "
   "virgin daughters of verse 8 suggest betrothal, but the Greek is left as it stands."),
  'shared': ["Lot went out and spoke to his sons-in-law.", "He told them to leave because the Lord was destroying the city.", "They thought he was joking."],
  'instructions': [ins(K, S, "Lot’s sons-in-law disbelieved his warning."), ins(W, R, "A warning from a man who has lived as his neighbours live is heard as a joke; Lot’s years in Sodom have cost him his credit.")],
  'entries': ['yhwh-yahweh'],
  'lost': [
   loses("Hebrew loqeche venotav, “who were taking his daughters,” a participle allowing betrothal, becomes Greek tous eilēphotas tas thygateras autou, “who had taken his daughters,” a completed perfect. Hebrew YHWH is “the Lord.”"),
   between("Latin “who were to marry his daughters” reads the Hebrew as betrothal; King James “which married his daughters” as marriage. Greek paizein, “to be joking,” matches Hebrew metsacheq."),
  ]},

 '19:15': {
  'received': "At dawn the angels urged Lot to take his wife and daughters and leave, lest he perish in the city’s punishment.",
  'explain': ("Night ends and the angels press. Take your wife and the two daughters here, and go, before the city’s iniquity sweeps you away. The "
   "Hebrew word covers both the sin and its punishment; the Greek says lawless deeds in the plural and adds an explicit “go out.” The sons-in-law "
   "are not mentioned again."),
  'shared': ["Dawn came and the angels urged Lot.", "He was to take his wife and his two daughters.", "Otherwise he would perish in the city’s punishment."],
  'instructions': [ins(C, S, "Get up, take your wife and daughters, and leave the city."), ins(W, R, "Dawn is the deadline; the mercy that waited through the night will not wait through the morning.")],
  'entries': ['angels'],
  'lost': [
   keeps("Greek adds kai exelthe, “and go out,” which the Hebrew leaves implied; Hebrew ba-avon ha-ir, “in the iniquity (or punishment) of the city,” is Greek syn tais anomiais tēs poleōs, “with the lawless deeds of the city,” plural."),
   between("Latin “lest you too perish in the city’s wickedness” and King James “lest thou be consumed in the iniquity of the city” follow the Hebrew; Hebrew ha-nimtsa’ot, “who are here,” is Latin and Greek “whom you have.”"),
  ]},

 '19:16': {
  'received': "While Lot hesitated, the angels took his family by the hand, because the Lord spared him, and brought them out of the city.",
  'explain': ("Lot delays and has to be led out by the hand, with his wife and daughters, because the Lord had compassion on him. The Hebrew says he "
   "lingered and the men grasped them, then sets them outside the city; the Greek says they were troubled, calls the rescuers angels, and keeps the "
   "bringing-out for the next verse. Rescue here is literally dragging."),
  'shared': ["Lot was slow to leave.", "The angels took him, his wife and his daughters by the hand.", "They did so because the Lord spared him."],
  'instructions': [ins(K, S, "The angels led Lot’s family out by the hand because the Lord spared him."), ins(W, R, "Lot is saved against his own slowness; the compassion of the Lord does for him what his will would not.")],
  'entries': ['angels', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew va-yitmahmah, “he lingered,” singular, becomes Greek kai etarachthēsan, “and they were troubled,” plural; Hebrew ha-anashim, “the men,” becomes hoi angeloi, “the angels”; Hebrew be-chemlat YHWH, “in the compassion of YHWH,” becomes en tō pheisasthai kyrion, “because the Lord spared.” The Hebrew clause “they brought him out and set him outside the city” has no counterpart here in the Greek, which continues in 19:17."),
   between("Latin “as he delayed, they took his hand … because the Lord spared him” keeps the lingering and the sparing; King James “while he lingered … the LORD being merciful unto him: and they brought him forth” follows the Hebrew."),
  ]},

 '19:17': {
  'received': "Once outside, Lot was told to flee for his life to the hills without looking back or stopping in the plain.",
  'explain': ("The instructions for flight: run, do not look back, do not stop in the plain, reach the hills. The Hebrew has a single speaker, he said; "
   "the Greek plural, they said, and stresses saving your own life. The Latin here supplies the setting outside the city that the Greek moved from "
   "verse 16. Jesus will recall Lot’s wife at this point."),
  'shared': ["They had brought them outside.", "Lot was told to escape for his life and not look back.", "He was to flee to the hill country and not stop in the plain."],
  'instructions': [ins(C, S, "Escape for your life; do not look back or stop in the plain; flee to the hills."), ins(W, R, "“Do not look back” is the whole discipline of flight; the one who turns to see what is lost is lost with it.")],
  'entries': ['angels'],
  'lost': [
   loses("Hebrew va-yomer, “he said,” singular, becomes Greek kai eipan, “they said,” plural; Hebrew himmalet al-nafshekha, “escape for your life,” becomes sōzōn sōze tēn seautou psychēn, “saving, save your own life,” with the pronoun stressed; the Hebrew ends “lest you be swept away,” the Greek adds “with them.”"),
   between("Latin “they brought him out and set him outside the city, and there they spoke to him” supplies the clause the Greek lacks in 19:16; King James “he said” follows the Hebrew singular. Luke 17:31–32 recalls the command."),
  ]},

 '19:18': {
  'received': "Lot answered, pleading with his rescuer.",
  'explain': ("Lot speaks to the two but addresses one as Lord, in the singular, as Abraham did in 18:3. The Hebrew begins with a refusal, no, please, "
   "Lord; the Greek with a petition, I beg you, Lord. The Hebrew pointing again makes the address the divine title; the Latin and King James read "
   "my lord. His request follows."),
  'shared': ["Lot spoke to them.", "He addressed one as Lord.", "He began a plea."],
  'instructions': [ins(K, S, "Lot pleaded with the angel rather than simply obeying."), ins(W, R, "Even in flight Lot bargains; the man dragged out by the hand still has terms.")],
  'entries': ['lord-translation'],
  'lost': [between("Hebrew al-na Adonai, “no, please, Lord,” a refusal, is Greek deomai, kyrie, “I beg you, Lord,” a petition. Latin “please, my lord” and King James “Oh, not so, my LORD” divide; both read the address as a lord.")]},

 '19:19': {
  'received': "Lot acknowledged the great kindness shown him but feared he could not reach the hills before disaster overtook him.",
  'explain': ("Lot thanks and then objects. The Hebrew says he has found favour and his rescuer has shown great kindness, chesed, in saving his life; "
   "the Greek says he has found mercy and that his rescuer has magnified his righteousness, reading the Hebrew kindness as faithful dealing. The "
   "objection is the same: the hills are too far, disaster will catch him."),
  'shared': ["Lot has found favour with his rescuer.", "His life has been saved by great kindness.", "He cannot reach the hill country before disaster overtakes him."],
  'instructions': [ins(K, S, "Lot feared he could not reach the hills in time."), ins(W, R, "Gratitude and distrust in one sentence; Lot believes he has been saved and does not believe he will be.")],
  'entries': [],
  'lost': [
   loses("Hebrew chen, “favour,” becomes Greek eleos, “mercy”; Hebrew va-tagdel chasdekha, “you have magnified your kindness,” becomes emegalynas tēn dikaiosynēn sou, “you have magnified your righteousness”; the relational chesed is read as righteousness. Hebrew ha-ra‘ah, “the disaster,” is Greek ta kaka, “calamities,” plural."),
   between("Latin “found favour … shown me great mercy” and King James “found grace … magnified thy mercy” keep favour and mercy with the Hebrew."),
  ]},

 '19:20': {
  'received': "Lot asked to flee instead to a small nearby city, where his life might be saved.",
  'explain': ("Lot proposes a nearer refuge and argues from its smallness: it is only a little place, surely it can be spared. The Hebrew asks permission, "
   "please let me escape there; the Greek states the result, I will be saved there. The question “is it not small?” is in all four. The city will be "
   "named from this plea."),
  'shared': ["A nearby city is close enough to flee to.", "It is small.", "Lot asks that his life be preserved there."],
  'instructions': [ins(K, S, "Lot asked to take refuge in the small city nearby."), ins(W, R, "Lot pleads for a city on the ground that it is too small to matter; the plea works, and smallness becomes its name.")],
  'entries': [],
  'lost': [between("Hebrew immaletah na shammah, “please let me escape there,” a request, is Greek ekei sōthēsomai, “there I will be saved,” a statement; Hebrew ha-lo mits‘ar hi, “is it not small?”, is kept as ou mikra estin. Latin “I shall be safe there” follows the Greek; King James “Oh, let me escape thither” the Hebrew.")]},

 '19:21': {
  'received': "The angel granted this too and promised not to overthrow the city Lot had named.",
  'explain': ("The request is granted with an idiom: the Hebrew lifting of the face, the Greek regarding of the face, both meaning to show favour, not "
   "to admire. The Latin says he has accepted Lot’s prayers. The city of the plea is spared for Lot, as Sodom would have been for ten."),
  'shared': ["The angel answered Lot.", "He granted this request as well.", "He will not overthrow the city Lot named."],
  'instructions': [ins(K, S, "Lot’s request was granted and Zoar spared."), ins(W, R, "One city of the five is spared, not for its righteousness but for one man’s plea; Abraham’s principle survives in a small way.")],
  'entries': [],
  'lost': [between("Hebrew nasati fanekha, “I have lifted your face,” and Greek ethaumasa sou to prosōpon, “I have regarded your face,” are the same idiom of favour in two languages; Latin “I have accepted your prayers” translates the sense; King James “I have accepted thee” likewise.")]},

 '19:22': {
  'received': "Lot was told to hurry, since nothing could be done until he arrived; so the city was named Zoar.",
  'explain': ("The destruction waits on Lot’s safety: I can do nothing until you are there. The city is named Zoar, “small,” from Lot’s plea; the pun "
   "is audible in Hebrew and lost in the Greek transliteration. The Latin calls it Segor. The sparing of Zoar is the one concession the plain receives."),
  'shared': ["Lot is told to hurry to the city.", "Nothing can be done until he arrives.", "The city was named Zoar."],
  'instructions': [ins(K, S, "The judgement waited on Lot’s arrival at Zoar."), ins(W, R, "God’s fire waits for one slow man; the righteous few hold back judgement by their very presence.")],
  'entries': [],
  'lost': [between("Hebrew Tso‘ar echoes mits‘ar, “small,” in 19:20; Greek Sēgōr is a spelling without the pun; Latin Segor likewise. Hebrew lo ukhal la‘asot davar, “I cannot do anything,” is Greek ou dynēsomai poiēsai pragma, “I will not be able to do anything.”")]},

 '19:23': {
  'received': "The sun had risen when Lot entered Zoar.",
  'explain': ("A time stamp: sunrise, and Lot inside the walls. The Hebrew and Latin say the sun had risen when he came; the Greek that the sun rose "
   "and Lot entered. The fire falls in daylight, in the next verse."),
  'shared': ["The sun rose over the earth.", "Lot entered Zoar.", "The two events coincide."],
  'instructions': [ins(K, S, "Lot reached Zoar at sunrise.")],
  'entries': [],
  'lost': [between("Hebrew ha-shemesh yatsa … ve-Lot ba, “the sun had come out … and Lot came,” is Greek ho hēlios exēlthen … kai Lōt eisēlthen, two coordinated past events. Latin and King James agree in sense.")]},

 '19:24': {
  'received': "The Lord rained sulfur and fire on Sodom and Gomorrah from the Lord out of heaven.",
  'explain': ("The destruction is told in one sentence, with the divine name twice: the Lord rained from the Lord out of heaven. All four versions keep "
   "the repetition. Later theology has read much into the doubling; the verse itself gives fire and sulfur from the sky on the two cities. Jesus and "
   "the apostles will cite this as the pattern of sudden judgement."),
  'shared': ["The Lord rained on Sodom and Gomorrah.", "He rained sulfur and fire.", "It came from the Lord out of heaven."],
  'instructions': [ins(K, S, "The Lord destroyed Sodom and Gomorrah with fire and sulfur from heaven."), ins(W, R, "The fire is said to come from the Lord twice over; the text will not let the judgement be blamed on nature or on angels.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew YHWH … me’et YHWH min-ha-shamayim and Greek kyrios … para kyriou ek tou ouranou both repeat the name; Latin Dominus … a Domino and King James “the LORD … from the LORD” likewise. Hebrew gofrit va-esh, “sulfur and fire,” is Greek theion kai pyr. Luke 17:29 and 2 Peter 2:6 cite the fall.")]},

 '19:25': {
  'received': "He overthrew the cities, the whole plain, every inhabitant and all that grew from the ground.",
  'explain': ("The scope is total: cities, region, people, vegetation. The Hebrew says the growth of the ground; the Greek everything that grew from "
   "the earth. The plain Lot chose for its greenness in 13:10 is stripped bare. The verb overthrow becomes the standing word for Sodom’s fate."),
  'shared': ["He overthrew those cities.", "He overthrew the whole region and all its inhabitants.", "He destroyed what grew from the ground."],
  'instructions': [ins(K, S, "The whole plain and everything in it was overthrown."), ins(W, R, "The green land of Lot’s choosing is made barren; what was chosen by sight is unmade to the roots.")],
  'entries': [],
  'lost': [between("Hebrew tsemach ha-adamah, “the growth of the ground,” is Greek panta ta anatellonta ek tēs gēs, “everything that grew from the earth,” with “everything” added. Latin “everything growing upon the ground” follows the Greek; King James “that which grew upon the ground” the Hebrew.")]},

 '19:26': {
  'received': "Lot’s wife looked back and became a pillar of salt.",
  'explain': ("One sentence, no explanation. She looked back, against the command of verse 17, and became a pillar of salt, as the Dead Sea shore "
   "still shows salt formations. The Hebrew says she looked back from behind him, placing her behind Lot; the Greek says she looked backward without "
   "the relative position. Jesus says, remember Lot’s wife."),
  'shared': ["Lot’s wife looked back.", "She became a pillar of salt.", "She disobeyed the command not to look behind."],
  'instructions': [ins(K, S, "Lot’s wife looked back and became a pillar of salt."), ins(W, R, "The look back is the last tie to Sodom and it is fatal; Jesus makes her the warning for all who cannot leave what is being judged.")],
  'entries': [],
  'lost': [between("Hebrew me-acharav, “from behind him,” locating her behind Lot, is absent from Greek eis ta opisō, “backward”; Latin “behind her” and King James “from behind him” divide. Hebrew netsiv melach and Greek stēlē halos are both “pillar of salt.” Luke 17:32 is the echo.")]},

 '19:27': {
  'received': "Early in the morning Abraham went to the place where he had stood before the Lord.",
  'explain': ("The narrative returns to Abraham, who rises early and goes back to the spot of his intercession in 18:22. He has not been told the outcome. "
   "The Hebrew says he stood before YHWH; the Latin with the Lord. The versions agree."),
  'shared': ["Abraham rose early in the morning.", "He went to the place of his intercession.", "It was where he had stood before the Lord."],
  'instructions': [ins(K, S, "Abraham returned at dawn to the place where he had pleaded for Sodom."), ins(W, R, "The intercessor goes back to the place of prayer to see the answer; prayer and its outcome are joined at one spot.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [between("Hebrew lifne YHWH, “before YHWH,” is Greek enantion kyriou, “before the Lord”; Latin cum Domino, “with the Lord.” King James follows the Hebrew.")]},

 '19:28': {
  'received': "Abraham looked toward Sodom and Gomorrah and saw the land smoking like a furnace.",
  'explain': ("From the heights he sees the answer to his plea. The Hebrew says smoke rose from the land like the smoke of a furnace; the Greek a flame "
   "rising like the vapour of a furnace; the Latin ashes rising like furnace smoke. Smoke, flame and ash belong to one scene, but each column names "
   "a different thing seen. There were not ten."),
  'shared': ["Abraham looked toward Sodom and Gomorrah and the whole plain.", "He saw something rising from the land.", "It was like a furnace."],
  'instructions': [ins(K, S, "Abraham saw the destruction of the plain from a distance."), ins(W, R, "The man who argued for the city sees it burn; the prayer was answered in the only way the city allowed.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew qitor ha-arets, “the smoke of the land,” and ke-qitor ha-kivshan, “like the smoke of the furnace,” become Greek phlox, “a flame,” rising hōsei atmis kaminou, “like the vapour of a furnace”; the thing seen changes from smoke to flame."),
   between("Latin favilla, “ashes,” rising like furnace smoke, is a third image; King James “the smoke of the country … as the smoke of a furnace” follows the Hebrew."),
  ]},

 '19:29': {
  'received': "When God destroyed the cities of the plain, he remembered Abraham and brought Lot out of the overthrow.",
  'explain': ("The narrator explains Lot’s rescue: God remembered Abraham. Lot is saved for his uncle’s sake, not his own. The Hebrew says God destroyed, "
   "God remembered, he overthrew; the Greek says the Lord wiped out all the cities, God remembered, the Lord overthrew; the Latin names God only. "
   "The remembering is the word of 8:1."),
  'shared': ["God destroyed the cities of the plain.", "God remembered Abraham.", "He sent Lot out of the overthrow of the cities where he had lived."],
  'instructions': [ins(K, S, "Lot was saved because God remembered Abraham."), ins(W, R, "Lot owes his life to another man’s standing with God; the righteous do save others, though not the city.")],
  'entries': ['abraham', 'god-theos', 'yhwh-yahweh'],
  'lost': [between("Hebrew Elohim … Elohim … va-yahafokh, “God … God … he overthrew,” is Greek kyrios … ho theos … kyrios, “the Lord … God … the Lord,” with pasas, “all,” added to the cities. Latin “God overthrew … He remembered” and King James “God destroyed … God remembered … he overthrew” follow the Hebrew.")]},

 '19:30': {
  'received': "Lot left Zoar out of fear and lived with his two daughters in a cave in the hills.",
  'explain': ("Lot ends where he was first told to go: the hills. He leaves the city spared for him, afraid to stay, and lives in a cave with his two "
   "daughters, his wife lost and his sons-in-law dead. The Greek repeats “with him” at the end. The man who chose the green plain ends in a hole in the rock."),
  'shared': ["Lot went up from Zoar.", "He lived in the hill country because he was afraid to stay in Zoar.", "He lived in a cave with his two daughters."],
  'instructions': [ins(K, S, "Lot left Zoar for a cave in the hills with his daughters."), ins(W, R, "Fear drives Lot even from the refuge he begged for; the rescued man cannot rest in his rescue.")],
  'entries': [],
  'lost': [between("Hebrew ba-har, “in the hill country,” is Greek en tō orei, “in the mountain”; the Greek adds met’ autou, “with him,” after the daughters at the end. Latin and King James agree in sense.")]},

 '19:31': {
  'received': "The elder daughter told the younger that their father was old and there was no man left to marry them.",
  'explain': ("The daughters reckon themselves the last people alive, or at least without any man in the land to marry. The text gives their assessment, "
   "not the narrator’s. The Hebrew calls her the firstborn; the Greek the older. “The way of all the earth” is the ordinary way of marriage. The plan follows."),
  'shared': ["The elder daughter spoke to the younger.", "Their father is old.", "There is no man in the land to marry them in the usual way."],
  'instructions': [ins(K, S, "Lot’s daughters believed no man was left to give them children."), ins(W, R, "Despair reasons from what it can see; the daughters have watched a world end and conclude the world has ended.")],
  'entries': [],
  'lost': [between("Hebrew ha-bekhirah, “the firstborn,” is Greek hē presbytera, “the older”; Hebrew ein ba-arets, “there is no one in the land,” is Greek oudeis estin epi tēs gēs, “no one on the earth,” the same word in both languages. Latin “no man remains in the land” and King James “not a man in the earth” divide.")]},

 '19:32': {
  'received': "She proposed to get their father drunk and lie with him to preserve his line.",
  'explain': ("The plan is stated as a duty: offspring from our father. The Hebrew says preserve seed; the Greek raise up seed, the phrase later used of "
   "a brother’s duty to a dead man’s widow; the Latin says make him drunk. The daughters do with wine what Sarai did with Hagar, force the future. "
   "Noah’s wine and nakedness are the nearer echo."),
  'shared': ["Come, let us give our father wine to drink.", "Let us lie with him.", "So that we may keep offspring from our father."],
  'instructions': [ins(K, S, "Lot’s daughters planned to conceive by their drunken father."), ins(W, R, "The desire for children, good in itself, is pursued by a crime; Scripture records it as it recorded Lot’s offer in verse 8, without a word of approval.")],
  'entries': [],
  'lost': [between("Hebrew u-nechayyeh me-avinu zara, “that we may keep alive seed from our father,” is Greek kai exanastēsōmen ek tou patros hēmōn sperma, “that we may raise up seed from our father,” the verb of the levirate (Deuteronomy 25:7; Matthew 22:24). Latin “make him drunk” and King James “preserve seed” divide.")]},

 '19:33': {
  'received': "That night they made their father drunk, and the elder lay with him without his knowing.",
  'explain': ("The deed is done, and the narrator insists on Lot’s ignorance: he did not know when she lay down or rose. The Greek repeats “that night” "
   "with the lying; the Latin adds “his daughter.” Lot’s drunkenness is his part in the guilt; the daughters’ act is theirs."),
  'shared': ["They gave their father wine that night.", "The elder went in and lay with her father.", "He did not know when she lay down or arose."],
  'instructions': [ins(K, S, "The elder daughter conceived by her drunken father, who knew nothing of it."), ins(W, R, "“He did not know” excuses Lot of the act and accuses him of the wine; drunkenness is how a man is made ignorant of his own life.")],
  'entries': [],
  'lost': [between("Greek repeats tēn nykta ekeinēn, “that night,” with the lying; the Hebrew has it once. Latin adds “his daughter”; King James follows the Hebrew.")]},

 '19:34': {
  'received': "Next day the elder told the younger to do the same that night.",
  'explain': ("The plan is repeated for the younger, in almost the same words as verse 32. The Hebrew has the elder say my father and last night; the "
   "Greek our father and yesterday. The phrase for the purpose, preserve or raise up seed, repeats. The daughters act in turn, as Sarah’s and Rachel’s "
   "maids will."),
  'shared': ["The next day the elder spoke to the younger.", "She had lain with their father the night before.", "They would give him wine again so the younger could lie with him and preserve offspring."],
  'instructions': [ins(K, S, "The daughters repeated the plan the second night.")],
  'entries': [],
  'lost': [between("Hebrew et-avi emesh, “with my father last night,” is Greek meta tou patros hēmōn chthes, “with our father yesterday”; Hebrew nechayyeh is again Greek exanastēsōmen. Latin and King James follow the Hebrew.")]},

 '19:35': {
  'received': "They made him drunk again, and the younger lay with him without his knowing.",
  'explain': ("The second night mirrors the first, and again the narrator insists on Lot’s ignorance. The Hebrew says the younger arose and lay with him; "
   "the Greek that she went in and lay with her father; the Latin adds “again.” The repetition is deliberate and bleak."),
  'shared': ["They gave their father wine that night also.", "The younger lay with him.", "He did not know when she lay down or arose."],
  'instructions': [ins(K, S, "The younger daughter also conceived by her drunken father.")],
  'entries': [],
  'lost': [between("Hebrew va-taqom … immo, “arose … with him,” is Greek eiselthousa … meta tou patros autēs, “going in … with her father.” Latin “again he did not perceive” adds the adverb; King James follows the Hebrew.")]},

 '19:36': {
  'received': "Both of Lot’s daughters conceived by their father.",
  'explain': ("The result is stated flatly. Both conceive; the plan has worked. The versions agree. Nothing is said of what Lot learned afterward, "
   "and Lot is not heard of again."),
  'shared': ["Both daughters conceived.", "They conceived by their father.", "Lot’s line continues through incest."],
  'instructions': [ins(K, S, "Both of Lot’s daughters bore children by their father."), ins(W, R, "The last word on Lot is silence; the man saved for Abraham’s sake disappears into a cave and a scandal.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James agree in every word.")]},

 '19:37': {
  'received': "The elder bore Moab, ancestor of the Moabites.",
  'explain': ("The sons are nations. The elder’s son is Moab, and the Hebrew gives the name without comment; the Greek adds the explanation, “from "
   "my father,” making the connection to the incest audible. The Moabites will be Israel’s neighbours and enemies, and Ruth the Moabitess will be "
   "David’s ancestor. The explanation reports the naming; it does not approve the act."),
  'shared': ["The elder daughter bore a son.", "She named him Moab.", "He is the father of the Moabites to this day."],
  'instructions': [ins(K, S, "Moab, father of the Moabites, was born of Lot’s elder daughter."), ins(W, R, "A people is born from a crime and still receives a place in the story; Ruth will come from Moab to the line of David.")],
  'entries': [],
  'lost': [
   keeps("Greek adds legousa, Ek tou patros mou, “saying, From my father,” an etymology the Hebrew does not give; the Greek hears me-av, “from father,” in Moab."),
   between("Latin and King James give the name without explanation, with the Hebrew. Ruth 1:4 and 4:17 bring the Moabitess into David’s line."),
  ]},

 '19:38': {
  'received': "The younger bore Ben-ammi, ancestor of the Ammonites.",
  'explain': ("The younger’s son is Ben-ammi, “son of my people,” in the Hebrew, ancestor of the Ammonites; the Greek calls him Amman and glosses the "
   "name “son of my kin”; the Latin calls him Ammon and glosses “son of my people.” The two peoples east of the Jordan are given an origin in Lot, "
   "Abraham’s nephew, kin to Israel and often its enemies."),
  'shared': ["The younger also bore a son.", "His name relates him to his mother’s people.", "He is the father of the Ammonites to this day."],
  'instructions': [ins(K, S, "The Ammonites descend from Lot’s younger daughter."), ins(W, R, "Moab and Ammon are family to Israel by this chapter; the law will remember their kinship and their origin together.")],
  'entries': [],
  'lost': [
   loses("Hebrew Ben-Ammi, “son of my people,” a name that is its own explanation, becomes Greek Amman with a separate gloss, huios tou genous mou, “son of my kin”; Hebrew bene Ammon, “sons of Ammon,” is Greek Ammanitai."),
   between("Latin “Ammon, that is, Son of My People” glosses like the Greek but keeps the sense of the Hebrew name; King James “Benammi … children of Ammon” follows the Hebrew. Deuteronomy 2:19 and 23:3 remember both peoples."),
  ]},
 }
}
