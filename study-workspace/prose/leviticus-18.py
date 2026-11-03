K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
NAKED = [between("All four columns keep the euphemism 'uncover nakedness'; the Greek word also carries the sense of shame or indecency.")]
VOMIT = [loses("Hebrew 'the land vomited out its inhabitants' is lost."), keeps("Greek 'the land became indignant with those settled upon it'."), between("The Latin and King James keep the Hebrew's vomiting image.")]
CUTOFF = [loses("Hebrew 'cut off from among their people' is lost in form."), keeps("Greek 'the souls that do them shall be destroyed from among their people'."), between("The Latin and King James have 'cut off'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'leviticus', 'chapter': 18,
 'chapterNote': "The laws by which Israel lives, set against the practices of Egypt and Canaan: the one who does them lives by them (18:5). Then the forbidden relationships, each framed as 'uncovering nakedness': father and mother, father's wife, sister, granddaughter, half-sister, aunts on both sides, uncle's wife, daughter-in-law, brother's wife, a woman and her daughter or granddaughter, two sisters at once; then a menstruating woman, a neighbour's wife, giving offspring to Molech, lying with a male, and bestiality. The chapter closes with the land itself: the nations before Israel defiled it and the land vomited them out, and Israel will be vomited out likewise if it does the same; whoever does these things is cut off. The Greek adds 'all' repeatedly and 'your God' (18:5, 26), repeats the prohibition at 18:11, has 'relative' for the Hebrew's 'aunt' (18:14), 'impiety' for 'wicked scheme' (18:17), 'to serve a ruler' for 'to be passed over to Molech' and 'holy name' for 'name of your God' (18:21), 'four-footed animal … insemination' (18:23), and three times 'the land became indignant' for the Hebrew's 'vomited out' (18:25, 28); at 18:25 the Greek also has God repay the inhabitants where the Hebrew visits the iniquity on the land, and the Greek 'destroyed' stands for 'cut off' (18:29). The Latin follows the Hebrew at Molech and the vomiting, and has 'joined by marriage' at 18:14.",
 'verses': {
  '18:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the laws of living."],
   "YHWH spoke on the laws by which Israel lives.", "After the altar and the blood, the body: the next laws govern what is done in the tent at night, not at the door by day.", FORMULA, ['yhwh-yahweh', 'moses']),
  '18:2': v("Moses is to tell Israel: I am YHWH your God.", "All four columns agree.", ["Speak to Israel.", "I am YHWH.", "Your God."],
   "The laws rested on God's own identity.", "'I am YHWH your God' before a word of law; the rules about the body begin from who owns it.", [AGREE], ['yhwh-yahweh', 'divine-names']),
  '18:3': v("Israel is not to act by the practices of Egypt where they lived, nor of Canaan where God brings them, nor walk in their statutes.", "All four columns agree.",
   ["Not Egypt's practices.", "Not Canaan's.", "Not their statutes."], "Israel was to reject both Egypt's and Canaan's ways.", "Behind and ahead: the land they left and the land they enter both have customs, and Israel is to belong to neither.", [AGREE], ['egypt', 'canaan'], "You shall not walk in their statutes."),
  '18:4': v("Israel does God's judgments and keeps his statutes, walking in them; I am YHWH your God.", "All four columns agree.",
   ["Do God's judgments.", "Keep his statutes.", "Walk in them."], "Israel was to walk in God's statutes instead.", "Not Canaan's statutes but God's; the alternative to the nations' customs is not freedom but a different walk.", [AGREE], ['yhwh-yahweh'], "You shall walk in My statutes."),
  '18:5': v("Keep God's statutes and judgments; the one who does them lives by them. I am YHWH.",
   "The Hebrew is spare; the Greek adds 'all' twice, 'and do them', and 'your God'. The Latin and King James follow the Hebrew.",
   ["Keep the statutes.", "The doer lives by them.", "I am YHWH."], "Doing the laws was the way of life.", "'Shall live by them': the law is offered as life, not as a cage; the one who does it is the one who lives. The verse will be quoted for centuries on what living by the law means.",
   [keeps("Greek 'all My ordinances and all My judgments, and do them … the Lord your God'."), between("The Latin and King James have the shorter form.")], ['yhwh-yahweh'], "The one who does them shall live by them."),
  '18:6': v("None of you approaches any close relative of his flesh to uncover nakedness. I am YHWH.", "All four columns agree; the Greek word for nakedness also carries shame.",
   ["No one approaches.", "Close relative of his flesh.", "To uncover nakedness."], "Sexual relations with close kin were forbidden.", "The heading of the list: 'flesh of his flesh' is too near; the euphemism 'uncover nakedness' will carry every verse that follows.", NAKED, ['yhwh-yahweh'], "None of you shall approach a close relative to uncover nakedness."),
  '18:7': v("Not the nakedness of your father or of your mother; she is your mother.", "All four columns agree; how the father phrase relates to the mother phrase is interpretive.",
   ["Not your father's nakedness.", "Not your mother's.", "She is your mother."], "The mother was the first named.", "The father's nakedness and the mother's are one; to lie with her is to uncover him. 'She is your mother' is the whole argument.", NAKED, [], "You shall not uncover your mother's nakedness."),
  '18:8': v("Not the nakedness of your father's wife; it is your father's nakedness.", "All four columns agree.",
   ["Not your father's wife.", "It is your father's nakedness.", "Though not your mother."], "The father's wife was forbidden as the father's own.", "A stepmother is not the mother, but she is the father's; the sin would be against him.", NAKED, [], "You shall not uncover your father's wife's nakedness."),
  '18:9': v("Not the nakedness of your sister, your father's or your mother's daughter, born at home or outside.", "All four columns agree.",
   ["Not your sister.", "Of father or mother.", "Born at home or outside."], "Sisters and half-sisters alike were forbidden.", "Half-sister, legitimate or not, raised in the house or elsewhere: the law closes every loophole a man might find in the word 'sister'.", NAKED, [], "You shall not uncover your sister's nakedness."),
  '18:10': v("Not the nakedness of your son's daughter or daughter's daughter, for theirs is your nakedness.", "All four columns agree.",
   ["Not your granddaughter.", "Son's or daughter's.", "Theirs is your nakedness."], "Granddaughters were forbidden as one's own flesh.", "'Theirs is your nakedness': the granddaughter is the man himself two generations on; the shame would be his own.", NAKED, [], "You shall not uncover your granddaughter's nakedness."),
  '18:11': v("Not the nakedness of your father's wife's daughter, begotten by your father; she is your sister.",
   "The Hebrew states paternity and stops; the Greek 'your sister by the same father' and repeats the prohibition. The Latin 'borne to your father'.",
   ["Father's wife's daughter.", "Begotten by your father.", "She is your sister."], "A half-sister by the father's wife was forbidden.", "The stepmother's daughter who is also the father's: 'she is your sister' settles it, whatever the household called her.",
   NAKED + [keeps("Greek 'she is your sister by the same father; you shall not uncover her nakedness'.")], [], "You shall not uncover your half-sister's nakedness."),
  '18:12': v("Not the nakedness of your father's sister; she is your father's close relative.", "All four columns agree.",
   ["Not your father's sister.", "His close relative.", "Flesh of his flesh."], "The paternal aunt was forbidden.", "The father's flesh is the son's flesh; his sister is kept out of reach.", NAKED, [], "You shall not uncover your father's sister's nakedness."),
  '18:13': v("Not the nakedness of your mother's sister; she is your mother's close relative.", "All four columns agree.",
   ["Not your mother's sister.", "Her close relative.", "Flesh of her flesh."], "The maternal aunt was forbidden.", "Both sides of the family: the mother's line is as near as the father's, in a world that often counted only the father's.", NAKED, [], "You shall not uncover your mother's sister's nakedness."),
  '18:14': v("Not the nakedness of your father's brother; do not approach his wife, she is your aunt.",
   "The Hebrew names her 'your aunt'; the Greek 'your relative' and 'go in to'; the Latin 'joined to you by marriage'.",
   ["Not your father's brother.", "Not his wife.", "She is your aunt."], "The uncle's wife was forbidden as an aunt.", "The uncle's nakedness is uncovered through his wife; a woman related only by marriage is still kin.",
   NAKED + [loses("Hebrew 'she is your aunt' is lost."), keeps("Greek 'you shall not go in to his wife; she is your relative'."), between("The Latin has 'joined to you by marriage'; the King James 'aunt'.")], [], "You shall not approach your uncle's wife."),
  '18:15': v("Not your daughter-in-law's nakedness; she is your son's wife.", "All four columns agree.",
   ["Not your daughter-in-law.", "Your son's wife.", "Her nakedness."], "The daughter-in-law was forbidden.", "She is the son's; to touch her is to strike the son, as the stepmother was the father's.", NAKED, [], "You shall not uncover your daughter-in-law's nakedness."),
  '18:16': v("Not the nakedness of your brother's wife; it is your brother's nakedness.", "All four columns agree; the relation to levirate marriage is interpretive.",
   ["Not your brother's wife.", "Your brother's nakedness.", "While he lives."], "The brother's wife was forbidden.", "The brother's wife is the brother's nakedness; Deuteronomy's levirate duty will stand as the exception when the brother is dead and childless.", NAKED, [], "You shall not uncover your brother's wife's nakedness."),
  '18:17': v("Not a woman and her daughter; nor her granddaughter; they are close relatives. It is a wicked scheme.",
   "The Hebrew 'close relatives … wicked scheme' (zimmah); the Greek 'your relatives … impiety'; the Latin 'incestuous'.",
   ["Not a woman and her daughter.", "Nor her granddaughter.", "A wicked scheme."], "A woman's descendants were forbidden with her.", "Mother and daughter, or a wife's granddaughter: the law calls this not weakness but 'scheme', a plan to use a family as a harem.",
   NAKED + [loses("Hebrew 'wicked scheme' is lost."), keeps("Greek 'they are your relatives; it is an act of impiety'."), between("The Latin has 'incest'; the King James 'wickedness'.")], [], "You shall not take a woman and her daughter."),
  '18:18': v("Do not take a woman in addition to her sister as a rival, to uncover her nakedness while the first lives.", "All four columns agree.",
   ["Not a woman and her sister.", "As a rival.", "While she lives."], "Two sisters at once were forbidden.", "'As a rival': Jacob's two wives are in view; the law forbids setting sisters against each other in one tent.", NAKED, ['jacob'], "You shall not take two sisters as rivals."),
  '18:19': v("Do not approach a woman in her menstrual uncleanness to uncover her nakedness.", "All four columns agree; the Hebrew 'separation' is rendered menstrual by context.",
   ["Not in her uncleanness.", "Separation.", "To uncover nakedness."], "Relations during menstruation were forbidden.", "From kinship to time: there is a season in which even a wife is set apart, and the man waits.",
   [keeps("Greek 'a woman in separation for her uncleanness'."), between("The Latin and King James have 'put apart for her uncleanness'.")], [], "You shall not approach a woman in her uncleanness."),
  '18:20': v("Do not lie with your neighbour's wife to emit semen and be defiled through her.", "All four columns agree.",
   ["Not your neighbour's wife.", "To emit semen.", "Defiled through her."], "Adultery was forbidden as defilement.", "Adultery is named as defilement before it is named as theft; the man is made unclean 'through her'.", [AGREE], [], "You shall not lie with your neighbour's wife."),
  '18:21': v("Do not give any of your offspring to be passed over to Molech, nor profane the name of your God. I am YHWH.",
   "The Hebrew names Molech and 'passed over'; the Greek 'to serve a ruler' and 'the holy name'. The Latin names Moloch. Fire is not stated in either text.",
   ["Not your offspring.", "Passed over to Molech.", "Not profaning God's name."], "Giving children to Molech was forbidden.", "In the midst of the sexual laws, a child given to a god: the Hebrew names Molech; the Greek read the word as 'king' and saw a ruler's service, and the sin's shape changes. Both end at the name of God.",
   [loses("Hebrew 'to be passed over to Molech' and 'the name of your God' are lost."), keeps("Greek 'to serve a ruler … the holy name'."), between("The Latin names Moloch; the King James 'pass through the fire to Molech'.")], ['gods', 'divine-names'], "You shall not give your offspring to Molech."),
  '18:22': v("Do not lie with a male as one lies with a woman; it is an abomination.", "All four columns agree; neither uses an age-specific word.",
   ["Not with a male.", "As with a woman.", "An abomination."], "Male intercourse was called abomination.", "'Abomination' (to'evah), the word used of detestable worship, is set here on an act; the law's later readers will dispute its reach, but the columns agree on the wording.", [AGREE], [], "You shall not lie with a male as with a woman."),
  '18:23': v("Do not lie with any animal and be defiled; a woman does not stand before an animal to mate; it is a perversion.",
   "The Hebrew 'animal … perversion' (tevel); the Greek 'four-footed animal … for insemination … detestable'. The Latin 'wicked act'.",
   ["Not with an animal.", "Nor a woman before one.", "A perversion."], "Bestiality was forbidden for both sexes.", "The word is 'confusion', the mixing of kinds; the law treats the crossing of species as a scrambling of the created order.",
   [loses("Hebrew 'perversion' (confusion of kinds) is lost."), keeps("Greek 'any four-footed animal for insemination … to be mounted; it is detestable'."), between("The Latin has 'wicked act'; the King James 'confusion'.")], ['creator'], "You shall not lie with any animal."),
  '18:24': v("Do not defile yourselves by any of these, for by all these the nations God drives out before you were defiled.", "All four columns agree; the Greek makes the causal clause explicit.",
   ["Not defiling yourselves.", "By these things.", "The nations were defiled."], "The nations' defilement explained their expulsion.", "The list is closed and the reason given: the land is being emptied of nations who did these things, and Israel enters on the same terms.", [AGREE], ['canaan']),
  '18:25': v("The land became defiled, and God visited its iniquity on it, and the land vomited out its inhabitants.",
   "The Hebrew has God visit the land's iniquity and the land vomit its people out; the Greek 'I repaid them for wrongdoing … the land became indignant with those settled on it'. The Latin future tense.",
   ["The land defiled.", "Iniquity visited.", "The land vomited them out."], "The land itself expelled its defilers.", "The land is a body that sickens and vomits; the Hebrew's image is physical and the Greek softened it to indignation, but in both the ground refuses its people.",
   VOMIT + [loses("Hebrew 'I visited its iniquity upon it' is lost."), keeps("Greek 'I repaid them for wrongdoing because of it'.")], ['canaan']),
  '18:26': v("Israel keeps God's statutes and judgments and does none of these abominations, native or resident foreigner.", "All four columns agree; the Greek adds 'all' twice and 'commands'.",
   ["Keep the statutes.", "None of these abominations.", "Native or foreigner."], "The laws bound natives and foreigners alike.", "The foreigner in Israel's land is under Israel's law here as at the altar; the land does not ask who you are.",
   [keeps("Greek 'all My statutes and all My commands … the resident foreigner who has joined himself among you'."), between("The Latin and King James have the shorter form.")], [], "You shall do none of these abominations."),
  '18:27': v("For the people of the land before you did all these abominations, and the land became defiled.", "All four columns agree.",
   ["The former people.", "Did these abominations.", "The land defiled."], "The former inhabitants had defiled the land.", "Said again: the Canaanites are not being expelled for being Canaanites but for what the list describes.", [AGREE], ['canaan']),
  '18:28': v("So that the land does not vomit you out when you defile it, as it vomited out the nation before you.",
   "The Hebrew 'vomit … nation' singular; the Greek 'indignant … nations' plural. The Latin and King James follow the Hebrew.",
   ["Lest the land vomit you.", "When you defile it.", "As the nation before."], "Israel risked the same expulsion.", "The warning turns on Israel: the same ground that spat out Canaan will spit out Israel, and the prophets will say it did.",
   VOMIT + [loses("Hebrew 'the nation' singular is lost."), keeps("Greek 'the nations before you'.")]),
  '18:29': v("Whoever does any of these abominations, the persons who do them are cut off from their people.", "All four columns agree; 'destroyed' in Greek.",
   ["Whoever does them.", "Any abomination.", "Cut off."], "Each offender was cut off.", "Not the land's vomiting only but the community's own excision; the people must do first what the land would otherwise do to them all.", CUTOFF),
  '18:30': v("Keep God's charge, doing none of the abominable practices done before you, and do not defile yourselves. I am YHWH your God.", "All four columns agree; the Greek links the clauses with 'so that'.",
   ["Keep God's charge.", "None of the former practices.", "I am YHWH your God."], "The chapter closed as it opened.", "'I am YHWH your God' at the end as at the start; the whole list is bracketed by the name of the one who gives both the land and the body.",
   [keeps("Greek 'all the abominable practices'."), between("The Latin and King James have separate imperatives.")], ['yhwh-yahweh'], "Keep My charge."),
 },
}
