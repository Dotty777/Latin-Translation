K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
BREAD = [loses("Hebrew 'the bread of his God' is lost."), keeps("Greek 'the gifts of his God'."), between("The Latin and King James keep 'bread'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'leviticus', 'chapter': 21,
 'chapterNote': "The holiness of the priests: an ordinary priest may defile himself for the dead only for his nearest kin (parents, children, brother, unmarried sister), may not shave bald patches, beard edges or gash himself, may not marry a prostitute, profaned or divorced woman, and his daughter who prostitutes herself is burned; the high priest, anointed and clothed, may not loosen his hair or tear his garments, enter where a corpse is even for his parents, or leave the sanctuary, and marries only a virgin of his own people; a descendant of Aaron with a blemish (blind, lame, mutilated, broken-limbed, hunchbacked, wasted, eye-defect, scabbed, crushed testicle) may eat the holy food but not approach curtain or altar. 'I am YHWH who sanctifies' recurs (21:8, 15, 23). The Greek pluralizes the priests (21:1), reverses parents' order (21:2), reads 'suddenly' where the Hebrew's difficult 'as a husband/master' stands (21:4), adds 'for a dead person' (21:5), has 'gifts' for the Hebrew's 'bread of his God' throughout (21:6, 8, 17, 21, 22), third person 'he shall sanctify him … sanctifies them' for the Hebrew's 'you shall regard him as holy … sanctifies you' (21:8), 'remove his turban' for 'let his hair hang loose' (21:10), adds 'from his own kin' (21:13), lists 'cut-off ear' for 'overgrown limb' (21:18) and 'skin spot, diseased eyelids, single testicle' for 'wasted, eye defect, crushed testicle' (21:20), and 'the holy place of his God' for 'My sanctuaries' (21:23). The Latin adds 'all that was commanded' at 21:24.",
 'verses': {
  '21:1': v("YHWH tells Moses to speak to the priests, Aaron's sons: a priest does not make himself unclean for a dead person among his people,",
   "The Hebrew singular 'a priest'; the Greek plural 'they shall not be defiled'. The speech formula agrees.",
   ["To the priests.", "Aaron's sons.", "Not unclean for the dead."], "Priests were kept from corpse defilement.", "After the people's holiness, the priests': the man who stands at the altar cannot stand at a grave.",
   FORMULA + [loses("Hebrew singular 'a priest shall not' is lost."), keeps("Greek plural 'they shall not be defiled for dead persons'.")], ['yhwh-yahweh', 'moses', 'high-priest'], "A priest shall not make himself unclean for the dead."),
  '21:2': v("Except for nearest kin: mother, father, son, daughter, brother;", "The Hebrew mother before father, singular children; the Greek father, mother, sons, daughters.",
   ["Nearest kin.", "Mother, father.", "Son, daughter, brother."], "Nearest kin were the exception.", "Blood is allowed its claim: for those who made him and those he made, the priest may be unclean a week.",
   [loses("Hebrew 'his mother, his father, his son, his daughter' is lost in order."), keeps("Greek 'father, mother, sons, daughters, and brother'."), between("The Latin and King James also have father first.")]),
  '21:3': v("And for his virgin sister near him, who has not belonged to a man, he may make himself unclean.", "All four columns agree; the Greek 'for these' resumes all relatives, the Hebrew 'for her' the sister.",
   ["A virgin sister.", "Not yet a man's.", "He may be unclean."], "The unmarried sister counted as nearest kin.", "The unmarried sister has no husband to mourn her; her brother the priest is allowed to.",
   [keeps("Greek 'for these he may defile himself'."), between("The Latin and King James have the sister as object.")]),
  '21:4': v("He does not make himself unclean as a husband among his people, profaning himself.",
   "The Hebrew ba'al 'husband' or 'master' in a difficult construction with several traditional readings; the Greek 'suddenly' (exapina); the Latin 'not even for a ruler'. The restrictions differ materially.",
   ["Not as a husband.", "Among his people.", "Profaning himself."], "The verse's scope is disputed.", "The one word the ancients could not agree on: husband, master, ruler, or suddenly. The rule is clear in intent, that the priest does not take on grief beyond his house, and dark in its letter.",
   [loses("Hebrew 'as a husband (ba'al) among his people' is lost."), keeps("Greek 'he shall not suddenly defile himself among his people'."), between("The Latin has 'not even for a ruler of his people'; the King James 'being a chief man among his people'.")]),
  '21:5': v("They do not make a bald patch, shave the beard's edge, or gash their flesh.", "The Hebrew leaves the mourning setting to context; the Greek adds 'for a dead person' and shifts to second person.",
   ["No bald patch.", "No shaved beard edge.", "No gashes."], "Mourning marks were forbidden to priests.", "The laity were told this in 19:27–28; the priests are told again, since their grief is more visible and the temptation to show it greater.",
   [keeps("Greek 'you shall not shave a bald patch on your head for a dead person'."), between("The Latin and King James follow the Hebrew's third person.")], [], "They shall not make a bald patch or gash their flesh."),
  '21:6': v("They are holy to their God and do not profane his name, for they present YHWH's fire offerings, the bread of their God; therefore holy.", "The Hebrew 'offerings by fire … bread of their God'; the Greek 'sacrifices … gifts'.",
   ["Holy to their God.", "Not profaning the name.", "They present God's bread."], "Priests were holy because they served God's table.", "'The bread of their God': the offerings are God's food, and the ones who serve it must be clean as a table-servant is.",
   BREAD + [loses("Hebrew 'offerings by fire' is lost."), keeps("Greek 'the Lord's sacrifices'.")], ['yhwh-yahweh', 'divine-names'], "They shall be holy to their God."),
  '21:7': v("They do not take a prostitute, a profaned woman or a divorced woman, for the priest is holy to his God.", "All four columns agree; the Greek 'expelled' for divorced and adds 'Lord'.",
   ["Not a prostitute.", "Not profaned or divorced.", "The priest is holy."], "Priestly marriage was restricted.", "The priest's house is part of the sanctuary; whom he marries is a matter of holiness, not only of taste.",
   [keeps("Greek 'a woman expelled by her husband … holy unto the Lord his God'."), between("The Latin and King James have 'divorced' or 'put away'.")], ['high-priest'], "They shall not take a prostitute or a divorced woman."),
  '21:8': v("You regard him as holy, for he presents the bread of your God; he is holy to you, for I, YHWH who sanctifies you, am holy.",
   "The Hebrew addresses the people 'you … sanctifies you'; the Greek 'he shall sanctify him … sanctifies them' and 'gifts'. The subject of the Greek 'he' is interpretive.",
   ["Regard him as holy.", "He presents God's bread.", "YHWH who sanctifies."], "The people were to treat the priest as holy.", "The people make the priest holy by how they treat him; his holiness is partly their act, and God's sanctifying stands behind both.",
   BREAD + [loses("Hebrew 'you shall regard him as holy … sanctifies you' is lost."), keeps("Greek 'he shall sanctify him … the Lord who sanctifies them'.")], ['yhwh-who-sanctifies', 'yhwh-yahweh'], "You shall regard the priest as holy."),
  '21:9': v("A priest's daughter who profanes herself by prostitution profanes her father; she is burned.", "All four columns agree; the Greek 'her father's name'.",
   ["A priest's daughter.", "Prostitution.", "Burned with fire."], "A priest's daughter's prostitution was burned.", "Fire, the penalty of 20:14, for the priest's daughter; the father's holiness makes her fall the graver.",
   [keeps("Greek 'she profanes her father's name'."), between("The Latin and King James have 'her father'.")]),
  '21:10': v("The greatest priest, anointed on the head and filled in hand to wear the garments, does not let his hair hang loose or tear his garments;",
   "The Hebrew para' 'let hair hang loose' (also read as uncovering); the Greek 'remove his turban'. The Latin 'hands consecrated'.",
   ["The high priest.", "Anointed and clothed.", "No loose hair, no torn garments."], "The high priest showed no mourning at all.", "Loose hair and torn clothes are the signs of grief; the anointed head may not show them, as Aaron could not when his sons died.",
   [loses("Hebrew 'let his hair hang loose' is lost."), keeps("Greek 'shall not remove his turban'."), between("The Latin and King James have 'uncover his head'.")], ['high-priest', 'anointing-oil'], "The high priest shall not tear his garments."),
  '21:11': v("He does not enter where any dead person is, nor make himself unclean even for father or mother.", "All four columns agree.",
   ["No entering where the dead are.", "Not even for parents.", "Unclean forbidden."], "The high priest could not mourn even parents.", "Not even his parents: the exceptions of 21:2 are closed for him; the oil on his head outweighs the blood in his veins.", [AGREE], ['high-priest'], "He shall not make himself unclean even for his father or mother."),
  '21:12': v("He does not leave the sanctuary or profane his God's sanctuary, for the consecration of the anointing oil is on him. I am YHWH.", "All four columns agree; 'holy precincts … what is consecrated' in Greek.",
   ["Not leaving the sanctuary.", "Not profaning it.", "The oil is on him."], "The anointed man stayed in the holy place.", "He may not walk out to the funeral; the sanctuary holds him as the oil marks him.",
   [keeps("Greek 'the holy anointing oil of God'."), between("The Latin and King James have 'the crown of the anointing oil'.")], ['tabernacle', 'anointing-oil', 'yhwh-yahweh']),
  '21:13': v("He takes a wife in her virginity.", "The Hebrew stops there; the Greek adds 'from his own kin', which both state in the next verse.",
   ["A wife.", "In her virginity.", "For the high priest."], "The high priest married a virgin.", "The strictest marriage law for the highest office; the house of the anointed begins from nothing shared.",
   [keeps("Greek 'a virgin wife from his own kin'."), between("The Latin and King James follow the Hebrew.")], ['high-priest'], "He shall take a wife in her virginity."),
  '21:14': v("A widow, a divorced woman, a profaned woman who is a prostitute: not these; a virgin from his people.", "The Hebrew joins 'profaned … prostitute'; the Greek separates them and 'only … from his own kin'.",
   ["Not a widow or divorced.", "Not profaned or prostitute.", "A virgin of his people."], "Even a widow was barred to the high priest.", "A widow is barred too, which the ordinary priest was not told; the high priest's bride has no history at all.",
   [keeps("Greek 'a widow, an expelled woman, a profaned woman, or a prostitute … only a virgin from his own kin'."), between("The Latin and King James follow the Hebrew.")], ['high-priest'], "He shall take only a virgin from his people."),
  '21:15': v("He does not profane his offspring among his people, for I am YHWH who sanctifies him.", "All four columns agree; the Latin 'not mingle his lineage'.",
   ["Not profaning his offspring.", "Among his people.", "YHWH who sanctifies."], "The high priest's line was kept holy.", "The marriage law protects the children: a high priest's son will be high priest, and his mother's past would be his.",
   [between("The Latin has 'not mingle the stock of his kindred with the common people'; the Greek and King James 'profane his seed'.")], ['yhwh-who-sanctifies', 'yhwh-yahweh']),
  '21:16': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On blemishes."],
   "YHWH spoke on priests with blemishes.", "A second speech: who among Aaron's sons may approach the altar at all.", FORMULA, ['yhwh-yahweh', 'moses']),
  '21:17': v("Say to Aaron: any of his offspring through their generations with a blemish does not approach to present the bread of his God.", "The Hebrew 'their generations … bread'; the Greek 'your generations … gifts'.",
   ["Aaron's offspring.", "With a blemish.", "Not to present God's bread."], "Blemished priests did not serve at the altar.", "The animal must be without blemish and so must the man who brings it; the altar asks wholeness of both.",
   BREAD + [keeps("Greek 'throughout your generations'.")], ['high-priest'], "No blemished priest shall present the bread of God."),
  '21:18': v("None with a blemish approaches: blind, lame, mutilated nose, overgrown limb;",
   "The Hebrew 'blind, lame … overgrown or disproportionate limb'; the Greek 'lame, blind … cut-off ear'. The Hebrew condition is uncertain.",
   ["Blind or lame.", "Mutilated nose.", "Overgrown limb."], "Visible deformities barred service.", "The list begins with what the eye sees first; the priest at the altar is seen by all Israel, and the law wants the sight whole.",
   [loses("Hebrew 'one with an overgrown limb' is lost."), keeps("Greek 'a lame man, a blind man … one with a cut-off ear'."), between("The Latin has 'small, large or crooked nose'; the King James 'any thing superfluous'.")]),
  '21:19': v("Or a broken foot or hand;", "All four columns agree; the Greek reverses the order.", ["Broken foot.", "Broken hand.", "Barred."],
   "Broken limbs barred service.", "A healed break still bars; the body that serves must never have been shattered.",
   [keeps("Greek 'a broken hand or a broken foot'."), between("The Latin and King James have foot first.")]),
  '21:20': v("Or a hunchback, one wasted, an eye defect, a scab or skin eruption, or a crushed testicle.",
   "The Hebrew daq 'wasted' is uncertain; the Greek 'skin spot' (ephelos), 'diseased eyelids', 'single testicle' for 'crushed testicle'. Ancient descriptions, not modern diagnoses.",
   ["Hunchback or wasted.", "Eye defect or scab.", "Crushed testicle."], "The list ended with less visible blemishes.", "Down to the hidden blemish: the priest's body is examined as the lamb's was, and the standard is the same.",
   [loses("Hebrew 'one who is wasted … a defect in his eye … a crushed testicle' are lost."), keeps("Greek 'one with a skin spot, one with diseased eyelids … one with a single testicle'."), between("The Latin has 'inflamed eyes, a white spot, a hernia'; the King James 'dwarf … blemish in his eye … stones broken'.")]),
  '21:21': v("No blemished offspring of Aaron approaches to present YHWH's fire offerings; he has a blemish; he does not present the bread of his God.", "The Hebrew 'YHWH … bread of his God'; the Greek 'your God … gifts of God'.",
   ["No blemished offspring of Aaron.", "Not YHWH's offerings.", "Not God's bread."], "The exclusion was restated.", "Said twice in one verse, 'he has a blemish'; the law's refusal is stated and then explained by repetition.",
   BREAD + [keeps("Greek 'the sacrifices unto your God … the gifts of God'.")], ['high-priest', 'yhwh-yahweh']),
  '21:22': v("He may eat the bread of his God, from the most holy and the holy things.", "All four columns agree; 'gifts' in Greek.",
   ["He may eat.", "God's bread.", "Most holy and holy."], "The blemished priest kept his portion.", "Barred from the altar, fed from it: the blemish costs him the service but not the sonship.",
   BREAD, ['high-priest']),
  '21:23': v("But he does not go toward the curtain or approach the altar, because of his blemish; he does not profane God's sanctuaries, for I am YHWH who sanctifies them.", "The Hebrew 'My sanctuaries'; the Greek 'the holy place of his God'.",
   ["Not to the curtain.", "Not to the altar.", "YHWH who sanctifies."], "Curtain and altar were off limits.", "Curtain and altar, the two holiest approaches; the line is drawn there and 'I am YHWH who sanctifies' is the reason, not the man's fault.",
   [loses("Hebrew 'My sanctuaries' is lost."), keeps("Greek 'the holy place of his God'."), between("The Latin and King James have 'My sanctuaries' or 'sanctuary'.")], ['altar', 'tabernacle', 'yhwh-who-sanctifies']),
  '21:24': v("Moses spoke to Aaron, his sons and all Israel.", "The Hebrew, Greek and King James agree; the Latin adds 'all that had been commanded'.",
   ["Moses spoke.", "To Aaron and his sons.", "And all Israel."], "The priestly laws were told to all.", "The laws about priests are told to the people too; everyone must know who may stand at the altar.",
   [between("The Latin adds 'all that the Lord had commanded'; the Greek and King James lack the clause.")], ['moses', 'high-priest']),
 },
}
