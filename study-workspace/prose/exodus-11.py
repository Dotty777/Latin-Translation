K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'exodus', 'chapter': 11,
 'chapterNote': "One more plague is announced. YHWH tells Moses that after it Pharaoh will drive Israel out, and that the people are to ask their neighbours for silver and gold; Moses is great in Egypt's eyes. Moses then delivers the warning of the death of every firstborn at midnight, from Pharaoh's to the slave girl's and the cattle's, with a great cry in Egypt and not a dog growling in Israel, and leaves Pharaoh in fierce anger. The chapter closes with the summary that Pharaoh would not listen so that the wonders might multiply. The Greek adds 'with everything' (11:1), 'secretly' and 'clothing' (11:2), 'and they lent to them' and Pharaoh among those before whom Moses was great (11:3), and 'greatly' with God as agent of the multiplying (11:9); it has 'enter' for 'go out' (11:4) and 'growl' for 'sharpen its tongue' (11:7). The Latin moves Moses' angry exit from 11:8 to the start of 11:9 and has 'the wonders that are written' in 11:10.",
 'verses': {
  '11:1': {
   'received': "YHWH tells Moses he will bring one more plague on Pharaoh and Egypt; afterward Pharaoh will let them go, and will drive them out completely.",
   'explain': "The Hebrew and King James have 'drive you out completely' or 'altogether'. The Greek adds 'with everything', making the completeness of the departure explicit; the source notes this does not imply the Hebrew lets Pharaoh keep anything. The Latin has 'compel you to depart'.",
   'shared': ["One more plague is coming.", "Pharaoh will let them go.", "He will drive them out completely."],
   'instructions': [ins(K, S, "YHWH would bring one more plague, after which Pharaoh would drive Israel out completely."), ins(W, R, "'One more': the count is nearly done, and God tells Moses so. The man who was told the heart would be hardened is now told when it will break.")],
   'entries': ['yhwh-yahweh', 'moses', 'plague-10'],
   'lost': [keeps("An added 'with everything' after 'altogether'."), between("The Latin has 'compel you to depart'; the King James 'thrust you out hence altogether'.")],
  },
  '11:2': {
   'received': "Moses is to speak in the people's hearing, that every man ask his neighbour and every woman hers for articles of silver and gold.",
   'explain': "The Hebrew, Latin and King James have silver and gold only. The Greek adds 'secretly' and 'clothing'; the source notes clothing appears in 12:35 and may be coordinated from there, but 'secretly' is unexplained. The King James has 'borrow'.",
   'shared': ["Moses speaks to the people.", "Each is to ask a neighbour.", "Silver and gold are asked for."],
   'instructions': [ins(K, S, "The people were to ask their neighbours for silver and gold."), ins(C, S, "Speak in the people's hearing."), ins(W, R, "Before the last plague comes the instruction about wages; the asking is to happen before the death, when the Egyptians still think they are being generous.")],
   'entries': ['moses'],
   'lost': [keeps("An added 'secretly' and 'and for clothing'."), between("The Latin has 'tell all the people' and 'friend'; the King James 'borrow'.")],
  },
  '11:3': {
   'received': "YHWH gives the people favour in the Egyptians' sight; and the man Moses is very great in Egypt, in the sight of Pharaoh's servants and the people.",
   'explain': "The Hebrew and King James have the favour given and Moses great before Pharaoh's servants and the people. The Greek adds 'and they lent to them' and names Pharaoh himself among those who saw Moses' greatness; the Latin puts the favour in the future, 'the Lord will give'. The source notes the lending clause sets no repayment terms.",
   'shared': ["YHWH gives the people favour with the Egyptians.", "Moses is very great in Egypt.", "Pharaoh's servants and the people see it."],
   'instructions': [ins(K, S, "YHWH gave Israel favour with the Egyptians, and Moses was very great in Egypt."), ins(W, R, "'The man Moses': the narrator steps back to call him a man, at the moment Egypt is most tempted to think him more; greatness is recorded and kept human.")],
   'entries': ['yhwh-yahweh', 'moses', 'term-favor', 'egypt'],
   'lost': [loses("Hebrew 'in the land of Egypt' is lost."), keeps("An added 'and they lent to them', and 'Pharaoh' among those before whom Moses was great."), between("The Latin has the favour as future, 'will give'; the King James follows the Hebrew.")],
  },
  '11:4': {
   'received': "Moses says, thus says YHWH: about midnight I will go out into the midst of Egypt.",
   'explain': "The Hebrew, Latin and King James have God 'going out' into Egypt; the Greek 'enter the midst of Egypt'. The Latin has 'he said' without naming Moses and 'at midnight'.",
   'shared': ["Moses speaks for YHWH.", "The time is about midnight.", "God will pass through Egypt."],
   'instructions': [ins(K, S, "Moses announced that about midnight YHWH would go out into the midst of Egypt."), ins(W, R, "God himself goes out this time; no staff, no hand, no wind. The tenth plague is the one he does in person.")],
   'entries': ['moses', 'yhwh-yahweh', 'plague-10'],
   'lost': [loses("Hebrew 'go out into the midst of Egypt' is lost."), keeps("Greek 'enter the midst of Egypt'."), between("The Latin has 'go out into Egypt' and omits Moses' name; the King James follows the Hebrew.")],
  },
  '11:5': {
   'received': "Every firstborn in Egypt will die, from Pharaoh's who sits on his throne to the slave girl's behind the handmill, and every firstborn of the livestock.",
   'explain': "All four columns agree, from throne to mill to beast. The Greek has 'beside the mill' and 'every beast'; the source keeps 'female slave' as the labour setting without a legal category.",
   'shared': ["Every firstborn in Egypt will die.", "From Pharaoh's to the slave girl's.", "The livestock's firstborn too."],
   'instructions': [ins(K, S, "Every firstborn in Egypt would die, from Pharaoh's on the throne to the slave girl's at the mill and the cattle's."), ins(W, R, "Throne to handmill: the plague ignores rank entirely, and the slave girl's son dies for Pharaoh's refusal as surely as Pharaoh's does.")],
   'entries': ['plague-10', 'egypt'],
   'lost': [AGREE],
  },
  '11:6': {
   'received': "There will be a great cry throughout Egypt, such as there has never been and never will be again.",
   'explain': "All four columns agree.",
   'shared': ["A great cry throughout Egypt.", "Never before.", "Never again."],
   'instructions': [ins(K, S, "A great cry would go through Egypt such as never was or would be."), ins(W, R, "Israel's cry rose to God in chapter 2; now Egypt's cry is foretold, and the two cries measure each other across the book.")],
   'entries': ['plague-10', 'egypt'],
   'lost': [AGREE],
  },
  '11:7': {
   'received': "But against any of the sons of Israel, human or animal, not a dog will sharpen its tongue, so that Pharaoh may know that YHWH distinguishes between Egypt and Israel.",
   'explain': "The Hebrew has 'sharpen its tongue', a vivid image; the King James 'move his tongue'; the Greek specifies 'growl'; the Latin 'utter a sound'. The Greek and Latin add 'how marvellously' or 'with what a wonder' to the distinguishing.",
   'shared': ["No harm touches Israel, human or animal.", "Not even a dog's tongue moves.", "YHWH distinguishes Egypt from Israel."],
   'instructions': [ins(K, S, "Not a dog would sharpen its tongue against Israel, that Pharaoh might know YHWH distinguished them from Egypt."), ins(W, R, "In Egypt a cry, in Israel not even a dog's growl; the silence in Goshen is as much a sign as the wailing beyond it.")],
   'entries': ['yhwh-yahweh', 'plague-10'],
   'lost': [loses("Hebrew 'sharpen its tongue' is lost."), keeps("Greek 'growl with its tongue' and 'how marvellously the Lord distinguishes'."), between("The Latin has 'utter a sound' and 'with what a wonder'; the King James 'move his tongue'.")],
  },
  '11:8': {
   'received': "All Pharaoh's servants will come down and bow to Moses, saying, 'Go out, you and all the people at your feet'; after that he will go out; and Moses leaves Pharaoh in fierce anger.",
   'explain': "The Hebrew, Greek and King James end with Moses' exit in anger; the Latin moves it to the start of 11:9 and has 'we will depart'. The Greek explains 'at your feet' as 'whom you lead' and names Moses. The source notes the bowing is homage, not worship.",
   'shared': ["Pharaoh's servants will bow to Moses.", "They will beg Israel to go.", "Then Moses will go out."],
   'instructions': [ins(K, S, "Pharaoh's servants would bow to Moses and beg him to go, and Moses left Pharaoh in fierce anger."), ins(W, R, "Moses, who was told he would die if he saw Pharaoh's face, says that face will one day beg him; he leaves angry, and the anger is the last human emotion before the midnight.")],
   'entries': ['moses'],
   'lost': [loses("Hebrew 'the people at your feet' is lost."), keeps("Greek 'whom you lead' and Moses named in the exit."), between("The Latin moves the angry exit to 11:9 and has 'we will depart'; the King James follows the Hebrew.")],
  },
  '11:9': {
   'received': "YHWH tells Moses that Pharaoh will not listen, so that his wonders may multiply in Egypt.",
   'explain': "The Hebrew and King James have 'that my wonders may be multiplied'. The Greek has 'that I may greatly multiply my signs and wonders', God as agent; the Latin 'that many signs may be done' and opens with Moses' angry exit carried from 11:8.",
   'shared': ["YHWH speaks to Moses.", "Pharaoh will not listen.", "The wonders multiply in Egypt."],
   'instructions': [ins(K, S, "YHWH said Pharaoh would not listen so that his wonders might multiply in Egypt."), ins(W, R, "The summary looks back over nine plagues and calls the refusal purposeful; God's wonders needed Pharaoh's no, and got it.")],
   'entries': ['yhwh-yahweh', 'moses', 'egyptian-plagues'],
   'lost': [loses("Hebrew 'that my wonders may multiply', passive, is lost."), keeps("Greek 'that I may greatly multiply my signs and wonders', God as agent."), between("The Latin prefixes the angry exit and has 'many signs may be done'; the King James follows the Hebrew.")],
  },
  '11:10': {
   'received': "Moses and Aaron do all these wonders before Pharaoh; YHWH makes his heart firm, and he does not let the sons of Israel go from his land.",
   'explain': "All four columns keep the divine hardening. The Greek has 'all these signs and wonders in the land of Egypt' and 'was unwilling to send'; the Latin 'all the wonders that are written'; the Hebrew 'made firm', the others 'hardened'.",
   'shared': ["Moses and Aaron did the wonders before Pharaoh.", "YHWH hardened his heart.", "He did not let Israel go."],
   'instructions': [ins(K, S, "Moses and Aaron did all the wonders, YHWH made Pharaoh's heart firm, and he did not let Israel go."), ins(W, R, "The sentence that has ended every plague ends the whole series; the next chapter will not end that way, and the reader knows it.")],
   'entries': ['moses', 'yhwh-yahweh', 'egyptian-plagues'],
   'lost': [loses("Hebrew 'all these wonders' and 'made firm' are lost."), keeps("Greek 'all these signs and wonders in the land of Egypt' and 'was unwilling to send'."), between("The Latin has 'the wonders that are written'; the King James 'hardened'.")],
  },
 },
}
