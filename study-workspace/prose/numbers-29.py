K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FIRE = [loses("Hebrew 'fire offering' is lost."), keeps("Greek 'offerings' (karpomata), without naming fire."), between("The Latin and King James have 'offering made by fire' or 'burnt offering'.")]
GRAIN = [loses("Hebrew 'grain offering' is lost."), keeps("Greek 'sacrifice'."), between("The Latin and King James have 'meat offering' or 'sacrifice'.")]
CALF = [loses("Hebrew 'young bull(s)' is lost."), keeps("Greek 'calf' or 'calves'."), between("The Latin and King James have 'bullock(s)'.")]
TENTH = [between("The Latin has 'a tenth of a tenth' per lamb; the Hebrew, Greek and King James 'a tenth' (of an ephah).")]
PLUR = [loses("Hebrew's singular 'its grain offering and its drink offering' is lost."), keeps("Greek plural 'their sacrifices and their drink offerings'."), between("The Latin and King James follow the Hebrew singular.")]
RULE = [between("The Latin has 'duly' (rite); the Greek and King James 'according to their number, after the manner/prescription'.")]
SIN = [between("The Latin has 'for the people's atonement' or 'for guilt'; the Greek 'to make propitiation for you'; the King James 'to make an atonement for you'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

ORD = {2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh'}
BULLS = {2: 'twelve', 3: 'eleven', 4: 'ten', 5: 'nine', 6: 'eight', 7: 'seven'}
WIS = {
 2: "Twelve bulls on the second day: the count falls by one each day, thirteen to seven, seventy bulls in all, a number the rabbis read as the seventy nations.",
 3: "Eleven bulls: the descending count makes the week a single shape rather than seven identical days; the feast is counting down to something.",
 4: "Ten bulls on the fourth day, the midpoint of the week; the rams and lambs never change, the bulls alone diminish.",
 5: "Nine bulls: no reason is given for the diminishing series, and the law does not explain itself here; it only requires exactness.",
 6: "Eight bulls: the sixth day, as in creation, is the last full day of work before a day set apart.",
 7: "Seven bulls on the seventh day: the series lands on the number of the week itself, and the full count of the feast's bulls is seventy.",
}

def day(n, first=False):
    k1, k2, k3 = f'29:{3*n+11}', f'29:{3*n+12}', f'29:{3*n+13}'
    o, b = ORD[n], BULLS[n]
    return {
     k1: v(f"On the {o} day, {b} young bulls, two rams, fourteen unblemished year-old lambs.", "All four columns agree on the animals; Greek 'calves'.",
       [f"The {o} day.", f"{b.capitalize()} bulls.", "Two rams, fourteen lambs."], f"The {o} day took {b} bulls.", WIS[n], CALF, [], f"Offer on the {o} day {b} bulls, two rams and fourteen lambs."),
     k2: v("Their grain offering and drink offerings for the bulls, rams and lambs by their number, according to the rule.", "The Hebrew plural 'drink offerings'; the Greek a singular collective; the Latin 'duly'.",
       ["Grain and drink offerings.", "By their number.", "According to the rule."], "The accompaniments followed the count.", "'By their number, according to the rule': the proportions of chapter 28 are assumed, not repeated; the law expects the priest to know the table.", GRAIN + RULE, []),
     k3: v("And one male goat for sin, besides the regular burnt offering, its grain offering and its drink offering.", "The Hebrew singular 'its grain offering and its drink offering'; the Greek plural.",
       ["One goat for sin.", "Besides the regular offering.", "Its grain and drink."], "A sin goat was added daily.", "Every festival day still has its goat for sin and still rests on the daily lambs; the feast is added to the ordinary, never substituted for it.", PLUR, ['altar']),
    }

VERSES = {
  '29:1': v("In the seventh month, on the first of the month, a holy assembly; no laborious work; a day of trumpet blasts for you.", "The Hebrew teru'ah 'blast, shout'; the Greek semasia 'signalling'; the Latin 'revered and holy … trumpet blasts'.",
   ["The seventh month, day one.", "A holy assembly, no work.", "A day of trumpet blasts."], "The first of the seventh month was a day of blasts.", "Yom Teru'ah, the day of the blast, later Rosh Hashanah: the autumn's first horn, ten days before Atonement, calling the people to attention before the reckoning.",
   [loses("Hebrew teru'ah, the alarm or jubilant blast, is lost."), keeps("Greek 'a day of signalling' (semasia)."), between("The Latin and King James have 'blowing the trumpets'.")], [], "Hold a holy assembly on the first of the seventh month and do no laborious work."),
  '29:2': v("A burnt offering as a pleasing aroma to YHWH: one young bull, one ram, seven unblemished year-old lambs.", "All four columns agree; Greek 'calf' and 'whole burnt offerings'.",
   ["A burnt offering.", "A pleasing aroma.", "One bull, one ram, seven lambs."], "The day's burnt offering was one, one and seven.", "The same set as the new moon's second half: the first of the seventh month is a new moon and more, a doubled day.", CALF, ['yhwh-yahweh', 'term-savor']),
  '29:3': v("Their grain offering: fine flour mixed with oil, three tenths for the bull, two tenths for the ram.", "The Hebrew minchah 'grain offering'; the Greek thysia 'sacrifice'.",
   ["Fine flour with oil.", "Three tenths for the bull.", "Two tenths for the ram."], "Flour was measured to the animal.", "Three, two, one: the flour scales to the beast, so that the whole offering is proportioned, nothing arbitrary.", GRAIN, []),
  '29:4': v("And one tenth for each of the seven lambs.", "All four columns agree.", ["One tenth.", "Each lamb.", "Seven lambs."], "A tenth went with each lamb.", "The small measure repeated seven times; the lambs are the most numerous and the least costly, and each still has its portion.", [AGREE], []),
  '29:5': v("And one male goat for sin, to make atonement for you.", "The Latin 'for the people's atonement'; the Greek 'to make propitiation for you'.",
   ["One male goat.", "For sin.", "To make atonement for you."], "A goat atoned on the day of blasts.", "Even the day of the trumpets needs its goat; no feast in Israel is pure celebration, every one carries a sin offering.", SIN, ['high-priest']),
  '29:6': v("Besides the new moon burnt offering and its grain offering, and the regular burnt offering and its grain offering, and their drink offerings according to their rule, a pleasing aroma, a fire offering to YHWH.", "The Greek supplies drink offerings for both sets and lacks the fire-offering designation; the Latin adds 'the same ceremonies'.",
   ["Besides the new moon offering.", "Besides the regular offering.", "A fire offering to YHWH."], "The day's offerings were stacked on the monthly and daily.", "Three layers on one altar: the daily lambs, the new moon's set, and the feast's set; the holy day does not cancel the ordinary but is built on it.", FIRE + [between("The Latin adds 'with the same ceremonies'; the Greek 'according to their prescription'.")], ['yhwh-yahweh', 'term-savor']),
  '29:7': v("On the tenth of this seventh month, a holy assembly; humble yourselves; do no work.", "The Greek lacks 'seventh'; the Latin 'afflict your souls … servile work'.",
   ["The tenth day.", "A holy assembly.", "Humble yourselves, no work."], "The tenth day was for self-denial.", "The Day of Atonement, given here only in its calendar form: the one day of the year on which the people's work is to afflict themselves; Leviticus 16 and 23 carry the ritual.",
   [loses("Hebrew 'the tenth of this seventh month' is lost."), keeps("Greek 'the tenth of this month', without 'seventh'."), between("The Latin has 'afflict your souls'; the King James likewise.")], ['high-priest'], "Humble yourselves on the tenth day and do no work."),
  '29:8': v("A burnt offering to YHWH as a pleasing aroma: one young bull, one ram, seven year-old lambs; they shall be unblemished for you.", "The Greek adds 'offerings' (karpomata); the animals agree.",
   ["A burnt offering.", "One bull, one ram, seven lambs.", "Unblemished for you."], "Atonement day had the same set.", "'Unblemished for you': the perfection of the animal is for the offerer's sake; a blemished gift would not carry his day.", CALF + [keeps("Greek adds 'offerings' (karpomata).")], ['yhwh-yahweh', 'term-savor']),
  '29:9': v("Their grain offering: fine flour mixed with oil, three tenths for the bull, two tenths for the one ram.", "All four columns agree on the measures.",
   ["Fine flour with oil.", "Three tenths for the bull.", "Two tenths for the ram."], "The flour followed the same scale.", "The chapter repeats its tables deliberately; a priest reading it was meant to be able to serve any day of the year from this page alone.", GRAIN, []),
  '29:10': v("One tenth for each of the seven lambs.", "The Latin 'a tenth of a tenth'; the Hebrew, Greek and King James 'a tenth'.",
   ["One tenth.", "Each lamb.", "Seven lambs."], "Each lamb had its tenth.", "The Latin's 'tenth of a tenth' is a slip repeated in several verses; the measure is a tenth of an ephah, about two quarts of flour.", TENTH, []),
  '29:11': v("One male goat for sin, besides the sin offering of atonement, the regular burnt offering, its grain offering, and their drink offerings.", "The Greek adds 'to make propitiation for you' and the concluding formula; its final drink offering is singular.",
   ["One goat for sin.", "Besides the atonement sin offering.", "Besides the regular offering."], "A festival goat stood beside the atonement goat.", "'Besides the sin offering of atonement': the great goat of Leviticus 16 is assumed; this is the ordinary festival goat, added on the day that already has the extraordinary one.",
   [keeps("Greek adds 'to make propitiation for you … according to their prescription, a pleasing aroma, an offering to the Lord'."), between("The Latin mentions 'what is usually offered for guilt'.")], ['high-priest']),
  '29:12': v("On the fifteenth of the seventh month, a holy assembly; no laborious work; keep a festival to YHWH seven days.", "All four columns agree.",
   ["The fifteenth day.", "A holy assembly, no work.", "A festival of seven days."], "The fifteenth began the seven-day feast.", "Tabernacles, the harvest-home at the full moon of the seventh month, the longest and gladdest feast, and the one with the heaviest altar.", [AGREE], ['yhwh-yahweh'], "Keep a festival to YHWH for seven days from the fifteenth of the seventh month."),
  '29:13': v("A burnt offering, a fire offering, a pleasing aroma to YHWH: thirteen young bulls, two rams, fourteen year-old lambs, unblemished.", "The Greek adds 'on the first day' and has 'offerings' for the fire offering.",
   ["Thirteen bulls.", "Two rams.", "Fourteen lambs."], "The first day took thirteen bulls.", "Thirteen bulls on one day, more than any other day in the calendar; the whole week will burn seventy bulls, fourteen rams, ninety-eight lambs, seven goats.",
   FIRE + [keeps("Greek adds 'On the first day' to place the offering.")], ['yhwh-yahweh', 'term-savor']),
  '29:14': v("Their grain offering: fine flour with oil, three tenths for each of the thirteen bulls, two tenths for each of the two rams.", "All four columns agree on quantities.",
   ["Three tenths per bull.", "Two tenths per ram.", "Thirteen and two."], "Flour scaled to thirteen bulls.", "Nearly four ephahs of flour for the bulls alone on the first day; the feast consumed the new harvest it celebrated.", GRAIN, []),
  '29:15': v("And one tenth for each of the fourteen lambs.", "The Latin 'a tenth of a tenth'; the others 'a tenth'.",
   ["One tenth.", "Each lamb.", "Fourteen lambs."], "Each of fourteen lambs had its tenth.", "Fourteen lambs, twice seven, every day for seven days; the lambs are the constant of the feast.", TENTH, []),
  '29:16': v("And one male goat for sin, besides the regular burnt offering, its grain offering and its drink offering.", "The Hebrew singular grain and drink offering; the Greek plural.",
   ["One goat for sin.", "Besides the regular offering.", "Its grain and drink."], "The first day's goat was added.", "The refrain of the chapter: 'besides the regular burnt offering'; nine times the law insists the daily lambs are not displaced by festival.", PLUR, ['altar']),
  '29:35': v("On the eighth day you shall have a solemn assembly; do no laborious work.", "The Hebrew atseret 'solemn assembly'; the Greek exodion 'closing festival'; the Latin 'most solemn'.",
   ["The eighth day.", "A solemn assembly.", "No laborious work."], "An eighth day closed the feast.", "Shemini Atseret, the eighth-day closing: the week of booths overflows into one more day, and the offerings drop back to the single set, as if the feast were ending quietly.",
   [loses("Hebrew atseret, 'solemn assembly, restraint', is lost."), keeps("Greek exodion, 'a closing festival'."), between("The Latin has 'most solemn'; the King James 'a solemn assembly'.")], [], "Hold a solemn assembly on the eighth day and do no laborious work."),
  '29:36': v("A burnt offering, a fire offering, a pleasing aroma to YHWH: one bull, one ram, seven unblemished year-old lambs.", "The Hebrew names the fire offering; the Greek 'offerings'.",
   ["One bull.", "One ram.", "Seven lambs."], "The eighth day returned to one, one and seven.", "From thirteen bulls back to one: the closing day uses the same set as the day of blasts and Atonement, binding the three autumn days together.", FIRE, ['yhwh-yahweh', 'term-savor']),
  '29:37': v("Their grain offering and drink offerings for the bull, the ram and the lambs by their number, according to the rule.", "All four columns agree; the Latin 'duly'.",
   ["Grain and drink offerings.", "By their number.", "According to the rule."], "The eighth day's accompaniments followed the rule.", "The same shorthand: the measures are known, the priest counts and pours.", GRAIN + RULE, []),
  '29:38': v("And one male goat for sin, besides the regular burnt offering, its grain offering and its drink offering.", "Hebrew singular; Greek plural.",
   ["One goat for sin.", "Besides the regular offering.", "Its grain and drink."], "The closing day had its goat.", "The last goat of the autumn: eight in Tabernacles alone, and the daily lambs under all of them.", PLUR, ['altar']),
  '29:39': v("These you shall offer to YHWH at your appointed times, apart from your vows and freewill offerings, for your burnt, grain, drink and peace offerings.", "The Greek coordinates the offering types after 'apart from'; shelamim becomes 'salvation offerings' (soteria).",
   ["At your appointed times.", "Apart from vows and freewill offerings.", "Burnt, grain, drink and peace."], "The calendar was the public minimum.", "The whole of 28–29 is the public, fixed sacrifice; on top of it rides everything personal, the vow, the freewill gift, the peace offering. The altar's year is the floor, not the ceiling.",
   [loses("Hebrew shelamim, 'peace' or 'well-being' offerings, is lost."), keeps("Greek 'offerings of salvation' (soteria)."), between("The Latin has 'peace offerings' (pacifica); the King James 'peace offerings'.")], ['yhwh-yahweh']),
}
for n in range(2, 8):
    VERSES.update(day(n))

CHAPTER = {
 'slug': 'numbers', 'chapter': 29,
 'chapterNote': "The calendar of public offerings, part two: the seventh month. The first day, the day of trumpet blasts: a holy assembly, one bull, one ram, seven lambs and a goat, on top of the new moon and daily offerings. The tenth, the Day of Atonement: self-denial, the same set, a goat beside the atonement goat. The fifteenth begins the seven-day feast of booths with thirteen bulls, two rams, fourteen lambs and a goat on the first day, the bulls falling by one each day to seven on the seventh (seventy in all), each day's grain and drink 'by their number, according to the rule', each day 'besides the regular burnt offering'. An eighth day of solemn assembly returns to one, one and seven. The close: all this at the appointed times, apart from vows, freewill and peace offerings. The Greek has 'a day of signalling' for 'trumpet blasts' (29:1), 'calves' for 'young bulls', 'sacrifice' for 'grain offering', 'offerings' for 'fire offering' (29:6, 13, 36), lacks 'seventh' at 29:7, adds 'on the first day' at 29:13 and a propitiation formula at 29:11, pluralises the daily 'its grain offering and its drink offering' throughout, 'a closing festival' for 'solemn assembly' (29:35), and 'salvation offerings' for 'peace offerings' (29:39). The Latin reads 'a tenth of a tenth' at 29:10 and 29:15 and 'duly' for 'according to the rule'.",
 'verses': VERSES,
}
