K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
MERIBAH = [loses("Hebrew 'Meribah' is lost as a name."), keeps("Greek 'Water of Dispute' or 'Reviling'."), between("The Latin has 'water of contradiction'; the King James 'Meribah'.")]
REVILE = [loses("Hebrew 'quarreled' is lost."), keeps("Greek 'reviled'."), between("The Latin has 'rebellion' or 'contradiction'; the King James 'chode'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 20,
 'chapterNote': "The fortieth year begins with three deaths. At Kadesh in Zin Miriam dies. There is no water; the people quarrel, wishing they had died with Korah's brothers; YHWH tells Moses to speak to the rock, and Moses, calling them rebels, strikes it twice; water pours out, and YHWH bars Moses and Aaron from the land for not trusting him to show his holiness: the waters of Meribah. Moses asks Edom for passage on the King's Highway as 'your brother Israel'; Edom refuses with an army and Israel turns away. At Mount Hor Aaron is stripped of his garments, which are put on Eleazar, and dies on the summit; Israel mourns thirty days. The Greek has 'reviled' for 'quarreled' (20:3, 13), 'to kill us' for 'for us to die' (20:4), plural commands to Moses and Aaron (20:8), 'disobedient … surely we are not to' (20:10), lacks 'in Me' (20:12), translates Meribah (20:13, 24), 'sojourners' (20:15), a statement for the request and 'cistern' for 'well' (20:17), 'alongside the mountain' for 'by the highway … on foot' (20:19), 'you (plural) provoked Me' for 'he … you rebelled against My command' (20:24), adds 'before the whole congregation' (20:25), 'he brought him up' for 'they went up' (20:27), and 'released' for 'died' (20:29). The Latin adds a spoken prayer at 20:6.",
 'verses': {
  '20:1': v("Israel, the whole congregation, came to the wilderness of Zin in the first month and stayed at Kadesh; Miriam died there and was buried.", "All four columns agree; Greek 'Sin' is Hebrew Zin.",
   ["Zin, the first month.", "At Kadesh.", "Miriam died."], "Miriam died at Kadesh.", "'The first month', and the text does not say of which year: thirty-eight years vanish between chapters 19 and 20, and the first thing on the far side is a grave. Miriam, who sang at the sea, dies without a word.",
   [AGREE], ['miriam']),
  '20:2': v("There was no water for the congregation, and they assembled against Moses and Aaron.", "All four columns agree.",
   ["No water.", "The congregation assembled.", "Against Moses and Aaron."], "Thirst renewed the quarrel.", "The second generation, and the same complaint as the first at Rephidim; the wilderness has not changed, and neither have they.", [AGREE], ['moses', 'high-priest']),
  '20:3': v("The people quarreled with Moses: if only we had perished when our brothers perished before YHWH!", "The Hebrew 'quarreled … perished'; the Greek 'reviled … destroyed'.",
   ["They quarreled.", "If only we had perished.", "With our brothers."], "They wished for Korah's death.", "'When our brothers perished': Korah's dead are their brothers now; the generation that watched the earth open wishes it had gone in too.",
   REVILE + [keeps("Greek 'when our brothers were destroyed'.")], ['moses', 'yhwh-yahweh']),
  '20:4': v("Why have you brought YHWH's assembly into this wilderness for us and our livestock to die?", "The Hebrew 'to die here'; the Greek 'to kill us'.",
   ["Why bring us here?", "YHWH's assembly.", "To die with our cattle."], "They accused Moses of murder.", "'YHWH's assembly', said to the man they accuse of killing it; the title is a claim against him.",
   [loses("Hebrew 'for us and our livestock to die here' is lost."), keeps("Greek 'to kill us and our livestock'.")]),
  '20:5': v("Why bring us from Egypt to this wretched place, no place for seed, figs, vines or pomegranates, and no water?", "All four columns agree.",
   ["From Egypt to here.", "No seed, figs, vines.", "No water."], "The wilderness was named for what it lacked.", "Figs, vines, pomegranates: the fruit the scouts carried from Eshcol, named now as what Kadesh does not have; they describe the land they refused while complaining of the land they chose.", [AGREE], ['egypt']),
  '20:6': v("Moses and Aaron went from the assembly to the Tent of Meeting's entrance and fell on their faces; YHWH's glory appeared.", "The Hebrew, Greek and King James agree; the Latin adds a spoken prayer for water.",
   ["To the tent's entrance.", "On their faces.", "The glory appeared."], "The leaders prostrated themselves again.", "Face down at the door once more; forty years on, the posture is the same and so is the answer: the glory.",
   TENT + [between("The Latin adds a spoken plea for water; the Greek and King James have the prostration and glory only.")], ['tabernacle', 'moses', 'high-priest']),
  '20:7': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the rock."],
   "God gave the instruction.", "The word before the fault; what Moses was told matters for what he did.", FORMULA, ['yhwh-yahweh', 'moses']),
  '20:8': v("Take the staff, assemble the congregation with Aaron, speak to the rock before their eyes and it will give water; bring water from the rock for them and their livestock.", "The Hebrew's final commands are singular; the Greek plural.",
   ["Take the staff.", "Speak to the rock.", "Water for all."], "Moses was told to speak.", "'Speak to the rock': at Rephidim he was told to strike; here to speak. The staff is in his hand and the command is in his ear, and they disagree.",
   [keeps("Greek 'you (plural) shall bring water out … shall give … to drink'.")], ['rock', 'high-priest'], "Speak to the rock before their eyes."),
  '20:9': v("Moses took the staff from before YHWH as he commanded.", "All four columns agree; the Greek repeats the name.",
   ["Moses took the staff.", "From before YHWH.", "As commanded."], "Moses took Aaron's budded staff.", "'The staff from before YHWH': Aaron's almond staff from the ark's room, the sign of mercy, taken out to strike a rock.", [AGREE], ['moses', 'yhwh-yahweh']),
  '20:10': v("Moses and Aaron assembled the congregation before the rock; he said: listen now, you rebels! shall we bring water from this rock for you?", "The Greek 'listen to me … disobedient … surely we are not to'.",
   ["Before the rock.", "Listen, you rebels!", "Shall we bring water?"], "Moses spoke in anger.", "'You rebels', and 'shall we bring water': the man who called himself nothing takes the water as his own to give or refuse. Psalm 106 says he spoke rashly with his lips.",
   [keeps("Greek 'Listen to me, you disobedient people! Surely we are not to bring water'."), between("The Latin has 'rebels and unbelievers'.")], ['moses', 'rock']),
  '20:11': v("Moses raised his hand and struck the rock twice with his staff; abundant water came out, and the congregation and livestock drank.", "All four columns agree. Paul calls the rock Christ.",
   ["He struck twice.", "Abundant water.", "All drank."], "Water came despite the fault.", "Struck, not spoken to, and twice; the water comes anyway, because the people's thirst is not the point of the judgment. Paul will say the rock was Christ, struck once too often.", [AGREE], ['rock', 'moses']),
  '20:12': v("YHWH said to Moses and Aaron: because you did not trust me to show me holy before Israel, you will not bring this assembly into the land I have given them.", "The Greek lacks 'in Me'.",
   ["You did not trust me.", "To show me holy.", "You will not bring them in."], "Moses and Aaron were barred.", "The sentence on Moses: not for anger, the text says, but for failing to trust God to be holy without being struck. Forty years of leading, and the land denied for one blow.",
   [loses("Hebrew 'did not trust in Me' is lost."), keeps("Greek 'did not believe so as to show Me holy'.")], ['moses', 'high-priest', 'yhwh-yahweh', 'canaan']),
  '20:13': v("These are the waters of Meribah, where Israel quarreled with YHWH and he showed himself holy among them.", "The Greek 'Water of Dispute … reviled'.",
   ["The waters of Meribah.", "Israel quarreled.", "He showed himself holy."], "The place was named for the quarrel.", "Meribah, 'quarrel', the same name as Rephidim's; God is shown holy at the water after all, in the judgment on the men who struck for it.",
   MERIBAH + REVILE, ['yhwh-yahweh']),
  '20:14': v("Moses sent messengers from Kadesh to the king of Edom: thus says your brother Israel: you know all the hardship that has found us.", "All four columns agree; the Greek angeloi are human messengers.",
   ["Messengers to Edom.", "Your brother Israel.", "You know our hardship."], "Moses appealed to Edom as kin.", "'Your brother Israel': Jacob speaking to Esau after four centuries, asking a road. The old quarrel is invoked as kinship.",
   [keeps("Greek 'angels' (messengers).")], ['moses', 'jacob']),
  '20:15': v("Our fathers went to Egypt and we lived there many days; the Egyptians mistreated us and our fathers.", "All four columns agree; the Greek 'as sojourners'.",
   ["Our fathers in Egypt.", "Many days.", "Mistreated."], "The appeal recited the exodus.", "Israel's story told to a foreign king in two sentences; the diplomacy begins with a confession of weakness.",
   [keeps("Greek 'we lived as sojourners in Egypt'.")], ['egypt']),
  '20:16': v("We cried to YHWH, he heard, sent a messenger, and brought us out of Egypt; now we are at Kadesh at the edge of your territory.", "The Hebrew mal'akh and Greek angelos both mean messenger or angel.",
   ["We cried to YHWH.", "He sent a messenger.", "Now at Kadesh."], "Israel's rescue was credited to God's messenger.", "'He sent an angel': Moses does not name himself as the deliverer; to Edom he is a messenger's people.",
   [between("The Hebrew and Greek words mean messenger or angel; the Latin and King James have 'angel'.")], ['angel-of-the-lord', 'yhwh-yahweh']),
  '20:17': v("Please let us pass through your land; we will not cross fields or vineyards or drink well water; we will keep the King's Highway and turn neither right nor left.", "The Hebrew requests and names well water; the Greek states and names the king's cistern.",
   ["Let us pass.", "No fields, vineyards or wells.", "The King's Highway only."], "Israel asked for harmless passage.", "The King's Highway, the old trade road east of the Dead Sea; Israel promises to touch nothing, and is refused anyway.",
   [loses("Hebrew 'please let us pass … well water' is lost."), keeps("Greek 'we will pass through your land … your cistern … the royal road'.")]),
  '20:18': v("Edom said: you shall not pass through me, or I will come out against you with the sword.", "All four columns agree; 'in war' in Greek.",
   ["You shall not pass.", "Through me.", "Or the sword."], "Edom refused.", "Esau's answer to Jacob: no, and a sword. The brotherhood Moses claimed is denied.",
   [keeps("Greek 'to meet you in war'.")]),
  '20:19': v("Israel said: we will go up by the highway; if we and our livestock drink your water we will pay; only a small matter, let me pass on foot.", "The Hebrew 'highway … on foot'; the Greek 'alongside the mountain' twice.",
   ["By the highway.", "We will pay for water.", "Only on foot."], "Israel offered to pay.", "'Let me pass on foot': the request shrinks to its least; a nation asks to walk through like a traveller.",
   [loses("Hebrew 'by the highway … let me pass through on foot' is lost."), keeps("Greek 'we will pass alongside the mountain … the matter is nothing; we will pass alongside the mountain'.")]),
  '20:20': v("He said: you shall not pass. Edom came out against him with a large force and a strong hand.", "All four columns agree.",
   ["You shall not pass.", "Edom came out.", "A strong hand."], "Edom showed its army.", "'A strong hand', the phrase for God's arm in Egypt, now Edom's against Israel; the brother stands in the road with the gesture of Pharaoh.", [AGREE]),
  '20:21': v("Edom refused Israel passage through his territory, and Israel turned away from him.", "All four columns agree.",
   ["Edom refused.", "Passage.", "Israel turned away."], "Israel did not fight Edom.", "Israel turns away: no war with the brother, as Deuteronomy 2 explains; the long way round begins.", [AGREE]),
  '20:22': v("They set out from Kadesh and the whole congregation came to Mount Hor.", "All four columns agree; the Latin places the Edom border here.",
   ["From Kadesh.", "The whole congregation.", "To Mount Hor."], "Israel reached Mount Hor.", "From Kadesh at last, after most of forty years; the first stop is a mountain and a funeral.", [between("The Latin adds 'at the borders of Edom' here.")]),
  '20:23': v("YHWH said to Moses and Aaron at Mount Hor on the border of Edom:", "All four columns agree; the Latin addresses Moses alone.",
   ["At Mount Hor.", "On Edom's border.", "To Moses and Aaron."], "God spoke at Edom's edge.", "Spoken to both brothers, about one of them.", [between("The Latin addresses Moses alone.")], ['yhwh-yahweh', 'moses', 'high-priest']),
  '20:24': v("Aaron shall be gathered to his people; he shall not enter the land I gave Israel, because you rebelled against my command at the waters of Meribah.", "The Hebrew 'he … you (plural) rebelled against My command'; the Greek 'you (plural) shall not enter … provoked Me at the Water of Reviling'.",
   ["Aaron gathered to his people.", "Not entering the land.", "Because of Meribah."], "Aaron's death was tied to the rock.", "'Gathered to his people', the gentle phrase for a death that is also a sentence; Aaron dies for Moses' blow as much as his own silence.",
   MERIBAH + [loses("Hebrew 'he shall not enter … you rebelled against My command' is lost."), keeps("Greek 'you (plural) shall certainly not enter … you provoked Me'.")], ['high-priest']),
  '20:25': v("Take Aaron and his son Eleazar and bring them up Mount Hor.", "The Greek adds 'before the whole congregation'.",
   ["Take Aaron.", "And Eleazar.", "Up Mount Hor."], "Father and son climbed together.", "Up the mountain with the heir: the succession is to happen in the open, on a summit.",
   [keeps("Greek adds 'before the whole congregation'.")], ['high-priest'], "Take Aaron and Eleazar and bring them up Mount Hor."),
  '20:26': v("Strip Aaron of his garments and put them on Eleazar; Aaron will be gathered to his people and die there.", "All four columns agree.",
   ["Strip Aaron.", "Clothe Eleazar.", "Aaron dies there."], "The priesthood passed by garments.", "The office is the clothes: ephod, breastpiece, turban lifted off the old man and set on the young one while both stand there; Aaron watches himself cease to be high priest before he dies.", [AGREE], ['high-priest', 'ephod', 'breastpiece']),
  '20:27': v("Moses did as YHWH commanded, and they went up Mount Hor before the eyes of the whole congregation.", "The Hebrew 'they went up'; the Greek 'he brought him up'.",
   ["Moses obeyed.", "They went up.", "Before all."], "The three climbed in sight of all.", "Three men climbing while the camp watches; everyone knows two will come down.",
   [loses("Hebrew 'they went up' is lost."), keeps("Greek 'he brought him up'.")], ['moses']),
  '20:28': v("Moses stripped Aaron of his garments and put them on Eleazar; Aaron died there on the summit, and Moses and Eleazar came down.", "The Greek leaves Moses implicit and lacks 'there'.",
   ["Garments to Eleazar.", "Aaron died on the summit.", "Two came down."], "Aaron died on Mount Hor.", "Moses undresses his brother. Aaron dies on a mountaintop as Moses will, and the sons who were left to him bury nothing; the text gives no grave.",
   [keeps("Greek 'he stripped Aaron' without naming Moses, and lacks 'there'.")], ['high-priest', 'moses']),
  '20:29': v("The whole congregation saw that Aaron had died, and all the house of Israel wept for Aaron thirty days.", "The Hebrew 'had died'; the Greek 'had been released'.",
   ["They saw Aaron had died.", "All Israel wept.", "Thirty days."], "Israel mourned Aaron a month.", "Thirty days for Aaron, as there will be for Moses; the people who grumbled at him weep for him, which is how it usually goes.",
   [loses("Hebrew 'had died' is lost."), keeps("Greek 'had been released'.")], ['high-priest']),
 },
}
