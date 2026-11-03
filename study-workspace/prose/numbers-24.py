K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
EYE = [loses("Hebrew 'the man whose eye is opened' (shetum, uncertain: opened or closed) is lost."), keeps("Greek 'the man who sees truly'."), between("The Latin has 'whose eye is closed'; the King James 'whose eyes are open'.")]
SLEEP = [loses("Hebrew 'a vision of Shaddai, falling down' is lost."), keeps("Greek 'a vision of God in sleep'."), between("The Latin has 'the Almighty … falling'; the King James 'the Almighty, falling into a trance'.")]
OX = [loses("Hebrew 'strength like a wild ox's' is lost."), keeps("Greek 'glory like a one-horned beast's'."), between("The Latin has 'rhinoceros'; the King James 'unicorn'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 24,
 'chapterNote': "Balaam's last oracles. Seeing that YHWH means to bless, Balaam drops his omens; God's Spirit comes on him and he speaks: 'How good are your tents, Jacob … water from his buckets, his king higher than Agag, strength like a wild ox, a lion no one rouses; blessed who bless you, cursed who curse you.' Balak claps his hands and dismisses him unpaid. Balaam's fourth oracle looks to the latter days: 'a star shall march from Jacob, a sceptre rise from Israel, crushing Moab and Seth, possessing Edom and Seir.' Then Amalek ('first among nations, its end destruction'), the Kenites (safe in the rock until Asshur), a lament ('who can live when God appoints this?'), and ships from Kittim afflicting Asshur and Eber and perishing too. Balaam and Balak go home. The Greek has 'within him' (24:2), 'the man who sees truly' for the uncertain 'whose eye is opened' (24:3, 15), 'in sleep' for 'falling down' and 'God' for Shaddai (24:4, 16), 'houses' (24:5), 'tents pitched by the Lord' for 'aloes planted by YHWH' (24:6), 'a man shall come forth from his seed and rule over many nations … higher than Gog' for 'water from his buckets … his king higher than Agag' (24:7), 'glory … one-horned beast … suck the marrow' (24:8), 'lion cub' (24:9), 'this third time … enemy' (24:10), 'glory' (24:11), 'God' (24:13), 'my place' (24:14), 'I will show him … pronounce him blessed … a man … Moab's leaders … plunder' for 'I see him … behold him … a sceptre … Moab's temples … break down' (24:17), 'Esau, his enemy' for 'Seir, his enemies' (24:18), 'arise' for 'rule' (24:19), 'their seed shall perish' (24:20), a conditional at 24:21 and 'a nest of craftiness … Beor' for 'Kain shall be burned' (24:22), adds 'he saw Og' and doubles the lament (24:23), and 'one shall come from the Kitians' hand' for 'ships from Kittim' (24:24).",
 'verses': {
  '24:1': v("Balaam saw that it pleased YHWH to bless Israel, so he did not go as before to seek omens; he turned his face toward the wilderness.", "All four columns agree.",
   ["It pleased YHWH to bless.", "No more omens.", "He faced the wilderness."], "Balaam gave up divination.", "He stops consulting omens: the diviner has learned that the answer will not change, and simply looks at the camp. The third oracle comes without a ritual.", [AGREE], ['yhwh-yahweh']),
  '24:2': v("Balaam raised his eyes and saw Israel dwelling by tribes, and God's Spirit came upon him.", "The Hebrew 'upon him'; the Greek 'within him'.",
   ["He saw Israel by tribes.", "God's Spirit.", "Came upon him."], "The Spirit inspired a pagan.", "The camp of chapter 2 seen from a hill, in its square by standards; and God's Spirit on a Mesopotamian sorcerer, who speaks the Torah's longest blessing of Israel.",
   [loses("Hebrew 'came upon him' is lost."), keeps("Greek 'came within him'."), between("The Latin has 'rushed upon him'.")], ['spirit-god-lord', 'term-pneuma-ruach']),
  '24:3': v("He took up his oracle: the utterance of Balaam son of Beor, of the man whose eye is opened,", "The Hebrew shetum is uncertain; the Greek 'who sees truly'; the Latin 'whose eye is closed'.",
   ["The utterance of Balaam.", "Son of Beor.", "The man whose eye is opened."], "The third oracle was formally introduced.", "'Whose eye is opened', or closed: the Hebrew word is read both ways, and the ambiguity suits a seer blinder than his donkey who now sees. The Greek chose sight.", EYE),
  '24:4': v("The utterance of one who hears God's words, who sees a vision of Shaddai, falling down with eyes uncovered:", "The Hebrew 'Shaddai … falling down'; the Greek 'God … in sleep'.",
   ["Hears God's words.", "Sees Shaddai's vision.", "Eyes uncovered."], "Balaam claimed true vision.", "'Falling down with eyes uncovered': prostrate and seeing at once, the posture of 22:31 made a title; the Greek thought he was asleep.", SLEEP, ['el-shaddai']),
  '24:5': v("How good are your tents, Jacob, your dwellings, Israel!", "The Hebrew 'tents … dwellings'; the Greek 'houses … tents'.",
   ["How good your tents.", "Jacob.", "Your dwellings, Israel."], "Israel's camp was praised.", "Mah tovu, the words Jews say entering a synagogue: a pagan's praise of Israel's tents became the Jewish doorway prayer.",
   [loses("Hebrew 'tents … dwellings' is lost."), keeps("Greek 'houses … tents'."), between("The Latin has 'tabernacles'; the King James 'tents … tabernacles'.")], ['jacob']),
  '24:6': v("Like valleys stretching out, like gardens by a river, like aloes planted by YHWH, like cedars by waters.", "The Hebrew 'aloes planted by YHWH'; the Greek 'tents pitched by the Lord'; 'shaded wooded valleys'.",
   ["Like valleys.", "Like gardens by a river.", "Like cedars by water."], "Israel was likened to a watered garden.", "Gardens and cedars and running water, said of a people camped in a desert: the seer describes what they will be, or what they are to God.",
   [loses("Hebrew 'aloes planted by YHWH … valleys stretching out' is lost."), keeps("Greek 'tents pitched by the Lord … shaded wooded valleys'.")], ['yhwh-yahweh', 'eden']),
  '24:7': v("Water flows from his buckets and his seed has abundant water; his king rises higher than Agag, and his kingdom is exalted.",
   "The Hebrew's water and seed and 'Agag'; the Greek 'a man shall come forth from his seed and rule over many nations; his kingdom shall rise higher than Gog'.",
   ["Water from his buckets.", "His king above Agag.", "His kingdom exalted."], "Israel's king would surpass Agag.", "Buckets overflowing and a king above Agag, the Amalekite Saul will spare; the Greek read instead a man from Israel ruling nations, higher than Gog, and the church read him as Messiah. Two prophecies in one verse.",
   [loses("Hebrew 'water shall flow from his buckets … his king shall rise higher than Agag' is lost."), keeps("Greek 'a man shall come forth from his seed and rule over many nations; his kingdom shall rise higher than Gog'."), between("The Latin and King James have the water and Agag.")], ['king-israel-jews', 'christ-messiah']),
  '24:8': v("God brings him out of Egypt; his strength is a wild ox's; he devours the nations against him, gnaws their bones, pierces them with his arrows.", "The Hebrew 'strength … wild ox … bones … arrows'; the Greek 'glory … one-horned beast … marrow from their fat … missiles'.",
   ["Out of Egypt.", "A wild ox's strength.", "Devouring nations."], "Israel's power was God's doing.", "The wild ox of 23:22 again, now devouring; the oracle's gentleness turns to teeth and arrows in a line.",
   OX + [loses("Hebrew 'gnaw their bones … arrows' is lost."), keeps("Greek 'suck the marrow from their fat parts … missiles'.")], ['egypt', 'elohim']),
  '24:9': v("He crouched and lay like a lion, like a lioness; who will rouse him? blessed who bless you, cursed who curse you.", "The Hebrew 'lioness'; the Greek 'lion cub'.",
   ["A lion lying down.", "Who will rouse him?", "Blessed who bless you."], "Abraham's blessing was pronounced on Israel.", "Jacob's blessing on Judah and God's on Abraham, in a Moabite king's hearing: 'cursed are those who curse you'. Balak has just hired a cursing, and hears his own sentence.",
   [loses("Hebrew 'lioness' is lost."), keeps("Greek 'lion cub'.")], ['abraham', 'lion-root-david']),
  '24:10': v("Balak's anger burned; he struck his hands together: I summoned you to curse my enemies, and you have thoroughly blessed them three times!", "The Greek 'enemy … this third time'.",
   ["Balak's anger.", "He clapped his hands.", "Blessed three times!"], "Balak lost his temper.", "The clap of hands, the gesture of a man whose money is gone; three curses bought, three blessings delivered.",
   [keeps("Greek 'my enemy … this third time'.")]),
  '24:11': v("Flee to your place! I said I would honour you, but YHWH has kept you from honour.", "The Greek 'glory'.",
   ["Flee to your place.", "I would have honoured you.", "YHWH kept you from it."], "Balaam was dismissed unpaid.", "'YHWH has kept you from honour': Balak says the true thing in anger; the prophet who would not curse goes home without his fee.",
   [keeps("Greek 'deprived you of glory'.")], ['yhwh-yahweh']),
  '24:12': v("Balaam said to Balak: did I not tell the messengers you sent to me:", "All four columns agree.",
   ["Did I not tell?", "Your messengers.", "Sent to me."], "Balaam recalled his warning.", "Balaam's defence is the record; he said so at the start.", [AGREE]),
  '24:13': v("If Balak gave me his house full of silver and gold, I could not go beyond YHWH's command to do good or evil of my own will; what YHWH speaks I speak.", "The Greek 'evil or good … God'.",
   ["A house of silver and gold.", "Not beyond YHWH's command.", "What YHWH speaks."], "Balaam repeated 22:18.", "Word for word his first answer: 'what YHWH speaks, I must speak'. For all his willingness to be bought, Balaam's mouth stayed God's.",
   [keeps("Greek 'to do evil or good on my own. Whatever God says'.")], ['yhwh-yahweh']),
  '24:14': v("Now I go to my people; come, I will advise you what this people will do to yours in the latter days.", "The Hebrew 'my people'; the Greek 'my place'.",
   ["I go to my people.", "I will advise you.", "In the latter days."], "Balaam offered a last word.", "'In the latter days': the dismissed seer offers a free prophecy, and it is the one the centuries remembered.",
   [loses("Hebrew 'to my people' is lost."), keeps("Greek 'returning to my place'.")]),
  '24:15': v("He took up his oracle: the utterance of Balaam son of Beor, of the man whose eye is opened,", "As 24:3; the Latin adds 'again'.",
   ["The utterance of Balaam.", "Son of Beor.", "Whose eye is opened."], "The fourth oracle began like the third.", "The formula repeated; the seer introduces himself for the last word.", EYE),
  '24:16': v("The utterance of one who hears God's words and knows the Most High's knowledge, who sees Shaddai's vision, falling down with eyes uncovered:", "The Greek 'knowledge from the Most High … God … in sleep'.",
   ["Hears God's words.", "Knows the Most High's knowledge.", "Sees Shaddai's vision."], "Balaam claimed the highest knowledge.", "El Elyon, the Most High, Melchizedek's name for God, added to the title; the oracle that follows is the farthest-seeing in the book.",
   SLEEP + [keeps("Greek 'knowledge from the Most High'.")], ['el-elyon', 'el-shaddai']),
  '24:17': v("I see him, but not now; I behold him, but not near: a star shall march from Jacob, a sceptre rise from Israel; it crushes Moab's temples and breaks down all the sons of Seth.",
   "The Hebrew 'see … behold … sceptre … temples … break down'; the Greek 'show … pronounce blessed … a man … leaders … plunder'. Neither names Jesus.",
   ["Not now, not near.", "A star from Jacob.", "A sceptre from Israel."], "A future ruler was foreseen.", "The star and the sceptre: David to the rabbis, Christ to the church, the Greek's 'a man' to both. 'Not now, not near': the one oracle Balaam himself says he does not understand.",
   [loses("Hebrew 'I see him … I behold him … a sceptre … Moab's temples … break down' is lost."), keeps("Greek 'I will show him … I pronounce him blessed … a man shall arise … Moab's leaders … plunder'."), between("The Latin and King James have the sceptre.")], ['jacob', 'david', 'christ-messiah', 'son-of-david']),
  '24:18': v("Edom becomes a possession, and Seir, his enemies, a possession, while Israel acts valiantly.", "The Hebrew 'Seir, his enemies'; the Greek 'Esau, his enemy'.",
   ["Edom a possession.", "Seir too.", "Israel valiant."], "Edom would fall to Israel.", "Edom, who barred the road in chapter 20, is promised to the star's hand; the brother's refusal is answered in prophecy.",
   [loses("Hebrew 'Seir, his enemies' is lost."), keeps("Greek 'Esau, his enemy'.")]),
  '24:19': v("One from Jacob rules and destroys the survivor from the city.", "The Hebrew 'rule'; the Greek 'arise'.",
   ["One from Jacob.", "Rules.", "Destroys the survivor."], "Jacob's ruler would be total.", "'The survivor from the city': the oracle does not leave a remnant of the enemy; the Greek softened 'rule' to 'arise'.",
   [loses("Hebrew 'shall rule' is lost."), keeps("Greek 'shall arise'.")], ['jacob']),
  '24:20': v("He saw Amalek and took up his oracle: Amalek was first among the nations, but its end is destruction.", "The Hebrew 'its end'; the Greek 'their seed shall perish'.",
   ["He saw Amalek.", "First among nations.", "Its end destruction."], "Amalek was doomed.", "Amalek, who attacked at Rephidim and cut down the stragglers, first to fight Israel and promised last; Saul and Esther will finish it.",
   [loses("Hebrew 'its end is destruction' is lost."), keeps("Greek 'their seed shall perish'.")]),
  '24:21': v("He saw the Kenites and took up his oracle: your dwelling is enduring and your nest set in the rock;", "The Greek makes it conditional 'even if'.",
   ["He saw the Kenites.", "Your dwelling endures.", "Your nest in the rock."], "The Kenites seemed secure.", "The Kenites, Hobab's people, Moses' in-laws, who will live among Judah; their rock-nest is praised before its end is told.",
   [keeps("Greek 'even if you set your nest in a rock'.")], ['rock']),
  '24:22': v("Yet Kain shall be burned away; how long until Asshur takes you captive?", "The Hebrew 'Kain … burned'; the Greek 'even if a nest of craftiness should belong to Beor, Assyrians shall take you captive'. The Hebrew is difficult.",
   ["Kain burned away.", "How long?", "Asshur takes you."], "Even the Kenites would fall to Assyria.", "Asshur named in the Torah: the empire that will carry Israel away is foreseen taking the Kenites first. The Greek lost the thread and wrote 'Beor'.",
   [loses("Hebrew 'yet Kain shall be burned away. How long' is lost."), keeps("Greek 'even if a nest of craftiness should belong to Beor'.")]),
  '24:23': v("He took up his oracle: alas, who can live when God appoints this?", "The Greek adds 'he saw Og' and doubles 'alas'.",
   ["He took up his oracle.", "Alas!", "Who can live?"], "Balaam lamented the future.", "'Who can live when God does this?' The seer who blessed Israel ends afraid of what he sees; the latter days are not safe for anyone.",
   [keeps("Greek 'he saw Og … Alas, alas! … brings these things about'.")], ['elohim', 'og']),
  '24:24': v("Ships come from the coast of Kittim and afflict Asshur and Eber; but they too end in destruction.", "The Hebrew 'ships from Kittim … Eber'; the Greek 'one from the Kitians' hand … the Hebrews'; the Latin 'triremes from Italy'.",
   ["Ships from Kittim.", "Afflict Asshur and Eber.", "They too perish."], "A western power would come and go.", "Ships from the west, Cyprus or beyond, that beat Assyria and perish in turn; the oracle ends with empires rising and falling in a line, and Israel's star above them all.",
   [loses("Hebrew 'ships … Eber' is lost."), keeps("Greek 'one shall come forth from the hand of the Kitians … the Hebrews'."), between("The Latin has 'triremes from Italy'; the King James 'ships … Chittim … Eber'.")]),
  '24:25': v("Balaam rose and returned to his place, and Balak went his way.", "All four columns agree; the Latin 'by the way he had come'.",
   ["Balaam rose.", "Returned to his place.", "Balak went home."], "The two parted.", "They go home, the king with nothing and the seer with nothing; but Balaam will be back in chapter 31, dead among Midian's kings, and chapter 25 will show whose counsel Peor followed.",
   [between("The Latin adds 'by the way he had come'.")]),
 },
}
