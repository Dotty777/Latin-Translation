K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
BITTER = [loses("Hebrew 'the bitter water that brings a curse' is lost."), keeps("Greek 'this curse-bringing water of testing'."), between("The Latin and King James have 'bitter water'.")]
GRAIN = [loses("Hebrew 'grain offering' is lost."), keeps("Greek 'sacrifice'."), between("The Latin has 'oblation'; the King James 'offering'.")]
STRAY = [loses("Hebrew 'acts unfaithfully' (ma'al) is lost."), keeps("Greek 'utterly disregards' or 'conceals'."), between("The Latin has 'despises'; the King James 'trespass'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 5,
 'chapterNote': "Three laws for the camp where God dwells: the leprous, the discharging and the corpse-defiled, male and female, sent outside it; a wrong done to a neighbour confessed and repaid in full with a fifth, to the kinsman or, failing one, to the priest with the ram of atonement, and the priest's dues; and the ordeal of the suspected wife. A husband seized by a spirit of jealousy brings his wife with a tenth of an ephah of barley without oil or frankincense; the priest stands her before YHWH, mixes holy water and dust from the Dwelling's floor in an earthen vessel, loosens her hair, puts the offering in her palms, lays the curse on her (thigh falling, belly swelling), she answers Amen, amen, he writes the curses and washes them into the water, waves and burns the offering, and she drinks: the guilty becomes a curse among her people, the innocent is free and bears children; the husband is free of guilt. The Greek has 'seminal discharge' (5:2), 'acts with utter disregard' for 'acts unfaithfully against YHWH' (5:6) and 'disregards' or 'conceals' for 'acts unfaithfully' (5:12, 27), 'first portion … unto the Lord' (5:9), 'sacrifice' for 'grain offering' and 'sin' for 'guilt' (5:15), 'clean, living water' for 'holy water' (5:17), 'uncover her head' for 'loosen her hair' and 'water of testing' for 'bitter water' throughout (5:18–24), 'place' for 'wave' (5:25), lacks the repeated drinking at 5:27, 'So be it' for 'Amen' (5:22), and 'bring forth seed' for 'be sown with seed' (5:28).",
 'verses': {
  '5:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On the unclean."],
   "YHWH spoke on excluding the unclean.", "The camp has been drawn and counted; now it is kept clean.", FORMULA, ['yhwh-yahweh', 'moses']),
  '5:2': v("Command Israel to send out of the camp everyone leprous, everyone with a discharge, and everyone unclean through a corpse.", "All four columns agree; the Greek 'seminal discharge'. Ancient categories, not diagnoses.",
   ["Lepers sent out.", "Those with a discharge.", "The corpse-defiled."], "Three uncleannesses left the camp.", "The three uncleannesses of Leviticus 13–15 and Numbers 19 named together; the camp is a holy place at the scale of a city.",
   [keeps("Greek 'everyone with a seminal discharge'."), between("The Latin and King James have 'issue'.")], [], "Send out of the camp everyone unclean."),
  '5:3': v("Male and female alike, outside the camp, so they do not defile their camps where God dwells among them.", "All four columns agree; the Latin 'while dwelling with you'.",
   ["Male and female.", "Outside the camp.", "Where God dwells."], "God's presence required a clean camp.", "'Where I dwell among them': the reason for exclusion is not the sick person's fault but the neighbour's holiness; Miriam will stand outside this camp seven days.",
   [between("The Latin has 'while I dwell with you'; the Greek and King James 'wherein I dwell among them'.")], ['miriam']),
  '5:4': v("Israel did so and sent them out; as YHWH spoke to Moses, so Israel did.", "All four columns agree.",
   ["Israel did so.", "Sent them out.", "As YHWH spoke."], "The command was obeyed.", "Done at once; the obedience formula still comes easily in chapter 5.", [AGREE], ['yhwh-yahweh', 'moses']),
  '5:5': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On restitution."],
   "YHWH spoke on restitution.", "From the body to the purse: a wrong done is a defilement too.", FORMULA, ['yhwh-yahweh', 'moses']),
  '5:6': v("When a man or woman commits any human sin, acting unfaithfully against YHWH, and becomes guilty,", "The Hebrew names unfaithfulness against YHWH; the Greek 'acts with utter disregard' without naming God here. The Latin 'negligence'.",
   ["Man or woman.", "Any human sin.", "Unfaithful against YHWH."], "Wrong to a neighbour was unfaithfulness to God.", "A theft from a neighbour is called treachery against YHWH; the two are one sin with two victims.",
   STRAY + [loses("Hebrew 'against YHWH' is lost."), keeps("Greek 'commits any of the sins of men'.")], ['yhwh-yahweh']),
  '5:7': v("They confess the sin, repay the wrong in full, add a fifth, and give it to the person wronged.", "All four columns agree.",
   ["Confess.", "Repay in full plus a fifth.", "To the wronged."], "Confession and restitution went together.", "Confess first, then pay: the mouth before the hand, and the fifth is the cost of having had to be made to.", [AGREE], [], "They shall confess the sin and repay with a fifth added."),
  '5:8': v("If the man has no kinsman to receive it, the repayment to YHWH belongs to the priest, besides the ram of atonement.", "All four columns agree.",
   ["No kinsman.", "Repayment to YHWH.", "The priest's, plus the ram."], "Unclaimed restitution went to the priest.", "If the victim is dead with no heir, God is the heir, and the priest takes it for him; a debt does not vanish because the creditor did.",
   [AGREE], ['high-priest', 'yhwh-yahweh']),
  '5:9': v("Every contribution from Israel's holy gifts brought to the priest is his.", "The Hebrew 'contribution'; the Greek 'first portion … unto the Lord'.",
   ["Every contribution.", "Brought to the priest.", "Is his."], "Priests kept what was brought them.", "The priests' income stated in passing, between the restitution and the ordeal.",
   [loses("Hebrew 'contribution' (terumah) is lost."), keeps("Greek 'every first portion … that they bring unto the Lord'."), between("The Latin and King James have 'offering' or 'firstfruits'.")], ['high-priest']),
  '5:10': v("Each man's holy gifts are his; whatever a man gives the priest is his.", "All four columns keep the compressed 'his/him'; the first clause is interpretive.",
   ["Each man's gifts.", "Given to the priest.", "His."], "What was given became the priest's.", "A knot of pronouns: the gift is the giver's until given, and then the priest's; the law insists on both ownerships in one breath.",
   [between("All four columns keep the compressed pronouns.")], ['high-priest']),
  '5:11': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On jealousy."],
   "YHWH spoke on the jealous husband.", "The third speech, the longest and strangest in the chapter.", FORMULA, ['yhwh-yahweh', 'moses']),
  '5:12': v("If any man's wife strays and acts unfaithfully against him,", "The Hebrew 'acts unfaithfully' (ma'al, as in 5:6); the Greek 'utterly disregards him'.",
   ["A man's wife.", "Strays.", "Unfaithful to him."], "The case of a straying wife was set.", "The same word as 5:6: adultery is treachery of the kind done against God, and the husband is its YHWH.", STRAY),
  '5:13': v("A man lies with her, hidden from her husband, she conceals it, is defiled, with no witness and not caught,", "All four columns agree.",
   ["Hidden adultery.", "No witness.", "Not caught."], "The ordeal was for unprovable cases.", "No witness, not caught: the ordeal exists precisely where the law's ordinary machinery of two witnesses cannot work.", [AGREE]),
  '5:14': v("A spirit of jealousy comes over him and he is jealous of his wife, whether she is defiled or not.", "All four columns agree.",
   ["A spirit of jealousy.", "Over the husband.", "Defiled or not."], "The husband's suspicion might be baseless.", "'Or she is not defiled': the law admits from the start that the husband may be wrong, and the rite is as much to protect her from him as him from her.", [AGREE], ['jealous']),
  '5:15': v("He brings his wife to the priest with her offering: a tenth of an ephah of barley flour, no oil or frankincense, a grain offering of jealousy, a memorial bringing guilt to remembrance.",
   "The Hebrew 'grain offering … guilt'; the Greek 'sacrifice … sin' and 'oiphi'; the Latin 'a tenth of a seah'.",
   ["To the priest.", "Barley, no oil or incense.", "A memorial of guilt."], "The jealousy offering was bare barley.", "Barley, the poor man's grain, without the oil or incense that make an offering pleasant; the gift is as grim as the occasion.",
   GRAIN + [loses("Hebrew 'bringing guilt to remembrance' is lost."), keeps("Greek 'bringing sin to remembrance … oiphi'."), between("The Latin has 'tenth of a seah'; the King James 'tenth part of an ephah'.")], ['high-priest', 'incense']),
  '5:16': v("The priest brings her near and stands her before YHWH.", "All four columns agree.", ["The priest brings her.", "Stands her.", "Before YHWH."],
   "The woman stood before God.", "She is set before YHWH, not before her husband; the judge in this case is the one who saw what no witness did.", [AGREE], ['high-priest', 'yhwh-yahweh']),
  '5:17': v("The priest takes holy water in an earthen vessel and puts dust from the Dwelling's floor into it.", "The Hebrew 'holy water'; the Greek 'clean, living water'. Holiness and cleanness are not the same word.",
   ["Holy water.", "An earthen vessel.", "Dust from the floor."], "Water and tabernacle dust were mixed.", "Holy water and holy dust in a clay cup: the only 'holy water' in the Torah, and it is made bitter with the ground God stands on.",
   [loses("Hebrew 'holy water' is lost."), keeps("Greek 'clean, living water'."), between("The Latin and King James have 'holy water'.")], ['tabernacle']),
  '5:18': v("The priest stands her before YHWH, loosens her hair, puts the memorial grain offering in her palms; in his hand the bitter water that brings a curse.",
   "The Hebrew 'loosen the hair'; the Greek 'uncover her head'; the Hebrew 'bitter water'; the Greek 'water of testing'.",
   ["Her hair loosened.", "The offering in her palms.", "The bitter water."], "The woman was made ready.", "Loosened hair, the sign of mourning and shame; she holds her own accusation in her hands while the priest holds the verdict in his.",
   BITTER + GRAIN + [loses("Hebrew 'loosen the hair of her head' is lost."), keeps("Greek 'uncover her head'.")], ['high-priest']),
  '5:19': v("The priest puts her under oath: if no man has lain with you and you have not strayed into defilement under your husband, be free from this bitter water.", "All four columns agree; 'water of testing' in Greek.",
   ["Under oath.", "If innocent.", "Free from the water."], "The innocent verdict was spoken first.", "The acquittal is said before the curse; the rite begins by naming the outcome it hopes for.", BITTER),
  '5:20': v("But if you have strayed under your husband, been defiled, and another man has put his emission in you,", "All four columns agree; the Greek 'or' and 'someone other than your husband has lain with you'.",
   ["If you have strayed.", "Been defiled.", "With another man."], "The guilty case was named.", "The guilty case is put as plainly as the innocent; the priest says aloud what no one saw.",
   [keeps("Greek 'or have become defiled, and someone other than your husband has lain with you'.")]),
  '5:21': v("The priest puts her under the oath of the curse: may YHWH make you a curse and an oath among your people, when he makes your thigh fall and your belly swell.", "All four columns keep the bodily imagery without a modern diagnosis.",
   ["The oath of the curse.", "A curse among your people.", "Thigh fall, belly swell."], "The curse was bodily.", "'Thigh' and 'belly', the body's seat of sex and childbearing; the curse strikes where the sin was, and the text will not say more precisely than that.",
   [between("All four columns keep 'thigh' and 'belly'; the Latin adds 'bursting'.")], ['yhwh-yahweh']),
  '5:22': v("May this curse-bringing water enter your inward parts, making the belly swell and the thigh fall. The woman says: Amen, amen.", "The Hebrew 'Amen, amen'; the Greek 'So be it, so be it'.",
   ["The water enters.", "Belly and thigh.", "Amen, amen."], "The woman assented to the curse.", "'Amen, amen': the first double amen in Scripture, spoken by a woman taking a curse on herself to prove it false.",
   [loses("Hebrew 'Amen, amen' is lost."), keeps("Greek 'So be it, so be it'."), between("The Latin and King James have 'Amen, amen'.")]),
  '5:23': v("The priest writes the curses in a scroll and wipes them into the bitter water.", "All four columns agree; 'water of testing' in Greek.",
   ["Curses written.", "In a scroll.", "Wiped into the water."], "The curse was dissolved in the water.", "Words washed off a scroll into a cup: she drinks the ink of her own sentence. The curse is literal, a text swallowed.", BITTER, ['scroll']),
  '5:24': v("He makes her drink the bitter water that brings a curse, and it enters her for bitterness.", "The Hebrew's repeated 'bitterness'; the Greek 'testing'.",
   ["She drinks.", "The bitter water.", "It enters her."], "The woman drank.", "Said here and again at 5:26–27; the Hebrew tells the drinking three times, as if the moment were too heavy for once.", BITTER),
  '5:25': v("The priest takes the jealousy offering from her hand, waves it before YHWH, and brings it to the altar.", "The Hebrew 'wave'; the Greek 'place'.",
   ["The offering taken.", "Waved before YHWH.", "To the altar."], "The offering was waved and brought.", "The barley lifted toward God before the fire; even the offering of jealousy is given the gesture of a gift.",
   GRAIN + [loses("Hebrew 'wave' is lost."), keeps("Greek 'place the sacrifice before the Lord'."), between("The Latin and King James have 'wave' or 'lift up'.")], ['altar', 'high-priest']),
  '5:26': v("The priest takes a handful as its memorial portion and burns it on the altar; afterward he makes her drink.", "All four columns agree; 'offer up' in Greek.",
   ["A handful.", "Burned on the altar.", "Then she drinks."], "The memorial was burned before the drinking.", "A handful of barley in the fire, and then the cup; the order is offering first, judgment second.",
   GRAIN + [keeps("Greek 'offer it up'.")], ['altar']),
  '5:27': v("He makes her drink; if she is defiled and acted unfaithfully against her husband, the water enters her for bitterness, her belly swells, her thigh falls, and she becomes a curse among her people.",
   "The Hebrew repeats the drinking and 'acted unfaithfully'; the Greek lacks the drinking and has 'concealed it'.",
   ["If defiled.", "Belly swells, thigh falls.", "A curse among her people."], "The guilty woman was cursed.", "The guilty outcome: God, who saw, makes the verdict visible in her body; the camp learns from her flesh what it could not learn from witnesses.",
   STRAY + [loses("Hebrew 'He shall make her drink the water' is lost."), keeps("Greek 'has concealed it from her husband'.")]),
  '5:28': v("If the woman is not defiled and is clean, she is free and is sown with seed.", "The Hebrew 'be sown with seed' (passive); the Greek 'bring forth seed'.",
   ["Not defiled.", "Free.", "Sown with seed."], "The innocent woman was blessed.", "The innocent is not merely spared but promised children; the ordeal that could curse her womb blesses it instead.",
   [loses("Hebrew 'shall be sown with seed' is lost."), keeps("Greek 'shall bring forth seed'."), between("The Latin and King James have 'conceive' or 'bear children'.")]),
  '5:29': v("This is the instruction for jealousy, when a wife strays under her husband and is defiled,", "All four columns agree.",
   ["The law of jealousy.", "A wife strays.", "Is defiled."], "The law was named.", "'The torah of jealousy': a law named for a passion, the only one so named.", [AGREE], ['jealous']),
  '5:30': v("Or when a spirit of jealousy comes over a man and he is jealous of his wife; he stands her before YHWH and the priest performs all this instruction.", "All four columns agree.",
   ["Or a jealous husband.", "Before YHWH.", "The priest performs it."], "The rite covered both cases.", "Whether she strayed or he only feared it, the rite is the same; the law gives the jealous man something to do other than what jealous men do.", [AGREE], ['high-priest', 'yhwh-yahweh']),
  '5:31': v("The man is free from guilt; that woman bears her guilt.", "All four columns agree.",
   ["The man free.", "The woman bears guilt.", "Asymmetrical."], "The husband bore no guilt for the accusation.", "The husband is cleared whatever the result; the woman bears whatever is hers. The asymmetry is the law's, and the text does not soften it.", [AGREE]),
 },
}
