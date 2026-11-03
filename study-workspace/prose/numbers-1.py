K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
DWELL = [loses("Hebrew 'Dwelling (mishkan) of Testimony' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin and King James have 'tabernacle of testimony'.")]
CENSUS = [loses("Hebrew 'their descendants by their clans' is lost."), keeps("Greek 'by their families, divisions, and ancestral houses … every male'."), between("The Latin has 'descent, families, households'; the King James 'generations … families … house of their fathers'.")]
REORDER = [between("The Greek lists the tribes in a different order; the source aligns each tribe with its Hebrew place and shows the Greek verse beside it. This is rearrangement, not a different count.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

# (verse of formula, verse of count, tribe, count words, reordered?, wisdom)
TRIBES = [
 (20, 21, 'Reuben, Israel\'s firstborn', 'forty-six thousand five hundred', False, "Reuben first by birth though no longer first in anything else; the census keeps the birth order the blessing did not."),
 (22, 23, 'Simeon', 'fifty-nine thousand three hundred', False, "Simeon's fifty-nine thousand will fall to twenty-two in the second census; the number here is the high mark of a tribe about to shrink."),
 (24, 25, 'Judah', 'seventy-four thousand six hundred', True, "Judah the largest already; the tribe of the sceptre leads in numbers before it leads in anything else."),
 (26, 27, 'Issachar', 'fifty-four thousand four hundred', True, "Issachar, the tribe Jacob called a strong donkey, counted among the strong."),
 (28, 29, 'Zebulun', 'fifty-seven thousand four hundred', True, "Zebulun, who will dwell by the sea, is a landlocked column of men here."),
 (30, 31, 'Joseph through Ephraim', 'forty thousand five hundred', True, "Ephraim before Manasseh, the younger before the elder, as Jacob's crossed hands ordained."),
 (32, 33, 'Manasseh', 'thirty-two thousand two hundred', True, "Manasseh the smallest tribe now; it will more than double by the second census, the only tribe to grow so much."),
 (34, 35, 'Benjamin', 'thirty-five thousand four hundred', True, "Benjamin small, as the youngest; the tribe of Saul begins near the bottom of the list."),
 (36, 37, 'Gad', 'forty-five thousand six hundred fifty', True, "The only count ending in fifty; the census is a real tally, not round numbers."),
 (38, 39, 'Dan', 'sixty-two thousand seven hundred', False, "Dan second only to Judah; the tribe that will hold the rear of the march has the men for it."),
 (40, 41, 'Asher', 'forty-one thousand five hundred', False, "Asher, whose bread would be rich; counted here as soldiers before farmers."),
 (42, 43, 'Naphtali', 'fifty-three thousand four hundred', False, "Naphtali closes the list, the last of Jacob's sons by Bilhah; the twelve are counted and Levi is not among them."),
]

VERSES = {
  '1:1': v("YHWH speaks to Moses in the wilderness of Sinai, in the Tent of Meeting, on the first day of the second month of the second year after the exodus.",
   "The setting and date agree in all four columns; the Hebrew 'Tent of Meeting', the Greek 'Tent of Testimony', the Latin 'tabernacle of the covenant'.",
   ["In the wilderness of Sinai.", "In the tent.", "Second month, second year."], "Numbers opened a year after Sinai.", "A month after the tabernacle was raised, a year and a fortnight out of Egypt: the book begins with a date, because it is about to count.",
   FORMULA + TENT, ['yhwh-yahweh', 'moses', 'sinai', 'tabernacle', 'egypt']),
  '1:2': v("Take a census of the whole congregation of Israel by clans and ancestral houses, counting the names of every male head by head.",
   "All four columns agree; the Greek synagoge 'congregation' does not by itself establish a later church polity.",
   ["A census.", "By clans and houses.", "Every male by name."], "The census was by name and household.", "Every name, head by head: not an estimate but a roll; the people who were 'as the sand' are now counted one by one.",
   [AGREE], [], "Take a census of the whole congregation."),
  '1:3': v("From twenty years old and up, everyone who goes out for military service; Moses and Aaron register them by armies.",
   "All four columns agree; the Greek repeats 'register'. Its verb episkeptomai does not designate a Christian office.",
   ["Twenty and up.", "Fit for service.", "Registered by Moses and Aaron."], "The census was a muster.", "This is a muster, not a headcount: men of fighting age, by armies. Israel is being organised to march.",
   [keeps("Greek 'register them with their army; you and Aaron shall register them'.")], ['moses', 'high-priest']),
  '1:4': v("A man from each tribe, head of his ancestral house, is with you.", "All four columns agree; the Greek 'rulers'.",
   ["One from each tribe.", "Head of his house.", "With Moses."], "Tribal heads assisted the count.", "Twelve men beside Moses, one per tribe; the count is done by the counted, through their own heads.",
   [keeps("Greek 'one of the rulers from each tribe'.")]),
  '1:5': v("The men who stand with you: for Reuben, Elizur son of Shedeur.", "All four columns agree.", ["Named men.", "For Reuben.", "Elizur son of Shedeur."],
   "Reuben's leader was Elizur.", "Elizur, 'my God is a rock'; the names of the twelve are mostly built on El, and tell what their fathers believed.", [AGREE], ['rock']),
  '1:6': v("For Simeon, Shelumiel son of Zurishaddai.", "All four columns agree.", ["For Simeon.", "Shelumiel.", "Son of Zurishaddai."],
   "Simeon's leader was Shelumiel.", "Zurishaddai, 'my rock is Shaddai': the patriarchs' name for God survives in a grandfather's name.", [AGREE], ['el-shaddai']),
  '1:7': v("For Judah, Nahshon son of Amminadab.", "All four columns agree.", ["For Judah.", "Nahshon.", "Son of Amminadab."],
   "Judah's leader was Nahshon.", "Nahshon son of Amminadab stands in the line from Judah to David and to Jesus; Matthew and Luke will name him.", [AGREE], ['david']),
  '1:8': v("For Issachar, Nethanel son of Zuar.", "All four columns agree.", ["For Issachar.", "Nethanel.", "Son of Zuar."],
   "Issachar's leader was Nethanel.", "Nethanel, 'God has given'; a name that reappears for a thousand years.", [AGREE]),
  '1:9': v("For Zebulun, Eliab son of Helon.", "All four columns agree.", ["For Zebulun.", "Eliab.", "Son of Helon."],
   "Zebulun's leader was Eliab.", "Eliab, 'my God is father'; another Eliab, of Reuben, will father Dathan and Abiram.", [AGREE]),
  '1:10': v("For the sons of Joseph: for Ephraim, Elishama son of Ammihud; for Manasseh, Gamaliel son of Pedahzur.", "All four columns agree.",
   ["Joseph's two sons.", "Elishama for Ephraim.", "Gamaliel for Manasseh."], "Joseph counted as two tribes.", "Joseph is two tribes, so that Levi can be none and the twelve still twelve. Elishama is Joshua's grandfather by Chronicles' reckoning.", [AGREE], ['joseph-son-of-jacob', 'joshua']),
  '1:11': v("For Benjamin, Abidan son of Gideoni.", "All four columns agree.", ["For Benjamin.", "Abidan.", "Son of Gideoni."],
   "Benjamin's leader was Abidan.", "Gideoni, from the root of Gideon, 'hewer'; a Benjaminite name before the judge of Manasseh bore it.", [AGREE]),
  '1:12': v("For Dan, Ahiezer son of Ammishaddai.", "All four columns agree.", ["For Dan.", "Ahiezer.", "Son of Ammishaddai."],
   "Dan's leader was Ahiezer.", "Ammishaddai, 'my kinsman is Shaddai'; the second Shaddai name in the list.", [AGREE], ['el-shaddai']),
  '1:13': v("For Asher, Pagiel son of Ocran.", "All four columns agree; spelling only.", ["For Asher.", "Pagiel.", "Son of Ocran."],
   "Asher's leader was Pagiel.", "Pagiel, 'God has met'; the names keep saying what the wilderness is about.", [AGREE]),
  '1:14': v("For Gad, Eliasaph son of Deuel.", "The Hebrew 'Deuel' here (and 'Reuel' at 2:14); the Greek Ragouel, rendered Reuel, throughout.",
   ["For Gad.", "Eliasaph.", "Son of Deuel or Reuel."], "Gad's leader's father is spelled two ways.", "Deuel or Reuel: a dalet and a resh look alike, and the two spellings sit side by side in the Hebrew itself.",
   [loses("Hebrew 'Deuel' is lost."), keeps("Greek 'Reuel' (Ragouel)."), between("The Latin and King James have 'Deuel' here and 'Reuel' at 2:14.")]),
  '1:15': v("For Naphtali, Ahira son of Enan.", "All four columns agree.", ["For Naphtali.", "Ahira.", "Son of Enan."],
   "Naphtali's leader was Ahira.", "Ahira, the one name in the list with 'evil' (ra) in it, 'my brother is evil' or 'brother of Ra'; the ancients did not flinch at it.", [AGREE]),
  '1:16': v("These were summoned from the congregation, leaders of their ancestral tribes, heads of Israel's thousands.", "The Greek chiliarchoi makes the thousands a command role; the Latin 'most distinguished leaders'.",
   ["Summoned from the congregation.", "Leaders of tribes.", "Heads of thousands."], "The twelve were Israel's chiefs.", "'Heads of thousands': the tribe is already an army in units, and these men command it.",
   [keeps("Greek 'commanders of Israel's thousands'."), between("The Latin has 'most distinguished leaders of the multitude and heads of the army'; the King James 'heads of thousands'.")]),
  '1:17': v("Moses and Aaron took these men designated by name.", "The Hebrew, Greek and King James agree; the Latin adds 'with the whole multitude'.",
   ["Moses and Aaron.", "Took the men.", "Designated by name."], "The named men were taken up.", "Named by God, taken by Moses: the chiefs are appointed from above and received from below.",
   [between("The Latin adds 'with the whole multitude of the people'; the Greek and King James 'called by name'.")], ['moses', 'high-priest']),
  '1:18': v("They assembled the whole congregation on the first of the second month; the men declared their descent by clans and houses, names counted, twenty and up, head by head.",
   "The Hebrew dates to the second month and has the men declare descent; the Greek 'the month of the second year', 'every male', and tabulation rather than declaration.",
   ["The congregation assembled.", "Descent declared.", "Twenty and up, head by head."], "Each man declared his lineage.", "'They declared their descent': every man says whose son he is; the census is a people reciting its own genealogy aloud.",
   [loses("Hebrew 'the first day of the second month … declared their descent' is lost."), keeps("Greek 'the first day of the month of the second year … registered them … every male'."), between("The Latin and King James have the second month.")]),
  '1:19': v("As YHWH commanded Moses, he registered them in the wilderness of Sinai.", "The Hebrew active singular; the Greek passive 'they were registered'.",
   ["As YHWH commanded.", "Registered.", "In Sinai's wilderness."], "The count was done as commanded.", "The obedience formula before the numbers; the list that follows is an act of obedience as much as of arithmetic.",
   [keeps("Greek 'they were registered'."), between("The Latin and King James have the passive too.")], ['yhwh-yahweh', 'moses', 'sinai']),
  '1:44': v("These are those registered by Moses, Aaron and the leaders of Israel, twelve men, one for each ancestral house.", "All four columns agree; the Greek 'one man for each tribe'.",
   ["Registered by Moses and Aaron.", "And twelve leaders.", "One per house."], "Twelve men oversaw the count.", "Twelve names at the top and twelve totals at the bottom; the list closes as it opened.",
   [keeps("Greek 'one man for each tribe, according to the tribe of their ancestral houses'.")], ['moses', 'high-priest']),
  '1:45': v("All registered among Israel by ancestral houses, twenty and up, everyone who goes out for service,", "The Hebrew 'by their ancestral houses'; the Greek 'with their army'.",
   ["All registered.", "Twenty and up.", "Fit for service."], "The total was introduced.", "The sum is of soldiers; the women, children and old are not in it, and the people is several times this number.",
   [loses("Hebrew 'by their ancestral houses' is lost."), keeps("Greek 'with their army'.")]),
  '1:46': v("Six hundred three thousand five hundred fifty.", "All four columns agree; the Latin adds 'men'.",
   ["603,550.", "Fighting men.", "The whole muster."], "The total was 603,550.", "603,550, the same figure as the Exodus 38 silver count; the half-shekels and the heads agree to the man.",
   [between("The Latin adds 'men' (viros); the Greek and King James have the number alone.")]),
  '1:47': v("The Levites, by their ancestral tribe, were not registered among them.", "All four columns agree.",
   ["The Levites.", "Not registered.", "Among them."], "Levi was outside the muster.", "One tribe missing from the army; the thirteenth, Levi, is kept for another count.", [AGREE]),
  '1:48': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the Levites."],
   "YHWH spoke on the Levites.", "A new speech for the tribe left out; their exemption is as much a command as the others' enrolment.", FORMULA, ['yhwh-yahweh', 'moses']),
  '1:49': v("Only, do not register the tribe of Levi or take their census among Israel.", "All four columns agree; the Greek 'see that you do not'.",
   ["Not Levi.", "No census.", "Among Israel."], "Levi was excluded by command.", "Levi uncounted among the soldiers, as David will learn when he counts them; the tribe belongs to a different arithmetic.",
   [keeps("Greek 'See that you do not register'.")], [], "You shall not register the tribe of Levi."),
  '1:50': v("Appoint the Levites over the Dwelling of Testimony, its furnishings and all that belongs to it; they carry it, serve it, and camp around it.", "All four columns agree; 'Tent … minister therein' in Greek.",
   ["Levites over the Dwelling.", "Carry and serve it.", "Camp around it."], "The Levites kept the tabernacle.", "Their service is their soldiering: to carry the house of God and sleep around it.",
   DWELL + [keeps("Greek 'over all that is therein … minister therein'.")], ['tabernacle'], "Appoint the Levites over the Dwelling of Testimony."),
  '1:51': v("When the Dwelling sets out the Levites take it down; when it camps they erect it; any unauthorized person who approaches is put to death.",
   "All four columns agree; the Greek 'let an outsider who approaches die'. 'Outsider' means outside the authorized group, not a foreigner.",
   ["Levites take it down.", "Levites set it up.", "Outsiders die."], "Only Levites handled the tabernacle.", "The holy thing is dangerous to touch; Uzzah will die for it. 'Outsider' here is any non-Levite, Judah included.",
   DWELL + [keeps("Greek 'let an outsider who approaches die'.")], ['tabernacle'], "Any unauthorized person who approaches shall be put to death."),
  '1:52': v("Israel camps each with his camp and by his standard, by their armies.", "The Hebrew 'camp … standard'; the Greek 'formation … command'.",
   ["Each with his camp.", "By his standard.", "By armies."], "Israel camped under standards.", "A standard for each tribe: the camp is a flag-ordered square, and chapter 2 will draw it.",
   [loses("Hebrew 'each by his standard' is lost."), keeps("Greek 'each in his own formation and each according to his own command'."), between("The Latin and King James have 'standards' or 'companies'.")]),
  '1:53': v("The Levites camp around the Dwelling of Testimony so wrath does not fall on the congregation; they keep its charge.",
   "The Hebrew 'wrath'; the Greek 'offence' (hamartema) and adds 'before the Lord'. The consequence shifts from judgment to wrongdoing.",
   ["Levites around the Dwelling.", "No wrath on the congregation.", "Keeping its charge."], "Levites shielded Israel from wrath.", "A ring of Levites between the people and the Presence; they are the insulation, and the Hebrew says plainly what they insulate against: wrath.",
   DWELL + [loses("Hebrew 'so that wrath does not fall on the congregation' is lost."), keeps("Greek 'there shall be no offence among the sons of Israel … camp before the Lord'."), between("The Latin and King James have 'wrath'.")], ['tabernacle']),
  '1:54': v("Israel did all YHWH commanded Moses; so they did.", "All four columns agree; the Greek adds 'and Aaron'.",
   ["Israel did all.", "As YHWH commanded.", "So they did."], "The chapter closed in obedience.", "'So they did': the book's first chapter ends in full obedience; it will not end that way often.",
   [keeps("Greek 'commanded Moses and Aaron'.")], ['yhwh-yahweh', 'moses']),
}

for f, c, tribe, count, re_, wis in TRIBES:
    short = tribe.split(',')[0].split(' through ')[-1]
    VERSES[f'1:{f}'] = v(f"The sons of {tribe}: their descendants by clans and ancestral houses, by number of names, every male twenty and up, everyone fit for service.",
      "All four columns give the same formula; the Greek has the fuller recurring wording 'families, divisions, ancestral houses … head by head, every male'." + (" The Greek places this tribe at a different point in its list." if re_ else ""),
      [f"The sons of {short}.", "By clans and houses.", "Twenty and up, fit for service."], f"{short} was enrolled by the standard formula.",
      "The formula repeated twelve times; the monotony is the point, every tribe counted by the same rule.",
      CENSUS + (REORDER if re_ else []))
    VERSES[f'1:{c}'] = v(f"Those registered for the tribe of {short}: {count}.",
      "The figure agrees in all four columns." + (" The Greek position differs; the source calls it rearrangement, not a competing total." if re_ else ""),
      [f"The tribe of {short}.", f"{count[0].upper()+count[1:]}.", "The same in every column."], f"{short} numbered {count}.", wis,
      [between("All four columns give the same number.")] + (REORDER if re_ else []))

CHAPTER = {
 'slug': 'numbers', 'chapter': 1,
 'chapterNote': "The first census, in the wilderness of Sinai on the first day of the second month of the second year: every male of twenty and up fit for service, by clans and ancestral houses, head by head, with a named leader from each tribe (Elizur, Shelumiel, Nahshon, Nethanel, Eliab, Elishama, Gamaliel, Abidan, Ahiezer, Pagiel, Eliasaph, Ahira). The twelve totals, from Reuben's 46,500 to Naphtali's 53,400, sum to 603,550. The Levites are not counted; they are set over the Dwelling of Testimony to carry, serve and camp around it, so that wrath does not fall on the congregation, and any outsider who approaches dies. The Greek has 'Tent of Testimony' for 'Tent of Meeting' and 'Dwelling', 'Reuel' for 'Deuel' (1:14), 'commanders of thousands' (1:16), dates the assembly to 'the month of the second year' (1:18), uses a fuller census formula with 'every male' and 'divisions', lists Judah through Gad in a different order (1:24–37; the source aligns by tribe and calls it rearrangement), 'offence' for 'wrath' and 'before the Lord' at 1:53, and adds Aaron at 1:54. The Latin has 'the whole multitude' at 1:17.",
 'verses': VERSES,
}
