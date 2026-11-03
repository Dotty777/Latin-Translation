# Study prose for Genesis 16 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 16,
 'chapterNote': (
  "Sarai’s plan, Hagar’s flight, the angel at the spring and the birth of Ishmael are the same story in every column. What varies is who "
  "does what in two sentences and how Hagar’s hard sayings are handled. The Hebrew keeps Sarai hoping to be “built up” through Hagar, Hagar "
  "seeing she has conceived and holding her mistress in contempt, the wild-donkey man, the name El-roi with its riddling question, and the "
  "well Beer-lahai-roi. The Greek keeps Abram having children through Hagar as the purpose, Sarai “dishonoured before her” with Sarai as the "
  "one who saw, God for YHWH in Sarai’s appeal, a “wild man,” “You are God who looked upon me … I saw before me the one who appeared to me,” "
  "and a well named “where I saw before me.” The Latin and King James follow the Hebrew; the Latin has Hagar seeing “the back of Him who sees me.”"),
 'verses': {

 '16:1': {
  'received': "Sarai had borne Abram no children, but she had an Egyptian slave named Hagar.",
  'explain': ("Ten years after the promise there is still no child, and the chapter opens with the fact and with the woman who will be the "
   "answer Sarai devises. Hagar is Egyptian, perhaps acquired in chapter 12, and her name has been linked to the Hebrew for stranger. Paul "
   "will make her a figure of Sinai and the covenant of slavery. All versions agree."),
  'shared': ["Sarai had borne Abram no children.", "She had an Egyptian slave woman.", "Her name was Hagar."],
  'instructions': [ins(K, S, "Sarai was still childless and owned an Egyptian slave, Hagar."), ins(W, R, "The chapter starts from the unfulfilled promise; what follows is what people do while God waits.")],
  'entries': ['sarah', 'hagar', 'abraham', 'egypt'],
  'lost': [between("Hebrew shifchah and Greek paidiskē are both “slave woman”; Latin ancilla and King James “handmaid” soften the English. Galatians 4:24–25 is Paul’s reading.")]},

 '16:2': {
  'received': "Sarai, kept from bearing by the Lord, told Abram to take Hagar so that children might come through her, and Abram agreed.",
  'explain': ("Sarai proposes what ancient marriage contracts allowed: a barren wife gives her slave to her husband and counts the child as "
   "hers; Rachel and Leah will do the same. The Hebrew has Sarai hope to be “built up” through Hagar, an uncertain hope for herself; the "
   "Greek states the purpose as Abram having children through her. The Hebrew says YHWH kept her from bearing; Abram listened to her voice."),
  'shared': ["Sarai says the Lord has kept her from bearing.", "She tells Abram to go in to her slave woman.", "Abram did as Sarai said."],
  'instructions': [ins(K, S, "Sarai gave Hagar to Abram to obtain a child, and Abram consented."), ins(W, R, "A lawful custom is used to hurry God’s promise; listening to a wife’s voice echoes 3:17, and the result will be grief for all three.")],
  'entries': ['sarah', 'hagar', 'abraham', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew ulai ibbaneh mimmennah, “perhaps I may be built up through her,” is Sarai’s uncertain hope for herself, with a pun on ben, son; Greek hina teknopoiēsēs ex autēs, “so that you may have children through her,” makes Abram the beneficiary and the purpose certain. Hebrew na, “please,” is absent; YHWH is “the Lord.”"),
   between("Latin “perhaps through her at least I may receive children” and King James “it may be that I may obtain children by her” keep Sarai as the hoped-for beneficiary; the Latin ends “when he agreed to her request,” running into 16:3. Genesis 30:3 and 30:9 repeat the custom."),
  ]},

 '16:3': {
  'received': "After ten years in Canaan, Sarai gave her Egyptian slave Hagar to Abram as a wife.",
  'explain': ("The date is given: ten years in the land since the promise of 12:4, with Sarai now about seventy-five. The plan comes from "
   "impatience with the delay. Hagar is given “as a wife,” a secondary wife; her status does not become Sarai’s. The versions agree, the "
   "Greek naming Abram and Sarai more fully and the Latin putting the ten years last."),
  'shared': ["Abram had lived ten years in Canaan.", "Sarai took Hagar her Egyptian slave.", "She gave her to Abram as a wife."],
  'instructions': [ins(K, S, "Sarai gave Hagar to Abram as a wife ten years after their arrival in Canaan.")],
  'entries': ['sarah', 'hagar', 'abraham', 'canaan'],
  'lost': [between("Hebrew and Greek agree closely, the Greek repeating “Abram’s wife” and “her husband Abram.” Latin “to her husband as a wife, ten years after they had begun living in the land” drops the names; King James follows the Hebrew.")]},

 '16:4': {
  'received': "Abram went in to Hagar and she conceived; seeing that she had conceived, she looked down on her mistress.",
  'explain': ("Hagar conceives at once where Sarai failed for years, and the household order turns over. The Hebrew says that when Hagar saw she "
   "had conceived, her mistress became contemptible in her eyes; the Greek that her mistress was dishonoured before her, without making "
   "Hagar the actor; the Latin says plainly she despised her mistress. The text does not say Sarai conceived."),
  'shared': ["Abram went in to Hagar.", "She conceived.", "Her mistress lost standing in her eyes."],
  'instructions': [ins(K, S, "Hagar conceived and her mistress was despised in her eyes."), ins(W, R, "The plan works and ruins the peace at once; a child by contrivance brings contempt before it brings joy.")],
  'entries': ['hagar', 'sarah'],
  'lost': [
   loses("Hebrew va-teqal gevirtah be-eineha, “her mistress became light in her eyes,” has Hagar’s eyes as the measure; Greek ētimasthē hē kyria enantion autēs, “the mistress was dishonoured before her,” removes Hagar as the one who judges. Hebrew “when she saw she had conceived” is Greek “she saw she was pregnant.”"),
   between("Latin “she despised her mistress” makes Hagar the actor outright; King James “her mistress was despised in her eyes” keeps the Hebrew. Greek synelaben, “conceived,” is the word of Luke 1:24."),
  ]},

 '16:5': {
  'received': "Sarai blamed Abram for the wrong done to her, since Hagar now despised her, and called on the Lord to judge between them.",
  'explain': ("Sarai turns on Abram. In the Hebrew she says the wrong is upon him, that she gave her slave into his embrace, and that when Hagar "
   "saw she had conceived Sarai became contemptible to her; she calls YHWH to judge. The Greek shifts the seeing to Sarai, “when I saw that "
   "she was pregnant, I was dishonoured,” opens with “I am wronged because of you,” and has God judge. The Latin has Hagar hold Sarai in contempt."),
  'shared': ["Sarai blamed Abram for the wrong done to her.", "She had given her slave woman into his embrace and was now despised.", "She called on the Lord to judge between them."],
  'instructions': [ins(K, S, "Sarai held Abram responsible for the contempt she suffered and appealed to God."), ins(W, R, "The one who made the plan blames the one who agreed to it; appealing to God’s judgement is easier than owning the scheme.")],
  'entries': ['sarah', 'hagar', 'abraham', 'yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew chamasi alekha, “my wrong is upon you,” becomes Greek adikoumai ek sou, “I am wronged because of you.” Hebrew va-tere ki haratah, “when she saw that she had conceived,” with Hagar seeing, becomes Greek idousa de hoti en gastri echei, a participle naturally attached to Sarai, “when I saw that she was pregnant.” Hebrew YHWH judge becomes Greek ho theos, “God.”"),
   between("Latin “you deal unjustly with me … when she saw that she had conceived, she held me in contempt … the Lord judge” and King James “my wrong be upon thee … when she saw that she had conceived, I was despised … the LORD judge” keep Hagar as the one seeing and the name."),
  ]},

 '16:6': {
  'received': "Abram left Hagar in Sarai’s power, and when Sarai mistreated her, Hagar fled.",
  'explain': ("Abram declines to judge and hands Hagar over: she is in your hand, do as you please. Sarai afflicts her, the Hebrew verb that "
   "will describe Israel in Egypt, and the Egyptian slave runs toward Egypt. The versions agree; the Latin drops “from her” at the end."),
  'shared': ["Abram told Sarai that Hagar was in her hand.", "He told her to do as she pleased.", "Sarai afflicted Hagar, and Hagar fled from her."],
  'instructions': [ins(K, S, "Abram left Hagar to Sarai, who treated her harshly until she fled."), ins(W, R, "Abram washes his hands and a pregnant woman runs into the desert; neutrality between a mistress and a slave is not neutral.")],
  'entries': ['hagar', 'sarah', 'abraham'],
  'lost': [between("Hebrew va-te‘anneha, “she afflicted her,” the verb of Exodus 1:11–12, is Greek ekakōsen autēn, “she mistreated her”; Hebrew mi-paneha, “from her face,” is Greek apo prosōpou autēs. Latin “she fled” drops the phrase; King James “fled from her face” keeps it.")]},

 '16:7': {
  'received': "The angel of the Lord found Hagar by a spring in the wilderness on the way to Shur.",
  'explain': ("The first appearance of the angel of the Lord in Scripture, and it is to an Egyptian slave woman. He finds her by a spring in the "
   "wilderness of Shur, the desert on Egypt’s frontier whose name means wall; she is heading home. The Hebrew says messenger, the Greek angel, "
   "the same word in each language. God’s messenger goes looking for the runaway, as the shepherd goes after the lost sheep."),
  'shared': ["The angel of the Lord found Hagar.", "She was by a spring of water in the wilderness.", "It was on the way to Shur."],
  'instructions': [ins(K, S, "The angel of the Lord sought out Hagar in the wilderness."), ins(W, R, "God’s first angel appears to a slave, a foreigner and a runaway; the search for the lost begins at the bottom of the household.")],
  'entries': ['angel-of-the-lord', 'hagar'],
  'lost': [between("Hebrew mal’akh YHWH and Greek angelos kyriou are both “messenger of the Lord”; the English article, a or the, does not decide who the figure is. Latin adds “in the desert” to the road; King James “fountain” for spring. Exodus 15:22 and Genesis 25:18 name Shur.")]},

 '16:8': {
  'received': "The angel asked Hagar, Sarai’s slave, where she had come from and where she was going; she said she was fleeing her mistress.",
  'explain': ("The angel knows her name and her place, and asks two questions that are really one: where from, where to. Hagar answers only the "
   "first; she has no destination. She still calls Sarai her mistress, accepting her place even while running. The Greek repeats the angel of "
   "the Lord as speaker; the Hebrew says simply “he said.”"),
  'shared': ["The angel addressed Hagar as Sarai’s slave woman.", "He asked where she had come from and where she was going.", "She said she was fleeing from her mistress Sarai."],
  'instructions': [ins(K, S, "Hagar admitted to the angel that she was fleeing from Sarai."), ins(W, R, "“Where are you going?” is the question Hagar cannot answer; flight has a from but no to.")],
  'entries': ['angel-of-the-lord', 'hagar', 'sarah'],
  'lost': [
   keeps("Greek repeats ho angelos kyriou, “the angel of the Lord,” as speaker and autē, “to her,” where the Hebrew has va-yomar, “he said”; the Greek makes the speaker explicit a second time."),
   between("Latin “and said to her” and King James “he said” follow the Hebrew. Greek kyrias, “mistress,” is the feminine of kyrios; Psalm 123:2 uses it."),
  ]},

 '16:9': {
  'received': "The angel told Hagar to return to her mistress and submit to her.",
  'explain': ("The hard command: go back, and submit under her hands. The Hebrew verb recalls the affliction of verse 6, the Greek the humiliation "
   "of verse 11; Hagar is to accept what she fled. The word for return is the prophets’ word for Israel’s return to God; Paul sends the runaway "
   "slave Onesimus back to Philemon. The versions agree."),
  'shared': ["The angel of the Lord spoke to Hagar.", "He told her to return to her mistress.", "He told her to submit under her hands."],
  'instructions': [ins(C, S, "Return to your mistress and submit to her."), ins(W, R, "Return comes before the promise; Hagar is sent back into the hard place with a blessing to carry.")],
  'entries': ['angel-of-the-lord', 'hagar'],
  'lost': [between("Hebrew hit‘anni tachat yadeha, “submit under her hands,” uses the root of the affliction in 16:6; Greek tapeinōthēti hypo tas cheiras autēs, “be humbled under her hands,” uses the root of the humiliation in 16:11. Latin “humble yourself” and King James “submit thyself” agree in sense. Philemon 12 is the echo.")]},

 '16:10': {
  'received': "The angel promised to multiply Hagar’s offspring beyond counting.",
  'explain': ("The angel speaks in the first person, as God: I will greatly multiply your offspring. It is the promise given to Abram, now given "
   "to the slave woman in her own right. The Greek doubles the verb to match the Hebrew emphasis. The versions agree."),
  'shared': ["The angel of the Lord spoke again.", "He will greatly multiply her offspring.", "They will be too many to count."],
  'instructions': [ins(K, S, "Hagar received God’s promise of innumerable descendants."), ins(W, R, "The promise to Abram does not run only through Sarai; God speaks the same words to the woman the household cast out.")],
  'entries': ['angel-of-the-lord', 'hagar'],
  'lost': [between("Hebrew harbah arbeh, “multiplying I will multiply,” is matched by Greek plēthynōn plēthynō; both say the offspring cannot be counted for multitude. Latin “again he said” drops the angel’s title; King James keeps it. Genesis 17:20 and 21:18 repeat the promise.")]},

 '16:11': {
  'received': "The angel announced that Hagar would bear a son named Ishmael, because the Lord had heard her affliction.",
  'explain': ("Ishmael, “God hears,” is the first person in Scripture named by God before birth, and the verse explains the name. The Hebrew says "
   "YHWH has heard your affliction; the Greek the Lord has listened to your humiliation, a slightly different shade of the same suffering. "
   "The announcement has the shape of Luke 1:13 and Matthew 1:21."),
  'shared': ["Hagar is pregnant and will bear a son.", "She is to name him Ishmael.", "The reason is that the Lord has heard her affliction."],
  'instructions': [ins(K, S, "God named Hagar’s son Ishmael because he heard her affliction."), ins(W, R, "The slave’s misery is heard and written into a name; God’s hearing is the first thing the child will be called.")],
  'entries': ['hagar', 'angel-of-the-lord', 'lord-translation'],
  'lost': [between("Hebrew onyekh, “your affliction,” is Greek tapeinōsei sou, “your humiliation”; Hebrew YHWH is “the Lord.” Latin “then he said … heard your affliction” and King James “the angel of the LORD said … heard thy affliction” follow the Hebrew. Hebrew Yishma‘el, “God hears,” is kept in all.")]},

 '16:12': {
  'received': "Ishmael would be a wild man, at odds with everyone, living opposite all his brothers.",
  'explain': ("The son’s character is foretold: untamed, in conflict with all, dwelling over against his kin. The Hebrew calls him a wild-donkey "
   "man, the animal of the open steppe; the Greek and Latin a wild man, losing the animal; the Latin has him pitch his tents opposite his "
   "brothers. “Opposite” may mean near, or in defiance; both are possible."),
  'shared': ["He will be a wild man.", "His hand will be against everyone and everyone’s against him.", "He will dwell opposite all his brothers."],
  'instructions': [ins(K, S, "Ishmael was foretold as a wild, independent man living among his kin."), ins(W, R, "Freedom and strife are promised together; the son of the runaway will be untamed as she was.")],
  'entries': [],
  'lost': [
   loses("Hebrew pere adam, “wild-donkey man,” is an animal image of the steppe (Job 39:5–8); Greek agroikos anthrōpos, “wild man,” “man of the field,” keeps the wildness and drops the donkey."),
   between("Latin “wild man … pitch his tents opposite” and King James “wild man … dwell in the presence of” both lose the donkey; the Latin adds the tents. Genesis 25:18 fulfils the dwelling."),
  ]},

 '16:13': {
  'received': "Hagar named the Lord who spoke to her the God who sees, for she had seen him and lived.",
  'explain': ("A slave woman gives God a name. The Hebrew name is El-roi, God of seeing or God who sees me, followed by a riddling question, "
   "“have I even here seen after the one who sees me?”, usually read as wonder at seeing and surviving. The Greek makes it plain: “You are "
   "God who looked upon me,” and “I saw before me the one who appeared to me.” The Latin has her see the back of him who sees her. None of the columns actually says she saw God’s back."),
  'shared': ["Hagar named the Lord who spoke to her.", "She called him the God who sees.", "She had seen the one who sees her."],
  'instructions': [ins(K, S, "Hagar named God as the one who sees, having seen him herself."), ins(W, R, "To be seen by God is Hagar’s whole comfort; the unseen slave is the first to give God a name for his seeing.")],
  'entries': ['el-roi', 'hagar'],
  'lost': [
   loses("Hebrew El Ro’i, “God of my seeing” or “God who sees me,” is a name; Greek sy ho theos ho epidōn me, “You are God who looked upon me,” is a sentence. Hebrew ha-gam halom ra’iti achare ro’i, “have I even here seen after the one who sees me?”, a question, becomes Greek kai gar enōpion eidon ophthenta moi, “for I also saw before me the one who appeared to me,” a statement. The riddle is gone."),
   between("Latin “the God who has seen me … I have seen the back of Him who sees me” reads achare, “after,” as the back; King James “Thou God seest me … have I also here looked after him that seeth me” keeps the question. Greek ophthenta, “appeared,” is the verb of 12:7 and 18:1."),
  ]},

 '16:14': {
  'received': "So the well was named for the Living One who sees, between Kadesh and Bered.",
  'explain': ("The place keeps the memory. The Hebrew name is Beer-lahai-roi, usually explained as Well of the Living One who sees me, where "
   "Isaac will later live. The Greek names it through Hagar’s own act, “Well where I saw before me,” and makes Hagar the one who named it; the "
   "Hebrew says it was called. The location between Kadesh and Bered agrees."),
  'shared': ["The well was given a name.", "The name recalls the seeing.", "It lies between Kadesh and Bered."],
  'instructions': [ins(K, S, "The well of Hagar’s vision was named and known between Kadesh and Bered.")],
  'entries': ['el-roi', 'hagar'],
  'lost': [
   loses("Hebrew Be’er Lachai Ro’i, “Well of the Living One who sees me,” is a name with the Living One in it; Greek phrear hou enōpion eidon, “well where I saw before me,” names it from Hagar’s seeing and has no Living One. Hebrew qara, “it was called,” is Greek ekalesen, “she called.”"),
   between("Latin “Well of the Living One Who Sees Me” and King James “Beerlahairoi” keep the Hebrew name, the Latin with “she called.” Genesis 24:62 and 25:11 place Isaac here; Kadesh is the Spring of Judgment of 14:7."),
  ]},

 '16:15': {
  'received': "Hagar bore Abram a son, and Abram named him Ishmael.",
  'explain': ("Hagar returns, as commanded, and bears the son. Abram gives him the name the angel announced, so the father accepts the name God "
   "chose. The Hebrew and Greek say Abram named him; the Latin leaves the subject implied. The verse is told without comment on the household."),
  'shared': ["Hagar bore Abram a son.", "Abram named the son.", "His name was Ishmael."],
  'instructions': [ins(K, S, "Ishmael was born to Abram by Hagar and named as the angel had said.")],
  'entries': ['hagar', 'abraham'],
  'lost': [between("Hebrew and Greek name Abram as the one who names, the Greek adding “his son whom Hagar bore him”; Latin “he named him Ishmael” leaves the subject implied; King James follows the Hebrew.")]},

 '16:16': {
  'received': "Abram was eighty-six when Hagar bore Ishmael.",
  'explain': ("The chapter ends with a date. Abram is eighty-six; thirteen silent years will pass before God speaks again at ninety-nine, and "
   "Ishmael will be thirteen when he is circumcised. All versions agree."),
  'shared': ["Abram was eighty-six years old.", "Hagar bore Ishmael.", "The birth is dated by Abram’s age."],
  'instructions': [ins(K, S, "Ishmael was born when Abram was eighty-six.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew, Greek, Latin and King James agree; the Latin says “bore him” for “bore to Abram.” Genesis 17:1 and 17:25 give the next dates.")]},
 }
}
