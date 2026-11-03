# Study prose for Genesis 40 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of titles and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 40,
 'chapterNote': (
  "The cupbearer and the baker: two dreams in prison, Joseph’s interpretations, the birthday feast, one restored and one hanged, and Joseph forgotten. The columns "
  "agree; the Hebrew keeps the officers as “officers,” the custody “in the captain of the guard’s house,” “each dream with its interpretation,” “its blossoms shot "
  "forth,” “Pharaoh’s hand,” the idiom “lift up your head” for both restoration and execution, “this house,” “white bread” or “white baskets,” and “a feast.” The Greek "
  "keeps “chief” for both officers from 40:1, “eunuchs,” “under the jailer,” “each dream and its vision,” “it shot forth shoots,” “Pharaoh’s hands,” “remember your "
  "office” for the lifted head, “this fortress,” “coarse bread,” “King Pharaoh,” “the birds of heaven,” and “a drinking feast.” Two Hebrew-column renderings were "
  "corrected today. The Latin and King James follow the Hebrew; the Latin has the baker hanged “upon a cross” and adds that the cupbearer forgot “as prosperity followed.”"),
 'verses': {

 '40:1': {
  'received': "Afterward the king of Egypt’s cupbearer and baker offended their lord.",
  'explain': ("Two court officers fall; the offence is not told. The Hebrew says cupbearer and baker; the Greek chief cupbearer and chief baker already; the Latin two court officials."),
  'shared': ["After these things.", "The king of Egypt’s cupbearer and baker offended.", "They offended their lord, the king of Egypt."],
  'instructions': [ins(K, S, "Pharaoh’s cupbearer and baker fell from favour."), ins(W, R, "Two men of Pharaoh’s table arrive in Joseph’s prison; the road from the pit to the palace is built by other men’s disgraces.")],
  'entries': ['egypt'],
  'lost': [keeps("Greek archioinochoos … archisitopoios, “chief cupbearer … chief baker,” already in this verse, where the Hebrew has mashqeh … ofeh, “cupbearer … baker,” the chief title first appearing in 40:2."), between("Latin “two court officials, the cupbearer and baker” and King James “the butler … and his baker” follow the Hebrew.")]},

 '40:2': {
  'received': "Pharaoh was angry with his two officers, the chief cupbearer and chief baker.",
  'explain': ("Sarisim, officers or eunuchs, the word of 37:36. The Greek says eunuchs; the Latin explains the offices."),
  'shared': ["Pharaoh was angry.", "With his two officers.", "The chief cupbearer and the chief baker."],
  'instructions': [ins(K, S, "Pharaoh was angry with two chief officers.")],
  'entries': [],
  'lost': [between("Hebrew shene sarisav, “his two officers,” is Greek tois dysi eunouchois autou, “his two eunuchs”; Latin “for one was chief of the cupbearers and the other chief of the bakers” explains; King James “two of his officers.”")]},

 '40:3': {
  'received': "He put them in custody in the house of the captain of the guard, in the prison where Joseph was.",
  'explain': ("The captain of the guard, Potiphar’s title; the prison is in his house. The Greek says under the jailer, in the prison where Joseph had been taken; the Latin the prison of the commander of the soldiers."),
  'shared': ["He put them in custody.", "It was in the house of the captain of the guard, in the prison.", "Joseph was confined there."],
  'instructions': [ins(K, S, "The officers were jailed where Joseph was."), ins(W, R, "The prison belongs to the house that condemned Joseph; his accuser’s husband is now the keeper of the men who will carry his name to Pharaoh.")],
  'entries': [],
  'lost': [between("Hebrew be-mishmar bet sar ha-tabbachim, “in custody in the house of the chief of the guard,” is Greek en phylakē para tō desmophylaki, “in custody with the jailer”; Latin “the prison of the commander of the soldiers,” King James “the house of the captain of the guard.”")]},

 '40:4': {
  'received': "The captain of the guard assigned Joseph to serve them, and they were in custody for some time.",
  'explain': ("Joseph waits on the men who will decide his future. The Hebrew says the captain of the guard; the Greek the chief jailer; the Latin the prison keeper."),
  'shared': ["Joseph was assigned to them.", "He served them.", "They remained in custody for some time."],
  'instructions': [ins(K, S, "Joseph attended the two officers."), ins(W, R, "Joseph serves in prison as he served in Potiphar’s house; the steward’s habit does not wait for freedom.")],
  'entries': [],
  'lost': [between("Hebrew sar ha-tabbachim, “the chief of the guard,” is Greek ho archidesmophylax, “the chief jailer”; Latin “the prison keeper,” King James “the captain of the guard.”")]},

 '40:5': {
  'received': "Both dreamed the same night, each a dream with its own meaning, the cupbearer and baker of the king of Egypt in prison.",
  'explain': ("Two dreams, two meanings; Pharaoh will dream two with one. The Hebrew says each according to the interpretation of his dream; the Greek each his own dream and its vision; the Latin an interpretation fitting him."),
  'shared': ["Both dreamed a dream the same night.", "Each had his own dream with its own meaning.", "They were the king of Egypt’s cupbearer and baker, confined in prison."],
  'instructions': [ins(K, S, "The two officers dreamed on one night."), ins(W, R, "Dreams again, as in chapter 37; the dreamer who was sold for his dreams will rise by reading other men’s. God speaks to Egyptians in the language Joseph knows.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew ish ke-fitron chalomo, “each according to the interpretation of his dream,” is Greek hekastos kata to hautou enypnion … horasis tou enypniou autou, “each his own dream … the vision of his dream”; Latin “each with an interpretation fitting him,” King James “each man according to the interpretation of his dream.”")]},

 '40:6': {
  'received': "Joseph came in the morning and saw they were troubled.",
  'explain': ("Joseph notices faces; the servant attends to the men, not only the task. The versions agree."),
  'shared': ["Joseph came to them in the morning.", "He looked at them.", "They were troubled."],
  'instructions': [ins(K, S, "Joseph noticed the officers’ distress.")],
  'entries': [],
  'lost': [AGREE]},

 '40:7': {
  'received': "He asked Pharaoh’s officers in custody with him why their faces were so sad today.",
  'explain': ("The Hebrew says officers, in custody in his master’s house; the Greek eunuchs; the Latin sadder than usual."),
  'shared': ["He questioned Pharaoh’s officers who were with him in custody in his master’s house.", "Why are your faces so sad?", "Today."],
  'instructions': [ins(K, S, "Joseph asked the cause of their sadness."), ins(W, R, "“Why are your faces sad?” A prisoner asks courtiers; compassion in the one who has most reason for his own sadness opens the door.")],
  'entries': [],
  'lost': [between("Hebrew serise Par‘oh, “Pharaoh’s officers,” is Greek tous eunouchous Pharaō; Latin “Why are your faces sadder today than usual?” compresses; King James “Pharaoh’s officers.”")]},

 '40:8': {
  'received': "We dreamed and have no interpreter. Joseph said, Do not interpretations belong to God? Tell me.",
  'explain': ("Joseph disclaims the art and claims the Giver. The Greek says does not their explanation come through God; the Latin tell me what you saw."),
  'shared': ["We have dreamed a dream and there is no one to interpret it.", "Do not interpretations belong to God?", "Tell me."],
  'instructions': [ins(K, S, "Joseph attributed dream interpretation to God."), ins(W, R, "“Interpretations belong to God”: Joseph will say the same to Pharaoh. The boy who told his dreams as his own glory now reads dreams as God’s message, and the change is his education.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew ha-lo le-Elohim pitronim, “do not interpretations belong to God?” is Greek ouchi dia tou theou hē diasaphēsis autōn estin, “is not their explanation through God?”; Latin “Does not interpretation belong to God? Tell me what you saw”; King James “Do not interpretations belong to God?”")]},

 '40:9': {
  'received': "The chief cupbearer told Joseph: in my dream a vine was before me,",
  'explain': ("The cupbearer first, with a vine. The versions agree."),
  'shared': ["The chief cupbearer told his dream to Joseph.", "In my dream.", "Behold, a vine was before me."],
  'instructions': [ins(K, S, "The cupbearer dreamed of a vine.")],
  'entries': [],
  'lost': [AGREE]},

 '40:10': {
  'received': "with three branches; it budded, blossomed, and its clusters ripened into grapes.",
  'explain': ("Growth compressed into a moment, as dreams do. The Hebrew says its blossoms shot forth; the Greek it shot forth shoots; the Latin gradually growing buds. The Hebrew-column rendering was corrected today."),
  'shared': ["On the vine were three branches.", "It budded and blossomed.", "Its clusters ripened into grapes."],
  'instructions': [ins(K, S, "The vine bore three branches and ripe grapes.")],
  'entries': ['grapevine'],
  'lost': [between("Hebrew altah nitzah, “its blossom came up,” is Greek anenēnochuia blastous, “having put forth shoots”; Latin “gradually growing buds; after the blossoms, the grapes ripened”; King James “her blossoms shot forth.”")]},

 '40:11': {
  'received': "Pharaoh’s cup was in my hand; I pressed the grapes into it and put the cup in Pharaoh’s hand.",
  'explain': ("The cupbearer’s office acted out. The Hebrew says Pharaoh’s hand; the Greek hands. The Hebrew-column rendering was corrected today."),
  'shared': ["Pharaoh’s cup was in my hand.", "I took the grapes and squeezed them into Pharaoh’s cup.", "I put the cup into Pharaoh’s hand."],
  'instructions': [ins(K, S, "The cupbearer dreamed of serving Pharaoh again.")],
  'entries': [],
  'lost': [between("Hebrew al-kaf Par‘oh, “on Pharaoh’s palm,” singular, is Greek eis tas cheiras Pharaō, “into Pharaoh’s hands,” plural; Latin and King James singular.")]},

 '40:12': {
  'received': "Joseph said: the three branches are three days.",
  'explain': ("The versions agree; the Latin yet to come."),
  'shared': ["Joseph said to him.", "This is its interpretation.", "The three branches are three days."],
  'instructions': [ins(K, S, "Joseph read the branches as three days.")],
  'entries': [],
  'lost': [AGREE]},

 '40:13': {
  'received': "In three days Pharaoh will lift up your head and restore you; you will hand him his cup as before.",
  'explain': ("Lift up your head, nasa rosh, to restore or to count; verse 19 will turn the idiom. The Greek says remember your office; the Latin remember your service."),
  'shared': ["Within three days Pharaoh will lift up your head.", "He will restore you to your position.", "You will put Pharaoh’s cup in his hand as before, when you were his cupbearer."],
  'instructions': [ins(K, S, "Joseph foretold the cupbearer’s restoration."), ins(W, R, "“Lift up your head”: the same words will mean death for the baker. Joseph speaks the idiom straight to one man and bends it for the other, and the Hebrew lets both hear the same phrase.")],
  'entries': [],
  'lost': [loses("Hebrew yissa Par‘oh et-roshekha, “Pharaoh will lift up your head,” becomes Greek mnēsthēsetai Pharaō tēs archēs sou, “Pharaoh will remember your office”; the idiom that 40:19 reverses is lost."), between("Latin “will remember your service” follows the Greek; King James “lift up thine head.”")]},

 '40:14': {
  'received': "Remember me when it goes well with you; show me kindness, mention me to Pharaoh, and get me out of this house.",
  'explain': ("Joseph’s one request for himself in the whole story. The Hebrew says this house; the Greek this fortress, remember me yourself; the Latin this prison."),
  'shared': ["Remember me when it goes well with you.", "Show me kindness and mention me to Pharaoh.", "Bring me out of this house."],
  'instructions': [ins(K, S, "Joseph asked the cupbearer to remember him."), ins(W, R, "Joseph asks to be remembered and is forgotten for two years; the man who trusts God still asks a man, and the delay is God’s timing, not the asking’s fault.")],
  'entries': [],
  'lost': [between("Hebrew min-ha-bayit ha-zeh, “from this house,” is Greek ek tou ochyrōmatos toutou, “from this fortress”; Greek adds dia seautou, “through yourself”; Latin “this prison,” King James “this house.”")]},

 '40:15': {
  'received': "I was stolen from the land of the Hebrews, and here too I have done nothing to deserve this pit.",
  'explain': ("Joseph’s own account: stolen, and innocent. Bor, pit, the word for the cistern his brothers used. The Latin says dungeon, though innocent."),
  'shared': ["I was stolen from the land of the Hebrews.", "Here also I have done nothing.", "Yet they put me in this pit."],
  'instructions': [ins(K, S, "Joseph protested his innocence and kidnapping."), ins(W, R, "“Stolen” covers his brothers’ crime without naming them; Joseph tells the truth and shields the guilty, which is how he will treat them in Egypt.")],
  'entries': [],
  'lost': [between("Hebrew ba-bor, “in the pit,” is Greek eis ton lakkon touton, “into this pit”; Latin “though innocent, I have been thrown into the dungeon”; King James “into the dungeon.”")]},

 '40:16': {
  'received': "Seeing the interpretation was good, the chief baker said: I too dreamed; three baskets of white bread were on my head.",
  'explain': ("The baker hopes for the same. The Hebrew salle chori is uncertain, baskets of white bread or wicker baskets; the Greek coarse bread; the Latin flour; the King James white baskets."),
  'shared': ["The chief baker saw that the interpretation was good.", "I too had a dream.", "There were three baskets on my head."],
  'instructions': [ins(K, S, "The baker told his dream of three baskets."), ins(W, R, "The baker speaks because the first reading was good; he wants the same verdict, and the dream will not give it. Joseph tells him anyway.")],
  'entries': [],
  'lost': [between("Hebrew salle chori, “baskets of white bread” or “wicker baskets,” is Greek kana chondritōn, “baskets of coarse bread”; Latin “baskets of flour,” King James “white baskets”; Hebrew ki tov patar, “that he interpreted well,” Greek hoti orthōs synekrinen, “that he interpreted correctly.”")]},

 '40:17': {
  'received': "In the top basket were all kinds of baked goods for Pharaoh, and birds ate them from the basket on my head.",
  'explain': ("Birds eating the king’s food unhindered: the omen. The Greek says King Pharaoh, the birds of heaven; the Latin food made by the baker’s art."),
  'shared': ["In the top basket were all kinds of baked food for Pharaoh.", "The birds were eating it.", "They ate from the basket on my head."],
  'instructions': [ins(K, S, "Birds ate Pharaoh’s food from the baker’s basket.")],
  'entries': [],
  'lost': [keeps("Greek basileus Pharaō, “King Pharaoh,” and ta peteina tou ouranou, “the birds of heaven,” for Hebrew Par‘oh and ha-of, “the birds.”"), between("Latin “every kind of food made by the baker’s art” and King James “all manner of bakemeats for Pharaoh” follow the Hebrew.")]},

 '40:18': {
  'received': "Joseph said: the three baskets are three days.",
  'explain': ("The same opening as verse 12; the ending will differ. The versions agree."),
  'shared': ["Joseph answered.", "This is its interpretation.", "The three baskets are three days."],
  'instructions': [ins(K, S, "Joseph read the baskets as three days.")],
  'entries': [],
  'lost': [AGREE]},

 '40:19': {
  'received': "In three days Pharaoh will lift your head off you and hang you on a tree, and the birds will eat your flesh.",
  'explain': ("The idiom turned: lift up your head from you. Hanged, impaled or exposed, the body left to birds. The Greek says take away your head; the Latin hang you upon a cross."),
  'shared': ["Within three days Pharaoh will lift your head from you.", "He will hang you on a tree.", "The birds will eat your flesh from you."],
  'instructions': [ins(K, S, "Joseph foretold the baker’s execution."), ins(W, R, "Joseph tells a condemned man the truth to his face; the interpreter does not flatter, and the honesty that will make him Pharaoh’s vizier is practised on a baker.")],
  'entries': [],
  'lost': [between("Hebrew yissa Par‘oh et-roshekha me-alekha, “Pharaoh will lift your head from upon you,” the idiom of 40:13 turned, is Greek apheilei Pharaō tēn kephalēn sou apo sou, “Pharaoh will take away your head from you”; Latin “hang you upon a cross,” Hebrew, Greek and King James “on a tree.”")]},

 '40:20': {
  'received': "On the third day, Pharaoh’s birthday, he feasted his servants and lifted up the heads of the chief cupbearer and chief baker.",
  'explain': ("The idiom a third time, neutral: he counted them, called them to account. The Greek says a drinking feast, remembered their offices; the Latin remembered."),
  'shared': ["The third day was Pharaoh’s birthday.", "He made a feast for all his servants.", "He lifted up the heads of the chief cupbearer and chief baker among his servants."],
  'instructions': [ins(K, S, "Pharaoh dealt with both officers on his birthday."), ins(W, R, "A birthday feast decides two fates; the king’s pleasure and the baker’s death come in the same sentence, and the narrator does not pause.")],
  'entries': [],
  'lost': [between("Hebrew mishteh, “feast,” is Greek poton, “drinking feast”; Hebrew va-yissa et-rosh, “he lifted the head,” is Greek emnēsthē tēs archēs, “remembered the office,” as in 40:13; Latin “remembered,” King James “lifted up the head.”")]},

 '40:21': {
  'received': "He restored the chief cupbearer, who put the cup in Pharaoh’s hand.",
  'explain': ("As Joseph said. The Latin says the one."),
  'shared': ["He restored the chief cupbearer to his office.", "He placed the cup.", "It was in Pharaoh’s hand."],
  'instructions': [ins(K, S, "The cupbearer was restored as foretold.")],
  'entries': [],
  'lost': [AGREE]},

 '40:22': {
  'received': "But the chief baker he hanged, as Joseph had interpreted.",
  'explain': ("As Joseph said. The Latin says upon a gallows, the interpreter’s truth proved."),
  'shared': ["He hanged the chief baker.", "It was just as Joseph had interpreted.", "The interpretation was fulfilled."],
  'instructions': [ins(K, S, "The baker was hanged as foretold."), ins(W, R, "Both readings prove true, and Joseph is still in prison; a true word does not free the one who speaks it, not yet.")],
  'entries': [],
  'lost': [between("Latin “hanged the other upon a gallows, so that the interpreter’s truth was proved” expands; Hebrew, Greek and King James “as Joseph had interpreted to them.”")]},

 '40:23': {
  'received': "Yet the chief cupbearer did not remember Joseph; he forgot him.",
  'explain': ("Two verbs for one failure: did not remember, forgot. Two years will pass. The Latin says as prosperity followed, his interpreter."),
  'shared': ["The chief cupbearer did not remember Joseph.", "He forgot him.", "Joseph remained in prison."],
  'instructions': [ins(K, S, "The cupbearer forgot Joseph."), ins(W, R, "“Did not remember … but forgot”: the Hebrew says it twice so the reader feels the two years. God’s remembering, when it comes in 41:1, will be timed to Pharaoh’s dream, not the cupbearer’s gratitude.")],
  'entries': [],
  'lost': [between("Latin “as prosperity followed, the chief cupbearer forgot his interpreter” paraphrases; Hebrew, Greek and King James “did not remember Joseph, but forgot him.”")]},
 }
}
