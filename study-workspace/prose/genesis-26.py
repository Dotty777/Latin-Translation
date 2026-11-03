# Study prose for Genesis 26 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 26,
 'chapterNote': (
  "Isaac’s one chapter of his own retraces his father’s steps: famine, Gerar, a wife called sister, wells, a covenant with Abimelech, and Beersheba. "
  "The Hebrew keeps “all these lands” in the plural, the well names Esek, Sitnah, Rehoboth and Shibah as names, Abraham named at the stopped wells, "
  "“I will bless you … for the sake of Abraham My servant,” and the servants’ report “we have found water.” The Greek keeps “all this land” in the "
  "singular, Abraham called “your father” in the promise, a hundredfold “of barley,” “tilled lands” for the Hebrew household, the well names translated "
  "(Injustice, Enmity, Broad Space, Oath, Well of the Oath), Ahuzzath as “groomsman,” “we have not loathed you,” “I have blessed you,” Elon “the Hivite,” "
  "and, alone among the columns, the servants’ report “we did not find water” in 26:32. The Latin and King James follow the Hebrew; the Latin translates "
  "the well names too (Dispute, Hostility, Spaciousness, Abundance)."),
 'verses': {

 '26:1': {
  'received': "In a second famine Isaac went to Abimelech, king of the Philistines, at Gerar.",
  'explain': ("A famine distinct from Abraham’s in chapter 12, and the same response: Isaac goes toward Egypt by way of Gerar, where his father had dealt "
   "with an Abimelech. This Abimelech, ninety years on, is likely a successor bearing the royal name. The Latin calls the first famine barrenness."),
  'shared': ["There was a famine in the land, besides the famine in Abraham’s days.", "Isaac went to Abimelech, king of the Philistines.", "He went to Gerar."],
  'instructions': [ins(K, S, "Famine drove Isaac to Gerar as it had driven Abraham."), ins(W, R, "The son walks his father’s road to the same city and, as the chapter shows, into the same temptation.")],
  'entries': ['isaac', 'abraham'],
  'lost': [between("Latin “after the barrenness (sterilitatem) that had occurred in Abraham’s days” varies the word for the first famine; the rest agree.")]},

 '26:2': {
  'received': "The Lord appeared and told him not to go down to Egypt but to live in the land He would name.",
  'explain': ("The first theophany to Isaac. Where Abraham went to Egypt unbidden, Isaac is forbidden it. The versions agree."),
  'shared': ["The Lord appeared to Isaac.", "Do not go down to Egypt.", "Dwell in the land I shall tell you of."],
  'instructions': [ins(C, S, "Do not go down to Egypt; dwell in the land I shall tell you."), ins(W, R, "God closes to Isaac the door Abraham walked through; the promise is to be kept inside its own borders this time.")],
  'entries': ['isaac', 'egypt', 'yhwh-yahweh'],
  'lost': [AGREE]},

 '26:3': {
  'received': "Sojourn here and I will be with you and bless you; I will give you and your seed all these lands and keep My oath to Abraham.",
  'explain': ("The promise is renewed to Isaac in his own right and grounded in the oath to Abraham. The Hebrew says all these lands, plural; the Greek all this land, singular; "
   "the Latin all these regions; the King James all these countries. Establish the oath is the Greek and Hebrew; the Latin fulfilling."),
  'shared': ["Sojourn in this land; I will be with you and bless you.", "To you and your seed I will give these lands.", "I will establish the oath I swore to your father Abraham."],
  'instructions': [ins(C, S, "Sojourn in this land."), ins(K, S, "God renewed the land promise and the oath to Isaac."), ins(W, R, "“I will be with you” is said to the son before anything is asked of him; presence precedes the land as it preceded the son.")],
  'entries': ['isaac', 'abraham', 'term-covenant'],
  'lost': [between("Hebrew kol-ha-aratzot ha-el, “all these lands,” is Greek pasan tēn gēn tautēn, “all this land,” here and in 26:4; Latin “all these regions” and King James “all these countries” keep the plural.")]},

 '26:4': {
  'received': "I will multiply your seed as the stars and give them these lands, and all nations will be blessed in your seed.",
  'explain': ("The stars of 15:5 and 22:17, and the nations blessed of 12:3 and 22:18, repeated to Isaac. The Hebrew form can be reflexive, bless themselves; "
   "the Greek, Latin and King James are passive, be blessed. Paul reads the seed in Galatians 3:16."),
  'shared': ["I will multiply your seed as the stars of heaven.", "I will give your seed all these lands.", "All nations of the earth shall be blessed in your seed."],
  'instructions': [ins(K, S, "The promises of seed, land and blessing to nations were given to Isaac."), ins(W, R, "Isaac receives Abraham’s promises in Abraham’s words; nothing is added, and nothing is held back.")],
  'entries': ['isaac'],
  'lost': [between("Hebrew ve-hitbarakhu, “shall bless themselves,” a reflexive, is Greek eneulogēthēsontai, “shall be blessed,” passive; Latin and King James passive; the plural lands again becomes singular in the Greek.")]},

 '26:5': {
  'received': "because Abraham obeyed Me and kept My charge, commandments, statutes and laws.",
  'explain': ("Abraham’s obedience is the stated ground. The list of legal terms, charge, commandments, statutes, laws, is the vocabulary of Deuteronomy "
   "applied back to Abraham. The Greek adds your father and orders the terms differently; the Latin precepts, commandments, rites and laws."),
  'shared': ["Abraham obeyed My voice.", "He kept My charge and commandments.", "He kept My statutes and laws."],
  'instructions': [ins(K, S, "God cited Abraham’s obedience as the reason for blessing Isaac."), ins(W, R, "Isaac is blessed for his father’s obedience; grace runs down the generations before Isaac has earned anything.")],
  'entries': ['abraham'],
  'lost': [keeps("An added ho patēr sou, “your father,” after Abraham in the Greek; Hebrew mishmarti mitzvotai chuqqotai ve-torotai, “My charge, My commandments, My statutes and My laws,” is Greek ta prostagmata mou kai tas entolas mou kai ta dikaiōmata mou kai ta nomima mou."), between("Latin “precepts and commandments … rites and laws” and King James “charge, commandments, statutes, and laws” follow the Hebrew count.")]},

 '26:6': {
  'received': "So Isaac stayed in Gerar.",
  'explain': ("Obedience: he stays where he was told. The versions agree."),
  'shared': ["Isaac stayed.", "He stayed in Gerar.", "He did not go to Egypt."],
  'instructions': [ins(K, S, "Isaac remained in Gerar as commanded.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '26:7': {
  'received': "Asked about his wife, he called Rebekah his sister, afraid of being killed for her beauty.",
  'explain': ("Abraham’s lie, now Isaac’s, and without even the half-truth of kinship; Rebekah is his cousin’s daughter, not his sister. The Greek names "
   "Rebekah at the start; the Hebrew his wife; the Latin he feared to acknowledge she was married to him."),
  'shared': ["The men of the place asked about his wife.", "He said, She is my sister.", "He feared they would kill him for Rebekah because she was beautiful."],
  'instructions': [ins(K, S, "Isaac passed Rebekah off as his sister in Gerar."), ins(W, R, "The sin of the father is repeated by the son in the same city; fear is inherited as readily as faith.")],
  'entries': ['isaac', 'rebekah'],
  'lost': [keeps("An added Rhebekkas, “Rebekah,” in the Greek’s opening clause where the Hebrew says ishto, “his wife.”"), between("Latin “feared to acknowledge that she was married to him” paraphrases the direct speech; King James follows the Hebrew.")]},

 '26:8': {
  'received': "After a long time Abimelech looked out of a window and saw Isaac caressing Rebekah.",
  'explain': ("The lie is found out by a glance. The verb is Isaac’s own name, metzacheq, laughing, playing, here of a husband’s affection. The Hebrew calls "
   "Abimelech king of the Philistines; the Greek king of Gerar; the Latin playing affectionately."),
  'shared': ["Isaac had been there a long time.", "Abimelech looked out through a window.", "He saw Isaac playing with Rebekah his wife."],
  'instructions': [ins(K, S, "Abimelech discovered that Rebekah was Isaac’s wife."), ins(W, R, "The laughter in Isaac’s name betrays him; what he could not say he could not help showing.")],
  'entries': ['isaac', 'rebekah'],
  'lost': [between("Hebrew melekh Pelishtim, “king of the Philistines,” is Greek ho basileus Gerarōn, “king of Gerar,” here; Latin and King James “king of the Philistines”; Hebrew metzacheq, “playing,” is Greek paizonta, Latin iocantem.")]},

 '26:9': {
  'received': "Abimelech confronted him; Isaac said he had feared dying on her account.",
  'explain': ("The Hebrew is an exclamation, behold, she is surely your wife, how could you say; the Greek makes it a question, so she is indeed your wife?; "
   "the Latin why did you lie. Isaac’s excuse is Abraham’s in 20:11, shorter."),
  'shared': ["Abimelech called Isaac.", "She is surely your wife; why did you say she was your sister?", "Isaac said he thought he might die because of her."],
  'instructions': [ins(K, S, "Isaac admitted the deception and his fear.")],
  'entries': ['isaac'],
  'lost': [between("Hebrew akh hinneh ishtekha hi ve-ekh amarta, “behold, surely she is your wife, and how did you say,” a statement, is Greek ara ge gynē sou estin; ti hoti eipas, “is she then your wife? why did you say,” a question; Latin “clearly she is your wife. Why did you lie”; King James “of a surety she is thy wife.”")]},

 '26:10': {
  'received': "Abimelech protested that someone might have lain with her and brought guilt on them all.",
  'explain': ("The pagan king’s moral indignation, as in chapter 20. The Hebrew says one of the people, guilt; the Greek one of my kin, an unwitting offence, "
   "agnoia, sin in ignorance; the Latin a great sin, and runs the command of verse 11 into this verse."),
  'shared': ["What have you done to us?", "One of the people might have lain with your wife.", "You would have brought guilt upon us."],
  'instructions': [ins(K, S, "Abimelech rebuked Isaac for exposing his people to guilt."), ins(W, R, "The king sees that a sin done in ignorance is still a sin and still brings guilt; the Philistine is more careful of holiness than the patriarch.")],
  'entries': [],
  'lost': [between("Hebrew achad ha-am, “one of the people,” is Greek tis tou genous mou, “one of my kin”; Hebrew asham, “guilt,” is Greek agnoian, “ignorance,” an unwitting offence; Latin “a great sin” and King James “guiltiness.”")]},

 '26:11': {
  'received': "He charged all the people that whoever touched Isaac or his wife would die.",
  'explain': ("Royal protection. The Hebrew says all the people, shall surely be put to death; the Greek all his people, liable to death; the Latin whoever "
   "touches this man’s wife, omitting the man."),
  'shared': ["Abimelech charged all the people.", "Whoever touches this man or his wife.", "He shall be put to death."],
  'instructions': [ins(K, S, "Abimelech placed Isaac and Rebekah under his protection."), ins(W, R, "The fear that made Isaac lie is answered by the king he lied to; protection comes from the quarter he distrusted.")],
  'entries': [],
  'lost': [keeps("An added autou, “his,” people in the Greek; Hebrew mot yumat, “dying he shall die,” is Greek enochos estai thanatō, “shall be liable to death.”"), between("Latin “whoever touches this man’s wife” drops the man; King James “this man or his wife.”")]},

 '26:12': {
  'received': "Isaac sowed and reaped a hundredfold that year, and the Lord blessed him.",
  'explain': ("The patriarch turns farmer and the blessing is visible in the harvest. The Greek says a hundredfold of barley; the others leave the crop unnamed."),
  'shared': ["Isaac sowed in that land.", "He reaped a hundredfold the same year.", "The Lord blessed him."],
  'instructions': [ins(K, S, "Isaac prospered as a farmer under God’s blessing."), ins(W, R, "The blessing follows the lie as it followed Abraham’s; grace is not withheld for failure, which is its scandal and its comfort.")],
  'entries': ['isaac', 'yhwh-yahweh'],
  'lost': [keeps("An added krithēn, “barley,” in the Greek names the crop."), between("Latin and King James leave it unnamed with the Hebrew.")]},

 '26:13': {
  'received': "He grew richer and richer until he was very great.",
  'explain': ("Three verbs of growth in the Hebrew. The versions agree; the Greek was exalted, advancing he increased."),
  'shared': ["The man became great.", "He went on prospering.", "He became very great."],
  'instructions': [ins(K, S, "Isaac became very wealthy.")],
  'entries': ['isaac'],
  'lost': [between("Hebrew va-yigdal … halokh ve-gadel, “he became great, going on and becoming great,” is Greek hypsōthē … probainōn meizōn egineto; Latin and King James follow the Hebrew’s sense.")]},

 '26:14': {
  'received': "He had flocks, herds and a great household, and the Philistines envied him.",
  'explain': ("The wealth and the envy. The Hebrew says a great avuddah, body of servants or husbandry; the Greek many tilled lands, taking the word as "
   "cultivation; the Latin a very large household; the King James great store of servants."),
  'shared': ["He had flocks and herds.", "He had a large establishment.", "The Philistines envied him."],
  'instructions': [ins(K, S, "The Philistines envied Isaac’s wealth."), ins(W, R, "Blessing draws envy; Isaac is about to be asked to leave for the very prosperity God gave him.")],
  'entries': ['isaac'],
  'lost': [between("Hebrew avuddah rabbah, “much service,” servants or farming, is Greek geōrgia polla, “many tilled lands”; Latin “a very large household” and King James “great store of servants” take the servants.")]},

 '26:15': {
  'received': "The Philistines had stopped up all the wells Abraham’s servants dug and filled them with earth.",
  'explain': ("Envy acts: the wells of Abraham are filled in. In a dry land this is hostility, not mischief. The Hebrew names Abraham; the Greek says his father without the name."),
  'shared': ["Abraham’s servants had dug wells in his days.", "The Philistines stopped them up.", "They filled them with earth."],
  'instructions': [ins(K, S, "The Philistines filled in Abraham’s wells."), ins(W, R, "The wells of the fathers are stopped by the next generation’s envy; the son must dig again what was already dug.")],
  'entries': ['abraham'],
  'lost': [loses("Hebrew Avraham aviv, “Abraham his father,” becomes Greek tou patros autou, “his father,” without the name."), between("Latin and King James name Abraham.")]},

 '26:16': {
  'received': "Abimelech told Isaac to leave because he had grown too mighty.",
  'explain': ("Expulsion by the king who had protected him. The versions agree; the Latin until Abimelech himself said."),
  'shared': ["Abimelech spoke to Isaac.", "Depart from us.", "You have become much mightier than we."],
  'instructions': [ins(K, S, "Abimelech expelled Isaac from Gerar."), ins(W, R, "“Mightier than we” is Pharaoh’s fear of Israel in Exodus 1:9 spoken a generation early; the blessed are always a worry to their hosts.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '26:17': {
  'received': "Isaac left and camped in the valley of Gerar.",
  'explain': ("He goes without protest to the wadi of Gerar, still Philistine country. The versions agree."),
  'shared': ["Isaac departed.", "He camped in the valley of Gerar.", "He dwelt there."],
  'instructions': [ins(K, S, "Isaac moved to the valley of Gerar.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '26:18': {
  'received': "He reopened the wells of Abraham’s day that the Philistines had stopped, and gave them their old names.",
  'explain': ("Restoration: the wells and the names. The Greek says Abraham’s servants dug them, Abraham his father twice; the Hebrew dug in the days of Abraham, his father; the Latin other wells."),
  'shared': ["Isaac dug again the wells of Abraham’s days.", "The Philistines had stopped them after Abraham died.", "He gave them the names his father had given."],
  'instructions': [ins(K, S, "Isaac restored his father’s wells and their names."), ins(W, R, "Isaac’s work is recovery, not discovery; the second generation’s calling is to reopen what the first dug and keep the names.")],
  'entries': ['isaac', 'abraham'],
  'lost': [keeps("An added hoi paides Abraam tou patros autou, “the servants of Abraham his father,” and a repeated Abraam in the Greek where the Hebrew says “in the days of Abraham his father … his father.”"), between("Latin “other wells” varies; King James follows the Hebrew.")]},

 '26:19': {
  'received': "Isaac’s servants dug in the valley and found a well of living water.",
  'explain': ("A new well with running water, mayim chayyim, the phrase Jeremiah and John will use. The Greek adds Gerar; the Latin flowing water."),
  'shared': ["Isaac’s servants dug in the valley.", "They found a well.", "It was living water."],
  'instructions': [ins(K, S, "Isaac’s servants found a spring in the valley.")],
  'entries': ['isaac'],
  'lost': [keeps("An added Gerarōn, “of Gerar,” after the valley in the Greek."), between("Latin “flowing water” and King James “springing water” render the living water; Latin drops Isaac’s servants.")]},

 '26:20': {
  'received': "Gerar’s herdsmen claimed the water, so he named the well Esek, contention.",
  'explain': ("The first quarrel. The Hebrew name Esek means contention, from the verb used; the Greek translates it Injustice, because they wronged him; the Latin Dispute; the King James Esek."),
  'shared': ["The herdsmen of Gerar quarrelled with Isaac’s herdsmen.", "They said the water was theirs.", "He named the well for the quarrel."],
  'instructions': [ins(K, S, "The first well was named Esek for the dispute."), ins(W, R, "Isaac names the well for the wrong and moves on; he records the injustice and does not fight for the water.")],
  'entries': ['isaac'],
  'lost': [loses("Hebrew Eseq … ki hit‘asseku immo, “Esek, because they contended with him,” a name and its echo, becomes Greek Adikia … ēdikēsan gar auton, “Injustice, for they wronged him,” a translation with a different sense."), between("Latin Calumniam, “Dispute,” translates; King James “Esek; because they strove with him” keeps the name.")]},

 '26:21': {
  'received': "They dug another well and quarrelled over it too, so he named it Sitnah, enmity.",
  'explain': ("The second quarrel. Sitnah is from the root of Satan, the adversary. The Greek adds Isaac moved on from there and translates the name Enmity; the Latin Hostility."),
  'shared': ["They dug another well.", "They quarrelled over that one also.", "He named it for the hostility."],
  'instructions': [ins(K, S, "The second well was named Sitnah.")],
  'entries': ['isaac'],
  'lost': [keeps("An added aparas de Isaak ekeithen, “Isaac moved on from there,” in the Greek; Hebrew Sitnah is Greek Echthria, “Enmity.”"), between("Latin Inimicitias, “Hostility,” translates; King James “Sitnah.”")]},

 '26:22': {
  'received': "He moved on and dug a third well, uncontested, and named it Rehoboth: the Lord has made room for us.",
  'explain': ("Room at last. Rehoboth means broad places. The Hebrew says we will be fruitful in the land; the Greek has increased us; the Latin Spaciousness, upon the earth."),
  'shared': ["He moved and dug another well.", "They did not quarrel over it.", "He named it Rehoboth, for the Lord has made room for us and we will be fruitful."],
  'instructions': [ins(K, S, "The third well, Rehoboth, was uncontested."), ins(W, R, "Isaac yields twice and the third time finds room; the meek inherit a well before they inherit the earth.")],
  'entries': ['isaac', 'yhwh-yahweh'],
  'lost': [between("Hebrew Rechovot … u-farinu, “Rehoboth … and we will be fruitful,” is Greek Eurychōria … kai ēuxēsen hēmas, “Broad Space … and has increased us,” a translation and a past tense; Latin Latitudinem, “Spaciousness,” and “caused us to increase upon the earth”; King James “Rehoboth … we shall be fruitful.”")]},

 '26:23': {
  'received': "From there he went up to Beersheba.",
  'explain': ("Back to Abraham’s Beersheba of 21:31. The Hebrew keeps the name; the Greek translates, the Well of the Oath; the Latin Beersheba."),
  'shared': ["He went up from there.", "He went to Beersheba.", "It was his father’s place."],
  'instructions': [ins(K, S, "Isaac returned to Beersheba.")],
  'entries': ['isaac'],
  'lost': [loses("Hebrew Be’er Sheva, a name, becomes Greek to phrear tou horkou, “the Well of the Oath,” a translation."), between("Latin and King James “Beersheba.”")]},

 '26:24': {
  'received': "That night the Lord appeared: I am the God of your father Abraham; fear not, I am with you and will bless you and multiply your seed for Abraham’s sake.",
  'explain': ("The second theophany, with fear not, the first time the phrase is addressed to a patriarch since 15:1. The Hebrew says I will bless you, for the sake "
   "of Abraham My servant; the Greek I have blessed you, Abraham your father; the Latin and King James follow the Hebrew."),
  'shared': ["The Lord appeared to him that night.", "I am the God of Abraham your father; fear not, I am with you.", "I will bless you and multiply your seed for Abraham’s sake."],
  'instructions': [ins(K, S, "God reassured Isaac at Beersheba."), ins(W, R, "“Fear not” comes to the man whose fear has shaped the chapter; God names the problem and answers it with presence.")],
  'entries': ['isaac', 'abraham', 'yhwh-yahweh'],
  'lost': [loses("Hebrew u-verakhtikha, “and I will bless you,” becomes Greek kai eulogēka se, “and I have blessed you”; Hebrew Avraham avdi, “Abraham My servant,” becomes Abraam ton patera sou, “Abraham your father.”"), between("Latin “I will bless you … My servant Abraham” and King James “will bless thee … my servant Abraham” keep the Hebrew.")]},

 '26:25': {
  'received': "He built an altar, called on the Lord’s name, pitched his tent, and his servants dug a well.",
  'explain': ("Isaac’s only altar, built at the place of the word, as Abraham built his. The Latin says he commanded his servants to dig; the others they dug."),
  'shared': ["He built an altar there and called on the name of the Lord.", "He pitched his tent there.", "Isaac’s servants dug a well."],
  'instructions': [ins(K, S, "Isaac worshipped at Beersheba and dug a well."), ins(W, R, "Altar, tent, well: worship, dwelling, water, in that order. The pattern of the fathers is the pattern of a settled faith.")],
  'entries': ['isaac', 'altar', 'yhwh-yahweh'],
  'lost': [between("Latin “commanded his servants to dig a well” makes Isaac the actor; Hebrew, Greek and King James “Isaac’s servants dug.”")]},

 '26:26': {
  'received': "Abimelech came from Gerar with Ahuzzath his adviser and Phicol his army commander.",
  'explain': ("The king who expelled him comes to him, with his court. Phicol was also the commander in Abraham’s day, 21:22; a title or a family name. The Hebrew "
   "calls Ahuzzath his companion; the Greek his groomsman, nymphagōgos; the Latin his friend."),
  'shared': ["Abimelech came to him from Gerar.", "Ahuzzath his companion came.", "Phicol the commander of his army came."],
  'instructions': [ins(K, S, "Abimelech sought out Isaac at Beersheba.")],
  'entries': [],
  'lost': [between("Hebrew mere‘ehu, “his companion” or “adviser,” is Greek ho nymphagōgos autou, “his groomsman,” a court title; Latin “his friend,” King James “one of his friends.”")]},

 '26:27': {
  'received': "Isaac asked why they came, since they hated him and had sent him away.",
  'explain': ("Isaac speaks plainly for once. The versions agree."),
  'shared': ["Isaac spoke to them.", "Why have you come to me?", "You hate me and sent me away."],
  'instructions': [ins(K, S, "Isaac confronted the Philistine delegation."), ins(W, R, "The man who lied about his wife tells the truth about his hosts; blessing has given him a voice.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '26:28': {
  'received': "They said they had seen the Lord was with him and wanted an oath and covenant.",
  'explain': ("The Philistines confess what the chapter has shown. The versions agree; the Latin compresses."),
  'shared': ["We have clearly seen that the Lord is with you.", "Let there be an oath between us and you.", "Let us make a covenant with you."],
  'instructions': [ins(K, S, "The Philistines sought a covenant because God was with Isaac."), ins(W, R, "“We saw that the Lord was with you” is said by the people who filled in his wells; the blessing on Isaac is visible even to his enemies.")],
  'entries': ['term-covenant', 'yhwh-yahweh'],
  'lost': [AGREE]},

 '26:29': {
  'received': "that he would do them no harm, as they had not touched him but sent him away in peace, blessed of the Lord.",
  'explain': ("Their version of events, which omits the wells. The Hebrew says we have not touched you; the Greek we have not loathed you; the Latin touched nothing of yours. The narrator does not endorse the claim."),
  'shared': ["You will do us no harm.", "We have not touched you but treated you well and sent you away in peace.", "You are now blessed of the Lord."],
  'instructions': [ins(K, S, "The Philistines asked for a non-aggression oath.")],
  'entries': ['yhwh-yahweh'],
  'lost': [loses("Hebrew lo nega‘anukha, “we have not touched you,” becomes Greek ouk ebdelyxametha se, “we have not loathed you.”"), between("Latin “touched nothing of yours” and King James “have not touched thee” keep the touching.")]},

 '26:30': {
  'received': "He made them a feast and they ate and drank.",
  'explain': ("Isaac accepts. The versions agree."),
  'shared': ["He made them a feast.", "They ate.", "They drank."],
  'instructions': [ins(K, S, "Isaac feasted the Philistines."), ins(W, R, "He feeds the men who starved his wells; the covenant meal is the patriarch’s answer to the envy of his neighbours.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '26:31': {
  'received': "In the morning they swore to one another and Isaac sent them away in peace.",
  'explain': ("The oath exchanged at dawn. The Hebrew says in peace; the Greek in safety; the Latin to their own place."),
  'shared': ["They rose early in the morning.", "They swore an oath to one another.", "Isaac sent them away and they departed in peace."],
  'instructions': [ins(K, S, "Isaac and Abimelech swore a mutual oath.")],
  'entries': ['isaac'],
  'lost': [between("Hebrew be-shalom, “in peace,” is Greek meta sōtērias, “with safety”; Latin “peacefully to their own place,” King James “in peace.”")]},

 '26:32': {
  'received': "That day Isaac’s servants reported on the well they had dug: We have found water.",
  'explain': ("The well of verse 25 strikes water on the day of the oath, giving the name of verse 33. The Hebrew, Latin and King James say we have found water; "
   "the Greek says we did not find water, a negation found in the Greek tradition alone and the one outright contradiction of the chapter. The Greek reading may "
   "reflect a different text or a scribal slip; the naming in verse 33 presumes success."),
  'shared': ["It was the same day.", "Isaac’s servants came and told him about the well they had dug.", "They reported on the water."],
  'instructions': [ins(K, S, "The servants reported finding water on the day of the oath."), ins(W, R, "Water and oath arrive together, and the place is named for both; the Greek’s “we did not find” stands as a reminder that even the columns can quarrel over a well.")],
  'entries': ['isaac'],
  'lost': [loses("Hebrew matzanu mayim, “we have found water,” becomes Greek ouch heuromen hydōr, “we did not find water”; the negative is the Greek’s alone and reverses the report."), between("Latin “we have found water” and King James “we have found water” follow the Hebrew.")]},

 '26:33': {
  'received': "He named it Shibah; so the city is Beersheba to this day.",
  'explain': ("Shibah means oath, or seven; Beersheba is the well of the oath, or of the seven, named already by Abraham in 21:31 and now renamed by his son for his own oath. "
   "The Greek translates Oath and Well of the Oath; the Latin Abundance, reading a different root."),
  'shared': ["He named the well.", "The city is called Beersheba.", "It is so to this day."],
  'instructions': [ins(K, S, "Isaac named the well Shibah, confirming the name Beersheba."), ins(W, R, "Father and son name the same well for oaths a generation apart; the place keeps the memory of two covenants.")],
  'entries': ['isaac'],
  'lost': [loses("Hebrew Shiv‘ah … Be’er Sheva, names, become Greek Horkos … Phrear horkou, “Oath … Well of Oath,” translations."), between("Latin Abundantiam, “Abundance,” reads the root of plenty; King James “Shebah … Beersheba.”")]},

 '26:34': {
  'received': "At forty Esau married two Hittite women, Judith daughter of Beeri and Basemath daughter of Elon.",
  'explain': ("Esau marries at the age his father did, but into Canaan, against the family rule of chapter 24. The Hebrew calls Elon a Hittite; the Greek a Hivite; the Latin from the same place. The names differ in 36:2."),
  'shared': ["Esau was forty years old.", "He married Judith, daughter of Beeri the Hittite.", "He married Basemath, daughter of Elon."],
  'instructions': [ins(K, S, "Esau took two Canaanite wives."), ins(W, R, "Esau does at forty what Abraham swore his servant must not do for Isaac; the birthright he sold, the marriage shows he never valued.")],
  'entries': ['isaac'],
  'lost': [loses("Hebrew Elon ha-Chitti, “Elon the Hittite,” becomes Greek Ailōn tou Euaiou, “Elon the Hivite,” a different people."), between("Latin “Elon from the same place” and King James “Elon the Hittite” follow the Hebrew’s sense.")]},

 '26:35': {
  'received': "They were a bitterness of spirit to Isaac and Rebekah.",
  'explain': ("The marriages grieve both parents, the one point on which Isaac and Rebekah agree. The Hebrew says a bitterness of spirit; the Greek continually quarrelling; the Latin both grieved the hearts of Isaac and Rebekah."),
  'shared': ["Esau’s wives affected his parents.", "They were a grief to Isaac.", "They were a grief to Rebekah."],
  'instructions': [ins(K, S, "Esau’s wives grieved Isaac and Rebekah."), ins(W, R, "The chapter ends with the household in bitterness; the stage is set for the deception of chapter 27.")],
  'entries': ['isaac', 'rebekah'],
  'lost': [loses("Hebrew morat ruach, “bitterness of spirit,” becomes Greek erizousai, “quarrelling,” an outward act for an inward grief."), between("Latin “grieved the hearts” and King James “a grief of mind” keep the inward sense.")]},
 }
}
