# Study prose for Genesis 15 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 15,
 'chapterNote': (
  "The vision, the promise of an heir, the stars, the faith reckoned as righteousness and the covenant of the pieces are the same in every "
  "column. What varies is in the hard phrases. The Hebrew keeps “I am a shield for you,” the obscure “son of acquisition of my house,” “from "
  "your own body,” “he trusted in YHWH and he reckoned it to him,” Ur, “to possess,” Abram driving the birds away, deep sleep and great "
  "darkness, a single torch after dark, and “I have given this land.” The Greek keeps “I shield you” and a future reward, Masek as a woman’s "
  "name, “the one who comes from you,” “Abram believed God and it was reckoned,” the country of the Chaldeans, “to inherit,” Abram sitting "
  "down with the birds, a trance and a dark fear, a flame appearing at sunset with torches, “here” for the return, Hivites in the list, and "
  "“I will give.” The Latin and King James follow the Hebrew; Paul and Stephen follow the Greek wording in Romans 4 and Acts 7."),
 'verses': {

 '15:1': {
  'received': "In a vision the Lord told Abram not to fear, for he was his shield and his reward would be very great.",
  'explain': ("After the war, a vision, the first in Scripture, and the first word is “do not fear.” The Hebrew says I am a shield for you, a "
   "noun; the Greek I shield you, a verb, I hold my shield over you. The Hebrew can be read so that God himself is the reward; the Greek "
   "makes the reward future and very great. Abram has just refused Sodom’s spoil, and God promises his own wages."),
  'shared': ["The word of the Lord came to Abram in a vision.", "He was told not to fear.", "God is his protection and his reward is very great."],
  'instructions': [ins(K, S, "God promised Abram protection and a great reward."), ins(W, R, "The man who refused a king’s payment is paid by God; what is declined for God’s sake is never simply lost.")],
  'entries': ['abraham', 'lord-translation'],
  'lost': [
   loses("Hebrew anokhi magen lakh, “I am a shield for you,” is a noun; Greek egō hyperaspizō sou, “I shield you,” is a verb. Hebrew sekharkha harbeh me’od, “your reward very great,” can be read with God as the reward; Greek ho misthos sou polys estai sphodra makes the reward a future thing."),
   keeps("Greek horama, “vision,” is the word of Acts 9:10 and 16:9; misthos, “reward,” is the wages of Matthew 5:12 and Hebrews 11:6."),
   between("Latin “I am your protector and your exceedingly great reward” and King James “I am thy shield, and thy exceeding great reward” read God as the reward, with the Hebrew. Psalm 18:2 calls God a shield."),
  ]},

 '15:2': {
  'received': "Abram asked what God could give him, since he was childless and a servant of his house stood to inherit.",
  'explain': ("Abram answers the promise with his grief. He addresses God as Master and asks what any gift means to a man without a child. The "
   "heir is Eliezer of Damascus, but the Hebrew phrase for his status is obscure, “son of acquisition of my house,” read as heir or steward. "
   "The Greek takes the word as a woman’s name, Masek, and makes Eliezer her son, born in the household. Luke uses the Greek word for childless of the Sadducees’ question."),
  'shared': ["Abram asked what God would give him.", "He goes childless.", "The heir of his house is Eliezer of Damascus."],
  'instructions': [ins(K, S, "Abram, childless, saw his servant Eliezer as his heir."), ins(W, R, "Faith may answer a promise with a complaint; Abram tells God plainly what the promise has not yet changed.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew Adonai YHWH, “Lord YHWH,” becomes Greek Despota, “Master,” without the name. Hebrew ben-mesheq beiti, “son of acquisition of my house,” an obscure phrase read as heir or steward, becomes Greek ho huios Masek tēs oikogenous mou, “the son of Masek, my household-born woman”; mesheq is taken as a name and given a sex."),
   between("Latin “Lord God … the son of my household’s steward is this Eliezer” and King James “LORD God … the steward of my house is this Eliezer” keep the name and read steward. Greek Despota is the address of Luke 2:29 and Acts 4:24; ateknos is Luke 20:28–30."),
  ]},

 '15:3': {
  'received': "Abram repeated that God had given him no offspring, so a man of his household would inherit.",
  'explain': ("The complaint is stated a second time, more bluntly: you have given me no seed, and a slave will be my heir. The Hebrew says a "
   "son of my house; the Greek a man born in my household. The verb inherit is the key word of the chapter, from the Greek for an allotted "
   "share; Paul says the promise that Abraham would be heir came by faith, not the Law."),
  'shared': ["God has given Abram no offspring.", "A member of his household will inherit.", "Abram states the problem to God."],
  'instructions': [ins(K, S, "Abram told God that a household servant would be his heir."), ins(W, R, "Saying the hard thing twice is not unbelief; Abram’s honesty is the ground on which the promise is spoken again.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew hen, “look,” is Greek epeidē, “since”; Hebrew ben-beiti, “son of my house,” is Greek ho oikogenēs mou, “my household-born man.” Latin and King James follow the Hebrew. Greek klēronomēsei, “will inherit,” is the word of Romans 4:13 and Galatians 3:18.")]},

 '15:4': {
  'received': "The Lord answered that the servant would not inherit, but a son of Abram’s own body would.",
  'explain': ("The answer is direct: not this man, but one who comes from you. The Hebrew says from your own body, literally your inward parts; "
   "the Greek says simply from you. The Hebrew introduces the answer with “behold, the word of YHWH”; the Greek with “immediately a voice "
   "of the Lord.” The promise of 12:2 becomes a promise of a son."),
  'shared': ["The word of the Lord came to Abram.", "This man will not be his heir.", "One who comes from Abram himself will inherit."],
  'instructions': [ins(K, S, "God promised Abram an heir from his own body."), ins(W, R, "God answers the complaint by narrowing the promise: not a nation in general, but a son in particular.")],
  'entries': ['abraham', 'lord-translation'],
  'lost': [
   loses("Hebrew ve-hinneh devar-YHWH, “and behold, the word of YHWH,” becomes Greek kai eutheōs phōnē kyriou, “and immediately a voice of the Lord”; Hebrew mi-me‘ekha, “from your inward parts,” becomes Greek ek sou, “from you.” The bodily term and the word-of-the-Lord formula are both gone."),
   between("Latin “at once the word of the Lord … from your own body” and King James “behold, the word of the LORD … out of thine own bowels” keep the body; the Latin shares the Greek “at once.”"),
  ]},

 '15:5': {
  'received': "God took Abram outside to count the stars, and told him his offspring would be as many.",
  'explain': ("The promise is given in the night sky. Abram is brought out of his tent and told to count the stars if he can; so shall his "
   "offspring be. Numbering the stars belongs to God alone in the Psalms. The dust of 13:16 becomes stars. The versions agree, with small "
   "differences in who is addressed."),
  'shared': ["God brought Abram outside.", "He told him to count the stars if he could.", "So shall his offspring be."],
  'instructions': [ins(K, S, "Abram’s offspring were promised to be as countless as the stars."), ins(W, R, "The childless man is shown the sky; the promise is made as large as the thing he cannot count.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew habbet-na ha-shamaymah, “look now toward the heavens,” is Greek anablepson eis ton ouranon, “look up to heaven.” Hebrew “said to him” is at the end, Greek at the beginning. Latin and King James agree. Psalm 147:4 and Hebrews 11:12 take up the stars.")]},

 '15:6': {
  'received': "Abram believed the Lord, and it was reckoned to him as righteousness.",
  'explain': ("The first time Scripture says anyone believed. The Hebrew verb is related to amen, firm and reliable; Abram leaned his weight on "
   "YHWH, and God counted it to him as righteousness. The Hebrew leaves both actors as “he”; the Greek names Abram, says God, and makes the "
   "reckoning passive, the form Paul quotes in Romans 4 and Galatians 3, noting that it comes before circumcision. James quotes it for faith completed by works."),
  'shared': ["Abram believed the Lord.", "It was reckoned to him.", "It was reckoned as righteousness."],
  'instructions': [ins(K, S, "Abram’s faith was counted to him as righteousness."), ins(W, R, "Righteousness is reckoned before any work is done or any sign given; the order of events is the whole argument of Romans 4.")],
  'entries': ['abraham', 'yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew ve-he’emin ba-YHWH va-yachsheveha lo tsedaqah, “and he trusted in YHWH and he reckoned it to him righteousness,” has pronouns for both and an active verb; Greek kai episteusen Abram tō theō kai elogisthē autō eis dikaiosynēn, “and Abram believed God and it was reckoned to him as righteousness,” names Abram, says God, and makes the reckoning passive."),
   keeps("Episteusen and elogisthē are the words Paul quotes in Romans 4:3 and Galatians 3:6 and James in 2:23; the New Testament argument runs on the Greek wording."),
   between("Latin “Abram believed God, and it was reckoned” follows the Greek; King James “he believed in the LORD; and he counted it to him” follows the Hebrew."),
  ]},

 '15:7': {
  'received': "God named himself as the one who brought Abram out of Ur of the Chaldeans to give him the land.",
  'explain': ("God identifies himself by what he has done, in words that will open the Ten Commandments: I am the one who brought you out. "
   "The Hebrew says I am YHWH, from Ur of the Chaldeans, to possess; the Greek I am God, from the country of the Chaldeans, to inherit, "
   "the wording Stephen uses. The land is promised again before the covenant rite."),
  'shared': ["God declares who he is.", "He brought Abram out of the land of the Chaldeans.", "He gives him this land to possess."],
  'instructions': [ins(K, S, "God who brought Abram from the Chaldeans promised him the land."), ins(W, R, "God names himself by a past rescue before promising a future gift; what he has done is the pledge of what he will do.")],
  'entries': ['abraham', 'ur', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew ani YHWH, “I am YHWH,” becomes Greek egō ho theos, “I am God”; Hebrew me-Ur Kasdim, “from Ur of the Chaldeans,” becomes ek chōras Chaldaiōn, “from the country of the Chaldeans”; Hebrew le-rishtah, “to possess,” becomes klēronomēsai, “to inherit.”"),
   between("Latin “I am the Lord who brought you out of Ur … to possess” and King James “I am the LORD … Ur of the Chaldees … to inherit” keep the name and Ur. Exodus 20:2 and Acts 7:4 are the echoes."),
  ]},

 '15:8': {
  'received': "Abram asked how he could know that he would possess the land.",
  'explain': ("Faith asks for a sign. The man just reckoned righteous for believing now asks how he can be sure. The Hebrew says Lord YHWH; "
   "the Greek Master Lord, keeping both titles this time; the Latin Lord God. Possess and inherit continue as before."),
  'shared': ["Abram addressed God as Lord.", "He asked by what he would know.", "The question is about possessing the land."],
  'instructions': [ins(K, S, "Abram asked God for assurance about the land."), ins(W, R, "Belief and the request for a sign stand two verses apart; the one does not cancel the other, and God answers the request with a covenant.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew Adonai YHWH is Greek Despota kyrie, “Master Lord,” with both titles where 15:2 had one; Hebrew irashennah, “I will possess it,” is Greek klēronomēsō, “I will inherit it.” Latin “Lord God … possess” and King James “LORD God … inherit” divide.")]},

 '15:9': {
  'received': "God told Abram to bring a heifer, a goat and a ram, each three years old, with a turtledove and a young pigeon.",
  'explain': ("The sign is a rite. Five creatures are called for, the same kinds later accepted for sacrifice under the Law, the birds being the "
   "offering of the poor that Mary and Joseph will bring. The three-year age follows the usual reading of the Hebrew form. The Hebrew says a "
   "young bird at the end; the Greek a pigeon without the age."),
  'shared': ["God told Abram to bring a three-year-old heifer, goat and ram.", "He was to bring a turtledove.", "He was to bring a young pigeon."],
  'instructions': [ins(C, S, "Bring a heifer, a goat and a ram, each three years old, with a turtledove and a pigeon."), ins(W, R, "The sign Abram asked for is a sacrifice; assurance comes through an act of worship, not an argument.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew gozal, “a young bird,” usually a young pigeon, is Greek peristeran, “a pigeon,” without the age; Hebrew qach li, “take for me,” is Greek labe moi, “bring me.” Latin “a pigeon” and King James “a young pigeon” divide. Leviticus 1:14 and Luke 2:24 take up the birds.")]},

 '15:10': {
  'received': "Abram cut the animals in two and laid the halves facing each other, but did not divide the birds.",
  'explain': ("Abram does as told. The animals are halved and the halves set opposite each other, making a path between; the birds are left "
   "whole. The Hebrew idiom for making a covenant is to cut one, and the cut pieces are its picture. The versions agree."),
  'shared': ["Abram brought all the animals.", "He divided them down the middle and laid the halves opposite each other.", "He did not divide the birds."],
  'instructions': [ins(K, S, "Abram prepared the divided animals for the covenant rite.")],
  'entries': ['abraham', 'term-covenant'],
  'lost': [between("Hebrew va-yevatter otam ba-tavekh, “he cut them in the middle,” is Greek dieilen auta mesa, “divided them down the middle”; Hebrew “he did not cut the birds,” with a collective singular, is Greek “he did not divide the birds.” Latin and King James agree in sense.")]},

 '15:11': {
  'received': "Birds of prey came down on the carcasses, and Abram kept watch over them.",
  'explain': ("The pieces lie exposed and scavengers come. The Hebrew, Latin and King James have Abram drive the birds away; the Greek has him "
   "sit down with them, which can be read as a vigil beside the divided pieces. The two actions differ, and the Greek should not be read "
   "as adding a rite. Jesus’ parable has birds snatching the seed from the path."),
  'shared': ["Birds came down on the carcasses.", "Abram was present at the pieces.", "He guarded the offering."],
  'instructions': [ins(K, S, "Abram stayed by the sacrifice while birds of prey threatened it."), ins(W, R, "The covenant offering must be guarded before God comes to it; waiting on God includes keeping the scavengers off.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew va-yashev otam Avram, “and Abram drove them away,” describes repelling the birds of prey (ayit). Greek kai synekathisen autois Abram, “and Abram sat down with them,” describes staying; the driving away is gone, and the birds are simply ornea, “birds.” The Greek adds “on their divided pieces.”"),
   between("Latin “Abram drove them away” and King James “Abram drove them away” follow the Hebrew. Matthew 13:4 and Deuteronomy 28:26 have birds on the fallen."),
  ]},

 '15:12': {
  'received': "At sunset a deep sleep fell on Abram, and a great dark dread came over him.",
  'explain': ("Night falls and so does sleep, the deep sleep of 2:21 in the Hebrew, a trance in the Greek, as there. Then terror and darkness, "
   "which the Hebrew gives as two nouns, a dread, a great darkness, and the Greek as one, a great dark fear. The darkness goes before the "
   "word about centuries of slavery."),
  'shared': ["The sun was setting.", "A deep sleep fell on Abram.", "A great dark fear fell on him."],
  'instructions': [ins(K, S, "Abram received the covenant word in a God-sent sleep and dread."), ins(W, R, "The promise of the land comes wrapped in darkness and fear; God does not hide the cost from the one he blesses.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew tardemah, “deep sleep,” becomes Greek ekstasis, “trance,” as at 2:21; Hebrew eimah chashekhah gedolah, “a dread, a great darkness,” becomes Greek phobos skoteinos megas, “a great dark fear,” one noun with adjectives."),
   between("Latin “a deep sleep … a great, dark dread” and King James “a deep sleep … an horror of great darkness” follow the Hebrew. Exodus 10:22 and Job 4:13–14 are the echoes."),
  ]},

 '15:13': {
  'received': "God told Abram that his offspring would be strangers, enslaved and afflicted in a foreign land for four hundred years.",
  'explain': ("The dark word is slavery. Egypt is not named, but the exodus is foretold: strangers in a land not theirs, serving and afflicted, "
   "four hundred years. The Hebrew has the descendants serve and then be afflicted; the Greek keeps the oppressors as subject of three "
   "verbs, enslave, mistreat, humble, and introduces the speech passively. Stephen quotes the verse; Exodus gives 430 years."),
  'shared': ["Abram is told to know for certain.", "His offspring will be strangers in a land not their own.", "They will be enslaved and afflicted four hundred years."],
  'instructions': [ins(K, S, "Abram’s descendants would suffer four hundred years as strangers before the promise was kept."), ins(W, R, "The promised people must first be slaves; the covenant includes the suffering, not only the land.")],
  'entries': ['abraham', 'egypt'],
  'lost': [
   loses("Hebrew va-yomer le-Avram, “he said to Abram,” becomes Greek kai errethē pros Abram, “it was said to Abram”; Hebrew va-avadum ve-innu otam, “they will serve them and they will afflict them,” two subjects, becomes Greek doulōsousin autous kai kakōsousin autous kai tapeinōsousin autous, “they will enslave, mistreat and humble them,” one subject, three verbs."),
   between("Latin “he was told … subject them to slavery and afflict them” shares the passive and the oppressor-subject; King James “he said … shall serve them; and they shall afflict them” follows the Hebrew. Acts 7:6 quotes; Exodus 12:40 and Galatians 3:17 give 430."),
  ]},

 '15:14': {
  'received': "God will judge the nation they serve, and afterward they will come out with great possessions.",
  'explain': ("Judgement on the oppressor and a rich departure: the exodus in one sentence, fulfilled when Israel leaves Egypt with gold, "
   "silver and flocks. The Greek adds “here,” pointing the return to the land where Abram stands, and says baggage for possessions. The "
   "Hebrew leaves the direction implied."),
  'shared': ["God will judge the nation they serve.", "Afterward they will come out.", "They will come out with great possessions."],
  'instructions': [ins(K, S, "God promised to judge the enslaving nation and bring Abram’s offspring out enriched."), ins(W, R, "The oppressor is judged by God, not fought by the slaves; deliverance and justice are one act.")],
  'entries': ['egypt'],
  'lost': [
   keeps("Greek adds hōde, “here,” to the coming out, making the return to this land explicit; Hebrew bi-rkhush gadol, “with great possessions,” is Greek meta aposkeuēs pollēs, “with much baggage.”"),
   between("Latin and King James “come out with great possessions / substance” follow the Hebrew without “here.” Exodus 12:35–38 is the fulfilment."),
  ]},

 '15:15': {
  'received': "Abram himself would die in peace and be buried at a good old age.",
  'explain': ("The long future for the descendants is set beside Abram’s own end: he will go to his fathers in peace and be buried old. The "
   "promise is fulfilled at his death at a hundred and seventy-five, and the same Greek phrase marks the death of David. The versions agree."),
  'shared': ["Abram will go to his fathers in peace.", "He will be buried.", "He will die at a good old age."],
  'instructions': [ins(K, S, "Abram was promised a peaceful death in old age."), ins(W, R, "Abram will not see the slavery or the land; his share of the promise is a good death, and he is told so plainly.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew tavo, “you will go,” is Greek apeleusē, “you will depart”; Hebrew tiqqaver, “you will be buried,” is Greek taphesis, “buried,” a participle. Latin and King James agree. Greek gērei kalō is the phrase of 25:8 and 1 Chronicles 29:28.")]},

 '15:16': {
  'received': "In the fourth generation they will return, when the iniquity of the Amorites is complete.",
  'explain': ("The delay is explained: the Amorites’ sin is not yet full. A generation here seems to match a long lifetime; Levi, Kohath, "
   "Amram, Moses span four from the descent into Egypt to the exodus. The Hebrew says iniquity, collective; the Greek sins, plural; the "
   "Latin iniquities. God waits on the Amorites as well as on Israel."),
  'shared': ["They will return here in the fourth generation.", "The reason is the iniquity of the Amorites.", "That iniquity is not yet complete."],
  'instructions': [ins(K, S, "The return to the land waited on the fullness of the Amorites’ sin."), ins(W, R, "God’s timing for his people is also his patience with their enemies; the land is not given until its holders have had their time.")],
  'entries': [],
  'lost': [between("Hebrew avon ha-Emori, “the iniquity of the Amorite,” singular and collective, is Greek hai hamartiai tōn Amorraiōn, “the sins of the Amorites,” plural; Hebrew shalem, “complete,” is Greek anapeplērōntai, “have been filled up.” Latin “iniquities … reached their fullness” and King James “iniquity … not yet full” divide. Exodus 6:16–20 gives the four generations.")]},

 '15:17': {
  'received': "After sunset, in the dark, a smoking furnace and a flaming torch passed between the pieces.",
  'explain': ("God makes the covenant alone. Only he, shown by the fire, walks between the pieces while Abram sleeps; Hebrews says he swore "
   "by himself. The Hebrew sets the scene after sunset in deep darkness, with one torch; the Greek has a flame appear as the sun sets, "
   "and torches in the plural. Fire and smoke will mark God’s presence at the bush and at Sinai."),
  'shared': ["The sun had set.", "A smoking furnace appeared.", "Fire passed between the divided pieces."],
  'instructions': [ins(K, S, "God alone passed between the pieces, binding himself to the covenant."), ins(W, R, "Abram sleeps while God walks the path of the oath; this covenant rests on God’s promise, not on Abram’s performance.")],
  'entries': ['term-covenant'],
  'lost': [
   loses("Hebrew va-alatah hayah, “and deep darkness came,” becomes Greek phlox egeneto, “a flame appeared”; darkness becomes fire. Hebrew lappid esh, “a torch of fire,” singular, becomes Greek lampades pyros, “fiery torches,” plural. Hebrew “the sun had set” becomes Greek “as the sun was setting.”"),
   between("Latin “when the sun had set and deep darkness came … a flaming torch” and King James “when the sun went down, and it was dark … a burning lamp” follow the Hebrew. Hebrews 6:13–18 reads the oath; Exodus 3:2 and 19:18 bring the fire."),
  ]},

 '15:18': {
  'received': "That day the Lord made a covenant with Abram, giving his offspring the land from the river of Egypt to the Euphrates.",
  'explain': ("The covenant is named and its content stated: the land from the brook of Egypt to the great river. The Hebrew idiom is to cut a "
   "covenant, matching the cut animals; the Greek word also means a will, and Hebrews and Galatians use both senses. The Hebrew says “I "
   "have given this land,” a grant already made; the Greek and Latin say “I will give.” The borders match those of Numbers and Deuteronomy."),
  'shared': ["On that day the Lord made a covenant with Abram.", "The land is given to his offspring.", "It runs from the river of Egypt to the river Euphrates."],
  'instructions': [ins(K, S, "God’s covenant with Abram promised the land from Egypt’s river to the Euphrates."), ins(W, R, "The Hebrew says the land is already given; a covenant turns a promise into a deed before the heir is born.")],
  'entries': ['term-covenant', 'abraham', 'egypt'],
  'lost': [
   loses("Hebrew natatti, “I have given,” a completed grant, becomes Greek dōsō, “I will give,” a future one. Hebrew YHWH is “the Lord.” Hebrew karat berit, “cut a covenant,” is Greek dietheto diathēkēn, “disposed a covenant,” losing the cutting."),
   keeps("Greek diathēkē, “covenant” and also “will,” is the word Galatians 3:15–17 and Hebrews 9:16 play on; the Greek reader hears both senses."),
   between("Latin “I will give” follows the Greek; King James “have I given” the Hebrew. Numbers 34:5 and Deuteronomy 1:7 give the borders; Revelation 9:14 returns to the Euphrates."),
  ]},

 '15:19': {
  'received': "The land of the Kenites, the Kenizzites and the Kadmonites,",
  'explain': ("The peoples of the land are listed, ten in the Hebrew. The Kenites were later linked with smiths; Moses’ father-in-law and Jael’s "
   "husband were Kenites. Caleb the faithful spy is called a Kenizzite. The Kadmonites, “easterners,” are named nowhere else. All versions agree."),
  'shared': ["The Kenites are named.", "The Kenizzites are named.", "The Kadmonites are named."],
  'instructions': [ins(K, S, "The promised land included the territories of the Kenites, Kenizzites and Kadmonites.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James agree; Greek Kenaious, Kenezaious, Kedmōnaious are the Hebrew names in Greek form. Judges 1:16 and Numbers 32:12 are the Kenites and Caleb.")]},

 '15:20': {
  'received': "the Hittites, the Perizzites and the Rephaim,",
  'explain': ("Three more: the Hittites, descendants of Heth from whom Abraham will buy Sarah’s grave; the Perizzites of the open villages; "
   "and the Rephaim, whom the Greek here transliterates rather than calling giants as it did in 14:5. All versions agree."),
  'shared': ["The Hittites are named.", "The Perizzites are named.", "The Rephaim are named."],
  'instructions': [ins(K, S, "The Hittites, Perizzites and Rephaim held parts of the promised land.")],
  'entries': ['rephaim'],
  'lost': [keeps("Greek Raphain keeps the Hebrew name Rephaim here, unlike gigantes in 14:5; the Greek is inconsistent between the two verses, and here agrees with the Hebrew."), between("Latin adds quoque, “also,” before the Rephaim; King James “Rephaims.” Genesis 23:3 and 2 Samuel 11:3 are Hittites; Deuteronomy 3:11 is Og the Rephaite.")]},

 '15:21': {
  'received': "the Amorites, the Canaanites, the Girgashites and the Jebusites.",
  'explain': ("The list closes with the Amorites whose sin was not yet full, the Canaanites, the Girgashites and the Jebusites of the future "
   "Jerusalem. The Hebrew, Latin and King James name four peoples here, ten in all; the Greek adds the Hivites, making eleven. The addition is "
   "a people, not a second rendering of one name."),
  'shared': ["The Amorites and Canaanites are named.", "The Girgashites are named.", "The Jebusites are named."],
  'instructions': [ins(K, S, "The Amorites, Canaanites, Girgashites and Jebusites complete the list of the land’s peoples."), ins(W, R, "Ten peoples hold the land Abram is promised; the gift is as hard as it is large.")],
  'entries': ['canaan', 'jerusalem'],
  'lost': [
   keeps("Greek adds kai tous Euaious, “and the Hivites,” between the Canaanites and the Girgashites; the Hebrew list has no Hivites in this verse, though they appear in other lists (Exodus 3:8)."),
   between("Latin and King James give the four of the Hebrew. Amos 2:9 recalls the Amorites; 2 Samuel 5:6–7 the Jebusites."),
  ]},
 }
}
