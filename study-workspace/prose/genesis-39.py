# Study prose for Genesis 39 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 39,
 'chapterNote': (
  "Joseph in Potiphar’s house: prosperity, the wife’s advances, the refusal, the false charge, and prison, where the Lord is with him again. The columns agree; "
  "the Hebrew keeps Potiphar as “captain of the guard,” “served him,” “he is no greater in this house than I,” “his garment” in the singular throughout, the wife’s "
  "accusation without quoted speech, “the prison” and “he remained there,” and “he was the doer of it.” The Greek keeps “eunuch, the chief cook,” “pleased him,” "
  "“very beautiful in appearance,” a conditional running across 39:8–9, “nothing in this house is above me,” “his garments” and “her hands” in the plural, an added "
  "“Sleep with me” and “I will sleep with you” inside the wife’s accusations, “the fortress,” and “everything was in Joseph’s charge.” The Latin and King James follow "
  "the Hebrew; the Latin adds that the master was “too ready to believe” his wife and that she kept the cloak “as proof.”"),
 'verses': {

 '39:1': {
  'received': "Joseph was brought down to Egypt and bought from the Ishmaelites by Potiphar, Pharaoh’s officer, captain of the guard, an Egyptian.",
  'explain': ("The story resumes from 37:36. The Hebrew says officer, captain of the guard; the Greek eunuch, chief cook; the Latin court official, commander of the army."),
  'shared': ["Joseph was brought down to Egypt.", "Potiphar, an officer of Pharaoh, captain of the guard, an Egyptian, bought him.", "He bought him from the Ishmaelites who had brought him down."],
  'instructions': [ins(K, S, "Potiphar bought Joseph in Egypt."), ins(W, R, "Brought down, bought, an Egyptian master: three humiliations in a verse, and the next verse says the Lord was with him. The descent and the presence go together.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew seris Par‘oh sar ha-tabbachim, “officer of Pharaoh, chief of the guard,” is Greek ho spadōn Pharaō, archimageiros, “Pharaoh’s eunuch, chief cook”; Latin “court official and commander of the army,” King James “officer … captain of the guard.”")]},

 '39:2': {
  'received': "The Lord was with Joseph, and he prospered in his Egyptian master’s house.",
  'explain': ("The refrain of the chapter, four times: the Lord was with Joseph. The Latin says prospered in everything, his master’s house."),
  'shared': ["The Lord was with Joseph.", "He was a successful man.", "He lived in the house of his Egyptian master."],
  'instructions': [ins(K, S, "God prospered Joseph as a slave."), ins(W, R, "“The Lord was with Joseph” in a slave’s quarters; the promise to the fathers travels into Egypt in the person of a bought boy.")],
  'entries': ['yhwh-yahweh', 'egypt'],
  'lost': [AGREE]},

 '39:3': {
  'received': "His master saw that the Lord was with him and prospered all he did.",
  'explain': ("The pagan sees what Joseph’s brothers did not. The Hebrew says saw; the Greek knew; the Latin knew very well, directed."),
  'shared': ["His master saw that the Lord was with him.", "The Lord made everything he did prosper.", "It was in his hands."],
  'instructions': [ins(K, S, "Potiphar recognised God’s blessing on Joseph."), ins(W, R, "Potiphar reads the Lord’s presence off Joseph’s work; Abimelech and Laban did the same with his fathers. The blessing is legible to outsiders.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew va-yar, “and he saw,” is Greek ēdei, “knew”; Latin “knew very well … directed everything,” King James “saw … made all that he did to prosper.”")]},

 '39:4': {
  'received': "Joseph found favour, served him, and was set over the household with everything in his charge.",
  'explain': ("From slave to steward. The Hebrew says served him; the Greek pleased him; the Latin ministered to him, governed the house."),
  'shared': ["Joseph found favour in his master’s sight.", "He served him.", "He was appointed over the household and everything was entrusted to him."],
  'instructions': [ins(K, S, "Potiphar made Joseph steward of his house."), ins(W, R, "Everything in Joseph’s hand: the phrase will be said of Pharaoh’s Egypt. The dream of rule begins to come true in a slave’s promotion.")],
  'entries': [],
  'lost': [between("Hebrew va-yesharet oto, “and he served him,” is Greek euērestēsen de autō, “and he pleased him”; Latin “ministered to him,” King James “served him.”")]},

 '39:5': {
  'received': "From then the Lord blessed the Egyptian’s house for Joseph’s sake, in house and field.",
  'explain': ("Blessing through the patriarch to his host, as to Laban. The Latin compresses."),
  'shared': ["He appointed him over his house and all he owned.", "The Lord blessed the Egyptian’s house for Joseph’s sake.", "The blessing of the Lord was on all he had, in house and field."],
  'instructions': [ins(K, S, "God blessed Potiphar’s house through Joseph."), ins(W, R, "“For Joseph’s sake”: the blessing of nations in Abraham’s seed, 12:3, reaches an Egyptian officer’s barns. The promise works even in slavery.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Latin “The Lord blessed the Egyptian’s house because of Joseph and multiplied all his possessions” drops the opening clause; Hebrew, Greek and King James keep “from the time that he had made him overseer.”")]},

 '39:6': {
  'received': "He left everything to Joseph and thought of nothing but his food. Joseph was handsome in form and face.",
  'explain': ("The master’s trust, and Joseph’s beauty, which introduces the trouble; the phrase is Rachel’s in 29:17. The Greek says very beautiful; the Latin omits the first clause."),
  'shared': ["He left all he had in Joseph’s hands.", "He concerned himself with nothing but the bread he ate.", "Joseph was handsome in form and appearance."],
  'instructions': [ins(K, S, "Joseph was trusted and handsome."), ins(W, R, "His mother’s beauty in a slave; the gift that won Jacob’s love for Rachel draws another’s eye to her son, and the chapter turns on it.")],
  'entries': [],
  'lost': [keeps("Greek kalos tō eidei kai hōraios tē opsei sphodra, “handsome in form and very beautiful in appearance,” adds sphodra, “very.”"), between("Latin drops “he left all he had in Joseph’s hand”; King James “a goodly person, and well favoured.”")]},

 '39:7': {
  'received': "After this his master’s wife eyed Joseph and said, Lie with me.",
  'explain': ("Two Hebrew words, shikhvah immi. The Latin says after many days, his mistress."),
  'shared': ["After these things.", "His master’s wife cast her eyes on Joseph.", "Lie with me."],
  'instructions': [ins(K, S, "Potiphar’s wife propositioned Joseph."), ins(W, R, "The dreamer who was hated for a coat is now wanted for his face; Joseph’s trials come from what others see in him, and he has chosen none of it.")],
  'entries': [],
  'lost': [AGREE]},

 '39:8': {
  'received': "He refused: my master has left all household matters to me and entrusted everything to me,",
  'explain': ("Joseph’s refusal, the first argument from trust. The Greek makes it a conditional, if my master…, completed in verse 9; the Latin refusing utterly the wicked deed."),
  'shared': ["He refused.", "My master leaves all household matters to me.", "He has entrusted everything he owns to my hand."],
  'instructions': [ins(K, S, "Joseph refused, citing his master’s trust."), ins(W, R, "Joseph argues from his master’s trust before he argues from God; the two reasons are one, since the trust is God’s doing.")],
  'entries': [],
  'lost': [between("Hebrew hen adoni lo-yada, “behold, my master does not know,” a statement, is Greek ei ho kyrios mou ou ginōskei, “if my master does not know,” a conditional completed in 39:9; Latin “Refusing utterly to consent to the wicked deed”; King James “my master wotteth not.”")]},

 '39:9': {
  'received': "he is no greater here than I, and has kept nothing from me but you, his wife; how could I do this great evil and sin against God?",
  'explain': ("The second argument: it is sin against God, not only against the master. The Hebrew says he is no greater in this house than I; the Greek nothing in this house is above me; the Latin my God."),
  'shared': ["He is no greater in this house than I.", "He has withheld nothing from me except you, because you are his wife.", "How could I do this great evil and sin against God?"],
  'instructions': [ins(K, S, "Joseph named adultery as sin against God."), ins(W, R, "“Sin against God” is the whole of Joseph’s ethics in four words; in a house with no altar, far from his father, the slave knows whose eye is on him.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew enennu gadol ba-bayit ha-zeh mimmenni, “he is not greater in this house than I,” is Greek ouch hyperechei en tē oikia tautē outhen emou, “nothing in this house is above me”; Latin “sin against my God,” Hebrew, Greek and King James “against God.”")]},

 '39:10': {
  'received': "Though she spoke to him daily, he would not lie with her or be with her.",
  'explain': ("Persistence met with persistence. The Latin says troubled the young man, refused the sexual wrongdoing."),
  'shared': ["She spoke to Joseph day after day.", "He would not listen to her.", "He would not lie beside her or be with her."],
  'instructions': [ins(K, S, "Joseph resisted repeated temptation."), ins(W, R, "Day after day: the refusal is not one heroic moment but a habit kept under pressure, which is what chastity usually is.")],
  'entries': [],
  'lost': [between("Hebrew lishkav etzlah lihyot immah, “to lie beside her, to be with her,” is Greek koimēthēnai met’ autēs tou syngenesthai autē, “to sleep with her and have relations with her”; Latin “he refused the sexual wrongdoing,” King James “to lie by her, or to be with her.”")]},

 '39:11': {
  'received': "One day he came into the house to work and none of the men were inside.",
  'explain': ("The opportunity. The Greek names Joseph; the Latin without anyone present."),
  'shared': ["One day he entered the house to do his work.", "None of the household men.", "They were not inside."],
  'instructions': [ins(K, S, "Joseph was alone in the house with the wife.")],
  'entries': [],
  'lost': [between("Greek adds Iōsēph as subject; Latin “without anyone present” for Hebrew ve-en ish me-anshe ha-bayit sham ba-bayit, “and no man of the men of the house was there in the house”; King James follows the Hebrew.")]},

 '39:12': {
  'received': "She caught his garment, saying, Lie with me; he left it in her hand and fled outside.",
  'explain': ("A second garment lost; the coat went to the brothers, the robe to the wife. The Hebrew says garment, hand, singular; the Greek clothes, hands, plural; the Latin the edge of his garment, cloak."),
  'shared': ["She caught him by his garment, saying, Lie with me.", "He left his garment in her hand.", "He fled outside."],
  'instructions': [ins(K, S, "Joseph fled, leaving his garment behind."), ins(W, R, "Joseph loses a garment to escape sin as he lost one to his brothers’ hate; both times the cloth is used to lie about him, and both times God uses the lie.")],
  'entries': [],
  'lost': [between("Hebrew be-vigdo … bigdo be-yadah, “by his garment … his garment in her hand,” singular, is Greek tōn himatiōn autou … ta himatia autou en tais chersin autēs, plural; Latin “the edge of his garment … his cloak,” King James “his garment … in her hand.”")]},

 '39:13': {
  'received': "When she saw he had left his garment and fled,",
  'explain': ("The Latin says and that she had been rejected; the Greek garments, hands."),
  'shared': ["She saw.", "He had left his garment in her hand.", "He had fled outside."],
  'instructions': [ins(K, S, "The wife held the evidence she would misuse.")],
  'entries': [],
  'lost': [between("Latin “and that she had been rejected” adds a motive; Hebrew, Greek and King James state only what she saw; Greek plural garments and hands.")]},

 '39:14': {
  'received': "she called the men of the house: See, he brought a Hebrew to mock us; he came to lie with me, and I screamed.",
  'explain': ("Rejection turned to accusation, and the master blamed too, he brought. The Hebrew says a Hebrew man, came in to lie with me; the Greek a Hebrew servant, and quotes him, Sleep with me."),
  'shared': ["She called the men of the house.", "See, he has brought us a Hebrew to mock us.", "He came in to lie with me, and I cried out loudly."],
  'instructions': [ins(K, S, "Potiphar’s wife falsely accused Joseph."), ins(W, R, "Her words to him are put in his mouth; the lie is the truth reversed, and the household hears it from the one with the cloak.")],
  'entries': [],
  'lost': [keeps("Greek paida Hebraion, “a Hebrew servant,” for Hebrew ish Ivri, “a Hebrew man,” and an added legōn, koimēthēti met’ emou, “saying, Sleep with me,” as quoted speech."), between("Latin “a Hebrew man … came in to lie with me” and King James follow the Hebrew.")]},

 '39:15': {
  'received': "When he heard me scream he left his garment beside me and fled outside.",
  'explain': ("Her version makes the scream the cause of his flight. The Greek says garments; the Latin the cloak I was holding."),
  'shared': ["He heard me lift my voice and cry out.", "He left his garment beside me.", "He fled outside."],
  'instructions': [ins(K, S, "The wife twisted Joseph’s flight into guilt.")],
  'entries': [],
  'lost': [between("Hebrew bigdo etzli, “his garment beside me,” singular, is Greek ta himatia autou par’ emoi, plural; Latin “the cloak I was holding,” King James “his garment with me.”")]},

 '39:16': {
  'received': "She kept his garment by her until his master came home.",
  'explain': ("The evidence held. The Latin says kept the cloak as proof of her story and showed it to her husband."),
  'shared': ["She kept his garment.", "It was beside her.", "Until his master came home."],
  'instructions': [ins(K, S, "The wife kept Joseph’s garment as evidence."), ins(W, R, "A garment kept to be shown to the master of the house: the brothers kept Joseph’s coat for the same purpose. Cloth lies well in this family’s story.")],
  'entries': [],
  'lost': [between("Latin “She kept the cloak as proof of her story and showed it to her husband when he returned home” expands; Hebrew, Greek and King James “laid up his garment by her, until his lord came home.”")]},

 '39:17': {
  'received': "She told him the same: the Hebrew slave you brought us came in to mock me.",
  'explain': ("To the husband, slave, not man, and you brought. The Greek adds and said, I will sleep with you."),
  'shared': ["She told him the same story.", "The Hebrew slave you brought us came in to me.", "He came to mock me."],
  'instructions': [ins(K, S, "The wife repeated the accusation to Potiphar.")],
  'entries': [],
  'lost': [keeps("An added kai eipen moi, koimēthēsomai meta sou, “and he said to me, I will sleep with you,” in the Greek."), between("Hebrew, Latin and King James end at “to mock me.”")]},

 '39:18': {
  'received': "When I screamed he left his garment beside me and fled.",
  'explain': ("The Greek adds when he heard; the versions otherwise agree."),
  'shared': ["I lifted my voice and cried out.", "He left his garment beside me.", "He fled outside."],
  'instructions': [ins(K, S, "The accusation was completed with the garment.")],
  'entries': [],
  'lost': [keeps("An added hōs ēkousen, “when he heard,” in the Greek, as in 39:15."), between("Hebrew, Latin and King James “as I lifted up my voice.”")]},

 '39:19': {
  'received': "When his master heard his wife’s words, his anger burned.",
  'explain': ("Your servant treated me so. The Latin adds too readily believing his wife."),
  'shared': ["His master heard his wife’s words.", "This is how your servant treated me.", "His anger was kindled."],
  'instructions': [ins(K, S, "Potiphar believed his wife and was enraged."), ins(W, R, "The master who saw the Lord with Joseph believes a lie against him; the Latin’s “too readily” is the reader’s thought too, and the imprisonment, not the execution, hints the master doubted.")],
  'entries': [],
  'lost': [between("Latin “too readily believing his wife’s words” adds a judgment; Hebrew, Greek and King James report the hearing and the anger.")]},

 '39:20': {
  'received': "Joseph’s master put him in the prison where the king’s prisoners were held, and there he stayed.",
  'explain': ("Prison, not death, for a slave accused of attempting his master’s wife. The Hebrew says bet ha-sohar, the round house, and he remained there; the Greek the fortress, without the last clause."),
  'shared': ["Joseph’s master took him.", "He put him in the prison where the king’s prisoners were confined.", "He remained there in prison."],
  'instructions': [ins(K, S, "Joseph was imprisoned among the king’s prisoners."), ins(W, R, "The king’s prison, where the king’s officers will come; Joseph’s road to Pharaoh runs through the cell the lie put him in.")],
  'entries': [],
  'lost': [loses("Hebrew va-yhi sham be-vet ha-sohar, “and he was there in the prison,” is absent from the Greek, which has ochyrōma, “fortress,” for the prison."), between("Latin “and he was confined there” and King James “and he was there in the prison” keep the clause.")]},

 '39:21': {
  'received': "But the Lord was with Joseph, showed him kindness, and gave him favour with the prison keeper.",
  'explain': ("The refrain again, in prison. Chesed, kindness; the Greek and Latin mercy. The Greek says chief jailer; the Latin the prison’s governor."),
  'shared': ["The Lord was with Joseph.", "He extended kindness to him.", "He gave him favour in the sight of the prison keeper."],
  'instructions': [ins(K, S, "God gave Joseph favour in prison."), ins(W, R, "The Lord was with him in the house and is with him in the pit; the presence does not depend on the address, and Joseph’s rise begins again from the bottom.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew chased, “kindness,” is Greek eleos, “mercy”; Hebrew sar bet-ha-sohar, “chief of the prison,” is Greek tou archidesmophylakos, “chief jailer,” Latin “the prison’s governor,” King James “the keeper of the prison.”")]},

 '39:22': {
  'received': "The keeper put all the prisoners in Joseph’s charge; whatever was done there, he did it.",
  'explain': ("Steward of the prison as of the house. The Hebrew ends he was the doer of it; the Greek entrusts the prison itself and lacks the clause; the Latin under his direction."),
  'shared': ["The prison keeper put all the prisoners in Joseph’s charge.", "Whatever was done there.", "He was responsible for it."],
  'instructions': [ins(K, S, "Joseph was made overseer of the prisoners."), ins(W, R, "In prison as in Potiphar’s house, everything comes into Joseph’s hand; the pattern is set for Egypt, and the reader is meant to see it.")],
  'entries': [],
  'lost': [loses("Hebrew hu hayah oseh, “he was the doer,” is absent from the Greek, which adds to desmōtērion, “the prison,” to what was entrusted."), between("Latin “whatever was done was under his direction” and King James “he was the doer of it” keep the sense.")]},

 '39:23': {
  'received': "The keeper looked after nothing in Joseph’s charge, because the Lord was with him and prospered all he did.",
  'explain': ("The chapter ends as it began, with the Lord’s presence and prosperity, now in a cell. The Greek adds everything was in Joseph’s charge and names the jailer; the Latin directed all his work."),
  'shared': ["The prison keeper did not inspect anything in Joseph’s charge.", "The Lord was with him.", "Whatever he did, the Lord made it prosper."],
  'instructions': [ins(K, S, "God prospered Joseph in prison as in the house."), ins(W, R, "The verse repeats 39:3 and 39:6 almost word for word, in prison; the narrator is saying that nothing has changed but the walls.")],
  'entries': ['yhwh-yahweh'],
  'lost': [keeps("An added panta gar ēn dia cheiros Iōsēph, “for everything was through Joseph’s hand,” and ho archidesmophylax, “the chief jailer,” as subject in the Greek."), between("Latin “directed all his work” and King James “the LORD made it to prosper” follow the Hebrew.")]},
 }
}
