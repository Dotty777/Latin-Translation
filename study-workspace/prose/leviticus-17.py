K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
CUTOFF = [loses("Hebrew 'cut off from his people' is lost in form."), keeps("Greek 'that soul shall be destroyed from among his people'."), between("The Latin has 'perish' or 'cut off'; the King James 'cut off'.")]
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the testimony'; the King James 'tabernacle of the congregation'.")]
HOUSE = [loses("Hebrew 'the house of Israel' is lost."), keeps("Greek 'the sons of Israel … the resident foreigners attached unto you'."), between("The Latin and King James have 'the house of Israel'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'leviticus', 'chapter': 17,
 'chapterNote': "The place of slaughter and the sanctity of blood: any Israelite who slaughters an ox, sheep or goat without bringing it to the Tent of Meeting is guilty of blood and cut off; sacrifices are to be brought to the priest and offered as peace offerings, and no longer to the goat-demons; anyone, Israelite or resident foreigner, who offers elsewhere or eats blood is cut off, for the life of the flesh is in the blood, given on the altar to atone; the blood of hunted game is poured out and covered; whoever eats carrion washes and is unclean until evening. The Greek adds the resident foreigners to the first rule (17:3), expands 17:4 with named offerings, acceptability and a repeated condition, has 'vain things' for the Hebrew's goat-demons (17:7), 'destroyed' for 'cut off', 'the life of all flesh is its blood' and 'in place of the life' (anti) for the Hebrew's 'the life of the flesh is in the blood … atones by the life' (17:11, 14), which the source marks as a material change in the stated rationale, and 'lawless deed' for 'guilt' (17:16). The Latin has 'demons' at 17:7.",
 'verses': {
  '17:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the place of slaughter."],
   "YHWH spoke on where animals may be killed.", "After the Day of Atonement, the law of blood; the altar that was just cleansed is now made the only place blood may be shed for God.", FORMULA, ['yhwh-yahweh', 'moses']),
  '17:2': v("Moses is to speak to Aaron, his sons and all Israel what YHWH commanded.", "All four columns agree.",
   ["To Aaron and his sons.", "And all Israel.", "What YHWH commanded."], "The law was addressed to priests and people alike.", "Priests and people together; the rule about where to kill an animal binds the one who offers and the one who brings.", [AGREE], ['high-priest', 'yhwh-yahweh']),
  '17:3': v("Any man of the house of Israel who slaughters an ox, sheep or goat in the camp or outside it,",
   "The Hebrew, Latin and King James name the house of Israel; the Greek adds 'or of the resident foreigners attached to you' and 'calf'. Both include foreigners in later rules.",
   ["Any man of Israel.", "Slaughters ox, sheep or goat.", "In or outside the camp."], "The rule covered any Israelite slaughtering sacrificial animals.", "Ox, sheep, goat: the three sacrificial species; the law does not yet say what is wrong, only who and what.",
   HOUSE + [keeps("Greek 'calf' for ox.")]),
  '17:4': v("And does not bring it to the Tent of Meeting to present to YHWH before his tabernacle, bloodguilt is reckoned to him; he has shed blood and is cut off from his people.",
   "The Hebrew and King James have one condition; the Greek greatly expands, naming burnt and deliverance offerings, 'acceptable … for a sweet savour', and repeating the outside-slaughter clause; 'destroyed' for 'cut off'.",
   ["Not brought to the tent.", "Bloodguilt reckoned.", "Cut off from his people."], "Slaughter away from the tent was reckoned as bloodshed.", "To kill an ox away from the altar is to shed blood, as if a man were murdered; the animal's life belongs to God, and spilling it elsewhere is theft of a life.",
   TENT + CUTOFF + [keeps("Greek adds 'to prepare it as a whole burnt offering or an offering of deliverance acceptable unto the Lord for a sweet savour; and whosoever slaughters outside …'.")], ['tabernacle', 'yhwh-yahweh']),
  '17:5': v("So that Israel brings the sacrifices they slaughter in the open field to YHWH at the tent's entrance, to the priest, as peace offerings.", "All four columns agree; the Greek 'plains' and 'deliverance'.",
   ["Sacrifices from the field.", "To the priest at the tent.", "As peace offerings."], "Field sacrifices were redirected to the sanctuary.", "Bring it in from the field: the law gathers every private slaughter to one door, and turns it into a shared meal before God.",
   TENT + [loses("Hebrew 'open field' and 'well-being' are lost."), keeps("Greek 'in the plains … a sacrifice of deliverance'.")], ['high-priest', 'tabernacle']),
  '17:6': v("The priest dashes the blood against YHWH's altar at the tent's entrance and burns the fat for a pleasing aroma.", "All four columns agree; the Greek 'pour all around' and 'offer up'.",
   ["Blood on YHWH's altar.", "At the tent's entrance.", "Fat burned for a pleasing aroma."], "Blood and fat went to the altar.", "Blood to the altar, fat to the fire; what a man would have done in the field is done at the door by the priest, and God receives it.",
   [loses("Hebrew 'dash' and 'burn' are lost."), keeps("Greek 'pour the blood all around … offer up the fat'."), between("The Latin and King James have 'pour' and 'burn'.")], ['high-priest', 'altar', 'term-savor']),
  '17:7': v("They no longer sacrifice to the goat-demons after which they prostitute themselves; a perpetual statute.",
   "The Hebrew se'irim are goat-like demons; the Greek 'the vain things' (mataioi); the Latin 'demons'; the King James 'devils'. The source says the Greek does not deny spirits exist.",
   ["No more sacrifices.", "To the goat-demons.", "A perpetual statute."], "Sacrifice to goat-demons was ended forever.", "Goat-demons of the field: the law reveals what the open-field slaughter was for; Israel had been feeding the desert's spirits, and the altar is the cure.",
   [loses("Hebrew 'goat-demons' (se'irim) is lost."), keeps("Greek 'the vain things after which they prostitute themselves'."), between("The Latin has 'demons'; the King James 'devils'.")], ['demons', 'evil-spirits-and-adversaries']),
  '17:8': v("Any man of the house of Israel or the resident foreigners among them who offers a burnt offering or sacrifice,", "All four columns agree in substance; the Greek 'sons of Israel' and 'sons of the resident foreigners'.",
   ["Any Israelite or foreigner.", "Offers a burnt offering.", "Or sacrifice."], "The rule extended to resident foreigners.", "The foreigner living among them is bound too; the altar's monopoly covers everyone under Israel's tents.",
   HOUSE, ['altar']),
  '17:9': v("And does not bring it to the Tent of Meeting to offer to YHWH is cut off from his people.", "All four columns agree; 'destroyed' in Greek.",
   ["Not brought to the tent.", "To offer to YHWH.", "Cut off."], "Offering elsewhere meant being cut off.", "Cut off for worshipping in the wrong place; a sacrifice to the right God at the wrong altar is no sacrifice.", TENT + CUTOFF, ['tabernacle', 'yhwh-yahweh']),
  '17:10': v("Any Israelite or resident foreigner who eats blood, God sets his face against and cuts off from his people.", "All four columns agree; 'destroy' in Greek.",
   ["Anyone who eats blood.", "God's face against him.", "Cut off."], "Eating blood brought God's own opposition.", "'I will set my face against': God himself turns on the blood-eater; the other penalties are the community's, this one is personal.",
   HOUSE + CUTOFF, ['yhwh-yahweh'], "None of you shall eat blood."),
  '17:11': v("For the life of the flesh is in the blood, and God has given it on the altar to make atonement for their lives, for the blood makes atonement by the life.",
   "The Hebrew locates life in the blood and has blood atone 'by the life'; the Greek 'the life of all flesh is its blood' and 'in place of the life' (anti), which the source marks as a material change in rationale while noting the Hebrew too permits an exchange reading.",
   ["Life in the blood.", "Given on the altar.", "To atone for lives."], "Blood atoned because it carried life.", "The reason behind every sacrifice in the book, given once: blood is life, and God takes the life on the altar in place of yours. The Greek says 'in place of' outright; the Hebrew lets the preposition carry it.",
   [loses("Hebrew 'the life of the flesh is in the blood' and 'makes atonement by the life' are lost."), keeps("Greek 'the life of all flesh is its blood … its blood shall make atonement in place of (anti) the life'."), between("The Latin has 'the life of the flesh is in the blood'; the King James 'the blood … maketh an atonement for the soul'.")], ['altar', 'redeemer']),
  '17:12': v("Therefore no Israelite eats blood, nor the resident foreigner among them.", "All four columns agree.",
   ["Therefore.", "No Israelite eats blood.", "Nor the foreigner."], "The blood prohibition bound all residents.", "'Therefore': the rule follows from the reason; because blood is life given for life, no one may make it food.", [AGREE], [], "None of you shall eat blood."),
  '17:13': v("Any Israelite or foreigner who hunts an edible animal or bird pours out its blood and covers it with dust.", "All four columns agree; the Greek 'wild animal' and 'earth'.",
   ["Hunting an edible animal.", "Pour out the blood.", "Cover it with dust."], "Hunted game's blood was poured out and covered.", "Game cannot be brought to the altar, so its blood is buried; the hunter gives the life back to the ground, as the priest gives it to God.",
   [keeps("Greek 'a wild animal or bird … cover it with earth'."), between("The Latin and King James have 'cover it with dust' or 'earth'.")]),
  '17:14': v("For the life of all flesh is its blood; Israel is told to eat no blood of any flesh, for the life of all flesh is its blood; whoever eats it is cut off.",
   "The Hebrew's first clause 'its blood with its life' is compressed and difficult; the Greek a direct identification; 'destroyed' for 'cut off'.",
   ["The life is the blood.", "Eat no blood.", "Whoever does is cut off."], "The blood rule was repeated with its reason.", "The reason said twice in one verse; the law will not let Israel forget why, and the why is that life is not theirs to eat.",
   CUTOFF + [loses("Hebrew 'its blood with its life' is lost."), keeps("Greek 'the life of all flesh is its blood'.")]),
  '17:15': v("Anyone, native or foreigner, who eats an animal found dead or torn washes his garments, bathes, and is unclean until evening; then clean.", "All four columns agree.",
   ["Eating carrion.", "Wash and bathe.", "Unclean until evening."], "Eating carrion required washing until evening.", "Carrion's blood was never poured out; the one who eats it has eaten blood by accident, and the penalty is only water and a day.", [AGREE]),
  '17:16': v("But if he does not wash them and bathe his body, he bears his guilt.", "All four columns agree; the Greek 'garments … in water' and 'lawless deed'.",
   ["Not washing.", "Not bathing.", "He bears his guilt."], "Neglecting to wash left the guilt on him.", "The remedy is small and refusing it is not; a man who will not wash carries the uncleanness himself, and the law calls that guilt.",
   [loses("Hebrew 'bear his guilt' is lost in form."), keeps("Greek 'does not wash his garments and does not bathe his body in water, he shall bear his lawless deed'."), between("The Latin and King James have 'bear his iniquity'.")]),
 },
}
