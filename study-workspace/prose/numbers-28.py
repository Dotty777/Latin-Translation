K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
FIRE = [loses("Hebrew 'fire offering' is lost."), keeps("Greek 'offering' or 'whole burnt offering', without naming fire."), between("The Latin and King James have 'offering made by fire'.")]
GRAIN = [loses("Hebrew 'grain offering' is lost."), keeps("Greek 'sacrifice'."), between("The Latin and King James have 'meat offering' or 'sacrifice'.")]
CALF = [loses("Hebrew 'young bulls' is lost."), keeps("Greek 'calves'."), between("The Latin and King James have 'bullocks'.")]
TENTH = [between("The Latin has 'a tenth of a tenth' per lamb; the Hebrew, Greek and King James 'a tenth' (of an ephah).")]
EVEN = [loses("Hebrew 'between the evenings' is lost."), keeps("Greek 'toward evening'."), between("The Latin and King James have 'at even'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 28,
 'chapterNote': "The calendar of public offerings, part one. Daily: two lambs, morning and between the evenings, each with a tenth of flour, a quarter hin of beaten oil and a quarter hin of strong drink, the regular burnt offering instituted at Sinai. Sabbath: two more lambs with their grain and drink. New moon: two bulls, a ram, seven lambs with grain and wine in the fixed proportions, and a goat for sin. Passover on the fourteenth of the first month and seven days of unleavened bread with the same offerings daily and holy assemblies on the first and seventh days. The day of firstfruits at Weeks: the same again. The Greek has 'My gifts, My donations … at My feasts' for 'My offering, My food for My fire offerings … at its appointed time' (28:2), 'offering' for 'fire offering' throughout, 'sacrifice' for 'grain offering', 'calves' for 'young bulls', 'toward evening' for 'between the evenings' (28:4, 8), lacks 'beaten' oil (28:5), lacks the fire-offering designation (28:6, 8, 13), 'new moons' (28:11), 'gift' for 'food' (28:24), 'new produce' for 'firstfruits' (28:26), adds 'unblemished' at 28:27 and 'for sin' at 28:30, and 'their sacrifice for Me' at 28:31. The Latin reads 'a tenth of a tenth' per lamb (28:13, 21, 29).",
 'verses': {
  '28:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the offerings."],
   "YHWH spoke on the public offerings.", "After Joshua's commissioning, the calendar of sacrifice for the land: what the altar will burn every day of every year once they are in.", FORMULA, ['yhwh-yahweh', 'moses']),
  '28:2': v("Command Israel: my offering, my food for my fire offerings, my pleasing aroma, take care to present it to me at its appointed time.", "The Hebrew 'My food for My fire offerings … at its appointed time'; the Greek 'My gifts, My donations, My offerings … at My feasts'.",
   ["My offering.", "My food.", "At its appointed time."], "God claimed his regular food.", "'My food': God calls the offerings his bread, as in Leviticus 21; the altar is a table laid twice a day, and the chapter is the menu.",
   [loses("Hebrew 'My food for My fire offerings … at its appointed time' is lost."), keeps("Greek 'My gifts, My donations, My offerings of sweet savour … at My feasts'.")], ['term-savor'], "Take care to present My offering at its appointed time."),
  '28:3': v("Say: this is the fire offering you present to YHWH: two unblemished year-old lambs daily as a regular burnt offering.", "All four columns agree; 'whole burning' in Greek.",
   ["The fire offering.", "Two lambs daily.", "A regular burnt offering."], "Two lambs a day were the base.", "The tamid, the 'continual': two lambs every day for as long as there is an altar, the heartbeat under all the feasts.", FIRE, ['yhwh-yahweh', 'altar']),
  '28:4': v("One lamb in the morning, the second between the evenings.", "The Hebrew 'between the evenings'; the Greek 'toward evening'.",
   ["One in the morning.", "One between the evenings.", "Daily."], "Morning and evening framed the day.", "Dawn and dusk: the day opens and closes with a lamb, and the hours of Passover and the cross are the hours of the evening lamb.", EVEN, ['lamb-of-god']),
  '28:5': v("With it a tenth of an ephah of fine flour as a grain offering, mixed with a quarter hin of beaten oil.", "The Greek lacks 'beaten'; 'oiphi … sacrifice'.",
   ["A tenth of flour.", "A grain offering.", "A quarter hin of beaten oil."], "Flour and oil went with each lamb.", "Beaten oil, the first pressing, the lampstand's oil; the daily bread offering uses the best.",
   GRAIN + [loses("Hebrew 'beaten oil' is lost."), keeps("Greek 'mixed with oil'.")], ['olive-tree']),
  '28:6': v("It is the regular burnt offering instituted at Mount Sinai, a pleasing aroma, a fire offering to YHWH.", "The Greek lacks the fire-offering designation.",
   ["The regular burnt offering.", "Instituted at Sinai.", "A pleasing aroma."], "The daily offering dated from Sinai.", "'Instituted at Mount Sinai': Exodus 29's command, kept through forty years of wandering and now ordered for the land.", FIRE, ['sinai', 'term-savor']),
  '28:7': v("Its drink offering a quarter hin for each lamb; pour out strong drink to YHWH in the holy place.", "All four columns agree; the Greek sikera 'strong drink'; the Latin 'wine'.",
   ["A quarter hin.", "Strong drink.", "Poured in the holy place."], "Strong drink was poured daily.", "Shekar, strong drink, poured at the altar; the only place the law has it offered to God rather than forbidden to priests.",
   [keeps("Greek 'strong drink' (sikera)."), between("The Latin has 'wine'; the King James 'strong wine'.")], ['yhwh-yahweh']),
  '28:8': v("The second lamb between the evenings, with the same grain and drink offering as the morning, a fire offering, a pleasing aroma.", "The Greek lacks the morning comparison and the fire designation.",
   ["The second lamb at evening.", "Same grain and drink.", "A pleasing aroma."], "The evening matched the morning.", "'As in the morning': the day is symmetrical; the evening lamb repeats the dawn's.",
   EVEN + FIRE + [loses("Hebrew 'the same … as in the morning' is lost."), keeps("Greek 'according to its sacrifice and according to its drink offering'.")]),
  '28:9': v("On the Sabbath, two unblemished year-old lambs with two tenths of flour and oil as grain offering, with its drink offering.", "All four columns agree.",
   ["On the Sabbath.", "Two more lambs.", "Grain and drink."], "The Sabbath doubled the daily.", "Four lambs on the Sabbath instead of two; the day of rest is the altar's busiest day of the week.", GRAIN),
  '28:10': v("The Sabbath burnt offering each Sabbath, in addition to the regular burnt offering and its drink offering.", "All four columns agree.",
   ["Each Sabbath.", "In addition.", "To the regular."], "Sabbath offerings were added, not substituted.", "'In addition to': the chapter's refrain; nothing replaces the daily lambs, everything stacks on them.", [AGREE]),
  '28:11': v("At your months' beginnings a burnt offering to YHWH: two young bulls, one ram, seven unblemished year-old lambs.", "The Greek 'new moons … calves'.",
   ["New moon.", "Two bulls, one ram.", "Seven lambs."], "The new moon had a large offering.", "Ten animals for the new moon; the month's first day is a feast, and the trumpets of 10:10 sound over it.",
   CALF + [keeps("Greek 'at the new moons'.")], ['yhwh-yahweh']),
  '28:12': v("For each bull three tenths of flour with oil as grain offering; for each ram two tenths.", "The Greek lacks the repeated 'grain offering'.",
   ["Three tenths per bull.", "Two per ram.", "With oil."], "The proportions of chapter 15 applied.", "The ladder of chapter 15 again: three, two, one.", GRAIN + CALF),
  '28:13': v("For each lamb a tenth of flour with oil as grain offering: a burnt offering, pleasing aroma, fire offering to YHWH.", "The Latin 'a tenth of a tenth'; the Greek 'sacrifice … offering'.",
   ["A tenth per lamb.", "A burnt offering.", "A pleasing aroma."], "Each lamb took a tenth.", "The lamb's tenth, the smallest measure; seven lambs, seven tenths.", GRAIN + FIRE + TENTH),
  '28:14': v("Drink offerings of wine: half a hin per bull, a third per ram, a quarter per lamb. The monthly burnt offering through the year.", "All four columns agree.",
   ["Half a hin per bull.", "A third per ram.", "A quarter per lamb."], "Wine was proportioned too.", "Twelve new moons a year, each with its ten animals and its wine; the year is marked by the moon at the altar.", [AGREE], ['grapevine']),
  '28:15': v("One male goat as a sin offering to YHWH, in addition to the regular burnt offering and its drink offering.", "All four columns agree.",
   ["One goat.", "For sin.", "In addition."], "A goat for sin closed the new moon.", "Every month begins with a sin offering; a new month is a new chance, and starts clean.", [AGREE], ['yhwh-yahweh']),
  '28:16': v("In the first month, the fourteenth day, is YHWH's Passover.", "All four columns agree.",
   ["The first month.", "The fourteenth.", "YHWH's Passover."], "Passover headed the feasts.", "The date without the lamb: Passover here is a date on the calendar; the household rite is assumed from Exodus 12.", [AGREE], ['passover-lamb']),
  '28:17': v("On the fifteenth a feast; unleavened bread is eaten seven days.", "All four columns agree.",
   ["The fifteenth.", "A feast.", "Unleavened bread seven days."], "Unleavened Bread followed.", "Seven days of flat bread, with the public offerings below added to the household's.", [AGREE], ['unleavened-bread']),
  '28:18': v("On the first day a holy assembly; no laborious work.", "All four columns agree; 'for you' in Greek.",
   ["The first day.", "A holy assembly.", "No laborious work."], "The first day was a rest.", "As in Leviticus 23: the first day holy.", [keeps("Greek 'a holy appointed assembly for you'.")]),
  '28:19': v("Present a fire offering, a burnt offering to YHWH: two young bulls, one ram, seven year-old lambs, unblemished.", "The Greek 'offerings … calves … for you'.",
   ["Two bulls, one ram.", "Seven lambs.", "Unblemished."], "Passover's daily offering matched the new moon's.", "The new moon's ten animals, every day for a week; Passover burns seventy animals in public before the private lambs are counted.", FIRE + CALF, ['yhwh-yahweh']),
  '28:20': v("Their grain offering of flour and oil: three tenths per bull, two per ram.", "All four columns agree.",
   ["Flour and oil.", "Three tenths per bull.", "Two per ram."], "The grain followed the scale.", "The same arithmetic.", GRAIN),
  '28:21': v("A tenth for each of the seven lambs.", "The Latin 'a tenth of a tenth'.",
   ["A tenth.", "Each lamb.", "Seven."], "Each lamb's tenth.", "Seven tenths for seven lambs.", TENTH),
  '28:22': v("One male goat as a sin offering to atone for you.", "All four columns agree.",
   ["One goat.", "For sin.", "To atone."], "A goat atoned daily.", "A sin offering each day of the feast; freedom is celebrated with atonement.", [AGREE]),
  '28:23': v("Offer these in addition to the morning burnt offering, which belongs to the regular burnt offering.", "The Greek repeats 'continual whole burnt offering' and lacks 'you shall offer these'.",
   ["In addition.", "To the morning offering.", "The regular."], "The daily lambs were never displaced.", "The two lambs under everything, again.", [keeps("Greek 'besides the continual morning whole burning, which is a continual whole burnt offering'.")]),
  '28:24': v("Offer these daily for seven days as food, a fire offering, a pleasing aroma to YHWH, in addition to the regular burnt offering and its drink offering.", "The Hebrew 'food … fire offering'; the Greek 'a gift, an offering' and adds the libation command.",
   ["Daily for seven days.", "Food, a fire offering.", "In addition."], "The week's offerings were summed.", "'As food': God's bread again, seven days of it.", FIRE + [loses("Hebrew 'as food' is lost."), keeps("Greek 'a gift … you shall prepare its drink offering'.")], ['term-savor']),
  '28:25': v("On the seventh day a holy assembly; no laborious work.", "All four columns agree.",
   ["The seventh day.", "A holy assembly.", "No laborious work."], "The feast closed with rest.", "Rest on both ends of the week, as in Leviticus 23.", [keeps("Greek 'a holy summoned assembly for you'.")]),
  '28:26': v("On the day of firstfruits, presenting a new grain offering to YHWH at your Feast of Weeks, a holy assembly; no laborious work.", "The Hebrew 'firstfruits … grain offering'; the Greek 'new produce … new sacrifice'.",
   ["The day of firstfruits.", "A new grain offering.", "At Weeks."], "Weeks was a holy day.", "Pentecost by its other name, the day of firstfruits; the wheat's first loaves of Leviticus 23 have their public animals here.",
   GRAIN + [loses("Hebrew 'firstfruits' is lost."), keeps("Greek 'new produce'.")], ['wheat', 'yhwh-yahweh']),
  '28:27': v("A burnt offering as a pleasing aroma to YHWH: two young bulls, one ram, seven year-old lambs.", "The Greek adds 'unblemished' here; the Hebrew at 28:31.",
   ["Two bulls, one ram.", "Seven lambs.", "A pleasing aroma."], "Weeks took the standard offering.", "Ten animals for the harvest's first day; Leviticus 23 had seven lambs, one bull, two rams, and the rabbis read the two lists as two offerings.", CALF + [keeps("Greek adds 'unblemished'.")], ['term-savor']),
  '28:28': v("Their grain offering of flour and oil: three tenths per bull, two per ram;", "All four columns agree.",
   ["Flour and oil.", "Three tenths per bull.", "Two per ram."], "The grain again.", "The same.", GRAIN),
  '28:29': v("A tenth for each of the seven lambs;", "The Latin 'a tenth of a tenth'.",
   ["A tenth.", "Each lamb.", "Seven."], "The lambs' tenth again.", "The same.", TENTH),
  '28:30': v("One male goat to atone for you.", "The Greek adds 'for sin'.",
   ["One goat.", "To atone.", "For you."], "A goat atoned at Weeks.", "The harvest feast too has its sin offering.", [keeps("Greek 'one male goat for sin'.")]),
  '28:31': v("Offer these in addition to the regular burnt offering and its grain offering; unblemished, with their drink offerings.", "The Hebrew includes the regular grain offering; the Greek 'prepare their sacrifice for Me'.",
   ["In addition to the regular.", "Unblemished.", "With drink offerings."], "The chapter ended on the daily base.", "'In addition to the regular': the last word of the chapter is the daily lambs, under the Sabbath, the moon, Passover and Weeks; chapter 29 will stack the autumn on top.",
   [loses("Hebrew 'and its grain offering' is lost."), keeps("Greek 'you shall prepare their sacrifice for Me'.")]),
 },
}
