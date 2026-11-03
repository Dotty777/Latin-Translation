# Study prose for Genesis 37 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 37,
 'chapterNote': (
  "The Joseph story opens: the favoured son, the coat, the dreams, the brothers’ hatred, the pit, the sale to Ishmaelites, the bloodied coat and Jacob’s grief. "
  "The columns agree on the plot. The Hebrew keeps “their father … all his brothers” in 37:4, “they hated him even more” at the end of 37:5, the second dream told "
  "to the brothers and then retold to the father, “wandering in the field,” “the Ishmaelites,” twenty pieces of silver, Joseph “torn to pieces,” Sheol, Medanites "
  "in 37:36, and Potiphar as “captain of the guard.” The Greek keeps Israel named as the hearer of the bad report, Jacob for Israel in 37:3, “his father … all his "
  "sons,” the omission of “they hated him even more” in 37:5, the father added to the hearers in 37:9, “the plain,” “these Ishmaelites,” twenty pieces of gold, "
  "Joseph “snatched away,” Hades, Midianites, and Potiphar as “eunuch, the chief cook.” Three Hebrew-column renderings were corrected today. The Latin and King "
  "James follow the Hebrew; the Latin makes Joseph sixteen, says he accused his brothers of “a very grave offence,” and expands the brothers’ hatred into "
  "“fuel for envy.”"),
 'verses': {

 '37:1': {
  'received': "Jacob lived in Canaan, where his father had sojourned.",
  'explain': ("Esau in Seir, Jacob in Canaan: the two toledot set side by side. The versions agree."),
  'shared': ["Jacob dwelt in the land.", "His father had sojourned there.", "It was the land of Canaan."],
  'instructions': [ins(K, S, "Jacob settled in Canaan as his father had."), ins(W, R, "Esau possesses Seir; Jacob sojourns in Canaan. The heir of the promise is still a guest in the land he inherits.")],
  'entries': ['jacob', 'canaan'],
  'lost': [AGREE]},

 '37:2': {
  'received': "These are the generations of Jacob. Joseph, seventeen, shepherding with his brothers, the sons of Bilhah and Zilpah, brought their father a bad report of them.",
  'explain': ("The toledot of Jacob is the story of Joseph. Seventeen, with the maids’ sons, a tale-bearer. The Hebrew says a bad report about them to their father; the Greek names Israel and leaves the object unstated; the Latin sixteen, accused them of a very grave offence."),
  'shared': ["These are the generations of Jacob.", "Joseph, seventeen, was tending the flock with his brothers, the sons of Bilhah and Zilpah.", "Joseph brought a bad report to their father."],
  'instructions': [ins(K, S, "Joseph at seventeen reported on his brothers."), ins(W, R, "Joseph enters as a seventeen-year-old informer; the narrator gives his flaw before his gifts, and the brothers’ hatred has a cause before it has a coat.")],
  'entries': ['jacob'],
  'lost': [keeps("Greek pros Israēl ton patera autōn, “to Israel their father,” names the hearer; Hebrew dibbatam ra‘ah, “their bad report,” the object, is Greek psogon ponēron, without autōn."), between("Latin “at sixteen years old … accused his brothers before his father of a very grave offence” varies; King James “seventeen … brought unto his father their evil report.”")]},

 '37:3': {
  'received': "Israel loved Joseph more than all his sons, as the child of his old age, and made him an ornate tunic.",
  'explain': ("The ketonet passim, a long-sleeved or ankle-length tunic, or of many colours as the Greek took it; Tamar wears one in 2 Samuel 13. The Hebrew says Israel; the Greek Jacob; the Latin woven in many colours."),
  'shared': ["Israel loved Joseph more than all his sons.", "He was the son of his old age.", "He made him a special tunic."],
  'instructions': [ins(K, S, "Jacob favoured Joseph with a special tunic."), ins(W, R, "Isaac loved Esau and Rebekah Jacob; Jacob loves Joseph. The favouritism that split his parents’ tent he repeats on his own sons, with a coat to make it visible.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew Yisra’el is Greek Iakōb here; Hebrew ketonet passim, “a tunic of passim,” long or ornamented, is Greek chitōna poikilon, “a many-coloured tunic”; Latin “woven in many colours,” King James “a coat of many colours.”")]},

 '37:4': {
  'received': "His brothers saw their father loved him above them all, and hated him, unable to speak a peaceable word to him.",
  'explain': ("Hatred, the word of 27:41 for Esau. The Hebrew says their father, more than all his brothers; the Greek his father, more than all his sons. The Hebrew-column rendering was corrected today."),
  'shared': ["His brothers saw that their father loved him more than all.", "They hated him.", "They could not speak peaceably to him."],
  'instructions': [ins(K, S, "The brothers hated Joseph for their father’s favour."), ins(W, R, "“Could not speak peaceably”: shalom is gone from the household before any deed is done; the chapter will end with the family unable to speak the truth at all.")],
  'entries': [],
  'lost': [between("Hebrew avihem mi-kol-echav, “their father … more than all his brothers,” is Greek ho patēr autou ek pantōn tōn huiōn autou, “his father … more than all his sons”; Latin and King James follow the Hebrew.")]},

 '37:5': {
  'received': "Joseph dreamed a dream and told his brothers, and they hated him the more.",
  'explain': ("The first dream. The Hebrew ends and they hated him even more; the Greek lacks the clause, keeping it for verse 8; the Latin sowed the seeds of greater hatred."),
  'shared': ["Joseph dreamed a dream.", "He told it to his brothers.", "Their hatred grew."],
  'instructions': [ins(K, S, "Joseph’s first dream deepened the hatred."), ins(W, R, "Joseph tells his dreams to men who hate him; whether innocence or pride, the telling is the dreamer’s first mistake and the plot’s first engine.")],
  'entries': [],
  'lost': [loses("Hebrew va-yosifu od seno oto, “and they hated him even more,” is absent from the Greek here."), between("Latin “this sowed the seeds of greater hatred” and King James “they hated him yet the more” keep it.")]},

 '37:6': {
  'received': "He said, Hear this dream I have dreamed:",
  'explain': ("The versions agree; the Latin seen."),
  'shared': ["He spoke to them.", "Hear this dream.", "I have dreamed it."],
  'instructions': [ins(K, S, "Joseph asked his brothers to hear his dream.")],
  'entries': [],
  'lost': [AGREE]},

 '37:7': {
  'received': "We were binding sheaves; my sheaf rose and stood, and your sheaves gathered round and bowed to it.",
  'explain': ("Grain: the dream’s content anticipates Egypt and the famine. The Hebrew says your sheaves gathered around; the Greek turned around; the Latin seemed to rise."),
  'shared': ["We were binding sheaves in the field.", "My sheaf rose and stood upright.", "Your sheaves gathered around and bowed down to my sheaf."],
  'instructions': [ins(K, S, "Joseph dreamed his brothers’ sheaves bowed to his."), ins(W, R, "The sheaves bow in the dream; in chapter 42 the brothers will bow in Egypt for grain. The dream is literal, and the brothers hear it as insolence.")],
  'entries': [],
  'lost': [between("Hebrew tesubbenah, “gathered around,” is Greek peristraphenta, “turning around”; Latin quasi, “as if,” softens; King James “stood round about.”")]},

 '37:8': {
  'received': "His brothers asked if he would reign and rule over them, and hated him the more for his dreams and words.",
  'explain': ("Reign and rule: the brothers read the dream exactly. The Latin says fuel for envy and hatred."),
  'shared': ["Shall you indeed reign over us?", "Shall you indeed rule over us?", "They hated him even more for his dreams and his words."],
  'instructions': [ins(K, S, "The brothers resented Joseph’s dream of ruling."), ins(W, R, "“Shall you reign over us?” He shall; the brothers prophesy in mockery, as Esau did in calling Jacob supplanter.")],
  'entries': [],
  'lost': [between("Latin “Thus his dreams and words supplied fuel for envy and hatred” paraphrases; Hebrew, Greek and King James “they hated him yet the more for his dreams, and for his words.”")]},

 '37:9': {
  'received': "He dreamed again and told his brothers: the sun, moon and eleven stars bowed to me.",
  'explain': ("The second dream, cosmic. Eleven stars for eleven brothers, sun and moon for parents. The Hebrew says told it to his brothers; the Greek to his father and his brothers, anticipating verse 10."),
  'shared': ["He dreamed another dream and told it.", "Behold, the sun, the moon and eleven stars.", "They were bowing down to me."],
  'instructions': [ins(K, S, "Joseph dreamed the heavenly bodies bowed to him."), ins(W, R, "The second dream includes the parents; Joseph’s ambition, or God’s plan, reaches past the brothers to the whole house. Jacob will bow to him in Egypt in all but gesture.")],
  'entries': [],
  'lost': [keeps("An added tō patri autou kai, “to his father and,” in the Greek before his brothers."), between("Hebrew, Latin and King James “told it to his brothers.”")]},

 '37:10': {
  'received': "He told his father and brothers, and his father rebuked him: shall I, your mother and your brothers bow to you?",
  'explain': ("Jacob rebukes but, verse 11, remembers. Your mother, though Rachel is dead; Leah, or the dream’s logic. The Hebrew opens he told it to his father and brothers; the Greek, having said so in verse 9, begins with the rebuke."),
  'shared': ["His father rebuked him.", "What is this dream you have dreamed?", "Shall I, your mother and your brothers come and bow to you to the ground?"],
  'instructions': [ins(K, S, "Jacob rebuked Joseph for the second dream."), ins(W, R, "Jacob rebukes the dream and keeps it; the father who was told by his own father’s mistake what blessing is knows a word from God when he scolds it.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew va-yesapper el-aviv ve-el-echav, “and he told it to his father and his brothers,” stands here; the Greek placed it in 37:9 and opens with the rebuke; Latin and King James keep it here.")]},

 '37:11': {
  'received': "His brothers envied him, but his father kept the matter in mind.",
  'explain': ("Envy, qin’ah, now joins hatred. Jacob watches. The Latin says silently considered. Luke 2:19 and 51 echo the phrase of Mary."),
  'shared': ["His brothers were jealous of him.", "But his father.", "He kept the saying in mind."],
  'instructions': [ins(K, S, "Jacob pondered the dream the brothers resented."), ins(W, R, "Envy in the sons, pondering in the father: the same dream divides the house into those who will sell Joseph and the one who will mourn him.")],
  'entries': [],
  'lost': [between("Hebrew shamar et-ha-davar, “kept the word,” is Greek dietērēsen to rhēma; Latin “silently considered the matter,” King James “observed the saying.”")]},

 '37:12': {
  'received': "His brothers went to pasture their father’s flock at Shechem.",
  'explain': ("Shechem, where they massacred a city; a bold return. The Latin says were staying."),
  'shared': ["His brothers went.", "They pastured their father’s flock.", "They were at Shechem."],
  'instructions': [ins(K, S, "The brothers took the flocks to Shechem.")],
  'entries': [],
  'lost': [between("Latin “While his brothers were staying in Shechem” varies; Hebrew, Greek and King James “went to feed their father’s flock in Shechem.”")]},

 '37:13': {
  'received': "Israel sent Joseph to his brothers at Shechem, and he said, Here I am.",
  'explain': ("Hinneni, the word of Abraham and Isaac, from Joseph: ready. The Latin carries the reply into verse 14."),
  'shared': ["Are not your brothers pasturing at Shechem?", "Come, I will send you to them.", "He said, Here I am."],
  'instructions': [ins(K, S, "Jacob sent Joseph to his brothers."), ins(W, R, "Jacob sends the favourite alone to the brothers who cannot speak to him peaceably; the father who pondered the dream does not ponder the danger.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew and Greek “Here I am” close the verse; Latin moves it to 37:14 as “I am ready”; King James “Here am I.”")]},

 '37:14': {
  'received': "Go see whether all is well with your brothers and the flock, and bring me word. He sent him from the valley of Hebron to Shechem.",
  'explain': ("Shalom asked after, in a household without it. Fifty miles from Hebron to Shechem. The Greek names Israel."),
  'shared': ["Go and see whether your brothers and the flock are well, and bring me word.", "He sent him from the valley of Hebron.", "He came to Shechem."],
  'instructions': [ins(K, S, "Joseph travelled from Hebron to Shechem."), ins(W, R, "“See whether it is well”: Joseph is sent to ask after peace among men who have none for him. The errand is innocent and the road leads to Egypt.")],
  'entries': ['hebron'],
  'lost': [keeps("An added Israēl as subject in the Greek: “Israel said to him.”"), between("Hebrew, Latin and King James “he said.”")]},

 '37:15': {
  'received': "A man found him wandering in the field and asked what he sought.",
  'explain': ("An anonymous man at the turning point, as at the Jabbok. The Hebrew says field; the Greek plain. The Hebrew-column rendering was corrected today."),
  'shared': ["A man found him.", "He was wandering in the field.", "What are you looking for?"],
  'instructions': [ins(K, S, "A stranger found Joseph lost near Shechem."), ins(W, R, "Had the man not found him, Joseph would have gone home; the whole of Israel’s history turns on a stranger’s direction in a field.")],
  'entries': [],
  'lost': [between("Hebrew ba-sadeh, “in the field,” is Greek en tō pediō, “in the plain”; Latin and King James “field.”")]},

 '37:16': {
  'received': "I seek my brothers; tell me where they are pasturing.",
  'explain': ("The versions agree."),
  'shared': ["I am looking for my brothers.", "Tell me, please.", "Where are they pasturing?"],
  'instructions': [ins(K, S, "Joseph asked the way to his brothers.")],
  'entries': [],
  'lost': [AGREE]},

 '37:17': {
  'received': "They have gone to Dothan, the man said; Joseph found them there.",
  'explain': ("Dothan, north of Shechem on the caravan road to Egypt. The versions agree."),
  'shared': ["They have moved on; I heard them say, Let us go to Dothan.", "Joseph went after his brothers.", "He found them in Dothan."],
  'instructions': [ins(K, S, "Joseph followed his brothers to Dothan.")],
  'entries': [],
  'lost': [AGREE]},

 '37:18': {
  'received': "They saw him from afar and, before he reached them, plotted to kill him.",
  'explain': ("The Greek adds wickedly. The versions agree."),
  'shared': ["They saw him from afar.", "Before he came near.", "They plotted against him to kill him."],
  'instructions': [ins(K, S, "The brothers conspired to kill Joseph."), ins(W, R, "Cain’s sin in ten brothers: the coat is seen before the face, and the plot is made before a word is spoken.")],
  'entries': [],
  'lost': [keeps("Greek eponēreuonto, “they plotted wickedly,” for Hebrew va-yitnakkelu, “they conspired.”"), between("Latin “plotted to kill him,” King James “conspired against him to slay him.”")]},

 '37:19': {
  'received': "They said, Here comes the dreamer.",
  'explain': ("Ba‘al ha-chalomot, master of dreams, in contempt. The versions agree."),
  'shared': ["They said to one another.", "Behold.", "That dreamer is coming."],
  'instructions': [ins(K, S, "The brothers mocked Joseph as the dreamer.")],
  'entries': [],
  'lost': [AGREE]},

 '37:20': {
  'received': "Let us kill him and throw him in a pit and say a wild beast ate him; then we shall see what becomes of his dreams.",
  'explain': ("The plan and its motive: to falsify the dreams. The Latin says an old cistern, what use his dreams are."),
  'shared': ["Come, let us kill him and throw him into one of the pits.", "We will say a wild beast devoured him.", "We shall see what becomes of his dreams."],
  'instructions': [ins(K, S, "The brothers planned murder and a cover story."), ins(W, R, "“We shall see what becomes of his dreams”: they will see, in Egypt, bowing. Men who try to kill a word from God become its instruments.")],
  'entries': [],
  'lost': [between("Latin “an old cistern … what use his dreams are to him” varies; Hebrew, Greek and King James “one of the pits … what will become of his dreams.”")]},

 '37:21': {
  'received': "Reuben heard and rescued him from them: let us not take his life.",
  'explain': ("Reuben, the firstborn, disgraced by Bilhah, intervenes. The Latin says strove to deliver and moves the speech to verse 22."),
  'shared': ["Reuben heard.", "He rescued him from their hands.", "Let us not take his life."],
  'instructions': [ins(K, S, "Reuben prevented the murder."), ins(W, R, "The firstborn who lost his standing tries to save the favourite; Reuben’s instinct is good and his nerve is short, and Judah will finish what he starts.")],
  'entries': [],
  'lost': [between("Latin “strove to deliver him” for Hebrew va-yatzilehu, “and he delivered him,” and moves “let us not take his life” to 37:22; Greek and King James follow the Hebrew.")]},

 '37:22': {
  'received': "Shed no blood; throw him in this pit and lay no hand on him, he said, meaning to return him to his father.",
  'explain': ("Reuben’s compromise, with the narrator’s note of his intent. The Latin says keep your hands innocent."),
  'shared': ["Shed no blood; throw him into this pit in the wilderness.", "Lay no hand on him.", "He meant to rescue him and return him to his father."],
  'instructions': [ins(K, S, "Reuben proposed the pit to save Joseph."), ins(W, R, "“Shed no blood” is Reuben’s whole courage; he does not say let him go. Half-measures save Joseph’s life and lose him to Egypt.")],
  'entries': [],
  'lost': [between("Latin “keep your hands innocent” for Hebrew ve-yad al-tishlechu-vo, “and lay no hand on him”; Greek and King James follow the Hebrew.")]},

 '37:23': {
  'received': "When Joseph came, they stripped him of his ornate tunic.",
  'explain': ("The coat first. The Hebrew says his tunic, the ornate tunic; the Greek once; the Latin long, many-coloured."),
  'shared': ["Joseph came to his brothers.", "They stripped him.", "They took the ornate tunic he was wearing."],
  'instructions': [ins(K, S, "The brothers stripped Joseph of his coat."), ins(W, R, "The coat comes off before the boy goes in; the brothers attack the sign of favour first, and the sign will be their lie to the father.")],
  'entries': [],
  'lost': [between("Hebrew et-kuttonto et-ketonet ha-passim, “his tunic, the ornate tunic,” is Greek ton chitōna ton poikilon once; Latin tunica talari et polymita, “long and many-coloured”; King James “his coat, his coat of many colours.”")]},

 '37:24': {
  'received': "They threw him into the pit; it was empty, without water.",
  'explain': ("No water: a death by thirst, or a mercy. The versions agree; the Latin an old cistern."),
  'shared': ["They took him and threw him into the pit.", "The pit was empty.", "There was no water in it."],
  'instructions': [ins(K, S, "Joseph was thrown into a dry pit.")],
  'entries': [],
  'lost': [AGREE]},

 '37:25': {
  'received': "They sat to eat, and saw an Ishmaelite caravan from Gilead carrying spices, balm and ladanum to Egypt.",
  'explain': ("Bread above the pit, and traders on the road. The goods are gum, balsam and resin, Gilead’s exports. The Greek says travellers, aromatics, resin, stacte."),
  'shared': ["They sat down to eat bread.", "They saw a caravan of Ishmaelites coming from Gilead.", "Their camels carried spices, balm and ladanum down to Egypt."],
  'instructions': [ins(K, S, "An Ishmaelite caravan passed on its way to Egypt."), ins(W, R, "They eat while he is in the pit; Amos will remember it. The caravan is providence dressed as commerce, and the brothers see only a sale.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew nekhot u-tzeri va-lot, “gum and balm and ladanum,” is Greek thymiamatōn kai rhētinēs kai staktēs, “aromatics and resin and stacte”; Hebrew orchat Yishme‘elim, “a caravan of Ishmaelites,” is Greek hodoiporoi Ismaēlitai, “Ishmaelite travellers.”")]},

 '37:26': {
  'received': "Judah said, What profit in killing our brother and hiding his blood?",
  'explain': ("Judah’s first speech, a merchant’s: what profit. The versions agree."),
  'shared': ["Judah spoke to his brothers.", "What profit is it if we kill our brother?", "And hide his blood?"],
  'instructions': [ins(K, S, "Judah argued against murder."), ins(W, R, "Judah saves Joseph by appeal to profit, not pity; the ancestor of David begins as a man who knows the price of things, and will learn their worth in chapter 44.")],
  'entries': [],
  'lost': [AGREE]},

 '37:27': {
  'received': "Let us sell him to the Ishmaelites and not lay hands on him, for he is our brother, our flesh. They agreed.",
  'explain': ("Our brother, our flesh: Judah says what the brothers have forgotten, to justify a sale. The Greek says these Ishmaelites; the Latin it is better, hands not defiled. The Hebrew-column rendering was corrected today."),
  'shared': ["Come, let us sell him to the Ishmaelites.", "Let not our hands be on him, for he is our brother and our flesh.", "His brothers listened to him."],
  'instructions': [ins(K, S, "The brothers agreed to sell Joseph."), ins(W, R, "“He is our brother” is the reason not to kill him and the reason, unspoken, that selling him is worse; the brothers settle for the sin that leaves no body.")],
  'entries': [],
  'lost': [keeps("An added toutois, “these,” before Ishmaelites in the Greek."), between("Latin “It is better that he be sold … so that our hands are not defiled” varies; King James “let us sell him to the Ishmeelites … his brethren were content.”")]},

 '37:28': {
  'received': "Midianite traders passed; they drew Joseph from the pit and sold him to the Ishmaelites for twenty pieces of silver, who took him to Egypt.",
  'explain': ("Midianites and Ishmaelites, two names for the caravan or two groups; the sellers are unnamed. The Hebrew says silver, the slave price of Leviticus 27:5; the Greek gold; the Latin and King James silver."),
  'shared': ["Midianite merchants passed by.", "They drew Joseph up from the pit and sold him to the Ishmaelites.", "For twenty pieces, and they brought Joseph to Egypt."],
  'instructions': [ins(K, S, "Joseph was sold for twenty pieces and taken to Egypt."), ins(W, R, "Twenty pieces of silver, the price of a boy; Zechariah and Matthew will know a price of thirty. Joseph goes down to Egypt as merchandise, and Israel will follow him.")],
  'entries': ['egypt'],
  'lost': [loses("Hebrew be-esrim kasef, “for twenty of silver,” becomes Greek eikosi chrysōn, “for twenty gold pieces.”"), between("Latin “twenty silver pieces” and King James “twenty pieces of silver” follow the Hebrew.")]},

 '37:29': {
  'received': "Reuben returned to the pit, found Joseph gone, and tore his clothes.",
  'explain': ("Reuben was absent for the sale. The Latin moves the tearing to verse 30."),
  'shared': ["Reuben returned to the pit.", "Joseph was not in the pit.", "He tore his garments."],
  'instructions': [ins(K, S, "Reuben found the pit empty.")],
  'entries': [],
  'lost': [between("Latin “returned to the cistern and did not find the boy” moves va-yiqra et-begadav, “and he tore his clothes,” to 37:30; Hebrew, Greek and King James have it here.")]},

 '37:30': {
  'received': "He told his brothers, The boy is gone; and I, where shall I go?",
  'explain': ("Reuben’s despair is for himself too: the firstborn must answer to the father. The versions agree."),
  'shared': ["He returned to his brothers.", "The child is gone!", "And I, where shall I go?"],
  'instructions': [ins(K, S, "Reuben despaired at Joseph’s loss."), ins(W, R, "“Where shall I go?” Reuben thinks of facing his father; the brothers will think of a goat. Grief and guilt divide at once into those who feel and those who fix.")],
  'entries': [],
  'lost': [AGREE]},

 '37:31': {
  'received': "They killed a goat and dipped Joseph’s tunic in the blood.",
  'explain': ("A goat, as in Jacob’s own deception of Isaac. The Hebrew says a male goat, dipped; the Greek a young goat, stained."),
  'shared': ["They took Joseph’s tunic.", "They slaughtered a goat.", "They dipped the tunic in the blood."],
  'instructions': [ins(K, S, "The brothers faked Joseph’s death with goat’s blood."), ins(W, R, "Jacob deceived his blind father with a goat’s skin; his sons deceive him with a goat’s blood. The measure he used is measured to him.")],
  'entries': [],
  'lost': [between("Hebrew se‘ir izzim, “a male goat,” va-yitbelu, “and dipped,” is Greek eriphon aigōn, “a young goat,” kai emolynan, “and stained”; Latin and King James follow the Hebrew.")]},

 '37:32': {
  'received': "They sent the tunic to their father: We found this; see whether it is your son’s.",
  'explain': ("Your son, not our brother; the lie is in the pronoun. The Hebrew says please recognise; the Latin sent men to carry it."),
  'shared': ["They sent the ornate tunic and brought it to their father.", "We found this.", "Recognise whether it is your son’s tunic."],
  'instructions': [ins(K, S, "The brothers presented the bloodied coat to Jacob."), ins(W, R, "“Recognise”: the verb Jacob will hear from Tamar in the next chapter, and that Judah will use of his own seal. The brothers let the coat lie for them and speak no lie themselves.")],
  'entries': [],
  'lost': [between("Hebrew hakker-na, “please recognise,” is Greek epignōthi; Latin “sent men to carry it … see whether”; King James “know now whether it be thy son’s coat or no.”")]},

 '37:33': {
  'received': "He recognised it: My son’s tunic; a wild beast has devoured him; Joseph is surely torn to pieces.",
  'explain': ("Jacob draws the conclusion the brothers planted. The Hebrew says torn to pieces; the Greek snatched away; the Latin repeats devoured."),
  'shared': ["He recognised it and said, It is my son’s tunic.", "A wild beast has devoured him.", "Joseph is surely torn."],
  'instructions': [ins(K, S, "Jacob believed Joseph killed by a beast."), ins(W, R, "Jacob recognises the coat and misreads the story; the man who deceived by touch is deceived by sight, and will live twenty-two years in a lie his sons let stand.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew tarof toraf Yosef, “torn, Joseph is torn,” is Greek thērion hērpasen ton Iōsēph, “a beast has snatched Joseph”; Latin “a wild animal has devoured Joseph,” King James “rent in pieces.”")]},

 '37:34': {
  'received': "Jacob tore his clothes, put on sackcloth and mourned his son many days.",
  'explain': ("The rites of grief: torn clothes, sackcloth, many days. The Latin says a long time."),
  'shared': ["Jacob tore his clothes.", "He put sackcloth on his loins.", "He mourned his son many days."],
  'instructions': [ins(K, S, "Jacob mourned Joseph at length.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '37:35': {
  'received': "His sons and daughters tried to comfort him, but he refused: I will go down to Sheol mourning to my son. So his father wept for him.",
  'explain': ("Sheol, the grave, the realm of the dead, first named here; the Greek Hades; the Latin the realm of the dead. The sons comfort the grief they caused."),
  'shared': ["All his sons and daughters came to comfort him, but he refused.", "I will go down to Sheol mourning to my son.", "His father wept for him."],
  'instructions': [ins(K, S, "Jacob refused comfort and expected to die grieving."), ins(W, R, "The sons who sold him comfort the father; the hypocrisy is total and the grief is real, and the narrator sets them in one sentence.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew She’olah, “to Sheol,” is Greek eis hadou, “to Hades,” Latin in infernum, “to the realm of the dead,” King James “into the grave”; Latin “all his children” for “sons and daughters.”")]},

 '37:36': {
  'received': "The Midianites sold Joseph in Egypt to Potiphar, Pharaoh’s officer, captain of the guard.",
  'explain': ("Potiphar, a saris, officer or eunuch, chief of the executioners or bodyguard. The Hebrew spells Medanites; the Greek says eunuch, the chief cook, reading the title literally; the Latin commander of the soldiers."),
  'shared': ["The Midianites sold him in Egypt.", "They sold him to Potiphar, an officer of Pharaoh.", "He was captain of the guard."],
  'instructions': [ins(K, S, "Joseph was sold to Potiphar in Egypt."), ins(W, R, "Joseph enters Egypt as a slave in an officer’s house; the sheaves and stars seem far, and the narrator leaves him there to tell Judah’s story first.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew ha-Medanim, “the Medanites,” is Greek hoi Madiēnaioi, “the Midianites”; Hebrew seris Par‘oh sar ha-tabbachim, “officer of Pharaoh, chief of the guard,” is Greek tō spadonti Pharaō, archimageirō, “Pharaoh’s eunuch, chief cook”; Latin “court official and commander of the soldiers,” King James “officer … captain of the guard.”")]},
 }
}
