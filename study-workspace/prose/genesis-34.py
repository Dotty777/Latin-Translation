# Study prose for Genesis 34 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 34,
 'chapterNote': (
  "Dinah at Shechem: the violation, the marriage proposal, the brothers’ deceitful demand for circumcision, and Simeon and Levi’s massacre. The columns tell the "
  "same story and differ chiefly in who is named and how many are blamed. The Hebrew keeps Hamor “the Hivite,” the singular “he had defiled” in 34:13, an unnamed "
  "“they” for the brothers’ speech in 34:14, “our daughter” in 34:17, “came upon the slain,” “their wealth, children and wives,” and the singular “should he have "
  "treated our sister” at the close. The Greek keeps Hamor “the Horite,” “the son of Hamor” named in 34:5, Shechem named in 34:7 with an added “such a thing must "
  "not happen,” “for your sons,” “the land is broad,” “we will give,” the plural “they had defiled,” Simeon and Levi named as speakers in 34:14, “live among you” in "
  "34:15, “our daughters,” “in the flesh of his foreskin,” “came upon the wounded,” “in the city” added to the plunder, and the plural “should they treat our sister.” "
  "The Latin and King James follow the Hebrew; the Latin adds that Shechem “fell in love with her” and that the pain is worst on the third day."),
 'verses': {

 '34:1': {
  'received': "Dinah, Leah’s daughter by Jacob, went out to see the women of the land.",
  'explain': ("Dinah, the only daughter, goes out to visit the local women; the narrator records no blame. The versions agree."),
  'shared': ["Dinah was the daughter Leah had borne to Jacob.", "She went out.", "She went to see the women of the land."],
  'instructions': [ins(K, S, "Dinah went out among the women of Shechem."), ins(W, R, "A girl goes visiting and a city dies; the chapter begins with the most ordinary of errands.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '34:2': {
  'received': "Shechem son of Hamor the Hivite, the local prince, saw her, seized her, lay with her and violated her.",
  'explain': ("Three verbs of force: took, lay, humbled. The Hebrew says Hivite; the Greek Horite, another people; the Latin adds fell in love with her and says violating the virgin by force."),
  'shared': ["Shechem, son of Hamor, prince of the land, saw her.", "He seized her and lay with her.", "He violated her."],
  'instructions': [ins(K, S, "Shechem raped Dinah."), ins(W, R, "The narrator gives three verbs and no excuse; whatever Shechem felt afterward is told afterward, and the act is named for what it was.")],
  'entries': [],
  'lost': [loses("Hebrew ha-Chivvi, “the Hivite,” becomes Greek ho Chorraios, “the Horite.”"), between("Latin “the Hivite … and fell in love with her … violating the virgin by force” adds; King James “the Hivite … took her, and lay with her, and defiled her.”")]},

 '34:3': {
  'received': "His soul clung to Dinah; he loved the girl and spoke tenderly to her.",
  'explain': ("Desire turns to attachment after the fact. Spoke to her heart is the Hebrew idiom for comforting speech. The Latin says soothed her sadness; the Greek spoke according to her heart. His love does not alter verse 2."),
  'shared': ["His soul clung to Dinah, Jacob’s daughter.", "He loved the young woman.", "He spoke tenderly to her."],
  'instructions': [ins(K, S, "Shechem became attached to Dinah after the assault."), ins(W, R, "Tender words after violence: the narrator reports them without softening what came before, and the reader is not asked to be moved.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew va-tidbaq nafsho be-Dinah, “and his soul clung to Dinah,” is Greek prosesche tē psychē Dinas, “he was attached to the soul of Dinah”; Hebrew al-lev ha-na‘ara, “to the heart of the girl,” Greek kata tēn dianoian tēs parthenou; Latin “soothed her sadness with tender words,” King James “spake kindly unto the damsel.”")]},

 '34:4': {
  'received': "Shechem asked his father Hamor to get him the girl as a wife.",
  'explain': ("The prince expects his father to arrange it, as Samson will. Girl, yaldah, child, in the Hebrew. The versions agree."),
  'shared': ["Shechem spoke to Hamor his father.", "Take this girl for me.", "As a wife."],
  'instructions': [ins(K, S, "Shechem sought to marry Dinah.")],
  'entries': [],
  'lost': [AGREE]},

 '34:5': {
  'received': "Jacob heard that Dinah had been defiled, but his sons were in the field, so he kept silent until they came.",
  'explain': ("Jacob’s silence, the first of two in the chapter. The Greek names the son of Hamor as the offender; the Latin omits Dinah and the defilement."),
  'shared': ["Jacob heard that his daughter Dinah had been defiled.", "His sons were with the cattle in the field.", "Jacob kept silent until they came."],
  'instructions': [ins(K, S, "Jacob waited for his sons before acting."), ins(W, R, "Jacob is silent; the father who wrestled God says nothing for his daughter, and his sons will fill the silence with swords.")],
  'entries': ['jacob'],
  'lost': [keeps("An added ho huios Emmōr, “the son of Hamor,” as subject in the Greek; Hebrew timme, “he had defiled,” unnamed."), between("Latin “Jacob heard this while his sons were absent” drops Dinah and the defilement; King James follows the Hebrew.")]},

 '34:6': {
  'received': "Hamor went out to speak with Jacob.",
  'explain': ("The father negotiates for the son. The versions agree."),
  'shared': ["Hamor, Shechem’s father.", "He went out to Jacob.", "He went to speak with him."],
  'instructions': [ins(K, S, "Hamor came to negotiate with Jacob.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '34:7': {
  'received': "Jacob’s sons came from the field grieved and furious, because an outrage had been done in Israel by lying with Jacob’s daughter; such a thing is not done.",
  'explain': ("Outrage in Israel, nevalah, the word for Tamar’s rape and the Gibeah crime; Israel here is the family. The Greek names Shechem, says deeply distressed, and adds such a thing must not happen as a rule; the Latin a disgraceful, unlawful act."),
  'shared': ["Jacob’s sons came in from the field when they heard.", "They were grieved and very angry.", "He had committed an outrage in Israel by lying with Jacob’s daughter; such a thing ought not to be done."],
  'instructions': [ins(K, S, "The brothers were outraged at Dinah’s violation."), ins(W, R, "“Such a thing is not done in Israel”: the first appearance of Israel as a people with a standard. The standard is right and the brothers will break it themselves.")],
  'entries': ['jacob'],
  'lost': [keeps("An added Sychem, “Shechem,” as subject in the Greek, katenychthēsan, “were deeply pierced,” for Hebrew va-yit‘atzvu, “were grieved,” and kai ouch houtōs estai, “and so it shall not be,” added after the Hebrew’s ve-khen lo ye‘aseh, “and so it is not done.”"), between("Latin “a disgraceful thing in Israel and committed an unlawful act” and King James “wrought folly in Israel” follow the Hebrew.")]},

 '34:8': {
  'received': "Hamor said his son Shechem’s soul longed for their daughter; give her to him as wife.",
  'explain': ("The proposal, made to the brothers as well as the father. The versions agree."),
  'shared': ["Hamor spoke to them.", "The soul of my son Shechem longs for your daughter.", "Give her to him as a wife."],
  'instructions': [ins(K, S, "Hamor formally asked for Dinah.")],
  'entries': [],
  'lost': [AGREE]},

 '34:9': {
  'received': "Intermarry with us: give us your daughters and take ours.",
  'explain': ("A general alliance by marriage, the thing Abraham and Isaac forbade. The Greek adds for your sons."),
  'shared': ["Make marriages with us.", "Give your daughters to us.", "Take our daughters for yourselves."],
  'instructions': [ins(K, S, "Hamor proposed intermarriage between the peoples."), ins(W, R, "Hamor offers what the patriarchs refused for three generations; the family would dissolve into Canaan by marriage, and the brothers’ crime will prevent what their faith should have.")],
  'entries': ['canaan'],
  'lost': [keeps("An added tois huiois hymōn, “for your sons,” in the Greek."), between("Hebrew, Latin and King James “take our daughters unto you.”")]},

 '34:10': {
  'received': "Live with us; the land is open to you; dwell, trade and acquire property in it.",
  'explain': ("Settlement rights. The Greek says the land is broad; the Hebrew the land shall be before you; the Latin at your disposal, cultivate it."),
  'shared': ["You shall dwell with us.", "The land shall be before you.", "Dwell and trade in it and acquire possessions."],
  'instructions': [ins(K, S, "Hamor offered Jacob’s family full settlement.")],
  'entries': [],
  'lost': [keeps("An added plateia, “broad,” in the Greek: “the land is broad before you,” anticipating 34:21."), between("Latin “The land is at your disposal; cultivate it” and King James “the land shall be before you” follow the Hebrew.")]},

 '34:11': {
  'received': "Shechem asked for favour and offered whatever they asked.",
  'explain': ("The suitor speaks for himself. The Hebrew says I will give; the Greek we will give; the Latin I will give."),
  'shared': ["Shechem spoke to her father and brothers.", "Let me find favour in your sight.", "Whatever you ask I will give."],
  'instructions': [ins(K, S, "Shechem offered any price for Dinah.")],
  'entries': [],
  'lost': [between("Hebrew etten, “I will give,” is Greek dōsomen, “we will give”; Latin and King James “I will give.”")]},

 '34:12': {
  'received': "Ask any bride-price and gift and I will pay; only give me the girl as wife.",
  'explain': ("Mohar and mattan, bride-price and gift; the Greek has one payment term; the Latin gladly."),
  'shared': ["Ask of me a very great bride-price and gift.", "I will give whatever you say.", "Only give me the young woman as a wife."],
  'instructions': [ins(K, S, "Shechem offered an unlimited bride-price."), ins(W, R, "Shechem will pay anything, as if the wrong were a price; the brothers will name a price that is not money.")],
  'entries': [],
  'lost': [between("Hebrew mohar u-mattan, “bride-price and gift,” is Greek tēn phernēn, “the marriage payment,” one term; Latin “marriage payment and ask for gifts”; King James “dowry and gift.”")]},

 '34:13': {
  'received': "Jacob’s sons answered Shechem and Hamor deceitfully, because he had defiled their sister Dinah.",
  'explain': ("Deceitfully, be-mirmah, the word of 27:35: Jacob’s sons inherit his method. The Hebrew says he had defiled; the Greek they had defiled, widening the blame to the city; the Latin enraged at their sister’s violation."),
  'shared': ["Jacob’s sons answered Shechem and Hamor his father.", "They answered deceitfully.", "It was because their sister Dinah had been defiled."],
  'instructions': [ins(K, S, "The brothers plotted a deceitful answer."), ins(W, R, "With deceit, as Isaac said of Jacob; the sons speak their father’s language, and the narrator names it before they open their mouths.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew asher timme, “because he had defiled,” singular, becomes Greek hoti emianan, “because they had defiled,” plural; the guilt spreads from Shechem to his people."), between("Latin “enraged at their sister’s violation” and King James “because he had defiled Dinah their sister” keep the singular.")]},

 '34:14': {
  'received': "They said they could not give their sister to an uncircumcised man; it would be a disgrace.",
  'explain': ("The covenant sign used as a bargaining chip. The Hebrew says they said; the Greek names Simeon and Levi, Dinah’s brothers and Leah’s sons, narrowing the speakers; the Latin unlawful and shameful."),
  'shared': ["We cannot do this thing.", "We cannot give our sister to one who is uncircumcised.", "That would be a disgrace to us."],
  'instructions': [ins(K, S, "The brothers made circumcision the condition."), ins(W, R, "Circumcision, the sign of Abraham’s covenant, is offered as a trick; the holiest thing the family has is spent on a ruse, and God is not mentioned in the chapter.")],
  'entries': [],
  'lost': [keeps("An added Symeōn kai Leui hoi adelphoi Dinas huioi de Leias, “Simeon and Levi, the brothers of Dinah and sons of Leah,” as speakers in the Greek, where the Hebrew has va-yomru, “and they said.”"), between("Latin and King James “they said.”")]},

 '34:15': {
  'received': "Only on this condition: become like us by circumcising every male.",
  'explain': ("The Greek adds and live among you; the Latin frames it as a covenant."),
  'shared': ["Only on this condition will we consent.", "Become like us.", "Circumcise every male among you."],
  'instructions': [ins(K, S, "Every male of Shechem was to be circumcised.")],
  'entries': [],
  'lost': [keeps("An added kai katoikēsomen en hymin, “and we will dwell among you,” in the Greek."), between("Latin “we can enter a covenant on this condition” and King James “in this will we consent” follow the Hebrew.")]},

 '34:16': {
  'received': "Then we will exchange daughters, live with you, and become one people.",
  'explain': ("The false promise of union. The Hebrew says one people; the Greek one family, wives; the Latin one people."),
  'shared': ["We will give our daughters and take yours.", "We will live with you.", "We will become one people."],
  'instructions': [ins(K, S, "The brothers feigned a promise of union.")],
  'entries': [],
  'lost': [between("Hebrew le-am echad, “one people,” is Greek hōs genos hen, “as one family”; Greek adds gynaikas, “wives”; Latin and King James “one people.”")]},

 '34:17': {
  'received': "If you will not be circumcised, we will take our daughter and go.",
  'explain': ("The threat. The Hebrew says our daughter, Dinah, still in Shechem’s house; the Greek our daughters."),
  'shared': ["If you will not listen and be circumcised.", "We will take our daughter.", "We will leave."],
  'instructions': [ins(K, S, "The brothers threatened to withdraw with Dinah.")],
  'entries': [],
  'lost': [loses("Hebrew bittenu, “our daughter,” singular, becomes Greek tas thygateras hēmōn, “our daughters.”"), between("Latin and King James “our daughter.”")]},

 '34:18': {
  'received': "Their words pleased Hamor and Shechem.",
  'explain': ("The trap is accepted. The versions agree."),
  'shared': ["Their words pleased Hamor.", "They pleased Shechem, Hamor’s son.", "The terms were accepted."],
  'instructions': [ins(K, S, "Hamor and Shechem accepted the terms.")],
  'entries': [],
  'lost': [AGREE]},

 '34:19': {
  'received': "The young man did not delay, for he delighted in Jacob’s daughter and was the most honoured of his father’s house.",
  'explain': ("Shechem’s eagerness and standing: the whole city will follow him. The versions agree; the Latin immediately, loved greatly."),
  'shared': ["The young man did not delay.", "He delighted in Jacob’s daughter.", "He was the most honoured in his father’s house."],
  'instructions': [ins(K, S, "Shechem hastened to comply."), ins(W, R, "The prince’s desire and honour carry his city into the trap; a whole town is circumcised for one man’s wanting, and dies for it.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '34:20': {
  'received': "Hamor and Shechem went to the city gate and spoke to the men of the city.",
  'explain': ("The gate, the place of public decision. The versions agree; the Latin the people."),
  'shared': ["Hamor and Shechem his son came to the gate of their city.", "They spoke to the men of the city.", "They proposed the terms."],
  'instructions': [ins(K, S, "The terms were put to the city at the gate.")],
  'entries': [],
  'lost': [AGREE]},

 '34:21': {
  'received': "These men are peaceful; let them dwell and trade here, for the land is broad; let us exchange daughters.",
  'explain': ("Peaceful, shelemim, the word for Jacob’s safe arrival in 33:18, now cruelly ironic. The Latin adds needs cultivators. The versions agree."),
  'shared': ["These men are peaceful with us; let them dwell and trade in the land.", "The land is broad enough for them.", "Let us take their daughters as wives and give them ours."],
  'instructions': [ins(K, S, "Hamor persuaded the city of the alliance."), ins(W, R, "“These men are peaceful”: Hamor describes the men who will kill him. The city is persuaded by its own hospitality.")],
  'entries': [],
  'lost': [between("Latin “it is spacious and wide and needs cultivators” expands; Hebrew, Greek and King James “the land is broad enough for them.”")]},

 '34:22': {
  'received': "Only on this condition will they dwell with us as one people: every male circumcised, as they are.",
  'explain': ("The condition restated to the city. The Hebrew says consent to dwell; the Greek become like us; the Latin the one thing delaying so great a benefit."),
  'shared': ["Only on this condition will the men consent to dwell with us as one people.", "Every male among us must be circumcised.", "As they are circumcised."],
  'instructions': [ins(K, S, "Circumcision was put to the city as the price of alliance.")],
  'entries': [],
  'lost': [between("Hebrew ye’otu lanu, “they will consent to us,” is Greek homoiōthēsontai hēmin, “they will become like us”; Latin “only one condition delaying so great a benefit”; King James “will the men consent unto us.”")]},

 '34:23': {
  'received': "Will not their livestock and property be ours? Only consent, and they will dwell with us.",
  'explain': ("Hamor’s appeal to greed; the city too has a motive. The Hebrew says consent; the Greek become like them; the Latin become one people."),
  'shared': ["Shall not their cattle, possessions and animals be ours?", "Only let us consent to them.", "They will dwell with us."],
  'instructions': [ins(K, S, "Hamor appealed to the city’s self-interest."), ins(W, R, "Each side plans to profit from the other: Shechem for Jacob’s cattle, Jacob’s sons for Shechem’s blood. The alliance is false from both gates.")],
  'entries': [],
  'lost': [between("Hebrew ne’otah lahem, “let us consent to them,” is Greek homoiōthōmen autois, “let us become like them”; Latin “by living together we shall become one people”; King James “let us consent unto them.”")]},

 '34:24': {
  'received': "All who went out of the city gate agreed, and every male was circumcised.",
  'explain': ("The Hebrew repeats all who went out of the gate of his city twice; the Greek once, adding in the flesh of his foreskin; the Latin everyone agreed."),
  'shared': ["All who went out of the gate of the city listened to Hamor and Shechem.", "Every male was circumcised.", "The whole city complied."],
  'instructions': [ins(K, S, "The men of Shechem were all circumcised.")],
  'entries': [],
  'lost': [keeps("An added tēn sarka tēs akrobystias autōn, “the flesh of their foreskin,” in the Greek, which drops the Hebrew’s repeated kol-yotze’e sha‘ar iro, “all who went out of the gate of his city.”"), between("Latin “Everyone agreed, and all the males were circumcised” compresses; King James repeats the gate with the Hebrew.")]},

 '34:25': {
  'received': "On the third day, when they were in pain, Simeon and Levi, Dinah’s brothers, took swords, entered the city unopposed, and killed every male.",
  'explain': ("The massacre, by two brothers, Leah’s sons like Dinah. Betach, in security, describes either the attackers’ boldness or the city’s unguardedness. The Latin adds that the pain is worst on the third day."),
  'shared': ["On the third day, while they were in pain.", "Simeon and Levi, Dinah’s brothers, each took his sword and came on the city.", "They killed every male."],
  'instructions': [ins(K, S, "Simeon and Levi slaughtered the men of Shechem."), ins(W, R, "The covenant sign becomes the wound through which a city is killed; Jacob’s curse in 49:5–7 will remember this, and Levi’s tribe will be given to God instead of land.")],
  'entries': [],
  'lost': [between("Hebrew betach, “securely,” is Greek asphalōs, “safely,” rendered “unopposed”; Latin “when the pain of the wounds is most severe … boldly”; King James “boldly.”")]},

 '34:26': {
  'received': "They killed Hamor and Shechem with the sword, took Dinah from Shechem’s house, and left.",
  'explain': ("Dinah was in Shechem’s house all along. The Latin omits the edge of the sword and went away; the others agree."),
  'shared': ["They killed Hamor and Shechem his son with the sword.", "They took Dinah out of Shechem’s house.", "They went away."],
  'instructions': [ins(K, S, "The brothers killed the princes and recovered Dinah."), ins(W, R, "Dinah is taken out of Shechem’s house, where she had been throughout the negotiations; the chapter never gives her a word.")],
  'entries': [],
  'lost': [between("Latin “also killed Hamor and Shechem, taking their sister Dinah” drops le-fi-cherev, “by the mouth of the sword,” and va-yetze’u, “and went out”; Hebrew, Greek and King James have both.")]},

 '34:27': {
  'received': "Jacob’s sons came upon the slain and plundered the city where their sister had been defiled.",
  'explain': ("The other brothers join for the spoil. The Hebrew says the slain; the Greek the wounded, which may include the dying; the Latin Jacob’s other sons, in revenge."),
  'shared': ["Jacob’s sons came upon the slain.", "They plundered the city.", "It was where their sister had been defiled."],
  'instructions': [ins(K, S, "The other brothers plundered the city."), ins(W, R, "Two killed and the rest looted; the family that could not keep one daughter safe strips a city, and calls it her honour.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew al-ha-chalalim, “upon the slain,” becomes Greek epi tous traumatias, “upon the wounded”; Greek adds Dinas, “Dinah.”"), between("Latin “Jacob’s other sons fell upon the slain … in revenge” and King James “came upon the slain” keep the slain.")]},

 '34:28': {
  'received': "They took their sheep, oxen, donkeys and all in the city and field.",
  'explain': ("The inventory of plunder. The versions agree; the Latin devastated."),
  'shared': ["They took their sheep, oxen and donkeys.", "They took what was in the city.", "They took what was in the field."],
  'instructions': [ins(K, S, "The brothers seized Shechem’s livestock and goods.")],
  'entries': [],
  'lost': [AGREE]},

 '34:29': {
  'received': "They carried off all their wealth, children and wives, and plundered the houses.",
  'explain': ("Captives as well as goods. The Hebrew says wealth, children, wives, in the houses; the Greek people, household goods, wives, in the city and houses; the Latin little ones and wives."),
  'shared': ["They took all their wealth and children and wives captive.", "They plundered.", "Everything in the houses."],
  'instructions': [ins(K, S, "Women and children of Shechem were taken captive."), ins(W, R, "The brothers take wives from the city they would not give a sister to; Hamor’s proposal is fulfilled by force, in one direction.")],
  'entries': [],
  'lost': [keeps("Greek ta sōmata autōn kai pasan tēn aposkeuēn autōn, “their persons and all their household goods,” for Hebrew chelam ve-et-kol-tappam, “their wealth and all their children,” and an added en tē polei, “in the city.”"), between("Latin “led their little ones and wives away captive” compresses; King James follows the Hebrew.")]},

 '34:30': {
  'received': "Jacob told Simeon and Levi they had made him odious to the Canaanites and Perizzites, and few as he was, he would be destroyed.",
  'explain': ("Jacob’s rebuke is for the danger, not the deed; the moral judgment waits for 49:5–7. Made me stink, the Hebrew says. The versions agree; the Latin adds when they had boldly done these things."),
  'shared': ["You have brought trouble on me by making me odious to the people of the land, the Canaanites and Perizzites.", "I am few in number.", "They will gather against me and strike me, and I and my house will be destroyed."],
  'instructions': [ins(K, S, "Jacob rebuked Simeon and Levi for endangering the family."), ins(W, R, "Jacob’s first words in the chapter are about himself: “you have troubled me.” Dinah is not mentioned; the father’s fear is for the house, and his silence before the sons is now a reproach.")],
  'entries': ['jacob', 'canaan'],
  'lost': [between("Hebrew le-hav’isheni, “to make me stink,” is Greek misēton me pepoiēkate, “you have made me hated”; Latin adds “When they had boldly done these things”; King James “to make me to stink.”")]},

 '34:31': {
  'received': "They said, Should he treat our sister like a prostitute?",
  'explain': ("The brothers’ last word, a question that answers Jacob’s fear with Dinah’s honour. The Hebrew says should he; the Greek and Latin should they, the city."),
  'shared': ["They answered.", "Should our sister be treated like a prostitute?", "The chapter ends on the question."],
  'instructions': [ins(K, S, "The brothers justified the massacre by Dinah’s honour."), ins(W, R, "The chapter ends in a question no one answers; the brothers have the last word and Jacob has none, and Genesis leaves the reader to judge.")],
  'entries': [],
  'lost': [loses("Hebrew ha-khe-zonah ya‘aseh, “shall he treat as a harlot,” singular, becomes Greek all’ hōsei pornē chrēsōntai, “but shall they use as a harlot,” plural."), between("Latin “Should they have used our sister” follows the Greek; King James “Should he deal with our sister” the Hebrew.")]},
 }
}
