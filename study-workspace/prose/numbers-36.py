K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
WEST = [loses("Hebrew 'plains of Moab' is lost."), keeps("Greek 'on the western side of Moab'."), between("The Latin and King James have 'plains of Moab'.")]
CLAN = [between("The Greek has 'their father's clan'; the Hebrew 'the clan of their father's tribe'; the Latin 'their own tribe'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 36,
 'chapterNote': "Zelophehad's daughters, second hearing. The heads of Gilead's clan point out that if the daughters, who inherit by the ruling of chapter 27, marry outside Manasseh, their land passes to another tribe and the Jubilee will not bring it back. Moses, at YHWH's word, rules that they are right: the daughters may marry whom they please, but within their father's tribe, and no inheritance is to pass from tribe to tribe; every heiress in Israel is to marry within her father's clan. The five marry their cousins and the land stays in Manasseh. The book closes: these are the commandments and judgments given on the plains of Moab by the Jordan opposite Jericho. The Greek adds Eleazar the priest to the hearing (36:1), 'release' for 'Jubilee' (36:4), 'thus speaks' without the verdict 'rightly' (36:5), 'father's clan' for 'clan of their father's tribe' (36:6–8), 'the Israelites' for 'the tribes' (36:9), reorders the daughters with Mahlah last and has 'cousins' (36:11), adds 'ordinances' and omits 'the Israelites' at 36:13, and 'western side' for 'plains' of Moab. The Latin at 36:7 extends the rule to all men and women.",
 'verses': {
  '36:1': v("The ancestral heads of the clan of Gilead son of Machir son of Manasseh, of the clans of Joseph's sons, came and spoke before Moses and the leaders, the ancestral heads of Israel.", "The Greek adds Eleazar the priest and uses tribal terms for the Hebrew clans.",
   ["The heads of Gilead's clan.", "Of Manasseh.", "Spoke before Moses and the leaders."], "Gilead's clan raised a case.", "The book's last case comes from the same family as one of its earlier ones: Zelophehad's daughters won their inheritance in chapter 27, and now their clansmen ask what happens to it when they marry.",
   [keeps("Greek adds 'and before Eleazar the priest'."), between("The Latin has 'the leaders of Israel'; the Greek 'the rulers of the ancestral houses'.")], ['moses', 'joseph-son-of-jacob']),
  '36:2': v("YHWH commanded my lord to give the land to Israel as inheritance by lot, and my lord was commanded by YHWH to give our brother Zelophehad's inheritance to his daughters.", "The Greek 'our lord' at first; the honorific is Moses.",
   ["YHWH commanded my lord.", "The land by lot.", "Zelophehad's inheritance to his daughters."], "They recall two commands.", "They state both rulings fairly and claim neither was wrong: the land by lot, the daughters' right. The problem is where the two meet, and they bring it as a question, not a protest.", [between("The Greek has 'our lord' then 'my lord'; the Hebrew 'my lord' twice.")], ['yhwh-yahweh']),
  '36:3': v("But if they marry men of another Israelite tribe, their inheritance will be taken from our ancestral inheritance and added to the tribe they marry into; it will be taken from our allotted inheritance.", "All four columns agree.",
   ["If they marry out.", "Their land goes with them.", "Taken from our lot."], "Marriage could move land between tribes.", "Land follows the husband: an heiress who marries out takes her father's fields into another tribe forever. The men of Gilead are defending the map of chapter 34 against the ruling of chapter 27.", [AGREE], []),
  '36:4': v("When the Jubilee comes for Israel, their inheritance will be added to the tribe they marry into, and taken from the inheritance of our ancestral tribe.", "The Hebrew names the Jubilee; the Greek 'if the release comes'; the Latin 'the fiftieth year of release'.",
   ["When the Jubilee comes.", "Added to the other tribe.", "Taken from ours."], "The Jubilee would not undo it.", "The Jubilee returns sold land to its clan; but an heiress's land is not sold, it is inherited, so the Jubilee would fix the transfer rather than reverse it. The clan has read Leviticus 25 carefully.",
   [loses("Hebrew 'Jubilee' (yobel) is lost."), keeps("Greek 'the release' (aphesis)."), between("The Latin has 'the jubilee, the fiftieth year of release'; the King James 'the jubile'.")], []),
  '36:5': v("Moses commanded Israel at YHWH's word: the tribe of Joseph's sons speaks rightly.", "The Hebrew ken 'rightly'; the Greek houtos 'thus', without the verdict.",
   ["Moses commanded.", "At YHWH's word.", "Joseph's tribe speaks rightly."], "Moses upheld the clan.", "'Speaks rightly': the same words God used of the daughters in 27:7. Both sides of the case are right, and the law must make room for both.",
   [loses("Hebrew 'speaks rightly' is lost."), keeps("Greek 'thus speaks the tribe of the sons of Joseph'."), between("The Latin and King James have 'has spoken rightly / well'.")], ['moses', 'yhwh-yahweh']),
  '36:6': v("This is what YHWH commands about Zelophehad's daughters: let them marry whom they think best, but within the clan of their father's tribe.", "The Hebrew 'the clan of their father's tribe'; the Greek 'their father's clan'; the Latin 'their own tribe'.",
   ["Marry whom they think best.", "But within the clan.", "Of their father's tribe."], "Free choice within the tribe.", "'Whom they think best': the daughters' consent is written into the ruling, a rare thing in ancient law. The limit is on tribe, not on will; inside Manasseh they choose.", CLAN, ['yhwh-yahweh'], "Let the daughters marry whom they think best, within their father's tribe."),
  '36:7': v("No inheritance of the Israelites shall pass from tribe to tribe, for every Israelite shall hold fast to the inheritance of his ancestral tribe.", "The Latin extends the rule to all men and women; the Greek to inheriting daughters.",
   ["No inheritance passes between tribes.", "Each holds fast.", "To his ancestral tribe."], "Tribal land is fixed.", "'Hold fast' (dabaq), the verb of Genesis 2:24 for a man and his wife: every Israelite is to cleave to his tribe's land as to a spouse. The tribes are permanent because the land is.",
   [between("The Latin applies the rule to 'all men and women'; the Greek to 'daughters who inherit'; the Hebrew and King James to 'the children of Israel'.")], [], "Let no inheritance pass from tribe to tribe."),
  '36:8': v("Every daughter who inherits among the Israelite tribes shall marry someone from the clan of her father's tribe, so that each Israelite may possess his ancestral inheritance.", "The Greek anchisteuo emphasises kin-succession; the Hebrew the ordinary inheriting verb and includes the tribe.",
   ["Every inheriting daughter.", "Marries within her father's clan.", "To keep the inheritance."], "The ruling becomes general law.", "From five women to every heiress in Israel: the case law becomes statute. A daughter who inherits carries her tribe's land and marries within it.", CLAN + [keeps("Greek 'shall be next of kin (anchisteuo) to one of her father's clan'.")], [], "Every inheriting daughter shall marry within her father's clan."),
  '36:9': v("No inheritance shall pass from one tribe to another, for the Israelite tribes shall each hold fast to their own inheritance.", "The Hebrew makes the tribes the subject; the Greek 'the Israelites'.",
   ["No inheritance passes.", "Tribe to tribe.", "Each holds fast."], "The principle is repeated.", "Said twice in three verses: the land map is to outlast every marriage. Israel's tribes are not to melt into one another through their daughters.",
   [between("The Greek has 'the Israelites'; the Hebrew and King James 'the tribes of the children of Israel'.")], []),
  '36:10': v("Zelophehad's daughters did as YHWH had commanded Moses.", "All four columns agree.",
   ["Zelophehad's daughters.", "Did as commanded.", "YHWH through Moses."], "The daughters obeyed.", "The women who asked for justice accept its limit: they won the land and keep it by marrying as the law now asks. Obedience from the people who began the case.", [AGREE], ['yhwh-yahweh', 'moses']),
  '36:11': v("Mahlah, Tirzah, Hoglah, Milcah and Noah, Zelophehad's daughters, married their uncles' sons.", "The Greek puts Mahlah last and has 'cousins'.",
   ["Mahlah, Tirzah, Hoglah.", "Milcah and Noah.", "Married their cousins."], "The five married cousins.", "The five names a third time (26:33, 27:1): the book will not let them be anonymous. They marry their father's brothers' sons, and the land stays in the house.",
   [loses("Hebrew order 'Mahlah, Tirzah, Hoglah, Milcah, Noah' and 'their uncles' sons' are lost."), keeps("Greek 'Tirzah, Hoglah, Milcah, Noah, Mahlah … their cousins'."), between("The Latin and King James keep the Hebrew order.")], []),
  '36:12': v("They married within the clans of Manasseh son of Joseph, and their inheritance stayed in the tribe of their father's clan.", "All four columns agree.",
   ["Within Manasseh.", "Their inheritance stayed.", "In their father's tribe."], "The land stayed in Manasseh.", "The resolution: the daughters keep their land and Manasseh keeps its daughters. Joshua 17:3–6 records the fields actually given.", [AGREE], ['joseph-son-of-jacob']),
  '36:13': v("These are the commandments and judgments that YHWH commanded the Israelites through Moses on the plains of Moab by the Jordan opposite Jericho.", "The Greek adds 'ordinances', omits 'the Israelites', and has 'western side of Moab'.",
   ["The commandments and judgments.", "Through Moses.", "On the plains of Moab."], "The book closes at the Jordan.", "Numbers ends where it has stood since chapter 22: at the river, looking across. Forty years, two censuses, a generation dead and another counted; the commandments given, the land not yet entered. Deuteronomy will be Moses' farewell from this same ground.",
   [keeps("Greek adds 'and the ordinances' and lacks 'to the Israelites'.")] + WEST, ['yhwh-yahweh', 'moses', 'jordan', 'jericho']),
 },
}
