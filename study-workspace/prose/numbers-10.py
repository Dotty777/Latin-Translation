K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
DWELL = [loses("Hebrew 'Dwelling' (mishkan) is lost."), keeps("Greek 'Tent'."), between("The Latin and King James have 'tabernacle'.")]
STD = [loses("Hebrew 'standard' (degel) is lost."), keeps("Greek 'formation … with their army'."), between("The Latin has 'companies'; the King James 'standard'.")]
FUT = [keeps("Greek shifts to a prospective future ('shall set out'); the Hebrew narrates."), between("The Latin and King James follow the Hebrew's past.")]
MOUTH = [loses("Hebrew 'at the mouth of YHWH' is lost."), keeps("Greek 'by the voice of the Lord'."), between("The Latin has 'command' (imperium); the King James 'commandment'.")]
LEADER = [between("All four columns name the same commander and father; 'over the army' / 'leader' is wording.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

def lead(ref, leader, father, tribe, wis):
    return v(f"{leader} son of {father} was over the army of the tribe of {tribe}.", "All four columns agree.",
      [f"{leader}.", f"Son of {father}.", f"Over {tribe}."], f"{leader} led {tribe} on the march.", wis, LEADER)

CHAPTER = {
 'slug': 'numbers', 'chapter': 10,
 'chapterNote': "The two silver trumpets, hammered, blown by Aaron's sons: both to gather the congregation at the tent door, one for the leaders, an alarm to move the camps east then south, a plain blast for assembly, an alarm in war to be remembered before God, and blasts over the offerings at feasts and new moons. On the twentieth of the second month of the second year the cloud rises and Israel leaves Sinai for Paran by stages in the order of chapter 2: Judah's standard first, then Gershon and Merari with the Dwelling, Reuben's standard, the Kohathites with the holy things, Ephraim's, and Dan's as rear guard. Moses asks Hobab the Midianite to come and be their eyes; the ark goes three days ahead to find a resting place, and Moses prays 'Rise, YHWH' when it moves and 'Return, YHWH' when it rests, under the cloud of YHWH by day. The Greek has 'you shall blow' and no 'before you' (10:3), 'all the rulers' without 'thousands' (10:4), adds third and fourth signals for west and north and 'southwest' (10:6), 'go out to war … resist' and no 'your God' (10:9), 'equipment' for 'stages' (10:12), 'formation' for 'standard' and future tenses in the march (10:17–25), 'Reuel' for 'Deuel' (10:20), 'armies' for 'stages' (10:28), 'you were with us … an elder' for 'you know where to camp … eyes' (10:31), 'all' and no 'from Your presence' (10:34), an accusative 'turn back the thousands' (10:35), and places the cloud sentence after the ark prayers (10:36) without 'of the Lord'.",
 'verses': {
  '10:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the trumpets."],
   "YHWH spoke on the trumpets.", "The cloud gives the sign in the sky; the trumpets will give it in the ear.", FORMULA, ['yhwh-yahweh', 'moses']),
  '10:2': v("Make two silver trumpets of hammered work, for calling the congregation and setting the camps in motion.", "All four columns agree.",
   ["Two silver trumpets.", "Hammered.", "To call and to move."], "Two trumpets governed the camp.", "Hammered silver like the lampstand's hammered gold: the instruments of the camp are made the way the furniture is.", [AGREE], [], "Make two silver trumpets."),
  '10:3': v("When they blow both, the whole congregation assembles before you at the Tent of Meeting's entrance.", "The Hebrew 'they … before you'; the Greek 'you shall blow' without 'before you'.",
   ["Both blown.", "The whole congregation.", "At the tent door."], "Two trumpets summoned everyone.", "Two horns, the whole people; the door of the tent is where six hundred thousand men come when called.",
   TENT + [keeps("Greek 'you shall blow them'."), loses("Hebrew 'before you' is lost.")], ['tabernacle']),
  '10:4': v("If they blow one, the leaders, heads of Israel's thousands, assemble before you.", "The Hebrew 'heads of thousands'; the Greek 'all the rulers, the leaders'.",
   ["One blown.", "The leaders.", "Before Moses."], "One trumpet summoned the chiefs.", "One horn for the few: the chiefs come alone, and a council is called by a single note.",
   [loses("Hebrew 'heads of Israel's thousands' is lost."), keeps("Greek 'all the rulers, the leaders of Israel'.")]),
  '10:5': v("When you blow an alarm, the camps on the east set out.", "All four columns agree; the Latin 'longer, broken blast'.",
   ["An alarm.", "The east camps.", "Set out."], "An alarm moved Judah's camp.", "The alarm, teru'ah, a broken quavering blast: the sound that moves Judah is the sound of war and New Year.",
   [keeps("Greek 'a signal'."), between("The Latin has 'a longer, broken blast'; the King James 'alarm'.")]),
  '10:6': v("A second alarm, and the camps on the south set out; they blow an alarm for their departures.",
   "The Hebrew has two alarms and a general rule; the Greek adds third and fourth signals for the sea-side and north camps, with 'southwest'.",
   ["A second alarm.", "The south camps.", "Alarms for departures."], "Alarms moved the camps in order.", "Two alarms in the Hebrew and the rest understood; the Greek spells out all four, east, south, west, north, so no camp moves unsignalled.",
   [loses("Hebrew's two alarms with a general rule are lost."), keeps("Greek 'a third signal … toward the sea … a fourth signal … toward the north … southwest'."), between("The Latin has 'likewise' for the rest; the King James follows the Hebrew.")]),
  '10:7': v("When assembling the assembly, blow but do not sound an alarm.", "All four columns agree; the Latin 'simple blast, not broken'.",
   ["Assembling.", "Blow.", "No alarm."], "Assembly and alarm were different notes.", "A plain note gathers, a broken note moves; the people learn to tell peace from war by the shape of a sound.",
   [between("The Latin has 'simple blast, not broken ringing'; the Greek 'not with a signal'.")], [], "You shall blow, but not sound an alarm."),
  '10:8': v("Aaron's sons the priests blow the trumpets; a perpetual statute through your generations.", "All four columns agree.",
   ["Aaron's sons.", "Blow the trumpets.", "A perpetual statute."], "Only priests blew them.", "The priests hold the horns; the signal to move the nation comes from the altar's men, not the army's.", [AGREE], ['high-priest'], "Aaron's sons the priests shall blow the trumpets."),
  '10:9': v("When you enter war in your land against the adversary oppressing you, sound an alarm; you are remembered before YHWH your God and saved from your enemies.", "The Hebrew 'enter war … oppressing … your God'; the Greek 'go out to war … resist' without 'your God'.",
   ["War in your land.", "Sound an alarm.", "Remembered and saved."], "The war alarm brought God's remembrance.", "The trumpet in war is not a signal to the troops but to God: 'you shall be remembered'. The horn is a prayer with no words.",
   [loses("Hebrew 'the adversary oppressing you … YHWH your God' is lost."), keeps("Greek 'go out to war … against the adversaries who resist you … before the Lord'.")], ['yhwh-yahweh', 'savior'], "Sound an alarm with the trumpets in war."),
  '10:10': v("On your day of gladness, at your festivals and new moons, blow the trumpets over your burnt and well-being offerings; a memorial before your God. I am YHWH your God.", "All four columns agree in substance; the Latin 'banquet'.",
   ["Days of gladness.", "Festivals and new moons.", "Over the offerings."], "Trumpets marked joy too.", "The same horns for joy as for war; the trumpets over the offerings are a memorial, so that the feast too is remembered before God.",
   [keeps("Greek 'the days of your gladness … sacrifices of deliverance'."), between("The Latin has 'banquet' (epulum); the King James 'day of your gladness'.")], ['yhwh-yahweh']),
  '10:11': v("In the second year, the second month, the twentieth day, the cloud rose from above the Dwelling of Testimony.", "All four columns agree.",
   ["The second year.", "The twentieth of the second month.", "The cloud rose."], "Israel's departure from Sinai was dated.", "Eleven months at Sinai, and on the twentieth of the second month the cloud lifts; the law is given, the camp is counted, the journey begins.",
   DWELL, ['tabernacle']),
  '10:12': v("Israel set out by stages from Sinai's wilderness, and the cloud settled in the wilderness of Paran.", "The Hebrew 'by stages from'; the Greek 'with their equipment in'.",
   ["By stages.", "From Sinai.", "The cloud in Paran."], "The march went from Sinai to Paran.", "From Sinai to Paran, the first leg of the journey toward the land; the mountain of the law is left behind for good.",
   [loses("Hebrew 'by stages' is lost."), keeps("Greek 'with their equipment'."), between("The Latin has 'by companies'; the King James 'journeys'.")], ['sinai']),
  '10:13': v("They set out for the first time at YHWH's mouth through Moses.", "All four columns agree; 'voice' in Greek.",
   ["The first time.", "At YHWH's mouth.", "Through Moses."], "The first march was by command.", "'For the first time': the whole machinery of chapters 1–10 moves for the first time, and it moves on a word.", MOUTH, ['yhwh-yahweh', 'moses']),
  '10:14': v("The standard of Judah's camp set out first by armies; Nahshon son of Amminadab over its army.", "All four columns agree; 'formation' in Greek.",
   ["Judah's standard first.", "By armies.", "Nahshon over it."], "Judah led the march.", "Judah first on the road as in the camp and at the altar; the book keeps its order.", STD, ['david']),
  '10:15': lead('10:15', 'Nethanel', 'Zuar', 'Issachar', "Issachar follows Judah out of Sinai."),
  '10:16': lead('10:16', 'Eliab', 'Helon', 'Zebulun', "The east division is on the road."),
  '10:17': v("The Dwelling was taken down, and the Gershonites and Merarites set out carrying it.", "The Hebrew narrates; the Greek 'they shall take down the Tent'.",
   ["The Dwelling taken down.", "Gershon and Merari.", "Carrying it."], "The tent's structure followed Judah.", "The house comes down and goes forward on wagons behind the first division, so it can be standing when the holy things arrive.",
   DWELL + FUT, ['tabernacle']),
  '10:18': v("The standard of Reuben's camp set out by armies; Elizur son of Shedeur over its army.", "All four columns agree; 'formation' in Greek.",
   ["Reuben's standard.", "By armies.", "Elizur over it."], "Reuben's division marched second.", "The south side follows the tent's frame.", STD),
  '10:19': lead('10:19', 'Shelumiel', 'Zurishaddai', 'Simeon', "Simeon beside Reuben on the road as in the camp."),
  '10:20': v("Eliasaph son of Deuel was over the army of Gad.", "The Hebrew 'Deuel'; the Greek 'Reuel', not harmonized.",
   ["Eliasaph.", "Son of Deuel.", "Over Gad."], "Eliasaph led Gad.", "Deuel for the last time; the name has been spelled two ways in every list.",
   [loses("Hebrew 'Deuel' is lost."), keeps("Greek 'Reuel'."), between("The Latin and King James have 'Deuel'.")]),
  '10:21': v("The Kohathites set out carrying the holy things; the Dwelling was to be erected before they arrived.", "Both texts leave the erecting subject unexpressed; the Greek future.",
   ["Kohathites.", "Carrying the holy things.", "The Dwelling up before they arrive."], "The ark travelled in the middle.", "The holy things in the centre of the column: when Kohath arrives the walls are already up, and the ark goes straight behind its curtain.",
   DWELL + FUT, ['ark-of-the-covenant']),
  '10:22': v("The standard of Ephraim's camp set out by armies; Elishama son of Ammihud over its army.", "All four columns agree; 'formation' and future in Greek.",
   ["Ephraim's standard.", "By armies.", "Elishama over it."], "Ephraim's division marched third.", "The west side, behind the ark.", STD + FUT, ['joseph-son-of-jacob']),
  '10:23': lead('10:23', 'Gamaliel', 'Pedahzur', 'Manasseh', "Manasseh with Ephraim."),
  '10:24': lead('10:24', 'Abidan', 'Gideoni', 'Benjamin', "Benjamin completes Rachel's division."),
  '10:25': v("The standard of Dan's camp set out as rear guard of all the camps by armies; Ahiezer son of Ammishaddai over its army.", "The Hebrew 'rear guard (gatherer)'; the Greek 'last of all'.",
   ["Dan's standard.", "Rear guard.", "Ahiezer over it."], "Dan guarded the rear.", "'The gatherer of all the camps': Dan picks up what falls behind; the rear guard's name is a verb for collecting.",
   STD + FUT + [loses("Hebrew 'rear guard' (gatherer) is lost."), keeps("Greek 'last of all the camps'.")]),
  '10:26': lead('10:26', 'Pagiel', 'Ocran', 'Asher', "Asher in the rear division."),
  '10:27': lead('10:27', 'Ahira', 'Enan', 'Naphtali', "Naphtali last; the column is complete."),
  '10:28': v("These were the stages of Israel by their armies; they set out.", "The Hebrew 'stages'; the Greek 'armies … with their force'.",
   ["The stages.", "By armies.", "They set out."], "The order of march was summed.", "The order given in chapter 2 is the order kept in chapter 10; for once in Numbers, a plan is carried out exactly.",
   [loses("Hebrew 'journey stages' is lost."), keeps("Greek 'armies … with their force'.")]),
  '10:29': v("Moses said to Hobab son of Reuel the Midianite, his relative by marriage: we set out for the place YHWH promised; come, and we will treat you well, for YHWH has promised good for Israel.", "All four columns agree; the kinship term is affinal and interpretive.",
   ["Moses to Hobab.", "Come with us.", "YHWH has promised good."], "Moses invited his Midianite kin.", "Moses invites a Midianite to the promised land; the first person offered a share in Israel's good is a foreigner and an in-law.",
   [between("The Hebrew hoten and Greek gambros are both affinal terms; the Latin and King James have 'father in law'.")], ['moses', 'yhwh-yahweh']),
  '10:30': v("He said: I will not go; I will go to my own land and kindred.", "All four columns agree.", ["I will not go.", "To my land.", "To my kindred."],
   "Hobab declined.", "A plain no: home is home, even against a promise.", [AGREE]),
  '10:31': v("He said: please do not leave us, for you know where we should camp in the wilderness and can be eyes for us.",
   "The Hebrew 'you know where to camp … be eyes for us'; the Greek 'you were with us in the wilderness … be an elder among us'. The reason and role differ.",
   ["Do not leave us.", "You know the wilderness.", "Be our eyes."], "Moses wanted Hobab as guide.", "Moses, who follows the cloud, still wants a man who knows the wells; the Hebrew asks for a guide, the Greek for an elder. Both ask a Midianite to stay.",
   [loses("Hebrew 'you know where we should camp … you can be eyes for us' is lost."), keeps("Greek 'you were with us in the wilderness, and you shall be an elder among us'."), between("The Latin and King James follow the Hebrew.")]),
  '10:32': v("If you go with us, whatever good YHWH does for us, we do for you.", "All four columns agree; the Latin 'the best of the wealth'.",
   ["If you go.", "Whatever good YHWH does.", "We do for you."], "Hobab was promised a share.", "The offer repeated; Judges 1:16 will show Hobab's people in Judah's land, so he came after all.",
   [between("The Latin has 'the best of the wealth the Lord hands over'; the Greek 'treat you well'.")], ['yhwh-yahweh']),
  '10:33': v("They set out from YHWH's mountain a three-day journey; the Ark of YHWH's Covenant went before them three days to seek a resting place.", "All four columns agree. Rashi has a second ark with the broken tablets.",
   ["From YHWH's mountain.", "Three days.", "The ark goes before."], "The ark led the way.", "The ark three days ahead of the people, alone with its bearers, looking for the next camp; the holiest thing in Israel is the scout.", [AGREE], ['ark-of-the-covenant', 'sinai']),
  '10:34': v("Whenever the ark set out, Moses said: Rise, YHWH! Let your enemies scatter and those who hate you flee from your presence.", "The Greek adds 'all' and lacks 'from Your presence'; its verse order differs.",
   ["The ark sets out.", "Rise, YHWH.", "Enemies scatter."], "Moses prayed at the ark's rising.", "'Rise, YHWH': the opening of Psalm 68, said every morning the ark moved; God is asked to stand up and march.",
   [loses("Hebrew 'flee from Your presence' is lost."), keeps("Greek 'let all them that hate Thee flee'."), between("The Latin and King James have 'from before thee'.")], ['ark-of-the-covenant', 'yhwh-yahweh', 'moses']),
  '10:35': v("Whenever it rested he said: Return, YHWH, to the myriads of Israel's thousands.",
   "The Hebrew asks YHWH to return to the multitudes; the Greek's accusative allows 'bring back the thousands'. Both compressed.",
   ["The ark rests.", "Return, YHWH.", "To Israel's myriads."], "Moses prayed at the ark's rest.", "'Return': at evening God is asked to come home to the camp; the ark's two prayers are the day's two gates.",
   [loses("Hebrew 'return to the myriads' is lost in form."), keeps("Greek 'Turn back, O Lord, the thousands and myriads in Israel'."), between("The Latin has 'return to the multitude of Israel's army'.")], ['yhwh-yahweh', 'moses']),
  '10:36': v("The cloud of YHWH was over them by day when they set out from the camp.", "The Greek places this after the prayers and lacks 'of the Lord'.",
   ["The cloud of YHWH.", "Over them by day.", "When they set out."], "The cloud covered the march.", "The chapter ends under the cloud: ark ahead, cloud above, Moses praying at both ends of the day. Chapter 11 will break it.",
   [loses("Hebrew 'the cloud of YHWH' is lost."), keeps("Greek 'the cloud was overshadowing them', placed after the ark prayers.")], ['yhwh-yahweh']),
 },
}
