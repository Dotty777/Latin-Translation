K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
WEST = [loses("Hebrew 'plains of Moab' is lost."), keeps("Greek 'on the western side of Moab'."), between("The Latin and King James have 'plains of Moab'.")]
DESTROY = [loses("Hebrew 'dispossess the inhabitants' is lost."), keeps("Greek 'destroy all who inhabit the land'."), between("The Latin and King James have 'drive out' / 'destroy' in different places.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

def name(heb, grk):
    return [loses(f"Hebrew '{heb}' is lost in form."), keeps(f"Greek '{grk}'."), between(f"The Latin and King James follow the Hebrew form '{heb}'.")]

def stage(frm, to, w, lost=None, explain="The stations agree; only the Greek spelling differs.", extra="", entries=None):
    return v(f"They set out from {frm} and camped at {to}{extra}.", explain, [f"From {frm}.", f"To {to}.", "A stage."], f"From {frm} to {to}.", w, lost if lost is not None else [AGREE], entries or [])

STAGES = {
  '33:5': stage("Rameses", "Succoth", "The first stage: Succoth, 'booths', the first night out of Egypt, remembered every year in the feast of that name.", [between("The Greek restates 'they set out from Rameses'.")], entries=['egypt']),
  '33:6': stage("Succoth", "Etham", "Etham at the desert's edge: the point where Egypt's fields end and the wilderness begins, and the pillar of cloud first leads.", name("Etham, at the edge of the wilderness", "Bouthan, a part of the wilderness"), "The Greek 'Bouthan, a part of the wilderness'; the Hebrew 'Etham, at the edge'.", ", at the edge of the wilderness"),
  '33:7': v("They set out from Etham and turned back toward Pi-hahiroth, opposite Baal-zephon, and camped before Migdol.", "The Greek replaces the turning back with a camping notice and part-translates 'mouth of Eiroth'.",
   ["From Etham.", "Turned back to Pi-hahiroth.", "Before Migdol."], "They turned back to the sea.", "'Turned back': the one stage that goes the wrong way, by God's design, to draw Pharaoh after them to the sea (Exodus 14:2).",
   [loses("Hebrew 'turned back toward Pi-hahiroth' is lost."), keeps("Greek 'camped at the mouth of Eiroth'."), between("The Latin and King James have 'turned back'.")], ['baal']),
  '33:8': v("They set out from before Hahiroth and crossed through the midst of the sea into the wilderness; they went three days through the wilderness of Etham and camped at Marah.", "The Greek lacks 'Etham' and translates Marah as 'Bitternesses'.",
   ["Through the midst of the sea.", "Three days in the wilderness.", "Camped at Marah."], "The sea crossing is one line.", "Exodus 14 in a clause: 'crossed through the midst of the sea'. The itinerary is a list, not a story; the greatest deliverance in the book is a stage between two camps.",
   [loses("Hebrew 'wilderness of Etham … Marah' is lost."), keeps("Greek 'through the wilderness … Bitternesses' (Pikriai), translating the name."), between("The Latin and King James have 'Etham' and 'Marah'.")], ['egypt']),
  '33:9': v("They set out from Marah and came to Elim; at Elim were twelve springs and seventy palms, and they camped there.", "The Greek adds 'beside the water'.",
   ["From Marah to Elim.", "Twelve springs.", "Seventy palms."], "Elim had water and shade.", "Twelve springs, seventy palms: the numbers of the tribes and of the elders, and the first rest after bitter water.", [keeps("Greek adds 'and they camped there beside the water'.")]),
  '33:10': stage("Elim", "the Sea of Reeds", "Back to the sea they crossed, this time to camp beside it: the route hugs the Gulf of Suez before turning inland.", [loses("Hebrew yam suph, 'Sea of Reeds', is lost."), keeps("Greek 'Red Sea'."), between("The Latin and King James have 'Red Sea'.")], "The Hebrew 'Sea of Reeds'; the Greek and the rest 'Red Sea'."),
  '33:11': stage("the Sea of Reeds", "the wilderness of Sin", "The wilderness of Sin, where the manna began (Exodus 16): the list does not mention it.", [between("The Latin carries the departure into the previous verse; the sea-name difference continues.")]),
  '33:12': stage("the wilderness of Sin", "Dophkah", "Dophkah and Alush appear nowhere else: stations the narrative skipped, preserved only by the list.", name("Dophkah", "Raphaka"), "The Greek 'Raphaka'."),
  '33:13': stage("Dophkah", "Alush", "Alush, unknown; a name kept because it was a night Israel slept somewhere.", name("Dophkah", "Raphaka"), "The Greek 'Raphaka' for the departure."),
  '33:14': stage("Alush", "Rephidim", "Rephidim: the rock struck for water and the battle with Amalek (Exodus 17). The list remembers only the thirst.", [AGREE], "All four columns agree.", ", where there was no water for the people to drink", ['rock']),
  '33:15': stage("Rephidim", "the wilderness of Sinai", "Sinai, where they stayed a year: the covenant, the tabernacle, the census. One line for the longest camp.", [AGREE], "All four columns agree.", "", ['sinai']),
  '33:16': stage("the wilderness of Sinai", "Kibroth-hattaavah", "'Graves of Craving' (chapter 11): the quail and the plague, named for the dead it left.", [loses("Hebrew 'Kibroth-hattaavah' as a name is lost."), keeps("Greek 'Graves of Desire', translating the name."), between("The Latin has 'Graves of Lust'; the King James 'Kibroth-hattaavah'.")], "The Greek translates the name."),
  '33:17': stage("Kibroth-hattaavah", "Hazeroth", "Hazeroth: Miriam's leprosy and seven days' wait (chapter 12).", [between("The Greek 'Graves of Desire' continues for the departure.")], "The translated name continues.", "", ['miriam']),
  '33:18': stage("Hazeroth", "Rithmah", "Rithmah, the 'broom-plant' camp, probably near Kadesh: from here the spies went out and the forty years began.", [AGREE], "All four columns agree."),
  '33:19': stage("Rithmah", "Rimmon-perez", "The wilderness years begin: seventeen stations from here to Kadesh again, and the narrative covers none of them.", [AGREE], "All four columns agree."),
  '33:20': stage("Rimmon-perez", "Libnah", "Libnah, 'white'; a name and nothing else.", name("Libnah", "Lemona"), "The Greek 'Lemona'."),
  '33:21': stage("Libnah", "Rissah", "Rissah; the list is the only record of thirty-eight years of a nation's life.", name("Rissah", "Dessa"), "The Greek 'Dessa'."),
  '33:22': stage("Rissah", "Kehelathah", "Kehelathah, 'assembly': perhaps a camp where the people gathered, perhaps only a name.", name("Kehelathah", "Makellath"), "The Greek 'Makellath'."),
  '33:23': stage("Kehelathah", "Mount Shepher", "Mount Shepher, 'beauty': the one station in the middle stretch called a mountain.", [loses("Hebrew 'Mount Shepher' is lost."), keeps("Greek 'Shaphar', without 'Mount'."), between("The Latin and King James have 'Mount Shapher'.")], "The Greek lacks 'Mount'."),
  '33:24': stage("Mount Shepher", "Haradah", "Haradah, 'trembling'; some read the names of these years as a map of moods.", [between("The Greek lacks 'Mount' for the departure.")], "The Greek lacks 'Mount'."),
  '33:25': stage("Haradah", "Makheloth", "Makheloth, 'assemblies'.", [AGREE], "All four columns agree."),
  '33:26': stage("Makheloth", "Tahath", "Tahath, 'below'.", name("Tahath", "Kataath"), "The Greek 'Kataath'."),
  '33:27': stage("Tahath", "Terah", "Terah, the name of Abraham's father, borne by a camp in the desert.", name("Terah", "Tarath"), "The Greek 'Tarath'.", "", ['abraham']),
  '33:28': stage("Terah", "Mithkah", "Mithkah, 'sweetness': after Marah's bitterness at the start, a sweet-water camp in the middle years.", [between("The Greek 'Tarath' continues for the departure.")], "The Greek 'Tarath' for the departure."),
  '33:29': stage("Mithkah", "Hashmonah", "Hashmonah, the name the Hasmoneans would later bear.", name("Hashmonah", "Selmona"), "The Greek 'Selmona', the same name it uses at 33:41."),
  '33:30': stage("Hashmonah", "Moseroth", "Moseroth, 'bonds' or 'chastisements'; Deuteronomy 10:6 places Aaron's death near Moserah, a tradition the list does not follow.", [between("The Greek 'Selmona' for the departure.")], "The Greek 'Selmona' for the departure."),
  '33:31': stage("Moseroth", "Bene-jaakan", "Bene-jaakan, 'the sons of Jaakan', a clan of Seir (1 Chronicles 1:42): the camp is at someone's wells.", name("Bene-jaakan", "Banaia"), "The Greek 'Banaia'."),
  '33:32': stage("Bene-jaakan", "Hor-haggidgad", "Hor-haggidgad, 'the hollow of Gidgad'; the Greek makes it a mountain.", [keeps("Greek 'Mount Gadgad' for 'Hor-haggidgad'."), between("The Latin and King James have 'Hor-hagidgad'.")], "The Greek 'Banaia' and 'Mount Gadgad'."),
  '33:33': stage("Hor-haggidgad", "Jotbathah", "Jotbathah, 'pleasantness', 'a land of brooks' in Deuteronomy 10:7.", [between("The Greek 'Mount Gadgad' for the departure.")], "The Greek 'Mount Gadgad' for the departure."),
  '33:34': stage("Jotbathah", "Abronah", "Abronah, 'passage'; the route is now descending toward the gulf of Aqaba.", [AGREE], "All four columns agree."),
  '33:35': stage("Abronah", "Ezion-geber", "Ezion-geber, Solomon's later port on the Red Sea: the wanderers reached the shore of the eastern gulf.", [AGREE], "All four columns agree."),
  '33:36': v("They set out from Ezion-geber and camped in the wilderness of Zin, that is, Kadesh.", "The Greek adds a stage: to the wilderness of Sin, then to Paran, that is Kadesh.",
   ["From Ezion-geber.", "The wilderness of Zin.", "That is, Kadesh."], "They returned to Kadesh.", "Kadesh again, in the fortieth year: Miriam's death, the struck rock, the refusal of Edom (chapter 20). The circle of the wilderness closes where it opened.",
   [keeps("Greek adds 'and they set out from the wilderness of Sin and camped in the wilderness of Paran, that is Kadesh'."), between("The Latin and King James go directly to the wilderness of Zin, that is Kadesh.")]),
  '33:37': v("They set out from Kadesh and camped at Mount Hor, at the edge of the land of Edom.", "The Latin 'at the farthest border of Edom'; the Greek 'near the land of Edom'.",
   ["From Kadesh.", "Mount Hor.", "The edge of Edom."], "Mount Hor was the next camp.", "Mount Hor on Edom's border: the list pauses here, the only station given a story, because Aaron died on it.", [between("The Latin has 'the farthest border of Edom'; the Greek 'near the land of Edom'.")]),
  '33:41': stage("Mount Hor", "Zalmonah", "After Aaron, the road south and east around Edom begins; Zalmonah may be the camp of the bronze serpent.", [AGREE], "All four columns agree.", "", ['bronze-serpent']),
  '33:42': stage("Zalmonah", "Punon", "Punon, the copper-mining district of Edom's Arabah, which some connect with the bronze of the serpent.", name("Punon", "Phino"), "The Greek 'Phino'."),
  '33:43': stage("Punon", "Oboth", "Oboth (21:10): the list and the narrative meet again.", [between("The Greek 'Phino' for the departure.")], "The Greek 'Phino' for the departure."),
  '33:44': stage("Oboth", "Iye-abarim", "Iye-abarim, 'the ruins of the crossings', on Moab's border (21:11): Israel has rounded Edom and faces north.", [loses("Hebrew 'Iye-abarim' is lost."), keeps("Greek 'Gai, on the other side, at the borders of Moab'."), between("The Latin and King James have 'Ije-abarim'.")], "The Greek 'Gai' and translates the crossing element.", ", on the border of Moab"),
  '33:45': stage("Iyim", "Dibon-gad", "Dibon-gad: already named for Gad, the tribe that will rebuild it (32:34); the list speaks from after the settlement.", [between("The Hebrew shortens the name to 'Iyim'; the Greek keeps 'Gai'.")], "The Hebrew shortens to 'Iyim'; the Greek 'Gai'."),
  '33:46': stage("Dibon-gad", "Almon-diblathaim", "Almon-diblathaim, the Beth-diblathaim of Jeremiah 48:22, in the heart of Moab's plateau.", name("Almon-diblathaim", "Gelmon-diblathaim"), "The Greek 'Gelmon'."),
  '33:47': stage("Almon-diblathaim", "the mountains of Abarim, before Nebo", "The mountains of Abarim before Nebo: the heights from which Moses will see the land and on which he will die (Deuteronomy 32:49).", [between("The Greek 'Gelmon' for the departure.")], "The Greek 'Gelmon' for the departure.", "", ['moses']),
  '33:48': stage("the mountains of Abarim", "the plains of Moab, by the Jordan opposite Jericho", "The last stage: the plains of Moab, where the book has been since chapter 22. Forty-two camps from Rameses to the Jordan.", WEST, "The Greek 'on the western side of Moab'.", "", ['jordan', 'jericho']),
  '33:49': v("They camped by the Jordan from Beth-jeshimoth to Abel-shittim, on the plains of Moab.", "The Greek has shortened name-forms and 'western side' for 'plains'.",
   ["By the Jordan.", "Beth-jeshimoth to Abel-shittim.", "The plains of Moab."], "The camp stretched along the Jordan.", "Abel-shittim, 'the acacia meadow', is the Shittim of Peor (25:1) and of Joshua's spies (Joshua 2:1): the last camp is the camp of the last sin and the first step into the land.", WEST, ['jordan']),
}

VERSES = {
  '33:1': v("These are the stages of the Israelites who came out of Egypt by their companies under Moses and Aaron.", "The Hebrew 'stages of departure'; the Greek 'stopping places'.",
   ["The stages of Israel.", "Out of Egypt.", "Under Moses and Aaron."], "The itinerary is introduced.", "Forty years in forty-two names: the chapter is the book's memory of where it slept. 'Under Moses and Aaron': Aaron is dead by the list's end, and the heading still gives him his place.",
   [between("The Hebrew has 'stages' (masa'ot, departures); the Greek 'stations' (stathmoi).")], ['moses', 'high-priest', 'egypt']),
  '33:2': v("Moses wrote down their departures by their stages at YHWH's command; these are their stages by their departures.", "The Latin 'recorded the camp sites, changed at the Lord's command'; the Greek coordinates departures and stations and adds a closing sentence.",
   ["Moses wrote them down.", "At YHWH's command.", "Stage by stage."], "The list is Moses' record.", "'Moses wrote': one of the few places the Torah says Moses wrote something, and what he wrote was a list of campsites. God wanted the route remembered, not just the events on it.",
   [between("The Latin has 'which they changed at the command of the Lord'; the Greek adds 'these are the stations of their journey'.")], ['moses', 'yhwh-yahweh', 'scroll']),
  '33:3': v("They set out from Rameses in the first month, on the fifteenth day; on the day after Passover the Israelites went out with a high hand in the sight of all Egypt,", "All four columns agree; 'with a high hand' in all.",
   ["From Rameses.", "The fifteenth of the first month.", "With a high hand before Egypt."], "The exodus is dated.", "'With a high hand': not fugitives but a people marching out in daylight under a raised arm. The date is Passover's morrow, the one date the whole calendar hangs on.", [AGREE], ['egypt', 'passover-lamb']),
  '33:4': v("while the Egyptians were burying all their firstborn whom YHWH had struck down; and YHWH had executed judgments on their gods.", "The Greek adds 'in the land of Egypt' and calls the action 'vengeance' rather than 'judgments'.",
   ["Egypt burying its firstborn.", "YHWH struck them.", "Judgments on their gods."], "Egypt buried its dead as Israel left.", "Two processions on one morning: Israel marching out, Egypt carrying its firstborn to the tombs. 'Judgments on their gods': the plagues were a trial of Egypt's pantheon, and the verdict was given.",
   [loses("Hebrew 'executed judgments' is lost."), keeps("Greek 'took vengeance on their gods … all their dead, every firstborn in the land of Egypt'."), between("The Latin has 'executed judgment'; the King James 'executed judgments'.")], ['plague-10', 'gods', 'yhwh-yahweh']),
  '33:38': v("Aaron the priest went up Mount Hor at YHWH's command and died there in the fortieth year after Israel came out of Egypt, in the fifth month, on the first day.", "The Greek omits the repeated 'Mount Hor' here and names it in the next verse.",
   ["Aaron went up at YHWH's command.", "He died there.", "The fortieth year, fifth month, first day."], "Aaron's death is dated.", "The only dated death in the list, and the only date between the exodus and the Jordan: the fortieth year, the fifth month, the first day. Aaron's death marks the end of the wandering as the exodus marked its beginning.",
   [between("The Latin names Mount Hor in this verse; the Greek in the next.")], ['high-priest', 'yhwh-yahweh', 'egypt']),
  '33:39': v("Aaron was 123 years old when he died on Mount Hor.", "The Greek names Aaron again and adds 'on Mount Hor'.",
   ["Aaron was 123.", "When he died.", "On Mount Hor."], "Aaron died at 123.", "Three years older than Moses, who will die at 120 within the year: the brothers born in Egypt's bondage both die on mountains at the edge of the land.", [between("The Greek repeats 'Aaron' and adds 'he died on Mount Hor'.")], ['high-priest']),
  '33:40': v("The Canaanite king of Arad, who lived in the Negev in the land of Canaan, heard of the Israelites' coming.", "The Greek omits 'the Negev'.",
   ["The king of Arad.", "In the Negev.", "Heard of Israel's coming."], "Arad's king heard.", "A fragment of 21:1 dropped into the list without its battle: the editor marks that Israel's approach was known in the land, and moves on.",
   [loses("Hebrew 'in the Negev' is lost."), keeps("Greek 'who lived in the land of Canaan'."), between("The Latin has 'in the south'; the King James 'in the south in the land of Canaan'.")], ['canaan']),
  '33:50': v("YHWH spoke to Moses on the plains of Moab by the Jordan opposite Jericho:", "The Greek 'western side of Moab' and adds 'saying'.",
   ["YHWH spoke.", "On the plains of Moab.", "By the Jordan."], "YHWH spoke at the Jordan.", "The list ends and the law resumes, at the river's edge: what to do once across.", FORMULA + WEST, ['yhwh-yahweh', 'moses', 'jordan', 'jericho']),
  '33:51': v("Speak to the Israelites: when you cross the Jordan into the land of Canaan,", "The Latin 'when you cross'; the Greek 'you are crossing'.",
   ["Speak to Israel.", "When you cross the Jordan.", "Into Canaan."], "Instructions for after the crossing.", "'When you cross': not if. The forty-two stages have made the crossing a certainty; the question now is what Israel does with the land.", [between("The Latin and King James have 'when ye are passed over'; the Greek 'you are crossing'.")], ['jordan', 'canaan']),
  '33:52': v("drive out all the inhabitants of the land before you, destroy all their figured stones, destroy all their cast images and demolish all their high places.", "The Greek 'destroy the inhabitants' for 'dispossess', and 'lookout places and pillars' for 'figured stones and high places'.",
   ["Drive out the inhabitants.", "Destroy their images.", "Demolish their high places."], "Canaan's cult was to be razed.", "Three objects: carved stones, cast metal, high places. The command is against a religion more than a people; the inhabitants are to be driven out, their gods destroyed. The Greek hardens the first verb.", DESTROY + [between("The Greek has 'lookout places (skopias) and pillars'; the Hebrew 'figured stones … high places'.")], ['gods'], "Drive out the inhabitants, destroy their images and demolish their high places."),
  '33:53': v("Take possession of the land and settle in it, for I have given you the land to possess.", "The Greek repeats 'destroy all who inhabit the land'; the Latin 'clearing the land'.",
   ["Take possession.", "Settle in it.", "I have given you the land."], "The land is given to be held.", "'I have given': the perfect tense of a gift already made. Possession is Israel's act, but the giving is God's and is finished before they cross.", DESTROY, ['canaan'], "Take possession of the land and settle in it."),
  '33:54': v("Inherit the land by lot by your clans: to the larger a larger inheritance, to the smaller a smaller; wherever the lot falls for anyone shall be his; inherit by your ancestral tribes.", "The Greek 'tribes' for 'clans' in the first clause and 'wherever his name comes out' for the lot falling.",
   ["By lot.", "Larger to the larger.", "By your ancestral tribes."], "The land goes by lot and by size.", "Lot and proportion together, as in 26:52–56: chance decides where, size decides how much. No tribe chooses its land, and no tribe is shortchanged by chance.",
   [between("The Greek has 'wherever his name comes out'; the Hebrew 'wherever the lot falls'.")], [], "Divide the land by lot according to your tribes, proportioned to their size."),
  '33:55': v("But if you do not drive out the inhabitants before you, those you leave will be barbs in your eyes and thorns in your sides, and will trouble you in the land where you live.", "The Greek 'destroy' and 'missiles' for 'thorns'.",
   ["If you do not drive them out.", "Barbs in your eyes.", "Thorns in your sides."], "Half-measures would wound Israel.", "'Barbs in your eyes and thorns in your sides': the warning Judges will fulfil to the letter. A tolerated Canaanite religion is a splinter the body cannot stop feeling.",
   DESTROY + [between("The Greek has 'splinters in your eyes and missiles in your sides'; the Latin 'nails and spears'; the King James 'pricks … thorns'.")], []),
  '33:56': v("Then I will do to you what I intended to do to them.", "All four columns agree.",
   ["Then I will do to you.", "What I intended.", "To do to them."], "Israel could suffer Canaan's fate.", "The chapter's last word turns the conquest round: the God who gives the land will take it back on the same terms. Israel is not exempt from the judgement it carries, and the exile will prove it.", [AGREE], ['yhwh-yahweh']),
}
VERSES.update(STAGES)

CHAPTER = {
 'slug': 'numbers', 'chapter': 33,
 'chapterNote': "The itinerary. Moses writes at YHWH's command the forty-two stages from Rameses to the plains of Moab: out of Egypt on Passover's morrow with a high hand while Egypt buried its firstborn; Succoth, Etham, the turn to Pi-hahiroth, through the sea to Marah and Elim; Sinai, the Graves of Craving, Hazeroth; seventeen unknown stations of the wilderness years; Kadesh, Mount Hor, where Aaron died at 123 in the fortieth year, fifth month, first day; round Edom by Zalmonah, Punon and Oboth to Moab's border; the mountains of Abarim; the Jordan camp from Beth-jeshimoth to Abel-shittim. Then the command for the crossing: drive out the inhabitants, destroy their images and high places, divide by lot and size, or those left will be barbs and thorns and Israel will suffer their fate. The Greek has 'stations' for 'stages' (33:1–2), 'vengeance' for 'judgments' (33:4), 'Bouthan' (33:6–7), drops the turning back (33:7), translates Marah as 'Bitternesses' (33:8) and Kibroth-hattaavah as 'Graves of Desire' (33:16), 'Red Sea' for 'Sea of Reeds' (33:10–11), respells many stations (Raphaka, Lemona, Dessa, Makellath, Shaphar, Kataath, Tarath, Selmona, Banaia, Phino, Gai, Gelmon), lacks 'Mount' at Shepher and adds it at Gidgad, inserts a Paran stage (33:36), omits the Negev (33:40), has 'western side of Moab' for 'plains of Moab' (33:48–50), 'destroy' for 'dispossess' (33:52–55), and 'missiles' for 'thorns' (33:55).",
 'verses': VERSES,
}
