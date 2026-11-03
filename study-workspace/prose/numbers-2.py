K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
STD = [loses("Hebrew 'standard' (degel) is lost."), keeps("Greek 'formation' (tagma) … 'with their army'."), between("The Latin and King James have 'standard' or 'companies'.")]
NEXT = [keeps("Greek supplies the recurring 'those camping next' formula where the Hebrew has only 'and the tribe of'."), between("The Latin and King James follow the Hebrew.")]
SAME = [between("All four columns give the same number.")]
ARMY = [between("The Latin adds 'by their companies'; the Greek 'with their army'; the King James 'throughout their armies'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

def count(ref, tribe, n, wis):
    return v(f"His army, those registered: {n}.", "All four columns give the same figure; 'his stock' / 'his army' is wording.",
      [f"{tribe}'s army.", f"{n[0].upper()+n[1:]}.", "The same in every column."], f"{tribe}'s army was {n}.", wis, SAME)

def nxt(ref, tribe, leader, father, hebrew_short, wis):
    exp = "All four columns agree." if not hebrew_short else "The Hebrew has only 'and the tribe of'; the Greek supplies 'those camping next'."
    return v(f"{'Beside him' if not hebrew_short else 'And'} the tribe of {tribe}; its leader {leader} son of {father}.", exp,
      [f"The tribe of {tribe}.", f"Leader {leader}.", f"Son of {father}."], f"{tribe} camped in this division under {leader}.", wis, NEXT if hebrew_short else [AGREE])

VERSES = {
  '2:1': v("YHWH speaks to Moses and Aaron.", "All four columns agree.", ["YHWH speaks.", "To Moses and Aaron.", "On the camp."],
   "YHWH spoke on the camp's order.", "Both brothers addressed: the camp is a matter for the priest as much as the leader, since its centre is the tent.", FORMULA, ['yhwh-yahweh', 'moses', 'high-priest']),
  '2:2': v("Israel camps each by his standard with the signs of their ancestral houses, at a distance around the Tent of Meeting.",
   "The Hebrew 'standard … at a distance'; the Greek 'each beside his neighbour, by formation … opposite'; the Latin 'companies, standards, banners'.",
   ["Each by his standard.", "Signs of their houses.", "Around the tent."], "The camp was a square around the tent.", "A square of tribes with God in the middle, at a distance: close enough to see the cloud, far enough to live. The camp is a map of the covenant.",
   TENT + STD + [keeps("Greek 'each beside his neighbour … opposite'.")], ['tabernacle'], "They shall camp around the Tent of Meeting."),
  '2:3': v("On the east toward sunrise, the standard of Judah's camp by armies; Judah's leader Nahshon son of Amminadab.", "The Hebrew 'toward sunrise'; the Greek 'first'.",
   ["East, toward sunrise.", "Judah's standard.", "Nahshon leads."], "Judah held the east.", "Judah faces the sunrise and the door of the tent, which opens east; the tribe of the king is placed at the entrance.",
   STD + [loses("Hebrew 'toward sunrise' is lost."), keeps("Greek 'those camping first toward the east'.")], ['david']),
  '2:4': count('2:4', 'Judah', 'seventy-four thousand six hundred', "The same number as chapter 1; the census and the camp agree."),
  '2:5': nxt('2:5', 'Issachar', 'Nethanel', 'Zuar', False, "Issachar at Judah's side, as Leah's sons stay together on the east."),
  '2:6': count('2:6', 'Issachar', 'fifty-four thousand four hundred', "Each tribe's number is read out again at its place; the camp is a census made visible."),
  '2:7': nxt('2:7', 'Zebulun', 'Eliab', 'Helon', True, "Zebulun completes the east with his brothers; three sons of Leah under one standard."),
  '2:8': count('2:8', 'Zebulun', 'fifty-seven thousand four hundred', "Fifty-seven thousand on the sunrise side with Judah and Issachar."),
  '2:9': v("All registered in Judah's camp by armies: 186,400. They set out first.", "All four columns agree on total and order.",
   ["Judah's camp.", "186,400.", "First to march."], "Judah's division led the march.", "The largest division and the first to move: the east side breaks camp before the tent is even lifted.", ARMY, [], "They shall set out first."),
  '2:10': v("The standard of Reuben's camp by armies on the south; Reuben's leader Elizur son of Shedeur.", "The Hebrew 'south'; the Greek lips 'southwest'.",
   ["South.", "Reuben's standard.", "Elizur leads."], "Reuben held the south.", "Reuben, the firstborn, on the right hand of the tent as one faces east; honoured with a side but not with the lead.",
   STD + [loses("Hebrew 'on the south' is lost."), keeps("Greek 'toward the southwest' (lips)."), between("The Latin and King James have 'south'.")]),
  '2:11': count('2:11', 'Reuben', 'forty-six thousand five hundred', "Reuben's number, the firstborn's, is middling; the standard is his but the strength is Judah's."),
  '2:12': nxt('2:12', 'Simeon', 'Shelumiel', 'Zurishaddai', False, "Simeon beside Reuben: the two eldest together on the south, as they were together in the Dinah affair."),
  '2:13': count('2:13', 'Simeon', 'fifty-nine thousand three hundred', "Simeon larger than Reuben here; the second census will reverse that savagely."),
  '2:14': nxt('2:14', 'Gad', 'Eliasaph', 'Reuel', True, "Gad, Zilpah's son, grouped with Leah's eldest; Reuel here where 1:14 had Deuel, in the Hebrew itself."),
  '2:15': count('2:15', 'Gad', 'forty-five thousand six hundred fifty', "The fifty again; the one unrounded tribe."),
  '2:16': v("All registered in Reuben's camp by armies: 151,450. They set out second.", "All four columns agree.",
   ["Reuben's camp.", "151,450.", "Second to march."], "Reuben's division marched second.", "Second: the south follows the east, and then the Levites with the tent come between the halves.", ARMY, [], "They shall set out second."),
  '2:17': v("Then the Tent of Meeting, the Levites' camp, sets out in the middle of the camps; as they camp so they march, each in place by standards.",
   "All four columns agree on the central position; the Greek 'shall be raised' and 'each beside his neighbour according to command'; the Latin 'through the Levites' duties'.",
   ["The tent in the middle.", "The Levites' camp.", "As they camp, so they march."], "The tabernacle moved at the centre.", "God in the middle of the column as in the middle of the square; the camp does not change shape when it moves, only stretches.",
   TENT + STD + [keeps("Greek 'the Tent of Testimony and the camp of the Levites shall be raised in the middle'.")], ['tabernacle']),
  '2:18': v("The standard of Ephraim's camp by armies on the west; Ephraim's leader Elishama son of Ammihud.", "The Hebrew yammah 'seaward' and the Greek thalassa both mean west.",
   ["West.", "Ephraim's standard.", "Elishama leads."], "Ephraim held the west.", "West, 'toward the sea', behind the tent: Joseph's house has the rear of the holy place, and Rachel's sons are together.",
   STD + [keeps("Greek 'toward the sea'."), between("The Latin and King James have 'west'.")], ['joseph-son-of-jacob']),
  '2:19': count('2:19', 'Ephraim', 'forty thousand five hundred', "Ephraim small now; the tribe that will name the northern kingdom starts at forty thousand."),
  '2:20': nxt('2:20', 'Manasseh', 'Gamaliel', 'Pedahzur', False, "Manasseh beside Ephraim, the elder beside the younger who leads him."),
  '2:21': count('2:21', 'Manasseh', 'thirty-two thousand two hundred', "The smallest number in the camp; Manasseh has the most growing to do."),
  '2:22': nxt('2:22', 'Benjamin', 'Abidan', 'Gideoni', True, "Benjamin with Joseph's sons on the west: Rachel's three grandsons and son together behind the tent."),
  '2:23': count('2:23', 'Benjamin', 'thirty-five thousand four hundred', "Benjamin's thirty-five thousand will nearly be wiped out in Judges; here it is whole."),
  '2:24': v("All registered in Ephraim's camp by armies: 108,100. They set out third.", "All four columns agree.",
   ["Ephraim's camp.", "108,100.", "Third to march."], "Ephraim's division marched third.", "The smallest division, third behind the tent; Rachel's camp is the lightest and the most sheltered.", ARMY, [], "They shall set out third."),
  '2:25': v("The standard of Dan's camp by armies on the north; Dan's leader Ahiezer son of Ammishaddai.", "All four columns agree; 'formation' in Greek.",
   ["North.", "Dan's standard.", "Ahiezer leads."], "Dan held the north.", "Dan on the north, the dangerous side in every prophet's geography; the second-largest tribe is set to face it.", STD),
  '2:26': count('2:26', 'Dan', 'sixty-two thousand seven hundred', "Sixty-two thousand on the north; the rear guard is nearly as strong as the van."),
  '2:27': nxt('2:27', 'Asher', 'Pagiel', 'Ocran', False, "Asher beside Dan: the sons of the handmaids gathered on the north."),
  '2:28': count('2:28', 'Asher', 'forty-one thousand five hundred', "Asher's forty-one thousand, the same as chapter 1 to the man."),
  '2:29': nxt('2:29', 'Naphtali', 'Ahira', 'Enan', True, "Naphtali closes the circle; Bilhah's two sons and Zilpah's second make the north."),
  '2:30': count('2:30', 'Naphtali', 'fifty-three thousand four hundred', "The last count read; the square is complete on all four sides."),
  '2:31': v("All registered in Dan's camp: 157,600. They set out last, by standards.", "All four columns agree; 'by their formation' in Greek.",
   ["Dan's camp.", "157,600.", "Last to march."], "Dan's division was the rear guard.", "Dan last: the rear guard, who gathers the stragglers; Deuteronomy 25 will remember the stragglers Amalek cut off.",
   STD, [], "They shall set out last."),
  '2:32': v("These are the registered of Israel by ancestral houses; all registered in the camps by armies: 603,550.", "All four columns agree.",
   ["Registered by houses.", "In the camps.", "603,550."], "The camp total matched the census.", "The same total as 1:46: the camp has lost no one and gained no one in the laying out.", ARMY),
  '2:33': v("The Levites were not registered among Israel, as YHWH commanded Moses.", "All four columns agree.",
   ["The Levites.", "Not registered.", "As commanded."], "Levi stayed uncounted.", "Said again, because the camp's centre is the one place without a number.", [AGREE], ['yhwh-yahweh', 'moses']),
  '2:34': v("Israel did all YHWH commanded Moses: they camped by standards and set out each by clan and house.", "All four columns agree; the Greek 'formations … divisions … each beside his neighbour'.",
   ["Israel did all.", "Camped by standards.", "Marched by clans."], "The camp order was kept.", "The second chapter also ends in obedience; the shape God drew is the shape Israel took, at rest and on the move.",
   STD + [keeps("Greek 'each beside his neighbour, by their divisions'.")], ['yhwh-yahweh', 'moses']),
}

CHAPTER = {
 'slug': 'numbers', 'chapter': 2,
 'chapterNote': "The camp around the Tent of Meeting, each tribe by its standard at a distance: on the east Judah (74,600) with Issachar and Zebulun, 186,400, who march first; on the south Reuben with Simeon and Gad, 151,450, second; then the tent and the Levites in the middle; on the west Ephraim with Manasseh and Benjamin, 108,100, third; on the north Dan with Asher and Naphtali, 157,600, last. The total is 603,550, the Levites uncounted; Israel camped and marched as commanded. The Greek has 'Tent of Testimony' for 'Tent of Meeting', 'formation' for 'standard' and 'with their army' throughout, adds 'each beside his neighbour' (2:2, 17, 34), 'first' for 'toward sunrise' (2:3), 'southwest' for 'south' (2:10), 'toward the sea' for 'west' (2:18), 'raised' for 'set out' (2:17), and supplies the 'those camping next' formula where the Hebrew has only 'and the tribe of' (2:7, 14, 22, 29). The Hebrew itself has 'Reuel' at 2:14 against 'Deuel' at 1:14. All numbers agree in every column.",
 'verses': VERSES,
}
