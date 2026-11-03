K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
ORDER = [between("The Greek places this tribe at a different point in its list (Judah, Issachar and Zebulun before Gad; Asher after Gad); the source aligns by tribe and the numbers agree.")]
SAME = [between("All four columns give the same number.")]
CLANS = [between("All four columns name the same ancestors and clans; spelling differs.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

def names(ref, tribe, text, wis, diff=None):
    if diff:
        return v(text, (diff[0][0] if isinstance(diff[0], list) else diff[0]), [f"{tribe}'s clans.", "Named.", "Ancestor and clan."], f"{tribe}'s clans were listed.", wis, diff[1] + ORDER if tribe in ('Judah','Issachar','Zebulun','Gad','Asher','Manasseh','Ephraim','Benjamin','Dan') else diff[1])
    return v(text, "All four columns agree.", [f"{tribe}'s clans.", "Named.", "Ancestor and clan."], f"{tribe}'s clans were listed.", wis, CLANS + (ORDER if tribe in ('Judah','Issachar','Zebulun','Gad','Asher','Manasseh','Ephraim','Benjamin','Dan') else []))

def total(ref, tribe, n, wis, first=None):
    return v(f"These were {tribe}'s clans: {n}.", "All four columns agree on the number.", [f"{tribe}.", f"{n[0].upper()+n[1:]}.", "The same in every column."], f"{tribe} numbered {n}.", wis, SAME + (ORDER if tribe in ('Judah','Issachar','Zebulun','Gad','Asher','Manasseh','Ephraim','Benjamin') else []))

CHAPTER = {
 'slug': 'numbers', 'chapter': 26,
 'chapterNote': "The second census, after the plague, in the plains of Moab by Moses and Eleazar: every man of twenty and up by clan. Reuben 43,730 (with Dathan and Abiram's fate recalled, and 'Korah's sons did not die'), Simeon 22,200, Gad 40,500, Judah 76,500, Issachar 64,300, Zebulun 60,500, Manasseh 52,700 (with Zelophehad's five daughters), Ephraim 32,500, Benjamin 45,600, Dan 64,400, Asher 53,400 (with Serah), Naphtali 45,400: total 601,730, against 603,550 forty years before. The land is to be divided by lot in proportion to numbers. The Levites, 23,000 from one month old, with Jochebed, Aaron's sons and the fire. Not one man of the first census remains except Caleb and Joshua. The Greek lacks 'son of Aaron' (26:1), orders the tribes Reuben, Simeon, Judah, Issachar, Zebulun, Gad, Asher, Manasseh, Ephraim, Benjamin, Dan, Naphtali (the source aligns by tribe), lacks the repeated 'Dathan and Abiram' (26:9), has 'Iamun' for Hamul (26:17), 'Addi' for Eri (26:25), 'Jamin' for Imnah (26:28), omits 'the sons of Beriah' (26:29), 'Ahiezer' for Iezer (26:34), 'Symaer' for Shemida (26:36), omits Becher and has 'Tanach' for Tahan (26:39), 'Eden' for Eran (26:40), 'Asyber … Iachiran' (26:42), omits Hupham (26:43), 'Adar' for Ard (26:44), 'Sami' for Shuham (26:46–47), 'Asiel' for Jahzeel (26:48), 'you shall divide' (26:56), omits the Mahlite clan and reorders (26:58), makes Jochebed the mother who 'bore these to Levi' (26:59), adds 'in the wilderness of Sinai' (26:61), and lacks Aaron's title (26:64). All totals agree in every column.",
 'verses': {
  '26:1': v("After the plague, YHWH said to Moses and Eleazar son of Aaron the priest:", "The Greek lacks 'son of Aaron'. The Hebrew's 25:19 'after the plague' is included here.",
   ["After the plague.", "YHWH to Moses.", "And Eleazar."], "A new census was ordered.", "'After the plague': Peor's dead are the last of the old generation, and the count that follows is of the survivors. Eleazar stands where Aaron stood in chapter 1.",
   [loses("Hebrew 'son of Aaron' is lost."), keeps("Greek 'Eleazar the priest'.")], ['yhwh-yahweh', 'moses', 'high-priest']),
  '26:2': v("Take a census of the whole congregation from twenty years old, by ancestral houses, everyone fit for service.", "All four columns agree; the Greek singular 'take'.",
   ["A census.", "From twenty.", "Fit for service."], "The muster was repeated.", "The same words as 1:2–3, forty years on, to men who were children then.", [keeps("Greek singular 'take'.")], [], "Take a census of the whole congregation."),
  '26:3': v("Moses and Eleazar spoke with them in the plains of Moab by the Jordan opposite Jericho:", "The Greek lacks 'with them' and transliterates 'Araboth'.",
   ["Moses and Eleazar.", "In the plains of Moab.", "By the Jordan."], "The count was taken at the Jordan.", "Counted at Sinai going out, counted at the Jordan going in; the two censuses frame the wilderness.",
   [keeps("Greek 'in Araboth of Moab' without 'with them'.")], ['moses', 'high-priest', 'jordan', 'jericho']),
  '26:4': v("From twenty years old, as YHWH commanded Moses and the Israelites who came out of Egypt.", "Both are compressed; the Greek 'These are the sons of Israel who came out of Egypt'.",
   ["From twenty.", "As YHWH commanded.", "Those who came out of Egypt."], "The census list began.", "'Who came out of Egypt': said of a people almost none of whom did; the children are counted under their fathers' title.",
   [keeps("Greek 'These are the sons of Israel who came out of Egypt'.")], ['egypt', 'yhwh-yahweh']),
  '26:5': names('26:5', 'Reuben', "Reuben, Israel's firstborn: from Hanoch the Hanochite clan, from Pallu the Palluite clan;", "Reuben first again, by birth; the clans are Genesis 46's names made families."),
  '26:6': names('26:6', 'Reuben', "From Hezron the Hezronite clan, from Carmi the Carmite clan.", "Four clans, as in Genesis; Reuben's house has not grown branches."),
  '26:7': total('26:7', 'Reuben', 'forty-three thousand seven hundred thirty', "Down 2,770 from Sinai; the firstborn's tribe shrank in the wilderness."),
  '26:8': v("The sons of Pallu: Eliab.", "All four columns agree; the Latin singular 'son'.", ["Pallu's sons.", "Eliab.", "One name."],
   "Eliab was named for a reason.", "Eliab named alone, so that his sons may be named; the census pauses for a story.", [between("The Latin has 'the son' singular.")]),
  '26:9': v("Eliab's sons: Nemuel, Dathan and Abiram; these were Dathan and Abiram, chosen men who contended against Moses and Aaron in Korah's company against YHWH.", "The Greek lacks the repeated 'Dathan and Abiram'.",
   ["Nemuel, Dathan, Abiram.", "Chosen men.", "Contended against YHWH."], "The rebels were recorded.", "The census writes the rebels into the roll, dead; a genealogy that remembers who went down into the earth.",
   [loses("Hebrew's repeated 'These were Dathan and Abiram' is lost."), keeps("Greek 'these … summoned members of the congregation'.")], ['moses', 'high-priest', 'yhwh-yahweh']),
  '26:10': v("The earth opened its mouth and swallowed them with Korah when the company died, when the fire consumed 250 men; they became a sign.", "All four columns agree; 'his congregation' in Greek.",
   ["The earth swallowed them.", "With Korah.", "A warning sign."], "Korah's fate was recalled.", "'They became a sign': the dead of chapter 16 are entered in the register as a warning, the one function the dead still serve.", [keeps("Greek 'his congregation'.")]),
  '26:11': v("But Korah's sons did not die.", "All four columns agree. Rashi credits their repentance.",
   ["Korah's sons.", "Did not die.", "Survived."], "Korah's line survived.", "Five Hebrew words, and from them the sons of Korah who wrote eleven psalms; the rebel's children sang in the temple he wanted to seize.", [AGREE]),
  '26:12': names('26:12', 'Simeon', "Simeon's sons by clans: from Nemuel the Nemuelite, from Jamin the Jaminite, from Jachin the Jachinite;", "Simeon's clans begin; one Genesis name, Ohad, is gone from the list.", (["All four columns agree; the Greek repeats 'the sons of Simeon'."], [keeps("Greek repeats the heading.")])),
  '26:13': names('26:13', 'Simeon', "From Zerah the Zerahite clan, from Shaul the Shaulite clan.", "Five clans where Genesis had six."),
  '26:14': total('26:14', 'Simeon', 'twenty-two thousand two hundred', "From 59,300 to 22,200: Simeon lost 37,100 men, the largest fall of any tribe; Zimri's tribe paid for Peor."),
  '26:15': v("Gad's sons by clans: from Zephon the Zephonite, from Haggi the Haggite, from Shuni the Shunite;", "The Greek places Gad after Zebulun (its 26:24).",
   ["Gad's clans.", "Zephon, Haggi.", "Shuni."], "Gad's clans were listed.", "Gad third in the Hebrew, as in the camp beside Reuben and Simeon; the Greek moved him down the list.", CLANS + ORDER),
  '26:16': v("From Ozni the Oznite clan, from Eri the Erite clan;", "The Greek 'Addi' for Eri.",
   ["Gad's clans.", "Ozni.", "Eri."], "More Gadite clans.", "Ozni for Genesis's Ezbon; the clan names shift between the lists.", ORDER + [loses("Hebrew 'Eri' is lost."), keeps("Greek 'Addi'.")]),
  '26:17': v("From Arod the Arodite clan, from Areli the Arelite clan.", "The Greek 'Ariel'.",
   ["Gad's clans.", "Arod.", "Areli."], "Gad's seven clans closed.", "Seven clans for Gad, the most of any tribe but Manasseh.", ORDER + [keeps("Greek 'Ariel' for Areli.")]),
  '26:18': total('26:18', 'Gad', 'forty thousand five hundred', "Down 5,150; Gad will ask for Sihon's land rather than cross the river."),
  '26:19': v("Judah's sons were Er and Onan; Er and Onan died in Canaan.", "The Greek places Judah after Simeon (its 26:15).",
   ["Er and Onan.", "Judah's sons.", "Died in Canaan."], "Judah's dead sons were recalled.", "Genesis 38 in a line: the two who died before Egypt, remembered in a count of those who will enter after it.", ORDER, ['canaan']),
  '26:20': names('26:20', 'Judah', "Judah's sons by clans: from Shelah the Shelanite, from Perez the Perezite, from Zerah the Zerahite.", "Perez, Tamar's son, the clan of David and the Messiah; the census does not know it yet.", (["The Greek 'Shelon'."], [keeps("Greek 'Shelon' for Shelah.")])),
  '26:21': names('26:21', 'Judah', "Perez's sons: from Hezron the Hezronite clan, from Hamul the Hamulite clan.", "Hezron, Ruth 4's Hezron, five generations from David; the royal line is a sub-clan here.", (["The Greek 'Iamun' for Hamul."], [loses("Hebrew 'Hamul' is lost."), keeps("Greek 'Iamun'.")])),
  '26:22': total('26:22', 'Judah', 'seventy-six thousand five hundred', "Up 1,900; Judah grew in the wilderness and is the largest tribe by far, as the camp's order implied."),
  '26:23': names('26:23', 'Issachar', "Issachar's sons by clans: from Tola the Tolaite, from Puah the Punite;", "Puah's clan is the Punite; the Hebrew's small irregularity the Greek smoothed.", (["The Hebrew 'Puah … Punite'; the Greek derives directly."], [keeps("Greek derives the clan from Puah.")])),
  '26:24': names('26:24', 'Issachar', "From Jashub the Jashubite clan, from Shimron the Shimronite clan.", "Jashub for Genesis's Iob; four clans."),
  '26:25': total('26:25', 'Issachar', 'sixty-four thousand three hundred', "Up 9,900, the second-largest growth; the strong donkey grew strong."),
  '26:26': names('26:26', 'Zebulun', "Zebulun's sons by clans: from Sered the Seredite, from Elon the Elonite, from Jahleel the Jahleelite.", "Three clans, Genesis's three names.", (["The Greek 'Allon … Allel'."], [keeps("Greek 'Allon' and 'Allel'.")])),
  '26:27': total('26:27', 'Zebulun', 'sixty thousand five hundred', "Up 3,100; the sea-tribe prospered inland."),
  '26:28': v("Joseph's sons by clans: Manasseh and Ephraim.", "All four columns agree; the Greek places Asher before Joseph.",
   ["Joseph's sons.", "Manasseh.", "Ephraim."], "Joseph's two tribes began.", "Joseph counted as two; Manasseh first this time, the elder before the younger, unlike chapter 1.", ORDER, ['joseph-son-of-jacob']),
  '26:29': names('26:29', 'Manasseh', "Manasseh's sons: from Machir the Machirite clan; Machir begat Gilead; from Gilead the Gileadite clan.", "Machir and Gilead: the clan will take the land named Gilead east of Jordan, and the name will be geography."),
  '26:30': names('26:30', 'Manasseh', "Gilead's sons: from Iezer the Iezerite clan, from Helek the Helekite clan;", "Iezer, Gideon's clan, Abiezer in Judges.", (["The Greek 'Ahiezer'."], [loses("Hebrew 'Iezer' is lost."), keeps("Greek 'Ahiezer'.")])),
  '26:31': names('26:31', 'Manasseh', "From Asriel the Asrielite clan, from Shechem the Shechemite clan;", "Shechem a clan-name in Manasseh before it is a city in Ephraim's hills."),
  '26:32': names('26:32', 'Manasseh', "From Shemida the Shemidaite clan, from Hepher the Hepherite clan.", "Hepher, father of Zelophehad; the next verse's daughters descend from here.", (["The Greek 'Symaer' for Shemida."], [loses("Hebrew 'Shemida' is lost."), keeps("Greek 'Symaer'.")])),
  '26:33': v("Zelophehad son of Hepher had no sons, only daughters: Mahlah, Noah, Hoglah, Milcah and Tirzah.", "All four columns agree.",
   ["Zelophehad.", "No sons.", "Five daughters named."], "Five daughters were named in the roll.", "Five women named in a census of men: Zelophehad's daughters, who in the next chapter will change the law of inheritance by asking.", [AGREE]),
  '26:34': total('26:34', 'Manasseh', 'fifty-two thousand seven hundred', "Up 20,500, from the smallest tribe to the sixth-largest; Manasseh's was the great growth of the forty years."),
  '26:35': v("Ephraim's sons by clans: from Shuthelah the Shuthelahite, from Becher the Becherite, from Tahan the Tahanite.", "The Greek lacks Becher and has 'Tanach'.",
   ["Ephraim's clans.", "Shuthelah, Becher.", "Tahan."], "Ephraim's clans were listed.", "Three clans in the Hebrew, two in the Greek; Becher dropped out of a list somewhere between the texts.",
   ORDER + [loses("Hebrew 'from Becher, the Becherite clan … Tahan' is lost."), keeps("Greek 'Shuthelah and Tanach' only.")]),
  '26:36': names('26:36', 'Ephraim', "Shuthelah's sons: from Eran the Eranite clan.", "One sub-clan for Ephraim; the tribe that will dominate the north is thin here.", (["The Greek 'Eden' for Eran."], [loses("Hebrew 'Eran' is lost."), keeps("Greek 'Eden'.")])),
  '26:37': v("These were Ephraim's clans: 32,500. These were Joseph's sons by clans.", "All four columns agree on the number; the Greek adds the Joseph note here.",
   ["Ephraim.", "32,500.", "Joseph's sons."], "Ephraim numbered 32,500.", "Down 8,000; Ephraim, favoured in chapter 1, falls behind Manasseh, and the crossed hands of Jacob are reversed for a generation.", SAME + ORDER, ['joseph-son-of-jacob']),
  '26:38': v("Benjamin's sons by clans: from Bela the Belaite, from Ashbel the Ashbelite, from Ahiram the Ahiramite;", "The Greek 'Asyber … Iachiran'.",
   ["Benjamin's clans.", "Bela, Ashbel.", "Ahiram."], "Benjamin's clans were listed.", "Benjamin's ten sons in Genesis become five clans here; the names have shifted in the telling.", ORDER + [keeps("Greek 'Asyber' and 'Iachiran'.")]),
  '26:39': v("From Shephupham the Shuphamite clan, from Hupham the Huphamite clan.", "The Greek has one entry, 'Sophan', lacking Hupham.",
   ["Benjamin's clans.", "Shephupham.", "Hupham."], "Two more clans.", "Two clans in the Hebrew, one in the Greek; Hupham is the second name the Greek list lost.",
   ORDER + [loses("Hebrew 'from Hupham, the Huphamite clan' is lost."), keeps("Greek 'Sophan' alone.")]),
  '26:40': names('26:40', 'Benjamin', "Bela's sons were Ard and Naaman: the Ardite clan; from Naaman the Naamite clan.", "Grandsons given clans; Benjamin's small tribe is subdivided finely.", (["The Greek 'Adar' for Ard."], [keeps("Greek 'Adar'.")])),
  '26:41': total('26:41', 'Benjamin', 'forty-five thousand six hundred', "Up 10,200; Benjamin grew, and the Greek's shorter clan list reaches the same sum."),
  '26:42': v("Dan's sons by clans: from Shuham the Shuhamite clan; these were Dan's clans.", "The Greek 'Sami'.",
   ["Dan's clans.", "Shuham.", "One clan."], "Dan had one clan.", "One clan, Shuham (Genesis's Hushim), for the second-largest tribe; sixty-four thousand men of one family.",
   ORDER + [loses("Hebrew 'Shuham' is lost."), keeps("Greek 'Sami'.")]),
  '26:43': v("All the Shuhamite clans registered: 64,400.", "All four columns agree on the number; 'Sami' in Greek.",
   ["The Shuhamites.", "64,400.", "Dan's total."], "Dan numbered 64,400.", "Up 1,700; Dan stays second, the rear guard still nearly as strong as Judah.", SAME),
  '26:44': names('26:44', 'Asher', "Asher's sons by clans: from Imnah the Imnite, from Ishvi the Ishvite, from Beriah the Beriite.", "Asher after Dan in the Hebrew, after Gad in the Greek.", (["The Greek 'Jamin' for Imnah."], [loses("Hebrew 'Imnah' is lost."), keeps("Greek 'Jamin'.")])),
  '26:45': names('26:45', 'Asher', "Beriah's sons: from Heber the Heberite clan, from Malchiel the Malchielite clan.", "Beriah's two sons, sub-clans of Asher.", (["The Greek omits 'the sons of Beriah'."], [loses("Hebrew 'the sons of Beriah' is lost."), keeps("Greek lists Heber and Malchiel without the heading.")])),
  '26:46': v("The name of Asher's daughter was Serah.", "All four columns agree; Greek 'Sara'.",
   ["Asher's daughter.", "Serah.", "Named."], "Serah was named.", "Serah, Asher's daughter, named in Genesis 46 and here two centuries later; legend made her the woman who lived to see every generation of the story.", [keeps("Greek 'Sara'.")]),
  '26:47': total('26:47', 'Asher', 'fifty-three thousand four hundred', "Up 11,900; Asher's bread was rich after all."),
  '26:48': names('26:48', 'Naphtali', "Naphtali's sons by clans: from Jahzeel the Jahzeelite, from Guni the Gunite;", "Naphtali last; the Hebrew and Greek numbering realign here.", (["The Greek 'Asiel' for Jahzeel."], [loses("Hebrew 'Jahzeel' is lost."), keeps("Greek 'Asiel'.")])),
  '26:49': names('26:49', 'Naphtali', "From Jezer the Jezerite clan, from Shillem the Shillemite clan.", "Four clans; Genesis's four names kept."),
  '26:50': v("These were Naphtali's clans: 45,400.", "All four columns agree.",
   ["Naphtali.", "45,400.", "The same in every column."], "Naphtali numbered 45,400.", "Down 8,000; the last tribe counted, and the twelve are done.", SAME),
  '26:51': v("Those registered of Israel: 601,730.", "All four columns agree; the twelve totals sum to it despite the list differences.",
   ["601,730.", "Registered.", "All Israel."], "The total was 601,730.", "601,730 against 603,550: forty years, a whole generation dead, and the nation is 1,820 men smaller. The wilderness neither destroyed nor grew them; it replaced them.", SAME),
  '26:52': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the land."],
   "God spoke on dividing the land.", "The count was for this: who gets how much.", [AGREE], ['yhwh-yahweh', 'moses']),
  '26:53': v("The land is divided among these as inheritance by the number of names.", "All four columns agree.",
   ["The land divided.", "Among these.", "By number of names."], "Land followed population.", "The census becomes a deed: every name counted is a share in the land, and the second generation is counted for what the first forfeited.", [AGREE], ['canaan'], "The land shall be divided among these by the number of names."),
  '26:54': v("To the larger a larger inheritance, to the smaller a smaller; each by its registered number.", "All four columns agree.",
   ["Larger, more.", "Smaller, less.", "By the count."], "Shares were proportional.", "Judah's 76,500 get more land than Simeon's 22,200; the map will be drawn from the arithmetic.", [AGREE]),
  '26:55': v("But the land is divided by lot; they inherit by the names of their ancestral tribes.", "All four columns agree.",
   ["By lot.", "By ancestral tribes.", "Inherit."], "Lot decided location.", "Size by number, place by lot: the land is both earned and given, and the lot keeps God's hand in the geography.", [AGREE]),
  '26:56': v("Their inheritance is divided by the lot's decision between larger and smaller.", "The Hebrew passive; the Greek 'you shall divide'.",
   ["The lot decides.", "Larger and smaller.", "Divided."], "Lot and number worked together.", "The rule restated; Joshua 14–19 will carry it out.", [keeps("Greek 'you shall divide by the lot'.")]),
  '26:57': v("The registered Levites by clans: from Gershon the Gershonite, from Kohath the Kohathite, from Merari the Merarite.", "The Greek omits 'registered'.",
   ["The Levites.", "Gershon, Kohath.", "Merari."], "Levi was counted separately again.", "Levi after the twelve, as in chapter 3; the tribe with no land is counted after the land is assigned.", [keeps("Greek lacks the registration phrase.")]),
  '26:58': v("Levi's clans: the Libnite, Hebronite, Mahlite, Mushite and Korahite clans. Kohath begat Amram.", "The Greek lacks the Mahlite clan and puts Korah before Mushi.",
   ["Levi's clans.", "Libnite to Korahite.", "Kohath begat Amram."], "The Levite clans were named.", "The Korahite clan listed among Levi's, alive; 26:11 said his sons did not die, and here is their name on the roll.",
   [loses("Hebrew 'the Mahlite clan' is lost."), keeps("Greek lists four clans with Korah before Mushi.")]),
  '26:59': v("Amram's wife was Jochebed, a daughter of Levi born to Levi in Egypt; she bore Aaron, Moses and their sister Miriam.", "The Hebrew: Jochebed born to Levi; the Greek: she 'bore these to Levi in Egypt', a difficult antecedent.",
   ["Jochebed, daughter of Levi.", "Born in Egypt.", "Mother of Aaron, Moses, Miriam."], "Moses' mother was named.", "Jochebed named at last, the woman of the basket; and Miriam, dead at Kadesh, named with her brothers as 'their sister'.",
   [loses("Hebrew 'born to Levi in Egypt' is lost."), keeps("Greek 'who bore these to Levi in Egypt'.")], ['moses', 'high-priest', 'miriam', 'egypt']),
  '26:60': v("To Aaron were born Nadab, Abihu, Eleazar and Ithamar.", "All four columns agree; Greek 'Abiud'.",
   ["Aaron's sons.", "Nadab, Abihu.", "Eleazar, Ithamar."], "Aaron's sons were listed.", "The four names again, two of them dead for thirty-nine years.", [keeps("Greek 'Abiud'.")], ['high-priest']),
  '26:61': v("Nadab and Abihu died offering unauthorized fire before YHWH.", "The Greek adds 'in the wilderness of Sinai'.",
   ["Nadab and Abihu.", "Died.", "Unauthorized fire."], "The fire was recalled.", "Told a third time in the book; the priesthood's own warning sign, beside Korah's.", [keeps("Greek adds 'in the wilderness of Sinai'.")], ['yhwh-yahweh']),
  '26:62': v("Registered: 23,000, every male from one month old; not registered among Israel, because no inheritance was given them.", "All four columns agree.",
   ["23,000.", "From one month.", "No inheritance."], "The Levites numbered 23,000.", "Up a thousand from 22,000; the landless tribe grew a little, and is counted apart because it owns nothing to be counted for.", [AGREE]),
  '26:63': v("These were registered by Moses and Eleazar the priest in the plains of Moab by the Jordan opposite Jericho.", "All four columns agree; 'Araboth' in Greek.",
   ["By Moses and Eleazar.", "In the plains of Moab.", "By the Jordan."], "The census was closed.", "The roll closed where it opened, at the river.", [keeps("Greek 'Araboth'.")], ['moses', 'high-priest', 'jordan']),
  '26:64': v("Among these was no man registered by Moses and Aaron the priest in the wilderness of Sinai.", "The Greek lacks Aaron's title.",
   ["Not one man.", "From the first census.", "In Sinai."], "The first generation was gone.", "Not one: the sentence of 14:29 executed to the man, and the census is its proof. Six hundred thousand names from chapter 1 and none of them here.",
   [loses("Hebrew 'Aaron the priest' is lost."), keeps("Greek 'Aaron'.")], ['moses', 'high-priest', 'sinai']),
  '26:65': v("For YHWH had said of them: they shall die in the wilderness. Not one remained except Caleb son of Jephunneh and Joshua son of Nun.", "All four columns agree; Greek Iesous is Joshua.",
   ["YHWH had said.", "They shall die.", "Except Caleb and Joshua."], "Only Caleb and Joshua survived.", "Two names from the old list, the two who said 'we can'; the chapter ends with them standing among 601,730 strangers' sons.", [AGREE], ['yhwh-yahweh', 'joshua']),
 },
}
