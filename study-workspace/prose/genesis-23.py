# Study prose for Genesis 23 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 23,
 'chapterNote': (
  "Sarah’s death and the purchase of her tomb are told alike in every column, with the same courtesies and the same price. What varies is names and "
  "the shape of the bargaining. The Hebrew keeps the lifespan formula “these were the years of Sarah’s life,” Kiriath-arba, “a prince of God,” the name "
  "Machpelah, the city gate as the public place, Ephron’s “no, my lord,” a difficult appeal in 23:13, shekels, and silver weighed out. The Greek keeps "
  "“the city of Arbok, which is in the hollow,” “a king from God,” “the double cave” for Machpelah throughout, “all who entered the city,” Ephron’s “come "
  "to my side,” Abraham’s “since you are on my side,” didrachms, and silver paid rather than weighed. The Latin and King James follow the Hebrew; the "
  "Latin also says “double cave.”"),
 'verses': {

 '23:1': {
  'received': "Sarah lived a hundred and twenty-seven years.",
  'explain': ("Sarah is the only woman whose age at death Scripture records. The Hebrew counts it in the old style, a hundred years and twenty years and "
   "seven years, and closes with the formula these were the years of Sarah’s life; the Greek and Latin give the total and drop the formula. She was "
   "ninety at Isaac’s birth, so Isaac is thirty-seven."),
  'shared': ["Sarah lived.", "Her years were a hundred and twenty-seven.", "Her life is summed up."],
  'instructions': [ins(K, S, "Sarah died at a hundred and twenty-seven."), ins(W, R, "The mother of the promise is given the honour of a counted life, like the patriarchs; no other woman in Scripture receives it.")],
  'entries': ['sarah'],
  'lost': [
   loses("Hebrew me’ah shanah ve-esrim shanah ve-sheva shanim, “a hundred years and twenty years and seven years,” repeats the noun, and the closing shene chayye Sarah, “the years of Sarah’s life,” is absent from the Greek, which gives the total once."),
   between("Latin “lived one hundred twenty-seven years” follows the Greek’s brevity; King James “these were the years of the life of Sarah” keeps the Hebrew formula."),
  ]},

 '23:2': {
  'received': "Sarah died at Hebron in Canaan, and Abraham came to mourn and weep for her.",
  'explain': ("She dies at Hebron, where Abraham had lived by the oaks of Mamre. The Hebrew names the town Kiriath-arba, city of four, and identifies it "
   "as Hebron; the Greek says the city of Arbok, which is in the hollow, adding a description, and names Sarah again; the Latin the city of Arba. Abraham "
   "comes, from Beersheba perhaps, to mourn: the Hebrew says mourn and weep, the Greek lament and mourn."),
  'shared': ["Sarah died at Kiriath-arba, which is Hebron.", "It was in the land of Canaan.", "Abraham came to mourn and weep for her."],
  'instructions': [ins(K, S, "Sarah died at Hebron and Abraham mourned her."), ins(W, R, "The first recorded mourning in Scripture is a husband’s for his wife; the patriarch weeps before he negotiates.")],
  'entries': ['sarah', 'abraham', 'hebron', 'canaan'],
  'lost': [
   loses("Hebrew Qiryat Arba, “Kiriath-arba,” becomes Greek polei Arbok, “the city of Arbok,” and the Greek adds hē estin en tō koilōmati, “which is in the hollow,” a phrase the Hebrew lacks; Hebrew lispod le-Sarah ve-livkotah, “to mourn Sarah and weep for her,” is Greek kopsasthai Sarran kai penthēsai, “to lament Sarah and mourn.”"),
   between("Latin “the city of Arba, which is Hebron” and King James “Kirjatharba; the same is Hebron” keep the name without the hollow; the Latin says “weep for her” without naming Sarah again."),
  ]},

 '23:3': {
  'received': "Abraham rose from beside his dead and spoke to the sons of Heth.",
  'explain': ("Mourning gives way to business. Abraham rises from before the body and addresses the Hittites, the sons of Heth, who hold Hebron. The "
   "Hebrew says from before his dead; the Greek from his dead; the Latin from his mourning duties. “His dead” is Sarah, named by her loss."),
  'shared': ["Abraham rose from his dead.", "He spoke to the sons of Heth.", "He turned from mourning to the matter of burial."],
  'instructions': [ins(K, S, "Abraham approached the Hittites about a burial place.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew me-al pene meto, “from before the face of his dead,” is Greek apo tou nekrou autou, “from his dead”; Latin “from his mourning duties” paraphrases. King James follows the Hebrew.")]},

 '23:4': {
  'received': "Abraham, a stranger and sojourner, asked them for a burial property to bury his dead.",
  'explain': ("Abraham owns nothing in the land of promise, and says so: a stranger and a resident alien. He asks for burial property, the Hebrew word "
   "for a holding, so that the grave will be his. The Hebrew pairs foreigner and resident; the Greek sojourner and temporary resident; the Latin asks "
   "for the right to a burial place. Hebrews makes this confession the mark of the patriarchs’ faith."),
  'shared': ["Abraham is a stranger and sojourner among them.", "He asks for burial property among them.", "He wants to bury his dead."],
  'instructions': [ins(K, S, "Abraham asked for a burial holding as a landless stranger."), ins(W, R, "The heir of the land asks for a grave in it; the first ground Abraham owns is the ground that holds his dead.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew ger ve-toshav, “a stranger and a resident,” is Greek paroikos kai parepidēmos, “a sojourner and a temporary resident,” the pair 1 Peter 2:11 uses; Hebrew achuzzat-qever, “a holding of a grave,” is Greek ktēsin taphou; Hebrew mi-lefanai, “from before me,” is Greek ap’ emou, “away from me.” Latin and King James follow the Hebrew. Hebrews 11:13 reads the confession.")]},

 '23:5': {
  'received': "The sons of Heth answered Abraham.",
  'explain': ("A formal introduction to a formal reply. The negotiation proceeds in the forms of courtesy. The Hebrew and Greek name Abraham; the Latin "
   "says simply they answered."),
  'shared': ["The sons of Heth answered.", "They spoke to Abraham.", "A reply follows."],
  'instructions': [ins(K, S, "The Hittites replied to Abraham’s request.")],
  'entries': [],
  'lost': [between("Hebrew and Greek name Abraham; Latin “the sons of Heth answered” drops it; King James “answered Abraham, saying unto him.”")]},

 '23:6': {
  'received': "They honoured Abraham as a prince of God and offered him the choice of their tombs.",
  'explain': ("The Hittites answer generously: bury your dead in the best of our tombs, no one will refuse you. They call Abraham a prince of God in the "
   "Hebrew, a king from God in the Greek, a mighty prince in the King James; the Greek opens with no, lord, as Ephron will in verse 11. The honorific is "
   "courtesy, not a coronation. A borrowed tomb is not what Abraham wants."),
  'shared': ["The sons of Heth ask Abraham to hear them.", "They call him a prince of God among them.", "They offer him the choicest of their tombs."],
  'instructions': [ins(K, S, "The Hittites offered Abraham free use of their tombs."), ins(W, R, "The stranger is called a prince; the land’s people see in Abraham what he does not claim for himself.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew nesi Elohim, “a prince of God,” becomes Greek basileus para theou, “a king from God”; the Greek adds mē, kyrie, “no, lord,” at the start, which the Hebrew lacks here."),
   between("Latin “a prince of God” follows the Hebrew; King James “a mighty prince” reads Elohim as a superlative."),
  ]},

 '23:7': {
  'received': "Abraham rose and bowed to the people of the land, the sons of Heth.",
  'explain': ("Abraham answers honour with a bow. He rises and bows to the whole assembly, the people of the land. The versions agree exactly."),
  'shared': ["Abraham rose.", "He bowed to the people of the land.", "They were the sons of Heth."],
  'instructions': [ins(K, S, "Abraham bowed to the Hittite assembly."), ins(W, R, "The prince of God bows to the people whose land is promised to him; courtesy costs him nothing and he pays it in full.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew, Greek, Latin and King James agree in every word.")]},

 '23:8': {
  'received': "Abraham asked them, if they were willing, to intercede for him with Ephron son of Zohar.",
  'explain': ("Abraham declines the offer of a borrowed tomb and names what he wants: a particular cave, owned by a particular man. He asks the assembly "
   "to approach Ephron for him, the proper form. The Hebrew says intercede; the Greek speak for me, and names Abraham. The Greek form of Zohar is Saar."),
  'shared': ["Abraham spoke to the sons of Heth.", "If they are willing that he bury his dead, they should hear him.", "He asks them to intercede with Ephron son of Zohar."],
  'instructions': [ins(K, S, "Abraham asked the assembly to approach Ephron on his behalf.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew u-fig‘u-li, “and intercede for me,” is Greek kai lalēsate peri emou, “and speak for me”; Hebrew Tsochar is Greek Saar, rendered Zohar. Latin “intercede for me” and King James “intreat for me” follow the Hebrew; the Latin drops “out of my sight.”")]},

 '23:9': {
  'received': "He asked that Ephron sell him the cave of Machpelah at the edge of his field, for full price, as a burial holding.",
  'explain': ("The property is named: the cave of Machpelah at the edge of Ephron’s field, for its full price in silver. The Hebrew keeps the name "
   "Machpelah; the Greek and Latin translate it, the double cave, and the Greek says in a part of his field. Abraham will not take it as a gift; the "
   "grave must be bought so that it is his."),
  'shared': ["Abraham asks for the cave of Machpelah that Ephron owns.", "It is at the edge of his field.", "He will pay its full price for it as burial property."],
  'instructions': [ins(K, S, "Abraham asked to buy the cave of Machpelah at full price."), ins(W, R, "Abraham insists on paying; a gift could be reclaimed, a purchase before witnesses cannot.")],
  'entries': ['abraham', 'hebron'],
  'lost': [
   loses("Hebrew me‘arat ha-Makhpelah, “the cave of Machpelah,” a name, becomes Greek to spēlaion to diploun, “the double cave,” a translation, here and throughout; Hebrew bi-qtseh sadehu, “at the edge of his field,” becomes en merei tou agrou autou, “in a part of his field”; Hebrew be-khesef male, “for full silver,” becomes argyriou tou axiou, “for its proper value in silver.”"),
   between("Latin “the double cave … at the edge of his field … a fair price” translates the name like the Greek but keeps the edge; King James “the cave of Machpelah … in the end of his field” follows the Hebrew."),
  ]},

 '23:10': {
  'received': "Ephron, who was present, answered Abraham publicly before the sons of Heth and all who came to the city gate.",
  'explain': ("Ephron is in the assembly and answers for himself, in public, before witnesses. The Hebrew sets the scene at the city gate, where business "
   "was done; the Greek says all who entered the city, without the gate. The Hebrew and Greek call him Ephron the Hittite; the Latin omits it. The "
   "publicity matters for what follows."),
  'shared': ["Ephron was sitting among the sons of Heth.", "He answered Abraham.", "He spoke in the hearing of the sons of Heth and all who came to the city."],
  'instructions': [ins(K, S, "Ephron answered Abraham before public witnesses."), ins(W, R, "The sale is made in the gate, before everyone; Abraham’s title to the grave will rest on what the whole town heard.")],
  'entries': [],
  'lost': [
   loses("Hebrew le-khol ba’e sha‘ar-iro, “before all who entered the gate of his city,” becomes Greek pasin tois eisporeuomenois eis tēn polin, “all who entered the city”; the gate is gone."),
   between("Latin “everyone entering his city’s gate” and King James “all that went in at the gate of his city” keep the gate; the Latin drops “the Hittite” and the sons of Heth."),
  ]},

 '23:11': {
  'received': "Ephron offered the field and the cave as a gift before his people, and told Abraham to bury his dead.",
  'explain': ("Ephron counters with a gift, the field as well as the cave, offered before his people. In Near Eastern bargaining an offer to give is an "
   "opening, not a conclusion, and Abraham treats it so. The Hebrew begins no, my lord, and says I give three times; the Greek begins come to my side, "
   "lord, and compresses; the Latin not so, my lord."),
  'shared': ["Ephron asks Abraham to hear him.", "He gives him the field and the cave in it before his people.", "He tells Abraham to bury his dead."],
  'instructions': [ins(K, S, "Ephron offered the field and cave to Abraham as a gift."), ins(W, R, "A gift offered in public is the first move of a sale; both men know it, and the courtesy is real even so.")],
  'entries': [],
  'lost': [
   loses("Hebrew lo-adoni, “no, my lord,” becomes Greek par’ emoi genou, kyrie, “come to my side, lord”; the Hebrew’s triple natatti, “I give … I give … I give,” is compressed to two verbs; Hebrew bene ammi, “the sons of my people,” becomes Greek politōn mou, “my fellow citizens.”"),
   between("Latin “not so, my lord … the sons of my people” and King James “nay, my lord … the sons of my people” follow the Hebrew; the Latin compresses the gifts like the Greek."),
  ]},

 '23:12': {
  'received': "Abraham bowed before the people of the land.",
  'explain': ("A second bow, to the whole assembly, before Abraham answers Ephron. The courtesies frame every exchange. The versions agree."),
  'shared': ["Abraham bowed.", "He bowed before the people of the land.", "He acknowledged Ephron’s offer with respect."],
  'instructions': [ins(K, S, "Abraham bowed again before replying.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew, Greek, Latin and King James agree in every word.")]},

 '23:13': {
  'received': "Abraham publicly asked Ephron to accept the price of the field so that he might bury his dead there.",
  'explain': ("Abraham declines the gift and insists on paying, before the same witnesses. The Hebrew opening is difficult, roughly if only you would "
   "hear me, I give the price of the field; the Greek says since you are on my side, hear me, answering Ephron’s come to my side; the Latin please hear "
   "me. In all, the money is to be taken so that the burial is on bought ground."),
  'shared': ["Abraham spoke to Ephron in the hearing of the people.", "He asks Ephron to take the price of the field.", "Then he will bury his dead there."],
  'instructions': [ins(K, S, "Abraham refused the gift and offered payment for the field."), ins(W, R, "The patriarch will owe nothing to the land’s people for his wife’s grave; independence is bought at full price.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew akh im-attah lu shema‘eni, “but if you, if only you would hear me,” a compressed appeal, becomes Greek epeidē pros emou ei, akouson mou, “since you are on my side, hear me,” answering 23:11; Hebrew natatti kesef ha-sadeh, “I give the silver of the field,” becomes labe to argyrion tou agrou par’ emou, “take the price of the field from me.”"),
   between("Latin “please hear me. I will give the price of the field; accept it” and King James “if thou wilt give it, I pray thee, hear me: I will give thee money” render the Hebrew appeal; the Latin says the people “stood around.”"),
  ]},

 '23:14': {
  'received': "Ephron answered Abraham.",
  'explain': ("The formal introduction again; the answer will name the price. The Hebrew and Greek name Abraham; the Latin says Ephron answered."),
  'shared': ["Ephron answered.", "He spoke to Abraham.", "The price follows."],
  'instructions': [ins(K, S, "Ephron replied to Abraham’s offer to pay.")],
  'entries': [],
  'lost': [between("Hebrew and Greek name Abraham; Latin drops the name; King James “answered Abraham, saying unto him.”")]},

 '23:15': {
  'received': "Ephron named four hundred shekels of silver as the land’s worth, calling it nothing between them, and told Abraham to bury his dead.",
  'explain': ("The price is named as if it were nothing: four hundred shekels, what is that between us? It is a high price, and the courtesy is the "
   "bargaining. The Hebrew says my lord, hear me, and shekels; the Greek no, lord, I have heard, and didrachms, the coin of the translators’ day; the "
   "Latin makes the price explicit. Abraham does not haggle."),
  'shared': ["Ephron addresses Abraham as lord.", "The land is worth four hundred shekels of silver, a trifle between them.", "He tells Abraham to bury his dead."],
  'instructions': [ins(K, S, "Ephron set the price at four hundred shekels of silver."), ins(W, R, "“What is that between me and you?” names a large sum as a trifle; the manners of the gate dress a hard bargain in soft words.")],
  'entries': [],
  'lost': [
   loses("Hebrew adoni shema‘eni, “my lord, hear me,” becomes Greek ouchi, kyrie, akēkoa gar, “no, lord, I have heard”; Hebrew sheqel-kesef, “shekels of silver,” becomes didrachmōn argyriou, “didrachms of silver.”"),
   between("Latin “my lord, hear me … four hundred shekels of silver. This is the price between you and me, but what is that?” expands; King James “my lord, hearken unto me … four hundred shekels of silver” follows the Hebrew."),
  ]},

 '23:16': {
  'received': "Abraham agreed and paid Ephron four hundred shekels of silver by the merchants’ standard, in the hearing of the sons of Heth.",
  'explain': ("The deal is done without haggling. The Hebrew says Abraham weighed out the silver, four hundred shekels current among merchants, before "
   "coins; the Greek says he paid him the silver, four hundred didrachms approved by merchants, with a verb of rendering what is due; the Latin weighed "
   "out silver of the accepted public standard. The witnesses are the same."),
  'shared': ["Abraham listened to Ephron.", "He paid him the silver Ephron had named, in the hearing of the sons of Heth.", "It was four hundred shekels of silver by the merchants’ standard."],
  'instructions': [ins(K, S, "Abraham paid the full price for the cave before witnesses."), ins(W, R, "No bargaining, no discount; Abraham pays what is asked so that the grave is his beyond dispute.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew va-yishqol, “he weighed out,” the act of paying in uncoined silver, becomes Greek apekatestēsen, “he paid” or “rendered”; Hebrew sheqel kesef over la-socher, “shekels of silver current with the merchant,” becomes tetrakosia didrachma argyriou dokimou emporois, “four hundred didrachms of silver approved by merchants.”"),
   between("Latin “weighed out the money … four hundred shekels of silver of the accepted public standard” and King James “weighed to Ephron the silver … current money with the merchant” keep the weighing with the Hebrew."),
  ]},

 '23:17': {
  'received': "So Ephron’s field at Machpelah facing Mamre, with its cave and all its trees, was conveyed",
  'explain': ("The deed is recorded in legal fullness: the field, the cave, every tree within the boundaries, facing Mamre where Abraham had lived. The "
   "Hebrew says the field at Machpelah; the Greek and Latin at the double cave, the Greek literally in the double cave, a description of locality. The "
   "sentence runs on into the next verse."),
  'shared': ["Ephron’s field at Machpelah, facing Mamre, is conveyed.", "The field, its cave and every tree in its boundaries are included.", "The transfer is secured."],
  'instructions': [ins(K, S, "The field, cave and trees of Machpelah passed to Abraham."), ins(W, R, "Every tree is listed; the first title deed in Scripture is written with a lawyer’s care, because this ground will hold six generations.")],
  'entries': ['abraham', 'hebron'],
  'lost': [between("Hebrew asher ba-Makhpelah, “which is at Machpelah,” is Greek ho ēn en tō diplō spēlaiō, “which was in the double cave,” a locality description; Hebrew va-yaqom, “was secured” or “stood,” is Greek ekyrōthē, “was established.” Latin “in which was the double cave” and King James “which was in Machpelah” divide.")]},

 '23:18': {
  'received': "to Abraham as his purchase, before the sons of Heth and all who came to the city gate.",
  'explain': ("The deed is completed: to Abraham, as a purchase, before witnesses. The Hebrew says as a purchase and names the gate; the Greek as a "
   "possession and the city; the Latin confirmed as Abraham’s possession at the gate. The land is Abraham’s by right and before all."),
  'shared': ["The field became Abraham’s.", "It was his by purchase.", "This was in the sight of the sons of Heth and all who came to the gate."],
  'instructions': [ins(K, S, "Abraham’s title to Machpelah was secured before all witnesses."), ins(W, R, "A grave bought in public is the first piece of the promised land to be held in fee; the promise begins to be owned at a funeral.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew le-miqnah, “as a purchase,” is Greek eis ktēsin, “as a possession”; Hebrew ba’e sha‘ar-iro, “who entered the gate of his city,” is again Greek “who entered the city.” Latin “as Abraham’s possession … entering that city’s gate” and King James “for a possession … at the gate of his city” keep the gate.")]},

 '23:19': {
  'received': "Then Abraham buried Sarah in the cave of the field of Machpelah facing Mamre, at Hebron in Canaan.",
  'explain': ("The burial, told with the full address: the cave, the field, Machpelah, Mamre, Hebron, Canaan. Sarah is the first to lie in the family tomb; "
   "Abraham, Isaac, Rebekah, Leah and Jacob will follow. The Hebrew keeps Machpelah; the Greek and Latin the double cave. The Latin says so Abraham buried."),
  'shared': ["Abraham buried his wife Sarah.", "It was in the cave of the field of Machpelah facing Mamre.", "That is Hebron, in the land of Canaan."],
  'instructions': [ins(K, S, "Sarah was the first buried in the cave of Machpelah."), ins(W, R, "The mother of the promise is laid in the land of the promise; her grave is the first inheritance taken up.")],
  'entries': ['sarah', 'abraham', 'hebron', 'canaan'],
  'lost': [between("Hebrew me‘arat sedeh ha-Makhpelah, “the cave of the field of Machpelah,” is Greek tō spēlaiō tou agrou tō diplō, “the double cave of the field”; Hebrew al-pene, “facing,” is Greek apenanti, “opposite.” Latin “the double cave of the field facing Mamre” and King James “the cave of the field of Machpelah before Mamre” divide. Genesis 25:9, 49:31 and 50:13 bring the others.")]},

 '23:20': {
  'received': "The field and its cave were confirmed to Abraham as a burial holding from the sons of Heth.",
  'explain': ("The chapter closes with the legal summary: field and cave, Abraham’s, for burial, from the Hittites. The Hebrew uses the standing verb of "
   "verse 17, were secured; the Greek an explicit verb of ratifying; the Latin has the sons of Heth confirm. The land promised to the offspring is now, "
   "in one small plot, Abraham’s own."),
  'shared': ["The field and its cave were made over to Abraham.", "They were his as burial property.", "They came from the sons of Heth."],
  'instructions': [ins(K, S, "Machpelah was legally Abraham’s burial property."), ins(W, R, "Of all the land promised, Abraham possessed a grave; Hebrews says he died in faith, not having received the promises, but greeting them from afar.")],
  'entries': ['abraham', 'hebron'],
  'lost': [between("Hebrew va-yaqom … le-Avraham, “stood to Abraham,” is Greek ekyrōthē … tō Abraam, “was ratified to Abraham”; Latin makes the sons of Heth the subject, “confirmed … as Abraham’s possession”; King James “were made sure unto Abraham.” Hebrews 11:13 reads the end.")]},
 }
}
