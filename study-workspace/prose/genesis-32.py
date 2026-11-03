# Study prose for Genesis 32 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 32,
 'chapterNote': (
  "Mahanaim, the embassy to Esau, the prayer, the gifts, and the night at the Jabbok where Jacob wrestles a man and becomes Israel. The reader’s verse numbers "
  "run one behind the Hebrew and Greek, which begin the chapter with Laban’s farewell; the bracketed RH numbers in the Greek column show the source numbering. The "
  "Hebrew keeps Mahanaim and Peniel as names, “return to your land and kindred,” “I am unworthy of all the kindness,” camels in the two camps, “sent them across,” "
  "“the dawn came up,” the hip socket dislocated, and “you have striven with God and with men and have prevailed.” The Greek keeps an added “the host of God encamped” "
  "in 32:1, “Encampments” and “Form of God” for the names, “hurry to the land of your birth,” “all the righteousness and truth … suffice for me,” “he sent them” of "
  "the gifts, “crossed the torrent,” the thigh “became numb,” and a verbless “with men you are powerful.” The Latin and King James follow the Hebrew; the Latin has "
  "“your brother Jacob” in 32:4, twenty bulls for ten in 32:15, and “if you have been strong against God, how much more against men.”"),
 'verses': {

 '32:1': {
  'received': "Jacob went on his way, and angels of God met him.",
  'explain': ("Angels at the border, as at Bethel when he left. The Greek adds he looked up and saw the host of God encamped; the Hebrew, Latin and King James have only the meeting. The Hebrew and Greek number this 32:2."),
  'shared': ["Jacob went on his way.", "Angels of God met him.", "He was returning to the land."],
  'instructions': [ins(K, S, "Angels met Jacob on his return."), ins(W, R, "Angels saw him out of the land and angels meet him coming back; the twenty years between are bracketed by heaven, whatever they looked like from inside.")],
  'entries': ['jacob', 'angels'],
  'lost': [keeps("An added kai anablepsas eiden parembolēn theou parembeblēkuian, “and having looked up he saw the host of God encamped,” in the Greek before the angels meet him."), between("Hebrew, Latin and King James “Jacob went on his way, and the angels of God met him.”")]},

 '32:2': {
  'received': "Jacob said, This is God’s camp, and named the place Mahanaim.",
  'explain': ("Mahanaim, two camps, a dual: God’s camp and his, or the two camps he will divide. The Hebrew and King James keep the name; the Greek translates Encampments; the Latin Mahanaim, that is, Camps."),
  'shared': ["Jacob saw them.", "This is the camp of God.", "He named the place Mahanaim."],
  'instructions': [ins(K, S, "Jacob named Mahanaim for God’s camp."), ins(W, R, "“God’s camp” beside Jacob’s: the man about to divide his household into two companies for fear of Esau is shown a third he did not count.")],
  'entries': ['jacob', 'elohim'],
  'lost': [loses("Hebrew Machanayim, a name, becomes Greek Parembolai, “Encampments,” a translation."), between("Latin “Mahanaim, that is, Camps” and King James “Mahanaim” keep the name.")]},

 '32:3': {
  'received': "Jacob sent messengers ahead to Esau in Seir, the country of Edom.",
  'explain': ("Esau has settled in Seir, south-east of the Dead Sea; Jacob must pass near it. Messengers, mal’akhim, is the word just used for angels. The versions agree."),
  'shared': ["Jacob sent messengers before him.", "They went to Esau his brother.", "He was in the land of Seir, the country of Edom."],
  'instructions': [ins(K, S, "Jacob sent an embassy to Esau."), ins(W, R, "God’s messengers meet Jacob and Jacob sends his own to Esau; the Hebrew uses one word for both, and the reader may ask which embassy mattered more.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '32:4': {
  'received': "He told them to say to his lord Esau that his servant Jacob had lived with Laban until now.",
  'explain': ("My lord, your servant: Jacob reverses the blessing of 27:29 in his own words. The Hebrew, Greek and King James say your servant Jacob; the Latin your brother Jacob."),
  'shared': ["Say to my lord Esau.", "Your servant Jacob says.", "I have lived with Laban and remained until now."],
  'instructions': [ins(K, S, "Jacob addressed Esau as lord and himself as servant."), ins(W, R, "The one blessed to be lord over his brother calls his brother lord; the stolen blessing is laid down in the first message home.")],
  'entries': ['jacob'],
  'lost': [between("Latin frater tuus Iacob, “your brother Jacob,” for Hebrew avdekha Ya‘aqov, “your servant Jacob”; Greek and King James “thy servant Jacob.”")]},

 '32:5': {
  'received': "I have oxen, donkeys, flocks and servants, and send word to my lord to find favour in your sight.",
  'explain': ("Wealth reported, favour sought. The Greek names Esau again and repeats your servant; the Hebrew and Latin my lord."),
  'shared': ["I have oxen, donkeys, flocks, and male and female servants.", "I have sent to tell my lord.", "That I may find favour in your sight."],
  'instructions': [ins(K, S, "Jacob reported his wealth and sought Esau’s favour.")],
  'entries': ['jacob'],
  'lost': [keeps("An added Ēsau, “Esau,” after my lord and ho pais sou, “your servant,” before find favour in the Greek; Greek egenonto moi, “I have acquired,” for Hebrew va-yhi-li, “I have.”"), between("Latin “I send a delegation to my lord” and King James “I have sent to tell my lord” follow the Hebrew.")]},

 '32:6': {
  'received': "The messengers returned: Esau is coming to meet you with four hundred men.",
  'explain': ("Four hundred men is an army, the number David led. No message from Esau, only the fact. The versions agree."),
  'shared': ["The messengers returned to Jacob.", "We came to your brother Esau, and he is coming to meet you.", "Four hundred men are with him."],
  'instructions': [ins(K, S, "Esau approached with four hundred men."), ins(W, R, "Esau sends no word, only himself and four hundred; the silence is the terror, and Jacob must read a brother he has not seen in twenty years.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '32:7': {
  'received': "Jacob, greatly afraid, divided his people and animals into two camps.",
  'explain': ("Mahanaim becomes literal: two camps. The Hebrew says afraid and distressed, flocks, herds, camels; the Greek afraid and perplexed, oxen and sheep, no camels; the Latin in terror, flocks, sheep, oxen, camels."),
  'shared': ["Jacob was greatly afraid and distressed.", "He divided the people with him and the animals.", "He made two camps."],
  'instructions': [ins(K, S, "Jacob divided his household against attack."), ins(W, R, "Fear and planning together: Jacob prays in the next verses, but first he divides the camp. Faith in Genesis does not stop a man from arranging what he can.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew ve-ha-gemallim, “and the camels,” is absent from the Greek list, which has tous boas kai ta probata, “the oxen and the sheep”; Hebrew va-yetzer lo, “and he was distressed,” is Greek kai ēporeito, “and was perplexed.”"), between("Latin “flocks, sheep, oxen, and camels” and King James “flocks, and herds, and the camels” keep the camels.")]},

 '32:8': {
  'received': "If Esau attacks one camp, the other may escape.",
  'explain': ("The reasoning. The versions agree."),
  'shared': ["If Esau comes to one camp and attacks it.", "The remaining camp.", "It will escape."],
  'instructions': [ins(K, S, "Jacob planned so that half might survive.")],
  'entries': [],
  'lost': [AGREE]},

 '32:9': {
  'received': "Jacob prayed: God of my father Abraham and God of my father Isaac, Lord, who told me to return and promised to do me good,",
  'explain': ("Jacob’s first recorded prayer, and the longest in Genesis. He names God by his fathers and by the promise of 31:3. The Hebrew says return to your land and kindred; the Greek hurry to the land of your birth; the Latin return to your land and birthplace."),
  'shared': ["God of my father Abraham and God of my father Isaac.", "Lord, who said to me, Return to your land and kindred.", "I will do you good."],
  'instructions': [ins(K, S, "Jacob prayed to the God of his fathers, recalling the promise."), ins(W, R, "The prayer begins by reminding God of His own word; Jacob argues from promise, and that is what prayer in Genesis looks like.")],
  'entries': ['jacob', 'abraham', 'isaac', 'yhwh-yahweh'],
  'lost': [between("Hebrew shuv le-artzekha u-le-moladtekha, “return to your land and your kindred,” is Greek apotreche eis tēn gēn tēs geneseōs sou, “hurry away to the land of your birth”; Latin “Return to your land and birthplace,” King James “Return unto thy country, and to thy kindred.”")]},

 '32:10': {
  'received': "I am unworthy of all the kindness and faithfulness You have shown me; with my staff I crossed this Jordan, and now I am two camps.",
  'explain': ("The Hebrew says I am too small for all the chesed and emet; the Greek all the righteousness and truth suffice for me, a different turn; the Latin unworthy of Your mercies. The staff and the two camps measure twenty years."),
  'shared': ["Jacob speaks of God’s kindness and faithfulness to His servant.", "With my staff I crossed this Jordan.", "Now I have become two camps."],
  'instructions': [ins(K, S, "Jacob confessed his unworthiness and God’s faithfulness."), ins(W, R, "“With my staff I crossed this Jordan”: the whole of chapters 28–31 in a clause. Jacob counts his blessings by what he carried out and what he brings back.")],
  'entries': ['jacob', 'jordan'],
  'lost': [loses("Hebrew qatonti mi-kol ha-chasadim u-mi-kol ha-emet, “I am too small for all the kindnesses and all the faithfulness,” becomes Greek hikanoutai moi apo pasēs dikaiosynēs kai apo pasēs alētheias, “all the righteousness and truth suffice for me”; the confession of unworthiness becomes sufficiency."), between("Latin “I am unworthy of all Your mercies and the faithfulness” and King James “I am not worthy of the least of all the mercies, and of all the truth” keep the Hebrew.")]},

 '32:11': {
  'received': "Deliver me from my brother Esau, for I fear he will come and kill me, mothers and children together.",
  'explain': ("The petition, plain. Mother with children, em al-banim, is a phrase for total slaughter. The Hebrew says from my brother’s hand, from Esau’s hand; the Greek once; the Latin I greatly fear him."),
  'shared': ["Deliver me from the hand of my brother Esau.", "I fear he will come and strike me.", "Mother with children."],
  'instructions': [ins(K, S, "Jacob prayed for rescue from Esau."), ins(W, R, "Jacob asks for his life and his children’s; the prayer is fear made honest, and it comes between two careful plans.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew mi-yad achi mi-yad Esav, “from my brother’s hand, from Esau’s hand,” is Greek ek cheiros tou adelphou mou Ēsau, once; Latin “I greatly fear him”; King James “from the hand of my brother, from the hand of Esau.”")]},

 '32:12': {
  'received': "But You said You would do me good and make my seed like the sand of the sea.",
  'explain': ("The promise again, as the close of the prayer: God’s word against Esau’s four hundred. The versions agree."),
  'shared': ["You said, I will surely do you good.", "I will make your seed like the sand of the sea.", "It cannot be counted for multitude."],
  'instructions': [ins(K, S, "Jacob pleaded God’s promise of innumerable seed."), ins(W, R, "If the seed is to be as the sand, the mothers and children cannot die tonight; Jacob holds God to His arithmetic.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '32:13': {
  'received': "He spent the night there and chose a gift for Esau from what he had.",
  'explain': ("Minchah, gift or tribute, the word for an offering. The Hebrew says selected a gift; the Greek took gifts and sent them; the Latin set apart gifts."),
  'shared': ["He stayed there that night.", "He took from what he had with him.", "A gift for Esau his brother."],
  'instructions': [ins(K, S, "Jacob prepared a gift for Esau."), ins(W, R, "Prayer, then a present: Jacob trusts God and bribes his brother in the same night, and the narrator finds nothing odd in it.")],
  'entries': ['jacob'],
  'lost': [keeps("An added kai exapesteilen, “and he sent them,” in the Greek; Hebrew va-yiqqach … minchah, “and he took … a gift.”"), between("Latin “set apart from what he had gifts” and King James “took … a present” follow the Hebrew.")]},

 '32:14': {
  'received': "two hundred she-goats, twenty he-goats, two hundred ewes, twenty rams,",
  'explain': ("The gift begins: breeding stock in herd proportions. The versions agree."),
  'shared': ["Two hundred she-goats and twenty he-goats.", "Two hundred ewes.", "Twenty rams."],
  'instructions': [ins(K, S, "The gift included goats and sheep in breeding ratio.")],
  'entries': [],
  'lost': [AGREE]},

 '32:15': {
  'received': "thirty nursing camels with their young, forty cows, ten bulls, twenty she-asses and ten foals.",
  'explain': ("Five hundred and fifty animals, a princely tribute. The Latin says twenty bulls for ten; the Greek donkeys without the sex."),
  'shared': ["Thirty nursing camels with their young.", "Forty cows and ten bulls.", "Twenty she-asses and ten foals."],
  'instructions': [ins(K, S, "The gift totalled over five hundred animals."), ins(W, R, "Jacob gives Esau a flock the size of a man’s fortune; the birthright bought for stew is repaid in camels.")],
  'entries': [],
  'lost': [between("Latin viginti tauros, “twenty bulls,” for Hebrew asarah, “ten”; Hebrew atonot, “female donkeys,” is Greek onous, “donkeys”; King James “ten bulls, twenty she asses.”")]},

 '32:16': {
  'received': "He gave them to his servants drove by drove and told them to go ahead with a space between droves.",
  'explain': ("Staggered gifts, so Esau meets wave after wave. The versions agree."),
  'shared': ["He gave them to his servants, each drove by itself.", "Pass on before me.", "Put a space between drove and drove."],
  'instructions': [ins(K, S, "Jacob staged the gifts in separated droves."), ins(W, R, "Each drove is a fresh surprise; Jacob wears his brother’s anger down with generosity timed like a campaign.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '32:17': {
  'received': "He told the first servant what to say if Esau asked whose he was, where he was going, and whose animals these were.",
  'explain': ("The script. The versions agree."),
  'shared': ["He commanded the first.", "If Esau meets you and asks whose you are and where you go.", "And whose these animals are before you."],
  'instructions': [ins(K, S, "Jacob scripted the servants’ answers.")],
  'entries': [],
  'lost': [AGREE]},

 '32:18': {
  'received': "Say, They are your servant Jacob’s, a gift to my lord Esau; and he himself is behind us.",
  'explain': ("The answer: servant, lord, gift, and Jacob following. The Hebrew says it is a gift sent; the Greek he has sent gifts."),
  'shared': ["They belong to your servant Jacob.", "It is a gift sent to my lord Esau.", "He himself is behind us."],
  'instructions': [ins(K, S, "Each drove was to be announced as Jacob’s gift to Esau.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew minchah hi sheluchah, “it is a gift sent,” is Greek dōra apestalken, “he has sent gifts,” plural; Latin “he has sent gifts,” King James “it is a present sent.”")]},

 '32:19': {
  'received': "He gave the same orders to the second, the third, and all who followed the droves.",
  'explain': ("The Greek adds the first to the list; the others begin with the second."),
  'shared': ["He commanded the second and the third.", "He commanded all who followed the droves.", "Speak this way to Esau when you find him."],
  'instructions': [ins(K, S, "All the drovers carried the same message.")],
  'entries': [],
  'lost': [keeps("An added tō prōtō kai, “the first and,” in the Greek before the second."), between("Hebrew, Latin and King James begin with “the second.”")]},

 '32:20': {
  'received': "Say too, Your servant Jacob is behind us; for he thought to appease Esau with the gift and then see his face.",
  'explain': ("Appease, kipper, the verb of atonement; see his face, lift up my face: the language of the sanctuary used of a brother. The Hebrew says going before me; the Greek before him, gifts; the Latin be favourable."),
  'shared': ["Also say, Your servant Jacob is behind us.", "I will appease him with the gift that goes before.", "Afterward I will see his face; perhaps he will accept me."],
  'instructions': [ins(K, S, "Jacob hoped the gifts would appease Esau before they met."), ins(W, R, "Jacob speaks of his brother as a worshipper of God: atonement, the face, acceptance. Reconciliation with Esau is the first liturgy he performs.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ba-minchah ha-holekhet lefanai, “with the gift going before me,” is Greek en tois dōrois tois proporeuomenois autou, “with the gifts going before him”; Latin “the gifts that go ahead,” King James “the present that goeth before me.”")]},

 '32:21': {
  'received': "The gift went ahead while Jacob spent the night in the camp.",
  'explain': ("The gifts cross; Jacob waits. The Hebrew says gift, singular; the Greek and Latin gifts."),
  'shared': ["The gift went ahead of him.", "He spent that night.", "He was in the camp."],
  'instructions': [ins(K, S, "The gifts went ahead; Jacob stayed the night.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ha-minchah, “the gift,” is Greek ta dōra, “the gifts”; Latin “the gifts,” King James “the present.”")]},

 '32:22': {
  'received': "In the night he took his two wives, two maids and eleven children across the ford of the Jabbok.",
  'explain': ("The Jabbok, a tributary of the Jordan, the border of Gilead. Eleven children, Dinah uncounted or Benjamin unborn. The Hebrew and Greek say rose in the night; the Latin rose early."),
  'shared': ["He rose in the night.", "He took his two wives, his two maids and his eleven children.", "He crossed the ford of the Jabbok."],
  'instructions': [ins(K, S, "Jacob brought his family across the Jabbok by night."), ins(W, R, "The crossing is at night, like the flight from Haran and the wedding of Leah; Jacob’s turning points come in the dark.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ba-laylah hu, “in that night,” and Greek tēn nykta, “in the night,” agree; Latin “he rose early”; Hebrew yeladav, “his children,” Latin and King James “sons.”")]},

 '32:23': {
  'received': "He sent them across the stream with all he had.",
  'explain': ("The Hebrew says he sent them across, staying behind; the Greek he crossed the torrent and brought over all; the Latin after bringing across everything. The Hebrew makes the solitude of the next verse deliberate."),
  'shared': ["He took them.", "They crossed the stream.", "All that he had went over."],
  'instructions': [ins(K, S, "Everything Jacob had crossed the Jabbok."), ins(W, R, "He sends everyone over and stays; the man who divided his camp for safety leaves himself the exposed one, and that is where the night finds him.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew va-ya‘avirem et-ha-nachal va-ya‘aver et-asher-lo, “and he sent them across the stream and sent across what he had,” is Greek kai diebē ton cheimarroun kai diebibasen panta ta autou, “and he crossed the torrent and brought over all his”; Latin “after bringing across everything”; King James “sent them over the brook.”")]},

 '32:24': {
  'received': "Jacob was left alone, and a man wrestled with him until daybreak.",
  'explain': ("A man, ish, unnamed; Hosea calls him an angel, Jacob will call him God. Wrestled, ye’aveq, plays on Jabbok and on Jacob. The Hebrew says until the dawn came up; the Greek until morning."),
  'shared': ["Jacob was left alone.", "A man wrestled with him.", "It lasted until dawn."],
  'instructions': [ins(K, S, "A man wrestled Jacob all night at the Jabbok."), ins(W, R, "Alone at last, after a life of wrestling men, Jacob is wrestled by one he did not choose; the night is the whole story told as a fight.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ad alot ha-shachar, “until the rising of the dawn,” is Greek heōs prōi, “until morning”; Latin “until morning,” King James “until the breaking of the day.”")]},

 '32:25': {
  'received': "Unable to prevail, the man touched Jacob’s hip socket and dislocated it as they wrestled.",
  'explain': ("The man, who cannot win, lames him with a touch. The Hebrew says the hollow of his thigh, the socket, was put out of joint; the Greek the broad part of his thigh became numb; the Latin the sinew withered. The anatomy is uncertain in both languages."),
  'shared': ["The man saw he could not prevail against Jacob.", "He touched the hollow of his thigh.", "Jacob’s hip was injured as he wrestled with him."],
  'instructions': [ins(K, S, "The stranger lamed Jacob with a touch."), ins(W, R, "He could not prevail and he could maim with a touch: the man’s strength is withheld, and the restraint is the clue to who he is.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew va-teqa kaf-yerekh Ya‘aqov, “and the socket of Jacob’s thigh was dislocated,” becomes Greek kai enarkēsen to platos tou mērou Iakōb, “and the broad part of Jacob’s thigh became numb”; displacement becomes numbness."), between("Latin “touched the sinew of his thigh, and it immediately withered” and King James “the hollow of Jacob’s thigh was out of joint” vary.")]},

 '32:26': {
  'received': "He said, Let me go, for dawn is breaking; Jacob said, I will not let you go unless you bless me.",
  'explain': ("The lamed man will not release the one who lamed him. The versions agree."),
  'shared': ["Let me go, for the dawn has risen.", "Jacob refused.", "I will not let you go unless you bless me."],
  'instructions': [ins(K, S, "Jacob demanded a blessing before releasing the man."), ins(W, R, "Jacob has stolen one blessing and bought another; this one he holds on for, crippled, until it is given. It is the first he has earned.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '32:27': {
  'received': "He asked Jacob’s name, and he said, Jacob.",
  'explain': ("The question Isaac asked blind, who are you, my son; this time Jacob gives his own name. The versions agree."),
  'shared': ["What is your name?", "He answered.", "Jacob."],
  'instructions': [ins(K, S, "Jacob gave his true name."), ins(W, R, "“I am Esau,” he told his father; “Jacob,” he tells the stranger. The confession of his name is the turning of his life.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '32:28': {
  'received': "Your name shall no longer be Jacob but Israel, for you have striven with God and with men and prevailed.",
  'explain': ("Israel, he strives with God, or God strives. The Hebrew says striven with God and with men and prevailed; the Greek you have been strong with God, and with men you are powerful, without a verb; the Latin if you have been strong against God, how much more against men; the King James as a prince hast thou power."),
  'shared': ["Your name shall no longer be Jacob but Israel.", "You have striven with God and with men.", "You have prevailed."],
  'instructions': [ins(K, S, "Jacob was renamed Israel for striving with God."), ins(W, R, "The heel-grasper becomes the God-wrestler; the new name does not erase the old but names what the old was for.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew ki-sarita im-Elohim ve-im-anashim va-tukhal, “for you have striven with God and with men and have prevailed,” becomes Greek hoti enischysas meta theou kai meta anthrōpōn dynatos, “because you have been strong with God and with men powerful,” the final verb lost and the striving become strength."), between("Latin “if you have been strong against God, how much more shall you prevail against men?” makes it an argument; King James “as a prince hast thou power with God and with men, and hast prevailed.”")]},

 '32:29': {
  'received': "Jacob asked his name; he said, Why do you ask my name? and blessed him there.",
  'explain': ("The name is refused, as to Manoah in Judges 13; the blessing is given. The versions agree."),
  'shared': ["Jacob asked, Tell me your name.", "Why is it that you ask my name?", "He blessed him there."],
  'instructions': [ins(K, S, "The stranger withheld his name but blessed Jacob."), ins(W, R, "Jacob gives his name and gets a new one; the stranger keeps his and gives a blessing. The asymmetry is the whole relation between God and man.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '32:30': {
  'received': "Jacob named the place Peniel: I have seen God face to face and my life is preserved.",
  'explain': ("Peniel, face of God. The Hebrew and Latin keep the name; the Greek translates Form of God, eidos theou. Face to face, and alive: the wonder of the sentence."),
  'shared': ["Jacob named the place Peniel.", "I have seen God face to face.", "My life has been preserved."],
  'instructions': [ins(K, S, "Jacob named Peniel for seeing God face to face."), ins(W, R, "“I have seen God face to face”: the man who feared to see Esau’s face has seen God’s and lived; the brother’s face tomorrow will be the smaller thing.")],
  'entries': ['jacob', 'elohim'],
  'lost': [loses("Hebrew Peni’el, “face of God,” a name, becomes Greek Eidos theou, “Form of God,” a translation with a different noun."), between("Latin “Peniel” and King James “Peniel” keep the name.")]},

 '32:31': {
  'received': "The sun rose on him as he passed Penuel, limping on his hip.",
  'explain': ("The sun that set at Bethel in 28:11 rises at Penuel; the Hebrew spells the name Penuel here. He limps. The Greek says Form of God; the Latin upon his foot."),
  'shared': ["The sun rose upon him.", "He passed Penuel.", "He was limping because of his hip."],
  'instructions': [ins(K, S, "Jacob left Peniel lame at sunrise."), ins(W, R, "The sun set on Jacob leaving Canaan and rises on him returning, lame; the blessing is real and so is the limp, and he carries both home.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew Penu’el, a variant spelling, is Greek to Eidos tou theou, “the Form of God”; Hebrew al-yerekho, “on his thigh,” Latin “upon his foot,” King James “upon his thigh.”")]},

 '32:32': {
  'received': "So Israelites to this day do not eat the sinew of the hip, because he touched Jacob’s hip at that sinew.",
  'explain': ("The one dietary custom in Genesis, the gid ha-nasheh, the sciatic sinew, still observed. The Hebrew says the hip socket; the Greek the sinew that became numb at the broad part of the thigh; the Latin the sinew that withered."),
  'shared': ["The children of Israel do not eat the sinew of the thigh.", "It is so to this day.", "Because he touched Jacob’s thigh at that sinew."],
  'instructions': [ins(K, S, "Israel’s avoidance of the thigh sinew commemorates Jacob’s wound."), ins(W, R, "A nation remembers its father’s limp at every meal; the wound that came with the blessing is kept in the kitchen, not the shrine.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew gid ha-nasheh asher al-kaf ha-yarekh, “the sinew of the nasheh which is on the socket of the thigh,” is Greek to neuron ho enarkēsen, ho estin epi tou platous tou mērou, “the sinew that became numb, which is on the broad part of the thigh”; Latin “the sinew that withered,” King James “the sinew which shrank.”")]},
 }
}
