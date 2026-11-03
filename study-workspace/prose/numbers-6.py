K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
NAZIR = [loses("Hebrew 'Nazirite … separation' (nazir, nezer) is lost."), keeps("Greek 'vow of purification' or 'consecration'."), between("The Latin has 'sanctified'; the King James 'Nazarite … separation'.")]
PEACE = [loses("Hebrew 'well-being' is lost."), keeps("Greek 'deliverance'."), between("The Latin and King James have 'peace offering'.")]
GRAIN = [loses("Hebrew 'grain offering' is lost."), keeps("Greek 'sacrifice'."), between("The Latin and King James have 'meat offering' or 'oblation'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 6,
 'chapterNote': "The Nazirite vow and the priestly blessing. A man or woman separated to YHWH abstains from everything of the vine, lets no razor touch the head, and does not approach the dead even for parents or siblings, because the consecration of God is on the head; if a death defiles the vow, the head is shaved on the seventh day, two birds and a lamb are offered, and the days begin again. At the end the Nazirite brings a lamb, a ewe, a ram and a basket of unleavened bread, shaves the head at the tent door and burns the hair under the peace offering, the priest waves the shoulder and bread, and the Nazirite may drink wine. Then Aaron's blessing: YHWH bless and keep you, make his face shine and be gracious, lift his face and give you peace; so they set the Name on Israel. The Greek has 'vow of purification/consecration' for the Hebrew's Nazirite terms throughout, 'enter where any dead person is' (6:6), 'whereon he was consecrated' for 'dedicate the days' (6:12), the vower presenting an offering rather than being brought (6:13), 'deliverance' for 'well-being', 'sacrifice' for 'grain offering', 'foreleg' for 'thigh' and 'present' for 'wave' (6:19–20), 'have mercy' for 'be gracious' (6:25), and places the Hebrew's 6:27 ('they shall put My name upon Israel and I will bless them') before the blessing at 6:23, adding 'I, the Lord'; the site's alignment therefore has twenty-six verses for this chapter.",
 'verses': {
  '6:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the Nazirite."],
   "YHWH spoke on the Nazirite vow.", "After the law for the suspected wife, a law for the voluntarily holy; the camp has room for both.", FORMULA, ['yhwh-yahweh', 'moses']),
  '6:2': v("When a man or woman makes a special vow, a Nazirite vow of separation to YHWH,", "The Hebrew names the Nazirite; the Greek 'vow of consecration … to be set apart' or 'purify oneself'. Both include women.",
   ["Man or woman.", "A special vow.", "Separation to YHWH."], "Anyone could vow separation.", "A man or a woman: the one holiness in the Torah a layperson may take up at will, and women are named first among those who may.", NAZIR, ['yhwh-yahweh']),
  '6:3': v("They abstain from wine and strong drink, drink no wine or strong-drink vinegar or grape infusion, and eat no fresh or dried grapes.", "All four columns agree; the Greek repeats the wine prohibition; the Latin 'everything that intoxicates'.",
   ["No wine or strong drink.", "No vinegar or infusion.", "No grapes."], "The vine was wholly forbidden.", "Not only drunkenness but the grape itself, down to the raisin; the vow refuses the whole plant, not the effect.",
   [keeps("Greek 'he shall be purified from wine'."), between("The Latin adds 'everything that can intoxicate'.")], ['grapevine'], "They shall abstain from wine and strong drink."),
  '6:4': v("All the days of separation they eat nothing from the grapevine, from seed to skin.", "All four columns agree; the Greek 'from pressed skins to the seed'.",
   ["All the days.", "Nothing from the vine.", "Seed to skin."], "The vine was forbidden entire.", "'From seed to skin': a merism for the whole fruit; the Nazirite's mouth is closed to the vine as the priest's is in the tent.", NAZIR, ['grapevine', 'term-merism']),
  '6:5': v("All the days of the vow no razor passes over the head; until the days are fulfilled they are holy, letting the locks grow.", "All four columns agree; 'purification' in Greek.",
   ["No razor.", "Until fulfilled.", "Hair grows long."], "The hair was left to grow.", "The hair is the vow made visible: Samson's strength and Absalom's beauty are both Nazirite hair in the story's memory.", NAZIR, [], "No razor shall pass over their head."),
  '6:6': v("All the days of separation to YHWH they do not approach a dead person.", "All four columns agree; 'enter where any dead person is' in Greek.",
   ["All the days.", "Not approaching.", "A dead person."], "The Nazirite avoided the dead.", "The high priest's rule laid on a layman for a season; the vow borrows the strictest holiness there is.",
   NAZIR + [keeps("Greek 'he shall not enter where any dead person is'.")], ['yhwh-yahweh']),
  '6:7': v("Not for father, mother, brother or sister when they die, because the consecration of their God is on their head.", "All four columns agree; 'the vow of his God' in Greek.",
   ["Not for parents.", "Not for siblings.", "Consecration on the head."], "Even family did not excuse defilement.", "Not even his mother's funeral; the ordinary priest may mourn her, but the Nazirite has taken the high priest's rule, and 'on his head' is where it sits.",
   [loses("Hebrew 'the consecration (nezer) of their God' is lost."), keeps("Greek 'the vow of his God is upon him'."), between("The Latin and King James have 'consecration'.")]),
  '6:8': v("All the days of separation they are holy to YHWH.", "All four columns agree.", ["All the days.", "Holy.", "To YHWH."],
   "The Nazirite was holy to God.", "Holy for a term: the vow has a calendar, and the holiness ends on a date.", NAZIR, ['yhwh-yahweh']),
  '6:9': v("If someone dies very suddenly beside them and defiles the consecrated head, they shave it on the day of cleansing, the seventh day.", "All four columns agree.",
   ["Sudden death beside them.", "The head defiled.", "Shaved on the seventh day."], "Accidental defilement reset the vow.", "A stranger falls dead beside him and months of hair come off; the vow is undone by an accident, and the law has a remedy ready.", [AGREE]),
  '6:10': v("On the eighth day they bring two turtledoves or two young pigeons to the priest at the Tent of Meeting's entrance.", "All four columns agree.",
   ["The eighth day.", "Two turtledoves or pigeons.", "To the priest."], "Birds were offered on the eighth day.", "The poor man's pair of birds, as for a new mother or a cleansed leper; the Nazirite's accident is priced low.", TENT, ['high-priest']),
  '6:11': v("The priest offers one as a sin offering and one as a burnt offering, atones for their sin regarding the dead, and they consecrate the head that day.", "All four columns agree; the Latin 'pray', the Greek 'propitiate'.",
   ["Sin and burnt offering.", "Atonement for the dead.", "Head reconsecrated."], "Atonement renewed the vow.", "'Sin in connection with the dead': proximity to a corpse is a sin without a sinner, and the altar covers it anyway.",
   [between("The Latin has the priest 'pray'; the Greek 'make propitiation'; the King James 'make an atonement'.")], ['high-priest']),
  '6:12': v("They dedicate to YHWH the days of separation and bring a year-old lamb as a guilt offering; the former days fall away, for the separation was defiled.",
   "The Hebrew commands renewed dedication of the days; the Greek 'whereon he was consecrated … for the days of the vow'.",
   ["Days rededicated.", "A lamb for guilt.", "Former days void."], "The count began again.", "'The former days shall fall away': every day of the vow before the accident is lost, and he starts from zero. A hard law, honestly stated.",
   NAZIR + [loses("Hebrew 'they shall dedicate to YHWH the days of their separation' is lost."), keeps("Greek 'whereon he was consecrated unto the Lord for the days of the vow'.")], ['yhwh-yahweh']),
  '6:13': v("This is the instruction for the Nazirite: on the day the separation is fulfilled, they are brought to the Tent of Meeting's entrance.", "The Hebrew 'bring him' (sometimes reflexive); the Greek 'he shall present his offering'.",
   ["The law of the Nazirite.", "The days fulfilled.", "To the tent's entrance."], "The vow ended at the tent.", "'Bring him': the Hebrew does not say who brings the Nazirite, as if he were himself the offering carried to the door.",
   TENT + NAZIR + [loses("Hebrew 'the person shall be brought' is lost."), keeps("Greek 'he shall present his offering at the doors'.")]),
  '6:14': v("They present to YHWH an unblemished year-old male lamb for a burnt offering, a year-old ewe for a sin offering, and an unblemished ram for well-being.", "All four columns agree on the animals; 'deliverance' in Greek.",
   ["A male lamb.", "A ewe lamb.", "A ram."], "Three animals closed the vow.", "Three animals to end a vow of abstinence: the Nazirite who gave up grapes gives a flock at the finish.", PEACE, ['yhwh-yahweh']),
  '6:15': v("A basket of unleavened bread of fine flour, cakes with oil and wafers spread with oil, with grain and drink offerings.", "All four columns agree; 'sacrifice' and singular 'libation' in Greek.",
   ["A basket of unleavened bread.", "Cakes and wafers with oil.", "Grain and drink offerings."], "Bread accompanied the animals.", "Bread and a drink offering, wine among them: wine is poured at the vow's end before the Nazirite may taste it.", GRAIN, ['unleavened-bread']),
  '6:16': v("The priest presents them before YHWH and offers the sin offering and burnt offering.", "All four columns agree.",
   ["The priest presents them.", "The sin offering.", "The burnt offering."], "The priest offered the first two.", "Sin first, then the whole gift; the order of every rite in the book.", [AGREE], ['high-priest', 'yhwh-yahweh']),
  '6:17': v("He offers the ram as a well-being sacrifice to YHWH with the basket of bread; the priest offers its grain and drink offering.", "All four columns agree in substance.",
   ["The ram for well-being.", "With the bread.", "Grain and drink."], "The peace offering came last.", "The ram and the bread are the feast; the vow ends in a meal shared with God.", PEACE + GRAIN, ['yhwh-yahweh']),
  '6:18': v("The Nazirite shaves the consecrated head at the Tent of Meeting's entrance, takes the hair and puts it on the fire under the well-being sacrifice.", "All four columns agree; the Greek omits the separate 'take'.",
   ["The head shaved.", "At the entrance.", "Hair burned under the sacrifice."], "The hair was burned with the offering.", "The hair goes into the fire under the ram: the thing that was holy all those months is given to God along with the meat. Nothing of the vow is kept.",
   TENT + PEACE + NAZIR, [], "The Nazirite shall shave the consecrated head and burn the hair."),
  '6:19': v("The priest takes the boiled shoulder of the ram, one unleavened cake and one wafer, and puts them on the Nazirite's palms after the hair is shaved.", "All four columns agree; 'foreleg' in Greek.",
   ["The boiled shoulder.", "A cake and a wafer.", "On the palms."], "The Nazirite held the priest's portion.", "The shorn man stands with the shoulder and bread in his hands, as the suspected wife stood with the barley; the hands hold what the mouth is about to be freed for.",
   [keeps("Greek 'the boiled foreleg'."), between("The Latin and King James have 'shoulder'.")], ['high-priest']),
  '6:20': v("The priest waves them as a wave offering before YHWH; they are holy for the priest with the breast and thigh. Afterward the Nazirite may drink wine.", "The Hebrew 'wave … thigh'; the Greek 'present … foreleg'.",
   ["Waved before YHWH.", "The priest's portion.", "Then wine."], "The vow ended with wine.", "'Afterward the Nazirite may drink wine': the first cup after the vow is the law's own permission, and the chapter ends the abstinence it began.",
   [loses("Hebrew 'wave … the thigh of the contribution' is lost."), keeps("Greek 'bring them as a presentation … the foreleg of the portion set apart'."), between("The Latin and King James have 'wave' and 'shoulder' or 'thigh'.")], ['high-priest', 'grapevine']),
  '6:21': v("This is the instruction for the Nazirite who vows an offering for the separation, besides what the hand can afford; according to the vow, so they do.", "All four columns agree in substance; the Greek compresses.",
   ["The law of the Nazirite.", "Besides what he can afford.", "According to the vow."], "The vow could exceed the minimum.", "The minimum is fixed and the maximum is the vower's: what his hand finds he may add, and what he vowed he must do.",
   NAZIR + [keeps("Greek 'according to the extent of his vow which he vows under the law of consecration'.")]),
  '6:22': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the blessing."],
   "YHWH spoke on the blessing.", "A short speech after the vow; the priests are given words, not animals.", FORMULA, ['yhwh-yahweh', 'moses']),
  '6:23': v("Speak to Aaron and his sons: thus you bless Israel, saying to them. (They shall put my name on Israel, and I will bless them.)",
   "The Hebrew's 6:27 is placed here by the Greek, before the blessing, with 'I, the Lord'; the site aligns it under 6:23 so the chapter has twenty-six verses.",
   ["Aaron and his sons.", "Thus you bless.", "God's name on Israel."], "Priests were told how to bless.", "'They shall put My name upon them': the blessing is not the priests' good wishes but God's name laid on the people; the Greek says so before the words, the Hebrew after.",
   [loses("Hebrew's order (name-promise after the blessing, 6:27) is lost."), keeps("Greek 'and they shall put My name upon the sons of Israel, and I, the Lord, will bless them' before the blessing."), between("The Latin has 'invoke My name'; the King James follows the Hebrew order.")], ['high-priest', 'divine-names'], "Thus you shall bless the sons of Israel."),
  '6:24': v("May YHWH bless you and keep you.", "All four columns agree; the 'you' is singular.",
   ["YHWH bless you.", "And keep you.", "Singular."], "The blessing opened with keeping.", "Three lines, growing longer: three words in Hebrew, then five, then seven. 'You' is singular; the whole people is blessed one at a time.", [AGREE], ['yhwh-yahweh']),
  '6:25': v("May YHWH make his face shine on you and be gracious to you.", "The Hebrew 'be gracious'; the Greek 'have mercy'; the Latin 'show his face'.",
   ["His face shine.", "Upon you.", "Be gracious."], "The second line asked for grace.", "A shining face is a smile; the blessing asks God to look at Israel and be glad.",
   [loses("Hebrew 'be gracious' is lost."), keeps("Greek 'have mercy upon you'."), between("The Latin has 'show His face'; the King James 'be gracious'.")], ['term-grace-charis', 'term-favor']),
  '6:26': v("May YHWH lift his face toward you and set peace for you.", "All four columns agree; 'give peace' in Greek.",
   ["His face lifted.", "Toward you.", "Peace."], "The blessing ended in peace.", "The last word is shalom, and the sixth of seven; the name YHWH three times, once in each line, is the name set on Israel.",
   [keeps("Greek 'give you peace'."), between("The Latin and King James have 'give thee peace'.")], ['yhwh-shalom', 'yhwh-yahweh']),
 },
}
