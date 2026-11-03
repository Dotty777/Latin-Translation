K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
BLOOD = [loses("Hebrew 'their blood is upon them' is lost."), keeps("Greek 'they are guilty'."), between("The Latin and King James keep the blood formula.")]
MOLECH = [loses("Hebrew 'Molech' is lost."), keeps("Greek 'a ruler' (archon)."), between("The Latin names Moloch; the King James 'Molech'.")]
CUTOFF = [loses("Hebrew 'cut off' is lost in form."), keeps("Greek 'destroy'."), between("The Latin and King James have 'cut off' or 'kill'.")]
VOMIT = [loses("Hebrew 'vomit you out' is lost."), keeps("Greek 'be indignant with you'."), between("The Latin and King James keep the vomiting image.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'leviticus', 'chapter': 20,
 'chapterNote': "The penalties for the offences of chapter 18 and the practices of chapter 19: giving offspring to Molech is stoned, and if the people look away God himself cuts off the man, his family and his followers; mediums are cut off; 'consecrate yourselves and be holy'; cursing parents, adultery, the father's wife, the daughter-in-law, male intercourse, a woman and her mother (burned), bestiality (the animal killed too), the sister, the menstruating woman, aunts, the uncle's wife and the brother's wife (childless), and finally the medium or spirit-knower stoned. Between the lists the land that vomits out the defiled, the nation whose statutes God abhorred, and the land of milk and honey given to a people separated from the nations, who must separate clean from unclean as God separated them. The Greek has 'a ruler' for Molech throughout (20:2–5) and 'the name of those consecrated to Me' for 'My holy name' (20:3), 'they are guilty' for the Hebrew's 'their blood is upon them' (20:9, 11–13, 16, 27), 'destroy' for 'cut off', 'they shall bear their sin' for 'he shall bear his guilt' (20:17), 'female relative' for 'aunt' and no 'bear their sin' (20:20), 'die childless' for 'be childless' (20:21), 'indignant' for 'vomit' (20:22), plural 'nations' (20:23) and 'all the nations' (20:24, 26), and omits 'consecrate yourselves' at 20:7. The Latin follows the Hebrew at Molech and the blood formula.",
 'verses': {
  '20:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On penalties."],
   "YHWH spoke on the penalties.", "Chapter 18 said what not to do; this chapter says what happens; the law's two halves.", FORMULA, ['yhwh-yahweh', 'moses']),
  '20:2': v("Any Israelite or resident foreigner who gives offspring to Molech is put to death; the people stone him.",
   "The Hebrew names Molech; the Greek 'a ruler' (archon), which does not identify every ruler with Molech. The Latin names Moloch.",
   ["Israelite or foreigner.", "Offspring to Molech.", "Stoned by the people."], "Molech worship was stoned.", "The first penalty is for the worst gift, a child to a god; the whole people throws the stones, since the whole land was defiled.",
   MOLECH, ['gods'], "Whoever gives his offspring to Molech shall be put to death."),
  '20:3': v("God sets his face against him and cuts him off, because he gave offspring to Molech, defiling the sanctuary and profaning God's holy name.",
   "The Hebrew 'My sanctuary … My holy name'; the Greek 'My holy things … the name of those consecrated to Me', shifting the object of profanation.",
   ["God's face against him.", "Cut off.", "Sanctuary defiled, name profaned."], "Molech worship defiled sanctuary and name.", "Giving a child away in a field somewhere defiles the sanctuary in the camp; the law joins the two places by God's name, which is dirtied wherever Israel is.",
   MOLECH + CUTOFF + [loses("Hebrew 'profaning My holy name' is lost."), keeps("Greek 'profaning the name of those consecrated to Me'.")], ['tabernacle', 'divine-names']),
  '20:4': v("If the people close their eyes to that man and do not kill him,", "All four columns agree in the people's failure; 'ruler' in Greek; the Latin 'negligent and despising'.",
   ["The people look away.", "From the Molech-giver.", "And do not kill him."], "The community might fail to act.", "The law foresees the people's silence; a neighbour's child sacrificed and no one willing to lift a stone.", MOLECH),
  '20:5': v("God sets his face against the man and his family, cutting off him and all who follow him in prostitution after Molech.",
   "The Hebrew 'all who prostitute themselves after him after Molech'; the Greek 'all who agree with him … after rulers' plural. 'Family' / 'kin'.",
   ["Against the man and his family.", "Cut off.", "And his followers."], "God himself punished when the people would not.", "When the people will not judge, God does, and more widely: the family and the followers go with him. The community's mercy becomes a larger judgment.",
   MOLECH + CUTOFF + [keeps("Greek 'all who agree with him … after rulers'.")], ['gods']),
  '20:6': v("The person who turns to mediums and spirit-knowers, prostituting himself after them, God sets his face against and cuts off.", "All four columns agree; 'enchanters … destroy' in Greek; the Latin 'kill'.",
   ["Turning to mediums.", "Prostituting after them.", "Cut off by God."], "Seeking mediums was cut off.", "The same word, 'prostituting', for Molech and for the medium; consulting the dead is a kind of adultery against God.",
   CUTOFF + [keeps("Greek 'spirit mediums or enchanters'.")], ['evil-spirits-and-adversaries']),
  '20:7': v("Consecrate yourselves and be holy, for I am YHWH your God.", "The Hebrew 'consecrate yourselves and be holy … I am YHWH your God'; the Greek omits 'consecrate yourselves' and adds 'am holy'.",
   ["Consecrate yourselves.", "Be holy.", "I am YHWH your God."], "Holiness was commanded in the midst of penalties.", "Between the stoning and the death lists, the call to be holy; the penalties are the shape of the holiness refused.",
   [loses("Hebrew 'consecrate yourselves' is lost."), keeps("Greek 'you shall be holy, for I, the Lord your God, am holy'."), between("The Latin and King James have 'sanctify yourselves'.")], ['yhwh-yahweh', 'holy-one-israel'], "Consecrate yourselves and be holy."),
  '20:8': v("Keep God's statutes and do them. I am YHWH who sanctifies you.", "All four columns agree.",
   ["Keep the statutes.", "Do them.", "YHWH who sanctifies."], "God sanctified the people who kept his law.", "'I am YHWH who sanctifies you': the holiness commanded in 20:7 is given here; Israel keeps the law and God does the making-holy.", [AGREE], ['yhwh-who-sanctifies', 'yhwh-yahweh'], "Keep My statutes and do them."),
  '20:9': v("Whoever curses father or mother is put to death; he has cursed them; his blood is upon him.", "The Hebrew 'curses … his blood is upon him'; the Greek 'speaks evil of … he shall be guilty'.",
   ["Cursing father or mother.", "Put to death.", "His blood upon him."], "Cursing parents was capital.", "The parent curse comes first among the family crimes; 'his blood is upon him' means the executioner bears no guilt, the dead man carries his own.",
   BLOOD + [keeps("Greek 'speaks evil of his father or his mother'.")], [], "Whoever curses his father or mother shall be put to death."),
  '20:10': v("A man who commits adultery with another's wife, his neighbour's wife: both adulterer and adulteress are put to death.", "All four columns agree; the Greek 'or'.",
   ["Adultery.", "With a neighbour's wife.", "Both die."], "Adultery was capital for both.", "Both die; the law does not punish the woman alone, as the nations did, nor spare the man of standing.", [AGREE], [], "The adulterer and the adulteress shall be put to death."),
  '20:11': v("A man who lies with his father's wife has uncovered his father's nakedness; both die; their blood is upon them.", "All four columns agree; 'guilty' in Greek.",
   ["Father's wife.", "Father's nakedness uncovered.", "Both die."], "The father's wife brought death to both.", "Reuben's sin with Bilhah, now with its penalty; the father's bed is the father's honour.", BLOOD),
  '20:12': v("A man who lies with his daughter-in-law: both die; they have committed a perversion; their blood is upon them.", "The Hebrew 'perversion' (tevel); the Greek 'acted impiously … guilty'.",
   ["Daughter-in-law.", "A perversion.", "Both die."], "The daughter-in-law brought death to both.", "'Confusion', the word used of bestiality in 18:23: generations are scrambled when a father takes his son's wife. Judah and Tamar hang over the verse.",
   BLOOD + [loses("Hebrew 'perversion' is lost."), keeps("Greek 'they have acted impiously'.")]),
  '20:13': v("A man who lies with a male as with a woman: both have done an abomination; they die; their blood is upon them.", "All four columns agree; 'guilty' in Greek.",
   ["Male with male.", "An abomination.", "Both die."], "Male intercourse was capital for both.", "The prohibition of 18:22 with its penalty; both partners alike, as in adultery.", BLOOD),
  '20:14': v("A man who takes a woman and her mother: a wicked scheme; he and they are burned, so there is no wickedness among you.", "All four columns agree; 'lawless deed … lawlessness' in Greek.",
   ["A woman and her mother.", "A wicked scheme.", "Burned with fire."], "The mother–daughter case was burned.", "Fire, the harshest death in the chapter, for the 'scheme' of 18:17; the household used as a harem is burned down to the ground.",
   [keeps("Greek 'a lawless deed … no lawlessness among you'."), between("The Latin and King James have 'wickedness'.")]),
  '20:15': v("A man who lies with an animal is put to death, and you kill the animal.", "All four columns agree; 'four-footed' in Greek.",
   ["A man with an animal.", "He dies.", "The animal killed."], "Bestiality killed man and animal.", "The animal dies too, though it cannot sin; the act has made it unfit to live among people.",
   [keeps("Greek 'a four-footed animal'."), between("The Latin has 'beast'; the King James 'beast'.")]),
  '20:16': v("A woman who approaches an animal to mate: kill the woman and the animal; their blood is upon them.", "All four columns agree; 'to be mounted … guilty' in Greek.",
   ["A woman with an animal.", "Both killed.", "Their blood upon them."], "The woman's case matched the man's.", "The same for the woman as for the man; 'their blood' is said even of the beast.", BLOOD),
  '20:17': v("A man who takes his sister, father's or mother's daughter, and they see each other's nakedness: a disgrace; cut off before their people; he bears his guilt.",
   "The Hebrew 'he shall bear his guilt'; the Greek 'they shall bear their sin' and 'destroyed'. 'Disgrace' / 'reproach'.",
   ["A sister.", "A disgrace.", "Cut off; he bears guilt."], "Incest with a sister was cut off.", "Not death but excision, and the guilt laid on him in the Hebrew, on both in the Greek; Abraham's marriage to a half-sister is left behind.",
   CUTOFF + [loses("Hebrew 'he shall bear his guilt' is lost."), keeps("Greek 'they shall bear their sin'.")], ['abraham']),
  '20:18': v("A man who lies with a menstruating woman has exposed her fountain, and she the source of her blood; both cut off.", "All four columns agree; 'flow … destroyed' in Greek.",
   ["During menstruation.", "Her fountain exposed.", "Both cut off."], "Menstrual intercourse was cut off.", "Both are cut off, she as well as he; the act is consensual and the penalty shared.", CUTOFF + [keeps("Greek 'the flow of her blood'.")]),
  '20:19': v("Do not uncover the nakedness of your mother's or father's sister; one who does exposes his close kin; they bear their guilt.", "The Hebrew mother's sister first; the Greek reverses. Both end plural.",
   ["Mother's or father's sister.", "Close kin exposed.", "They bear guilt."], "Aunts carried guilt without a stated death.", "No death and no cutting off, only 'they bear their guilt'; the penalty is left to God.",
   [loses("Hebrew order 'mother's sister or father's sister' is lost."), keeps("Greek 'father's sister or mother's sister … his own kinship'.")]),
  '20:20': v("A man who lies with his aunt has uncovered his uncle's nakedness; they bear their sin; they die childless.",
   "The Hebrew 'his aunt … his uncle's nakedness … bear their sin'; the Greek 'his female relative … his kinship' and omits the sin clause.",
   ["The uncle's wife.", "Uncle's nakedness.", "Die childless."], "The uncle's wife brought childlessness.", "Childless: the punishment fits the crime, for a union that confuses the family is denied a family.",
   [loses("Hebrew 'his aunt … his uncle's nakedness … they shall bear their sin' are lost."), keeps("Greek 'his female relative … the nakedness of his kinship'."), between("The Latin specifies the uncle's wife and both bearing sin.")]),
  '20:21': v("A man who takes his brother's wife: an impurity; he has uncovered his brother's nakedness; they are childless.", "The Hebrew 'be childless'; the Greek 'die childless'. 'Impurity' / 'uncleanness'; the Latin 'unlawful'.",
   ["The brother's wife.", "An impurity.", "Childless."], "The brother's wife brought childlessness.", "'Childless', not 'die childless' as in 20:20: the Hebrew is gentler here, and the levirate exception sits behind the verse.",
   [loses("Hebrew 'they shall be childless' is lost."), keeps("Greek 'they shall die childless … an uncleanness'."), between("The Latin has 'unlawful'; the King James 'an unclean thing'.")]),
  '20:22': v("Keep all God's statutes and judgments so the land to which he brings you does not vomit you out.", "The Hebrew 'vomit'; the Greek 'be indignant'. The Latin and King James follow the Hebrew.",
   ["Keep all the statutes.", "The land you enter.", "Lest it vomit you."], "Obedience kept Israel in the land.", "The land's stomach again; the whole penalty code is finally about staying in the land.", VOMIT, ['canaan'], "Keep all My statutes and judgments."),
  '20:23': v("Do not walk in the statutes of the nation God drives out, for they did all these things and he abhorred them.", "The Hebrew 'nation' singular, 'before you'; the Greek 'nations' plural, 'from you'.",
   ["Not the nation's statutes.", "They did these things.", "God abhorred them."], "The nations were abhorred for these acts.", "'I abhorred them': the chapter's list is what God found loathsome in Canaan; Israel was not chosen to do the same in the same place.",
   [loses("Hebrew 'the nation' singular is lost."), keeps("Greek 'the nations that I am driving away from you'.")], ['canaan']),
  '20:24': v("God said: you shall inherit their land, a land flowing with milk and honey. I am YHWH your God who separated you from the peoples.", "The Hebrew prospective; the Greek imperative 'inherit' and 'all the nations'.",
   ["Inherit their land.", "Milk and honey.", "Separated from the peoples."], "The land was promised to a separated people.", "Milk and honey in a chapter of stonings; the gift and the terms are one speech.",
   [keeps("Greek 'Inherit their land … from all the nations'."), between("The Latin has 'other peoples'; the King James 'other people'.")], ['canaan', 'yhwh-yahweh']),
  '20:25': v("Distinguish clean from unclean animal and bird; do not make yourselves detestable through what God set apart as unclean.", "All four columns agree; the Greek reverses the bird order and uses plurals.",
   ["Clean from unclean.", "Animal and bird.", "Set apart as unclean."], "Israel separated creatures as God separated Israel.", "Separated people, separated food: the kitchen is where Israel practises daily the distinction God made in choosing them.", [AGREE], [], "Distinguish between the clean and the unclean."),
  '20:26': v("You shall be holy to me, for I, YHWH, am holy; I separated you from the peoples to be mine.", "All four columns agree; the Greek 'your God' and 'all the nations'.",
   ["Holy to me.", "For I am holy.", "Separated to be mine."], "Holiness meant belonging to God.", "'To be Mine': the end of separation is possession, God's own people, and holiness is the family resemblance.",
   [keeps("Greek 'the Lord your God … from all the nations'."), between("The Latin and King James follow the Hebrew.")], ['yhwh-yahweh', 'holy-one-israel'], "You shall be holy to Me."),
  '20:27': v("A man or woman who is a medium or spirit-knower is put to death; stoned; their blood is upon them.", "All four columns agree; the Greek 'both … enchanter … guilty'.",
   ["Medium or spirit-knower.", "Man or woman.", "Stoned."], "Mediums themselves were stoned.", "The chapter began with the client of the medium cut off (20:6) and ends with the medium stoned; the dead are not to be consulted, from either side.",
   BLOOD + [keeps("Greek 'spirit-medium or an enchanter, both shall surely be put to death'.")], ['evil-spirits-and-adversaries'], "A medium shall be put to death."),
 },
}
