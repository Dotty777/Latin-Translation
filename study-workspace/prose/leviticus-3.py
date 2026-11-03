K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
PEACE = [loses("Hebrew 'sacrifice of well-being' (shelamim) is lost."), keeps("Greek 'sacrifice of deliverance' (soterion), which the source says is not itself a prediction of Christ."), between("The Latin and King James have 'peace offering'.")]
KIDNEYS = [loses("Hebrew 'loins' and 'appendage of the liver' are lost."), keeps("Greek 'by the thighs' and 'the lobe upon the liver'."), between("The Latin has 'flanks' and 'membrane of the liver'; the King James 'flanks' and 'caul above the liver'.")]
BURN = [loses("Hebrew 'burn' is lost as the explicit verb."), keeps("Greek 'offer up upon the altar'."), between("The Latin and King James have 'burn' with the Hebrew.")]

CHAPTER = {
 'slug': 'leviticus', 'chapter': 3,
 'chapterNote': "The sacrifice of well-being, or peace offering: from the herd, male or female, unblemished, hand laid on, slaughtered at the tent's entrance, blood dashed around the altar, the fat of the entrails, kidneys and liver lobe burned on the altar over the burnt offering; from the flock, a sheep with its whole fat tail, or a goat, the same; the priest burns the fat as food, an offering by fire, and all fat is YHWH's; a perpetual statute that Israel eat neither fat nor blood. The Greek has 'sacrifice of deliverance' for well-being, 'gift' for offering, 'hands' plural (3:2, 8, 13), 'pour' for 'dash', 'thighs' for 'loins' and 'lobe' for 'appendage' of the liver, 'offer up' for 'burn', 'belly' for 'entrails'; it adds 'the altar of whole burnt offerings' (3:2) and 'before the Lord' (3:13), lacks the Hebrew's 'food' (3:11, 16), and at 3:9 names 'the unblemished loin … with the muscles of the lower back' where the Hebrew prescribes the whole fat tail, a material anatomical difference the source keeps visible. The Latin and King James follow the Hebrew's 'peace offering' and 'burn' while sharing the Greek's 'pour'.",
 'verses': {
  '3:1': {
   'received': "If the offering is a sacrifice of well-being from the herd, male or female, it is brought unblemished before YHWH.",
   'explain': "The Hebrew shelamim stresses peace or well-being; the Greek soterion deliverance; the Latin and King James 'peace offering'. All allow male or female.",
   'shared': ["A peace offering.", "From the herd, male or female.", "Unblemished before YHWH."],
   'instructions': [ins(K, S, "The peace offering could be male or female, but unblemished."), ins(C, S, "Whether male or female, he shall bring it unblemished before YHWH."), ins(W, R, "Male or female: the peace offering is the one sacrifice that does not insist on a male; it is a meal shared with God, and the herd's females are welcome at it.")],
   'entries': ['altar', 'yhwh-yahweh'],
   'lost': PEACE,
  },
  '3:2': {
   'received': "He lays his hand on the head of his offering and slaughters it at the entrance of the Tent of Meeting; Aaron's sons, the priests, dash the blood all around against the altar.",
   'explain': "The Hebrew has hand singular and 'dash'; the Greek 'hands' and 'pour' and adds 'the altar of whole burnt offerings'; the Latin 'pour'.",
   'shared': ["Hand on the head.", "Slaughtered at the tent's entrance.", "The priests put the blood around the altar."],
   'instructions': [ins(K, S, "The offerer laid his hand on the peace offering and killed it at the tent door."), ins(W, R, "The same hand and the same door as the burnt offering; the rites begin alike and part at the altar, where this one is shared.")],
   'entries': ['altar', 'high-priest', 'tabernacle'],
   'lost': [loses("Hebrew 'his hand' and 'dash' are lost."), keeps("Greek 'his hands', 'pour', and 'the altar of whole burnt offerings'."), between("The Latin has 'his hand' and 'pour'; the King James 'his hand' and 'sprinkle'.")],
  },
  '3:3': {
   'received': "From the sacrifice of well-being he presents an offering by fire to YHWH: the fat covering the entrails and all the fat on them.",
   'explain': "The Hebrew and King James have the singular presenter; the Greek and Latin plural 'they'; the Greek 'belly' for 'entrails'.",
   'shared': ["An offering to YHWH.", "The fat covering the entrails.", "All the fat on them."],
   'instructions': [ins(K, S, "The inner fat of the peace offering was presented to YHWH."), ins(W, R, "The fat is God's share of a meal eaten by the family; he takes the richest part and leaves the meat.")],
   'entries': ['altar', 'yhwh-yahweh'],
   'lost': [loses("Hebrew singular 'he shall present', 'offering by fire', and 'entrails' are lost."), keeps("Greek 'they shall bring an offering unto the Lord: the fat which covers the belly'."), between("The Latin has plural 'they shall present' and 'internal organs'; the King James 'he shall offer … the inwards'.")],
  },
  '3:4': {
   'received': "The two kidneys with the fat on them by the loins, and the appendage of the liver, removed with the kidneys.",
   'explain': "All four columns agree in the parts; the Greek 'thighs' for loins and 'lobe' for appendage; the Latin 'flanks' and 'membrane'.",
   'shared': ["The two kidneys.", "The fat on them.", "The liver's lobe, with the kidneys."],
   'instructions': [ins(K, S, "The kidneys, their fat and the liver lobe were part of God's portion."), ins(W, R, "Kidneys and liver, the seat of feeling in Hebrew idiom; the innermost organs go to God as the innermost man should.")],
   'entries': ['altar'],
   'lost': KIDNEYS,
  },
  '3:5': {
   'received': "Aaron's sons burn it on the altar on the burnt offering on the wood on the fire: an offering by fire, a pleasing aroma to YHWH.",
   'explain': "The Hebrew, Latin and King James have 'burn'; the Greek 'offer up', 'the priests', and plural 'whole burnt offerings'.",
   'shared': ["Burned on the altar.", "On the burnt offering.", "A pleasing aroma to YHWH."],
   'instructions': [ins(K, S, "The fat was burned on top of the burnt offering as a pleasing aroma."), ins(W, R, "On the burnt offering: the peace offering's fat is laid over the morning lamb; the shared meal rides on the whole gift.")],
   'entries': ['altar', 'high-priest', 'term-savor', 'yhwh-yahweh'],
   'lost': BURN + [keeps("Greek 'the sons of Aaron, the priests' and 'upon the whole burnt offerings'.")],
  },
  '3:6': {
   'received': "If the offering for a sacrifice of well-being to YHWH is from the flock, male or female, it is brought unblemished.",
   'explain': "All four columns agree; the Latin 'from the sheep'.",
   'shared': ["From the flock.", "Male or female.", "Unblemished."],
   'instructions': [ins(K, S, "Peace offerings from the flock were likewise male or female, unblemished."), ins(W, R, "The flock rule repeats the herd's; the law is written out in full for each animal so that no offerer has to guess.")],
   'entries': ['altar'],
   'lost': PEACE,
  },
  '3:7': {
   'received': "If he brings a sheep as his offering, he presents it before YHWH.",
   'explain': "All four columns agree; the Greek and Latin 'lamb'.",
   'shared': ["A sheep.", "Brought as the offering.", "Before YHWH."],
   'instructions': [ins(K, S, "A sheep was presented before YHWH as a peace offering."), ins(W, R, "Sheep and goat are treated separately because their fat differs; the law knows the animals it legislates.")],
   'entries': ['lamb-of-god', 'yhwh-yahweh'],
   'lost': [loses("Hebrew 'sheep' is lost."), keeps("Greek 'a lamb as his gift'."), between("The Latin and King James have 'a lamb'.")],
  },
  '3:8': {
   'received': "He lays his hand on its head and slaughters it before the Tent of Meeting; Aaron's sons dash its blood around the altar.",
   'explain': "The Hebrew 'hand', 'before the tent', 'dash'; the Greek 'hands', 'beside the doors of the Tent of Testimony', 'pour', and 'the priests'.",
   'shared': ["Hand on its head.", "Slaughtered before the tent.", "Blood around the altar."],
   'instructions': [ins(K, S, "The sheep was killed before the tent and its blood dashed around the altar."), ins(W, R, "The same three acts, hand, knife, blood, for the third time; the ritual is learned by repetition, and the text teaches it that way.")],
   'entries': ['altar', 'high-priest', 'tabernacle'],
   'lost': [loses("Hebrew 'his hand', 'before the Tent of Meeting', and 'dash' are lost."), keeps("Greek 'his hands', 'beside the doors of the Tent of Testimony', 'the priests', and 'pour'."), between("The Latin has 'his hand', 'at the entrance', and 'pour'; the King James 'sprinkle'.")],
  },
  '3:9': {
   'received': "From the sacrifice of well-being he presents its fat as an offering by fire to YHWH: the whole fat tail removed close to the backbone, the fat covering the entrails and all the fat on them.",
   'explain': "The Hebrew, Latin and King James prescribe the whole fat tail or rump; the Greek 'the unblemished loin, which he shall remove with the muscles of the lower back', a materially different anatomical instruction; the Greek also 'unto God'.",
   'shared': ["The fat presented to God.", "Removed near the backbone.", "The fat of the entrails."],
   'instructions': [ins(K, S, "The sheep's whole fat tail was part of God's portion."), ins(W, R, "The fat tail: the broad-tailed sheep of the Near East carries its richness behind, and the Hebrew gives that whole store to God.")],
   'entries': ['altar', 'lamb-of-god'],
   'lost': [loses("Hebrew 'the entire fat tail, which he shall remove close to the backbone' is lost."), keeps("Greek 'the fat and the unblemished loin, which he shall remove with the muscles of the lower back' and 'unto God'."), between("The Latin has 'the fat and the whole tail'; the King James 'the whole rump … hard by the backbone'.")],
  },
  '3:10': {
   'received': "The two kidneys with the fat on them by the loins, and the appendage of the liver, removed with the kidneys.",
   'explain': "All four columns agree in substance; the Greek runs into verse 11; the Latin repeats the belly fat and organs.",
   'shared': ["The two kidneys.", "The fat on them.", "The liver's lobe."],
   'instructions': [ins(K, S, "The sheep's kidneys and liver lobe went to the altar."), ins(W, R, "The organs named again, exactly; the law's repetitions are its way of making sure.")],
   'entries': ['altar'],
   'lost': KIDNEYS + [between("The Latin repeats 'the fat that covers the belly and all the internal organs' here.")],
  },
  '3:11': {
   'received': "The priest burns it on the altar: food, an offering by fire to YHWH.",
   'explain': "The Hebrew, Latin and King James call the offering 'food'; the Greek 'a sweet savour, an offering unto the Lord' and 'offer up'.",
   'shared': ["The priest.", "On the altar.", "An offering to YHWH."],
   'instructions': [ins(K, S, "The priest burned the sheep's fat as food for YHWH's fire."), ins(W, R, "'Food': the Hebrew calls the altar's share a meal, lehem, bread; the peace offering is a dinner at which God is served first.")],
   'entries': ['altar', 'high-priest', 'yhwh-yahweh'],
   'lost': BURN + [loses("Hebrew 'food' is lost."), keeps("Greek 'a sweet savour, an offering unto the Lord'."), between("The Latin has 'as food for the fire'; the King James 'the food of the offering made by fire'.")],
  },
  '3:12': {
   'received': "If the offering is a goat, he presents it before YHWH.",
   'explain': "All four columns agree.",
   'shared': ["A goat.", "The offering.", "Before YHWH."],
   'instructions': [ins(K, S, "A goat could be a peace offering before YHWH."), ins(W, R, "The goat, the poorer man's flock animal, is a peace offering too; the shared meal with God is not reserved for those with sheep.")],
   'entries': ['yhwh-yahweh'],
   'lost': [AGREE],
  },
  '3:13': {
   'received': "He lays his hand on its head and slaughters it before the Tent of Meeting; Aaron's sons dash its blood around the altar.",
   'explain': "The Hebrew 'hand' singular and singular slaughterer; the Greek 'hands', plural 'they shall slaughter', 'before the Lord', 'the priests', 'pour'.",
   'shared': ["Hand on its head.", "Slaughtered at the tent.", "Blood around the altar."],
   'instructions': [ins(K, S, "The goat was killed before the tent and its blood dashed around the altar."), ins(W, R, "The goat gets the same hand and the same blood as the bull; before the altar the animals are equal in rite.")],
   'entries': ['altar', 'high-priest', 'tabernacle'],
   'lost': [loses("Hebrew 'his hand', singular 'slaughter', and 'dash' are lost."), keeps("Greek 'his hands', 'they shall slaughter it before the Lord beside the doors of the Tent of Testimony', 'the priests', 'pour'."), between("The Latin has 'his hand' and 'pour'; the King James 'his hand' and 'sprinkle'.")],
  },
  '3:14': {
   'received': "From it he presents his offering as an offering by fire to YHWH: the fat covering the entrails and all the fat on them.",
   'explain': "The Hebrew and King James have the singular presenter; the Greek 'offer up' and 'belly'; the Latin plural 'they shall take … as food for the Lord's fire'.",
   'shared': ["An offering to YHWH.", "The fat covering the entrails.", "All the fat on them."],
   'instructions': [ins(K, S, "The goat's inner fat was offered to YHWH."), ins(W, R, "The same fat from a goat as from a bull; what God takes does not change with the animal's price.")],
   'entries': ['altar', 'yhwh-yahweh'],
   'lost': [loses("Hebrew 'offering by fire' and 'entrails' are lost."), keeps("Greek 'he shall offer up an offering unto the Lord: the fat which covers the belly'."), between("The Latin has 'They shall take from it, as food for the Lord's fire'; the King James follows the Hebrew.")],
  },
  '3:15': {
   'received': "The two kidneys with the fat on them by the loins, and the appendage of the liver, removed with the kidneys.",
   'explain': "All four columns agree in substance; the Greek 'all the fat' and 'thighs'; the Latin 'membrane over them' and 'the fat of the liver'.",
   'shared': ["The two kidneys.", "The fat on them.", "The liver's lobe."],
   'instructions': [ins(K, S, "The goat's kidneys and liver lobe went to the altar."), ins(W, R, "Third time for the kidneys; the chapter is a butcher's manual as much as a liturgy, and both are God's.")],
   'entries': ['altar'],
   'lost': KIDNEYS + [keeps("Greek 'all the fat upon them'.")],
  },
  '3:16': {
   'received': "The priest burns them on the altar: food, an offering by fire for a pleasing aroma. All the fat belongs to YHWH.",
   'explain': "The Hebrew, Latin and King James have 'food'; the Greek lacks it. All reserve the fat to God.",
   'shared': ["The priest burns them.", "A pleasing aroma.", "All the fat is YHWH's."],
   'instructions': [ins(K, S, "All fat belonged to YHWH and was burned as his food."), ins(C, S, "All the fat belongs to YHWH."), ins(W, R, "'All the fat is YHWH's': a line of law that is also a line of diet; what Israel may not eat is what God does.")],
   'entries': ['altar', 'high-priest', 'term-savor', 'yhwh-yahweh'],
   'lost': BURN + [loses("Hebrew 'food' is lost."), keeps("Greek 'an offering, a sweet savour unto the Lord. All the fat is the Lord's'.")],
  },
  '3:17': {
   'received': "A perpetual statute through the generations in all dwellings: eat neither fat nor blood.",
   'explain': "All four columns agree; the sacrificial context identifies the fat meant.",
   'shared': ["A perpetual statute.", "In all dwellings.", "Neither fat nor blood eaten."],
   'instructions': [ins(K, S, "Israel was forbidden forever to eat fat or blood."), ins(C, S, "You shall eat neither any fat nor any blood."), ins(W, R, "Fat and blood, God's portion and the animal's life, both kept off Israel's table; the chapter ends by reaching from the altar into every kitchen.")],
   'entries': ['yhwh-yahweh'],
   'lost': [AGREE],
  },
 },
}
