# Study prose for Genesis 45 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 45,
 'chapterNote': (
  "Joseph makes himself known: “I am Joseph,” the theology of the sale (“God sent me ahead of you”), the invitation to Goshen, Pharaoh’s welcome, the wagons, "
  "and Jacob’s revival. The columns agree; the Hebrew keeps “could no longer restrain himself,” “to preserve life … a great deliverance,” “lord of all Egypt,” Goshen, "
  "“your household … impoverished,” “your households” in 45:18, Joseph “commanded” by Pharaoh, “the best of all the land,” three hundred pieces of silver, female "
  "donkeys with “grain, bread and provisions,” “do not quarrel,” “his heart grew numb,” and “Enough!” The Greek keeps “could no longer bear the presence,” “a remnant "
  "… to nourish a great remnant,” “like a father to Pharaoh,” “Gesem of Arabia,” “your sons … wiped out,” “your possessions,” Pharaoh telling Joseph to “give this "
  "command,” “Pharaoh the king,” two robes each for the brothers and three hundred pieces of gold for Benjamin, “female mules,” “do not become angry,” “Jacob was "
  "stunned,” and “it is a great thing to me.” Two Hebrew-column renderings were corrected today. The Latin and King James follow the Hebrew; the Latin has Joseph speak "
  "“gently” and Jacob wake “as from a deep sleep.”"),
 'verses': {

 '45:1': {
  'received': "Joseph could restrain himself no longer; he sent everyone out, and no one was there when he made himself known to his brothers.",
  'explain': ("Judah’s speech breaks the mask. The Hebrew says could no longer restrain himself, hit’appeq, the verb of 43:31; the Greek could no longer bear the presence of those standing by; the Latin so that no stranger would be present."),
  'shared': ["Joseph could no longer restrain himself before all who stood by him.", "He cried, Send everyone away from me!", "No one remained when Joseph made himself known to his brothers."],
  'instructions': [ins(K, S, "Joseph cleared the room to reveal himself."), ins(W, R, "Judah’s offer to be a slave for Benjamin ends the test; Joseph could hold out against fear and guilt but not against this. Recognition in Genesis comes when a man offers himself.")],
  'entries': [],
  'lost': [between("Hebrew ve-lo-yakhol Yosef le-hit’appeq, “and Joseph could not restrain himself,” is Greek kai ouk ēdynato Iōsēph anechesthai pantōn tōn parestēkotōn autō, “and Joseph could not bear all those standing by him”; Latin “could no longer restrain himself with so many standing before him”; King James “could not refrain himself.”")]},

 '45:2': {
  'received': "He wept aloud; the Egyptians heard, and Pharaoh’s house heard.",
  'explain': ("The third weeping, and loud; the palace hears. The Greek adds all and the sound reached."),
  'shared': ["He wept aloud.", "The Egyptians heard it.", "Pharaoh’s household heard it."],
  'instructions': [ins(K, S, "Joseph’s weeping was heard in the palace."), ins(W, R, "The governor who wept in a chamber weeps so the palace hears; the private grief of two chapters is let out at once, and Egypt learns its lord has a family.")],
  'entries': ['egypt'],
  'lost': [keeps("An added pantes, “all,” the Egyptians, and akouston egeneto eis ton oikon Pharaō, “it became audible in Pharaoh’s house,” in the Greek."), between("Hebrew, Latin and King James “the Egyptians and the house of Pharaoh heard.”")]},

 '45:3': {
  'received': "Joseph said, I am Joseph; is my father still alive? His brothers could not answer, so dismayed were they before him.",
  'explain': ("Two sentences: the name, and the father. The brothers are speechless. The Latin says overwhelmed with terror; the Greek troubled."),
  'shared': ["I am Joseph!", "Is my father still alive?", "His brothers could not answer him, for they were dismayed in his presence."],
  'instructions': [ins(K, S, "Joseph revealed his identity."), ins(W, R, "“I am Joseph” is followed at once by “is my father alive”; the son has already asked it twice as a stranger, and asks it now as himself. The brothers hear a dead man speak.")],
  'entries': [],
  'lost': [between("Hebrew nivhalu mi-panav, “they were dismayed before his face,” is Greek etarachthēsan gar, “for they were troubled”; Latin “overwhelmed with terror,” King James “troubled at his presence.”")]},

 '45:4': {
  'received': "Come near to me, he said; they came near. I am Joseph your brother, whom you sold into Egypt.",
  'explain': ("The second identification names the crime: whom you sold. Come near, as Judah came near. The Latin says gently."),
  'shared': ["Joseph said to his brothers, Come near to me.", "They came near.", "I am Joseph your brother, whom you sold into Egypt."],
  'instructions': [ins(K, S, "Joseph named himself as the brother they sold."), ins(W, R, "“Whom you sold into Egypt”: the sin is named in the same breath as the brotherhood, and neither cancels the other. Forgiveness begins by saying what happened.")],
  'entries': ['egypt'],
  'lost': [between("Latin “He said to them gently” adds; Hebrew geshu-na elai, “please come near to me,” Greek engisate pros me, King James “Come near to me, I pray you.”")]},

 '45:5': {
  'received': "Do not grieve or be angry with yourselves for selling me here, for God sent me ahead of you to preserve life.",
  'explain': ("Joseph’s reading of his life: God sent me. He does not say they did not sin; he says God used it. The Hebrew says to preserve life; the Greek for life; the Latin do not be afraid, for your preservation."),
  'shared': ["Do not grieve or be angry with yourselves that you sold me here.", "God sent me ahead of you.", "To preserve life."],
  'instructions': [ins(K, S, "Joseph attributed his sale to God’s saving purpose."), ins(W, R, "“God sent me before you to preserve life”: Joseph does not excuse the brothers, he outranks their deed with God’s. The theology of the whole book is in a slave-trader’s pardon.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew le-michyah, “for preservation of life,” is Greek eis zōēn, “for life”; Hebrew al-te‘atzvu, “do not grieve,” Latin “Do not be afraid”; King James “be not grieved, nor angry with yourselves.”")]},

 '45:6': {
  'received': "The famine has been two years in the land, and five more remain without ploughing or harvest.",
  'explain': ("The reckoning: year two of seven. The versions agree."),
  'shared': ["The famine has been in the land these two years.", "Five years remain.", "There will be neither ploughing nor harvest."],
  'instructions': [ins(K, S, "Five years of famine remained.")],
  'entries': [],
  'lost': [AGREE]},

 '45:7': {
  'received': "God sent me ahead to preserve you a remnant on earth and keep you alive by a great deliverance.",
  'explain': ("Remnant, she’erit, the prophets’ word; a great deliverance, peletah. The Greek says to leave a remnant of you and to nourish a great remnant; the Latin so that you may be preserved and have food."),
  'shared': ["God sent me ahead of you.", "To preserve a remnant for you on earth.", "To keep you alive through a great deliverance."],
  'instructions': [ins(K, S, "Joseph saw himself as God’s means of saving the family."), ins(W, R, "A remnant kept alive by a great deliverance: the words Isaiah will use for Israel are first used of twelve brothers and their father fed in a famine. The pattern of salvation is set in a family.")],
  'entries': ['elohim'],
  'lost': [loses("Hebrew u-le-hachayot lakhem li-fletah gedolah, “and to keep you alive for a great deliverance,” becomes Greek kai ekthrepsai hymōn kataleipsin megalēn, “and to nourish a great remnant of you”; deliverance becomes feeding."), between("Latin “so that you may be preserved upon the earth and have food to live” follows the Greek’s sense; King James “to save your lives by a great deliverance.”")]},

 '45:8': {
  'received': "So it was not you who sent me here but God, who made me a father to Pharaoh, lord of his house and ruler of all Egypt.",
  'explain': ("Not you but God: said twice. Father to Pharaoh, an Egyptian title of the vizier. The Greek says like a father; the Latin not by your plan but by God’s will."),
  'shared': ["It was not you who sent me here, but God.", "He has made me a father to Pharaoh and lord of all his house.", "Ruler over all the land of Egypt."],
  'instructions': [ins(K, S, "Joseph credited God with his position in Egypt."), ins(W, R, "“Not you, but God”: the sentence lets the brothers off and holds them responsible at once; they did send him, and God sent him. Joseph lives in both truths.")],
  'entries': ['elohim', 'egypt'],
  'lost': [keeps("Greek hōs patera Pharaō, “like a father to Pharaoh,” adds hōs, “like.”"), between("Latin “It was not by your plan but by God’s will that I was sent here” paraphrases; King James “he hath made me a father to Pharaoh.”")]},

 '45:9': {
  'received': "Hurry to my father and say: Your son Joseph says, God has made me lord of all Egypt; come down to me without delay.",
  'explain': ("The message to Jacob, in the form of a royal letter. The Greek says all the land of Egypt. The Hebrew-column rendering was corrected today."),
  'shared': ["Hurry, go up to my father.", "Thus says your son Joseph: God has made me lord of all Egypt.", "Come down to me; do not delay."],
  'instructions': [ins(C, S, "Go up to my father and tell him to come down to me."), ins(W, R, "“Thus says your son Joseph”: the formula of a king’s herald, from the boy who was told to bring his father word of his brothers. The errand of 37:14 is finished in reverse.")],
  'entries': ['elohim', 'egypt'],
  'lost': [between("Hebrew le-adon le-khol-Mitzrayim, “lord of all Egypt,” is Greek kyrion pasēs gēs Aigyptou, “lord of all the land of Egypt”; Latin “the whole land of Egypt,” King James “lord of all Egypt.”")]},

 '45:10': {
  'received': "You shall live in Goshen, near me, with your children, grandchildren, flocks, herds and all you have.",
  'explain': ("Goshen, the eastern delta, pasture for shepherds. The Greek says Gesem of Arabia, the Ptolemaic name for the eastern nome."),
  'shared': ["You will live in the land of Goshen and be near me.", "You, your children and grandchildren.", "Your flocks, your herds and all you have."],
  'instructions': [ins(K, S, "Joseph offered Goshen to his family."), ins(W, R, "Goshen, near me: Joseph places his father where he can see him, and the land of Israel’s four hundred years is chosen as a son’s convenience.")],
  'entries': ['egypt'],
  'lost': [keeps("Greek en gē Gesem Arabias, “in the land of Gesem of Arabia,” adds the regional name to Hebrew be-eretz Goshen."), between("Latin and King James “the land of Goshen.”")]},

 '45:11': {
  'received': "I will provide for you there through the five years of famine, lest you, your household and all you have come to poverty.",
  'explain': ("The Hebrew says household, impoverished; the Greek sons, wiped out; the Latin perish."),
  'shared': ["I will provide for you there.", "Five years of famine remain.", "So you, your household and all you have will not be impoverished."],
  'instructions': [ins(K, S, "Joseph promised to feed his family through the famine.")],
  'entries': [],
  'lost': [between("Hebrew u-vetekha … pen tivvaresh, “and your household … lest you be impoverished,” is Greek kai hoi huioi sou … hina mē ektribēte, “and your sons … lest you be wiped out”; Latin “lest you perish, and your household,” King James “thy household … come to poverty.”")]},

 '45:12': {
  'received': "Your eyes and my brother Benjamin’s see that it is my own mouth speaking to you.",
  'explain': ("My own mouth: in Hebrew, without the interpreter. Benjamin named as witness. The versions agree."),
  'shared': ["Your eyes see.", "The eyes of my brother Benjamin see.", "It is my own mouth that speaks to you."],
  'instructions': [ins(K, S, "Joseph offered his own speech as proof."), ins(W, R, "“My mouth speaks to you”: no interpreter now. The Hebrew the brothers spoke freely before him in 42:23 is the proof he gives them, and the language is the recognition.")],
  'entries': [],
  'lost': [AGREE]},

 '45:13': {
  'received': "Tell my father of all my glory in Egypt and all you have seen, and hurry and bring him down.",
  'explain': ("Glory, kavod, as in 31:1, wealth and rank. The versions agree."),
  'shared': ["Tell my father all my glory in Egypt.", "Tell him all you have seen.", "Hurry and bring my father down here."],
  'instructions': [ins(C, S, "Tell my father and bring him down here."), ins(W, R, "He wants his father told of his glory; the boy who told his dreams has not wholly left the man, and the wish is forgivable.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '45:14': {
  'received': "He fell on Benjamin’s neck and wept, and Benjamin wept on his neck.",
  'explain': ("The two sons of Rachel. Esau fell on Jacob’s neck in 33:4. The versions agree."),
  'shared': ["He fell on the neck of his brother Benjamin.", "He wept.", "Benjamin wept on his neck."],
  'instructions': [ins(K, S, "Joseph and Benjamin wept together."), ins(W, R, "Rachel’s two sons, who never knew each other, weep on one another’s necks; the mother who died asking for a second son has her two together at last.")],
  'entries': [],
  'lost': [AGREE]},

 '45:15': {
  'received': "He kissed all his brothers and wept over them; after that they talked with him.",
  'explain': ("Then speech returns. The Latin says dared to speak."),
  'shared': ["He kissed all his brothers.", "He wept over them.", "After that his brothers spoke with him."],
  'instructions': [ins(K, S, "The brothers were reconciled with Joseph."), ins(W, R, "“After that his brothers talked with him”: they could not speak peaceably to him in 37:4, and now, after his tears, they can. The kiss undoes the silence of twenty-two years.")],
  'entries': [],
  'lost': [between("Latin “After this they dared to speak to him” adds the daring; Hebrew, Greek and King James “after that his brethren talked with him.”")]},

 '45:16': {
  'received': "The news reached Pharaoh’s house, Joseph’s brothers have come, and Pharaoh and his servants were pleased.",
  'explain': ("The court approves. The Greek says spread, rejoiced; the Latin the king’s court."),
  'shared': ["The report reached Pharaoh’s house.", "Joseph’s brothers have come.", "Pharaoh and his servants were pleased."],
  'instructions': [ins(K, S, "Pharaoh welcomed news of Joseph’s brothers.")],
  'entries': [],
  'lost': [between("Hebrew va-yitav be-ene Par‘oh, “and it was good in Pharaoh’s eyes,” is Greek echarē de Pharaō, “and Pharaoh rejoiced”; Latin “Pharaoh and his whole household rejoiced,” King James “it pleased Pharaoh well.”")]},

 '45:17': {
  'received': "Pharaoh told Joseph: say to your brothers, load your animals and go to Canaan;",
  'explain': ("Pharaoh himself arranges the move. The Greek says transport; the Hebrew beasts."),
  'shared': ["Pharaoh said to Joseph, Tell your brothers.", "Load your animals.", "Go to the land of Canaan."],
  'instructions': [ins(K, S, "Pharaoh ordered the family brought to Egypt.")],
  'entries': ['canaan'],
  'lost': [between("Hebrew be‘irkhem, “your beasts,” is Greek ta poreia hymōn, “your transport”; Latin “your animals,” King James “your beasts.”")]},

 '45:18': {
  'received': "take your father and households and come to me; I will give you the good of Egypt and you shall eat the fat of the land.",
  'explain': ("The fat of the land, chelev: the best. The Hebrew says households; the Greek possessions, the marrow; the Latin kindred, the richest."),
  'shared': ["Take your father and your households and come to me.", "I will give you the good things of Egypt.", "You will eat the fat of the land."],
  'instructions': [ins(K, S, "Pharaoh promised Egypt’s best to Jacob’s house."), ins(W, R, "“The fat of the land”: Egypt offers Israel its best, and Israel will later be enslaved in the same land. The welcome is sincere and the future is not in Pharaoh’s gift.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew u-vatekhem, “and your households,” is Greek kai ta hyparchonta hymōn, “and your possessions”; Hebrew chelev ha-aretz, “the fat of the land,” is Greek ton myelon tēs gēs, “the marrow of the land”; Latin “your father and kindred … the richest of the land,” King James “your households … the fat of the land.”")]},

 '45:19': {
  'received': "You are commanded: take wagons from Egypt for your children and wives, bring your father and come.",
  'explain': ("Wagons, agalot, Egyptian technology, the proof that will convince Jacob. The Hebrew addresses Joseph, you are commanded; the Greek tells him to give the command; the Latin hurry to come."),
  'shared': ["Take wagons from Egypt.", "They are for your little ones and your wives.", "Bring your father and come."],
  'instructions': [ins(K, S, "Pharaoh provided wagons for the migration."), ins(W, R, "Pharaoh’s wagons carry Israel into Egypt; the state’s kindness is the beginning of the sojourn Abraham was told of in 15:13.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew ve-attah tzuvveitah zot asu, “and you are commanded, do this,” addressed to Joseph, is Greek sy de enteilai tauta, “and you, command these things,” Joseph to issue the order; Latin “Command them also to take wagons … hurry to come as soon as possible”; King James “Now thou art commanded, this do ye.”")]},

 '45:20': {
  'received': "Do not worry about your goods, for the best of all Egypt is yours.",
  'explain': ("Leave the furniture; Egypt will replace it. The Hebrew says the best of all the land; the Greek all the good things of Egypt; the Latin leave none behind. The Hebrew-column rendering was corrected today."),
  'shared': ["Do not be concerned about your belongings.", "The best of all the land of Egypt.", "It is yours."],
  'instructions': [ins(K, S, "Pharaoh told them not to spare their possessions.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew ki-tuv kol-eretz Mitzrayim lakhem hu, “for the best of all the land of Egypt is yours,” is Greek ta gar panta agatha Aigyptou hymin estai, “for all the good things of Egypt will be yours”; Latin “Leave none of your household goods behind, for all Egypt’s riches shall be yours”; King James “the good of all the land of Egypt is yours.”")]},

 '45:21': {
  'received': "The sons of Israel did so; Joseph gave them wagons by Pharaoh’s order and provisions for the way.",
  'explain': ("The Greek adds the king. The versions agree."),
  'shared': ["The sons of Israel did so.", "Joseph gave them wagons according to Pharaoh’s word.", "He gave them provisions for the journey."],
  'instructions': [ins(K, S, "The brothers were equipped for the journey.")],
  'entries': [],
  'lost': [keeps("An added tou basileōs, “the king,” after Pharaoh in the Greek."), between("Hebrew, Latin and King James “Pharaoh.”")]},

 '45:22': {
  'received': "He gave each a change of clothing, but Benjamin three hundred pieces of silver and five changes.",
  'explain': ("Clothing again, from the man stripped of his coat; and Benjamin favoured fivefold, as at the table. The Hebrew says changes of clothing, silver; the Greek two robes each, gold; the Latin two robes, silver, five excellent robes."),
  'shared': ["He gave each of them changes of clothing.", "To Benjamin he gave three hundred pieces of silver.", "And five changes of clothing."],
  'instructions': [ins(K, S, "Joseph gave gifts, with Benjamin favoured."), ins(W, R, "Joseph clothes the brothers who stripped him and loads Benjamin with five garments; the favouritism of their father is repeated openly, and tested one last time, and this time it holds.")],
  'entries': [],
  'lost': [loses("Hebrew chalifot semalot, “changes of garments,” becomes Greek dissas stolas, “two robes each”; Hebrew shelosh me’ot kesef, “three hundred of silver,” becomes triakosious chrysous, “three hundred gold pieces.”"), between("Latin “two robes … three hundred silver pieces and five excellent robes” mixes; King James “changes of raiment … three hundred pieces of silver.”")]},

 '45:23': {
  'received': "To his father he sent ten donkeys laden with Egypt’s goods and ten she-asses with grain, bread and food for the journey.",
  'explain': ("Gifts for the father, as Jacob sent gifts to the man. The Hebrew says she-asses, grain, bread, provisions; the Greek female mules, bread; the Latin wheat and bread, the same money and clothing."),
  'shared': ["To his father he sent likewise.", "Ten male donkeys loaded with Egypt’s good things.", "Ten female donkeys loaded with grain, bread and provisions for his father’s journey."],
  'instructions': [ins(K, S, "Joseph sent provisions and gifts to Jacob."), ins(W, R, "Jacob sent balm and honey to the man in Egypt; the man sends back donkeys laden with Egypt. The father’s gift is answered tenfold by the son he does not know he gave it to.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew atonot, “female donkeys,” is Greek hēmionous, “female mules”; Hebrew bar va-lechem u-mazon, “grain and bread and food,” is Greek artous, “bread,” alone; Latin “wheat and bread,” King James “corn and bread and meat.”")]},

 '45:24': {
  'received': "He sent his brothers off, saying, Do not quarrel on the way.",
  'explain': ("Tirgezu, be agitated, quarrel, or fear; the brothers have a long road to talk over who was to blame. The Greek and Latin say do not become angry."),
  'shared': ["He sent his brothers away.", "They departed.", "He said, Do not quarrel on the way."],
  'instructions': [ins(C, S, "Do not quarrel on the way."), ins(W, R, "“Fall not out by the way”: Joseph knows the road home will be spent assigning blame, and forbids it. The forgiven are told not to unforgive one another.")],
  'entries': [],
  'lost': [between("Hebrew al-tirgezu ba-darekh, “do not be agitated on the way,” is Greek mē orgizesthe en tē hodō, “do not be angry on the way”; Latin “Do not become angry on the way,” King James “See that ye fall not out by the way.”")]},

 '45:25': {
  'received': "They went up from Egypt to their father Jacob in Canaan.",
  'explain': ("The versions agree."),
  'shared': ["They went up out of Egypt.", "They came to the land of Canaan.", "They came to their father Jacob."],
  'instructions': [ins(K, S, "The brothers returned to Jacob.")],
  'entries': ['jacob', 'canaan', 'egypt'],
  'lost': [AGREE]},

 '45:26': {
  'received': "They told him, Joseph is still alive and rules all Egypt. His heart went numb; he did not believe them.",
  'explain': ("The news, and disbelief; the heart stops, va-yafog. The Greek says your son Joseph, Jacob was stunned; the Latin as though awakening from a deep sleep."),
  'shared': ["Joseph is still alive, and he rules all Egypt!", "His heart grew numb.", "He did not believe them."],
  'instructions': [ins(K, S, "Jacob could not believe Joseph lived."), ins(W, R, "The sons who told him Joseph was dead tell him Joseph lives, and he does not believe them; twenty-two years of a lie have made the truth incredible from their mouths.")],
  'entries': ['jacob', 'egypt'],
  'lost': [between("Hebrew va-yafog libbo, “and his heart grew numb,” is Greek kai exestē hē dianoia Iakōb, “and Jacob’s mind was astonished,” with ho huios sou, “your son,” added; Latin “as though awakening from a deep sleep”; King James “Jacob’s heart fainted.”")]},

 '45:27': {
  'received': "They told him all Joseph had said, and when he saw the wagons Joseph sent, the spirit of their father Jacob revived.",
  'explain': ("The wagons convince where words did not; Egyptian wagons are not a story. The Hebrew says revived, va-techi; the Greek was rekindled."),
  'shared': ["They told him all Joseph had said to them.", "He saw the wagons Joseph had sent to carry him.", "The spirit of Jacob their father revived."],
  'instructions': [ins(K, S, "The wagons convinced Jacob and revived him."), ins(W, R, "“The spirit of Jacob revived”: life comes back into the old man at the sight of wagons. The reader has waited since 37:35 for this sentence.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew va-techi ruach Ya‘aqov, “and the spirit of Jacob lived,” is Greek anezōpyrēsen to pneuma Iakōb, “the spirit of Jacob was rekindled”; Latin “his spirit revived,” King James “the spirit of Jacob their father revived.”")]},

 '45:28': {
  'received': "Israel said, Enough! My son Joseph is still alive; I will go and see him before I die.",
  'explain': ("Israel, the name of strength, returns with the news. Rav, enough, much. The Greek says it is a great thing to me if; the Latin it is enough for me if."),
  'shared': ["Israel said.", "Enough! Joseph my son is still alive.", "I will go and see him before I die."],
  'instructions': [ins(K, S, "Jacob resolved to go to Joseph."), ins(W, R, "“Enough; Joseph my son is yet alive”: the man who said he would go down to Sheol mourning will go down to Egypt rejoicing. The name Israel is used for the first time since the famine, and the father is a wrestler again.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew rav od-Yosef beni chai, “much! Joseph my son still lives,” is Greek mega moi estin, ei eti Iōsēph ho huios mou zē, “it is a great thing to me, if my son Joseph still lives”; Latin “It is enough for me if my son Joseph is still alive,” King James “It is enough; Joseph my son is yet alive.”")]},
 }
}
