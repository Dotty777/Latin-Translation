K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
TENT = [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'Tent of Testimony'."), between("The Latin has 'tabernacle of the covenant'; the King James 'tabernacle of the congregation'.")]
LEP = [between("The Hebrew tsara'at and Greek lepra name the ancient skin-affliction category, not modern Hansen's disease; the Latin and King James have 'leprous'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 12,
 'chapterNote': "Miriam and Aaron speak against Moses over his Cushite wife and his monopoly of God's word; Moses is the humblest man on earth. YHWH summons the three to the tent, comes down in the pillar of cloud, and distinguishes Moses from every prophet: to prophets he speaks in vision and dream, to Moses mouth to mouth, plainly, and Moses beholds YHWH's form. The cloud withdraws and Miriam is leprous white as snow; Aaron pleads, Moses cries 'O God, heal her', and YHWH shuts her out of the camp seven days as a father's spittle would shame a daughter; the people wait, then march to Paran. The Greek has 'Ethiopian' for 'Cushite' and repeats Moses' name (12:1), 'spoken unto' for 'spoken through' (12:2), 'meek' for 'humble' (12:3), reverses Aaron and Miriam and repeats the destination (12:4), 'were called' for 'He called' (12:5), 'a prophet unto the Lord … in sleep' (12:6), 'he saw the glory of the Lord' for 'he beholds YHWH's form' (12:8), 'ignorantly' for 'foolishly' (12:11), 'a miscarried child … consumes half her flesh' for 'a dead child whose flesh is half consumed' (12:12), and 'until Miriam was cleansed' for 'received back' (12:15). The Latin has 'alone' at 12:4 and 'white' at 12:10.",
 'verses': {
  '12:1': v("Miriam and Aaron spoke against Moses because of the Cushite woman he had married.", "The Hebrew 'Cushite'; the Greek 'Ethiopian' and repeats Moses' name. The woman is unnamed; Zipporah is an interpretation.",
   ["Miriam and Aaron.", "Against Moses.", "The Cushite wife."], "Moses' siblings attacked his marriage.", "Miriam named first: the prophetess leads the complaint, and the pretext is a foreign wife. The real grievance comes in the next verse.",
   [loses("Hebrew 'Cushite' is lost."), keeps("Greek 'Ethiopian … for he had married an Ethiopian woman'."), between("The Latin and King James have 'Ethiopian'.")], ['miriam', 'high-priest', 'moses']),
  '12:2': v("They said: has YHWH spoken only through Moses? has he not also spoken through us? And YHWH heard.", "The Hebrew 'through' (b-); the Greek 'unto'. The claim to privileged speech is the same.",
   ["Only through Moses?", "Not through us?", "YHWH heard."], "The quarrel was over prophecy.", "'Has he not spoken through us also?' True, and beside the point; the chapter will say what Moses has that they do not. 'And YHWH heard' is the quiet threat.",
   [keeps("Greek 'spoken only unto Moses … unto us'."), between("The Latin and King James have 'by Moses … by us'.")], ['yhwh-yahweh', 'moses']),
  '12:3': v("Now the man Moses was very humble, more than anyone on the face of the earth.", "The Hebrew 'humble'; the Greek 'meek'; overlapping senses.",
   ["The man Moses.", "Very humble.", "More than anyone."], "Moses' humility was noted.", "The narrator's aside: Moses will not defend himself, so the text does. The humblest man on earth is about to be defended by God.",
   [keeps("Greek 'very meek'."), between("The Latin has 'most gentle'; the King James 'very meek'.")], ['moses']),
  '12:4': v("Suddenly YHWH said to Moses, Aaron and Miriam: come out, all three, to the Tent of Meeting; and the three came out.", "The Greek reverses Aaron and Miriam and repeats the destination; the Latin 'alone'.",
   ["Suddenly.", "All three to the tent.", "They came out."], "God summoned the three at once.", "'Suddenly': no deliberation, the three are called like children to the door; the matter is settled where God lives.",
   TENT + [keeps("Greek 'Moses, Miriam, and Aaron … came out to the Tent of Testimony'."), between("The Latin adds 'alone'.")], ['tabernacle', 'yhwh-yahweh']),
  '12:5': v("YHWH came down in a pillar of cloud, stood at the tent's entrance, and called Aaron and Miriam; both came forward.", "All four columns agree; 'were called' in Greek.",
   ["The pillar of cloud.", "At the entrance.", "Aaron and Miriam called."], "God separated the two from Moses.", "Two called forward, one left standing; the separation is made before a word is spoken.",
   [keeps("Greek 'Aaron and Miriam were called'."), between("The Latin and King James have 'called'.")], ['yhwh-yahweh', 'high-priest', 'miriam']),
  '12:6': v("Hear my words: if there is a prophet among you, I, YHWH, make myself known to him in a vision; I speak with him in a dream.", "The Hebrew's divine name sits oddly; the Greek 'a prophet among you unto the Lord … in sleep'.",
   ["Hear my words.", "A prophet.", "Vision and dream."], "Prophets received vision and dream.", "Vision and dream, the ordinary channels; Miriam is a prophetess and this is how she hears. It is not nothing, and it is not what Moses has.",
   [keeps("Greek 'a prophet among you unto the Lord … in sleep'."), between("The Latin has 'vision or dream'; the King James 'vision … dream'.")], ['yhwh-yahweh']),
  '12:7': v("Not so my servant Moses; he is faithful in all my house.", "All four columns agree; the Latin 'most faithful'.",
   ["Not so Moses.", "My servant.", "Faithful in all my house."], "Moses was God's trusted steward.", "'Faithful in all My house': the steward with the keys, not a visitor at the door. Hebrews 3 will set Jesus beside this verse.",
   [between("The Latin has 'most faithful'; the Greek and King James 'faithful'.")], ['moses', 'servant']),
  '12:8': v("With him I speak mouth to mouth, plainly, not in riddles, and he beholds YHWH's form. Why were you not afraid to speak against my servant Moses?",
   "The Hebrew 'he beholds YHWH's form' (temunah); the Greek 'he saw the glory of the Lord'. The object of Moses' vision differs.",
   ["Mouth to mouth.", "Not in riddles.", "He beholds YHWH's form."], "Moses alone saw God's form.", "'Mouth to mouth', and 'the form of YHWH': the Hebrew says Moses sees something of God himself; the Greek, uneasy, made it glory. The boldest verse about Moses in the Torah.",
   [loses("Hebrew 'he beholds YHWH's form' is lost."), keeps("Greek 'in visible appearance … he saw the glory of the Lord'."), between("The Latin has 'sees the Lord openly'; the King James 'the similitude of the LORD'.")], ['moses', 'yhwh-yahweh', 'servant']),
  '12:9': v("YHWH's anger flared against them, and he departed.", "All four columns agree.",
   ["YHWH's anger.", "Against them.", "He departed."], "God left in anger.", "He leaves: the cloud lifts from the door, and what it was hiding is seen.", [AGREE], ['yhwh-yahweh']),
  '12:10': v("The cloud withdrew from the tent, and there was Miriam, afflicted with skin disease, white as snow; Aaron turned, and she was diseased.", "All four columns agree; the Latin alone has 'white'. Ancient category, not Hansen's disease.",
   ["The cloud withdrew.", "Miriam leprous as snow.", "Aaron saw."], "Miriam was struck with leprosy.", "Miriam alone is struck, though Aaron spoke too; she led, and she is marked. Aaron 'turned toward' her: the priest who diagnoses leprosy looks at his sister.",
   LEP + [between("The Latin has 'white as snow'; the Greek and King James 'as snow'.")], ['miriam', 'high-priest']),
  '12:11': v("Aaron said to Moses: please, my lord, do not lay on us the sin in which we acted foolishly and sinned.", "The Hebrew 'foolishly'; the Greek 'ignorantly'.",
   ["Please, my lord.", "Do not lay the sin on us.", "We acted foolishly."], "Aaron confessed to Moses.", "'My lord', from the elder brother to the younger: Aaron's confession is also a submission, the answer to 12:2.",
   [loses("Hebrew 'acted foolishly' is lost."), keeps("Greek 'we acted ignorantly'."), between("The Latin and King James have 'foolishly'.")], ['high-priest', 'moses']),
  '12:12': v("Do not let her be like a dead child whose flesh is half consumed when it comes from its mother's womb.",
   "The Hebrew 'his flesh', the dead child's; the Greek 'a miscarried child … it consumes half her flesh', the referent shifted to Miriam.",
   ["Not like a dead child.", "Flesh half consumed.", "From the womb."], "Aaron pleaded for Miriam.", "The image is a stillbirth: the leprous woman is already half dead, half eaten. Aaron's plea is the plea of a brother who has lost two sons.",
   [loses("Hebrew 'a dead child whose flesh is half consumed' is lost."), keeps("Greek 'a miscarried child … it consumes half her flesh'."), between("The Latin has 'already devoured by leprosy'; the King James 'half consumed'.")], ['miriam']),
  '12:13': v("Moses cried to YHWH: O God, please heal her, please!", "All four columns agree; the Hebrew repeats its particle.",
   ["Moses cried.", "O God.", "Heal her, please!"], "Moses prayed for his accuser.", "Five Hebrew words, the shortest prayer in the Torah, for the sister who attacked him; the humblest man on earth asks nothing for himself.", [AGREE], ['moses', 'yhwh-yahweh', 'yhwh-rapha']),
  '12:14': v("YHWH said: if her father had spat in her face, would she not be disgraced seven days? shut her outside the camp seven days; afterward she may be received back.", "All four columns agree; 'set apart … enter' in Greek.",
   ["A father's spittle.", "Seven days.", "Outside the camp."], "Miriam was excluded a week.", "God as a father who spat in his daughter's face: the punishment is shame, not destruction, and it has a term. Seven days, then home.",
   [keeps("Greek 'set apart outside the camp … afterward she shall enter'."), between("The Latin has 'called back'; the King James 'received in again'.")], ['yhwh-yahweh'], "Let her be shut outside the camp for seven days."),
  '12:15': v("Miriam was shut outside the camp seven days, and the people did not set out until she was received back.", "The Hebrew 'received back'; the Greek 'cleansed'.",
   ["Miriam outside.", "Seven days.", "The people waited."], "The whole camp waited for Miriam.", "Six hundred thousand men wait a week for one woman; the camp does not move without its prophetess, and the law of chapter 5 is kept on the most honoured of its subjects.",
   [loses("Hebrew 'until Miriam was received back' is lost."), keeps("Greek 'until Miriam was cleansed'."), between("The Latin and King James have 'brought in again'.")], ['miriam']),
  '12:16': v("Afterward the people set out from Hazeroth and camped in the wilderness of Paran.", "All four columns agree.",
   ["From Hazeroth.", "To Paran.", "They camped."], "The march reached Paran.", "Paran, the edge of the land; from here the spies go out, and the book's great failure begins.", [AGREE]),
 },
}
