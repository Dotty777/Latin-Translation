K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
CALF = [loses("Hebrew 'bulls' is lost."), keeps("Greek 'calves'."), between("The Latin and King James have 'bullocks' or 'calves'.")]
GOD = [loses("Hebrew 'YHWH' is lost."), keeps("Greek 'God'."), between("The Latin and King James have 'the Lord'.")]
BURNT = [loses("Hebrew 'burnt offering' is lost."), keeps("Greek 'sacrifice' or 'whole burnt offerings'."), between("The Latin and King James have 'burnt offering' or 'sacrifice'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 23,
 'chapterNote': "Balaam's first two oracles. Seven altars, seven bulls and rams; Balaam goes aside to meet YHWH, who puts a word in his mouth: 'How can I curse whom God has not cursed? a people dwelling alone; who can count the dust of Jacob? let me die the death of the upright.' Balak protests and moves him to Pisgah; a second word: 'God is not a man that he should lie … he has blessed and I cannot reverse it; he has not seen iniquity in Jacob; YHWH their God is with them, the acclamation of a king among them; God brings them out of Egypt with a wild ox's strength; no divination in Israel; a people rising like a lion.' Balak says curse them not nor bless them, and tries a third place, Peor. The Greek has 'calves' for 'bulls' throughout, 'God' for 'YHWH' in most places, a singular offerer (23:2), expands 23:3 and 'went straight on' for 'a bare height', adds 'God's Spirit came upon him' and 'Mesopotamia' for 'Aram' (23:7), reverses the divine names and doubles 'curse' (23:8), 'mountains … shall see' (23:9), 'who has measured Jacob's seed … may my seed be like their seed' for 'the dust of Jacob … a fourth … let my end be like theirs' (23:10), 'lookout … Hewn Height' for Zophim and Pisgah (23:14), 'inquire of God' (23:15), 'as a witness' (23:18), 'led astray … threatened' for 'lie … change His mind' (23:19), 'I will bless' for 'He has blessed' (23:20), 'no toil … no distress … glories of rulers' for 'not looked upon iniquity … trouble … acclamation of a king' (23:21), 'glory as a one-horned beast' for 'strength like a wild ox' (23:22), 'will accomplish' for 'has done' (23:23), and 'lion cub … exult' (23:24).",
 'verses': {
  '23:1': v("Balaam said to Balak: build me seven altars here and prepare seven bulls and seven rams.", "The Hebrew 'bulls'; the Greek 'calves' and bomoi for pagan altars.",
   ["Seven altars.", "Seven bulls.", "Seven rams."], "Balaam began with sacrifice.", "Seven altars for a curse: Balaam does divination the expensive way, as if the number of altars could move God.",
   CALF + [keeps("Greek bomoi, the word for pagan altars, not the sanctuary's.")]),
  '23:2': v("Balak did as Balaam said; Balak and Balaam offered a bull and a ram on each altar.", "The Hebrew names both; the Greek a singular agent.",
   ["Balak did so.", "A bull and a ram.", "On each altar."], "King and seer sacrificed together.", "Fourteen animals on seven altars; the pagan rite is performed exactly, and will fail exactly.",
   CALF + [loses("Hebrew 'Balak and Balaam offered' is lost."), keeps("Greek 'he offered'.")]),
  '23:3': v("Balaam said: stand by your burnt offering while I go; perhaps YHWH will meet me, and what he shows me I will tell you. He went to a bare height.", "The Hebrew shephi 'bare height' is difficult; the Greek expands Balak's standing and 'went straight on … to inquire of God'.",
   ["Stand by your offering.", "Perhaps YHWH will meet me.", "He went aside."], "Balaam sought a meeting with God.", "'Perhaps YHWH will meet me': the diviner does not command God; he goes to a bare hill and hopes.",
   BURNT + GOD + [loses("Hebrew 'he went to a bare height' is lost."), keeps("Greek 'Balak stood beside his sacrifice, and Balaam went to inquire of God; he went straight on'.")], ['yhwh-yahweh']),
  '23:4': v("God met Balaam, who said: I have arranged seven altars and offered a bull and a ram on each.", "All four columns agree; 'appeared … calf' in Greek.",
   ["God met Balaam.", "Seven altars.", "A bull and ram on each."], "Balaam reported his sacrifices.", "He tells God what he has spent, as if submitting an invoice; God does not reply to it.", CALF + [keeps("Greek 'God appeared to Balaam'.")], ['elohim']),
  '23:5': v("YHWH put a word in Balaam's mouth: return to Balak and speak thus.", "All four columns agree; 'God' in Greek.",
   ["YHWH put a word.", "In Balaam's mouth.", "Return and speak."], "God gave Balaam his words.", "'Put a word in his mouth': the prophet as a vessel; whatever Balaam wanted to say, this is what comes out.", GOD, ['yhwh-yahweh']),
  '23:6': v("He returned, and there Balak stood by his burnt offering with all Moab's officials.", "All four columns agree; plural offerings in Greek.",
   ["He returned.", "Balak by his offering.", "With all the officials."], "The court waited for the curse.", "The whole Moabite court at the altars, waiting for the words they paid for.", BURNT),
  '23:7': v("He took up his oracle: Balak brought me from Aram, Moab's king from the eastern mountains: come, curse Jacob; come, denounce Israel.",
   "The Hebrew begins with the oracle; the Greek adds 'God's Spirit came upon him' (the Hebrew has that at 24:2) and 'Mesopotamia' for Aram.",
   ["Balak brought me from Aram.", "Come, curse Jacob.", "Denounce Israel."], "The first oracle began with Balak's request.", "The oracle opens by quoting the commission, so that everyone hears what was asked before hearing what is given instead.",
   [keeps("Greek 'God's Spirit came upon him … from Mesopotamia … call down a curse'."), between("The Latin and King James have 'Aram' or 'Syria' and no Spirit clause here.")], ['jacob']),
  '23:8': v("How can I curse whom God has not cursed? how denounce whom YHWH has not denounced?", "The Greek reverses the divine names and repeats 'curse'.",
   ["How can I curse?", "Whom God has not cursed.", "Whom YHWH has not denounced."], "Balaam could not curse the blessed.", "The first words out of the bought mouth: a refusal. Balaam cannot curse what God has not, and says so in front of the king who paid.",
   [keeps("Greek 'whom the Lord does not curse … whom God does not curse'.")], ['elohim', 'yhwh-yahweh']),
  '23:9': v("From the rock-tops I see them, from the hills I behold them: a people dwelling alone, not reckoned among the nations.", "The Hebrew 'rocks … I see'; the Greek 'mountains … I shall see'.",
   ["From the heights I see them.", "A people dwelling alone.", "Not reckoned among nations."], "Israel was seen as set apart.", "'A people dwelling alone': the seer sees from Baal's height what Leviticus said from Sinai, a nation separated. Dwelling alone is their blessing and will be their burden.",
   [loses("Hebrew 'tops of rocks … I see' is lost."), keeps("Greek 'tops of mountains … I shall see'.")]),
  '23:10': v("Who can count the dust of Jacob or number a fourth of Israel? let me die the death of the upright, and my end be like theirs!",
   "The Hebrew 'dust … a fourth … my end'; the Greek 'who has measured Jacob's seed … count Israel's clans … may my seed be like their seed'.",
   ["Who can count Jacob's dust?", "A fourth of Israel?", "Let me die the death of the upright."], "Balaam envied Israel's end.", "'The dust of Jacob', Abraham's promise in Balaam's mouth; and the hired curser asks to die as Israel dies. He will not: chapter 31 kills him with Midian.",
   [loses("Hebrew 'the dust of Jacob … a fourth of Israel … let my end be like theirs' is lost."), keeps("Greek 'who has measured Jacob's seed exactly … count Israel's clans … may my seed be like their seed'.")], ['jacob', 'abraham']),
  '23:11': v("Balak said: what have you done to me? I brought you to curse my enemies, and you have blessed them!", "All four columns agree.",
   ["What have you done?", "I brought you to curse.", "You have blessed!"], "Balak protested the blessing.", "'You have thoroughly blessed them': the king's outrage is the oracle's proof; the curse came out backwards and everyone heard it.", [AGREE]),
  '23:12': v("He answered: must I not take care to speak what YHWH puts in my mouth?", "All four columns agree; 'God' in Greek.",
   ["Must I not take care?", "To speak.", "What YHWH puts in my mouth."], "Balaam pleaded his constraint.", "The excuse is also the truth: his mouth is not his own. Balak was warned at 22:38.", GOD, ['yhwh-yahweh']),
  '23:13': v("Balak said: come to another place where you see only their edge, not all; curse them from there.", "All four columns agree.",
   ["Another place.", "See only part.", "Curse from there."], "Balak tried a different view.", "Balak's theory: the view was the problem; see fewer of them and the curse may take. Magic as geography.", [AGREE]),
  '23:14': v("He took him to the field of Zophim on the summit of Pisgah, built seven altars and offered a bull and a ram on each.", "The Hebrew names Zophim and Pisgah; the Greek 'a lookout in a field … the Hewn Height'.",
   ["The field of Zophim.", "The summit of Pisgah.", "Seven altars again."], "The rite was repeated on Pisgah.", "Pisgah, where Moses will stand to see the land; Balaam stands there to curse the people who will enter it.",
   CALF + [loses("Hebrew 'the field of Zophim … Pisgah' is lost."), keeps("Greek 'a lookout in a field … the summit of the Hewn Height'.")]),
  '23:15': v("He said to Balak: stand here by your burnt offering while I seek a meeting over there.", "The Hebrew leaves the object unstated; the Greek 'inquire of God'.",
   ["Stand by your offering.", "I will seek a meeting.", "Over there."], "Balaam went aside again.", "The same move; Balaam still goes to meet, not to command.", BURNT + [keeps("Greek 'while I go to inquire of God'.")]),
  '23:16': v("YHWH met Balaam, put a word in his mouth: return to Balak and speak thus.", "All four columns agree; 'God' in Greek.",
   ["YHWH met him.", "A word in his mouth.", "Return and speak."], "God gave the second word.", "The second word given as the first; the location changed nothing.", GOD, ['yhwh-yahweh']),
  '23:17': v("He came to him; Balak stood by his burnt offering with Moab's officials, and asked: what did YHWH say?", "The Greek adds 'all'.",
   ["He came.", "Balak by his offering.", "What did YHWH say?"], "Balak asked for the word.", "'What did YHWH say?' Balak uses the name now; he is learning whose word this is.", BURNT + [keeps("Greek 'all the officials'.")], ['yhwh-yahweh']),
  '23:18': v("He took up his oracle: rise, Balak, and hear; listen to me, son of Zippor!", "The Hebrew 'listen to me'; the Greek 'listen as a witness'.",
   ["Rise, Balak.", "Hear.", "Listen, son of Zippor."], "The second oracle addressed Balak.", "'Rise and hear': the king is told to stand for the word, as Israel stood at Sinai.",
   [loses("Hebrew 'listen to me' is lost."), keeps("Greek 'listen as a witness'.")]),
  '23:19': v("God is not a man that he should lie, or a son of man that he should change his mind; has he said and will not do? spoken and not fulfil?",
   "The Hebrew 'lie … change His mind'; the Greek 'be led astray … be threatened'. Both affirm God's reliable word.",
   ["God is not a man.", "He does not lie or repent.", "He does what he says."], "God's word was declared unchangeable.", "'God is not a man that He should lie': the pagan prophet states Israel's doctrine of God's faithfulness more plainly than Israel ever did. Balak hired a curse and got a creed.",
   [loses("Hebrew 'that He should lie … change His mind' is lost."), keeps("Greek 'to be led astray … to be threatened'."), between("The Latin and King James have 'lie … repent'.")], ['elohim']),
  '23:20': v("I have received a command to bless; he has blessed, and I cannot reverse it.", "The Hebrew 'He has blessed … I cannot'; the Greek 'I will bless and certainly will not'.",
   ["A command to bless.", "He has blessed.", "I cannot reverse it."], "The blessing could not be undone.", "'He has blessed, and I cannot reverse it': the blessing is already given, long before Balaam; he can only report it.",
   [loses("Hebrew 'He has blessed, and I cannot reverse it' is lost."), keeps("Greek 'I will bless and certainly will not reverse it'.")]),
  '23:21': v("He has not looked on iniquity in Jacob or seen trouble in Israel; YHWH their God is with them, and the acclamation of a king is among them.",
   "The Hebrew 'not looked upon iniquity … trouble … acclamation of a king'; the Greek 'no toil … no distress … the glories of rulers'. The Hebrew words can also mean misfortune.",
   ["No iniquity seen in Jacob.", "YHWH their God with them.", "A king's acclamation."], "God saw no fault in Israel.", "'He has not seen iniquity in Jacob': after Korah, the quail, Kadesh; the seer is shown Israel as God chooses to see it. 'The shout of a king among them', and the king is YHWH.",
   [loses("Hebrew 'He has not looked upon iniquity … trouble … the acclamation of a king' is lost."), keeps("Greek 'no toil in Jacob, neither shall distress be seen … the glories of rulers'."), between("The Latin has 'no idol in Jacob'; the King James 'iniquity … perverseness … shout of a king'.")], ['yhwh-yahweh', 'jacob', 'king-israel-jews']),
  '23:22': v("God brings them out of Egypt; for them there is strength like a wild ox's.", "The Hebrew 'strength … wild ox'; the Greek 'glory … one-horned beast'.",
   ["God brings them out of Egypt.", "Strength.", "Like a wild ox."], "The exodus was their strength.", "'Like the horns of the wild ox': the aurochs, the strongest beast the ancients knew; the Greek made it one-horned and the Latin a rhinoceros, and the English a unicorn.",
   [loses("Hebrew 'strength like a wild ox's' is lost."), keeps("Greek 'his glory is as that of a one-horned beast' (monokeros)."), between("The Latin has 'rhinoceros'; the King James 'unicorn'.")], ['egypt', 'elohim']),
  '23:23': v("No omen-taking in Jacob, no divination in Israel; at the appointed time it is said of Jacob and Israel: what God has done!", "The Hebrew past 'has done'; the Greek future 'will accomplish'. Hebrew 'in' may be 'against'.",
   ["No omens in Jacob.", "No divination in Israel.", "What God has done!"], "Israel needed no diviners.", "A diviner saying there is no divination in Israel: Balaam's trade is useless against them, because they are told what God does without it.",
   [loses("Hebrew 'What God has done!' is lost."), keeps("Greek 'what God will accomplish'.")], ['spirit-of-divination']),
  '23:24': v("A people rises like a lioness and lifts itself like a lion; it will not lie down till it eats prey and drinks the blood of the slain.", "The Hebrew 'lioness … lifts itself … lie down'; the Greek 'lion cub … exult … sleep'.",
   ["Like a lioness.", "Like a lion.", "Devouring prey."], "Israel was a lion to its enemies.", "Judah's lion from Jacob's blessing, now the whole people's; the seer hired to make them prey calls them the predator.",
   [loses("Hebrew 'lioness … lifts itself up … lie down' is lost."), keeps("Greek 'lion cub … exult … sleep'.")], ['lion-root-david']),
  '23:25': v("Balak said: do not curse them at all, and do not bless them at all!", "All four columns agree.",
   ["Do not curse.", "Do not bless.", "At all!"], "Balak begged for silence.", "Having bought a curse and received two blessings, the king settles for nothing; silence is the best he can hope for now.", [AGREE]),
  '23:26': v("Balaam answered: did I not tell you I must do all YHWH says?", "All four columns agree; 'God' in Greek.",
   ["Did I not tell you?", "I must do.", "All YHWH says."], "Balaam repeated his constraint.", "Third time said: the man cannot help it. Balaam's helplessness is the story's comedy and its theology.", GOD, ['yhwh-yahweh']),
  '23:27': v("Balak said: come, I will take you to another place; perhaps it will be right in God's eyes to curse them from there.", "All four columns agree.",
   ["Another place.", "Perhaps God will allow.", "Curse from there."], "Balak tried a third time.", "'Perhaps it will be right in God's eyes': Balak has learned the vocabulary and nothing else; he still thinks the right hill will change God's mind.", [AGREE], ['elohim']),
  '23:28': v("Balak took Balaam to the summit of Peor, overlooking the wasteland.", "All four columns agree.",
   ["To Peor.", "The summit.", "Over the waste."], "The third site was Peor.", "Peor: the name of the god Israel will whore after in chapter 25. The third curse is attempted from the mountain of Israel's next sin.", [AGREE]),
  '23:29': v("Balaam said: build me seven altars here and prepare seven bulls and seven rams.", "All four columns agree; 'calves' in Greek.",
   ["Seven altars.", "Seven bulls.", "Seven rams."], "The rite was set up a third time.", "Twenty-one altars and forty-two animals so far, for three blessings.", CALF),
  '23:30': v("Balak did as Balaam said and offered a bull and a ram on each altar.", "All four columns agree; 'calf' in Greek.",
   ["Balak did so.", "A bull and a ram.", "On each altar."], "Balak complied again.", "The king obeys the prophet as the prophet obeys God; the chain runs the wrong way for Balak.", CALF),
 },
}
