K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
NAQAB = [loses("Hebrew naqab, read as 'blaspheme', is lost."), keeps("Greek 'names/pronounces the Name'."), between("The Latin and King James have 'blaspheme'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'leviticus', 'chapter': 24,
 'chapterNote': "The lamps and the bread, then the blasphemer. Pure beaten oil keeps the lamp burning from evening to morning outside the curtain, arranged by Aaron on the pure lampstand; twelve cakes of two tenths each in two rows on the pure table with frankincense, renewed every Sabbath as a perpetual covenant, eaten by Aaron's sons as most holy. Then the son of an Israelite woman and an Egyptian father fights in the camp, blasphemes the Name and curses, and is held until YHWH decides: the hearers lay hands on his head and the congregation stones him outside the camp; whoever blasphemes the Name dies, foreigner or native. Attached: whoever kills a person dies, an animal is repaid life for life, injury for injury, fracture for fracture, eye for eye, tooth for tooth; one law for foreigner and native. The Greek has the oil brought 'to Me' not 'to you' (24:2), 'Aaron and his sons … burn' for 'Aaron … arrange' (24:3), 'you shall burn … until morning' (24:4), adds salt to the frankincense and lacks 'offering by fire' (24:7), 'before the sons of Israel' for 'from' (24:8), 'pronounced the Name' for 'blasphemed' (24:11, 16, which the source warns must not be read as criminalizing every utterance, since 24:11 and 15 join it to cursing), 'God' for 'his God' (24:15), adds 'and the person dies' (24:17, 21) and lacks the animal clause at 24:21.",
 'verses': {
  '24:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the lamps."],
   "YHWH spoke on the lamps and bread.", "Back into the tent after the calendar: the light that burns every night and the bread set every week, the sanctuary's own daily and weekly rhythm.", FORMULA, ['yhwh-yahweh', 'moses']),
  '24:2': v("Command Israel to bring you pure beaten olive oil for the light, to keep a lamp burning continually.", "The Hebrew 'bring you' (Moses); the Greek 'bring Me' (God). The Latin 'purest and clear'.",
   ["Pure beaten oil.", "For the light.", "A lamp continually."], "Israel supplied the lamp oil.", "The people bring the oil; the light in the holy place is lit from their olives, a continual gift that keeps a continual flame.",
   [loses("Hebrew 'bring you' is lost."), keeps("Greek 'bring Me pure beaten olive oil'."), between("The Latin and King James have 'bring unto thee'.")], ['olive-tree', 'lampstand'], "Bring pure olive oil to keep the lamp burning continually."),
  '24:3': v("Outside the curtain of the testimony in the Tent of Meeting, Aaron arranges it from evening to morning before YHWH continually; a perpetual statute.",
   "The Hebrew names Aaron alone, 'arrange', 'curtain of the testimony'; the Greek 'Aaron and his sons', 'burn', 'veil … Tent of Testimony'.",
   ["Outside the curtain.", "Aaron arranges it.", "Evening to morning."], "Aaron tended the lamp nightly.", "From evening to morning: the lamp burns while Israel sleeps, the one light in the camp that never goes out.",
   [loses("Hebrew 'Aaron shall arrange it … Tent of Meeting … curtain of the testimony' are lost."), keeps("Greek 'in the Tent of Testimony, Aaron and his sons shall burn it'."), between("The Latin and King James have 'tabernacle of the congregation' or 'testimony' and Aaron alone.")], ['high-priest', 'tabernacle', 'yhwh-yahweh']),
  '24:4': v("He arranges the lamps on the pure lampstand before YHWH continually.", "The Hebrew 'he … arrange … continually'; the Greek 'you (plural) … burn … until morning'.",
   ["The lamps arranged.", "On the pure lampstand.", "Before YHWH continually."], "The pure lampstand held the lamps.", "'Pure' lampstand, pure gold: the light stands on the costliest metal, and 'continually' is the word for both oil and gold.",
   [loses("Hebrew 'he shall arrange … continually' is lost."), keeps("Greek 'you shall burn the lamps … until morning'."), between("The Latin has 'always'; the King James 'continually'.")], ['lampstand', 'yhwh-yahweh']),
  '24:5': v("Take fine flour and bake twelve cakes, two tenths each.", "All four columns agree; 'make … loaves' in Greek.",
   ["Fine flour.", "Twelve cakes.", "Two tenths each."], "Twelve loaves were baked.", "Twelve, one for each tribe; the whole people laid on the table as bread.", [keeps("Greek 'make twelve loaves'.")], ['wheat']),
  '24:6': v("Place them in two rows of six on the pure table before YHWH.", "All four columns agree.",
   ["Two arrangements.", "Six in each.", "On the pure table."], "The bread stood in two rows.", "Two stacks of six on gold; the bread of the Presence, set where God is said to see it.", [AGREE], ['yhwh-yahweh', 'bread-of-life']),
  '24:7': v("Put pure frankincense on each row; it serves as a memorial portion for the bread, a fire offering to YHWH.",
   "The Hebrew frankincense only, 'an offering by fire'; the Greek adds salt and 'set before the Lord as a memorial for the loaves'.",
   ["Pure frankincense.", "A memorial portion.", "A fire offering."], "Frankincense made the bread an offering.", "The bread itself is not burned; the frankincense on it goes to the fire as its memorial, so the loaves can be eaten and still count as given.",
   [loses("Hebrew 'an offering by fire to YHWH' is lost."), keeps("Greek adds 'and salt' and 'set before the Lord'."), between("The Latin and King James have frankincense only.")], ['incense', 'yhwh-yahweh']),
  '24:8': v("Sabbath by Sabbath he arranges it before YHWH continually, from Israel as a perpetual covenant.", "The Hebrew 'from the sons of Israel'; the Greek 'before the sons of Israel'. The Latin 'replaced'.",
   ["Every Sabbath.", "Before YHWH continually.", "A perpetual covenant."], "The bread was renewed weekly.", "Fresh bread every Sabbath, 'a perpetual covenant'; the table is a standing agreement that God feeds and is fed.",
   [loses("Hebrew 'from the sons of Israel' is lost."), keeps("Greek 'before the sons of Israel'."), between("The Latin has 'replaced'; the King James 'taken from the children of Israel'.")], ['term-covenant', 'yhwh-yahweh'], "Sabbath by Sabbath he shall arrange it before YHWH."),
  '24:9': v("It belongs to Aaron and his sons; they eat it in a holy place, most holy from YHWH's fire offerings, a perpetual due.", "All four columns agree; offering terms differ.",
   ["Aaron's and his sons'.", "Eaten in a holy place.", "Most holy."], "The priests ate the old bread.", "The week-old bread is the priests' food; David will eat it in need, and Jesus will remember that he did.",
   [keeps("Greek 'from the things sacrificed unto the Lord'."), between("The Latin and King James have 'offerings made by fire'.")], ['high-priest', 'bread-of-life']),
  '24:10': v("The son of an Israelite woman and an Egyptian father went out among Israel, and he and an Israelite man fought in the camp.", "All four columns agree.",
   ["An Israelite woman's son.", "An Egyptian father.", "A fight in the camp."], "A half-Egyptian man fought in the camp.", "The law breaks for a story, as in chapter 10: a man of mixed birth, a fight, and a word spoken in anger.",
   [AGREE], ['egypt']),
  '24:11': v("He blasphemed the Name and cursed; they brought him to Moses. His mother was Shelomith daughter of Dibri of Dan.",
   "The Hebrew naqab read as 'blasphemed'; the Greek 'pronounced the Name'. Both have 'cursed'. The names agree.",
   ["Blasphemed the Name.", "And cursed.", "Shelomith of Dan."], "The man cursed the Name.", "'The Name', not spoken even in telling the story; his mother is named, his father's people are named, and he is called only 'the son'.",
   NAQAB, ['moses', 'divine-names']),
  '24:12': v("They put him in custody until a decision was made clear by YHWH's mouth.", "The Hebrew 'made clear to them by the mouth of YHWH'; the Greek 'to judge him by the Lord's command'.",
   ["In custody.", "Awaiting a decision.", "From YHWH's mouth."], "The case waited on God.", "No law yet covered it; Moses waits. Four times in the Torah a case is held until God speaks, and this is one.",
   [loses("Hebrew 'a decision might be made clear to them' is lost."), keeps("Greek 'to judge him by the Lord's command'."), between("The Latin has 'until they learned the command'; the King James 'that the mind of the LORD might be shewed'.")], ['yhwh-yahweh']),
  '24:13': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "The decision."],
   "YHWH gave the decision.", "The answer comes; the formula that opened laws now opens a verdict.", FORMULA, ['yhwh-yahweh', 'moses']),
  '24:14': v("Bring the curser outside the camp; all who heard lay hands on his head; the whole congregation stones him.", "All four columns agree.",
   ["Outside the camp.", "Hearers lay on hands.", "The congregation stones."], "The hearers and congregation executed him.", "Those who heard the curse lay hands on him, as on a sacrifice, giving back the word they received; then the whole people throws.", [AGREE], [], "All who heard him shall lay their hands on his head."),
  '24:15': v("Tell Israel: any man who curses his God bears his sin.", "The Hebrew 'his God'; the Greek 'God'.",
   ["Whoever curses his God.", "Bears his sin.", "A general law."], "Cursing God carried guilt.", "From the case to the rule: cursing one's God bears sin, before the Name is even mentioned.",
   [loses("Hebrew 'his God' is lost."), keeps("Greek 'a man who curses God'."), between("The Latin and King James have 'his God'.")], [], "Whoever curses his God shall bear his sin."),
  '24:16': v("One who blasphemes YHWH's name is put to death; the congregation stones him; foreigner or native, blaspheming the Name, he dies.",
   "The Hebrew naqab 'blaspheme' (also 'name'); the Greek 'names the Lord's name'. Verses 11 and 15 join it to cursing; the Greek should not be read as forbidding every reverent utterance.",
   ["Blaspheming the Name.", "Stoned.", "Foreigner or native."], "Blasphemy of the Name was capital for all.", "The Greek's 'names the Name' is the seed of the custom of never saying it; the Hebrew means cursing by it. Either way, the Name is the one word that cannot be misused and lived.",
   NAQAB, ['divine-names', 'yhwh-yahweh'], "Whoever blasphemes the Name shall be put to death."),
  '24:17': v("One who strikes down any human life is put to death.", "All four columns agree; the Greek adds 'and the person dies'.",
   ["Striking a human life.", "Death.", "For murder."], "Murder was capital.", "A life for a life; the law of Noah restated beside the law of the Name.", [keeps("Greek 'strikes a human being and the person dies'.")], [], "Whoever kills a person shall be put to death."),
  '24:18': v("One who strikes down an animal's life makes restitution, life for life.", "All four columns agree; the Greek 'and it dies'.",
   ["Striking an animal.", "Restitution.", "Life for life."], "Animal killing was repaid.", "Life for life for a beast means a beast, not a man; the formula is the same and the price is not.",
   [keeps("Greek 'strikes an animal and it dies'."), between("The Latin has 'give a replacement'.")], [], "Whoever kills an animal shall make restitution."),
  '24:19': v("A man who causes a blemish in his fellow: as he did, so it is done to him.", "All four columns agree.",
   ["Causing a blemish.", "In his fellow.", "Done to him in return."], "Injury was repaid in kind.", "'As he has done': the law of measure; the injurer learns what he did by receiving it.", [AGREE]),
  '24:20': v("Fracture for fracture, eye for eye, tooth for tooth; as he blemished a person, so it is inflicted on him.", "All four columns agree; the enforcement is a reception question.",
   ["Fracture for fracture.", "Eye for eye.", "Tooth for tooth."], "The formula of equivalence was stated.", "Eye for eye: a ceiling, not a floor, limiting vengeance to the size of the wound; later readers made it a price and Jesus made it a mercy.", [AGREE]),
  '24:21': v("One who strikes an animal repays; one who strikes a human is put to death.", "The Hebrew has both clauses; the Greek only the human, with 'and the person dies'.",
   ["An animal repaid.", "A human put to death.", "Restated."], "The two penalties were set side by side.", "The pair said again, so no one confuses them: property is repaid, a person is avenged.",
   [loses("Hebrew 'one who strikes down an animal shall make restitution' is lost."), keeps("Greek 'one who strikes a human being and the person dies shall surely be put to death'."), between("The Latin and King James have both clauses.")]),
  '24:22': v("One judgment for foreigner and native alike, for I am YHWH your God.", "All four columns agree.",
   ["One judgment.", "Foreigner and native.", "I am YHWH."], "The law was one for all residents.", "One law, because the blasphemer was half Egyptian: the story's point is that his father's people did not exempt him or condemn him; the law is the same for all.", [AGREE], ['yhwh-yahweh'], "You shall have one judgment for foreigner and native."),
  '24:23': v("Moses spoke to Israel; they brought the curser outside the camp and stoned him; Israel did as YHWH commanded Moses.", "All four columns agree.",
   ["Moses spoke.", "They stoned him.", "As YHWH commanded."], "The sentence was carried out.", "The story closes as it must; the Name is defended by the people who heard it misused, and the law stands written beside the grave.", [AGREE], ['moses', 'yhwh-yahweh']),
 },
}
