K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
NEGEB = [loses("Hebrew 'Negeb' is lost."), keeps("Greek 'this wilderness'."), between("The Latin has 'the southern region'; the King James 'southward'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

def spy(ref, tribe, name, father, wis, diff=None, ent=None):
    if diff:
        return v(f"From the tribe of {tribe}, {name} son of {father};", diff[0], [f"From {tribe}.", f"{name}.", f"Son of {father}."], f"{tribe} sent {name}.", wis, diff[1], ent or [])
    return v(f"From the tribe of {tribe}, {name} son of {father};", "All four columns agree.", [f"From {tribe}.", f"{name}.", f"Son of {father}."], f"{tribe} sent {name}.", wis, [AGREE], ent or [])

CHAPTER = {
 'slug': 'numbers', 'chapter': 13,
 'chapterNote': "The scouts. At YHWH's word Moses sends twelve leaders, one per tribe (Shammua, Shaphat, Caleb, Igal, Hoshea whom Moses renames Joshua, Palti, Gaddiel, Gaddi, Ammiel, Sethur, Nahbi, Geuel), from Paran through the Negeb into the hill country to see the land, its people, its towns and its soil, in the season of first grapes. They go from Zin to Rehob, reach Hebron where the Anakites live, cut a cluster at Wadi Eshcol, and return after forty days to Kadesh: the land flows with milk and honey, but the people are strong, the cities fortified, Amalek in the Negeb, Hittites, Jebusites and Amorites in the hills, Canaanites by the sea and Jordan. Caleb says go up; the others say the land devours its inhabitants and its people are Nephilim beside whom they were grasshoppers. The Greek has 'Canaanites … as a possession … ancestral families' (13:2), 'Salamiel' for Shammua (13:4), 'Souri' for Hori (13:5), 'Iabi' for Vophsi (13:14), 'Gaddiel' for Geuel (13:15), 'this wilderness' for 'Negeb' (13:17, 22), 'days of spring, forerunners of the grape harvest' (13:20), 'Ephaath' for Hamath (13:21), plural travellers at 13:22, inspection and plural poles at 13:23, 'bold … walls' (13:28), adds the Hivites (13:29), 'No!' and 'against them' (13:30), 'we are not going up' (13:31), 'dismay' for 'bad report' (13:32), and 'giants' without the Anakite genealogy and with 'indeed so we were' (13:33).",
 'verses': {
  '13:1': v("YHWH speaks to Moses.", "All four columns agree; the Latin adds 'there'.", ["YHWH speaks.", "To Moses.", "On the land."],
   "YHWH spoke on scouting the land.", "At the edge of Canaan God himself orders the reconnaissance; Deuteronomy will say the people asked for it first.", FORMULA, ['yhwh-yahweh', 'moses']),
  '13:2': v("Send men to explore the land of Canaan which I am giving Israel; one man from each ancestral tribe, each a leader.", "All four columns agree; the Greek 'Canaanites … for a possession … groups of ancestral families'.",
   ["Send men.", "To explore Canaan.", "One leader per tribe."], "Twelve leaders were to scout.", "'Which I am giving': the gift is stated before the scouting; the land is already theirs on paper, and the men go to see what they own.",
   [keeps("Greek 'the land of the Canaanites … for a possession … according to the groups of their ancestral families'.")], ['canaan'], "Send men to explore the land of Canaan."),
  '13:3': v("Moses sent them from the wilderness of Paran at YHWH's command; all were heads of the Israelites.", "All four columns agree; 'voice' in Greek.",
   ["From Paran.", "At YHWH's command.", "All heads."], "Moses sent the chiefs.", "Chiefs, not scouts by trade: the men who will report are the men the tribes trust, which is why the report will carry.",
   [keeps("Greek 'through the Lord's voice'.")], ['moses', 'yhwh-yahweh']),
  '13:4': spy('13:4', 'Reuben', 'Shammua', 'Zaccur', "Reuben first again; the list follows birth more than camp this time.",
   ("The Hebrew 'Shammua'; the Greek 'Salamiel'. The father agrees.", [loses("Hebrew 'Shammua' is lost."), keeps("Greek 'Salamiel'."), between("The Latin has 'Sammua'; the King James 'Shammua'.")])),
  '13:5': spy('13:5', 'Simeon', 'Shaphat', 'Hori', "Shaphat, 'he has judged'; a name for a man who will misjudge.",
   ("The Hebrew 'Hori'; the Greek 'Souri'.", [loses("Hebrew 'Hori' is lost."), keeps("Greek 'Souri'."), between("The Latin has 'Huri'; the King James 'Hori'.")])),
  '13:6': spy('13:6', 'Judah', 'Caleb', 'Jephunneh', "Caleb of Judah, the one name in the list the reader is meant to remember; forty-five years later he will take Hebron."),
  '13:7': spy('13:7', 'Issachar', 'Igal', 'Joseph', "Igal son of Joseph; a Joseph outside Joseph's tribe."),
  '13:8': spy('13:8', 'Ephraim', 'Hoshea', 'Nun', "Hoshea, 'salvation'; the name he had before Moses added God's to it.", None, ['joshua']),
  '13:9': spy('13:9', 'Benjamin', 'Palti', 'Raphu', "Palti, 'my deliverance'; the names promise more than the men do."),
  '13:10': spy('13:10', 'Zebulun', 'Gaddiel', 'Sodi', "Gaddiel; the Greek will use the same form for Gad's man at 13:15."),
  '13:11': v("From the tribe of Joseph, from the tribe of Manasseh, Gaddi son of Susi;", "All four columns agree; 'sons of Manasseh' in Greek.",
   ["From Joseph.", "Manasseh.", "Gaddi son of Susi."], "Manasseh sent Gaddi.", "Manasseh called 'the tribe of Joseph' here, Ephraim not; the father's name is given to the elder son's tribe.",
   [keeps("Greek 'of the sons of Manasseh'.")], ['joseph-son-of-jacob']),
  '13:12': spy('13:12', 'Dan', 'Ammiel', 'Gemalli', "Ammiel, 'my kinsman is God'."),
  '13:13': spy('13:13', 'Asher', 'Sethur', 'Michael', "Sethur son of Michael; the archangel's name first appears as a scout's father."),
  '13:14': spy('13:14', 'Naphtali', 'Nahbi', 'Vophsi', "Nahbi, 'hidden'; a scout's name.",
   ("The Hebrew 'Vophsi'; the Greek 'Iabi'.", [loses("Hebrew 'Vophsi' is lost."), keeps("Greek 'Iabi'."), between("The Latin has 'Vapsi'; the King James 'Vophsi'.")])),
  '13:15': spy('13:15', 'Gad', 'Geuel', 'Machi', "Geuel closes the twelve; the Greek gives him Zebulun's man's name.",
   ("The Hebrew 'Geuel'; the Greek 'Gaddiel', as at 13:10.", [loses("Hebrew 'Geuel' is lost."), keeps("Greek 'Gaddiel'."), between("The Latin and King James have 'Geuel'.")])),
  '13:16': v("These were the men Moses sent to explore the land; Moses named Hoshea son of Nun Joshua.", "All four columns agree; the Greek Iesous refers to Joshua.",
   ["The men sent.", "Hoshea son of Nun.", "Named Joshua."], "Hoshea became Joshua.", "'Salvation' becomes 'YHWH saves': Moses puts God's name into his servant's, and the Greek spells it Iesous, the name the gospels will use.", [AGREE], ['joshua', 'moses', 'savior']),
  '13:17': v("Moses sent them to explore Canaan: go up through the Negeb and into the hill country.", "The Hebrew 'Negeb'; the Greek 'this wilderness'.",
   ["Explore Canaan.", "Through the Negeb.", "Into the hills."], "The route was south to north.", "Up from the dry south into the hills: the route Abraham walked in reverse, and Judah's future land first.", NEGEB, ['moses', 'canaan']),
  '13:18': v("See what the land is like, and whether its people are strong or weak, few or many.", "All four columns agree.",
   ["See the land.", "The people strong or weak.", "Few or many."], "The brief was military and agricultural.", "A soldier's questions first; Moses wants to know what he is marching into.", [AGREE]),
  '13:19': v("Is the land good or bad? what are the towns, open camps or fortified?", "All four columns agree; the Greek reverses the order and says 'walls'.",
   ["Land good or bad?", "The towns?", "Open or fortified?"], "Towns and soil were to be judged.", "Camps or walls: the question the spies will answer with fear.",
   [keeps("Greek 'walled or unwalled'.")]),
  '13:20': v("Is the land rich or poor? are there trees? take courage and bring some fruit. It was the season of first ripe grapes.", "The Hebrew 'first ripe grapes'; the Greek 'days of spring, forerunners of the grape harvest' and 'neglected' for 'poor'.",
   ["Rich or poor?", "Trees?", "Bring fruit; grape season."], "They were to bring fruit.", "'Take courage': Moses knows what fear will do to a report, and says so before they go. The grapes are just ripening; the land is at its most persuasive.",
   [loses("Hebrew 'the season of the first ripe grapes … poor' is lost."), keeps("Greek 'days of spring, forerunners of the grape harvest … neglected'."), between("The Latin has 'rich or barren … first ripe grapes'.")], ['grapevine']),
  '13:21': v("They went up and explored from the wilderness of Zin to Rehob at the entrance to Hamath.", "The Greek 'Sin … Raab … Ephaath'; Zin is not every Sin.",
   ["From Zin.", "To Rehob.", "Entrance to Hamath."], "They covered the whole land.", "From the southern desert to the Syrian border, the whole length of the promise walked in forty days.",
   [loses("Hebrew 'Hamath' is lost."), keeps("Greek 'Raab, as one enters Ephaath'."), between("The Latin and King James have 'Rehob … Hamath'.")]),
  '13:22': v("They went up through the Negeb and he came to Hebron, where Ahiman, Sheshai and Talmai, descendants of Anak, lived; Hebron was built seven years before Zoan in Egypt.", "The Hebrew's singular 'he came' is unexplained (Caleb by tradition); the Greek plural; 'Tanis' for Zoan.",
   ["To Hebron.", "The sons of Anak.", "Older than Zoan."], "Hebron and the Anakites were seen.", "'He came to Hebron': one man, unnamed, goes to the giants' city; tradition says Caleb, and Caleb will ask for Hebron as his reward.",
   NEGEB + [loses("Hebrew singular 'he came' is lost."), keeps("Greek plural 'they came … Tanis'."), between("The Latin and King James have 'they came … Zoan'.")], ['hebron', 'anakim', 'egypt']),
  '13:23': v("They came to Wadi Eshcol and cut a branch with one cluster of grapes; two men carried it on a pole, with pomegranates and figs.", "The Greek adds inspection and has plural poles without 'two men'.",
   ["Wadi Eshcol.", "One cluster on a pole.", "Pomegranates and figs."], "They carried back a giant cluster.", "A cluster so heavy two men carry it on a pole: the land's evidence for itself, and the spies bring it to argue against it.",
   [loses("Hebrew 'two men carried it on a pole' is lost."), keeps("Greek 'inspected it … carried it on carrying poles'."), between("The Latin and King James have 'two men … a staff'.")], ['grapevine']),
  '13:24': v("The place was called Wadi Eshcol because of the cluster Israel cut there.", "All four columns agree; the Greek translates 'Ravine of the Cluster'.",
   ["Wadi Eshcol.", "Named for the cluster.", "Israel cut it."], "The wadi was named for the grapes.", "A good name for once on the wilderness map; the valley remembers the fruit, not the fear.",
   [keeps("Greek 'Ravine of the Cluster'."), between("The Latin has 'Nehelescol'; the King James 'Eshcol'.")]),
  '13:25': v("They returned from exploring the land after forty days.", "All four columns agree.",
   ["They returned.", "After forty days.", "From exploring."], "The scouting took forty days.", "Forty days, which will become forty years; the arithmetic of 14:34 is set up here.", [AGREE]),
  '13:26': v("They came to Moses, Aaron and the whole congregation in the wilderness of Paran at Kadesh, reported, and showed the land's fruit.", "All four columns agree.",
   ["To Moses and Aaron.", "At Kadesh.", "Report and fruit."], "The report was given at Kadesh.", "Kadesh, where Israel will sit for most of forty years; the spies come back to the place the people will not leave.", [AGREE], ['moses', 'high-priest']),
  '13:27': v("We came to the land you sent us to; it indeed flows with milk and honey, and this is its fruit.", "All four columns agree; the Hebrew 'indeed'.",
   ["We came to the land.", "Milk and honey.", "This is its fruit."], "The report began well.", "The first sentence confirms God's own description; the spies agree with the promise before they disagree with it.",
   [keeps("Greek 'this is its fruit'."), between("The Latin adds 'as can be known from the fruits'.")]),
  '13:28': v("But the people are strong, the cities fortified and very large; we saw Anak's descendants there.", "The Hebrew 'strong'; the Greek 'bold … with walls'.",
   ["But the people are strong.", "Cities fortified.", "Anak's sons."], "The 'but' turned the report.", "'But': the word that undoes the gift. Everything after it is true, and everything after it is unbelief.",
   [keeps("Greek 'the nation is bold … strongly fortified with walls'."), between("The Latin and King James have 'strong'.")], ['anakim']),
  '13:29': v("Amalek in the Negeb; Hittites, Jebusites and Amorites in the hills; Canaanites by the sea and the Jordan.", "The Greek adds the Hivites and 'river'.",
   ["Amalek south.", "Hittites and Amorites in the hills.", "Canaanites by sea and Jordan."], "The land's peoples were mapped.", "A map of enemies on every side; the spies have seen the inhabitants and forgotten the landlord.",
   [keeps("Greek adds 'the Hivite' and 'the river Jordan'."), between("The Latin and King James lack the Hivites.")], ['canaan', 'jordan']),
  '13:30': v("Caleb quieted the people before Moses and said: let us go up and take it, for we can surely overcome it.", "The Greek adds 'No!' and 'against them'; the Hebrew's object is the land.",
   ["Caleb quieted them.", "Let us go up.", "We can overcome."], "Caleb dissented.", "One voice against ten; Caleb's 'we can' is the first and almost the last faith in the chapter.",
   [keeps("Greek 'No! We shall certainly go up … prevail against them'."), between("The Latin and King James follow the Hebrew.")]),
  '13:31': v("The men who went with him said: we cannot go up against the people, for they are stronger than we.", "The Greek adds 'we are not going up' and 'much stronger'.",
   ["The others said.", "We cannot go up.", "They are stronger."], "Ten said no.", "'We cannot': the majority report in three words, and the forty years begin in them.",
   [keeps("Greek 'We are not going up … much stronger than we are'.")]),
  '13:32': v("They spread a bad report: the land we explored devours its inhabitants, and all its people are of great stature.", "The Hebrew 'bad report'; the Greek 'brought dismay' (ekstasis).",
   ["A bad report.", "A land that devours.", "Men of great stature."], "The land was slandered.", "'A land that devours its inhabitants': the land of milk and honey turned into a mouth. The spies make the gift a monster.",
   [loses("Hebrew 'spread a bad report' is lost."), keeps("Greek 'brought dismay concerning the land'."), between("The Latin has 'disparaged'; the King James 'an evil report'.")], ['canaan']),
  '13:33': v("There we saw the Nephilim, the sons of Anak from the Nephilim; we seemed grasshoppers in our own eyes, and so we were in theirs.",
   "The Hebrew gives the Anakite genealogy and both perspectives; the Greek 'giants … like grasshoppers before them, and indeed so we were before them'.",
   ["The Nephilim.", "Sons of Anak.", "Grasshoppers."], "The spies saw themselves as grasshoppers.", "'In our own eyes': the fear is of their own smallness first; the giants are what grasshoppers see. The Greek dropped the Genesis 6 lineage and kept only 'giants'.",
   [loses("Hebrew 'the Nephilim—the sons of Anak come from the Nephilim … in our own eyes' is lost."), keeps("Greek 'the giants … like grasshoppers before them, and indeed so we were before them'."), between("The Latin has 'monstrous men of giant stock'; the King James 'giants, the sons of Anak'.")], ['nephilim', 'anakim', 'ancient-giants']),
 },
}
