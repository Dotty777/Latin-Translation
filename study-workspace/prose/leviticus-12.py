K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
BLOOD = [loses("Hebrew 'the blood of purification' is lost."), keeps("Greek 'her unclean blood'."), between("The Latin and King James have 'the blood of her purification' or 'purifying'.")]

CHAPTER = {
 'slug': 'leviticus', 'chapter': 12,
 'chapterNote': "Purification after childbirth: a woman who bears a son is unclean seven days as in her menstruation, the boy is circumcised on the eighth day, and she remains thirty-three days in the blood of purification, touching nothing holy; for a daughter the periods are doubled, fourteen and sixty-six days. When the days are complete she brings a year-old lamb for a burnt offering and a pigeon or turtledove for a sin offering, or two birds if she cannot afford a lamb; the priest makes atonement and she is clean from the source of her blood. The Greek has 'receives seed' for the Hebrew 'conceives' (12:2), an unnamed 'he shall circumcise' for the Hebrew passive (12:3), 'her unclean blood' for 'the blood of purification' (12:4–5), which the source marks as a material difference of terminology, 'unblemished' added at 12:6, and the priest as the agent who cleanses her at 12:7 where the Hebrew has 'she shall be clean'. The Latin renders atonement as the priest's prayer. Neither column makes childbirth a moral fault.",
 'verses': {
  '12:1': {
   'received': "YHWH speaks to Moses.",
   'explain': "All four columns agree.",
   'shared': ["YHWH speaks.", "To Moses.", "On childbirth."],
   'instructions': [ins(K, S, "YHWH gave Moses the law of the mother's purification."), ins(W, R, "After the animals, the mother; the law turns from what is eaten to what gives birth, and treats both as matters of clean and unclean.")],
   'entries': ['yhwh-yahweh', 'moses'],
   'lost': FORMULA,
  },
  '12:2': {
   'received': "If a woman conceives and bears a male, she is unclean seven days, as in the days of her menstrual separation.",
   'explain': "The Hebrew tazria' 'conceives'; the Greek and Latin passive 'receives seed'; the King James 'conceived seed'. The source says neither text calls childbirth a transgression.",
   'shared': ["A woman bears a male.", "Unclean seven days.", "As in menstruation."],
   'instructions': [ins(K, S, "A mother of a son was unclean seven days."), ins(W, R, "Unclean after birth as after menstruation; the law treats the blood of childbirth as blood, not as sin, and the mother's state is the body's, not the soul's.")],
   'entries': [],
   'lost': [loses("Hebrew 'conceives' (tazria') is lost."), keeps("Greek 'receives seed' (spermatisthe) and 'as in the days of separation for her menstrual discharge'."), between("The Latin has 'having received seed'; the King James 'have conceived seed'.")],
  },
  '12:3': {
   'received': "On the eighth day the flesh of his foreskin is circumcised.",
   'explain': "The Hebrew and King James are passive; the Greek 'he shall circumcise' with an unnamed agent; the Latin 'the infant shall be circumcised'.",
   'shared': ["The eighth day.", "Circumcision.", "Of the boy."],
   'instructions': [ins(K, S, "The son was circumcised on the eighth day."), ins(C, S, "On the eighth day the flesh of his foreskin shall be circumcised."), ins(W, R, "The eighth day, when the mother's first uncleanness ends; the covenant is cut into the child as soon as his mother may hold him clean.")],
   'entries': ['term-covenant', 'abraham'],
   'lost': [loses("Hebrew passive 'shall be circumcised' is lost."), keeps("Greek 'he shall circumcise the flesh of his foreskin', an unnamed agent."), between("The Latin has 'the infant shall be circumcised'; the King James follows the Hebrew.")],
  },
  '12:4': {
   'received': "She remains thirty-three days in the blood of purification, touching nothing holy and not entering the sanctuary until her days of purification are complete.",
   'explain': "The Hebrew, Latin and King James have 'blood of purification'; the Greek 'her unclean blood', which the source calls a material difference in describing her condition, though the duration and restrictions agree.",
   'shared': ["Thirty-three days.", "Nothing holy touched.", "Not entering the sanctuary."],
   'instructions': [ins(K, S, "The mother kept from holy things thirty-three days more."), ins(W, R, "'The blood of purification': the Hebrew names the blood by what it is doing, cleansing her; the Greek names it by what it is, unclean. Forty days in all before she may come to the sanctuary.")],
   'entries': ['tabernacle'],
   'lost': BLOOD,
  },
  '12:5': {
   'received': "If she bears a female, she is unclean two weeks as in her menstruation, and remains sixty-six days in the blood of purification.",
   'explain': "All four columns agree in the doubled periods; the Greek 'twice seven days' and 'her unclean blood'.",
   'shared': ["A female born.", "Two weeks unclean.", "Sixty-six days more."],
   'instructions': [ins(K, S, "A daughter's birth doubled the mother's periods to eighty days."), ins(W, R, "Twice the time for a daughter; the law does not say why, and readers have argued since; the one thing certain is that the girl's birth is marked by more days, not fewer.")],
   'entries': [],
   'lost': BLOOD + [keeps("Greek 'twice seven days according to her menstrual discharge'.")],
  },
  '12:6': {
   'received': "When her days of purification for a son or daughter are complete, she brings to the priest at the Tent of Meeting's entrance a year-old lamb for a burnt offering and a young pigeon or turtledove for a sin offering.",
   'explain': "All four columns agree; the Greek adds 'unblemished' and has 'Tent of Testimony'; the Latin 'hand them to the priest'.",
   'shared': ["Days complete.", "A year-old lamb for burnt offering.", "A pigeon or turtledove for sin."],
   'instructions': [ins(K, S, "The mother brought a lamb and a bird at the end of her days."), ins(W, R, "A burnt offering and a sin offering for a birth; the mother comes to the door with a gift and a cleansing, the same two offerings the priests brought on their own first day.")],
   'entries': ['high-priest', 'tabernacle', 'lamb-of-god'],
   'lost': [loses("Hebrew 'Tent of Meeting' is lost."), keeps("Greek 'an unblemished year-old lamb' and 'Tent of Testimony'."), between("The Latin has 'tabernacle of the testimony … hand them to the priest'; the King James 'tabernacle of the congregation'.")],
  },
  '12:7': {
   'received': "The priest presents it before YHWH and makes atonement for her, and she is clean from the source of her blood; this is the law for a woman who bears a male or female.",
   'explain': "The Hebrew and King James have 'she shall be clean'; the Greek 'cleanse her from the fountain of her blood', the priest as agent; the Latin 'pray for her'.",
   'shared': ["Presented before YHWH.", "Atonement for her.", "Clean from her blood; the law for a mother."],
   'instructions': [ins(K, S, "The priest's atonement made the mother clean."), ins(W, R, "'Clean from the source of her blood': the mother is restored to the sanctuary, and the law calls this the law of the one who gives birth, as if birth itself were the thing being blessed.")],
   'entries': ['high-priest', 'yhwh-yahweh'],
   'lost': [loses("Hebrew 'she shall be clean from the source of her blood' is lost."), keeps("Greek 'the priest shall … cleanse her from the fountain of her blood'."), between("The Latin has 'pray for her, and thus she shall be cleansed'; the King James 'she shall be cleansed'.")],
  },
  '12:8': {
   'received': "If she cannot afford a sheep, she takes two turtledoves or two young pigeons, one for a burnt offering and one for a sin offering; the priest makes atonement, and she is clean.",
   'explain': "All four columns agree; the Greek 'if her hand cannot provide'; the Latin 'pray for her'.",
   'shared': ["If she cannot afford a sheep.", "Two birds, burnt and sin.", "Atonement; she is clean."],
   'instructions': [ins(K, S, "A poor mother brought two birds instead of a lamb."), ins(W, R, "Two birds for the poor mother; the law of chapter 5 reaches the lying-in room, and the Gospel will remember a mother who brought the birds.")],
   'entries': ['high-priest', 'mary-mother-of-jesus'],
   'lost': [keeps("Greek 'If her hand cannot provide enough for a lamb'."), between("The Latin has 'If her means are insufficient … The priest shall pray for her'; the King James 'if she be not able to bring a lamb'.")],
  },
 },
}
