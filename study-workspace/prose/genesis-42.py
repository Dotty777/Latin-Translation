# Study prose for Genesis 42 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 42,
 'chapterNote': (
  "The brothers’ first journey to Egypt: Jacob’s reproach, ten go down, Joseph recognises them and they do not recognise him, the charge of spying, three days in "
  "prison, Simeon held, the silver in the sacks, and Jacob’s refusal to send Benjamin. The columns agree on the plot; the Hebrew keeps “why do you look at one "
  "another,” “harm” as Jacob’s fear, the dreams “about them,” “the nakedness of the land,” “honest men,” “as Pharaoh lives,” “bound” in custody, “for your hungry "
  "households,” “their heart went out,” “treated us as spies,” “my gray hairs,” and Sheol. The Greek keeps “why are you sitting idle,” “a grain sale,” “a little "
  "food,” “sickness” as the fear, “the tracks of the country,” “men of peace,” “by Pharaoh’s health,” “taken away,” “the grain you have purchased,” an added "
  "“placed us in custody,” Joseph named in 42:24, “bundle of silver” in 42:27, “their hearts were astonished,” “my old age,” and Hades. One Hebrew-column rendering "
  "was corrected today. The Latin and King James follow the Hebrew; the Latin moves the binding of Simeon to 42:25 and has Jacob say “Simeon is held in bonds.”"),
 'verses': {

 '42:1': {
  'received': "Jacob saw there was grain in Egypt and asked his sons why they looked at one another.",
  'explain': ("The famine reaches Canaan; the father reproaches sons who do nothing. The Hebrew says why do you look at one another; the Greek why are you sitting idle, a grain sale; the Latin heard, doing nothing."),
  'shared': ["Jacob saw that there was grain in Egypt.", "He spoke to his sons.", "Why are you idle?"],
  'instructions': [ins(K, S, "Jacob urged his sons to act in the famine."), ins(W, R, "“Why do you look at one another?” The brothers have a reason not to go to Egypt that their father does not know; the look between them is twenty years old.")],
  'entries': ['jacob', 'egypt'],
  'lost': [between("Hebrew lammah titra’u, “why do you look at one another,” is Greek hina ti rhathymeite, “why are you idle”; Hebrew ki yesh-shever, “that there was grain,” is Greek hoti estin prasis, “that there was a sale”; Latin “heard that food was being sold … why are you doing nothing”; King James “Why do ye look one upon another?”")]},

 '42:2': {
  'received': "Go down to Egypt and buy grain, that we may live and not die.",
  'explain': ("Live and not die, the formula of famine. The Greek says a little food; the Latin not be consumed by scarcity."),
  'shared': ["I have heard there is grain in Egypt.", "Go down and buy for us.", "That we may live and not die."],
  'instructions': [ins(C, S, "Go down to Egypt and buy grain for us."), ins(W, R, "Jacob sends his sons down to Egypt for life; Abraham went down for the same reason. The family’s survival has always run through the land it will be enslaved in.")],
  'entries': ['egypt'],
  'lost': [keeps("An added mikra brōmata, “a little food,” in the Greek."), between("Latin “buy what we need, so that we may live and not be consumed by scarcity”; King James “buy for us from thence; that we may live, and not die.”")]},

 '42:3': {
  'received': "Joseph’s ten brothers went down to buy grain in Egypt.",
  'explain': ("Joseph’s brothers, the narrator says, not Jacob’s sons; the chapter is about Joseph. The versions agree."),
  'shared': ["Joseph’s ten brothers.", "They went down.", "To buy grain from Egypt."],
  'instructions': [ins(K, S, "Ten brothers went to Egypt for grain.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '42:4': {
  'received': "Jacob kept Benjamin, Joseph’s brother, back, lest harm befall him.",
  'explain': ("Benjamin, Rachel’s other son, is now the favourite kept home. The Hebrew says harm, ason; the Greek sickness; the Latin on the journey."),
  'shared': ["Jacob did not send Benjamin, Joseph’s brother, with them.", "He said.", "Lest harm befall him."],
  'instructions': [ins(K, S, "Jacob kept Benjamin at home."), ins(W, R, "Jacob has learned what happens when he sends a favourite son out with his brothers; Benjamin stays, and the lesson will be tested.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew ason, “harm,” becomes Greek malakia, “sickness.”"), between("Latin “some harm … on the journey” and King James “mischief” follow the Hebrew.")]},

 '42:5': {
  'received': "The sons of Israel came to buy among the others, for the famine was in Canaan.",
  'explain': ("Among those who came: anonymous in a crowd of buyers. The versions agree."),
  'shared': ["The sons of Israel came to buy grain.", "They came among the others who came.", "The famine was in the land of Canaan."],
  'instructions': [ins(K, S, "The brothers joined the buyers in Egypt.")],
  'entries': ['canaan'],
  'lost': [AGREE]},

 '42:6': {
  'received': "Joseph was governor of the land and sold to all; his brothers came and bowed to the ground before him.",
  'explain': ("The sheaves of 37:7 bow. Shallit, governor, the word of Daniel’s Babylon. The Latin runs on into verse 7."),
  'shared': ["Joseph was the ruler of the land and sold to all the people.", "Joseph’s brothers came.", "They bowed down before him with their faces to the ground."],
  'instructions': [ins(K, S, "The brothers bowed to Joseph unknowing."), ins(W, R, "Faces to the ground before the dreamer: the dream is fulfilled and no one in it knows. “We shall see what will become of his dreams,” they said; they are seeing.")],
  'entries': [],
  'lost': [between("Latin “When his brothers bowed to him” runs the clause into 42:7 and drops “faces to the ground”; Hebrew, Greek and King James complete the verse.")]},

 '42:7': {
  'received': "Joseph recognised his brothers but acted as a stranger and spoke harshly: Where are you from? From Canaan, to buy food.",
  'explain': ("Recognised, hikkir, the chapter’s verb; and made himself strange, yitnakker, the same root turned. The versions agree."),
  'shared': ["Joseph saw his brothers and recognised them.", "He acted like a stranger and spoke harshly: Where do you come from?", "From the land of Canaan, to buy food."],
  'instructions': [ins(K, S, "Joseph concealed himself and questioned his brothers."), ins(W, R, "Joseph recognises and estranges in one Hebrew root; he knows them and will not be known, and the harshness is a mask over a face about to weep.")],
  'entries': ['canaan'],
  'lost': [AGREE]},

 '42:8': {
  'received': "Joseph knew his brothers, but they did not know him.",
  'explain': ("Seventeen when sold, thirty-nine now, shaved and Egyptian. The versions agree."),
  'shared': ["Joseph recognised his brothers.", "They did not recognise him.", "The knowledge was one-sided."],
  'instructions': [ins(K, S, "The recognition was one-sided."), ins(W, R, "They did not know him: Joseph has the advantage of a god, seeing and unseen, and the next two chapters are what he does with it.")],
  'entries': [],
  'lost': [AGREE]},

 '42:9': {
  'received': "Joseph remembered his dreams about them and said, You are spies, come to see the nakedness of the land.",
  'explain': ("The dreams return as the brothers bow. Spies, a charge that forces them to explain their family. The Hebrew says dreams about them, the nakedness of the land; the Greek the dreams he had seen, the tracks of the country; the Latin weak places."),
  'shared': ["Joseph remembered the dreams.", "You are spies!", "You have come to see the nakedness of the land."],
  'instructions': [ins(K, S, "Joseph accused his brothers of spying."), ins(W, R, "He remembers the dreams and accuses them of spying; the accusation is false and the test is real, and he is finding out whether the men who sold him have changed.")],
  'entries': [],
  'lost': [loses("Hebrew asher chalam lahem, “which he dreamed about them,” becomes Greek ha eiden autos, “which he had seen,” without them; Hebrew ervat ha-aretz, “the nakedness of the land,” becomes ta ichnē tēs chōras, “the tracks of the country.”"), between("Latin “the country’s weak places” and King James “the nakedness of the land” follow the Hebrew’s sense.")]},

 '42:10': {
  'received': "No, my lord; your servants have come to buy food.",
  'explain': ("My lord, your servants: the brothers speak the language of the dream. The versions agree."),
  'shared': ["No, my lord.", "Your servants have come.", "To buy food."],
  'instructions': [ins(K, S, "The brothers denied spying.")],
  'entries': [],
  'lost': [AGREE]},

 '42:11': {
  'received': "We are all one man’s sons; we are honest men, not spies.",
  'explain': ("Kenim, honest, upright; the Greek men of peace; the Latin plotting no evil. One man’s sons: they argue that spies would not come as a family."),
  'shared': ["We are all sons of one man.", "We are honest men.", "Your servants are not spies."],
  'instructions': [ins(K, S, "The brothers protested their honesty."), ins(W, R, "“We are honest men,” say the ten who sold their brother and lied to their father; Joseph lets the word stand and tests it.")],
  'entries': [],
  'lost': [between("Hebrew kenim, “honest,” is Greek eirēnikoi, “peaceful,” here and through the chapter; Latin “we have come peaceably, and your servants are plotting no evil”; King James “true men.”")]},

 '42:12': {
  'received': "No; you have come to see the nakedness of the land.",
  'explain': ("Joseph repeats the charge. The Greek says tracks; the Latin unprotected parts."),
  'shared': ["He said to them, No.", "You have come to see.", "The nakedness of the land."],
  'instructions': [ins(K, S, "Joseph pressed the accusation.")],
  'entries': [],
  'lost': [between("Hebrew ervat ha-aretz is Greek ta ichnē tēs gēs, “the tracks of the land”; Latin “the unprotected parts of this land”; King James “the nakedness of the land.”")]},

 '42:13': {
  'received': "Your servants are twelve brothers, sons of one man in Canaan; the youngest is with our father, and one is no more.",
  'explain': ("Twelve, counting the one who is no more; the brothers tell Joseph about Joseph. The Greek lacks sons of one man; the Latin no longer alive."),
  'shared': ["Your servants are twelve brothers, sons of one man in Canaan.", "The youngest is with our father today.", "One is no more."],
  'instructions': [ins(K, S, "The brothers told Joseph of Benjamin and the lost brother."), ins(W, R, "“One is no more”: they report Joseph’s death to Joseph. He learns his father lives and Benjamin lives, and the test turns toward Benjamin.")],
  'entries': ['canaan'],
  'lost': [loses("Hebrew bene ish-echad, “sons of one man,” is absent from the Greek here."), between("Latin “sons of one man in the land of Canaan” and King James “the sons of one man” keep it.")]},

 '42:14': {
  'received': "It is as I said: you are spies.",
  'explain': ("The versions agree."),
  'shared': ["Joseph said to them.", "It is just as I told you.", "You are spies."],
  'instructions': [ins(K, S, "Joseph repeated the charge a third time.")],
  'entries': [],
  'lost': [AGREE]},

 '42:15': {
  'received': "You will be tested by this: as Pharaoh lives, you will not leave unless your youngest brother comes.",
  'explain': ("The oath by Pharaoh’s life, Egyptian in form. The Hebrew says tested, as Pharaoh lives; the Greek exposed, by Pharaoh’s health; the Latin put you to the test."),
  'shared': ["By this you will be tested.", "As Pharaoh lives, you will not leave here.", "Unless your youngest brother comes here."],
  'instructions': [ins(K, S, "Joseph demanded Benjamin as proof."), ins(W, R, "Joseph wants Benjamin: to see his brother, and to see what the ten will do with Rachel’s other son. The oath by Pharaoh keeps the Egyptian mask on.")],
  'entries': [],
  'lost': [between("Hebrew tibbachenu, “you will be tested,” che Par‘oh, “by the life of Pharaoh,” is Greek phaneroi esesthe, “you will be exposed,” nē tēn hygieian Pharaō, “by the health of Pharaoh”; Latin “I shall put you to the test. By Pharaoh’s life”; King James “Hereby ye shall be proved: By the life of Pharaoh.”")]},

 '42:16': {
  'received': "Send one to fetch your brother while the rest stay bound, to prove your words; if not, as Pharaoh lives, you are spies.",
  'explain': ("Joseph’s first proposal: one goes, nine stay. He will reverse it. The Hebrew says remain bound; the Greek taken away, until your words become clear; the Latin bound."),
  'shared': ["Send one of you to bring your brother.", "The rest will remain bound while your words are tested.", "If not, as Pharaoh lives, you are spies."],
  'instructions': [ins(K, S, "Joseph proposed holding nine and sending one.")],
  'entries': [],
  'lost': [between("Hebrew he’aseru, “be bound,” is Greek apachthēte, “be taken away”; Hebrew ha-emet ittekhem, “whether truth is with you,” Greek ei alētheuete ē ou, “whether you tell the truth or not”; Latin “remain bound,” King James “kept in prison.”")]},

 '42:17': {
  'received': "He put them all in custody for three days.",
  'explain': ("Three days in Joseph’s prison, as Joseph spent years in theirs. The versions agree."),
  'shared': ["He put them in custody.", "All together.", "For three days."],
  'instructions': [ins(K, S, "The brothers were jailed three days."), ins(W, R, "Three days in a pit for the men who left him in one; Joseph measures the lesson and does not take the full price.")],
  'entries': [],
  'lost': [AGREE]},

 '42:18': {
  'received': "On the third day Joseph said: Do this and live, for I fear God.",
  'explain': ("I fear God: the Egyptian governor confesses the brothers’ God. The Greek lacks Joseph’s name; the Latin brought them out of prison."),
  'shared': ["On the third day Joseph spoke to them.", "Do this and live.", "For I fear God."],
  'instructions': [ins(K, S, "Joseph softened the terms, professing fear of God."), ins(W, R, "“I fear God” from an Egyptian’s mouth should have told them something; it tells the reader that the harshness is bounded by conscience, and the test is not revenge.")],
  'entries': ['elohim'],
  'lost': [between("Greek kai eipen autois, “and he said to them,” without Iōsēph; Latin “he brought them out of prison and said”; Hebrew and King James name Joseph.")]},

 '42:19': {
  'received': "If you are honest, let one brother stay bound while the rest carry grain to your hungry households.",
  'explain': ("Reversed: nine go, one stays. The Hebrew says for the famine of your households; the Greek the grain you have purchased; the Latin to your homes."),
  'shared': ["If you are honest men, let one brother remain bound in prison.", "The rest of you go.", "Carry grain for your hungry households."],
  'instructions': [ins(K, S, "Joseph held one brother and released nine."), ins(W, R, "He keeps one and feeds the rest; the famine at home is real and Joseph will not let his father starve to test his brothers.")],
  'entries': [],
  'lost': [between("Hebrew shever ra‘avon batekhem, “grain for the famine of your houses,” is Greek ton agorasmon tēs sitodosias hymōn, “the purchase of your grain-supply”; Latin “the grain you have bought to your homes,” King James “corn for the famine of your houses.”")]},

 '42:20': {
  'received': "Bring your youngest brother to me, that your words be verified and you not die. They did so.",
  'explain': ("The Hebrew says and you will not die; the Greek otherwise you shall die; the same condition from two sides."),
  'shared': ["Bring your youngest brother to me.", "Your words will be verified.", "You will not die. And they did so."],
  'instructions': [ins(C, S, "Bring your youngest brother to me."), ins(K, S, "The brothers accepted Joseph’s terms.")],
  'entries': [],
  'lost': [between("Hebrew ve-lo tamutu, “and you will not die,” is Greek ei de mē, apothaneisthe, “but if not, you will die”; Latin “that you may not die,” King James “ye shall not die.”")]},

 '42:21': {
  'received': "They said to each other: truly we are guilty for our brother; we saw his anguish when he begged and would not listen; so this distress has come.",
  'explain': ("The first confession, among themselves, twenty years late. His anguish: they saw it then and say so now. The Greek says disregarded his anguish; the Latin deservedly."),
  'shared': ["Truly we are guilty concerning our brother.", "We saw the anguish of his soul when he begged us, but would not listen.", "Therefore this distress has come upon us."],
  'instructions': [ins(K, S, "The brothers confessed their guilt toward Joseph."), ins(W, R, "They connect the prison to the pit without being told; conscience does Joseph’s work for him, and he hears, in his own tongue, that they remember him begging.")],
  'entries': [],
  'lost': [between("Hebrew asher ra’inu tzarat nafsho, “in that we saw the anguish of his soul,” is Greek hypereidomen tēn thlipsin tēs psychēs autou, “we disregarded the anguish of his soul”; Latin “We suffer this deservedly, because we sinned”; King James “We are verily guilty.”")]},

 '42:22': {
  'received': "Reuben said: Did I not tell you not to sin against the boy? You would not listen; now his blood is required.",
  'explain': ("Reuben’s I told you so, and the theology of blood, 9:5. The versions agree in substance."),
  'shared': ["Did I not tell you, Do not sin against the boy?", "You would not listen.", "Now his blood is required of us."],
  'instructions': [ins(K, S, "Reuben recalled his warning."), ins(W, R, "“His blood is required”: they think Joseph dead and themselves under judgment for it. The one they think they killed is listening, and the blood they fear will not be required.")],
  'entries': [],
  'lost': [between("Hebrew al-techet’u va-yeled, “do not sin against the child,” is Greek mē adikēsēte to paidarion, “do not wrong the boy”; Latin “One of them, Reuben,” adds; King James “Do not sin against the child.”")]},

 '42:23': {
  'received': "They did not know Joseph understood, for an interpreter stood between them.",
  'explain': ("The interpreter, a prop of the disguise; Joseph hears Hebrew while pretending to need Egyptian. The versions agree."),
  'shared': ["They did not know that Joseph understood them.", "An interpreter.", "He stood between them."],
  'instructions': [ins(K, S, "Joseph understood the brothers’ Hebrew."), ins(W, R, "The interpreter between them is the whole situation in a man: Joseph understands everything and is understood by no one.")],
  'entries': [],
  'lost': [AGREE]},

 '42:24': {
  'received': "He turned away and wept, then returned and spoke to them, took Simeon and bound him before their eyes.",
  'explain': ("Joseph’s first weeping, of seven. Simeon chosen: the second son, perhaps the leader in the pit, or the next after Reuben who had tried to save him. The Greek names Joseph; the Latin moves the binding to verse 25."),
  'shared': ["He turned away from them and wept.", "He returned and spoke to them.", "He took Simeon and bound him before their eyes."],
  'instructions': [ins(K, S, "Joseph wept secretly and held Simeon."), ins(W, R, "He weeps where they cannot see and binds Simeon where they can; Joseph’s tenderness and his justice are kept in separate rooms, and the reader is shown both.")],
  'entries': [],
  'lost': [keeps("An added Iōsēph as subject of “returned” in the Greek."), between("Latin “He turned away briefly and wept, then returned and spoke to them” moves Simeon’s binding to 42:25; Hebrew and King James have it here.")]},

 '42:25': {
  'received': "Joseph ordered their sacks filled, each man’s silver returned to his sack, and provisions given; it was done.",
  'explain': ("Grain, silver returned, food for the road: a gift disguised as a sale, and a trap. The Latin opens with Simeon bound here."),
  'shared': ["Joseph ordered their vessels filled with grain.", "Each man’s silver was to be returned to his sack and provisions given for the way.", "It was done for them."],
  'instructions': [ins(K, S, "Joseph returned the brothers’ silver secretly."), ins(W, R, "He gives back the silver: the brothers once took silver for him, and will find silver they did not pay. The returned money is grace that feels like a snare.")],
  'entries': [],
  'lost': [between("Latin “He took Simeon and bound him in their presence, and commanded his attendants” carries 42:24’s binding here; Hebrew, Greek and King James begin with the order.")]},

 '42:26': {
  'received': "They loaded the grain on their donkeys and left.",
  'explain': ("The versions agree."),
  'shared': ["They loaded their grain on their donkeys.", "They departed.", "They left that place."],
  'instructions': [ins(K, S, "The brothers set out for Canaan.")],
  'entries': [],
  'lost': [AGREE]},

 '42:27': {
  'received': "At the lodging place one opened his sack to feed his donkey and saw his silver at its mouth.",
  'explain': ("The first discovery, on the road; the rest in 42:35. The Hebrew says his donkey, his silver; the Greek his donkeys, his bundle of silver."),
  'shared': ["One of them opened his sack to feed his donkey at the lodging place.", "He saw his silver.", "It was in the mouth of his sack."],
  'instructions': [ins(K, S, "One brother found his silver returned.")],
  'entries': [],
  'lost': [between("Hebrew la-chamoro, “to his donkey,” is Greek tois onois autou, “to his donkeys”; Hebrew kaspo, “his silver,” is Greek ton desmon tou argyriou autou, “his bundle of silver”; Latin and King James follow the Hebrew.")]},

 '42:28': {
  'received': "My silver is returned, here in my sack! Their hearts failed and they trembled: What is this God has done to us?",
  'explain': ("The Hebrew idiom is their heart went out; the Greek their hearts were astonished; the Latin astonished and troubled. What has God done: the first time they name God in the story. The Hebrew-column rendering was corrected today."),
  'shared': ["My silver has been returned; here it is in my sack!", "Their hearts failed and they were afraid.", "What is this that God has done to us?"],
  'instructions': [ins(K, S, "The brothers feared a trap from God."), ins(W, R, "“What is this that God has done to us?” Returned silver terrifies men who once pocketed silver for a brother; a gift reads as judgment to a guilty conscience.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew va-yetze libbam, “and their heart went out,” is Greek kai exestē hē kardia autōn, “and their heart was astonished”; Latin “Astonished and troubled,” King James “their heart failed them.”")]},

 '42:29': {
  'received': "They came to Jacob in Canaan and told him all that had happened.",
  'explain': ("The versions agree."),
  'shared': ["They came to their father Jacob in the land of Canaan.", "They reported to him.", "All that had happened to them."],
  'instructions': [ins(K, S, "The brothers reported to Jacob.")],
  'entries': ['jacob', 'canaan'],
  'lost': [AGREE]},

 '42:30': {
  'received': "The lord of the land spoke harshly and treated us as spies.",
  'explain': ("The Greek adds placed us in custody; the Latin thought we were spies."),
  'shared': ["The man who is lord of the land spoke harshly to us.", "He treated us.", "As spies of the land."],
  'instructions': [ins(K, S, "The brothers described Joseph’s treatment.")],
  'entries': [],
  'lost': [keeps("An added kai etheto hēmas en phylakē, “and placed us in custody,” in the Greek."), between("Latin “thought we were spies” and King James “took us for spies” follow the Hebrew.")]},

 '42:31': {
  'received': "We told him we are honest men, not spies.",
  'explain': ("The versions agree; the Greek men of peace."),
  'shared': ["We said to him.", "We are honest men.", "We are not spies."],
  'instructions': [ins(K, S, "The brothers repeated their defence.")],
  'entries': [],
  'lost': [between("Hebrew kenim is Greek eirēnikoi, “peaceful”; Latin “peaceful men … plotting no schemes”; King James “true men.”")]},

 '42:32': {
  'received': "We are twelve brothers of one father; one is no more and the youngest is with our father in Canaan.",
  'explain': ("The versions agree."),
  'shared': ["We are twelve brothers, sons of our father.", "One is no more.", "The youngest is with our father in Canaan."],
  'instructions': [ins(K, S, "The brothers repeated their account of the family.")],
  'entries': ['canaan'],
  'lost': [AGREE]},

 '42:33': {
  'received': "The lord of the land said: leave one brother with me, take grain for your households, and go;",
  'explain': ("Retold, with the hungry households. The Latin says the food your households need; the Greek the grain purchased."),
  'shared': ["The man who rules the land said, By this I will know you are honest.", "Leave one brother with me and take grain for your hungry households.", "And go."],
  'instructions': [ins(K, S, "The brothers relayed Joseph’s terms.")],
  'entries': [],
  'lost': [between("Hebrew ra‘avon batekhem, “the famine of your houses,” is Greek ton agorasmon tēs sitodosias tou oikou hymōn, “the purchased grain of your house”; Latin “the food your households need,” King James “food for the famine of your households.”")]},

 '42:34': {
  'received': "bring your youngest brother and I will know you are honest; I will restore your brother and you may trade.",
  'explain': ("The Latin says the one held in bonds, buy whatever you wish; the Greek men of peace."),
  'shared': ["Bring your youngest brother to me.", "Then I will know you are not spies but honest men.", "I will restore your brother and you may trade in the land."],
  'instructions': [ins(K, S, "Benjamin’s coming would free Simeon."), ins(W, R, "The brothers must now ask their father for Benjamin, the one thing he refused; the road to Simeon runs through Jacob’s fear.")],
  'entries': [],
  'lost': [between("Latin “you may recover the one held in bonds and afterward have permission to buy whatever you wish” paraphrases; Hebrew, Greek and King James “I will deliver you your brother, and ye shall traffick in the land.”")]},

 '42:35': {
  'received': "Emptying their sacks, each found his bundle of silver; they and their father saw and were afraid.",
  'explain': ("The full discovery, before Jacob. The Latin says tied up at the mouth, when all were terrified together."),
  'shared': ["As they emptied their sacks, each man’s bundle of silver was in his sack.", "They and their father saw the bundles.", "They were afraid."],
  'instructions': [ins(K, S, "All the silver was found, alarming Jacob too."), ins(W, R, "Jacob sees the silver and hears of the man in Egypt; to him it is one more thing taken, to the reader it is the son he mourns sending gifts.")],
  'entries': [],
  'lost': [AGREE]},

 '42:36': {
  'received': "Jacob said: You have bereaved me; Joseph is gone, Simeon is gone, and you would take Benjamin. All this has come on me.",
  'explain': ("Jacob counts his losses and blames his sons, more truly than he knows. The Latin says Simeon is held in bonds, all these evils."),
  'shared': ["You have bereaved me of my children.", "Joseph is no more, Simeon is no more, and you would take Benjamin.", "All these things have come upon me."],
  'instructions': [ins(K, S, "Jacob refused to risk Benjamin."), ins(W, R, "“Me you have bereaved”: Jacob accuses the sons who did bereave him, of Joseph, and they cannot answer without confessing. The old man’s grief is his sons’ secret spoken aloud.")],
  'entries': ['jacob'],
  'lost': [between("Latin “Simeon is held in bonds … All these evils have fallen upon me” varies Hebrew ve-Shim‘on enennu, “and Simeon is not”; Greek and King James follow the Hebrew.")]},

 '42:37': {
  'received': "Reuben said: Kill my two sons if I do not bring him back; put him in my hand and I will return him.",
  'explain': ("Reuben’s desperate offer, grandsons for a son; Jacob ignores it. The versions agree."),
  'shared': ["Reuben spoke to his father.", "Kill my two sons if I do not bring him back to you.", "Put him in my hand and I will restore him."],
  'instructions': [ins(K, S, "Reuben offered his sons as surety for Benjamin."), ins(W, R, "Reuben offers what no father would take, and is not answered; the firstborn means well and misjudges again. Judah’s offer in 43:9 will be of himself.")],
  'entries': [],
  'lost': [AGREE]},

 '42:38': {
  'received': "My son shall not go with you; his brother is dead and he alone is left. If harm befell him you would bring my gray hairs down to Sheol in sorrow.",
  'explain': ("Jacob’s refusal, with the whole of his grief. He alone is left: of Rachel’s sons. The Hebrew says harm, my gray hairs, Sheol; the Greek sickness, my old age, Hades; the Latin the realm of the dead."),
  'shared': ["My son will not go down with you; his brother is dead and he alone is left.", "If harm befalls him on the way.", "You will bring my gray hairs down in sorrow to Sheol."],
  'instructions': [ins(K, S, "Jacob refused to send Benjamin."), ins(W, R, "“He alone is left”: ten sons stand before him and Jacob counts one. The favouritism that lost Joseph is intact, and Benjamin will go to Egypt in spite of it, by hunger.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew ason, “harm,” becomes Greek malakia, “sickness”; Hebrew sevati, “my gray hairs,” becomes to gēras mou, “my old age”; Hebrew She’olah is Greek eis hadou."), between("Latin “any misfortune … my gray hairs … the realm of the dead” and King James “mischief … my gray hairs … the grave” follow the Hebrew.")]},
 }
}
