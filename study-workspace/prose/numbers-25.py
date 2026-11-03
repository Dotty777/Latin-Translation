K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
INIT = [loses("Hebrew 'joined itself to' (tsamad) is lost."), keeps("Greek 'was initiated into the worship of' (telesthe); no later mystery-rite detail is implied."), between("The Latin and King James have 'initiated' or 'joined'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 25,
 'chapterNote': "Baal of Peor. At Shittim the people go after Moab's daughters, eat their sacrifices and bow to their gods; Israel joins itself to Baal of Peor and YHWH's anger burns; the leaders are to be exposed in the sun and the judges to kill their men who joined. Zimri, a Simeonite chief, brings Cozbi, a Midianite princess, before the weeping congregation; Phinehas son of Eleazar follows them into the chamber and pierces both, and the plague stops at 24,000. YHWH gives Phinehas a covenant of peace and perpetual priesthood for his zeal, and orders Israel to treat Midian as enemies for the deceit of Peor. The Greek has 'profaned themselves' (25:1), 'idols' for 'gods' (25:2), 'initiated into the worship of' for 'joined itself to' (25:3, 5), 'make a public example' for 'expose' (25:4), 'tribes … his own kinsman' for 'judges … his men' (25:5), reverses the roles at 25:6 ('brought his brother to the Midianite woman'), 'lance' (25:7), 'furnace' for 'chamber' and 'womb' for 'belly' (25:8), lacks 'My' before covenant (25:12), 'the nation of Ommoth' for 'clans' (25:15), and adds 'Speak to the sons of Israel' at 25:16. The Latin has the leaders hanged on gibbets (25:4) and a brothel (25:8).",
 'verses': {
  '25:1': v("Israel stayed at Shittim, and the people began sexual immorality with Moab's daughters.", "The Hebrew 'began'; the Greek 'profaned themselves by engaging in'.",
   ["At Shittim.", "The people began.", "Immorality with Moab's daughters."], "Israel fell to Moab's women.", "What Balak's curses could not do, Moab's daughters do in a verse; the camp Balaam called good tents is in Moab's beds. Shittim is the last camp before the Jordan.",
   [loses("Hebrew 'began' is lost."), keeps("Greek 'profaned themselves'.")]),
  '25:2': v("They invited the people to their gods' sacrifices; the people ate and bowed to their gods.", "The Hebrew 'gods'; the Greek 'idols' and names the food as sacrificial.",
   ["Invited to sacrifices.", "The people ate.", "Bowed to their gods."], "Sex led to sacrifice.", "From the bed to the altar: the women's invitation is to a meal, and the meal is worship. The sin of 25:1 becomes the sin of 25:3 at a table.",
   [loses("Hebrew 'their gods' is lost."), keeps("Greek 'their idols … ate from their sacrifices'.")], ['gods']),
  '25:3': v("Israel joined itself to Baal of Peor, and YHWH's anger burned against Israel.", "The Hebrew 'joined itself'; the Greek 'was initiated into the worship of'.",
   ["Joined to Baal of Peor.", "YHWH's anger.", "Against Israel."], "Israel worshipped Baal.", "Baal-Peor, the god of the mountain from which Balaam blessed them; 'yoked' to him, the Hebrew says, the word for an ox's harness.",
   INIT, ['baal', 'yhwh-yahweh']),
  '25:4': v("YHWH said to Moses: take all the people's leaders and expose them to YHWH in the sun, so his anger turns from Israel.", "The Hebrew hoqa 'expose' in an execution sense; the Greek 'make a public example'; the Latin 'hang on gibbets'. The referent of 'them' is interpretive.",
   ["Take the leaders.", "Expose them in the sun.", "Turn the anger."], "The leaders were sentenced.", "'Expose them in the sun': impale or hang, the verb is grim and uncertain; the chiefs who let it happen answer for it in daylight.",
   [loses("Hebrew 'expose them (hoqa) to YHWH' is lost."), keeps("Greek 'make a public example of them before the Lord'."), between("The Latin has 'hang them on gibbets'; the King James 'hang them up'.")], ['yhwh-yahweh', 'moses'], "Take all the leaders of the people and expose them."),
  '25:5': v("Moses said to Israel's judges: each of you kill his men who joined Baal of Peor.", "The Hebrew 'judges … his men'; the Greek 'tribes … his own kinsman'.",
   ["To the judges.", "Each kill his men.", "Who joined Baal."], "The judges executed the guilty.", "Each judge kills his own: the purge is done by the men who know the sinners by name, as at the calf.",
   INIT + [loses("Hebrew 'judges … his men' is lost."), keeps("Greek 'Israel's tribes … his own kinsman'.")], ['moses', 'baal'], "Each of you shall kill his men who joined Baal of Peor."),
  '25:6': v("An Israelite man brought a Midianite woman to his brothers before Moses and the whole congregation, who were weeping at the Tent of Meeting's entrance.", "The Hebrew 'brought a Midianite woman to his brothers'; the Greek 'brought his brother to the Midianite woman'. The Latin 'a Midianite prostitute'.",
   ["An Israelite man.", "A Midianite woman.", "Before the weeping congregation."], "A chief flaunted his sin.", "While the people weep at the door, a man parades a Midianite woman past them; the sin is public and the grief is public and they meet at the tent.",
   TENT + [loses("Hebrew 'brought a Midianite woman to his brothers' is lost."), keeps("Greek 'brought his brother to the Midianite woman'.")], ['tabernacle', 'moses']),
  '25:7': v("Phinehas son of Eleazar, son of Aaron the priest, saw, rose from the congregation and took a spear.", "All four columns agree; 'lance' in Greek; 'dagger' in Latin.",
   ["Phinehas saw.", "Rose from the congregation.", "Took a spear."], "Phinehas acted.", "Phinehas, the third generation of priests, takes a spear instead of a censer; his grandfather stood between the dead and the living with incense, and he does it with iron.",
   [keeps("Greek 'a lance'."), between("The Latin has 'dagger'; the King James 'javelin'.")], ['high-priest']),
  '25:8': v("He followed the Israelite into the chamber and pierced both, the man and the woman through her belly; the plague on Israel stopped.", "The Hebrew qubbah 'chamber' and 'belly'; the Greek 'furnace' and 'womb'; the Latin 'brothel … genitals'.",
   ["Into the chamber.", "Pierced both.", "The plague stopped."], "One spear ended the plague.", "Two bodies on one spear and the plague stops; the rabbis counted the miracles in the thrust. The holiest act in the chapter is a killing, and the text does not flinch.",
   [loses("Hebrew 'the chamber (qubbah) … her belly' is lost."), keeps("Greek 'the furnace (kaminos) … her womb'."), between("The Latin has 'brothel … genitals'; the King James 'tent … belly'.")], ['high-priest']),
  '25:9': v("Those who died in the plague were 24,000.", "All four columns agree; Paul's 23,000 is a reception variant.",
   ["24,000.", "Died.", "In the plague."], "The plague killed 24,000.", "Twenty-four thousand, more than Korah's plague; Paul will say twenty-three thousand 'in one day', and the difference has been argued since.", [AGREE]),
  '25:10': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On Phinehas."],
   "God spoke about Phinehas.", "God's verdict on the spear.", FORMULA, ['yhwh-yahweh', 'moses']),
  '25:11': v("Phinehas son of Eleazar, son of Aaron, turned my wrath from Israel by being zealous with my zeal among them, so I did not consume Israel in my jealousy.", "All four columns agree.",
   ["Phinehas turned my wrath.", "Zealous with my zeal.", "Israel not consumed."], "Phinehas's zeal was God's own.", "'Zealous with My zeal': the man's anger and God's are one, which is why it saved rather than damned. The verse is the charter of every zealot since, and the measure by which most fail.",
   [AGREE], ['high-priest', 'jealous']),
  '25:12': v("Therefore say: I give him my covenant of peace.", "The Hebrew 'My covenant'; the Greek 'a covenant'.",
   ["Therefore say.", "I give him.", "My covenant of peace."], "Phinehas received a covenant of peace.", "A covenant of peace for a killing: the peace is Israel's, bought by the spear, and the man who bought it is given it.",
   [loses("Hebrew 'My covenant' is lost."), keeps("Greek 'a covenant of peace'.")], ['term-covenant', 'yhwh-shalom']),
  '25:13': v("For him and his offspring a covenant of perpetual priesthood, because he was zealous for his God and atoned for Israel.", "All four columns agree.",
   ["Perpetual priesthood.", "For him and his seed.", "He atoned for Israel."], "The high priesthood was fixed in Phinehas's line.", "'Made atonement': a spear-thrust counted as atonement, the priest's office done with the wrong tool and the right heart. Zadok's line will descend from this verse.",
   [AGREE], ['high-priest', 'term-covenant']),
  '25:14': v("The slain Israelite was Zimri son of Salu, leader of a Simeonite ancestral house.", "All four columns agree.",
   ["Zimri son of Salu.", "A leader.", "Of Simeon."], "The sinner was a Simeonite chief.", "A chief of Simeon; the tribe will lose 37,000 men between the censuses, and the rabbis blamed Peor.", [AGREE]),
  '25:15': v("The slain Midianite woman was Cozbi daughter of Zur, head of clans, an ancestral house in Midian.", "The Hebrew 'ummot 'clans'; the Greek 'the nation of Ommoth'.",
   ["Cozbi daughter of Zur.", "Head of clans.", "Of Midian."], "The woman was a Midianite princess.", "Cozbi, a princess, daughter of a king Israel will kill in chapter 31; her name means 'deceitful', and 25:18 will use the root.",
   [loses("Hebrew 'head of clans' is lost."), keeps("Greek 'ruler of the nation of Ommoth'.")]),
  '25:16': v("YHWH speaks to Moses.", "The Greek adds 'Speak to the sons of Israel, saying'.",
   ["YHWH speaks.", "To Moses.", "On Midian."], "God turned to Midian.", "Moab's daughters began it but Midian is named for punishment; Midian's elders counselled Balak, and Midian's princess came to the tent.", FORMULA + [keeps("Greek adds 'Speak to the sons of Israel, saying'.")], ['yhwh-yahweh', 'moses']),
  '25:17': v("Treat the Midianites as enemies and strike them,", "All four columns agree.",
   ["The Midianites.", "As enemies.", "Strike them."], "War on Midian was ordered.", "Midian, Moses' wife's people and Hobab's; the command to strike them is the chapter's hardest line for Moses himself.", [AGREE], [], "Treat the Midianites as enemies and strike them."),
  '25:18': v("For they treated you as enemies by the schemes with which they deceived you over Peor and over Cozbi, their sister, struck down on the plague day because of Peor.", "All four columns agree; the Greek present 'deceive'.",
   ["Their schemes.", "Over Peor and Cozbi.", "Their sister."], "Midian's deceit was the charge.", "'Their sister': Cozbi was sent, not strayed; the seduction was policy, and 31:16 will name Balaam as its author. The war of chapter 31 is declared here.",
   [keeps("Greek present tense 'the deceit by which they deceive you'.")], ['baal']),
 },
}
