# Study prose for Genesis 29 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 29,
 'chapterNote': (
  "Jacob at the well, Rachel, Laban, fourteen years for two wives, and the first four sons. The columns agree on the story; the Hebrew keeps “a well in the "
  "field,” “all the flocks are gathered,” Rachel “a shepherdess,” “the news about Jacob,” “surely you are my bone and my flesh,” Laban’s question “should you "
  "serve me for nothing?”, “we will give you,” and “a feast.” The Greek keeps a long added genealogy at the head of the chapter (“to Laban the son of Bethuel "
  "the Syrian, the brother of Rebekah, the mother of Jacob and Esau”), “the plain,” “all the shepherds are gathered,” “the name of Jacob,” “of my bones and of "
  "my flesh,” Laban’s statement “you shall not serve me for nothing,” “I will give you,” “a wedding feast,” Jacob named twice in 29:23 and in Leah’s first two "
  "births, and Rachel named in 29:31. Four Hebrew-column renderings were corrected today to the Masoretic wording. The Latin and King James follow the Hebrew; "
  "the Latin rearranges 29:23–25 and 29:28–30 into connected narrative."),
 'verses': {

 '29:1': {
  'received': "Jacob went on to the land of the people of the East.",
  'explain': ("The Hebrew says lifted his feet, a lively idiom for setting off, and gives only the destination, the land of the sons of the east. The Greek adds the whole "
   "family tag from 28:5: to Laban the son of Bethuel the Syrian, the brother of Rebekah, the mother of Jacob and Esau. The Latin and King James follow the Hebrew."),
  'shared': ["Jacob went on his way.", "He came to the land of the East.", "He was bound for Laban."],
  'instructions': [ins(K, S, "Jacob travelled east toward Laban’s country."), ins(W, R, "Bethel is behind him and the vision with it; the road east is ordinary again, and the rest of the chapter has no angels in it.")],
  'entries': ['jacob'],
  'lost': [keeps("An added pros Laban ton huion Bathouēl tou Syrou, adelphon de Rhebekkas mētros Iakōb kai Ēsau, “to Laban the son of Bethuel the Syrian, the brother of Rebekah, the mother of Jacob and Esau,” in the Greek, repeated from 28:5; Hebrew va-yissa Ya‘aqov raglav, “Jacob lifted his feet,” is the idiom of setting out."), between("Latin “journeyed on and came to the eastern land” and King James “went on his journey, and came into the land of the people of the east” follow the Hebrew.")]},

 '29:2': {
  'received': "He saw a well in the field with three flocks lying by it and a great stone over its mouth.",
  'explain': ("A well, as for Abraham’s servant; a stone over it, too heavy for one man, as the next verses explain. The Hebrew says in the field; the Greek in the plain. The Hebrew-column rendering was corrected today."),
  'shared': ["He saw a well in the field.", "Three flocks of sheep were lying by it, for the flocks were watered from it.", "A great stone was over the mouth of the well."],
  'instructions': [ins(K, S, "Jacob came to a covered well with flocks waiting.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew be’er ba-sadeh, “a well in the field,” is Greek phrear en tō pediō, “a well in the plain”; Latin and King James “field.”")]},

 '29:3': {
  'received': "When all the flocks gathered, the stone was rolled off, the sheep watered, and the stone replaced.",
  'explain': ("The custom of the well: wait for all, roll together, water, close. The versions agree."),
  'shared': ["All the flocks would gather there.", "They would roll the stone from the well’s mouth and water the sheep.", "Then they put the stone back in its place."],
  'instructions': [ins(K, S, "The well was opened only when all the flocks had come."), ins(W, R, "The stone is a rule as much as a weight: no one waters before the others. Jacob is about to break it for love.")],
  'entries': [],
  'lost': [AGREE]},

 '29:4': {
  'received': "Jacob asked the shepherds where they were from; they said Haran.",
  'explain': ("My brothers, he calls them, the courtesy of strangers. Haran: he has arrived. The versions agree."),
  'shared': ["Jacob said, My brothers, where are you from?", "They answered.", "We are from Haran."],
  'instructions': [ins(K, S, "Jacob learned he had reached Haran.")],
  'entries': ['jacob', 'haran'],
  'lost': [AGREE]},

 '29:5': {
  'received': "He asked if they knew Laban son of Nahor; they did.",
  'explain': ("Laban is Bethuel’s son and Nahor’s grandson; son of Nahor names the better-known ancestor. The versions agree."),
  'shared': ["Do you know Laban the son of Nahor?", "They answered.", "We know him."],
  'instructions': [ins(K, S, "The shepherds knew Laban.")],
  'entries': [],
  'lost': [AGREE]},

 '29:6': {
  'received': "He asked if Laban was well; they said he was, and here came his daughter Rachel with the sheep.",
  'explain': ("Shalom lo, is it peace with him. Rachel appears on cue, as Rebekah did. The Hebrew and Latin make her approach part of the shepherds’ speech; the Greek makes it narration."),
  'shared': ["Is he well?", "He is well.", "Behold, Rachel his daughter is coming with the sheep."],
  'instructions': [ins(K, S, "Rachel approached as Jacob asked after Laban."), ins(W, R, "The bride arrives at a well again; providence repeats its pattern, and this time the man is there himself.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew and Latin keep “and behold, Rachel his daughter is coming” within the shepherds’ speech; the Greek closes the speech at “he is well” and narrates her coming; King James follows the Hebrew.")]},

 '29:7': {
  'received': "Jacob said it was still full day, too early to gather the flocks; water them and go on grazing.",
  'explain': ("Jacob, a herdsman himself, tells strangers their business. The Latin adds not time to bring the flocks to the folds, first give water; the others are shorter."),
  'shared': ["There is still much of the day left.", "It is not time to gather the livestock.", "Water the sheep and take them to pasture."],
  'instructions': [ins(K, S, "Jacob urged the shepherds to water and move on."), ins(W, R, "He wants the shepherds gone, perhaps, before Rachel arrives; the chapter never says so, but Jacob is a man who arranges things.")],
  'entries': ['jacob'],
  'lost': [between("Latin “it is not time to bring the flocks back to the folds. First give the sheep water, and then lead them back to pasture” expands; Hebrew, Greek and King James are briefer.")]},

 '29:8': {
  'received': "They said they could not until all the flocks were gathered and the stone rolled away.",
  'explain': ("The custom restated as a refusal. The Hebrew says until all the flocks are gathered; the Greek all the shepherds; the Latin all the animals, and we remove."),
  'shared': ["We cannot.", "Not until all are gathered and the stone is rolled from the well’s mouth.", "Then we water the sheep."],
  'instructions': [ins(K, S, "The shepherds kept to the custom of the well.")],
  'entries': [],
  'lost': [between("Hebrew ad asher ye’asefu kol-ha-adarim, “until all the flocks are gathered,” is Greek heōs tou synachthēnai pantas tous poimenas, “until all the shepherds are gathered”; Latin “all the animals,” King James “all the flocks.”")]},

 '29:9': {
  'received': "While he spoke, Rachel came with her father’s sheep, for she was a shepherdess.",
  'explain': ("Rachel, whose name means ewe, keeps her father’s flock. The Greek names Laban and repeats her father’s sheep; the Hebrew says she was a shepherdess; the Latin she herself tended the flock."),
  'shared': ["While he was still speaking with them.", "Rachel came with her father’s sheep.", "She tended them."],
  'instructions': [ins(K, S, "Rachel arrived tending Laban’s flock."), ins(W, R, "Rachel comes as a working shepherdess, not a girl drawing water; Jacob’s wife will be his partner in the trade that makes him rich.")],
  'entries': [],
  'lost': [keeps("An added hē thygatēr Laban, “Laban’s daughter,” and ta probata tou patros autēs, “her father’s sheep,” repeated, in the Greek; Hebrew ki ro‘ah hi, “for she was a shepherdess.”"), between("Latin “for she herself tended the flock” and King James “for she kept them” follow the Hebrew.")]},

 '29:10': {
  'received': "Seeing Rachel and Laban’s sheep, Jacob rolled the stone from the well himself and watered the flock.",
  'explain': ("Laban his mother’s brother three times in the Hebrew and Greek, the emphasis of kinship; and a feat of strength, the stone moved alone. The Latin says knew she was his cousin, his uncle Laban, and places the watering in the next verse."),
  'shared': ["Jacob saw Rachel, daughter of Laban his mother’s brother, and Laban’s sheep.", "He went up and rolled the stone from the well’s mouth.", "He watered the sheep of Laban his mother’s brother."],
  'instructions': [ins(K, S, "Jacob single-handedly opened the well for Rachel’s flock."), ins(W, R, "Love moves the stone the shepherds would not; the man who lay on a stone at Bethel rolls one away at Haran.")],
  'entries': ['jacob'],
  'lost': [between("Latin “when Jacob saw her and knew she was his cousin, and saw the sheep of his uncle Laban, he removed the stone” compresses the threefold “Laban his mother’s brother” and moves the watering to 29:11; Hebrew, Greek and King James agree.")]},

 '29:11': {
  'received': "Jacob kissed Rachel and wept aloud.",
  'explain': ("A kinsman’s kiss, before he has told her who he is, and tears: relief, recognition, the end of the road. The versions agree; the Latin after watering the flock."),
  'shared': ["Jacob kissed Rachel.", "He lifted his voice.", "He wept."],
  'instructions': [ins(K, S, "Jacob kissed Rachel and wept.")],
  'entries': ['jacob'],
  'lost': [between("Latin “after watering the flock, he kissed her” carries the watering here; Hebrew, Greek and King James have it in 29:10.")]},

 '29:12': {
  'received': "He told Rachel he was her father’s kinsman and Rebekah’s son; she ran to tell her father.",
  'explain': ("Brother in the Hebrew and Greek is kinsman; Jacob is Laban’s nephew. Rachel runs as Rebekah ran. The versions agree."),
  'shared': ["Jacob told Rachel he was her father’s kinsman.", "He was Rebekah’s son.", "She ran and told her father."],
  'instructions': [ins(K, S, "Jacob identified himself to Rachel.")],
  'entries': ['jacob', 'rebekah'],
  'lost': [between("Hebrew achi aviha, “her father’s brother,” and Greek adelphos tou patros autēs are kinship terms for nephew; Latin “kinsman,” King James “brother.”")]},

 '29:13': {
  'received': "Laban ran to meet Jacob, embraced and kissed him, brought him home, and heard his story.",
  'explain': ("Laban’s welcome, warm and, as the reader of chapter 24 remembers, alert to what a visitor may bring. The Hebrew says heard the news; the Greek heard the name; the Latin adds kissed him eagerly and hearing the reasons for his journey."),
  'shared': ["Laban heard of Jacob his sister’s son.", "He ran to meet him, embraced and kissed him, and brought him into his house.", "Jacob told Laban all these things."],
  'instructions': [ins(K, S, "Laban welcomed Jacob into his house."), ins(W, R, "Laban runs, embraces, kisses: the same Laban who ran to the man with gold at the well. Jacob arrives with nothing, and the welcome will be priced accordingly.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew shema Ya‘aqov, “the report of Jacob,” is Greek to onoma Iakōb, “the name of Jacob”; Latin “kissed him eagerly … after hearing the reasons for his journey” expands; King James “the tidings of Jacob.”")]},

 '29:14': {
  'received': "Laban said, Surely you are my bone and my flesh, and Jacob stayed a month.",
  'explain': ("The kinship formula of 2:23. The Hebrew says surely you are my bone and my flesh; the Greek you are of my bones and of my flesh; the Latin my bone and my flesh. The Hebrew-column rendering was corrected today."),
  'shared': ["Laban spoke to him.", "You are my bone and my flesh.", "He stayed with him a full month."],
  'instructions': [ins(K, S, "Laban acknowledged Jacob as kin and housed him a month.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew akh atzmi u-vesari attah, “surely my bone and my flesh are you,” is Greek ek tōn ostōn mou kai ek tēs sarkos mou ei sy, “you are of my bones and of my flesh,” without the particle; Latin and King James follow the Hebrew.")]},

 '29:15': {
  'received': "Laban said that as kin Jacob should not serve for nothing, and asked his wages.",
  'explain': ("A month of unpaid work, then the question that opens the bargaining. The Hebrew makes it a question, should you serve me for nothing?; the Greek a statement, you shall not; the Latin a question."),
  'shared': ["Because you are my kinsman.", "Should you serve me for nothing?", "Tell me what your wages should be."],
  'instructions': [ins(K, S, "Laban asked Jacob to name his wages."), ins(W, R, "The offer sounds generous and is a trap: once wages are named, Jacob is a hired man, not a guest.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ha-khi achi attah va-avadtani chinnam, “because you are my kinsman, shall you serve me for nothing?” a question, is Greek ou douleuseis moi dōrean, “you shall not serve me for nothing,” a statement; Latin and King James keep the question.")]},

 '29:16': {
  'received': "Laban had two daughters, Leah the elder and Rachel the younger.",
  'explain': ("The sisters introduced for the bargain. The versions agree."),
  'shared': ["Laban had two daughters.", "The older was Leah.", "The younger was Rachel."],
  'instructions': [ins(K, S, "Laban had two daughters, Leah and Rachel.")],
  'entries': [],
  'lost': [AGREE]},

 '29:17': {
  'received': "Leah’s eyes were weak, but Rachel was beautiful in form and face.",
  'explain': ("The Hebrew rakkot, tender, soft, may be a compliment or a defect; the Greek weak settles it; the Latin weak, beautiful in face and lovely in appearance; the King James tender eyed, well favoured. The contrast, whatever Leah’s eyes, is with Rachel’s beauty."),
  'shared': ["Leah’s eyes were tender.", "Rachel was beautiful in form.", "She was beautiful in appearance."],
  'instructions': [ins(K, S, "Leah and Rachel are contrasted in looks."), ins(W, R, "Leah is described by one feature and Rachel by her whole form; the narrator sees them as Jacob did, and the mother of Judah is introduced by what she lacked.")],
  'entries': [],
  'lost': [between("Hebrew rakkot, “tender,” is Greek astheneis, “weak”; Latin “weak,” King James “tender eyed”; Hebrew yefat-to’ar vi-yfat mar’eh, “beautiful of form and beautiful of appearance,” Greek kalē tō eidei kai hōraia tē opsei.")]},

 '29:18': {
  'received': "Jacob loved Rachel and offered seven years’ service for her.",
  'explain': ("The bride-price of a man without goods is labour; seven years is generous. He names Rachel, your younger daughter, precisely. The versions agree."),
  'shared': ["Jacob loved Rachel.", "I will serve you seven years.", "For Rachel your younger daughter."],
  'instructions': [ins(K, S, "Jacob offered seven years’ work for Rachel."), ins(W, R, "“Your younger daughter”: Jacob is exact, as a man who has himself traded on an elder’s rights would be. The exactness will not save him.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '29:19': {
  'received': "Laban said it was better to give her to Jacob than to another; stay with me.",
  'explain': ("Agreement without a promise: better that I give her to you is not I will. The versions agree."),
  'shared': ["It is better that I give her to you.", "Than to another man.", "Stay with me."],
  'instructions': [ins(K, S, "Laban accepted the terms in principle."), ins(W, R, "Laban never says yes; he says better. Jacob, who tricked a blind man with a borrowed voice, does not hear the gap.")],
  'entries': [],
  'lost': [AGREE]},

 '29:20': {
  'received': "Jacob served seven years for Rachel, and they seemed a few days for his love of her.",
  'explain': ("One of the tenderest sentences in Genesis. The versions agree; the Latin the greatness of his love."),
  'shared': ["Jacob served seven years for Rachel.", "They seemed to him a few days.", "It was because he loved her."],
  'instructions': [ins(K, S, "Seven years passed quickly for love of Rachel."), ins(W, R, "Rebekah promised a few days in Haran; the few days become seven years that feel like a few days. Love alters the clock that exile stopped.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '29:21': {
  'received': "Jacob asked Laban for his wife, his days being fulfilled.",
  'explain': ("Blunt: give me my wife, that I may go in to her. The versions agree; the Latin the time is fulfilled."),
  'shared': ["Give me my wife.", "My days are fulfilled.", "That I may go in to her."],
  'instructions': [ins(K, S, "Jacob claimed Rachel at the end of seven years.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '29:22': {
  'received': "Laban gathered the men of the place and made a feast.",
  'explain': ("A public wedding, with witnesses who will make the substitution hard to undo. The Hebrew says a feast; the Greek a wedding feast; the Latin a great gathering of friends."),
  'shared': ["Laban gathered all the men of the place.", "He made a feast.", "It was the wedding."],
  'instructions': [ins(K, S, "Laban held a wedding feast.")],
  'entries': [],
  'lost': [keeps("Greek gamon, “wedding,” for Hebrew mishteh, “feast,” names the occasion."), between("Latin “a great gathering of friends to a feast and celebrated the wedding”; King James “a feast.”")]},

 '29:23': {
  'received': "In the evening he brought Leah to Jacob, and he went in to her.",
  'explain': ("The switch, under cover of darkness and a veil. The Hebrew says and he went in to her; the Greek repeats Jacob’s name; the Latin breaks the verse and moves the going in to verse 24. The Hebrew-column rendering was corrected today."),
  'shared': ["It was evening.", "He took Leah his daughter and brought her to Jacob.", "He went in to her."],
  'instructions': [ins(K, S, "Laban substituted Leah for Rachel."), ins(W, R, "The deceiver is deceived in the dark by a substituted elder for a younger; Isaac could not see, and now Jacob cannot.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew va-yavo eleha, “and he went in to her,” is Greek kai eisēlthen pros autēn Iakōb, with Jacob’s name repeated; Latin moves the clause to 29:24; King James follows the Hebrew.")]},

 '29:24': {
  'received': "Laban gave Leah his maid Zilpah.",
  'explain': ("Zilpah, who will bear Gad and Asher. The Latin here includes Jacob going in to her according to custom and seeing Leah in the morning, which the others place in verses 23 and 25."),
  'shared': ["Laban gave his maid Zilpah.", "He gave her to his daughter Leah.", "She was to be her maid."],
  'instructions': [ins(K, S, "Zilpah became Leah’s maid.")],
  'entries': [],
  'lost': [between("Latin “Jacob went in to her according to custom, but when morning came, he saw Leah” gathers the clauses of 29:23 and 29:25 here; Hebrew, Greek and King James keep this verse to Zilpah.")]},

 '29:25': {
  'received': "In the morning it was Leah; Jacob asked Laban why he had deceived him after he served for Rachel.",
  'explain': ("Behold, it was Leah: the Hebrew’s shock in three words. Jacob’s what have you done to me is Abimelech’s to Isaac; deceived, rimmitani, is the word Isaac used of Jacob in 27:35. The Latin omits the morning discovery, having placed it in verse 24."),
  'shared': ["In the morning, behold, it was Leah.", "What is this you have done to me? Did I not serve you for Rachel?", "Why have you deceived me?"],
  'instructions': [ins(K, S, "Jacob discovered the substitution and protested."), ins(W, R, "“Why have you deceived me?” is asked by the man who answered “I am Esau”; the word is the same, and the narrator lets him hear it.")],
  'entries': ['jacob'],
  'lost': [between("Latin “he said to his father-in-law” omits va-yhi va-boqer ve-hinneh hi Le’ah, “in the morning, behold, it was Leah,” placed in 29:24; Hebrew rimmitani, “you have deceived me,” Greek parelogisō me, “you have defrauded me.”")]},

 '29:26': {
  'received': "Laban said it was not the custom to give the younger before the firstborn.",
  'explain': ("Laban’s defence, which is also a rebuke Jacob can hear: the younger before the firstborn, bekhirah. The Hebrew and King James say firstborn; the Greek and Latin older."),
  'shared': ["It is not done so in our place.", "To give the younger.", "Before the firstborn."],
  'instructions': [ins(K, S, "Laban cited custom for giving the elder first."), ins(W, R, "“Not the younger before the firstborn”: in Haran the rule Jacob broke at home is enforced against him. He does not argue.")],
  'entries': [],
  'lost': [between("Hebrew lifne ha-bekhirah, “before the firstborn,” is Greek prin ē tēn presbyteran, “before the older”; Latin “the younger in marriage first”; King James “before the firstborn.”")]},

 '29:27': {
  'received': "Finish this one’s week, and we will give you the other for seven more years’ service.",
  'explain': ("The week is the seven-day wedding feast, not seven years; Rachel follows at its end, with the price to be paid afterward. The Hebrew says we will give; the Greek and Latin I will give."),
  'shared': ["Complete this one’s week.", "Then the other will be given to you also.", "In exchange for another seven years of service."],
  'instructions': [ins(K, S, "Laban offered Rachel for seven more years."), ins(W, R, "Laban doubles his price and calls it custom; Jacob, who priced a birthright at a bowl of stew, pays fourteen years for a wife.")],
  'entries': [],
  'lost': [between("Hebrew ve-nittenah, “and we will give,” is Greek kai dōsō soi, “and I will give you”; Latin “I will also give,” King James “we will give.”")]},

 '29:28': {
  'received': "Jacob did so, and after the week Laban gave him Rachel as wife.",
  'explain': ("Rachel is married within the week, before the second seven years begin. The versions agree; the Latin he agreed to the arrangement."),
  'shared': ["Jacob did so.", "He fulfilled her week.", "Laban gave him Rachel his daughter as wife."],
  'instructions': [ins(K, S, "Jacob married Rachel after Leah’s week.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '29:29': {
  'received': "Laban gave Rachel his maid Bilhah.",
  'explain': ("Bilhah, who will bear Dan and Naphtali. The versions agree."),
  'shared': ["Laban gave his maid Bilhah.", "He gave her to his daughter Rachel.", "She was to be her maid."],
  'instructions': [ins(K, S, "Bilhah became Rachel’s maid.")],
  'entries': [],
  'lost': [AGREE]},

 '29:30': {
  'received': "Jacob went in to Rachel too, loved her more than Leah, and served another seven years.",
  'explain': ("Two wives, unequal love, and seven years more. The versions agree; the Latin at last obtaining the marriage he desired."),
  'shared': ["Jacob went in to Rachel also.", "He loved Rachel more than Leah.", "He served with Laban another seven years."],
  'instructions': [ins(K, S, "Jacob loved Rachel more and served seven more years."), ins(W, R, "“More than Leah” is the seed of the next chapter and of the twelve tribes’ rivalries; unequal love in one tent becomes history.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '29:31': {
  'received': "The Lord saw Leah was unloved and opened her womb; Rachel was barren.",
  'explain': ("God sides with the unloved. The Hebrew says hated, senu’ah, a legal term for the less favoured wife; the Greek unloved and names Rachel; the Latin he slighted Leah, her sister."),
  'shared': ["The Lord saw that Leah was unloved.", "He opened her womb.", "Rachel was barren."],
  'instructions': [ins(K, S, "God gave children to Leah while Rachel was barren."), ins(W, R, "The Lord saw, as He saw Hagar and Sarah; the overlooked wife is the one He attends to, and the beloved waits as Sarah and Rebekah waited.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew senu’ah, “hated,” is Greek miseitai, “is unloved,” the Greek adding Rhachēl where the Hebrew has the name too; Latin “he slighted Leah … her sister remained barren”; King James “Leah was hated.”")]},

 '29:32': {
  'received': "Leah bore Reuben, saying the Lord had seen her affliction and now her husband would love her.",
  'explain': ("Reuben, see, a son, explained by the Lord has seen my affliction. The Greek adds to Jacob and says humiliation; the Hebrew affliction; the Latin humiliation."),
  'shared': ["Leah conceived and bore a son and named him Reuben.", "The Lord has seen my affliction.", "Now my husband will love me."],
  'instructions': [ins(K, S, "Leah named Reuben for God’s seeing her affliction."), ins(W, R, "Leah’s first word as a mother is God’s seeing and her second is her husband’s love; the sons are prayers for a man who does not answer.")],
  'entries': ['yhwh-yahweh'],
  'lost': [keeps("An added tō Iakōb, “to Jacob,” after bore a son in the Greek; Hebrew be-onyi, “my affliction,” Greek tēn tapeinōsin mou, “my humiliation.”"), between("Latin “humiliation” follows the Greek; King James “affliction” the Hebrew.")]},

 '29:33': {
  'received': "She bore Simeon, because the Lord heard she was unloved.",
  'explain': ("Simeon, from shama, to hear. The Greek adds a second son to Jacob; the Hebrew a son; the Latin held in contempt."),
  'shared': ["She conceived again and bore a son.", "The Lord heard that I am unloved and gave me this one also.", "She named him Simeon."],
  'instructions': [ins(K, S, "Leah named Simeon for God’s hearing.")],
  'entries': ['yhwh-yahweh'],
  'lost': [keeps("An added deuteron tō Iakōb, “a second, to Jacob,” in the Greek."), between("Latin “held in contempt” for “unloved”; King James “hated.”")]},

 '29:34': {
  'received': "She bore Levi, saying her husband would now be joined to her for three sons.",
  'explain': ("Levi, from lavah, to join. The Hebrew says joined to me, he was named; the Greek on my side; the Latin she named him. Levi’s tribe will be joined to the Lord instead."),
  'shared': ["She conceived again and bore a son.", "Now my husband will be joined to me, for I have borne him three sons.", "He was named Levi."],
  'instructions': [ins(K, S, "Leah named Levi hoping for her husband’s attachment."), ins(W, R, "Three sons and the hope is still for a husband’s nearness; Levi’s name asks for a joining that will come, in his tribe, to God.")],
  'entries': [],
  'lost': [between("Hebrew yillaveh ishi elai, “my husband will be joined to me,” is Greek pros emou estai ho anēr mou, “my husband will be on my side”; Latin “joined to me … she named him Levi”; King James “joined unto me … was his name called Levi.”")]},

 '29:35': {
  'received': "She bore Judah, saying, Now I will praise the Lord, and then stopped bearing.",
  'explain': ("Judah, from yadah, to praise or thank. The fourth son is named not for husband or rivalry but for God, and from him come David and the Messiah. The Hebrew says praise; the Greek give thanks; the Latin a fourth time, praise."),
  'shared': ["She conceived again and bore a son.", "Now I will praise the Lord.", "She named him Judah and ceased bearing."],
  'instructions': [ins(K, S, "Leah named Judah for praise of the Lord."), ins(W, R, "After three names about her husband, Leah’s fourth is about God alone; the tribe of kings is named in the moment an unloved woman stopped asking to be loved.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew odeh et-YHWH, “I will praise YHWH,” is Greek exomologēsomai kyriō, “I will give thanks to the Lord”; Latin “a fourth time … I will praise the Lord”; King James “Now will I praise the LORD.”")]},
 }
}
