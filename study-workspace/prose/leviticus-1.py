K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
PLURAL = [loses("Hebrew's singular agent, the offerer, is lost."), keeps("Greek plural 'they shall', the preparation described as shared work."), between("The Latin and King James keep the singular with the Hebrew; the Latin's 'pouring' matches the Greek against the Hebrew 'dash'.")]
BURN = [loses("Hebrew 'burn' (make smoke) is lost as the explicit verb."), keeps("Greek 'place upon the altar', the fire of verses 7–8 supplying the burning."), between("The Latin and King James have 'burn' with the Hebrew.")]

CHAPTER = {
 'slug': 'leviticus', 'chapter': 1,
 'chapterNote': "YHWH calls to Moses from the Tent of Meeting and gives the law of the burnt offering: an unblemished male from the herd, slaughtered at the tent's entrance, its blood dashed around the altar, the animal skinned and cut up, its entrails and legs washed, all of it burned as a pleasing aroma; the same from the flock, slaughtered on the altar's north side; and the bird offering of turtledove or pigeon, head pinched off, blood drained at the altar's side, crop thrown to the ash place, the bird torn open by its wings and burned whole. The Greek throughout has 'Tent of Testimony' for Tent of Meeting, 'gift' for offering, 'whole burnt offering', plural agents where the Hebrew has the single offerer slaughter, skin, cut and wash (1:5, 6, 9, 11, 12, 13), and 'place' where the Hebrew has 'burn' (1:9, 13, 15, 17), the altar's fire of 1:7–8 making the burning plain in both. The Greek adds hand-laying to the flock rule (1:10) and drains the bird's blood at the altar's base rather than its side (1:15), the one material ritual difference the source marks. The Latin follows the Hebrew's singular and 'burn' while sharing the Greek's 'pour'.",
 'verses': {
  '1:1': {
   'received': "YHWH calls to Moses and speaks to him from the Tent of Meeting.",
   'explain': "All four columns agree in the call and the speaking; the Greek 'He called … and the Lord spoke' and 'Tent of Testimony'; the Latin and King James name the Lord as caller.",
   'shared': ["YHWH calls to Moses.", "He speaks to him.", "From the tent."],
   'instructions': [ins(K, S, "YHWH spoke to Moses from the Tent of Meeting."), ins(W, R, "Exodus ended with Moses unable to enter the glory-filled tent; Leviticus begins with God calling to him from inside it. The voice comes out to the man who could not go in.")],
   'entries': ['yhwh-yahweh', 'moses', 'tabernacle'],
   'lost': [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony' and the unnamed caller, 'He called unto Moses, and the Lord spoke'."), between("The Latin has 'The Lord called Moses … from the tabernacle of the testimony'; the King James 'the tabernacle of the congregation'.")],
  },
  '1:2': {
   'received': "Moses is to tell Israel: when anyone brings an offering to YHWH, it is from the livestock, herd or flock.",
   'explain': "All four columns agree; the Greek 'gifts' plural for the Hebrew 'offering' (qorban); the Latin 'sacrificial offering … victims'.",
   'shared': ["Speak to the sons of Israel.", "An offering to YHWH.", "From the herd or the flock."],
   'instructions': [ins(K, S, "Offerings to YHWH came from the herd or the flock."), ins(C, S, "When anyone among you brings an offering to YHWH, you shall bring it from the livestock."), ins(W, R, "'When anyone brings': the book of sacrifice opens with a voluntary gift, not a demand; the first law assumes someone wants to give.")],
   'entries': ['yhwh-yahweh', 'altar'],
   'lost': [loses("Hebrew 'offering' (qorban) singular is lost."), keeps("Greek 'gifts' plural, 'If a man among you brings gifts unto the Lord'."), between("The Latin has 'a sacrificial offering … victims'; the King James 'an offering'.")],
  },
  '1:3': {
   'received': "If the offering is a burnt offering from the herd, he brings an unblemished male to the entrance of the Tent of Meeting, for acceptance before YHWH.",
   'explain': "All four columns have the unblemished male at the tent door; the Hebrew 'for acceptance' and Greek 'acceptable' concern the offering's acceptability, not the offerer's will; the King James 'of his own voluntary will'.",
   'shared': ["A burnt offering from the herd.", "An unblemished male.", "At the tent's entrance before YHWH."],
   'instructions': [ins(K, S, "The burnt offering from the herd was an unblemished male brought to the tent's door."), ins(C, S, "He shall bring an unblemished male to the entrance of the Tent of Meeting."), ins(W, R, "Unblemished: God is given the best animal, not the spare; the rule against defects is the first rule of worship.")],
   'entries': ['altar', 'tabernacle', 'yhwh-yahweh'],
   'lost': [loses("Hebrew 'for acceptance' (lirtsono) and 'Tent of Meeting' are lost."), keeps("Greek 'whole burnt offering', 'acceptable before the Lord', 'Tent of Testimony'."), between("The Latin has 'to obtain the Lord's favour'; the King James 'of his own voluntary will', reading the Hebrew as the offerer's will.")],
  },
  '1:4': {
   'received': "He lays his hand on the head of the burnt offering, and it is accepted for him to make atonement for him.",
   'explain': "All four columns agree; the Greek 'propitiation' (exilaskomai) for Hebrew atonement (kipper), a rendering choice the source says does not oppose the rites' purposes; the Latin 'expiation'.",
   'shared': ["Hand on the head.", "Accepted for him.", "To make atonement."],
   'instructions': [ins(K, S, "Laying a hand on the burnt offering made it accepted for atonement."), ins(C, S, "He shall lay his hand on the head of the burnt offering."), ins(W, R, "A hand on the head: the offerer touches what will die for him; the animal is not sent off but claimed, and the claim is the atonement.")],
   'entries': ['altar'],
   'lost': [loses("Hebrew 'burnt offering' and 'atonement' are lost in form."), keeps("Greek 'the offering' and 'propitiation'."), between("The Latin has 'the sacrificial animal' and 'expiation'; the King James 'atonement'.")],
  },
  '1:5': {
   'received': "He slaughters the young bull before YHWH, and Aaron's sons, the priests, present the blood and dash it all around against the altar at the entrance of the Tent of Meeting.",
   'explain': "The Hebrew, Latin and King James have the offerer slaughter; the Greek plural 'they shall slaughter the calf'. The Greek and Latin 'pour', the Hebrew 'dash'. The source notes the Greek does not call its plural slaughterers priests.",
   'shared': ["Slaughtered before YHWH.", "Aaron's sons present the blood.", "Blood around the altar at the tent door."],
   'instructions': [ins(K, S, "The offerer slaughtered the bull and the priests dashed its blood around the altar."), ins(W, R, "The layman kills and the priest handles the blood; the division of labour is drawn at the blood, which is the part that belongs to God.")],
   'entries': ['altar', 'high-priest', 'yhwh-yahweh'],
   'lost': PLURAL,
  },
  '1:6': {
   'received': "He skins the burnt offering and cuts it into pieces.",
   'explain': "The Hebrew and King James have the singular; the Greek and Latin plural, 'they'; the Greek 'limb by limb'.",
   'shared': ["The burnt offering skinned.", "Cut.", "Into its pieces."],
   'instructions': [ins(K, S, "The burnt offering was skinned and cut up."), ins(W, R, "The skin comes off before the fire; the hide is kept, the priest's portion, the one part of a whole offering that is not burned.")],
   'entries': ['altar'],
   'lost': [loses("Hebrew singular 'he shall skin' and 'into its pieces' are lost."), keeps("Greek 'when they have skinned … they shall divide it limb by limb'."), between("The Latin has plural 'they shall cut its limbs'; the King James 'he shall flay'.")],
  },
  '1:7': {
   'received': "The sons of Aaron the priest put fire on the altar and arrange wood on the fire.",
   'explain': "The Hebrew and King James have 'Aaron the priest' singular; the Greek 'the sons of Aaron, the priests'; the Latin 'they'.",
   'shared': ["Fire on the altar.", "Wood arranged.", "By Aaron's sons."],
   'instructions': [ins(K, S, "The priests laid fire and wood on the altar."), ins(W, R, "Fire first, then wood, then the pieces; the altar is built up in layers, and the order is given as a rule.")],
   'entries': ['altar', 'high-priest'],
   'lost': [loses("Hebrew 'the sons of Aaron the priest', Aaron named as priest, is lost."), keeps("Greek 'the sons of Aaron, the priests'."), between("The Latin has 'They shall put fire upon the altar'; the King James 'the sons of Aaron the priest'.")],
  },
  '1:8': {
   'received': "Aaron's sons, the priests, arrange the pieces, head and suet on the wood on the fire on the altar.",
   'explain': "All four columns agree; the Latin 'everything adhering to the liver' for the suet.",
   'shared': ["The pieces and the head.", "The suet.", "On the wood on the fire."],
   'instructions': [ins(K, S, "The priests arranged the pieces, head and fat on the altar fire."), ins(W, R, "The head and the fat named apart from the pieces; the animal is reassembled on the fire in a set order, as if being laid out rather than thrown on.")],
   'entries': ['altar', 'high-priest'],
   'lost': [keeps("Greek 'the divided parts, and the head, and the fat'."), between("The Latin has 'the head and everything adhering to the liver'; the King James 'the parts, the head, and the fat'.")],
  },
  '1:9': {
   'received': "He washes its entrails and legs with water, and the priest burns all of it on the altar: a burnt offering, an offering by fire, a pleasing aroma to YHWH.",
   'explain': "The Hebrew has the offerer wash and the priest burn; the Greek 'they shall wash' and 'the priests shall place all'. The source insists the Greek's fire of 1:7–8 makes the offering burned in both.",
   'shared': ["Entrails and legs washed.", "All of it on the altar.", "A pleasing aroma to YHWH."],
   'instructions': [ins(K, S, "The washed animal was wholly burned as a pleasing aroma to YHWH."), ins(W, R, "'A pleasing aroma': the first thing God is said to receive from the altar is a smell; the whole burnt offering gives him nothing to hold, only what rises.")],
   'entries': ['altar', 'term-savor', 'yhwh-yahweh'],
   'lost': BURN + [loses("Hebrew 'an offering by fire' is lost."), keeps("Greek 'It is an offering, a sacrifice, a sweet savour unto the Lord'.")],
  },
  '1:10': {
   'received': "If the offering is from the flock, sheep or goats, as a burnt offering, he brings an unblemished male.",
   'explain': "The Hebrew, Latin and King James have the animal rule only; the Greek adds 'and lay his hand upon its head', repeating 1:4's act for the flock. The source says not to insert the clause into the Hebrew.",
   'shared': ["From the flock.", "Sheep or goats.", "An unblemished male."],
   'instructions': [ins(K, S, "A burnt offering from the flock was likewise an unblemished male."), ins(C, S, "If his offering is from the flock, he shall bring an unblemished male."), ins(W, R, "Sheep and goats for those without cattle; the law scales the gift to the giver, and the smaller animal is accepted on the same terms.")],
   'entries': ['altar', 'lamb-of-god'],
   'lost': [keeps("Greek adds 'and lay his hand upon its head', and has 'lambs and young goats'."), between("The Latin and King James have no hand-laying clause here, with the Hebrew.")],
  },
  '1:11': {
   'received': "He slaughters it on the north side of the altar before YHWH, and Aaron's sons, the priests, dash its blood all around against the altar.",
   'explain': "The Hebrew and King James have the singular slaughterer and 'dash' or 'sprinkle'; the Greek plural 'they shall slaughter' and 'pour'; the Latin singular and 'pour'.",
   'shared': ["Slaughtered on the north side.", "Before YHWH.", "Blood around the altar."],
   'instructions': [ins(K, S, "The flock animal was killed on the altar's north side and its blood dashed around."), ins(W, R, "The north side: the only compass point in the chapter, a working detail that fixes where the knife is used in a crowded court.")],
   'entries': ['altar', 'high-priest', 'yhwh-yahweh'],
   'lost': PLURAL,
  },
  '1:12': {
   'received': "He cuts it into pieces with its head and suet, and the priest arranges them on the wood on the fire.",
   'explain': "The Hebrew and King James have singular offerer and priest; the Greek 'they shall divide … the priests shall pile'; the Latin plural dividers and 'everything adhering to the liver'.",
   'shared': ["Cut into pieces.", "Head and suet.", "Arranged on the altar wood."],
   'instructions': [ins(K, S, "The flock animal was cut up and laid on the fire like the bull."), ins(W, R, "The same steps for sheep as for bull; the smaller gift gets the full rite, not a shortened one.")],
   'entries': ['altar', 'high-priest'],
   'lost': [loses("Hebrew singular 'he shall cut' and 'the priest shall arrange' are lost."), keeps("Greek 'they shall divide it limb by limb … the priests shall pile them'."), between("The Latin has plural 'They shall divide the limbs' and 'everything adhering to the liver'; the King James keeps the singulars.")],
  },
  '1:13': {
   'received': "He washes the entrails and legs with water; the priest presents all of it and burns it on the altar, a burnt offering, an offering by fire, a pleasing aroma to YHWH.",
   'explain': "The Hebrew and King James have the offerer wash and the priest burn; the Greek and Latin 'they shall wash'; the Greek 'place it upon the altar'.",
   'shared': ["Entrails and legs washed.", "The priest presents all of it.", "A pleasing aroma to YHWH."],
   'instructions': [ins(K, S, "The whole flock animal was burned as a pleasing aroma."), ins(W, R, "'The priest shall present all of it': nothing of the burnt offering is kept for the table; it is the one sacrifice that feeds no one.")],
   'entries': ['altar', 'term-savor', 'yhwh-yahweh'],
   'lost': BURN + [loses("Hebrew singular 'he shall wash' is lost."), keeps("Greek 'they shall wash' and 'the priest shall bring all, and place it upon the altar'.")],
  },
  '1:14': {
   'received': "If the burnt offering to YHWH is of birds, he brings turtledoves or young pigeons.",
   'explain': "The Hebrew and King James have 'young pigeons' and the third person; the Greek 'if you bring an offering of birds as a gift' shifting to 'he', and 'pigeons' without 'young'.",
   'shared': ["A burnt offering of birds.", "Turtledoves.", "Pigeons."],
   'instructions': [ins(K, S, "The poorest burnt offering was a turtledove or young pigeon."), ins(C, S, "If his offering to YHWH is a burnt offering of birds, he shall bring turtledoves or young pigeons."), ins(W, R, "Birds for the poor; the law descends from bull to sheep to dove so that no one in Israel is too poor to give God a whole offering.")],
   'entries': ['altar', 'yhwh-yahweh'],
   'lost': [loses("Hebrew 'young pigeons' and the consistent third person are lost."), keeps("Greek 'if you bring an offering of birds as a gift … he shall bring his gift from the turtledoves or the pigeons'."), between("The Latin and King James have 'young pigeons'.")],
  },
  '1:15': {
   'received': "The priest brings it to the altar, pinches off its head, and burns it on the altar; its blood is drained out against the side of the altar.",
   'explain': "The Hebrew and King James drain the blood at the altar's side; the Greek 'at the base of the altar', which the source calls a material ritual difference, and 'place' for 'burn'; the Latin 'twist its head back at the neck, open the wound … upon the edge of the altar'.",
   'shared': ["The priest brings it to the altar.", "The head removed.", "The blood drained on the altar."],
   'instructions': [ins(K, S, "The priest pinched off the bird's head, burned it, and drained the blood at the altar's side."), ins(W, R, "A bird has too little blood to dash; it is drained against the stone, and the law gives even that trickle its place.")],
   'entries': ['altar', 'high-priest'],
   'lost': [loses("Hebrew 'burn it on the altar' and 'against the side of the altar' are lost."), keeps("Greek 'the priest shall place it upon the altar, and drain the blood at the base of the altar'."), between("The Latin has 'twist its head back at the neck, open the wound, and let the blood run down upon the edge of the altar'; the King James 'wring off his head … wrung out at the side'.")],
  },
  '1:16': {
   'received': "He removes its crop with its feathers and throws it beside the altar on the east, at the place for ashes.",
   'explain': "All four columns agree; the Hebrew word rendered 'with its feathers' is lexically difficult and follows its traditional sense.",
   'shared': ["The crop removed.", "Thrown beside the altar on the east.", "At the ash place."],
   'instructions': [ins(K, S, "The bird's crop was thrown to the ash heap east of the altar."), ins(W, R, "The crop, full of whatever the bird last ate, goes to the ashes; what is unclean in the offering is set aside, not burned to God.")],
   'entries': ['altar'],
   'lost': [AGREE],
  },
  '1:17': {
   'received': "He tears it open by its wings without dividing it; the priest burns it on the altar on the wood on the fire: a burnt offering, an offering by fire, a pleasing aroma to YHWH.",
   'explain': "The Hebrew, Latin and King James have 'burn'; the Greek 'place'. The Latin adds 'or divide it with a blade' and 'with fire placed beneath the wood'.",
   'shared': ["Torn open by the wings.", "Not divided.", "Burned on the altar as a pleasing aroma."],
   'instructions': [ins(K, S, "The bird was torn open but kept whole and burned as a pleasing aroma."), ins(W, R, "Not divided: the bird is too small to cut up and is offered whole and opened; the chapter ends on the littlest gift being called by the same name as the bull's.")],
   'entries': ['altar', 'term-savor', 'yhwh-yahweh'],
   'lost': BURN + [loses("Hebrew 'an offering by fire' is lost."), keeps("Greek 'It is an offering, a sacrifice, a sweet savour unto the Lord'.")],
  },
 },
}
