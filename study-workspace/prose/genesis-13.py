# Study prose for Genesis 13 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 13,
 'chapterNote': (
  "The return from Egypt, the parting of Abram and Lot and the renewed promise are the same in every column. What varies is small and "
  "mostly geographical. The Hebrew keeps the Negev as Abram’s route up from Egypt, journeying by stages, an altar “made at first,” the "
  "garden of YHWH, Lot’s tents reaching as far as Sodom among the cities of the plain, dust for the offspring, the four compass points, and "
  "the oaks of Mamre. The Greek keeps the wilderness for the Negev, “where he had made a beginning,” the paradise of God, Lot in one city and "
  "encamped in Sodom, sand for dust, “the sea” for west, God where the Hebrew has YHWH, and a single oak of Mamre. The Latin and King James "
  "follow the Hebrew; the Latin has “the valley of Mamre.”"),
 'verses': {

 '13:1': {
  'received': "Abram went up from Egypt with his wife, all he had and Lot, back toward the south of the land.",
  'explain': ("Leaving Egypt is always going up, because the land of promise lies higher; Scripture speaks of the exodus the same way. Abram "
   "returns the way he came, with Sarai, his goods and Lot. The Hebrew says toward the Negev, the Latin the southern region; the Greek "
   "says into the wilderness, the dry land he crossed on the way down."),
  'shared': ["Abram went up from Egypt.", "His wife and all he had went with him.", "Lot was with him."],
  'instructions': [ins(K, S, "Abram returned from Egypt to the south of the land with his household and Lot."), ins(W, R, "Going up out of Egypt is the shape of return; the way back to the promise retraces the way of the failure.")],
  'entries': ['abraham', 'egypt'],
  'lost': [
   loses("Hebrew ha-negbah, “toward the Negev,” names the southern region; Greek eis tēn erēmon, “into the wilderness,” describes the terrain. The Negev is gone from the Greek, as in 12:9."),
   between("Latin “the southern region” and King James “the south” follow the Hebrew. Greek anebē, “went up,” is the verb of every return from Egypt (46:4; Exodus 13:18)."),
  ]},

 '13:2': {
  'received': "Abram was very rich in livestock, silver and gold.",
  'explain': ("The wealth gathered in Haran and Egypt is now stated outright. The Hebrew says Abram was very heavy, the word that also gives "
   "glory, and his weight of wealth will divide the family. This is the first mention of silver as wealth in Scripture. The Latin omits the "
   "livestock; the others name it."),
  'shared': ["Abram was very rich.", "He had silver and gold.", "His wealth is stated before the quarrel."],
  'instructions': [ins(K, S, "Abram returned from Egypt a very rich man."), ins(W, R, "Riches are a weight as the Hebrew says; the next verses show what the weight does to kinship.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew kaved me’od, “very heavy,” is Greek plousios sphodra, “very rich.” Latin “possessions of gold and silver” drops the livestock; King James “cattle, silver, and gold” keeps it. Greek argyrion, “silver,” is the money of 23:16.")]},

 '13:3': {
  'received': "Abram travelled back from the south to Bethel, to the place where his tent had first stood between Bethel and Ai.",
  'explain': ("Abram goes back to the exact spot of 12:8, his place of first worship, before anything new happens. The Hebrew says he went by "
   "stages from the Negev; the Greek that he went the way he had come, into the wilderness; the Latin that he returned along his route "
   "from the south. Abraham never builds a house in the land; Hebrews says he lived in tents looking for the city with foundations."),
  'shared': ["Abram travelled from the south.", "He came to Bethel.", "He returned to where his tent had first been, between Bethel and Ai."],
  'instructions': [ins(K, S, "Abram returned to his first camp between Bethel and Ai.")],
  'entries': ['abraham', 'bethel'],
  'lost': [
   loses("Hebrew le-massa‘av mi-negev, “by his stages from the Negev,” becomes Greek hothen ēlthen, eis tēn erēmon, “from where he had come, into the wilderness”; the stages and the Negev are gone."),
   between("Latin “along the way he had come, from the south” combines the two; King James “on his journeys from the south” follows the Hebrew. Hebrews 11:9–10 reads the tent."),
  ]},

 '13:4': {
  'received': "He came to the place of the altar he had made before, and called on the name of the Lord.",
  'explain': ("Abram returns to the altar, not to a city, and resumes the worship broken off by the famine. The Hebrew says the altar he had "
   "made there at first; the Greek the place of the altar where he had made a beginning, turning the first altar into a first step. "
   "The calling on the Lord’s name repeats 12:8."),
  'shared': ["He came to the place of the earlier altar.", "He had made it at the first.", "There Abram called on the name of the Lord."],
  'instructions': [ins(K, S, "Abram resumed worship at the altar he had built before Egypt."), ins(W, R, "After a failure the way back is the old altar; Abram begins again where he first prayed.")],
  'entries': ['abraham', 'altar', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew asher-asah sham ba-rishonah, “which he had made there at first,” describes the altar; Greek hou epoiēsen ekei tēn archēn, “where he had made a beginning,” describes an act. Hebrew YHWH is “the Lord.”"),
   between("Latin “the altar he had made before” and King James “the altar, which he had made there at the first” follow the Hebrew; the Latin drops Abram’s name."),
  ]},

 '13:5': {
  'received': "Lot, who travelled with Abram, also had flocks, herds and tents.",
  'explain': ("Lot has grown wealthy too. His tents mean households; he now heads his own families and servants, not merely a share of his "
   "uncle’s camp. The Greek says sheep where the Hebrew says flocks. The two camps are ready to collide."),
  'shared': ["Lot travelled with Abram.", "Lot had flocks and herds.", "Lot had tents."],
  'instructions': [ins(K, S, "Lot had become a wealthy householder in his own right.")],
  'entries': [],
  'lost': [between("Hebrew tson, “flocks,” is Greek probata, “sheep,” as in chapter 7; the Latin spells it out, “flocks of sheep, herds.” Hebrew gam, “also,” is absent from the Greek. Greek skēnai, “tents,” is the word of 4:20.")]},

 '13:6': {
  'received': "The land could not support them together because their possessions were so great.",
  'explain': ("Prosperity, not poverty, divides them. There is not enough pasture for two such camps in one place. The Hebrew says the land "
   "could not bear them; the Greek that it could not accommodate them; the sense is the same practical difficulty, and the verse says it twice."),
  'shared': ["The land could not support them living together.", "Their possessions were great.", "They could not live together."],
  'instructions': [ins(K, S, "Abram and Lot could no longer live together because of their wealth."), ins(W, R, "Plenty can separate as surely as want; the land that could feed two poor men cannot hold two rich ones.")],
  'entries': [],
  'lost': [between("Hebrew lo-nasa otam, “could not bear them,” is Greek ouk echōrei autous, “could not contain them.” Latin and King James agree in sense; the Latin ends “could not live in the same place.”")]},

 '13:7': {
  'received': "The herdsmen of Abram and Lot quarrelled, while the Canaanites and Perizzites lived in the land.",
  'explain': ("The strife is between servants, but it threatens the masters. The note about the Canaanites and Perizzites, dwellers in "
   "unwalled villages, reminds the reader that the land is not yet Abram’s and that a family quarrel is watched by strangers. The versions agree."),
  'shared': ["There was strife between Abram’s herdsmen and Lot’s.", "The Canaanites were then in the land.", "The Perizzites were in the land too."],
  'instructions': [ins(K, S, "A quarrel arose between the herdsmen of Abram and of Lot."), ins(W, R, "Quarrels among God’s people are seen by those outside; the Canaanites are mentioned so that the reader remembers who is watching.")],
  'entries': ['canaan'],
  'lost': [between("Hebrew riv, “strife,” is Greek machē, “quarrel”; the Latin compresses “herdsmen of Abram and Lot.” Greek Pherezaioi are the Perizzites of 15:20 and Joshua 17:15.")]},

 '13:8': {
  'received': "Abram asked Lot that there be no strife between them or their herdsmen, since they were kinsmen.",
  'explain': ("Abram speaks first and speaks for peace. He calls Lot his brother, the word for kinsmen generally, not a correction of uncle "
   "and nephew. The Hebrew and Latin include a polite appeal, “please”; the Greek states the wish directly. The elder gives way to the younger."),
  'shared': ["Abram spoke to Lot.", "He asked that there be no strife between them or their herdsmen.", "He gave the reason: we are brothers."],
  'instructions': [ins(K, S, "Abram sought peace with Lot on the ground of kinship."), ins(W, R, "“We are brothers” is reason enough to end a quarrel; Abram puts kinship above pasture.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew al-na, “please let there not be,” has a particle of entreaty that Greek mē estō, “let there not be,” lacks; Latin “please” and King James “I pray thee” keep it. Hebrew achim and Greek adelphoi are “brothers,” kinsmen.")]},

 '13:9': {
  'received': "Abram offered Lot the whole land and the first choice: left or right, he would take the other.",
  'explain': ("Abram, the one to whom the land was promised, gives his nephew first pick of it. If Lot goes left Abram goes right, and the "
   "reverse. The Hebrew again says please; the Latin begins “see.” The offer is generous to the point of risk, and the next verses show "
   "what Lot does with it."),
  'shared': ["The whole land is before Lot.", "Abram asks Lot to separate from him.", "Whichever side Lot takes, Abram will take the other."],
  'instructions': [ins(K, S, "Abram let Lot choose his land first."), ins(W, R, "The heir of the promise can afford to give the first choice away; he trusts the one who gave the land, not his own grip on it.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew hippared na, “please separate,” has the entreaty the Greek diachōristhēti lacks; Latin “please” and King James “I pray thee” keep it. The left-and-right offer is the same in all four.")]},

 '13:10': {
  'received': "Lot looked at the well-watered Jordan plain, like the garden of the Lord and like Egypt, before Sodom and Gomorrah were destroyed.",
  'explain': ("Lot chooses with his eyes. The Jordan valley, here named for the first time, is green like the garden of Eden and like Egypt; "
   "the narrator adds that this was before the destruction of Sodom and Gomorrah, so the reader knows what Lot does not. The Hebrew says "
   "the garden of YHWH; the Greek the paradise of God. Zoar is the small city that will be spared."),
  'shared': ["Lot looked at the whole region of the Jordan.", "It was well watered, like the garden of the Lord and like Egypt toward Zoar.", "This was before the Lord destroyed Sodom and Gomorrah."],
  'instructions': [ins(K, S, "Lot chose the Jordan plain for its beauty before its destruction."), ins(W, R, "What looks like paradise and Egypt at once is chosen for what it looks like; the reader is told the end before Lot makes the choice.")],
  'entries': ['jordan', 'egypt', 'eden', 'yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew gan-YHWH, “the garden of YHWH,” becomes Greek paradeisos tou theou, “the paradise of God”; Hebrew YHWH destroyed becomes Greek ho theos katastrepsai, “God overturned.” Hebrew bo’akhah Tso‘ar, “as you go toward Zoar,” becomes heōs elthein eis Zogora, “as far as Zoar.”"),
   between("Latin “the Lord destroyed … the garden of the Lord” and King James “the LORD destroyed … the garden of the LORD” keep the name. Greek Iordanēs is the Jordan of Joshua 3:17 and Matthew 3:13; 19:20–23 explains Zoar."),
  ]},

 '13:11': {
  'received': "Lot chose the whole Jordan plain and moved east, and the two parted.",
  'explain': ("Lot picks for himself, and picks what will be destroyed; the Greek verb for choosing is the one used of God choosing his "
   "people. In Genesis moving east often means moving away, Adam from Eden, Cain to Nod, the builders to Babel. The Hebrew is usually "
   "read as eastward; the Greek says from the east. They separate."),
  'shared': ["Lot chose the whole region of the Jordan.", "He journeyed east.", "They separated from one another."],
  'instructions': [ins(K, S, "Lot chose the Jordan plain and parted from Abram."), ins(W, R, "To choose for oneself by sight is Lot’s whole story; his eastward move repeats the pattern of leaving.")],
  'entries': ['jordan'],
  'lost': [between("Hebrew mi-qedem can mean “eastward” or “from the east”; Greek apo anatolōn reads “from the east,” Latin likewise, King James “journeyed east.” Hebrew “each from his brother” is kept in the Latin and spelled “the one from the other” in King James. Greek exelexato, “chose,” is the verb of Deuteronomy 7:6.")]},

 '13:12': {
  'received': "Abram settled in Canaan, while Lot settled among the cities of the plain and pitched his tents toward Sodom.",
  'explain': ("The two homes are set side by side. Abram stays in the land of Canaan; Lot takes the valley. The Hebrew has Lot settle in the "
   "cities of the plain and pitch his tents as far as Sodom, a process reaching toward the city; the Greek has him settle in a city of the "
   "region and encamp in Sodom itself. The Latin and King James stand nearer the Hebrew."),
  'shared': ["Abram settled in the land of Canaan.", "Lot settled in the region of the Jordan.", "Lot’s tents reached Sodom."],
  'instructions': [ins(K, S, "Abram stayed in Canaan while Lot moved toward Sodom."), ins(W, R, "Lot’s tents move toward Sodom by degrees; in the next chapter he is inside it. Drift ends in residence.")],
  'entries': ['abraham', 'canaan'],
  'lost': [
   loses("Hebrew be-are ha-kikkar, “in the cities of the plain,” plural, and va-ye’ehal ad-Sedom, “pitched his tents as far as Sodom,” a movement toward. Greek en polei tōn perichōrōn, “in a city of the surrounding region,” singular, and eskēnōsen en Sodomois, “encamped in Sodom,” a position. The Hebrew’s gradual approach is gone."),
   between("Latin “the towns around the Jordan … lived in Sodom” keeps the plural and the residence; King James “the cities of the plain … pitched his tent toward Sodom” follows the Hebrew."),
  ]},

 '13:13': {
  'received': "The men of Sodom were exceedingly wicked sinners against the Lord.",
  'explain': ("The verdict on Sodom is given before Lot arrives, so that the reader judges his choice. The Hebrew says they sinned against "
   "YHWH; the Greek before God, in his sight. Ezekiel names Sodom’s pride, plenty and neglect of the poor; Jude names sexual sin. The "
   "versions agree on the exceeding wickedness."),
  'shared': ["The men of Sodom were wicked.", "They were sinners against the Lord.", "Their wickedness was exceeding."],
  'instructions': [ins(K, S, "Sodom was already known for wickedness when Lot settled there."), ins(W, R, "A green valley and a wicked city go together in Lot’s choice; the eye saw the one and ignored the other.")],
  'entries': ['yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew la-YHWH, “against YHWH,” becomes Greek enantion tou theou, “before God”; the name changes and the relation shifts from against to in the sight of."),
   between("Latin “before the Lord” and King James “before the LORD” keep the name but share the Greek’s “before.” Ezekiel 16:49–50 and Jude 7 describe the sins."),
  ]},

 '13:14': {
  'received': "After Lot had gone, the Lord told Abram to look north, south, east and west from where he stood.",
  'explain': ("When Lot has taken the best, God speaks. Abram is told to look in all four directions. The Hebrew says YHWH; the Greek God. "
   "The Greek says “the sea” for west, as the Hebrew idiom does elsewhere; for people in the land the Mediterranean simply meant west. "
   "The whole horizon is in view."),
  'shared': ["Lot had separated from Abram.", "The Lord spoke to Abram.", "He told him to look north, south, east and west."],
  'instructions': [ins(C, S, "Raise your eyes and look in every direction from where you are."), ins(W, R, "Lot looked and chose; Abram is told to look and receive. The same act of looking is faith or grasping according to who commands it.")],
  'entries': ['abraham', 'yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew YHWH becomes Greek ho theos. Hebrew yammah, “seaward,” is Greek thalassan, “the sea,” which the Hebrew column renders “westward.” Greek adds nyn, “now,” to “where you are.”"),
   between("Latin “the Lord … east and west” and King James “the LORD … westward” follow the Hebrew name and give the compass point."),
  ]},

 '13:15': {
  'received': "God promised all the land Abram could see to him and his offspring forever.",
  'explain': ("The promise of 12:7 is enlarged in two directions: to Abram himself as well as his offspring, and forever. Everything in sight "
   "is included. All versions agree exactly."),
  'shared': ["All the land Abram sees is promised.", "It is promised to him and his offspring.", "It is promised forever."],
  'instructions': [ins(K, S, "God promised Abram and his offspring all the land he could see, forever."), ins(W, R, "Lot took a valley; Abram is given everything in sight. Giving up the first choice loses nothing that God means to give.")],
  'entries': ['abraham', 'canaan'],
  'lost': [between("Hebrew, Greek, Latin and King James agree. Hebrew ad-olam and Greek heōs tou aiōnos are both “forever.”")]},

 '13:16': {
  'received': "God promised to make Abram’s offspring as countless as the dust of the earth.",
  'explain': ("The childless man is promised descendants beyond counting. The Hebrew compares them to the dust of the earth; the Greek to its "
   "sand. Later the image will be the stars of heaven and the sand of the seashore. Both carry the comparison into a second clause: if "
   "anyone can count the dust, your offspring too can be counted."),
  'shared': ["God will make Abram’s offspring like the dust of the earth.", "The dust cannot be counted.", "Neither will his offspring be counted."],
  'instructions': [ins(K, S, "Abram’s descendants will be beyond counting."), ins(W, R, "The promise is given in the image of what Abram walks on; the ordinary ground becomes the measure of hope.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew afar ha-arets, “dust of the earth,” becomes Greek ammos tēs gēs, “sand of the earth,” twice. The dust, with its echo of 2:7 and 3:19, is gone from the Greek."),
   between("Latin and King James keep dust with the Hebrew. Genesis 15:5, 22:17 and 28:14 vary the image; Romans 9:27 uses sand."),
  ]},

 '13:17': {
  'received': "God told Abram to walk the length and breadth of the land, for it would be his.",
  'explain': ("Looking is followed by walking. Abram is to pace out the land as an owner surveys a property, though he will own only a grave "
   "in it. The command and the promise agree in every version."),
  'shared': ["Abram is to arise and walk through the land.", "He is to cover its length and breadth.", "God will give it to him."],
  'instructions': [ins(C, S, "Arise and walk through the length and breadth of the land."), ins(W, R, "Walking the land is a way of believing the promise; the feet take possession before the title comes.")],
  'entries': ['abraham', 'canaan'],
  'lost': [between("Hebrew, Greek, Latin and King James agree in every clause.")]},

 '13:18': {
  'received': "Abram moved his tent to the oaks of Mamre at Hebron and built an altar to the Lord there.",
  'explain': ("Abram settles at Hebron, the home and burial place of the patriarchs and later David’s first capital, by the trees of Mamre, "
   "named for an Amorite ally. Here God will visit him in chapter 18. The Hebrew says oaks, plural; the Greek one oak; the Latin a valley. "
   "The chapter ends as 12 did, with an altar to the Lord."),
  'shared': ["Abram moved his tent.", "He settled by Mamre at Hebron.", "He built an altar there to the Lord."],
  'instructions': [ins(K, S, "Abram settled at Hebron and built an altar."), ins(W, R, "The chapter that began with a return to an old altar ends with a new one; worship frames the parting from Lot.")],
  'entries': ['abraham', 'hebron', 'altar', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew elone Mamre, “the oaks of Mamre,” plural, becomes Greek tēn dryn tēn Mambrē, “the oak of Mamre,” singular; YHWH is “the Lord.”"),
   between("Latin “the valley of Mamre” and King James “the plain of Mamre” take the Hebrew word as a place rather than trees. Genesis 14:13, 18:1 and 23:19 return to Mamre; 2 Samuel 5:3 to Hebron."),
  ]},
 }
}
