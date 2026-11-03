K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
BURN = [loses("Hebrew 'burn' is lost as the explicit verb."), keeps("Greek 'place upon the altar'."), between("The Latin and King James have 'burn' with the Hebrew.")]
GRAIN = [loses("Hebrew 'grain offering' (minhah) is lost as a specific term."), keeps("Greek 'sacrifice' (thysia), the ingredients identifying it as cereal."), between("The Latin has 'sacrifice' or 'offering'; the King James 'meat offering', food not flesh.")]

CHAPTER = {
 'slug': 'leviticus', 'chapter': 2,
 'chapterNote': "The grain offering: fine flour with oil and frankincense, of which the priest burns a handful as a memorial portion and keeps the rest, most holy, for Aaron's sons; the same baked in an oven, on a griddle or in a pan, broken and oiled; no leaven or honey on the altar, though they may be brought as firstfruits; salt on every offering, the salt of the covenant; and the firstfruits offering of roasted crushed fresh grain with oil and frankincense. The Greek has 'gift' and 'sacrifice' for the Hebrew's specific grain offering (minhah), 'place' or 'offer up' for 'burn' (2:2, 9, 11, 16), 'hearth' for the Hebrew's deep pan (2:7), 'the covenant of the Lord' for 'of your God' (2:13), and 'new roasted and crushed groats' without the Hebrew's fire phrase (2:14); it adds 'it is a sacrifice' (2:1) and 'unto the Lord' (2:4, 2:6). The King James's 'meat offering' means food, not flesh.",
 'verses': {
  '2:1': {
   'received': "When anyone brings a grain offering as a gift to YHWH, it is fine flour; he pours oil on it and puts frankincense on it.",
   'explain': "All four columns agree in the ingredients; the Greek 'if a soul brings a gift as a sacrifice' and adds 'It is a sacrifice'; the King James 'meat offering' is food.",
   'shared': ["A grain offering to YHWH.", "Fine flour.", "Oil and frankincense on it."],
   'instructions': [ins(K, S, "The grain offering was fine flour with oil and frankincense."), ins(C, S, "His offering shall be fine flour; he shall pour oil on it and put frankincense on it."), ins(W, R, "After the animals, bread: the second offering has no blood at all, and the poor man's flour is received on the same altar as the rich man's bull.")],
   'entries': ['altar', 'wheat', 'olive-tree', 'incense'],
   'lost': GRAIN + [keeps("Greek adds the closing 'It is a sacrifice'.")],
  },
  '2:2': {
   'received': "He brings it to Aaron's sons, the priests, takes a full handful of flour and oil with all the frankincense, and the priest burns the memorial portion on the altar, an offering by fire, a pleasing aroma to YHWH.",
   'explain': "The Hebrew, Latin and King James have the handful; the Hebrew and King James 'burn', the Greek and Latin 'place'; the Latin 'one of them shall take'.",
   'shared': ["Brought to the priests.", "A handful with all the frankincense.", "The memorial portion on the altar."],
   'instructions': [ins(K, S, "A handful of the grain offering was burned as its memorial portion."), ins(W, R, "A handful for God and the rest for the priest; the grain offering is mostly eaten, and the altar gets a memorial, a reminder of the whole.")],
   'entries': ['altar', 'high-priest', 'term-savor', 'yhwh-yahweh'],
   'lost': BURN + [loses("Hebrew 'an offering by fire' is lost."), keeps("Greek 'a sacrifice, a sweet savour unto the Lord'.")],
  },
  '2:3': {
   'received': "What remains of the grain offering belongs to Aaron and his sons; it is most holy among YHWH's offerings by fire.",
   'explain': "All four columns agree; the Greek 'sacrifices of the Lord' for 'offerings by fire'.",
   'shared': ["The remainder.", "Aaron's and his sons'.", "Most holy."],
   'instructions': [ins(K, S, "The rest of the grain offering was the priests' most holy portion."), ins(W, R, "Most holy, and eaten: the priests' bread is of the highest grade of holiness, so that their meals are a kind of worship.")],
   'entries': ['high-priest', 'yhwh-yahweh'],
   'lost': GRAIN,
  },
  '2:4': {
   'received': "An oven-baked grain offering is fine flour, unleavened cakes mixed with oil and unleavened wafers spread with oil.",
   'explain': "All four columns agree; the Greek 'a gift unto the Lord' and the third person for the Hebrew 'you'.",
   'shared': ["Baked in an oven.", "Unleavened cakes with oil.", "Unleavened wafers with oil."],
   'instructions': [ins(K, S, "Oven-baked grain offerings were unleavened cakes and wafers with oil."), ins(W, R, "Cakes and wafers, the two shapes of unleavened bread from Exodus 29; the priest's ordination bread becomes everyone's offering.")],
   'entries': ['unleavened-bread', 'altar'],
   'lost': [loses("Hebrew 'when you bring' second person is lost."), keeps("Greek 'if he brings a gift as a sacrifice baked in an oven, a gift unto the Lord'."), between("The Latin and King James keep the second person.")],
  },
  '2:5': {
   'received': "A grain offering prepared on a griddle is fine flour mixed with oil, unleavened.",
   'explain': "All four columns agree; the Latin 'in a pan'.",
   'shared': ["Prepared on a griddle.", "Fine flour with oil.", "Unleavened."],
   'instructions': [ins(K, S, "Griddle offerings were unleavened flour and oil."), ins(W, R, "Oven, griddle, pan: the law names the kitchen's three tools; God accepts bread however a household makes it.")],
   'entries': ['unleavened-bread'],
   'lost': [keeps("Greek 'a sacrifice from a griddle'."), between("The Latin has 'prepared in a pan'; the King James 'baken in a pan'.")],
  },
  '2:6': {
   'received': "It is broken into pieces and oil poured on it; it is a grain offering.",
   'explain': "The Hebrew and King James have the singular and 'it is a grain offering'; the Greek plural 'them' and 'a sacrifice unto the Lord'; the Latin lacks the closing identification.",
   'shared': ["Broken into pieces.", "Oil poured on.", "A grain offering."],
   'instructions': [ins(K, S, "The griddle cake was broken up and oiled."), ins(W, R, "Broken before it is given; the bread is torn so that a handful can be taken, and the breaking is part of the offering.")],
   'entries': ['unleavened-bread'],
   'lost': [loses("Hebrew singular 'break it' and 'it is a grain offering' are lost."), keeps("Greek 'break them into pieces' and 'It is a sacrifice unto the Lord'."), between("The Latin has 'divide it into small pieces' without the identification; the King James 'it is a meat offering'.")],
  },
  '2:7': {
   'received': "A grain offering prepared in a deep pan is made of fine flour with oil.",
   'explain': "The Hebrew's marheshet is a cooking vessel; the Greek eschara a hearth or brazier; the Latin 'griddle', the King James 'fryingpan'. The source does not equate the equipment.",
   'shared': ["A cooking vessel.", "Fine flour.", "With oil."],
   'instructions': [ins(K, S, "Pan-cooked grain offerings were flour and oil."), ins(W, R, "No one is sure what vessel the Hebrew means; four translations give four utensils, and the offering is the same.")],
   'entries': ['unleavened-bread'],
   'lost': [loses("Hebrew 'deep pan' (marheshet) is lost."), keeps("Greek 'a sacrifice from a hearth' (eschara)."), between("The Latin has 'on a griddle'; the King James 'in the fryingpan'.")],
  },
  '2:8': {
   'received': "The grain offering made from these is brought to YHWH, presented to the priest, who brings it near the altar.",
   'explain': "The Hebrew and King James have the priest bring it to the altar; the Greek a participial run-on, 'when he has drawn near unto the altar', continuing into verse 9; the Latin 'place it in the priest's hands'.",
   'shared': ["Brought to YHWH.", "Presented to the priest.", "To the altar."],
   'instructions': [ins(K, S, "The cooked offering went through the priest to the altar."), ins(W, R, "The offerer stops at the priest; the bread crosses the last step to the altar in other hands.")],
   'entries': ['altar', 'high-priest', 'yhwh-yahweh'],
   'lost': [loses("Hebrew 'who shall bring it near the altar' as a finite clause is lost."), keeps("Greek 'he shall bring it unto the priest; and when he has drawn near unto the altar', running into verse 9."), between("The Latin has 'place it in the priest's hands'; the King James follows the Hebrew.")],
  },
  '2:9': {
   'received': "The priest removes the memorial portion from the grain offering and burns it on the altar, an offering by fire, a pleasing aroma to YHWH.",
   'explain': "The Hebrew, Latin and King James have 'burn'; the Greek 'place' and repeats 'the priest'.",
   'shared': ["The memorial portion.", "On the altar.", "A pleasing aroma to YHWH."],
   'instructions': [ins(K, S, "The priest burned the memorial portion of the cooked offering."), ins(W, R, "The memorial portion again; God is given the part that remembers the whole, and the rule is the same for raw flour and baked bread.")],
   'entries': ['altar', 'high-priest', 'term-savor', 'yhwh-yahweh'],
   'lost': BURN,
  },
  '2:10': {
   'received': "What is left belongs to Aaron and his sons, most holy among YHWH's offerings by fire.",
   'explain': "All four columns agree.",
   'shared': ["What is left.", "Aaron's and his sons'.", "Most holy."],
   'instructions': [ins(K, S, "The rest of the cooked offering was the priests' most holy food."), ins(W, R, "Repeated from 2:3 so that no kind of grain offering is left out; the priests' bread is secured by law twice.")],
   'entries': ['high-priest', 'yhwh-yahweh'],
   'lost': GRAIN,
  },
  '2:11': {
   'received': "No grain offering to YHWH is made with leaven, for no leaven or honey is burned as an offering by fire to YHWH.",
   'explain': "The Hebrew, Latin and King James have 'burn'; the Greek 'bring … as an offering'. All forbid leaven and honey.",
   'shared': ["No leaven.", "No honey.", "In YHWH's fire offering."],
   'instructions': [ins(K, S, "Leaven and honey were barred from the altar."), ins(C, S, "No grain offering that you bring to YHWH shall be made with leaven."), ins(W, R, "No leaven and no honey: nothing that ferments and nothing that sweetens; the altar's bread is plain, as the exodus bread was.")],
   'entries': ['unleavened-bread', 'altar', 'yhwh-yahweh'],
   'lost': [loses("Hebrew 'you shall not burn any leaven or any honey' is lost."), keeps("Greek 'you shall bring neither any leaven nor any honey from it as an offering'."), between("The Latin has 'No leaven or honey shall be burned'; the King James 'ye shall burn no leaven, nor any honey'.")],
  },
  '2:12': {
   'received': "They may be brought to YHWH as an offering of firstfruits, but they do not go up on the altar for a pleasing aroma.",
   'explain': "All four columns agree; the Greek 'a gift of firstfruits', the Latin 'firstfruits and gifts'.",
   'shared': ["Brought as firstfruits.", "Not on the altar.", "Not for a pleasing aroma."],
   'instructions': [ins(K, S, "Leaven and honey could be firstfruits but never altar food."), ins(W, R, "Permitted to be given and forbidden to be burned; the leavened loaf is God's at the door and not on the fire.")],
   'entries': ['altar', 'term-savor'],
   'lost': [keeps("Greek 'As a gift of firstfruits you shall bring them … it shall not be brought up upon the altar'."), between("The Latin has 'only as firstfruits and gifts … not be placed upon the altar'; the King James 'not be burnt on the altar'.")],
  },
  '2:13': {
   'received': "Every grain offering is seasoned with salt; the salt of the covenant of your God is not missing from it; with all offerings bring salt.",
   'explain': "The Hebrew, Latin and King James have 'the covenant of your God'; the Greek 'the covenant of the Lord' and adds 'unto the Lord your God'. The source says this does not make two covenants.",
   'shared': ["Salt on every offering.", "The salt of the covenant.", "Not to be missing."],
   'instructions': [ins(K, S, "Salt, the salt of the covenant, went on every offering."), ins(C, S, "Season every offering of your grain offering with salt."), ins(W, R, "'The salt of the covenant': salt keeps, and the covenant is meant to; every offering carries the one thing on the table that does not spoil.")],
   'entries': ['term-covenant', 'altar'],
   'lost': [loses("Hebrew 'the covenant of your God' is lost."), keeps("Greek 'the salt of the covenant of the Lord' and 'bring salt unto the Lord your God'."), between("The Latin and King James have 'your God's covenant' or 'the covenant of thy God'.")],
  },
  '2:14': {
   'received': "A grain offering of firstfruits to YHWH is fresh ears roasted in the fire, crushed fresh grain.",
   'explain': "The Hebrew, Latin and King James have fresh or green ears and the fire; the Greek 'new roasted and crushed groats' without the fire phrase.",
   'shared': ["A firstfruits grain offering.", "Roasted.", "Crushed fresh grain."],
   'instructions': [ins(K, S, "The firstfruits offering was roasted, crushed new grain."), ins(W, R, "Green ears roasted: the first grain of the year is eaten half-ripe and parched, and the first of that goes to God before anyone has bread from it.")],
   'entries': ['wheat', 'yhwh-yahweh'],
   'lost': [loses("Hebrew 'fresh ears roasted in the fire' is lost."), keeps("Greek 'new roasted and crushed groats unto the Lord'."), between("The Latin has 'ears of grain still green … roast them in the fire and crush them into coarse meal'; the King James 'green ears of corn dried by the fire'.")],
  },
  '2:15': {
   'received': "Oil is put on it and frankincense placed on it; it is a grain offering.",
   'explain': "All four columns agree; the Greek 'pour oil'; the Latin 'because it is the Lord's offering'.",
   'shared': ["Oil on it.", "Frankincense on it.", "A grain offering."],
   'instructions': [ins(K, S, "Oil and frankincense were added to the firstfruits grain."), ins(W, R, "Oil and frankincense on parched grain, the same dressing as on fine flour; the rough first harvest is honoured like the finest milling.")],
   'entries': ['olive-tree', 'incense'],
   'lost': [keeps("Greek 'pour oil upon it … It is a sacrifice'."), between("The Latin has 'because it is the Lord's offering'; the King James 'it is a meat offering'.")],
  },
  '2:16': {
   'received': "The priest burns the memorial portion, some of the crushed grain and oil with all the frankincense, an offering by fire to YHWH.",
   'explain': "The Hebrew, Latin and King James have 'burn'; the Greek 'offer up', a verb that does not itself specify combustion.",
   'shared': ["The memorial portion.", "Grain, oil and all the frankincense.", "An offering to YHWH."],
   'instructions': [ins(K, S, "The priest burned the firstfruits' memorial portion."), ins(W, R, "All the frankincense every time, but only some of the grain; the fragrance is wholly God's, the food is shared.")],
   'entries': ['altar', 'high-priest', 'incense', 'yhwh-yahweh'],
   'lost': [loses("Hebrew 'burn' and 'offering by fire' are lost."), keeps("Greek 'the priest shall offer up its memorial portion … It is an offering unto the Lord'."), between("The Latin has 'the priest shall burn … as a memorial of the gift'; the King James 'burn the memorial of it'.")],
  },
 },
}
