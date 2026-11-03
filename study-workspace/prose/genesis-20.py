# Study prose for Genesis 20 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 20,
 'chapterNote': (
  "Abraham’s second “she is my sister,” God’s warning to Abimelech, the king’s rebuke and the restoration of Sarah are the same story in "
  "every column. What varies is explanation and emphasis. The Hebrew keeps Abraham’s motive for his own mouth in 20:11, a dream, “she is "
  "married to a husband,” Abimelech’s “how have I sinned,” integrity and innocence, God “keeping” Abimelech from sin, “kindness” for Sarah’s "
  "part, the thousand pieces of silver first in 20:16, and a difficult closing clause about a covering of the eyes and vindication. The Greek "
  "keeps a narrator’s note in 20:2 that Abraham feared for his life, “sleep” for dream, “she has lived with a husband,” an “ignorant and righteous "
  "nation,” purity and righteousness, God “sparing” Abimelech, “righteousness” for kindness, a thousand didrachms already in 20:14, and in 20:16 "
  "“for the honour of your face … speak the truth in everything.” The Latin and King James follow the Hebrew; the Latin has Abimelech rise in the night."),
 'verses': {

 '20:1': {
  'received': "Abraham moved south, settled between Kadesh and Shur, and sojourned in Gerar.",
  'explain': ("After Sodom, Abraham moves to the south country, the Negev, and lives as a resident alien in Gerar, a Philistine town near the Egyptian "
   "frontier. Kadesh and Shur were named in 14:7 and 16:7. The Hebrew says the land of the Negev; the Greek and Latin the southern land; none says "
   "wilderness here. The scene is set for a second version of chapter 12."),
  'shared': ["Abraham journeyed from there to the south country.", "He settled between Kadesh and Shur.", "He sojourned in Gerar."],
  'instructions': [ins(K, S, "Abraham settled in the south and lived as a sojourner in Gerar.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew artsah ha-negev, “to the land of the Negev,” is Greek eis gēn pros liba, “to the land toward the south”; Hebrew va-yagor, “he sojourned,” is Greek parōkēsen. Latin “the southern land … staying as a stranger” and King James “the south country … sojourned” agree in sense.")]},

 '20:2': {
  'received': "Abraham called Sarah his sister, and Abimelech king of Gerar took her.",
  'explain': ("The old lie returns, this time with Sarah ninety and promised a son within the year. The Hebrew tells it in two bare clauses: he said she "
   "is my sister; Abimelech took her. The Greek inserts the narrator’s explanation that Abraham feared the men of the city would kill him for her; "
   "the Hebrew keeps that explanation for Abraham’s own mouth in verse 11. The king of Gerar sends for her as Pharaoh did."),
  'shared': ["Abraham said of Sarah that she was his sister.", "Abimelech was king of Gerar.", "Abimelech sent and took Sarah."],
  'instructions': [ins(K, S, "Abraham again passed Sarah off as his sister, and the king of Gerar took her."), ins(W, R, "The lie that failed in Egypt is tried again on the eve of Isaac’s conception; fear outlives both rebuke and promise.")],
  'entries': ['abraham', 'sarah'],
  'lost': [
   keeps("Greek adds ephobēthē gar eipein hoti Gynē mou estin, mēpote apokteinōsin auton hoi andres tēs poleōs di’ autēn, “for he was afraid to say, She is my wife, lest the men of the city kill him because of her,” a narrator’s explanation the Hebrew leaves for 20:11."),
   between("Latin and King James have the two bare clauses with the Hebrew; the Latin says “took her” for “took Sarah.”"),
  ]},

 '20:3': {
  'received': "God came to Abimelech in a dream and warned that he was a dead man for taking a married woman.",
  'explain': ("God intervenes directly, speaking to a pagan king in a dream, as he will to Laban and to Pharaoh’s officials. The Hebrew says a dream and "
   "“she is married to a husband,” an idiom for a wife under a husband’s authority; the Greek says in sleep at night and “she has lived with a husband.” "
   "The sentence is death, before any act."),
  'shared': ["God came to Abimelech at night.", "He told him he would die because of the woman he had taken.", "The reason is that she is a married woman."],
  'instructions': [ins(K, S, "God warned Abimelech in a dream that Sarah was another man’s wife."), ins(W, R, "God protects the promise by speaking to the outsider; Abimelech is told what Abraham should have told him.")],
  'entries': ['sarah', 'god-theos'],
  'lost': [between("Hebrew ba-chalom, “in a dream,” is Greek en hypnō, “in sleep”; Hebrew be‘ulat ba‘al, “married to a husband,” is Greek synōkēkuia andri, “has lived with a husband.” Hebrew hinnekha met, “you are a dead man,” is Greek sy apothnēskeis, “you are dying.” Latin “in a dream … she has a husband” and King James “in a dream … a man’s wife” follow the Hebrew.")]},

 '20:4': {
  'received': "Abimelech, who had not touched her, asked whether the Lord would destroy a righteous nation.",
  'explain': ("The narrator clears Abimelech, and Abimelech pleads. He has not approached her; will God kill a righteous nation? The Greek and Latin add "
   "“ignorant,” unknowing, to the nation’s plea, and the Greek says touched for approached. Abimelech speaks like Abraham in chapter 18, appealing "
   "to God’s justice, and his people stand or fall with him."),
  'shared': ["Abimelech had not approached Sarah.", "He addressed God as Lord.", "He asked whether God would kill a righteous nation."],
  'instructions': [ins(K, S, "Abimelech protested his innocence and his people’s to God."), ins(W, R, "The pagan king argues as Abraham did for Sodom; the appeal to a just God is not the property of the covenant.")],
  'entries': ['lord-translation'],
  'lost': [
   keeps("Greek adds agnooun, “ignorant,” to the nation, ethnos agnooun kai dikaion, “an ignorant and righteous nation,” and says ouch hēpsato, “had not touched,” for Hebrew lo qarav, “had not approached.”"),
   between("Latin “an unknowing and righteous nation” follows the Greek addition; King James “a righteous nation” follows the Hebrew. Hebrew ha-goy gam-tsaddiq, “even a righteous nation,” has gam, “even,” which King James keeps as “also.”"),
  ]},

 '20:5': {
  'received': "Abimelech pleaded that both Abraham and Sarah had called each other brother and sister, and that he had acted in integrity.",
  'explain': ("Abimelech’s defence is complete: both of them said it, and he acted with a clean heart and clean hands. The Hebrew says integrity of heart "
   "and innocence of hands; the Greek pure heart and righteous hands; the Latin innocence and cleanness. The Hebrew stresses “she herself” said it; "
   "the Greek says plainly she told me. Sarah’s complicity is recorded."),
  'shared': ["Abraham told Abimelech she was his sister.", "Sarah herself said he was her brother.", "Abimelech acted with integrity of heart and innocence of hands."],
  'instructions': [ins(K, S, "Abimelech acted in good faith on what Abraham and Sarah both told him."), ins(W, R, "Sarah’s word is quoted beside Abraham’s; the deception was a shared act, and the king was its victim.")],
  'entries': ['abraham', 'sarah'],
  'lost': [between("Hebrew be-tom levavi u-ve-niqyon kappai, “in integrity of my heart and innocence of my hands,” is Greek en kathara kardia kai en dikaiosynē cheirōn, “with a pure heart and righteousness of hands”; Hebrew ve-hi gam-hi amerah, “and she herself said,” is Greek kai autē moi eipen, “and she told me.” Latin “innocence of heart and cleanness of hands” and King James “integrity … innocency” follow the Hebrew sense.")]},

 '20:6': {
  'received': "God acknowledged Abimelech’s integrity and said he had kept him from sinning by not letting him touch her.",
  'explain': ("God agrees: I too knew. Then he claims the restraint as his own work. The Hebrew says I myself kept you from sinning against me; the "
   "Greek I spared you so that you would not sin; the Latin I kept you from sinning. In all, God did not allow him to touch her. The Greek adds "
   "“in sleep” and reorders cause and result."),
  'shared': ["God spoke to Abimelech in the dream.", "He knew Abimelech acted with integrity.", "God kept him from sinning and did not let him touch Sarah."],
  'instructions': [ins(K, S, "God himself had prevented Abimelech from sinning with Sarah."), ins(W, R, "Innocence here is God’s gift as much as the king’s virtue; the sin not committed was prevented, not merely avoided.")],
  'entries': ['sarah', 'god-theos'],
  'lost': [
   loses("Hebrew va-echsokh gam-anokhi otekha me-chato-li, “and I myself kept you from sinning against me,” becomes Greek kai ephisamēn egō sou tou mē hamartein se eis eme, “and I spared you so that you would not sin against me”; restraint becomes sparing. Hebrew ba-chalom, “in the dream,” is Greek kath’ hypnon, “in sleep.” Hebrew be-tom-levavekha is Greek en kathara kardia."),
   between("Latin “God said to him … therefore I kept you from sinning” drops the dream and keeps the restraint; King James “in a dream … I also withheld thee” follows the Hebrew."),
  ]},

 '20:7': {
  'received': "God commanded Abimelech to return Abraham’s wife, since he was a prophet who would pray for him; otherwise he and all his would die.",
  'explain': ("Abraham is called a prophet, the first use of the word in Scripture, and the deceived king is told that the deceiver will pray for him. "
   "The command is to restore the wife; the alternative is death for the king and all his house. The Hebrew intensifies, you shall surely die; the "
   "Greek you will die. The versions agree."),
  'shared': ["Abimelech is to return the man’s wife.", "Abraham is a prophet who will pray for him so that he lives.", "If he does not return her, he and all his will die."],
  'instructions': [ins(C, S, "Return the man’s wife."), ins(K, S, "Abraham was named a prophet whose prayer would heal Abimelech."), ins(W, R, "The one who sinned against the king is the one appointed to pray for him; God’s choice of intercessor is not a judgement on his conduct.")],
  'entries': ['abraham', 'sarah'],
  'lost': [between("Hebrew mot tamut, “you shall surely die,” is Greek apothanē, “you will die,” without the doubling; Hebrew eshet-ha-ish, “the man’s wife,” is Greek tēn gynaika tō anthrōpō, “the wife to the man.” Latin “shall surely die” and King James “thou shalt surely die” keep the emphasis. Hebrew navi and Greek prophētēs are both “prophet.”")]},

 '20:8': {
  'received': "Abimelech rose early, told his servants everything, and they were very afraid.",
  'explain': ("The king acts at once: he gathers his court and tells them the dream, and fear spreads. The Hebrew and Greek have him rise early in the "
   "morning; the Latin immediately in the night. The Greek says all the men were afraid; the Hebrew the men. A pagan court fears the God of Abraham "
   "before Abraham has said a word."),
  'shared': ["Abimelech rose early.", "He called all his servants and told them everything.", "The men were very afraid."],
  'instructions': [ins(K, S, "Abimelech’s court heard the warning and feared."), ins(W, R, "Fear of God is found in Gerar, where Abraham assumed there was none; the king’s household proves his assumption wrong.")],
  'entries': [],
  'lost': [between("Hebrew ba-boqer, “in the morning,” is Greek to prōi; the Latin has “immediately in the night.” Greek adds pantes, “all,” to the men who feared; Hebrew ha-anashim, “the men.” King James “early in the morning … the men were sore afraid” follows the Hebrew.")]},

 '20:9': {
  'received': "Abimelech summoned Abraham and rebuked him for bringing great sin on him and his kingdom by a deed that ought not be done.",
  'explain': ("The king turns on the prophet with the question God asked Eve and Pharaoh asked Abraham: what have you done? The Hebrew has Abimelech ask "
   "how he personally sinned against Abraham; the Greek and Latin how we sinned, the people with him. The Hebrew ends with a general rule, things that "
   "ought not be done; the Greek with a deed no one would do. Abraham makes no defence until asked twice."),
  'shared': ["Abimelech called Abraham and asked what he had done.", "He asked how he had sinned against Abraham to deserve such sin on his kingdom.", "Abraham had done to him what ought not be done."],
  'instructions': [ins(K, S, "Abimelech justly rebuked Abraham for endangering his kingdom."), ins(W, R, "The pagan king names the wrong the patriarch would not; once again the outsider is the moral teacher in the scene.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew u-meh-chatati lakh, “and how have I sinned against you,” singular, becomes Greek mē ti hēmartomen eis se, “have we sinned against you,” plural; Hebrew ma‘asim asher lo-ye‘asu, “deeds that are not done,” a general prohibition, becomes Greek ergon ho oudeis poiēsei, “a deed that no one would do.”"),
   between("Latin “how have we sinned … things you ought not to have done” shares the Greek plural and the Hebrew rule; King James “what have I offended thee … deeds … that ought not to be done” follows the Hebrew. Genesis 3:13 and 12:18 are the earlier question."),
  ]},

 '20:10': {
  'received': "Abimelech asked Abraham what he had seen that made him do this.",
  'explain': ("A second question, more searching: what did you see? What was it about us that made you think this necessary? The versions agree; the "
   "Latin says he demanded again. Abraham’s answer will reveal his assumption about Gerar."),
  'shared': ["Abimelech spoke to Abraham again.", "He asked what Abraham had seen.", "He asked what led him to do this."],
  'instructions': [ins(K, S, "Abimelech pressed Abraham for his reasons."), ins(W, R, "“What did you see?” asks the deceiver to name his fear; the question is an invitation to honesty after a lie.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew mah ra’ita, “what did you see,” is Greek ti enidōn, “what seeing”; Latin “again he demanded” drops the names; King James follows the Hebrew.")]},

 '20:11': {
  'received': "Abraham explained that he thought there was no fear of God in the place and that he would be killed for his wife.",
  'explain': ("Abraham gives the motive the Greek narrator already supplied in verse 2: he assumed the place had no fear of God and that he would be "
   "killed. The Hebrew says fear of God; the Greek reverence for God, a word for piety or worship. The Latin softens “surely” to “perhaps.” The "
   "assumption is Abraham’s, and the chapter has already shown it wrong."),
  'shared': ["Abraham answered.", "He thought there was no fear of God in the place.", "He feared they would kill him because of his wife."],
  'instructions': [ins(K, S, "Abraham acted from fear and a low estimate of Gerar’s piety."), ins(W, R, "Abraham judged the city by his fear and was wrong; the godless place he imagined had a king who feared God more than he did that day.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew yir’at Elohim, “fear of God,” is Greek theosebeia, “reverence for God”; Hebrew raq, “surely,” is Greek ara, “surely,” but Latin forsitan, “perhaps.” King James “surely the fear of God is not in this place” follows the Hebrew.")]},

 '20:12': {
  'received': "Abraham added that Sarah really was his half-sister, his father’s daughter, who became his wife.",
  'explain': ("The half-truth is explained: Sarah is his father’s daughter by another mother, a marriage the later law will forbid. So the lie was "
   "built on a fact. The versions agree; the Latin says I took her as my wife. The explanation excuses the words and not the deception."),
  'shared': ["Sarah truly is Abraham’s sister.", "She is his father’s daughter but not his mother’s.", "She became his wife."],
  'instructions': [ins(K, S, "Sarah was Abraham’s half-sister as well as his wife."), ins(W, R, "A true word used to mislead is still a lie; Abraham’s defence proves the fact and not the honesty.")],
  'entries': ['abraham', 'sarah'],
  'lost': [between("Hebrew ve-gam omnah, “and besides, truly,” is Greek kai gar alēthōs, “for truly”; Hebrew va-tehi-li le-ishah, “she became my wife,” is Greek egenēthē moi eis gynaika; Latin “I took her as my wife.” King James follows the Hebrew. Leviticus 18:9 later forbids the union.")]},

 '20:13': {
  'received': "Abraham said that when God brought him from his father’s house he asked Sarah to call him brother wherever they went.",
  'explain': ("The deception was a standing arrangement from the beginning of the journey. The Hebrew says God caused me to wander from my father’s "
   "house and calls Sarah’s part a kindness, chesed; the Greek says God brought me out and calls it a righteousness, the same substitution as in 19:19. "
   "The Hebrew unusually pairs God with a plural verb here; God is the rendering, with the grammar noted."),
  'shared': ["God brought Abraham out of his father’s house.", "Abraham asked Sarah to show him this kindness.", "Wherever they went she was to say he was her brother."],
  'instructions': [ins(K, S, "Abraham and Sarah had agreed from the start to call each other brother and sister."), ins(W, R, "A policy of deception adopted at the call itself; the father of faith left Haran with a lie already packed.")],
  'entries': ['abraham', 'sarah', 'haran'],
  'lost': [
   loses("Hebrew hit‘u oti Elohim, “God caused me to wander,” with a plural verb, becomes Greek exēgagen me ho theos, “God brought me out,” singular; Hebrew chasdekh, “your kindness,” becomes Greek tēn dikaiosynēn, “the righteousness,” as in 19:19."),
   between("Latin “when God led me out … show me this kindness” and King James “when God caused me to wander … this thy kindness” keep kindness; the Latin shares the Greek verb of leading."),
  ]},

 '20:14': {
  'received': "Abimelech gave Abraham flocks, herds and servants, and restored Sarah to him.",
  'explain': ("The king makes restitution to the man who wronged him, as Pharaoh enriched Abram. Flocks, herds, male and female slaves, and Sarah herself. "
   "The Greek adds a thousand didrachms here, the silver the Hebrew first mentions in verse 16, and has calves for oxen. The gifts are the Hebrew "
   "custom of settling a wrong with goods."),
  'shared': ["Abimelech took livestock and servants.", "He gave them to Abraham.", "He returned his wife Sarah to him."],
  'instructions': [ins(K, S, "Abimelech restored Sarah to Abraham with gifts."), ins(W, R, "The wronged king pays the one who wronged him; Abraham is enriched by his lie a second time, and the text lets the irony stand.")],
  'entries': ['abraham', 'sarah'],
  'lost': [
   keeps("Greek adds chilia didrachma, “a thousand didrachms,” at the head of the gifts, anticipating the silver of 20:16; Hebrew tson u-vaqar, “flocks and cattle,” is Greek probata kai moschous, “sheep and calves.”"),
   between("Latin “sheep, oxen, male servants, and maidservants” and King James “sheep, and oxen, and menservants, and womenservants” follow the Hebrew without the money."),
  ]},

 '20:15': {
  'received': "Abimelech offered Abraham his whole land to settle wherever he pleased.",
  'explain': ("The king’s generosity goes beyond restitution: the land is open to Abraham. The Greek names the addressee; the Hebrew says Abimelech said; "
   "the Latin says the land. The man who feared for his life in Gerar is given the run of it."),
  'shared': ["Abimelech spoke.", "His land is before Abraham.", "Abraham may settle wherever he pleases."],
  'instructions': [ins(K, S, "Abimelech gave Abraham freedom to live anywhere in his land."), ins(W, R, "Fear expected death and received a home; Abraham’s dread of the place is answered by its king’s welcome.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew hinneh artsi lefanekha, “behold, my land is before you,” is Greek idou hē gē mou enantion sou; the Greek adds “to Abraham”; the Latin says “the land” without “my.” King James follows the Hebrew.")]},

 '20:16': {
  'received': "To Sarah Abimelech said he had given her brother a thousand pieces of silver as a covering for her before all, and the matter was settled.",
  'explain': ("The hardest verse of the chapter. The Hebrew says the silver is a covering of the eyes for Sarah before all who are with her, and ends "
   "with a clause read as “you are vindicated” or “you have been reproved”; the Latin reads it as “remember you were found out.” The Greek gives "
   "a different resolution: the money is for the honour of your face and for all the women with you, and Sarah is told to speak the truth in everything. "
   "Abimelech’s irony, “your brother,” is in all."),
  'shared': ["Abimelech spoke to Sarah.", "He had given her “brother” a thousand pieces of silver.", "The gift concerns her standing before all who are with her."],
  'instructions': [ins(K, S, "Abimelech compensated Sarah publicly and closed the matter."), ins(W, R, "“Your brother” is the king’s rebuke; the money covers Sarah’s honour and uncovers Abraham’s pretence.")],
  'entries': ['sarah'],
  'lost': [
   loses("Hebrew kesut einayim, “a covering of the eyes,” an idiom for compensation that closes a matter, becomes Greek eis timēn tou prosōpou sou, “for the honour of your face”; Hebrew ve-et kol ve-nokhachat, “and before everyone you are vindicated” (or reproved), becomes Greek kai panta alētheuson, “and speak the truth in everything,” an imperative. Hebrew elef kesef, “a thousand of silver,” is Greek chilia didrachma; Hebrew “all who are with you” is Greek “all the women with you.”"),
   between("Latin “a covering for your eyes … remember that you have been found out” and King James “a covering of the eyes … thus she was reproved” read the last Hebrew clause as rebuke; the Hebrew column reads vindication. The uncertainty of the Hebrew is real."),
  ]},

 '20:17': {
  'received': "Abraham prayed, and God healed Abimelech and his household so that they bore children again.",
  'explain': ("The prophet does what God said he would: he prays, and the king’s house is healed. The healing is of fertility, as the next verse explains. "
   "The man who feared Gerar would kill him becomes its healer. The versions agree; the Latin drops “to God.”"),
  'shared': ["Abraham prayed to God.", "God healed Abimelech, his wife and his slave women.", "They bore children."],
  'instructions': [ins(K, S, "Abraham’s prayer healed Abimelech’s household."), ins(W, R, "The intercessor is the one who caused the trouble; God uses Abraham’s prayer without first making Abraham worthy of it.")],
  'entries': ['abraham', 'god-theos'],
  'lost': [between("Hebrew, Greek and King James agree; Latin “Abraham prayed” omits “to God.” Hebrew amhotav, “his slave women,” is Greek paidiskai, the word of 12:16 and 16:1.")]},

 '20:18': {
  'received': "The Lord had closed every womb in Abimelech’s house because of Sarah.",
  'explain': ("The narrator explains the healing: the Lord had shut every womb in the house because of Sarah, so that no child could be conceived while "
   "she was there and no doubt cast on Isaac’s paternity. The Hebrew says YHWH had completely closed; the Greek the Lord had completely closed from "
   "outside, adding a phrase; the Latin simply closed. No medical mechanism is given."),
  'shared': ["The Lord had closed every womb in Abimelech’s household.", "He had done so completely.", "It was because of Sarah, Abraham’s wife."],
  'instructions': [ins(K, S, "God had made Abimelech’s house barren while Sarah was in it."), ins(W, R, "The barrenness of Gerar guards the son of the promise; God closes other wombs so that no one can doubt whose child Isaac is.")],
  'entries': ['sarah', 'yhwh-yahweh'],
  'lost': [between("Hebrew atsor atsar YHWH, “YHWH had completely closed,” is Greek synekleise kyrios exōthen, “the Lord had completely closed from outside,” with exōthen added; Latin “closed” drops the intensifier; King James “fast closed up” keeps it. Hebrew kol-rechem, “every womb,” is Greek pasan mētran.")]},
 }
}
