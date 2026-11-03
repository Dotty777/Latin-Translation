K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
RULER = [between("The Greek adds 'the ruler' (archon); the Hebrew 'leader' (nasi); the King James 'prince'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

def name(heb, grk):
    return [loses(f"Hebrew '{heb}' is lost in form."), keeps(f"Greek '{grk}'."), between(f"The Latin and King James follow the Hebrew '{heb}'.")]

def chief(key, tribe, man, father, w, lost, explain, entries=None):
    return v(f"from the tribe of {tribe}, the leader {man} son of {father};", explain, [f"The tribe of {tribe}.", f"{man}.", f"Son of {father}."], f"{tribe}'s chief was {man}.", w, lost, entries or [])

CHAPTER = {
 'slug': 'numbers', 'chapter': 34,
 'chapterNote': "The borders of the land and the men who will divide it. South: from the wilderness of Zin by Edom and the Salt Sea's end, round the Ascent of Akrabbim and south of Kadesh-barnea to Hazar-addar, Azmon and the Wadi of Egypt to the sea. West: the Great Sea. North: from the sea to Mount Hor (not Aaron's), Lebo-hamath, Zedad, Ziphron, Hazar-enan. East: Hazar-enan to Shepham, Riblah east of Ain, the eastern shore of Chinnereth, down the Jordan to the Salt Sea. Nine and a half tribes inherit inside it; Reuben, Gad and half-Manasseh already have the east. Eleazar and Joshua with one chief from each tribe will apportion it; the ten chiefs are named, Caleb first. The Greek has 'southwest' (lips) for 'south' (34:3–4), Senna and Arad for Zin and Hazar-addar (34:4), 'the mountain' for 'Mount Hor' (34:7–8), Sarada, Dephrona (34:8–9), Arbela and Bela with 'springs' for Riblah and Ain (34:11), names Manasseh and 'to Moses' at 34:13, adds 'from the south' (34:15), and respells several chiefs and fathers (Salamiel, Eldad, Bakchir/Egli, Ouphi, Sabatha, Oza, Achior, Benammihud) and adds 'the ruler' to each.",
 'verses': {
  '34:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the borders."], "YHWH spoke of borders.", "The land has been promised since Genesis 12; now, for the first time, it is drawn. A promise becomes a map.", FORMULA, ['yhwh-yahweh', 'moses']),
  '34:2': v("Command Israel: when you enter the land of Canaan, this is the land that falls to you as inheritance, the land of Canaan by its borders.", "The Latin 'falls to you by lot'; the Greek 'your inheritance with its boundaries'.",
   ["When you enter Canaan.", "The land that falls to you.", "By its borders."], "Canaan is defined by its borders.", "'Falls to you': the verb of the lot. The land is a thing that falls, like dice, from God's hand; its borders are his and Israel will not set them.", [between("The Latin has 'by lot'; the Greek 'as inheritance with its boundaries'.")], ['canaan'], "Enter the land of Canaan as your inheritance within these borders."),
  '34:3': v("Your south side runs from the wilderness of Zin along Edom; your southern border begins at the east end of the Salt Sea.", "The Greek lips 'southwest' for 'south'; Sin for Zin.",
   ["The south side.", "From Zin along Edom.", "The Salt Sea's east end."], "The southern border begins at the Dead Sea.", "The border starts where the wandering ended, at Zin and Edom: the desert Israel just left becomes the land's southern wall.",
   [loses("Hebrew 'south' (negev) is lost."), keeps("Greek 'southwest' (lips)."), between("The Latin has 'south and east'; the King James 'south'.")], []),
  '34:4': v("Your border turns south of the Ascent of Akrabbim, passes to Zin, ends south of Kadesh-barnea, goes to Hazar-addar and passes to Azmon.", "The Greek 'Senna' and 'the settlement of Arad' for Zin and Hazar-addar.",
   ["The Ascent of Akrabbim.", "South of Kadesh-barnea.", "Hazar-addar and Azmon."], "The border skirts Kadesh.", "Kadesh-barnea, the camp of the spies and the forty years, lies just inside the line: the place of the refusal becomes part of the possession.",
   [loses("Hebrew 'Zin … Hazar-addar' is lost."), keeps("Greek 'Senna … the settlement of Arad'."), between("The Latin has 'Addar'; the King James 'Hazar-addar'; 'Ascent of Scorpions' in Latin for Akrabbim.")], []),
  '34:5': v("The border turns from Azmon to the Wadi of Egypt and ends at the sea.", "All four columns agree.",
   ["From Azmon.", "The Wadi of Egypt.", "To the sea."], "The south ends at the Wadi of Egypt.", "The Wadi of Egypt, the Brook Besor or El-Arish: Egypt's edge is Israel's edge, and the two lands touch at a dry riverbed.", [AGREE], ['egypt']),
  '34:6': v("Your western border: the Great Sea is the border. This is your western border.", "The Hebrew yam means both sea and west; the Greek keeps the sea terminology.",
   ["The western border.", "The Great Sea.", "The sea is the line."], "The sea is the west.", "The one border no one disputes: the Mediterranean. Israel will rarely hold its coast, but the sea is given.", [between("The Hebrew uses 'sea' for 'west'; the Greek 'the sea boundary'; the Latin 'begins and ends at the Great Sea'.")], []),
  '34:7': v("This is your northern border: from the Great Sea mark a line to Mount Hor.", "The Greek 'the mountain', not preserving Hor as a name; the Latin 'the highest mountain'.",
   ["The northern border.", "From the Great Sea.", "To Mount Hor."], "The north starts at a mountain.", "A different Mount Hor from Aaron's: this one is in Lebanon, perhaps Hermon or a peak of the range. The name means simply 'the mountain'.",
   [loses("Hebrew 'Mount Hor' as a name is lost."), keeps("Greek 'measure a line beside the mountain'."), between("The Latin has 'the highest mountain'; the King James 'mount Hor'.")], []),
  '34:8': v("From Mount Hor mark a line to Lebo-hamath, and the border ends at Zedad.", "The Greek 'the entrance to Hamath' and 'Sarada'; 'for them' for 'for you'.",
   ["From Mount Hor.", "To Lebo-hamath.", "Ends at Zedad."], "The north reaches toward Hamath.", "Lebo-hamath, 'the entrance of Hamath': the far northern limit, which Israel touched only under David and Solomon. The map is the ideal, not the usual.",
   [between("The Greek has 'the entrance to Hamath … Sarada'; the Hebrew 'Lebo-hamath … Zedad'.")], []),
  '34:9': v("The border goes to Ziphron and ends at Hazar-enan. This is your northern border.", "The Greek 'Dephrona'.",
   ["To Ziphron.", "Ends at Hazar-enan.", "The northern border."], "Hazar-enan closes the north.", "Hazar-enan, 'the enclosure of the spring', the corner where north turns to east; Ezekiel 47 will use the same point.", name("Ziphron", "Dephrona"), []),
  '34:10': v("Mark your eastern border from Hazar-enan to Shepham.", "All four columns agree.",
   ["The eastern border.", "From Hazar-enan.", "To Shepham."], "The east begins at Hazar-enan.", "The eastern line runs down the Syrian side: not the Jordan alone, but a strip east of it in the north, the land that Dan and Manasseh would reach for.", [AGREE], []),
  '34:11': v("The border descends from Shepham to Riblah east of Ain, and descends to touch the eastern slope of the Sea of Chinnereth.", "The Greek 'Arbela', adds 'Bela', and interprets Ain as 'springs'; the Latin 'the spring of Daphnim'.",
   ["From Shepham to Riblah.", "East of Ain.", "The Sea of Chinnereth."], "The line reaches Galilee's shore.", "Chinnereth, the harp-shaped lake, Galilee: the border touches its eastern shoulder, so the whole lake is inside. Here the gospel's fishermen will work in the land as drawn.",
   [loses("Hebrew 'Riblah east of Ain' is lost."), keeps("Greek 'Arbela … Bela … the springs … the eastern ridge of the sea'."), between("The Latin has 'Riblah opposite the spring of Daphnim'; the King James 'Riblah, on the east side of Ain'.")], []),
  '34:12': v("The border descends to the Jordan and ends at the Salt Sea. This is your land by its borders all round.", "All four columns agree.",
   ["Down the Jordan.", "Ends at the Salt Sea.", "The land all round."], "The Jordan closes the circuit.", "The circle closes at the Salt Sea where it began. 'Your land by its borders all round': a finished shape, the first time Israel has been given a geography and not just a direction.", [AGREE], ['jordan']),
  '34:13': v("Moses commanded Israel: this is the land you shall inherit by lot, which YHWH commanded to give to the nine tribes and the half-tribe.", "The Greek adds 'to Moses' and names Manasseh.",
   ["Inherit by lot.", "YHWH commanded.", "Nine tribes and a half."], "Nine and a half tribes inherit within.", "Nine and a half: the arithmetic of chapter 32 shows here. The borders just drawn exclude two and a half tribes, who chose land outside the promise.",
   [keeps("Greek adds 'the Lord prescribed to Moses' and 'the half-tribe of Manasseh'.")], ['moses', 'yhwh-yahweh'], "Inherit this land by lot, nine tribes and a half."),
  '34:14': v("For the tribe of Reuben by its ancestral houses, the tribe of Gad by its ancestral houses, and the half-tribe of Manasseh have received their inheritance.", "The Greek condenses the ancestral-house formula.",
   ["Reuben.", "Gad.", "Half-Manasseh have received."], "The eastern tribes are already settled.", "'Have received': the perfect tense; the east is a done thing, outside the map, recorded as a fact and not blessed or blamed.", [between("The Latin has 'by families and clan numbers'; the Greek 'by ancestral houses' once.")], []),
  '34:15': v("The two tribes and the half-tribe have received their inheritance across the Jordan opposite Jericho, eastward toward the sunrise.", "The Hebrew doubles the east; the Greek adds 'from the south'.",
   ["Two tribes and a half.", "Across the Jordan.", "Toward the sunrise."], "The east is outside the borders.", "'Toward the sunrise': the doubled direction insists on it. Two and a half tribes live where the sun rises on the promised land, looking across the river at it.",
   [keeps("Greek adds 'from the south'."), between("The Hebrew and King James have 'eastward, toward the sunrising'.")], ['jordan', 'jericho']),
  '34:16': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the dividers."], "YHWH named the dividers.", "Borders need surveyors: the second speech appoints the men who will turn the map into fields.", FORMULA, ['yhwh-yahweh', 'moses']),
  '34:17': v("These are the names of the men who shall take possession of the land for you: Eleazar the priest and Joshua son of Nun.", "The Latin 'divide'; the Greek 'obtain as inheritance for the people'.",
   ["Eleazar the priest.", "Joshua son of Nun.", "They apportion the land."], "Eleazar and Joshua lead the division.", "Priest and general together, as Moses and Aaron were: the land is divided by the sanctuary and the army jointly, so that no tribe can say the sword alone gave it its share.",
   [between("The Latin has 'who shall divide the land'; the Greek 'who shall obtain the land for you'.")], ['high-priest', 'joshua']),
  '34:18': v("Take one leader from each tribe to apportion the land.", "The Greek adds 'to you' and makes it a command to Israel; the Latin lists the leaders.",
   ["One leader.", "From each tribe.", "To apportion the land."], "Each tribe sends a chief.", "A tribal witness at every boundary stone: the division is done in the sight of every tribe's representative, which is how a lot is kept honest.", [between("The Greek has 'you shall take for yourselves one ruler from each tribe'; the Latin 'and one leader from each tribe'.")], [], "Take one leader from each tribe to apportion the land."),
  '34:19': v("These are the names of the men: from the tribe of Judah, Caleb son of Jephunneh;", "All four columns agree.",
   ["The names.", "Judah.", "Caleb son of Jephunneh."], "Caleb heads the list.", "Caleb, forty-five years after he saw the land and said it could be taken, is the first man named to divide it. Hebron will be his (Joshua 14).", [AGREE], ['hebron']),
  '34:20': chief('34:20', "Simeon", "Shemuel", "Ammihud", "A Simeonite Samuel, two centuries before the prophet; Simeon's share will be swallowed inside Judah's.", name("Shemuel", "Salamiel"), "The Greek 'Salamiel'."),
  '34:21': chief('34:21', "Benjamin", "Elidad", "Chislon", "Elidad, 'my God has loved'; Benjamin's lot will hold Jerusalem's border.", name("Elidad", "Eldad"), "The Greek 'Eldad'."),
  '34:22': chief('34:22', "Dan", "Bukki", "Jogli", "Dan draws a coastal lot it cannot hold and migrates north (Judges 18); the surveyor could not foresee that.", name("Bukki son of Jogli", "Bakchir son of Egli") + RULER, "The Greek 'Bakchir son of Egli' and adds 'the ruler'."),
  '34:23': v("from the sons of Joseph: from the tribe of Manasseh, the leader Hanniel son of Ephod;", "The Greek 'Ouphi' for Ephod and adds 'the ruler'.",
   ["The sons of Joseph.", "Manasseh.", "Hanniel son of Ephod."], "Manasseh's western chief was Hanniel.", "The western half of Manasseh: the tribe is divided by the river, with a chief for the half that chose the promise.", name("Ephod", "Ouphi") + RULER, ['joseph-son-of-jacob']),
  '34:24': chief('34:24', "Ephraim", "Kemuel", "Shiphtan", "Ephraim, Joshua's own tribe, listed after Manasseh here though it took the firstborn's blessing from Jacob.", name("Shiphtan", "Sabatha") + RULER, "The Greek 'Sabatha' and adds 'the ruler'."),
  '34:25': chief('34:25', "Zebulun", "Elizaphan", "Parnach", "Zebulun, whose lot touches the Galilee the gospel will walk.", RULER, "All four columns agree; the Greek adds 'the ruler'."),
  '34:26': chief('34:26', "Issachar", "Paltiel", "Azzan", "Paltiel, 'God is my deliverance'; Issachar's lot is the Jezreel valley, the land's granary and battlefield.", name("Azzan", "Oza") + RULER, "The Greek 'Oza'."),
  '34:27': chief('34:27', "Asher", "Ahihud", "Shelomi", "Asher's chief for the northern coast; the tribe will never dislodge the Phoenician cities (Judges 1:31).", name("Ahihud", "Achior") + RULER, "The Greek 'Achior'."),
  '34:28': chief('34:28', "Naphtali", "Pedahel", "Ammihud", "Pedahel, 'God has ransomed': the last chief, for the tribe of the far north. Ten chiefs, for the nine and a half tribes west of the river.", name("Ammihud", "Benammihud") + RULER, "The Greek 'Benammihud'."),
  '34:29': v("These are the men YHWH commanded to assign the Israelites their inheritance in the land of Canaan.", "All four columns agree.",
   ["These are the men.", "YHWH commanded.", "To assign the inheritance."], "The commission is sealed.", "Of these twelve, Caleb and Joshua are the only ones with names the reader already knows; the rest are new men for a new land, chosen under Moses but to work after him.", [AGREE], ['yhwh-yahweh', 'canaan']),
 },
}
