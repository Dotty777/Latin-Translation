K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
DWELL = [loses("Hebrew 'Dwelling' (mishkan) is lost."), keeps("Greek 'Tent'."), between("The Latin and King James have 'tabernacle'.")]
MOUTH = [loses("Hebrew 'at the mouth of YHWH' is lost."), keeps("Greek 'by the command of the Lord' or 'voice'."), between("The Latin and King James have 'word' or 'commandment of the Lord'.")]
EVEN = [loses("Hebrew 'between the evenings' is lost."), keeps("Greek 'toward evening'."), between("The Latin has 'at evening'; the King James 'at even'.")]
PROSP = [keeps("Greek states the rule prospectively ('shall camp … shall set out'); the Hebrew narrates what they did."), between("The Latin and King James follow the Hebrew's past tense.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 9,
 'chapterNote': "The second Passover and the cloud. In the first month of the second year Israel keeps the Passover at Sinai; men unclean through a corpse ask why they should be excluded, Moses waits for YHWH's word, and a second Passover is granted on the fourteenth of the second month to the unclean and the far traveller, with unleavened bread and bitter herbs, nothing left till morning, no bone broken; the clean who neglect it are cut off, and the resident alien keeps it by one law. Then the cloud: it covered the Dwelling the day it was raised, fire by night, and Israel set out when it rose and camped where it settled, whether for two days, a month or a year, at the mouth of YHWH through Moses. The Greek has 'tell them' (9:2), 'first month … toward evening … at the appointed times' (9:3), a compressed 9:5 ('at the beginning') without the evening and renewed Passover, 'destroyed' for 'cut off' and 'distant' repeated (9:13), 'newcomer … in your land' for 'resident alien' (9:14), 'Tent, the House of Testimony' (9:15), adds 'by day' (9:16), states the cloud rules prospectively with camp before setting out (9:18), 'God' for 'YHWH' (9:19), 'by day or by night' for the Hebrew's day-and-night clause (9:21), 'a month' only for 'two days, a month, or days on end' and lacks the rising clause (9:22), and lacks the camping clause at 9:23.",
 'verses': {
  '9:1': v("YHWH speaks to Moses in Sinai's wilderness, in the second year after the exodus, in the first month.", "All four columns agree; the date precedes 1:1.",
   ["In Sinai's wilderness.", "The second year.", "The first month."], "The Passover law came a month before the census.", "A step back in time: the first month, before the census of the second; the book is not in order, and tells us so with a date.",
   FORMULA, ['yhwh-yahweh', 'moses', 'sinai', 'egypt']),
  '9:2': v("Israel observes the Passover at its appointed time.", "All four columns agree; the Greek 'tell the sons of Israel'.",
   ["Israel.", "Observes the Passover.", "At its time."], "The Passover was to be kept.", "The first anniversary: a year since the night in Egypt, and the lamb is eaten in freedom.", [keeps("Greek 'Tell the sons of Israel to observe'.")], ['passover-lamb'], "Observe the Passover at its appointed time."),
  '9:3': v("On the fourteenth of this month, between the evenings, at its appointed time, by all its statutes and ordinances.", "The Hebrew 'this month … between the evenings'; the Greek 'first month … toward evening … appointed times'.",
   ["The fourteenth.", "Between the evenings.", "By all its statutes."], "The date and rules were fixed.", "Between the evenings, as in Exodus 12; the hour is kept exactly, the one fixed point in a wandering year.",
   EVEN + [keeps("Greek 'first month … at the appointed times … its prescribed determination'.")], ['passover-lamb']),
  '9:4': v("Moses told Israel to observe the Passover.", "All four columns agree.", ["Moses told Israel.", "To observe.", "The Passover."],
   "Moses passed on the command.", "Said and relayed.", [AGREE], ['moses']),
  '9:5': v("They observed the Passover in the first month, the fourteenth day, between the evenings, in Sinai's wilderness; as YHWH commanded Moses, so Israel did.",
   "The Hebrew is full; the Greek 'at the beginning, on the fourteenth day … in the wilderness of Sinai' without the evening or the renewed Passover.",
   ["They kept the Passover.", "The fourteenth, at Sinai.", "As commanded."], "The first anniversary Passover was kept.", "The second Passover ever, the first in freedom; the only one recorded in the wilderness until Joshua's at Jericho.",
   EVEN + [loses("Hebrew 'they observed the Passover … between the evenings' is lost."), keeps("Greek 'At the beginning, on the fourteenth day of the month … the sons of Israel did'.")], ['sinai', 'passover-lamb', 'yhwh-yahweh']),
  '9:6': v("Men unclean through a corpse could not observe the Passover that day; they came before Moses and Aaron.", "All four columns agree; the Greek 'arrived'.",
   ["Men unclean by a corpse.", "Could not keep it.", "Came to Moses and Aaron."], "A hard case arose.", "A funeral the week before and a man is shut out of the year's great night; the law of chapter 5 has a cost, and the men bring the cost to Moses.", [keeps("Greek 'men arrived who were unclean'.")], ['moses', 'high-priest']),
  '9:7': v("They said: we are unclean through a corpse; why should we be kept from presenting YHWH's offering at its time among Israel?", "All four columns agree.",
   ["We are unclean.", "Why kept back?", "From YHWH's offering."], "The men asked for a remedy.", "Not a complaint but a question, and a pious one: they want to give, and the law stops them. The question changes the law.", [AGREE], ['yhwh-yahweh']),
  '9:8': v("Moses said: wait, and I will hear what YHWH commands concerning you.", "All four columns agree; 'stand here' in Greek; the Latin 'consult'.",
   ["Wait.", "I will hear.", "What YHWH commands."], "Moses sought a ruling.", "'Wait, and I will hear': Moses does not know, and says so; the second of the four cases in the Torah held for God's answer.",
   [keeps("Greek 'Stand here'."), between("The Latin has 'I will consult the Lord'.")], ['moses', 'yhwh-yahweh']),
  '9:9': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "The ruling."],
   "YHWH answered.", "The answer comes, and it is larger than the question.", FORMULA, ['yhwh-yahweh', 'moses']),
  '9:10': v("Anyone among you or your generations unclean through a corpse or on a distant journey nevertheless observes the Passover to YHWH.", "All four columns agree; the Latin 'in your nation'.",
   ["Unclean or far away.", "In any generation.", "Still keeps the Passover."], "A second chance was granted.", "The ruling covers a case no one asked about, the traveller far from home; God answers the question and the next one.",
   [keeps("Greek 'among you, or among your generations'."), between("The Latin has 'in your nation'.")], ['passover-lamb'], "He shall observe the Passover to YHWH."),
  '9:11': v("In the second month, the fourteenth day, between the evenings, with unleavened bread and bitter herbs.", "All four columns agree; the Latin 'wild lettuces'.",
   ["The second month.", "The fourteenth.", "Unleavened bread and bitter herbs."], "The second Passover was a month later.", "A month's grace: the same night re-run for those who missed it, with the same bread and the same bitterness.",
   EVEN + [between("The Latin has 'wild lettuces' for bitter herbs.")], ['unleavened-bread']),
  '9:12': v("None left till morning, no bone broken; by every statute of the Passover.", "All four columns agree. John reads the unbroken bone as fulfilled in Jesus.",
   ["None till morning.", "No bone broken.", "Every statute."], "The second Passover kept every rule.", "'Break no bone of it': the lamb whole to the end; John will stand at a cross and remember the rule.", [AGREE], ['passover-lamb', 'lamb-of-god'], "They shall break no bone of it."),
  '9:13': v("A person clean and not on a journey who neglects the Passover is cut off; because he did not present YHWH's offering at its time, he bears his sin.", "The Hebrew 'cut off … on a journey'; the Greek 'destroyed … distant journey'.",
   ["Clean and at home.", "Neglects the Passover.", "Cut off; bears his sin."], "Neglect of Passover was cut off.", "The mercy of the second month makes neglect inexcusable; the one who could and did not has no second chance.",
   [loses("Hebrew 'cut off' is lost."), keeps("Greek 'that soul shall be destroyed … not on a distant journey'."), between("The Latin and King James have 'cut off'.")], ['yhwh-yahweh']),
  '9:14': v("A resident alien among you who observes the Passover does so by its statute and ordinance; one statute for alien and native.", "The Hebrew 'resident alien'; the Greek 'sojourner (proselytos) … in your land'.",
   ["A resident alien.", "By the same statute.", "One law for all."], "Aliens kept Passover by the same law.", "One law for the stranger: the Passover that began as Israel's alone is open to the foreigner who lives among them, on the same terms.",
   [keeps("Greek 'if a sojourner comes unto you in your land'."), between("The Latin has 'foreigner and sojourner'; the King James 'stranger'.")], [], "You shall have one statute for alien and native."),
  '9:15': v("On the day the Dwelling was raised the cloud covered it, the Tent of Testimony; in the evening an appearance like fire over it until morning.", "The Hebrew 'Dwelling … Tent of Testimony'; the Greek 'Tent … House of Testimony'.",
   ["The day the Dwelling was raised.", "The cloud covered it.", "Fire by night."], "The cloud took its place over the tent.", "Back to Exodus 40: the cloud that led them from Egypt settles on the finished house, and glows at night like a hearth.",
   DWELL + [keeps("Greek 'the Tent, the House of Testimony'.")], ['tabernacle']),
  '9:16': v("So it was continually: the cloud covered it, and an appearance of fire by night.", "All four columns agree; the Greek adds 'by day'.",
   ["Continually.", "Cloud.", "Fire by night."], "Cloud and fire were constant.", "'Continually': the whole wilderness under one cloud by day and one fire by night; the weather of the camp was God.", [keeps("Greek 'the cloud covered it by day'.")]),
  '9:17': v("Whenever the cloud rose from the Tent, Israel set out; where it settled, Israel camped.", "All four columns agree; 'stood' in Greek.",
   ["The cloud rises; they go.", "The cloud settles; they camp.", "Israel follows."], "The cloud gave the marching orders.", "No itinerary, no map: Israel moves when the cloud moves and stops where it stops. The whole journey is one rule.",
   [keeps("Greek 'where the cloud stood'."), between("The Latin and King James have 'abode'.")]),
  '9:18': v("At the mouth of YHWH Israel set out and at his mouth they camped; as long as the cloud dwelt over the Dwelling they camped.", "The Greek reverses to camp/set out and makes it prospective.",
   ["At YHWH's mouth they set out.", "At his mouth they camped.", "While the cloud dwelt."], "The cloud was God's command.", "The cloud is called 'the mouth of YHWH': the people read God's will in the sky, as the rest of the book will read it in Moses.",
   MOUTH + DWELL + PROSP, ['yhwh-yahweh', 'tabernacle']),
  '9:19': v("When the cloud stayed many days over the Dwelling, Israel kept YHWH's charge and did not set out.", "All four columns agree; 'God' in Greek.",
   ["Many days.", "YHWH's charge kept.", "Not setting out."], "Long halts were kept patiently.", "Many days in one place is obedience too; waiting is a charge kept.",
   DWELL + PROSP + [keeps("Greek 'the charge of God'.")], ['yhwh-yahweh']),
  '9:20': v("Sometimes the cloud stayed a few days; at YHWH's mouth they camped and at his mouth set out.", "All four columns agree in substance; the Greek 'voice … command'.",
   ["A few days.", "At YHWH's mouth.", "Camped and set out."], "Short halts followed the same rule.", "A few days or many, the rule is the same; the length of a stay is never Israel's to decide.", MOUTH + PROSP, ['yhwh-yahweh']),
  '9:21': v("Sometimes the cloud stayed from evening to morning; when it rose in the morning they set out; or a day and a night, and when it rose they set out.", "The Hebrew has two sequences; the Greek one, with 'by day or by night'.",
   ["Evening to morning.", "Or a day and a night.", "When it rose, they set out."], "Even one night's halt was obeyed.", "One night only and the tents come down again at dawn; the camp could be struck at any hour, and the Greek says so outright, 'by day or by night'.",
   [loses("Hebrew 'or if it remained a day and a night, when the cloud rose, they set out' is lost."), keeps("Greek 'they shall set out by day or by night'.")]),
  '9:22': v("Whether two days, a month or a year, while the cloud lingered over the Dwelling Israel camped and did not set out; when it rose they set out.",
   "The Hebrew 'two days, a month, or days (a year)'; the Greek 'the days of a month' only, without the rising clause.",
   ["Two days, a month, a year.", "While the cloud lingered.", "Camped; then set out."], "Halts of any length were obeyed.", "'Days', which the rabbis read as a year: a whole year in one camp if the cloud sat still. Patience is the wilderness's first lesson, and the hardest.",
   DWELL + [loses("Hebrew 'two days … or days on end … when it rose, they set out' is lost."), keeps("Greek 'for the days of a month … shall camp'.")], ['tabernacle']),
  '9:23': v("At YHWH's mouth they camped and at his mouth set out; they kept YHWH's charge at his mouth through Moses.", "The Greek lacks the camping clause.",
   ["At YHWH's mouth.", "Camped and set out.", "Through Moses."], "The chapter closed on obedience.", "'Through Moses': the cloud's command reaches the people through a man; the sky speaks, and Moses says when to strike the tents.",
   MOUTH + [loses("Hebrew 'at the mouth of YHWH they camped' is lost."), keeps("Greek 'for by the command of the Lord they shall set out'.")], ['yhwh-yahweh', 'moses']),
 },
}
