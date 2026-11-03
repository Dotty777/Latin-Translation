K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
PLURAL = [loses("Hebrew plural 'brothers' is lost."), keeps("Greek singular 'brother'."), between("The Latin has the plural; the King James 'brethren'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 27,
 'chapterNote': "Two successions. Zelophehad's five daughters stand before Moses, Eleazar and the congregation: their father died for his own sin, not Korah's, and had no son; why should his name be erased? Moses brings it to YHWH, who says they speak rightly, and makes it law: daughter, then brothers, then father's brothers, then nearest kin. Then YHWH tells Moses to climb Abarim, see the land, and be gathered like Aaron, for Meribah; Moses asks the God of the spirits of all flesh for a shepherd so the people are not sheep without one, and is told to take Joshua, a man with spirit in him, lay his hand on him before Eleazar and the people, give him some of his majesty, and have Eleazar inquire for him by the Urim. Moses does so. The Greek compresses the ancestry (27:1), has a prohibition for the question at 27:4, singulars 'brother … father's brother' (27:9–10), 'tribe' for 'clan' and 'rule of judgment' (27:11), names Mount Nebo and Canaan (27:12), adds 'at Mount Hor' (27:13), expands 'you did not sanctify Me' (27:14), 'God of spirits and of all flesh' (27:16), 'hands' for 'hand' and 'spirit within him' (27:18), adds instruction to and about Joshua (27:19), 'glory … obey him' (27:20), 'they shall ask him for the judgment of the manifestations' for 'he shall inquire for him by the Urim' (27:21), and 'presented' for 'commissioned' (27:23).",
 'verses': {
  '27:1': v("The daughters of Zelophehad son of Hepher, son of Gilead, son of Machir, son of Manasseh, of Manasseh's clans, came forward: Mahlah, Noah, Hoglah, Milcah, Tirzah.", "The Greek compresses, lacking the separate 'son of Manasseh'.",
   ["Zelophehad's daughters.", "Of Manasseh.", "Five names."], "Five sisters brought a case.", "Five women walk to the front of a nation of men with a legal question; the census named them in passing, and now they speak.",
   [loses("Hebrew 'son of Manasseh, of the clans of Manasseh' is lost."), keeps("Greek 'of the clan of Manasseh among the sons of Joseph'.")], ['joseph-son-of-jacob']),
  '27:2': v("They stood before Moses, Eleazar the priest, the leaders and the whole congregation at the Tent of Meeting's entrance:", "All four columns agree in substance.",
   ["Before Moses and Eleazar.", "The leaders and all.", "At the tent."], "The case was public.", "At the door of the tent, before everyone: the sisters do not petition privately but make the law in public.", TENT, ['moses', 'high-priest', 'tabernacle']),
  '27:3': v("Our father died in the wilderness; he was not in Korah's company against YHWH but died for his own sin, and had no sons.", "All four columns agree; the sin is not specified.",
   ["Our father died.", "Not with Korah.", "He had no sons."], "They cleared their father's name.", "'He died for his own sin': the ordinary death of the wilderness generation, not the rebel's; the daughters distinguish the two before asking anything.", [AGREE], ['yhwh-yahweh']),
  '27:4': v("Why should our father's name be removed from his clan because he had no son? give us a possession among our father's brothers.", "The Hebrew asks why; the Greek 'let it not be erased'.",
   ["Why remove his name?", "Because no son?", "Give us a possession."], "They claimed their father's share.", "'Why should his name be erased?' The plea is for the father's name, not their own fortune; a dead man's place in the land depends on his daughters' nerve.",
   [loses("Hebrew 'Why should our father's name be removed' is lost."), keeps("Greek 'Let our father's name not be erased'.")]),
  '27:5': v("Moses brought their case before YHWH.", "All four columns agree.", ["Moses brought it.", "Their case.", "Before YHWH."],
   "Moses sought a ruling.", "The fourth case held for God's word; Moses has no law for daughters, and does not invent one.", [AGREE], ['moses', 'yhwh-yahweh']),
  '27:6': v("YHWH said to Moses:", "All four columns agree.", ["YHWH speaks.", "To Moses.", "The ruling."],
   "God ruled.", "The answer, and it is in the women's favour.", [AGREE], ['yhwh-yahweh', 'moses']),
  '27:7': v("Zelophehad's daughters speak rightly; give them an inherited possession among their father's brothers and transfer their father's inheritance to them.", "All four columns agree.",
   ["They speak rightly.", "Give them a possession.", "Their father's inheritance."], "The daughters won.", "'They speak rightly': God agrees with five women against the assumptions of a whole legal system, and the law of Israel changes because they asked.", [AGREE], [], "Give them an inherited possession among their father's brothers."),
  '27:8': v("Tell Israel: if a man dies without a son, transfer his inheritance to his daughter.", "All four columns agree.",
   ["No son.", "His inheritance.", "To his daughter."], "Daughters could inherit.", "From a case to a statute: every daughter in Israel inherits where there is no son, because of Mahlah and her sisters.", [AGREE], [], "If a man dies without a son, transfer his inheritance to his daughter."),
  '27:9': v("If no daughter, give his inheritance to his brothers.", "The Hebrew plural; the Greek singular.",
   ["No daughter.", "To his brothers.", "Next in line."], "Brothers came next.", "The order of succession begins; the land must stay in the family.", PLURAL),
  '27:10': v("If no brothers, to his father's brothers.", "The Hebrew plural; the Greek singular.",
   ["No brothers.", "His father's brothers.", "Next."], "Uncles came next.", "Up a generation and across; the inheritance climbs the tree looking for a male.", PLURAL),
  '27:11': v("If his father has no brothers, to his nearest relative in his clan, who possesses it. A legal statute for Israel, as YHWH commanded Moses.", "The Hebrew 'clan'; the Greek 'tribe' and 'a rule of judgment'.",
   ["No uncles.", "The nearest kin.", "A legal statute."], "The nearest kinsman was the last heir.", "The nearest kin, the go'el of Leviticus 25: the land never leaves the clan. Chapter 36 will add that the daughters must marry within it.",
   [loses("Hebrew 'within his clan … a legal statute' is lost."), keeps("Greek 'from his tribe … a rule of judgment'.")], ['redeemer']),
  '27:12': v("YHWH said to Moses: go up this mountain of Abarim and see the land I have given Israel.", "The Hebrew 'Abarim'; the Greek 'the mountain on the farther side, this is Mount Nebo … Canaan … as a possession'.",
   ["Go up Abarim.", "See the land.", "Given to Israel."], "Moses was told to look at the land.", "'See the land': the sight is Moses' whole portion of it. Deuteronomy 34 will tell the climb; here the order is given, and the law goes on.",
   [loses("Hebrew 'this mountain of Abarim' is lost."), keeps("Greek 'the mountain on the farther side—this is Mount Nebo—and see the land of Canaan … as a possession'.")], ['moses', 'canaan']),
  '27:13': v("When you have seen it, you too will be gathered to your people, as your brother Aaron was gathered.", "The Greek adds 'at Mount Hor'.",
   ["See it.", "Be gathered.", "Like Aaron."], "Moses' death was announced.", "'You too': the sentence of Meribah, said gently. Moses will see what Aaron did not, and die on a mountain like him.",
   [keeps("Greek adds 'at Mount Hor'.")], ['high-priest']),
  '27:14': v("Because you rebelled against my command in Zin at the congregation's dispute, about showing me holy through the water; these are the waters of Meribah at Kadesh.", "The Greek adds 'you did not sanctify Me' and 'Water of Dispute'.",
   ["You rebelled.", "At the waters of Meribah.", "Not showing me holy."], "The reason was Meribah.", "The reason given again, and it is still the rock; forty years of faithfulness do not cancel one blow, and the text does not soften it.",
   [keeps("Greek 'transgressed My word … you did not sanctify Me at the water … the Water of Dispute'.")]),
  '27:15': v("Moses spoke to YHWH:", "All four columns agree.", ["Moses spoke.", "To YHWH.", "A request."],
   "Moses answered with a request.", "Told he will die, Moses asks nothing for himself; his reply is about the people.", [AGREE], ['moses', 'yhwh-yahweh']),
  '27:16': v("Let YHWH, the God of the spirits of all flesh, appoint a man over the congregation,", "The Hebrew 'the spirits of all flesh'; the Greek 'spirits and of all flesh'.",
   ["God of all spirits.", "Appoint a man.", "Over the congregation."], "Moses asked for a successor.", "'God of the spirits of all flesh', the title from 16:22 when Moses pleaded for the people; he uses it again to ask who will plead after him.",
   [keeps("Greek 'the God of spirits and of all flesh'.")], ['elohim', 'term-pneuma-ruach']),
  '27:17': v("Who goes out and comes in before them, leads them out and brings them in, so YHWH's congregation is not like sheep without a shepherd.", "All four columns agree. Mark uses the image of Jesus.",
   ["Go out and come in.", "Lead them.", "Not sheep without a shepherd."], "Moses wanted a shepherd for Israel.", "'Sheep without a shepherd': the old shepherd's fear for his flock, and the phrase Jesus will see in a Galilean crowd. Moses asks to be replaced.", [AGREE], ['good-shepherd', 'yhwh-my-shepherd']),
  '27:18': v("YHWH said to Moses: take Joshua son of Nun, a man in whom there is spirit, and lay your hand on him.", "The Hebrew 'hand' singular, 'in whom there is spirit'; the Greek 'hands … spirit within him'.",
   ["Take Joshua.", "A man with spirit.", "Lay your hand on him."], "Joshua was named.", "Joshua, the scout who said yes, the attendant who wanted the prophets silenced; 'a man in whom there is spirit', which is the only qualification named.",
   [loses("Hebrew 'lay your hand' is lost."), keeps("Greek 'you shall lay your hands upon him … spirit within him'.")], ['joshua', 'spirit-god-lord'], "Take Joshua son of Nun and lay your hand on him."),
  '27:19': v("Stand him before Eleazar the priest and the whole congregation, and commission him before their eyes.", "The Greek adds instruction to Joshua and instructions about him.",
   ["Before Eleazar.", "Before the congregation.", "Commission him."], "The commissioning was public.", "Before the priest and the people, in the open; Joshua's authority is seen being given, so it cannot be doubted later.",
   [keeps("Greek 'shall instruct him before all the congregation, and shall give instructions concerning him'.")], ['high-priest', 'joshua']),
  '27:20': v("Put some of your majesty on him, so the whole congregation obeys.", "The Hebrew 'majesty … the whole congregation'; the Greek 'glory … obey him'.",
   ["Some of your majesty.", "On him.", "That they obey."], "Moses shared his authority.", "'Some of your majesty', as 'some of the Spirit' went to the seventy; Moses is divided again, and does not shrink.",
   [loses("Hebrew 'majesty … the whole congregation of the sons of Israel may obey' is lost."), keeps("Greek 'of your glory … that the sons of Israel may obey him'.")], ['moses']),
  '27:21': v("He stands before Eleazar, who inquires for him by the judgment of the Urim before YHWH; at his word they go out and come in, he and all Israel.", "The Hebrew: Eleazar inquires for Joshua; the Greek: 'they shall ask him for the judgment of the manifestations'.",
   ["Before Eleazar.", "The Urim's judgment.", "At his word they go."], "Joshua would rule with the priest's oracle.", "Joshua is not Moses: he does not speak with God mouth to mouth but asks through Eleazar's Urim. The leadership is split between a soldier and a priest.",
   [loses("Hebrew 'who shall inquire for him by the judgment of the Urim' is lost."), keeps("Greek 'they shall ask him for the judgment of the manifestations (dela)'.")], ['high-priest', 'breastpiece', 'joshua']),
  '27:22': v("Moses did as YHWH commanded; he took Joshua and stood him before Eleazar and the whole congregation.", "All four columns agree.",
   ["Moses did so.", "Took Joshua.", "Before Eleazar and all."], "Moses obeyed.", "Done; the man who asked to be replaced installs his replacement himself.", [AGREE], ['moses', 'joshua', 'high-priest']),
  '27:23': v("He laid his hands on him and commissioned him, as YHWH had spoken through Moses.", "The Hebrew 'commissioned … spoken through Moses'; the Greek 'presented … commanded Moses'.",
   ["Laid his hands.", "Commissioned him.", "As YHWH spoke."], "Joshua was commissioned.", "Both hands, where God said one: Moses gives more than he was told. The succession is done, and the rest of the book Moses leads with his heir beside him.",
   [loses("Hebrew 'commissioned him, as YHWH had spoken through Moses' is lost."), keeps("Greek 'presented him, as the Lord had commanded Moses'.")], ['moses', 'joshua']),
 },
}
