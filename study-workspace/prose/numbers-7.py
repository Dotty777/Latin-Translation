K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
DWELL = [loses("Hebrew 'Dwelling' (mishkan) is lost."), keeps("Greek 'Tent'."), between("The Latin and King James have 'tabernacle'.")]
GRAIN = [loses("Hebrew 'grain offering' is lost."), keeps("Greek 'sacrifice'."), between("The Latin and King James have 'meat offering' or 'sacrifice'.")]
LADLE = [loses("Hebrew 'ladle' (kaf, a palm-shaped vessel) is lost."), keeps("Greek 'incense vessel'; the gold measure is abbreviated and no modern value is implied."), between("The Latin has 'little mortar'; the King James 'spoon'.")]
CALF = [keeps("Greek 'calf' for the Hebrew's 'young bull'."), between("The Latin has 'ox'; the King James 'young bullock'.")]
GOAT = [keeps("Greek 'one male goat from the goats for sin'."), between("The Hebrew, Latin and King James have 'one kid of the goats for a sin offering'.")]
PEACE = [loses("Hebrew 'well-being sacrifice … two cattle … five year-old lambs' is lost."), keeps("Greek 'sacrifice of deliverance … two heifers … five year-old ewe lambs', making the animals female."), between("The Latin and King James have 'peace offerings … oxen … lambs'.")]
RULER = [keeps("Greek adds 'ruler of the tribe'."), between("The Hebrew, Latin and King James have 'for the tribe' or 'prince'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

DAYS = [
 (12, 'first', 'Nahshon son of Amminadab', 'Judah', "Judah first on the first day: the camp's order is the offering's order; the tribe at the sunrise side gives at sunrise.", ['david']),
 (18, 'second', 'Nethanel son of Zuar', 'Issachar', "Issachar's gift is identical to Judah's; the smaller tribe gives the same as the larger, and no tribe outbids another.", []),
 (24, 'third', 'Eliab son of Helon', 'Zebulun', "The east side completes its three days; the altar has received three identical gifts and will receive nine more.", []),
 (30, 'fourth', 'Elizur son of Shedeur', 'Reuben', "The firstborn tribe gives fourth; birth order yields to the camp's order here as everywhere in the book.", []),
 (36, 'fifth', 'Shelumiel son of Zurishaddai', 'Simeon', "Simeon, the tribe without a blessing in Deuteronomy, gives like all the rest; the altar does not know which tribes will dwindle.", []),
 (42, 'sixth', 'Eliasaph son of Deuel', 'Gad', "Deuel again in the Hebrew, Reuel again in the Greek; the one name the chapter cannot settle.", []),
 (48, 'seventh', 'Elishama son of Ammihud', 'Ephraim', "Ephraim leads Joseph's house on the seventh day; the west side begins behind the tent.", ['joseph-son-of-jacob']),
 (54, 'eighth', 'Gamaliel son of Pedahzur', 'Manasseh', "Manasseh, the smallest tribe, gives the full gift on the eighth day; the offering is not scaled to size.", []),
 (60, 'ninth', 'Abidan son of Gideoni', 'Benjamin', "Benjamin on the ninth day; Rachel's house has given its three.", []),
 (66, 'tenth', 'Ahiezer son of Ammishaddai', 'Dan', "Dan opens the north side's three days; the rear guard brings its silver to the front.", []),
 (72, 'eleventh', 'Pagiel son of Ocran', 'Asher', "Asher on the eleventh day; the gift that has not varied in eleven days does not vary now.", []),
 (78, 'twelfth', 'Ahira son of Enan', 'Naphtali', "Naphtali closes the twelve: twelve days, twelve identical gifts, and the altar is dedicated by the whole people equally.", []),
]

VERSES = {
  '7:1': v("On the day Moses finished setting up the Dwelling he anointed and consecrated it, its furnishings, the altar and its utensils.", "All four columns agree; the Greek repeats 'anointed and consecrated them'.",
   ["Moses finished the Dwelling.", "Anointed and consecrated it.", "And the altar."], "The chapter returned to the tabernacle's first day.", "The chapter steps back a month to the day the tent went up (Exodus 40); the leaders' gifts belong to that day, before the census.", DWELL, ['moses', 'tabernacle', 'anointing-oil', 'altar']),
  '7:2': v("Israel's leaders, heads of ancestral houses, tribal leaders who stood over the registered, presented offerings.", "All four columns agree; the Greek numbers them 'twelve'.",
   ["Israel's leaders.", "Heads of houses.", "Presented offerings."], "The twelve leaders gave.", "The same twelve who counted the people now give for them; the census-takers become donors.", [keeps("Greek 'twelve rulers of their ancestral houses'.")]),
  '7:3': v("Their offering before YHWH: six covered wagons and twelve oxen, a wagon for every two leaders and an ox each, before the Dwelling.", "All four columns agree; 'calf' in Greek.",
   ["Six covered wagons.", "Twelve oxen.", "Before the Dwelling."], "Wagons and oxen were given.", "Two chiefs to a wagon: the first gift is the means of carrying all the others; before the altar's silver, the Levites' transport.", DWELL + CALF, ['yhwh-yahweh', 'tabernacle']),
  '7:4': v("YHWH said to Moses:", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the wagons."],
   "YHWH spoke about the wagons.", "God accepts the gift and directs it; the chiefs gave without being told, and the telling comes after.", [AGREE], ['yhwh-yahweh', 'moses']),
  '7:5': v("Take these from them for the service of the Tent of Meeting; give them to the Levites, each by his service.", "All four columns agree.",
   ["Take them.", "For the tent's service.", "To the Levites by service."], "The wagons went to the Levites.", "'Each according to his service': the wagons are not shared evenly but by load; the law of chapter 4 decides who gets wheels.", TENT, ['tabernacle'], "Give them to the Levites, each according to his service."),
  '7:6': v("Moses took the wagons and oxen and gave them to the Levites.", "All four columns agree.", ["Moses took them.", "Wagons and oxen.", "To the Levites."],
   "Moses distributed them.", "Done.", [AGREE], ['moses']),
  '7:7': v("Two wagons and four oxen to the Gershonites by their service.", "All four columns agree.", ["Two wagons.", "Four oxen.", "To Gershon."],
   "Gershon received two wagons.", "Two wagons for curtains and coverings; cloth is bulky but light.", [keeps("Greek 'according to their ministries'.")]),
  '7:8': v("Four wagons and eight oxen to the Merarites by their service, under Ithamar son of Aaron.", "All four columns agree; 'through Ithamar' in Greek.",
   ["Four wagons.", "Eight oxen.", "To Merari under Ithamar."], "Merari received four wagons.", "Four for the boards and bars; the house with the heaviest load gets two-thirds of the wheels.", [keeps("Greek 'through Ithamar'."), between("The Latin and King James have 'under the hand of Ithamar'.")], ['high-priest']),
  '7:9': v("None to the Kohathites, because the service of the holy things was theirs; they carry on the shoulder.", "All four columns agree.",
   ["None to Kohath.", "The holy things.", "On the shoulder."], "Kohath carried without wagons.", "No cart for the ark: the holiest things ride on men, and David's cart at Nachon's threshing floor will be the cost of forgetting this verse.", [AGREE], ['ark-of-the-covenant']),
  '7:10': v("The leaders presented the dedication offering for the altar on the day it was anointed, before the altar.", "All four columns agree.",
   ["The dedication offering.", "On the anointing day.", "Before the altar."], "The altar's dedication began.", "The second gift, for the altar itself; the chapter now slows to one tribe a day.", [AGREE], ['altar']),
  '7:11': v("YHWH said to Moses: one leader each day, one leader each day, presents his offering for the altar's dedication.", "All four columns agree; the repetition is kept.",
   ["One leader a day.", "One a day.", "For the dedication."], "The gifts were spread over twelve days.", "'One leader each day, one leader each day': the repetition is the rhythm the next seventy-two verses will keep. Twelve days so that no tribe is lost in a crowd.", [AGREE], ['yhwh-yahweh', 'moses'], "One leader each day shall present his offering."),
  '7:84': v("This was the altar's dedication offering from Israel's leaders on the day it was anointed: twelve silver dishes, twelve silver basins, twelve gold ladles.", "All four columns agree; 'incense vessels' in Greek.",
   ["The dedication offering.", "Twelve dishes, twelve basins.", "Twelve gold ladles."], "The vessels were totalled.", "The sums begin; the book that counted men now counts silver.", LADLE, ['altar']),
  '7:85': v("Each dish 130 shekels, each basin seventy; all the silver 2,400 sanctuary shekels.", "All four columns agree.",
   ["130 per dish.", "Seventy per basin.", "2,400 shekels in all."], "The silver totalled 2,400 shekels.", "Twelve times two hundred: the arithmetic is shown, as always in Numbers.", [AGREE]),
  '7:86': v("The twelve gold ladles full of incense, ten sanctuary shekels each; all the gold 120 shekels.", "The Hebrew gives the per-vessel weight; the Greek omits it in the summary.",
   ["Twelve gold ladles.", "Ten shekels each.", "120 shekels."], "The gold totalled 120 shekels.", "A hundred and twenty shekels of gold full of incense; the altar's dedication smells before it burns.",
   LADLE + [loses("Hebrew 'each weighing ten sanctuary shekels' is lost."), keeps("Greek has the total only.")], ['incense']),
  '7:87': v("All the cattle for the burnt offering: twelve bulls, twelve rams, twelve year-old lambs with their grain offering; twelve male goats for sin.", "All four columns agree; the Greek adds 'drink offerings'.",
   ["Twelve bulls.", "Twelve rams, twelve lambs.", "Twelve goats."], "The burnt and sin offerings were totalled.", "Thirty-six animals burned whole, twelve for sin; the altar's first fortnight.",
   CALF + GRAIN + [keeps("Greek adds 'and drink offerings'.")], ['altar']),
  '7:88': v("All the cattle for the well-being sacrifice: twenty-four bulls, sixty rams, sixty goats, sixty year-old lambs. This was the altar's dedication after it was anointed.",
   "The Hebrew 'bulls … lambs'; the Greek 'heifers … unblemished ewe lambs' and adds 'after the filling of his hands'.",
   ["Twenty-four bulls.", "Sixty rams, goats, lambs.", "The dedication after anointing."], "The peace offerings were totalled.", "Two hundred and four animals eaten before God: the dedication of the altar was twelve days of feasting for the whole camp.",
   PEACE + [keeps("Greek adds 'unblemished … after the filling of his hands and after anointing him'.")], ['altar']),
  '7:89': v("When Moses entered the Tent of Meeting to speak with him, he heard the voice speaking from above the atonement cover on the Ark of Testimony, between the two cherubim; he spoke to him.",
   "The Greek names 'the voice of the Lord'; the final pronouns are left as the sources have them. The Latin 'to seek the oracle'.",
   ["Moses enters the tent.", "The voice from above the cover.", "Between the cherubim."], "God spoke from above the ark.", "After the gifts, the voice: God speaks from between the cherubim, over the cover, as Exodus 25:22 promised. The chapter's long inventory ends in a conversation.",
   TENT + [keeps("Greek 'the voice of the Lord … the propitiatory cover'."), between("The Latin has 'to seek the oracle'; the King James 'mercy seat'.")], ['moses', 'ark-of-the-covenant', 'cherubim', 'tabernacle']),
}

for n, day, leader, tribe, wis, ent in DAYS:
    f = f"{leader}, leader of {tribe}" if n == 12 else f"{leader}, leader of {tribe}"
    deuel = (n == 42)
    VERSES[f'7:{n}'] = v(f"On the {day} day {leader}, leader of {tribe}, presented his offering.",
      "All four columns agree; the Greek adds 'ruler of the tribe'." + (" The Hebrew 'Deuel'; the Greek 'Reuel', as at 1:14." if deuel else ""),
      [f"The {day} day.", f"{leader.split(' son')[0]}.", f"For {tribe}."], f"{tribe} gave on the {day} day.", wis,
      RULER + ([loses("Hebrew 'Deuel' is lost."), keeps("Greek 'Reuel'.")] if deuel else []), ent)
    VERSES[f'7:{n+1}'] = v("His offering: one silver dish of 130 shekels, one silver basin of seventy sanctuary shekels, both full of fine flour with oil for a grain offering;",
      "All four columns agree on weights and contents; 'sacrifice' in Greek. The dish's unit is supplied from 7:85.",
      ["A silver dish, 130.", "A silver basin, seventy.", "Flour and oil."], f"{tribe}'s silver matched every other tribe's.", "The same dish and basin as every tribe before and after; equality is written in silver, a shekel at a time.", GRAIN)
    VERSES[f'7:{n+2}'] = v("One gold ladle of ten shekels full of incense;", "The Hebrew 'ladle' (kaf); the Greek 'incense vessel'.",
      ["One gold ladle.", "Ten shekels.", "Full of incense."], f"{tribe} gave gold and incense.", "Ten shekels of gold shaped like a palm, cupping incense; the one gift that is for smell rather than food.", LADLE, ['incense'])
    VERSES[f'7:{n+3}'] = v("One young bull, one ram, one year-old male lamb for a burnt offering;", "All four columns agree; 'calf' in Greek.",
      ["A young bull.", "A ram.", "A year-old lamb."], f"{tribe}'s burnt offering was three animals.", "Bull, ram, lamb: one of each of the flock's three kinds, burned whole.", CALF)
    VERSES[f'7:{n+4}'] = v("One male goat for a sin offering;", "All four columns agree.",
      ["One male goat.", "For sin.", "The same every day."], f"{tribe} gave a goat for sin.", "A goat for sin even on a day of gifts; the dedication does not assume the givers are clean.", GOAT)
    VERSES[f'7:{n+5}'] = v(f"For a well-being sacrifice: two cattle, five rams, five male goats, five year-old lambs. This was the offering of {leader}.",
      "The Hebrew 'cattle … lambs'; the Greek 'heifers … ewe lambs', making the animals female.",
      ["Two cattle.", "Five rams, five goats, five lambs.", f"The offering of {leader.split(' son')[0]}."], f"{tribe}'s peace offering was seventeen animals.", f"Seventeen animals for the feast and the gift signed with the giver's name; {tribe}'s day is done.", PEACE)

CHAPTER = {
 'slug': 'numbers', 'chapter': 7,
 'chapterNote': "The leaders' gifts on the day the Dwelling was anointed: six covered wagons and twelve oxen, given to the Gershonites (two wagons) and Merarites (four) but not to the Kohathites, who carry on the shoulder; then, one leader a day for twelve days in the camp's order (Judah, Issachar, Zebulun, Reuben, Simeon, Gad, Ephraim, Manasseh, Benjamin, Dan, Asher, Naphtali), an identical offering from each: a silver dish of 130 shekels and basin of seventy full of flour and oil, a gold ladle of ten shekels full of incense, a bull, ram and lamb for burnt offering, a goat for sin, and two cattle, five rams, five goats and five lambs for well-being. The totals: 2,400 shekels of silver, 120 of gold, twelve bulls, rams, lambs and goats, twenty-four bulls and sixty each of rams, goats and lambs. Then Moses hears the voice from above the ark's cover between the cherubim. The Greek has 'Tent' for 'Dwelling', 'twelve rulers' (7:2), 'calf' for 'young bull', 'sacrifice' for 'grain offering', 'incense vessel' for 'ladle', 'ruler of the tribe' in each day's heading, 'Reuel' for 'Deuel' (7:42, 47), 'heifers' and 'ewe lambs' for the Hebrew's masculine cattle and lambs in every peace offering (7:17 and eleven times more, 7:88), omits the per-ladle weight at 7:86, adds drink offerings at 7:87 and 'unblemished … after the filling of his hands' at 7:88, and names 'the voice of the Lord' at 7:89. All numbers agree in every column.",
 'verses': VERSES,
}
