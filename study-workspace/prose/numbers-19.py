K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
WATER = [loses("Hebrew 'water for impurity' (mei niddah) is lost."), keeps("Greek 'water of sprinkling'."), between("The Latin has 'water of sprinkling'; the King James 'water of separation'.")]
HOUSE = [loses("Hebrew 'tent' is lost."), keeps("Greek 'house'."), between("The Latin and King James have 'tent'.")]
CUTOFF = [loses("Hebrew 'cut off' is lost."), keeps("Greek 'wiped out' or 'destroyed'."), between("The Latin and King James have 'cut off' or 'perish'.")]
COW = [keeps("Greek 'heifer' (damalis)."), between("The Hebrew has 'cow'; the Latin and King James 'heifer'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 19,
 'chapterNote': "The red cow and the water for impurity. A red, unblemished, never-yoked cow is given to Eleazar, slaughtered outside the camp before him, its blood sprinkled seven times toward the tent, and burned whole with cedar, hyssop and scarlet; priest, burner and ash-gatherer are unclean till evening; the ashes are kept in a clean place for water for impurity. Whoever touches a corpse is unclean seven days and is sprinkled with the ash-water on the third and seventh; one who refuses is cut off for defiling YHWH's Dwelling. A death in a tent defiles all who enter and every open vessel; in the field, the slain, a corpse, a bone or a grave defile; the sprinkler washes, the toucher of the water is unclean till evening, and whatever the unclean touches is unclean. The Greek adds 'a clean place' at the slaughter (19:3), omits the finger (19:4), has plural 'they' throwing the wood (19:6), omits 'water' twice (19:8), 'water of sprinkling … a means of purification' for 'water for impurity … a purification offering' (19:9), attaches both days to purification (19:12), 'wiped out … Tent' for 'cut off … Dwelling' (19:13), 'house' for 'tent' (19:14, 18), omits 'by a sword' (19:16), 'pour living water' (19:17), adds the touchers to the sprinkling (19:18), 'destroyed … holy things' (19:20), and 'for you' for 'for them' (19:21).",
 'verses': {
  '19:1': v("YHWH speaks to Moses and Aaron.", "All four columns agree.", ["YHWH speaks.", "To Moses and Aaron.", "On the red cow."],
   "YHWH spoke on corpse impurity.", "After 14,700 dead in the camp, a law for the living who touched them.", [AGREE], ['yhwh-yahweh', 'moses', 'high-priest']),
  '19:2': v("This is the statute of the instruction YHWH commanded: tell Israel to bring you a red cow, sound and without defect, never yoked.", "All four columns agree; 'heifer' outside the Hebrew; the Latin 'of full age'.",
   ["The statute of the law.", "A red cow.", "Unblemished, never yoked."], "A red cow was required.", "'The statute of the law', the rabbis' name for the rule with no reason given; a red cow, perfect and unworked, for the uncleanness that has no cure but this.",
   COW + [between("The Latin adds 'of full age'.")], [], "Let them bring you a red cow without defect."),
  '19:3': v("Give it to Eleazar the priest; it is taken outside the camp and slaughtered before him.", "The Greek adds 'unto a clean place'.",
   ["To Eleazar.", "Outside the camp.", "Slaughtered before him."], "Eleazar oversaw the slaughter.", "Not on the altar but outside the camp, and not by the high priest but his son: the one sacrifice killed away from the sanctuary, for a defilement that comes from outside it.",
   [keeps("Greek 'they shall bring it outside the camp unto a clean place'."), between("The Latin has 'in everyone's sight'.")], ['high-priest']),
  '19:4': v("Eleazar takes some blood with his finger and sprinkles it seven times toward the front of the Tent of Meeting.", "The Greek omits the finger and the priestly title.",
   ["Eleazar takes blood.", "Sprinkles seven times.", "Toward the tent."], "The blood pointed at the tent.", "Blood flicked toward the tent from outside the camp: the rite stands at a distance and aims at the holy place it may not enter.",
   TENT + [loses("Hebrew 'with his finger … the priest' is lost."), keeps("Greek has Eleazar sprinkle without the finger.")], ['high-priest', 'tabernacle']),
  '19:5': v("The cow is burned before his eyes: skin, flesh, blood and dung.", "All four columns agree.",
   ["Burned before him.", "Skin, flesh, blood.", "And dung."], "The whole cow was burned.", "Everything, even the blood, even the dung: nothing of the cow goes to anyone; it is turned entirely to ash for the water.", COW, []),
  '19:6': v("The priest takes cedar, hyssop and scarlet and throws them into the burning cow.", "The Hebrew singular priest; the Greek plural 'they shall throw'.",
   ["Cedar wood.", "Hyssop and scarlet.", "Into the fire."], "Three materials joined the fire.", "Cedar, hyssop and scarlet, the leper's cleansing kit of Leviticus 14; the ashes will carry the materials of healing.",
   [keeps("Greek 'they shall throw them'."), between("The Latin and King James have the priest throw them.")], ['high-priest']),
  '19:7': v("The priest washes his clothes and bathes; afterward he may enter the camp, but is unclean until evening.", "All four columns agree.",
   ["The priest washes.", "Enters the camp.", "Unclean till evening."], "The rite defiled the priest.", "The purifying rite makes its priest unclean: the paradox the rabbis prized, that the cow cleanses the defiled and defiles the clean.", [AGREE], ['high-priest']),
  '19:8': v("The one who burns it washes his clothes in water and bathes his body in water; unclean until evening.", "The Greek omits 'in water' twice.",
   ["The burner washes.", "Bathes.", "Unclean till evening."], "The burner too was defiled.", "Everyone who touches the cow's making is marked by it till sundown.", [loses("Hebrew 'in water … in water' is lost."), keeps("Greek has washing and bathing without naming water.")]),
  '19:9': v("A clean man gathers the cow's ashes and deposits them outside the camp in a clean place; kept for the congregation for water for impurity; it is a purification offering.", "The Hebrew 'water for impurity … purification offering (chatta't)'; the Greek 'water of sprinkling … a means of purification'.",
   ["A clean man gathers the ashes.", "Kept outside the camp.", "For water for impurity."], "The ashes were stored.", "A heap of ashes outside the camp, Israel's cure for death kept where the dead are; the Hebrew calls it a sin offering, the one sin offering that is a powder.",
   WATER + [loses("Hebrew 'it is a purification offering' is lost."), keeps("Greek 'it is a means of purification' (hagnisma).")]),
  '19:10': v("The gatherer washes his clothes and is unclean until evening; a perpetual statute for Israel and the resident alien.", "All four columns agree; 'sojourners' in Greek.",
   ["The gatherer washes.", "Unclean till evening.", "A perpetual statute for all."], "The law bound aliens too.", "Alien and native share death and its cure; the one law of chapter 15 holds at the graveside.",
   [keeps("Greek 'the attached sojourners'."), between("The Latin and King James have 'stranger'.")]),
  '19:11': v("Whoever touches a dead person, any human corpse, is unclean seven days.", "All four columns agree.",
   ["Touching a corpse.", "Any human.", "Unclean seven days."], "Corpse contact meant a week's uncleanness.", "Seven days for a touch: death is the strongest uncleanness in the law, and the only one that needs the cow.", [AGREE], [], "Whoever touches a dead person shall be unclean seven days."),
  '19:12': v("He purifies himself with it on the third day and on the seventh day is clean; if he does not purify himself on the third, he is not clean on the seventh.", "The Hebrew's clause division has the seventh as the result; the Greek attaches both days to purification; 19:19 settles it.",
   ["Purified on the third.", "Clean on the seventh.", "Else not clean."], "Purification took two sprinklings.", "Third and seventh: two sprinklings a week apart, and skipping the first voids the second. The cure has a calendar.",
   [keeps("Greek 'purified on the third day and on the seventh day … if he is not purified on the third day and on the seventh day'.")]),
  '19:13': v("Whoever touches a corpse and does not purify himself defiles YHWH's Dwelling; he is cut off from Israel; because water for impurity was not dashed on him, his uncleanness remains.", "The Greek 'Tent … wiped out … water of sprinkling'.",
   ["Not purified.", "Defiles the Dwelling.", "Cut off."], "Refusing the water was a capital matter.", "Not the touch but the refusal: the man who stays unclean defiles the Dwelling from wherever he stands, and is cut off for it.",
   WATER + CUTOFF + [loses("Hebrew 'YHWH's Dwelling' is lost."), keeps("Greek 'the Tent of the Lord'.")], ['tabernacle', 'yhwh-yahweh']),
  '19:14': v("This is the instruction: when a person dies in a tent, everyone who enters and everything in it is unclean seven days.", "The Hebrew 'tent'; the Greek 'house'.",
   ["A death in a tent.", "All who enter.", "Everything in it."], "A death defiled the whole tent.", "The tent itself becomes unclean, and every pot in it; death spreads through a dwelling like smoke. The Greek wrote 'house' for readers who had houses.",
   HOUSE),
  '19:15': v("Every open vessel without a tied covering is unclean.", "All four columns agree.",
   ["Every open vessel.", "No tied covering.", "Unclean."], "Open vessels caught the uncleanness.", "A lidded jar is safe, an open one is not; death enters where air does.", [AGREE]),
  '19:16': v("Anyone who touches in the open field one killed by a sword, a corpse, a human bone or a grave is unclean seven days.", "The Hebrew 'by a sword'; the Greek omits the weapon.",
   ["In the open field.", "The slain, a corpse, a bone, a grave.", "Unclean seven days."], "Field contact defiled too.", "A bone in a field, a grave stepped on: death reaches from the ground; Jesus will call the Pharisees unmarked graves because of this verse.",
   [loses("Hebrew 'killed by a sword' is lost."), keeps("Greek 'one slain' (traumatias) without the weapon.")]),
  '19:17': v("For the unclean they take ashes from the burned purification offering, and fresh water is put over them in a vessel.", "The Greek 'pour living water'.",
   ["Ashes.", "Fresh water.", "In a vessel."], "Ash and water were mixed.", "'Living water' over dead ash: running water poured on what fire left, the two cleansers of the law in one bowl.",
   [keeps("Greek 'they shall pour living water over them'."), between("The Latin has 'fresh water'; the King James 'running water'.")]),
  '19:18': v("A clean man takes hyssop, dips it, and sprinkles the tent, all the vessels and the people there, and whoever touched the bone, the slain, the corpse or the grave.", "The Greek 'house … human bone' and adds the touchers.",
   ["Hyssop dipped.", "Sprinkled on tent and vessels.", "And on the touchers."], "Hyssop applied the water.", "Hyssop, the Passover brush: the plant that marked the doors in Egypt sprinkles the tent of the dead. 'Purge me with hyssop', David will pray.",
   HOUSE + [keeps("Greek 'the human bone … on whoever touched'.")]),
  '19:19': v("The clean person sprinkles the unclean on the third and seventh days, purifies him on the seventh; he washes his clothes, bathes, and is clean at evening.", "All four columns agree; 'unclean until evening' in Greek.",
   ["Third and seventh days.", "Wash and bathe.", "Clean at evening."], "The week ended in cleanness.", "The seventh day, a wash, and sundown: a man who touched death is given back to the camp.",
   [keeps("Greek 'he shall be unclean until evening'."), between("The Latin and King James have 'clean at even'.")]),
  '19:20': v("A person who becomes unclean and does not purify himself is cut off from the assembly, for he defiled YHWH's sanctuary; water for impurity was not dashed on him; he is unclean.", "The Greek 'destroyed … holy things'.",
   ["Not purified.", "Cut off.", "Defiled the sanctuary."], "Refusal was repeated as capital.", "Said twice in the chapter: the water is not optional. To stay unclean is to carry death into God's camp.",
   WATER + CUTOFF + [loses("Hebrew 'YHWH's sanctuary' is lost."), keeps("Greek 'the holy things of the Lord'.")], ['tabernacle']),
  '19:21': v("A perpetual statute for them: the sprinkler washes his clothes, and whoever touches the water for impurity is unclean until evening.", "The Hebrew 'for them'; the Greek 'for you'.",
   ["A perpetual statute.", "The sprinkler washes.", "Touching the water defiles."], "Even the water defiled.", "The water that cleanses the unclean makes the clean unclean: the paradox again, and the law states it without explaining it.",
   WATER + [loses("Hebrew 'for them' is lost."), keeps("Greek 'for you'.")]),
  '19:22': v("Whatever the unclean person touches is unclean, and whoever touches it is unclean until evening.", "All four columns agree.",
   ["What the unclean touches.", "Is unclean.", "And the toucher till evening."], "Uncleanness spread by contact.", "Death is contagious at one remove; the chapter ends with the chain of touch, which only the ash-water breaks.", [AGREE]),
 },
}
