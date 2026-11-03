K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
WAVE = [loses("Hebrew 'wave them as a wave offering' is lost."), keeps("Greek 'set them apart as a gift' or 'give them before the Lord'."), between("The Latin has 'offer as a gift'; the King James 'offer … for an offering'.")]
PRAY = [between("The Latin has the priest 'pray'; the Greek 'make propitiation'; the King James 'make an atonement'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 8,
 'chapterNote': "The lamps and the Levites. Aaron sets the seven lamps to shine toward the front of the hammered-gold lampstand made to the pattern shown Moses. The Levites are cleansed with purification water, a razor over the whole body and washed clothes; the congregation lays hands on them, Aaron waves them as a wave offering, they lay hands on two bulls offered for sin and burnt offering, and they enter the tent's service as God's own, taken in place of the firstborn he claimed in Egypt and given to Aaron so that no plague falls on Israel at the sanctuary. They serve from twenty-five to fifty, then assist their brothers without working. The Greek has 'set in place … from one side' for 'raise' (8:2–3), 'solid gold, stem and lilies' for 'hammered, base and flower-work' (8:4), 'year-old' for 'second' bull (8:8), 'set apart as a gift' or 'give' for 'wave' throughout (8:11, 13, 15, 21), 'he shall offer' for the Hebrew's command (8:12), 'no one approaching the holy things' for 'no plague when they approach' (8:19), and 'his brother shall minister' for 'they may assist their brothers' (8:26). Both have twenty-five at 8:24, where chapter 4 had thirty in the Hebrew. The Latin adds the lampstand's southern position at 8:2.",
 'verses': {
  '8:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the lamps."],
   "YHWH spoke on the lamps.", "After the twelve days of gifts, a word about light; the altar is dedicated and the lamps are lit.", FORMULA, ['yhwh-yahweh', 'moses']),
  '8:2': v("Speak to Aaron: when you raise the lamps, the seven lamps give light toward the front of the lampstand.", "The Hebrew 'raise' (also 'light'); the Greek 'set in place … from one side'; the Latin adds the southern position and the table.",
   ["Aaron raises the lamps.", "Seven lamps.", "Light toward the front."], "The lamps faced forward.", "Seven flames turned to throw their light forward, across the tent toward the table of bread; the lampstand lights the meal.",
   [loses("Hebrew 'raise the lamps' is lost."), keeps("Greek 'set the lamps in place, the seven lamps shall shine from one side'."), between("The Latin adds 'on the south side … facing north toward the table'; the King James 'lightest the lamps'.")], ['high-priest', 'lampstand'], "The seven lamps shall give light toward the front of the lampstand."),
  '8:3': v("Aaron did so, raising its lamps toward the front of the lampstand as YHWH commanded Moses.", "All four columns agree; the Greek 'lit … from the one side'.",
   ["Aaron did so.", "Lamps toward the front.", "As commanded."], "Aaron lit the lamps as told.", "Aaron's obedience in a line; the chapter is careful to say the lamps were lit right.",
   [keeps("Greek 'he lit its lamps from the one side'."), between("The Latin has 'placed the lamps'; the King James 'lighted'.")], ['high-priest', 'lampstand']),
  '8:4': v("The lampstand's workmanship: hammered gold from base to flower-work, all hammered; made to the pattern YHWH showed Moses.", "The Hebrew 'hammered … base … flower-work'; the Greek 'solid … stem … lilies'; the Latin 'hammered … shaft and branches'.",
   ["Hammered gold.", "Base to flowers.", "To the pattern shown."], "The lampstand matched its heavenly pattern.", "One piece of beaten gold, base to petal, after a pattern seen on the mountain; the lamp is a copy of something Moses saw.",
   [loses("Hebrew 'hammered … from its base to its flower-work' is lost."), keeps("Greek 'solid gold, its stem and its lilies, entirely solid'."), between("The Latin has 'hammered … shaft and branches'; the King James 'beaten work … shaft … flowers'.")], ['lampstand', 'sinai']),
  '8:5': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On cleansing Levites."],
   "YHWH spoke on consecrating the Levites.", "The Levites were counted and assigned; now they are made clean to begin.", FORMULA, ['yhwh-yahweh', 'moses']),
  '8:6': v("Take the Levites from among Israel and cleanse them.", "All four columns agree.", ["Take the Levites.", "From Israel.", "Cleanse them."],
   "The Levites were to be cleansed.", "Not anointed like priests but cleansed; the Levites are washed, not consecrated with oil. The difference marks their rank.", [AGREE], [], "Take the Levites and cleanse them."),
  '8:7': v("Sprinkle purification water on them, let them pass a razor over all their flesh, wash their clothes and cleanse themselves.", "All four columns agree; the Hebrew's water term carries the sin root.",
   ["Purification water.", "A razor over the body.", "Washed clothes."], "Water, razor and laundry cleansed them.", "Shaved from head to foot like a cleansed leper: the Levites enter service looking like men who have just been healed.",
   [keeps("Greek 'water of purification'."), between("The Hebrew has 'water of sin'; the Latin and King James 'water of purifying' or 'expiation'.")]),
  '8:8': v("They take a young bull with its grain offering of fine flour and oil, and you take a second young bull for a sin offering.", "The Hebrew 'second'; the Greek 'year-old calf', supplying an age.",
   ["A young bull with grain.", "A second bull.", "For sin."], "Two bulls were offered.", "Two bulls for a tribe: the Levites' consecration costs less than Aaron's, and the bulls carry the whole tribe's hands.",
   [loses("Hebrew 'a second young bull' is lost."), keeps("Greek 'a year-old calf from the cattle for sin'."), between("The Latin and King James have 'another young bullock'.")]),
  '8:9': v("Bring the Levites before the Tent of Meeting and assemble the whole congregation.", "All four columns agree.",
   ["Levites before the tent.", "The whole congregation.", "Assembled."], "All Israel witnessed.", "The whole people gathered to see one tribe set aside; the Levites' status is public from the first day.", TENT, ['tabernacle']),
  '8:10': v("Bring the Levites before YHWH, and Israel lays hands on the Levites.", "All four columns agree.",
   ["Before YHWH.", "Israel lays hands.", "On the Levites."], "Israel laid hands on its Levites.", "The people lay hands on the Levites as a man lays hands on his sacrifice: the tribe is Israel's offering, and the gesture says so.", [AGREE], ['yhwh-yahweh']),
  '8:11': v("Aaron waves the Levites as a wave offering before YHWH from Israel, so they may perform YHWH's service.", "The Hebrew 'wave as a wave offering'; the Greek 'set apart as a gift'.",
   ["Aaron waves the Levites.", "A wave offering.", "For YHWH's service."], "The Levites were waved like an offering.", "A whole tribe 'waved' before God, as a priest lifts a breast of meat; the Greek could not picture it and wrote 'gift'. The Hebrew means the Levites are lifted up and handed over.",
   WAVE, ['high-priest', 'yhwh-yahweh'], "Aaron shall wave the Levites as a wave offering."),
  '8:12': v("The Levites lay hands on the bulls' heads; offer one for sin and one as a burnt offering to YHWH, to atone for the Levites.", "The Hebrew commands 'offer'; the Greek 'he shall offer'.",
   ["Levites lay hands on the bulls.", "Sin and burnt offering.", "Atonement for them."], "The Levites' bulls atoned for them.", "Hands on the bulls as Israel's hands were on them: the offering has its own offering, and the chain of substitution runs to the altar.",
   PRAY + [keeps("Greek 'he shall offer'."), between("The Hebrew, Latin and King James have the command 'offer'.")], ['altar', 'yhwh-yahweh']),
  '8:13': v("Stand the Levites before Aaron and his sons and wave them as a wave offering to YHWH.", "The Hebrew 'wave'; the Greek adds 'before the Lord' and 'give them as a gift'.",
   ["Before Aaron and his sons.", "Waved.", "To YHWH."], "The waving was repeated.", "Before the priests and waved toward God: the Levites are given to both at once, the priests their masters and God their owner.",
   WAVE + [keeps("Greek adds 'before the Lord'.")], ['high-priest']),
  '8:14': v("Separate the Levites from among Israel; the Levites are God's.", "All four columns agree.",
   ["Separate the Levites.", "From Israel.", "They are God's."], "The Levites were set apart as God's.", "'The Levites shall be Mine': the sentence of 3:12 said again at the moment of consecration; separation is for possession.", [AGREE], [], "Separate the Levites from among the sons of Israel."),
  '8:15': v("Afterward the Levites enter to serve the Tent of Meeting; cleanse them and wave them as a wave offering.", "The Hebrew 'wave'; the Greek 'give them before the Lord'.",
   ["Afterward they enter.", "To serve the tent.", "Cleansed and waved."], "Service began after the waving.", "First cleansed, then waved, then at work; the order is water, gift, labour.", TENT + WAVE, ['tabernacle']),
  '8:16': v("For they are wholly given to God from Israel; in place of those opening every womb, every firstborn, he has taken them.", "All four columns agree; 'given as a gift' in Greek.",
   ["Wholly given.", "In place of the firstborn.", "Taken for God."], "The Levites replaced the firstborn.", "'Given, given' once more; the reason behind the rite is the exchange made in chapter 3.", [keeps("Greek 'given to Me as a gift'.")]),
  '8:17': v("Every firstborn of Israel is God's, human and animal; when he struck Egypt's firstborn he consecrated them.", "All four columns agree.",
   ["Every firstborn is God's.", "Human and animal.", "Since Egypt."], "The claim dated from Egypt.", "The tenth plague remembered at the Levites' ordination; every Levite stands where an eldest son would have stood.", [AGREE], ['egypt', 'plague-10']),
  '8:18': v("God took the Levites in place of every firstborn of Israel.", "All four columns agree.",
   ["God took the Levites.", "In place of.", "Every firstborn."], "The exchange was restated.", "Said a third time in the chapter; the substitution is the Levites' whole charter.", [AGREE]),
  '8:19': v("God gave the Levites to Aaron and his sons to serve Israel in the Tent of Meeting and atone for Israel, so no plague falls on Israel when they approach the sanctuary.",
   "The Hebrew 'no plague when they approach'; the Greek 'no one among Israel approaching the holy things'. The negative governs different things.",
   ["Given to Aaron.", "To serve and atone.", "No plague at the sanctuary."], "The Levites shielded Israel from plague.", "The Levites are a buffer: they stand near so the people need not, and the plague that nearness would bring falls on no one. The Greek turned the protection into a prohibition.",
   TENT + [loses("Hebrew 'so that no plague should fall among the sons of Israel when they approach' is lost."), keeps("Greek 'there shall be no one among the sons of Israel approaching the holy things'."), between("The Latin and King James have 'no plague'.")], ['high-priest', 'tabernacle']),
  '8:20': v("Moses, Aaron and the whole congregation did for the Levites all YHWH commanded Moses; so Israel did for them.", "All four columns agree.",
   ["Moses, Aaron, the congregation.", "Did all commanded.", "For the Levites."], "The consecration was carried out.", "Everyone named in the doing: the leader, the priest and the people make the Levites what they are.", [AGREE], ['moses', 'high-priest', 'yhwh-yahweh']),
  '8:21': v("The Levites purified themselves and washed their clothes; Aaron waved them before YHWH and atoned for them to cleanse them.", "The Hebrew 'wave'; the Greek 'gave them as a gift'; the Latin 'prayed'.",
   ["Levites purified.", "Aaron waved them.", "Atoned and cleansed."], "The rite was performed as commanded.", "The execution repeats the command, waving and all; the Greek keeps its 'gift' here too.", WAVE + PRAY, ['high-priest', 'yhwh-yahweh']),
  '8:22': v("Afterward the Levites entered their service in the Tent of Meeting before Aaron and his sons; as YHWH commanded Moses, so they did.", "All four columns agree.",
   ["Afterward they entered.", "Before Aaron and his sons.", "As commanded."], "The Levites began serving.", "The Levites go in to work; the long preparation of chapters 1–8 ends with men lifting curtains.", TENT, ['tabernacle', 'high-priest']),
  '8:23': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On ages."],
   "YHWH spoke on Levite ages.", "A short rule on when the service begins and ends.", FORMULA, ['yhwh-yahweh', 'moses']),
  '8:24': v("For the Levites: from twenty-five years old they enter the service of the Tent of Meeting.", "All four columns have twenty-five here; the Hebrew of chapter 4 had thirty.",
   ["From twenty-five.", "They enter.", "The tent's service."], "Service began at twenty-five.", "Twenty-five here, thirty in chapter 4: the Hebrew has both, and the rabbis made the five years an apprenticeship. The Greek read twenty-five in both places.",
   TENT + [between("All columns have twenty-five here; see 4:3 for the thirty.")], ['tabernacle'], "From twenty-five years old they shall enter the service."),
  '8:25': v("From fifty they withdraw from the service of the work and work no more.", "All four columns agree. Rashi limits the retirement to carrying.",
   ["From fifty.", "Withdraw.", "Work no more."], "Service ended at fifty.", "Retirement at fifty, the only retirement age in Scripture; the shoulders that carried the ark are spared after twenty-five years.", [AGREE]),
  '8:26': v("They may assist their brothers in the Tent of Meeting, keeping charge, but do no work. Thus deal with the Levites in their charges.",
   "The Hebrew has the retired Levite assist his brothers; the Greek 'his brother shall minister'.",
   ["Assisting their brothers.", "Keeping charge.", "No work."], "Retired Levites kept watch.", "The old Levite stands guard and advises but does not lift; the law finds a place for the man past his strength.",
   TENT + [loses("Hebrew 'they may assist their brothers' is lost."), keeps("Greek 'his brother shall minister in the Tent of Testimony'."), between("The Latin and King James have 'minister with their brethren'.")], ['tabernacle']),
 },
}
