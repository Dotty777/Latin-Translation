K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
CENSER = [keeps("Greek 'fire pans'."), between("The Hebrew, Latin and King James have 'censers'.")]
NUM = [between("The site follows the Greek chapter division: this chapter's 17:1–15 are the Hebrew and English 16:36–50, and 17:16–28 are English 17:1–13.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 17,
 'chapterNote': "The aftermath of Korah and the budding staff. (The site follows the Greek division: 17:1–15 here are English 16:36–50.) Eleazar gathers the bronze censers of the burned men and hammers them into a covering for the altar, a sign that no outsider may offer incense. Next day the congregation accuses Moses and Aaron of killing YHWH's people; the glory appears, wrath goes out, and Aaron runs with a censer of altar fire and incense into the assembly and stands between the dead and the living until the plague stops at 14,700. Then twelve staffs, one per tribe, Aaron's for Levi, are laid before the testimony; Aaron's alone buds, flowers and bears almonds, and is kept as a sign; the people cry that everyone who approaches the Dwelling dies. The Greek addresses Eleazar directly and adds 'bronze … strange fire … there' (17:2), 'became a sign' (17:3), 'applied' without hammering (17:4), 'place incense … faction' (17:5), omits 'the whole congregation' (17:6), 'rushed toward' for 'turned toward' (17:7), adds Aaron as addressee (17:9) and witness (17:23) and actor (17:26), 'into the camp … strike the people' for 'to the congregation … the plague' (17:11), 'each tribe shall give' (17:18), 'make Myself known unto you' singular for 'meet with you' plural (17:19), 'nuts … sprouted' for 'almonds … ripened' (17:23), 'testimonies' and 'sons of the disobedient' (17:25), a third exclamation (17:27), and 'touches the tent' for 'approaches the Dwelling' (17:28). The Latin at 17:21 sets Aaron's staff beside the twelve rather than among them.",
 'verses': {
  '17:1': v("YHWH spoke to Moses.", "All four columns agree; the Greek runs on to add Eleazar. English 16:36.",
   ["YHWH speaks.", "To Moses.", "On the censers."], "God spoke after the fire.", "The fire has done its work and the censers lie in the ash; God speaks about what to do with holy metal.", FORMULA + NUM, ['yhwh-yahweh', 'moses']),
  '17:2': v("Tell Eleazar son of Aaron to lift the censers from the burning and scatter the fire far away, for the censers have become holy.", "The Greek addresses Eleazar directly, adds 'bronze' and 'strange fire', and 'there' for 'far away'.",
   ["Eleazar lifts the censers.", "Scatters the fire.", "They are holy."], "The censers had become holy.", "Eleazar, not Aaron, handles the dead men's pans; the high priest may not touch what the dead held. And the censers are holy: offered to God wrongly, they are still offered.",
   CENSER + [loses("Hebrew 'tell Eleazar … scatter the fire far away' is lost."), keeps("Greek 'and to Eleazar … the bronze fire pans … scatter this strange fire there'.")], ['high-priest', 'incense']),
  '17:3': v("The censers of these men who sinned at the cost of their lives: hammer them into sheets to cover the altar; because they were presented before YHWH they became holy, and are a sign to Israel.", "The Greek 'became a sign' for 'shall be a sign'; its subject runs on from 17:2.",
   ["The sinners' censers.", "Hammered onto the altar.", "A sign to Israel."], "The censers plated the altar.", "The rebels' censers become the altar's skin: every sacrifice from now on burns on the metal of the men who wanted the priesthood. The warning is built into the furniture.",
   CENSER + [keeps("Greek 'and became a sign to the sons of Israel'.")], ['altar']),
  '17:4': v("Eleazar took the bronze censers of those burned and they hammered them into a covering for the altar,", "All four columns agree; the Greek 'applied' without repeating the hammering.",
   ["Eleazar took them.", "Bronze censers.", "A covering for the altar."], "The altar was plated.", "Done: the altar wears the rebellion.", CENSER + [keeps("Greek 'Eleazar son of Aaron … applied them'.")], ['high-priest', 'altar']),
  '17:5': v("A reminder that no outsider not of Aaron's line should approach to burn incense before YHWH, lest he become like Korah and his company, as YHWH said through Moses.", "The Greek 'place incense … faction' and lacks 'to him'. Outsider is defined by descent.",
   ["A reminder.", "No outsider offers incense.", "Lest like Korah."], "Incense was Aaron's line's alone.", "'Lest he become like Korah': Korah's name is now a warning hammered into bronze; Uzziah the king will forget it and be struck with leprosy at the incense altar.",
   [keeps("Greek 'to place incense … Korah and his faction'.")], ['incense', 'high-priest']),
  '17:6': v("The next day the whole congregation grumbled against Moses and Aaron: you have put YHWH's people to death!", "The Greek omits 'the whole congregation'.",
   ["The next day.", "Grumbling.", "You killed YHWH's people!"], "The people blamed the leaders.", "Two hundred and fifty burned, three families swallowed, and the next morning the people blame Moses. 'YHWH's people', they say of Korah's dead.",
   [loses("Hebrew 'the whole Israelite congregation' is lost."), keeps("Greek 'the sons of Israel'.")], ['moses', 'high-priest']),
  '17:7': v("When the congregation assembled against Moses and Aaron they turned toward the Tent of Meeting; the cloud covered it and YHWH's glory appeared.", "The Hebrew 'turned toward'; the Greek 'rushed toward'.",
   ["Assembled against them.", "Toward the tent.", "The glory appeared."], "God intervened again.", "A mob at the tent and the cloud comes down; the pattern of chapters 14 and 16 a third time.",
   TENT + [loses("Hebrew 'turned toward' is lost."), keeps("Greek 'rushed toward the Tent of Testimony'."), between("The Latin has 'fled in'.")], ['tabernacle', 'yhwh-yahweh']),
  '17:8': v("Moses and Aaron came before the Tent of Meeting.", "All four columns agree; the Greek 'into the area before'.",
   ["Moses and Aaron.", "Came before.", "The tent."], "The leaders went to the tent.", "The two accused go to the door, where God is.", TENT + [keeps("Greek 'came into the area before the Tent'.")], ['moses', 'high-priest']),
  '17:9': v("YHWH spoke to Moses.", "The Hebrew Moses alone; the Greek 'Moses and Aaron'.", ["YHWH speaks.", "To Moses.", "On the congregation."],
   "God spoke in the crisis.", "The word comes fast; there is no time for a formula.", FORMULA + [keeps("Greek adds 'and Aaron'.")], ['yhwh-yahweh', 'moses']),
  '17:10': v("Withdraw from this congregation and I will consume them in a moment. They fell on their faces.", "All four columns agree.",
   ["Withdraw.", "I will consume them.", "They fell on their faces."], "God threatened and the leaders pleaded.", "The same words as 16:21 and the same answer; Moses and Aaron on their faces for the third time in two chapters.", [AGREE]),
  '17:11': v("Moses said to Aaron: take the censer, put altar fire and incense on it, carry it quickly to the congregation and atone for them, for wrath has gone out from YHWH; the plague has begun.", "The Hebrew 'to the congregation … the plague'; the Greek 'into the camp … strike the people'.",
   ["Take the censer.", "Altar fire and incense.", "Run and atone; the plague has begun."], "Moses sent Aaron with incense.", "Incense, the thing the 250 died for, is now the thing that saves; the same smoke in the right hands turns wrath. Moses does not pray this time; he acts.",
   CENSER + [loses("Hebrew 'to the congregation … the plague has begun' is lost."), keeps("Greek 'into the camp … it has begun to strike the people'.")], ['high-priest', 'incense', 'altar', 'yhwh-yahweh'], "Take the censer and make atonement for them quickly."),
  '17:12': v("Aaron took it as Moses said and ran into the assembly; the plague had begun; he put on the incense and atoned for the people.", "All four columns agree.",
   ["Aaron ran.", "The plague had begun.", "Incense and atonement."], "Aaron ran into the plague.", "The high priest running: the only time Aaron runs in Scripture, into a dying crowd with a pan of coals.", [AGREE], ['high-priest', 'incense']),
  '17:13': v("He stood between the dead and the living, and the plague was stopped.", "All four columns agree.",
   ["Between the dead and the living.", "He stood.", "The plague stopped."], "Aaron's incense halted the plague.", "'Between the dead and the living': the whole office of a priest in one posture. Where he stands, the dying stops.", [AGREE], ['high-priest', 'mediator']),
  '17:14': v("Those who died in the plague were 14,700, apart from those who died in Korah's affair.", "All four columns agree.",
   ["14,700 dead.", "In the plague.", "Besides Korah's."], "The plague killed 14,700.", "Fourteen thousand seven hundred for one morning's grumbling; the camp's second census is being taken by death.", [AGREE]),
  '17:15': v("Aaron returned to Moses at the Tent of Meeting's entrance, and the plague was stopped.", "All four columns agree. English 16:50 ends here.",
   ["Aaron returned.", "To the entrance.", "The plague stopped."], "The crisis ended at the tent door.", "Back to the door with an empty censer; the chapter's first half ends where it began, at the altar, with Aaron proved.", TENT + NUM, ['high-priest', 'tabernacle']),
  '17:16': v("YHWH speaks to Moses.", "All four columns agree. English 17:1.", ["YHWH speaks.", "To Moses.", "On the staffs."],
   "God proposed a quieter proof.", "After fire, earth and plague, a sign that kills no one: a stick that flowers.", FORMULA + NUM, ['yhwh-yahweh', 'moses']),
  '17:17': v("Speak to Israel and take a staff for each ancestral house from all their leaders, twelve staffs; write each man's name on his staff.", "All four columns agree.",
   ["Twelve staffs.", "One per house.", "Each name written."], "Twelve named staffs were gathered.", "Twelve dead sticks with names on them; the test is which one God can make live.", [AGREE]),
  '17:18': v("Write Aaron's name on Levi's staff, for there is one staff for the head of each ancestral house.", "The Greek 'each tribe shall give one staff'.",
   ["Aaron's name.", "On Levi's staff.", "One per house."], "Levi's staff bore Aaron's name.", "Levi's staff is Aaron's: the tribe's claim and the priest's are one stick, and Korah's distinction between them is erased.",
   [keeps("Greek 'they shall give one staff for each tribe'.")], ['high-priest']),
  '17:19': v("Place them in the Tent of Meeting before the testimony, where I meet with you.", "The Hebrew 'meet with you' plural; the Greek 'make Myself known unto you' singular.",
   ["In the tent.", "Before the testimony.", "Where I meet you."], "The staffs lay before the ark.", "Before the testimony, the tablets in the ark; the sticks spend the night with the law.",
   TENT + [loses("Hebrew 'where I will meet with you' (plural) is lost."), keeps("Greek 'where I will make Myself known unto you' (singular).")], ['ark-of-the-covenant', 'tabernacle']),
  '17:20': v("The staff of the man I choose will blossom; I will quiet Israel's complaints against me, which they grumble against you.", "All four columns agree.",
   ["The chosen staff blossoms.", "Complaints quieted.", "Against me, against you."], "A flower would settle it.", "'Against Me … against you': God names himself the true target of every grumble at Moses, and promises to end it with a blossom.", [AGREE], ['yhwh-yahweh']),
  '17:21': v("Moses spoke to Israel and the leaders gave him staffs, one per leader, twelve; Aaron's staff was among them.", "The Hebrew, Greek and King James agree; the Latin sets Aaron's staff beside the twelve.",
   ["Twelve staffs given.", "One per leader.", "Aaron's among them."], "The staffs were collected.", "'Among their staffs': twelve, with Aaron's counted in; the Latin made it a thirteenth, and the number has been argued since.",
   [between("The Latin has Aaron's staff besides the twelve; the Greek and King James among them.")], ['high-priest', 'moses']),
  '17:22': v("Moses placed the staffs before YHWH in the Tent of Testimony.", "All four columns agree; the Hebrew itself has 'Tent of Testimony' here.",
   ["Moses placed them.", "Before YHWH.", "In the Tent of Testimony."], "The staffs lay overnight.", "The Hebrew uses the Greek's name for the tent here, 'Tent of Testimony'; for once the columns agree on the title.", [AGREE], ['tabernacle', 'yhwh-yahweh']),
  '17:23': v("Next day Moses entered the Tent of Testimony, and Aaron's staff for the house of Levi had blossomed: buds, flowers, and ripe almonds.", "The Greek adds Aaron, has 'sprouted … nuts' for 'blossomed … ripened almonds'.",
   ["Next day.", "Aaron's staff blossomed.", "Buds, flowers, almonds."], "Aaron's staff bore almonds.", "Bud, flower and fruit on one dead stick overnight, a whole almond year in a night; the almond is the first tree to flower in the land, and its name means 'watchful'.",
   [loses("Hebrew 'Moses entered … ripened almonds' is lost."), keeps("Greek 'Moses and Aaron entered … sprouted … produced nuts'."), between("The Latin has Moses alone and 'leaves'; the King James 'almonds'.")], ['high-priest', 'moses']),
  '17:24': v("Moses brought all the staffs from before YHWH to all Israel; they looked, and each man took his staff.", "All four columns agree.",
   ["Moses brought them out.", "They looked.", "Each took his own."], "The proof was shown to all.", "Eleven dry sticks handed back and one in flower; the leaders take their staffs home and the argument is over.", [AGREE], ['moses']),
  '17:25': v("YHWH said to Moses: return Aaron's staff before the testimony, kept as a sign for the rebellious; end their complaints against me, so they do not die.", "The Greek 'testimonies … sons of the disobedient' and makes the cessation the subject.",
   ["Return Aaron's staff.", "A sign for the rebellious.", "So they do not die."], "The staff was kept in the ark's room.", "Kept before the ark with the manna jar: the budded staff is Israel's second memorial of mercy, and Hebrews 9 puts it inside the ark.",
   [loses("Hebrew 'the testimony … the rebellious' is lost."), keeps("Greek 'before the testimonies … the sons of the disobedient'.")], ['ark-of-the-covenant', 'high-priest'], "Return Aaron's staff before the testimony as a sign."),
  '17:26': v("Moses did so; as YHWH commanded him, so he did.", "The Hebrew Moses alone; the Greek 'Moses and Aaron'.",
   ["Moses did so.", "As commanded.", "So he did."], "Moses obeyed.", "The formula, with the Greek bringing Aaron into it.", [keeps("Greek 'Moses and Aaron did so'.")], ['moses']),
  '17:27': v("Israel said to Moses: look, we are dying! we are lost! all of us are lost!", "The Hebrew repeats 'lost … all of us'; the Greek has three exclamations.",
   ["We are dying!", "We are lost!", "All of us!"], "The people despaired.", "Not repentance but panic: three cries, and the people who would not keep their distance now fear they cannot survive the nearness.",
   [keeps("Greek 'we are consumed! We are lost! We are utterly spent!'.")], ['moses']),
  '17:28': v("Everyone who approaches YHWH's Dwelling dies; are we all to perish?", "The Hebrew 'approaches … Dwelling'; the Greek 'touches the Lord's tent'.",
   ["Who approaches dies.", "YHWH's Dwelling.", "Must we all perish?"], "The people feared the sanctuary itself.", "The right fear at last: the holy place kills, and the answer to 'are we all to perish?' is the next chapter, where the priests are set to stand between.",
   [loses("Hebrew 'who approaches, who approaches YHWH's Dwelling' is lost."), keeps("Greek 'who touches the Lord's tent'."), between("The Latin and King James have 'cometh near'.")], ['tabernacle', 'yhwh-yahweh']),
 },
}
