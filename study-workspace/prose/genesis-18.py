# Study prose for Genesis 18 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

def plea(ref, n, received, explain, shared, know, lost, wisdom=None):
    v = {'received': received, 'explain': explain, 'shared': shared,
         'instructions': [ins(K, S, know)], 'entries': ['abraham'], 'lost': lost}
    if wisdom: v['instructions'].append(ins(W, R, wisdom))
    return v

CHAPTER = {
 'slug': 'genesis', 'chapter': 18,
 'chapterNote': (
  "The three visitors, the meal, Sarah’s laugh, the announcement of Isaac and Abraham’s plea for Sodom are the same story in every column. "
  "What varies is who speaks and how Abraham speaks. The Hebrew keeps YHWH appearing in the heat of the day, “a little water,” the morsel of "
  "bread and the strengthening of the heart, a plural “they said” in 18:9, Sarah’s question about pleasure after she is worn out, “too wonderful "
  "for YHWH,” Sodom alone in 18:16, “I have known him” as election, “whether they have done altogether,” and Abraham’s “do not let the Lord be "
  "angry.” The Greek keeps God appearing at noon by one oak, feet washed by others, a single speaker in 18:9, Sarah’s “it has not happened to "
  "me up to now,” “is any word impossible with God,” Sodom and Gomorrah looked down upon, “Abraham my servant,” “I knew that he would command,” "
  "“whether they are being brought to an end,” and Abraham’s elliptical “please, Lord, if I may speak.” The Latin and King James follow the "
  "Hebrew; the Latin has Sarah laugh already in 18:10 and adds “this is not Your way” in 18:25."),
 'verses': {

 '18:1': {
  'received': "The Lord appeared to Abraham by the trees of Mamre as he sat at his tent door in the heat of the day.",
  'explain': ("The chapter opens with the appearance and then tells of three men, showing only gradually who is speaking. Abraham sits at his "
   "tent door at the hour when travel stopped. The Hebrew says YHWH appeared by the oaks in the heat of the day; the Greek says God appeared "
   "by the oak at noon; the Latin places him in the valley of Mamre. Large trees marked meeting places in the patriarchs’ stories."),
  'shared': ["The Lord appeared to Abraham.", "It was by Mamre.", "Abraham sat at the tent entrance in the heat of the day."],
  'instructions': [ins(K, S, "The Lord appeared to Abraham at Mamre in the heat of the day."), ins(W, R, "God comes at the hour when no one travels; the visit arrives as an interruption of rest, not as a scheduled vision.")],
  'entries': ['abraham', 'hebron', 'yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew YHWH becomes Greek ho theos, “God”; Hebrew elone, “oaks,” is a singular drys; Hebrew ke-chom ha-yom, “in the heat of the day,” becomes Greek mesēmbrias, “at noon.” The Hebrew says “the tent,” the Greek “his tent.”"),
   between("Latin “the Lord … valley of Mamre … heat of the day” and King James “the LORD … plains of Mamre … heat of the day” keep the name and the heat. Greek ōphthē is the verb of 12:7 and 17:1."),
  ]},

 '18:2': {
  'received': "Abraham looked up, saw three men standing near, ran to meet them and bowed to the ground.",
  'explain': ("Abraham sees ordinary travellers, three men, and does what a host does: runs and bows. Hebrews urges hospitality because some have "
   "entertained angels without knowing it. The Hebrew says they stood near him; the Greek over him, the view of a seated man looking up. The "
   "bow by itself does not settle whether it is worship or greeting."),
  'shared': ["Abraham raised his eyes and saw three men.", "They were standing near him.", "He ran to meet them and bowed to the ground."],
  'instructions': [ins(K, S, "Abraham welcomed three unknown travellers with haste and honour."), ins(W, R, "The welcome is given before the guests are known; hospitality that waits to learn who the stranger is has already failed.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew nitsavim alav, “standing near him,” is Greek heistēkeisan epanō autou, “standing over him,” the seated host’s view; Hebrew “the tent entrance” is Greek “his tent entrance.” Latin “appeared standing near him” and King James “stood by him” follow the Hebrew. Hebrews 13:2 is the echo.")]},

 '18:3': {
  'received': "Abraham addressed one as Lord and begged him not to pass his servant by.",
  'explain': ("Abraham speaks to one of the three in the singular, calling him Lord. The Hebrew pointing reads the word as the divine title Adonai, "
   "though the sense “my lord” to a chief guest is also possible, and interpreters divide. The request is simply not to pass by. The versions agree; "
   "the Hebrew adds “please.”"),
  'shared': ["Abraham addressed one of them as Lord.", "He asked whether he had found favour.", "He begged them not to pass his servant by."],
  'instructions': [ins(K, S, "Abraham begged the visitors not to pass him by."), ins(W, R, "The host asks to be allowed to serve; the favour he seeks is the chance to give.")],
  'entries': ['abraham', 'lord-translation'],
  'lost': [between("Hebrew Adonai, pointed as the divine title, is Greek kyrie, “Lord,” both singular; Hebrew be-einekha, “in your eyes,” is Greek enantion sou, “before you”; Hebrew na, “please,” is absent from the Greek but kept by King James “I pray thee.” Latin follows the Hebrew.")]},

 '18:4': {
  'received': "Abraham offered water for their feet and rest under the tree.",
  'explain': ("The first act of welcome: water for dusty feet and shade. The Hebrew tells the guests to wash their feet themselves; the Greek has "
   "water brought and others wash them, making the service explicit. Only the Hebrew says a little water, part of the courtesy that understates "
   "what is offered. Jesus will wash his disciples’ feet, and the Greek word for refresh is the one the rich man uses for cooling his tongue."),
  'shared': ["Water is to be brought.", "The guests’ feet are to be washed.", "They are to rest under the tree."],
  'instructions': [ins(K, S, "Abraham offered his guests water for their feet and rest."), ins(W, R, "Hospitality begins at the feet; the lowest service is the first one offered.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew me‘at mayim, “a little water,” loses “a little” in Greek; Hebrew ve-rachatsu ragleikhem, “and wash your feet,” addressed to the guests, becomes Greek kai nipsatōsan tous podas hymōn, “and let them wash your feet,” done for them by others. Hebrew hinnashe‘u, “rest,” is Greek katapsyxate, “cool yourselves.”"),
   between("Latin “let me bring a little water; wash your feet” and King James “let a little water be fetched, and wash your feet” follow the Hebrew. John 13:5 and Luke 16:24 are the echoes."),
  ]},

 '18:5': {
  'received': "Abraham promised bread to refresh them before they went on, and they agreed.",
  'explain': ("He offers a morsel of bread and will serve a feast; understatement was part of ancient courtesy. The Hebrew says a morsel and uses "
   "the idiom of strengthening the heart; the Greek says bread and you shall eat, and names their onward road. Abraham calls himself their "
   "servant, the host’s polite form. The guests accept in the same words in every version."),
  'shared': ["Abraham will bring bread.", "They will refresh themselves and then go on.", "They said, Do as you have said."],
  'instructions': [ins(K, S, "Abraham offered food and the visitors accepted."), ins(W, R, "“Since you have come to your servant” turns the guests’ arrival into the host’s honour; the one who serves is the one favoured.")],
  'entries': ['abraham'],
  'lost': [
   loses("Hebrew pat-lechem, “a morsel of bread,” is Greek arton, “bread”; Hebrew ve-sa‘adu libbekhem, “and strengthen your heart,” is Greek kai phagesthe, “and you shall eat.” The Greek adds eis tēn hodon hymōn, “on your way,” and changes “you have come” to “you have turned aside.”"),
   between("Latin “a morsel of bread … strengthen your hearts … this is why you have turned aside” and King James “a morsel of bread, and comfort ye your hearts” keep the Hebrew idiom; the Latin shares the Greek “turned aside.” Judges 19:5 uses the same phrase."),
  ]},

 '18:6': {
  'received': "Abraham hurried to Sarah and told her to knead three measures of fine flour into cakes.",
  'explain': ("The feast begins. Three seahs of fine flour is a great quantity for three guests, the same amount as the leaven of Jesus’ parable. "
   "The flour is the kind later named for the grain offering, and the cakes are baked under the embers, as Israel baked on the way out of Egypt. "
   "The Greek says measures for seahs and spells out the baking; no modern volume is implied."),
  'shared': ["Abraham hurried into the tent to Sarah.", "He told her to hurry with three measures of fine flour.", "She was to knead it and make cakes."],
  'instructions': [ins(K, S, "Abraham had Sarah bake a large quantity of fine cakes for the guests."), ins(W, R, "The “morsel of bread” becomes three measures of fine flour; the host’s words were small and his gift is large.")],
  'entries': ['abraham', 'sarah'],
  'lost': [between("Hebrew shelosh se’im, “three seahs,” is Greek tria metra, “three measures”; Hebrew ugot, “cakes,” is Greek enkryphias, “hidden loaves,” baked in the embers. Latin “loaves baked under the ashes” follows the Greek detail; King James “cakes upon the hearth” the Hebrew. Matthew 13:33 and Exodus 12:39 are the echoes.")]},

 '18:7': {
  'received': "Abraham ran to the herd, chose a tender calf, and had a servant prepare it quickly.",
  'explain': ("Meat was eaten only on great occasions, and an old man running was unusual; Abraham does both, as the father in the parable runs "
   "and kills a calf for the son who comes home. The Hebrew says a young man, the Greek an attendant, both read in the household setting without "
   "fixing an age. The versions agree."),
  'shared': ["Abraham ran to the herd.", "He took a tender and good calf.", "He gave it to a servant, who hurried to prepare it."],
  'instructions': [ins(K, S, "Abraham prepared a calf for his guests."), ins(W, R, "Everything in this scene is done running; eagerness to serve is itself part of the gift.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew na‘ar, “young man,” is Greek pais, “attendant”; Hebrew ben-baqar rakh va-tov, “a calf tender and good,” is Greek moscharion hapalon kai kalon. Latin “very tender, choice calf” and King James “a calf tender and good” agree. Luke 15:20 and 15:23 are the running father and the calf.")]},

 '18:8': {
  'received': "Abraham set curds, milk and the calf before them and stood by while they ate under the tree.",
  'explain': ("The meal is served and the host stands, as a servant does. The guests eat, which later readers found remarkable of heavenly "
   "visitors; in Tobit the angel says he only seemed to eat. The Hebrew says curds, the Greek and Latin butter; the Hebrew puts the eating last, "
   "the Greek before the standing, and the Latin carries it into the next verse."),
  'shared': ["Abraham set curds, milk and the calf before them.", "He stood by them under the tree.", "They ate."],
  'instructions': [ins(K, S, "Abraham served the meal and stood by as the visitors ate."), ins(W, R, "The patriarch stands while strangers sit and eat; the father of the faithful is pictured as a waiter.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew chem’ah, “curds,” is Greek boutyron, “butter”; Hebrew ends va-yokhelu, “and they ate,” after the standing, Greek has kai ephagon before it. Latin omits the eating here and gives it in 18:9; King James follows the Hebrew order. Tobit 12:19 and Luke 24:43 reflect on angels eating.")]},

 '18:9': {
  'received': "The visitors asked where Sarah was, and Abraham said she was in the tent.",
  'explain': ("The guests know Sarah’s name, and the question turns the visit from hospitality to promise. The Hebrew has the three ask, “they "
   "said”; the Greek has one speaker, “he said to him,” the spokesman who will carry the rest of the scene. The Latin adds that this was when "
   "they had eaten. Abraham answers that she is in the tent, where she will hear what follows."),
  'shared': ["The visitors asked after Sarah.", "They asked where she was.", "Abraham said she was in the tent."],
  'instructions': [ins(K, S, "The visitors asked for Sarah by name.")],
  'entries': ['abraham', 'sarah'],
  'lost': [
   loses("Hebrew va-yomeru elav, “they said to him,” plural, becomes Greek eipen de pros auton, “he said to him,” singular; the Greek picks out one speaker where the Hebrew has the three ask together."),
   between("Latin “when they had eaten, they said” and King James “they said unto him” keep the plural; the Latin adds the eating moved from 18:8."),
  ]},

 '18:10': {
  'received': "He promised to return at the same season next year, when Sarah would have a son, and Sarah heard it from the tent door.",
  'explain': ("The promise of 17:19 is now spoken where Sarah can hear it. The Hebrew says at the time of life, the Greek at this season when the "
   "time comes round, both understood of the same season next year, the word Paul quotes for the child of promise. The Hebrew places the tent "
   "entrance behind the speaker; the Greek makes Sarah the one behind him. The Latin has her laugh already here."),
  'shared': ["The speaker will return at this time next year.", "Sarah will have a son.", "Sarah was listening at the tent entrance behind him."],
  'instructions': [ins(K, S, "Sarah heard the promise of a son within the year."), ins(W, R, "The promise is spoken for the woman behind the door; God arranges that the one who must believe is the one who overhears.")],
  'entries': ['sarah', 'abraham', 'isaac'],
  'lost': [
   loses("Hebrew ka‘et chayyah, “at the time of life,” becomes Greek kata ton kairon touton eis hōras, “at this season, when the time comes round”; Hebrew shov ashuv, “I will surely return,” loses its doubling; Hebrew ve-hu acharav, “and it was behind him,” of the entrance, becomes Greek ousa opisthen autou, “being behind him,” of Sarah. Hebrew hinneh, “behold,” is dropped."),
   between("Latin “at this time, life continuing … hearing this, Sarah laughed behind the tent’s entrance” follows the Hebrew idiom but moves the laugh forward; King James “according to the time of life … Sarah heard it in the tent door, which was behind him” follows the Hebrew. Romans 9:9 quotes the Greek."),
  ]},

 '18:11': {
  'received': "Abraham and Sarah were old, and Sarah was past the age of childbearing.",
  'explain': ("The narrator states the obstacle plainly, with a euphemism: the way of women had ceased for Sarah. Both are old and advanced in days, "
   "the phrase Luke uses of Zechariah and Elizabeth before John’s birth. The versions agree; the Greek names both, the Latin says “both.”"),
  'shared': ["Abraham and Sarah were old.", "They were advanced in days.", "Sarah was past childbearing."],
  'instructions': [ins(K, S, "Sarah was past the age of bearing when the son was promised."), ins(W, R, "The impossibility is written down before the laugh, so that the laugh is understood and the promise is measured against it.")],
  'entries': ['abraham', 'sarah'],
  'lost': [between("Hebrew orach ka-nashim, “the way of women,” is Greek ta gynaikeia, “the things of women,” both euphemisms; Hebrew ba’im ba-yamim, “advanced in days,” is Greek probebēkotes hēmerōn, the phrase of Luke 1:7. Latin “both were old” drops the names; King James keeps them.")]},

 '18:12': {
  'received': "Sarah laughed to herself at the idea of having a child when she and her lord were old.",
  'explain': ("Sarah’s laugh answers Abraham’s in 17:17, and the same Hebrew verb will name the child. Her words differ across the columns. The Hebrew "
   "asks, after I am worn out shall I have pleasure, with my lord also old; the Greek says it has not happened to me up to now, and my lord is old, "
   "without the worn-out or the pleasure. The Latin asks whether she will give herself to pleasure. Peter holds Sarah up for calling Abraham lord."),
  'shared': ["Sarah laughed within herself.", "She spoke of her own age.", "She called Abraham her lord and noted that he too was old."],
  'instructions': [ins(K, S, "Sarah laughed inwardly at the promise because of her and Abraham’s age."), ins(W, R, "The laugh is private and the reasoning is sound; faith is asked to go against what the body knows.")],
  'entries': ['sarah', 'abraham', 'isaac'],
  'lost': [
   loses("Hebrew achare veloti hayetah-li ednah, “after I am worn out shall I have pleasure,” a question with the words for wearing out and pleasure, becomes Greek oupō men moi gegonen heōs tou nyn, “it has not happened to me up to now,” a statement without either word. Hebrew va-adoni zaqen, “and my lord is old,” is kept."),
   between("Latin “now that I have grown old, and my lord is an old man, shall I give myself to pleasure?” and King James “after I am waxed old shall I have pleasure, my lord being old also?” keep the Hebrew question. 1 Peter 3:6 is Peter’s use."),
  ]},

 '18:13': {
  'received': "The Lord asked Abraham why Sarah laughed at the thought of bearing a child in old age.",
  'explain': ("The speaker is now named: YHWH in the Hebrew, the Lord in the Greek. He knows the silent laugh and quotes it, a reminder that God "
   "knows unspoken thoughts. The Greek adds “within herself,” echoing verse 12, and splits her question into two clauses. Hebrews says Sarah by "
   "faith received power to conceive though past the age."),
  'shared': ["The Lord spoke to Abraham.", "He asked why Sarah laughed.", "He quoted her doubt about bearing a child in old age."],
  'instructions': [ins(K, S, "The Lord knew and named Sarah’s silent laugh."), ins(W, R, "The question is put to Abraham, not Sarah; the husband is asked to answer for the wife’s doubt, and cannot.")],
  'entries': ['sarah', 'abraham', 'yhwh-yahweh'],
  'lost': [
   keeps("Greek adds en heautē, “within herself,” to the laugh, repeating 18:12, and renders Sarah’s words as two clauses, “Will I really bear a child? But I have grown old.” Hebrew YHWH is “the Lord.”"),
   between("Latin “shall I really give birth as an old woman?” and King James “shall I of a surety bear a child, which am old?” keep one clause with the Hebrew. Psalm 139:2 and Luke 5:22 are God knowing thoughts; Hebrews 11:11 is Sarah’s faith."),
  ]},

 '18:14': {
  'received': "Nothing is too hard for the Lord: at the appointed time next year Sarah will have a son.",
  'explain': ("The rebuke is a question that becomes a creed. The Hebrew asks whether anything is too wonderful for YHWH; the Greek whether any "
   "word is impossible with God, almost exactly Gabriel’s words to Mary. Both languages use a word that means both a spoken word and a thing, "
   "so a promise from God is already a reality. The promise of verse 10 is repeated with the appointed time."),
  'shared': ["Nothing is too hard for the Lord.", "He will return at the appointed time.", "Sarah will have a son."],
  'instructions': [ins(K, S, "God declared that nothing is impossible for him and repeated the promise."), ins(W, R, "The answer to the laugh is not an argument but a question about God; what is impossible for a body is not impossible for a word.")],
  'entries': ['sarah', 'yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew ha-yippale me-YHWH davar, “is anything too wonderful for YHWH,” becomes Greek mē adynatei para tō theō rhēma, “is any word impossible with God”; wonder becomes impossibility and the name becomes God. Hebrew ka‘et chayyah is again “when the time comes round.”"),
   keeps("Greek adynatei … rhēma is the wording Luke 1:37 gives Gabriel; the Greek reader hears the annunciation in Sarah’s tent."),
   between("Latin “is anything difficult for God? At the appointed time … life continuing” and King James “is any thing too hard for the LORD? At the time appointed” keep the appointed time; the Latin has God, the King James the name."),
  ]},

 '18:15': {
  'received': "Sarah denied laughing, out of fear, and was told that she had.",
  'explain': ("Sarah’s fear shows she now knows who is speaking. Her laugh had been doubt; her denial is fear of being found out. The correction is "
   "brief and final: no, you did laugh. The Greek verb for denying is the one used of Peter in the courtyard. The versions agree; the Latin names "
   "the Lord as the one who answers."),
  'shared': ["Sarah denied that she had laughed.", "She denied it because she was afraid.", "She was told, No, you did laugh."],
  'instructions': [ins(K, S, "Sarah’s denial was met with the truth."), ins(W, R, "Fear produces a lie as quickly as doubt produced a laugh; God corrects both without withdrawing the promise.")],
  'entries': ['sarah'],
  'lost': [between("Hebrew, Greek and King James agree word for word in sense; the Latin opens “terrified” and names the Lord. Greek ērnēsato, “denied,” is the verb of Matthew 26:70; ephobēthē, “was afraid,” recalls 3:10.")]},

 '18:16': {
  'received': "The men rose and looked toward Sodom, and Abraham walked with them to see them on their way.",
  'explain': ("The visit ends as hospitality required, with the host walking the guests part of the way. From the heights of Hebron the men look "
   "toward the plain. The Hebrew says they looked toward Sodom; the Greek adds Gomorrah and says they looked down, the view from the hills. The "
   "two cities will become Scripture’s standing example of judgement."),
  'shared': ["The men rose from there.", "They looked toward Sodom.", "Abraham went with them to send them on their way."],
  'instructions': [ins(K, S, "Abraham escorted his guests as they set out toward Sodom."), ins(W, R, "The last duty of the host becomes the occasion of the chapter’s second half; walking the guests out, Abraham is let into God’s counsel.")],
  'entries': ['abraham'],
  'lost': [
   keeps("Greek adds kai Gomorra, “and Gomorrah,” to the city looked toward, and katablepsan, “looked down,” for Hebrew va-yashqifu, “looked.” The Greek names both cities before verse 20 does."),
   between("Latin “looked toward Sodom” and King James “looked toward Sodom” have Sodom alone with the Hebrew. Greek sympropempōn, “escorting,” is the word of Acts 20:38 and 3 John 6."),
  ]},

 '18:17': {
  'received': "The Lord deliberated whether to hide from Abraham what he was about to do.",
  'explain': ("God thinks aloud, and the thought is about disclosure. Amos will say the Lord does nothing without revealing his counsel to his "
   "servants the prophets. The Greek calls Abraham “my servant,” a title not in the Hebrew verse, though the Hebrew will call him so in 26:24. "
   "The Hebrew leaves the sentence open to run into verse 18."),
  'shared': ["The Lord spoke.", "He asked whether he should hide his purpose from Abraham.", "What he is about to do is in view."],
  'instructions': [ins(K, S, "God chose to let Abraham know his purpose against Sodom."), ins(W, R, "The friend of God is told what God is doing; revelation here is an act of friendship, not of office.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [
   keeps("Greek adds tou paidos mou, “my servant,” after Abraham; the Hebrew has only “from Abraham.” Pais is here a service word, servant, not child. Hebrew YHWH is “the Lord.”"),
   between("Latin “can I conceal from Abraham what I am about to do” and King James “shall I hide from Abraham that thing which I do” have no title. Amos 3:7 and John 15:15 are the echoes; James 2:23 calls Abraham God’s friend."),
  ]},

 '18:18': {
  'received': "Abraham will become a great nation, and all the nations of the earth will be blessed in him.",
  'explain': ("The reason for telling Abraham is the promise itself. The blessing of 12:3 is restated for the nations, the word the New Testament "
   "uses for the Gentiles; Paul quotes it as the gospel announced beforehand. The Hebrew calls the nation great and mighty; the Greek great "
   "and numerous; the Latin great and very mighty."),
  'shared': ["Abraham will surely become a great nation.", "All the nations of the earth will be blessed in him.", "This is why God tells him his purpose."],
  'instructions': [ins(K, S, "The promise of blessing for all nations through Abraham was restated."), ins(W, R, "The man through whom all nations are to be blessed is told of a judgement on two cities; blessing and judgement are revealed to the same friend.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew gadol ve-atsum, “great and mighty,” is Greek mega kai poly, “great and numerous”; Latin “great and very mighty,” King James “great and mighty.” Greek eneulogēthēsontai, “shall be blessed,” is the word Galatians 3:8 quotes.")]},

 '18:19': {
  'received': "God knows Abraham, who will command his household to keep the Lord’s way of righteousness and justice, so that the promise may be fulfilled.",
  'explain': ("Election and instruction are bound together. The Hebrew says I have known him, the verb of choosing, followed by purpose: so that he "
   "may command his household to keep the way of YHWH. The Greek says I knew that he would command his household, making the instruction the content "
   "of God’s knowledge, and has plural ways. In both, the promise depends on Abraham teaching righteousness and justice at home."),
  'shared': ["God knows Abraham.", "Abraham will command his children and household to keep the way of the Lord.", "This is so that the Lord may bring about what he has spoken."],
  'instructions': [ins(K, S, "Abraham was chosen to teach his household righteousness and justice."), ins(W, R, "The household is where the promise is kept or lost; the father of nations is first a teacher of his own children.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew ki yeda‘tiv lema‘an asher yetsavveh, “for I have known him, so that he may command,” is election with a purpose; Greek ēdein gar hoti syntaxei, “for I knew that he would command,” makes the commanding what God knows. Hebrew derekh YHWH, “the way of YHWH,” singular, is Greek tas hodous kyriou, “the ways of the Lord,” plural; the Greek adds “everything.”"),
   between("Latin “for I know that he will command” follows the Greek construction; King James “for I know him, that he will command” holds both. Amos 3:2 uses the Hebrew knowing; Deuteronomy 6:7 the teaching."),
  ]},

 '18:20': {
  'received': "The Lord said that the outcry against Sodom and Gomorrah was great and their sin very grave.",
  'explain': ("The charge is stated. An outcry has risen, from the cities or against them, and their sin is heavy. The Hebrew has collective sin "
   "and the word heavy; the Greek plural sins and an outcry that has increased. The Greek word for sin first meant missing a target; here it is the "
   "whole weight of Sodom’s wrongdoing."),
  'shared': ["The Lord spoke of Sodom and Gomorrah.", "Their outcry is great.", "Their sin is very grave."],
  'instructions': [ins(K, S, "God judged the sin of Sodom and Gomorrah to be very grave."), ins(W, R, "An outcry reaches God before the fire falls; judgement answers a cry, and the cry is heard.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew chattatam kavedah me’od, “their sin is very heavy,” singular, is Greek hai hamartiai autōn megalai sphodra, “their sins are very great,” plural; Hebrew rabbah, “is great,” of the outcry is Greek peplēthyntai, “has increased.” Latin and King James keep the singular sin.")]},

 '18:21': {
  'received': "The Lord would go down and see whether Sodom’s deeds matched the outcry, so as to know.",
  'explain': ("God will investigate before he judges, as he came down at Babel. The Hebrew asks whether they have done altogether according to the "
   "outcry, an active question about completed wrongdoing; the Greek has a passive, whether they are being brought to an end according to the "
   "outcry, which can mean completion or destruction, and the difficulty is left standing. The Latin asks whether their deeds fulfil the outcry."),
  'shared': ["The Lord will go down and see.", "He will test the outcry against the facts.", "If not, he will know."],
  'instructions': [ins(K, S, "God resolved to examine Sodom before acting."), ins(W, R, "Even the Judge of all the earth is shown going down to look; justice is pictured as taking the trouble to know.")],
  'entries': [],
  'lost': [
   loses("Hebrew ha-ketsa‘aqatah ha-ba’ah elai asu kalah, “whether they have done altogether according to the outcry that has come to me,” active, becomes Greek ei kata tēn kraugēn autōn tēn erchomenēn pros me syntelountai, “whether they are being brought to an end according to their outcry,” passive and ambiguous between completion and destruction."),
   between("Latin “whether their deeds fulfil the outcry” and King James “whether they have done altogether according to the cry” follow the Hebrew. Genesis 11:5 and Exodus 3:8 are the going down."),
  ]},

 '18:22': {
  'received': "The men went on toward Sodom, but Abraham remained standing before the Lord.",
  'explain': ("Two of the three go on; Abraham stays, standing before the Lord, the posture of a servant or an intercessor. Jewish scribal tradition "
   "lists this verse among places where the wording was adjusted, the earlier reading being that the Lord stood before Abraham; both printed texts "
   "read as they stand. The Hebrew and Latin say still stood; the Greek stood."),
  'shared': ["The men turned and went toward Sodom.", "Abraham stayed.", "He stood before the Lord."],
  'instructions': [ins(K, S, "Abraham remained before the Lord as the others went to Sodom."), ins(W, R, "To stand before the Lord when others have gone is the beginning of intercession; Abraham stays to speak for a city not his own.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [between("Hebrew odennu omed, “still standing,” is Greek ēn hestēkōs, “was standing,” without “still”; Hebrew va-yelekhu Sedomah, “went toward Sodom,” is Greek ēlthon eis Sodoma, “came to Sodom.” Latin adhuc and King James “stood yet” keep “still.” The scribal note concerns the Hebrew tradition only.")]},

 '18:23': plea('18:23', 50,
  "Abraham drew near and asked whether God would destroy the righteous with the wicked.",
  ("The intercession begins with a question about justice. Abraham draws near, the verb Hebrews uses for approaching God with boldness, and asks whether "
   "the righteous will be swept away with the wicked. The Greek adds here what the Hebrew saves for verse 25, so that the righteous would be like the "
   "ungodly; its word for the wicked means those without reverence for God. Peter will call Lot the righteous man this plea ends up saving."),
  ["Abraham drew near.", "He asked whether God would destroy the righteous with the wicked.", "The righteous and the wicked would then share one fate."],
  "Abraham questioned whether God would destroy the righteous with the wicked.",
  [keeps("Greek adds kai estai ho dikaios hōs ho asebēs, “and the righteous will be like the ungodly,” to the first question; the Hebrew has the clause only in 18:25. Hebrew tispeh, “sweep away,” is Greek synapoleis, “destroy together.”"),
   between("Latin “he drew near and said, Will You destroy the righteous with the wicked?” and King James follow the Hebrew’s single question. Hebrews 10:22 is the drawing near; 2 Peter 2:7–8 is Lot.")],
  wisdom="Abraham’s first word for Sodom is about God’s character, not the city’s merit; intercession begins by appealing to who God is."),

 '18:24': plea('18:24', 50,
  "Abraham asked whether God would spare the city for the sake of fifty righteous within it.",
  ("The first number: fifty. Abraham asks that the whole place be spared for the sake of fifty righteous in it. The Hebrew begins “perhaps” and leaves "
   "the object of the sweeping away implicit; the Greek asks directly whether God will destroy them and spare the whole place; the Latin asks whether "
   "they shall perish together. The righteous are to be the city’s protection."),
  ["Perhaps there are fifty righteous in the city.", "Will God sweep it away?", "Will he not spare the place for the sake of the fifty?"],
  "Abraham asked God to spare Sodom for the sake of fifty righteous people.",
  [between("Hebrew ulai, “perhaps,” is Greek ean, “if”; Hebrew ha-af tispeh, “will you indeed sweep away,” without an object, is Greek apoleis autous, “will you destroy them,” and the Greek adds panta, “whole,” to the place. Latin “shall they perish together” and King James “wilt thou also destroy” follow the Hebrew shape.")],
  wisdom="The righteous few are asked to count for the many; Abraham’s theology is that a city can be carried by those who do right in it."),

 '18:25': plea('18:25', 50,
  "Abraham insisted that the Judge of all the earth could not kill the righteous with the wicked.",
  ("The strongest word of the plea: far be it from you. To treat the righteous as the wicked would be unjust, and the Judge of all the earth must "
   "do justice. The Hebrew asks it as a question; the Greek addresses God directly, you who judge all the earth, will you not do justice; the Latin "
   "adds “this is not your way” and makes the end a statement. The Greek has the righteous-like-the-wicked clause here as well as in verse 23."),
  ["Far be it from God to kill the righteous with the wicked.", "The righteous must not fare like the wicked.", "The Judge of all the earth will do justice."],
  "Abraham appealed to God as the just Judge of all the earth.",
  [between("Hebrew chalilah lekha, “far be it from you,” twice, is Greek mēdamōs, “by no means,” twice; Hebrew ha-shofet kol-ha-arets lo ya‘aseh mishpat, “shall the Judge of all the earth not do justice,” is Greek ho krinōn pasan tēn gēn ou poiēseis krisin, “you who judge all the earth, will you not do justice,” in the second person. Latin adds non est hoc tuum, “this is not Your way,” and ends with a statement; King James follows the Hebrew.")],
  wisdom="Abraham holds God to God’s own justice; the boldest prayer in Genesis is a reminder to the Judge of what judging means."),

 '18:26': plea('18:26', 50,
  "The Lord agreed to spare the whole place if he found fifty righteous in Sodom.",
  ("God accepts the principle and the number. If fifty righteous are found, the whole place is spared for their sake, not only the righteous themselves. "
   "The Hebrew verb is to lift or bear, which can mean forgive or spare; the Greek is to release, with the same range. The Hebrew says YHWH; the Latin "
   "adds “to him.”"),
  ["The Lord answered.", "If he finds fifty righteous in Sodom he will spare it.", "He will spare the whole place for their sake."],
  "God agreed to spare Sodom for fifty righteous.",
  [between("Hebrew ve-nasa’ti le-khol-ha-maqom, “I will lift (spare, forgive) the whole place,” is Greek aphēsō panta ton topon, “I will release (forgive) the whole place”; both verbs cover sparing and forgiving. Hebrew YHWH is “the Lord.” Latin and King James say spare.")],
  wisdom="God consents at once; the plea is not resisted but welcomed, and the bargaining that follows is Abraham’s caution, not God’s reluctance."),

 '18:27': plea('18:27', 45,
  "Abraham acknowledged his boldness in speaking to the Lord, being only dust and ashes.",
  ("Before the next number Abraham lowers himself: he is dust and ashes, the dust of 2:7 and 3:19 with the ashes of mourning. The Hebrew says he has "
   "undertaken to speak; the Greek that he has begun; the Latin, since he has begun he will speak. The Hebrew dust is earth in the Greek."),
  ["Abraham answered.", "He has undertaken to speak to the Lord.", "He is but dust and ashes."],
  "Abraham confessed his lowliness before pressing his plea.",
  [between("Hebrew hinneh-na ho’alti, “look, I have undertaken,” is Greek nyn ērxamēn, “now I have begun”; Hebrew afar va-efer, “dust and ashes,” a sound-pair, is Greek gē kai spodos, “earth and ashes.” Latin “since I have begun, I will speak … dust and ashes” and King James “I have taken upon me to speak … dust and ashes” keep the dust.")],
  wisdom="Boldness and humility speak in the same breath; dust and ashes argues with the Judge of all the earth and is heard."),

 '18:28': plea('18:28', 45,
  "Abraham asked whether five fewer would doom the city, and God promised not to destroy it for forty-five.",
  ("The bargaining begins: what if the fifty lack five? The Hebrew asks whether God will destroy the whole city for lack of five; the Greek because of "
   "the five; the Latin because there are forty-five. God’s answer is the same in all, forty-five will save it; the Greek makes the refusal emphatic, "
   "I will certainly not destroy it."),
  ["Perhaps the fifty righteous lack five.", "Will God destroy the whole city for lack of five?", "God will not destroy it if he finds forty-five."],
  "God agreed to spare Sodom for forty-five righteous.",
  [between("Hebrew lo ashchit, “I will not destroy,” is Greek ou mē apolesō, “I will certainly not destroy,” an emphatic negative repeated through the dialogue; Hebrew ba-chamishah, “for the five,” is Greek dia tous pente, “because of the five,” and Latin “because there are forty-five.” King James follows the Hebrew.")],
  wisdom="Abraham argues from the few who are missing, not the many who are wicked; mercy is pleaded for in the smallest unit."),

 '18:29': plea('18:29', 40,
  "Abraham asked about forty, and God promised not to act for the sake of forty.",
  ("The number falls to forty. The Hebrew has God say I will not do it; the Greek I will certainly not destroy it; the Latin I will not strike it. The "
   "Latin expands Abraham’s question, what will you do. The assurance is the same."),
  ["Abraham spoke to him again.", "Perhaps forty will be found there.", "God will not do it for the sake of the forty."],
  "God agreed to spare Sodom for forty righteous.",
  [between("Hebrew lo e‘eseh, “I will not do it,” is Greek ou mē apolesō, “I will certainly not destroy,” supplying the verb; Latin non percutiam, “I will not strike,” and “what will You do?” expand; King James “I will not do it” follows the Hebrew.")]),

 '18:30': plea('18:30', 30,
  "Abraham begged the Lord not to be angry as he asked about thirty, and God promised to spare the city for thirty.",
  ("Abraham senses he is pressing. The Hebrew has him say please do not let the Lord be angry, and I will speak; the Greek has an elliptical "
   "please, Lord, if I may speak, without the anger; the Latin keeps the anger. The number is thirty, and God will not do it, or in the Greek will "
   "certainly not destroy it."),
  ["Abraham asked leave to speak.", "Perhaps thirty will be found there.", "God will not do it if he finds thirty."],
  "God agreed to spare Sodom for thirty righteous.",
  [loses("Hebrew al-na yichar la-Adonai, “please do not let the Lord be angry,” names the anger Abraham fears; Greek mē ti, kyrie, ean lalēsō, “please, Lord, if I may speak,” is an elliptical appeal with no anger. Hebrew lo e‘eseh is again Greek ou mē apolesō."),
   between("Latin “please do not be angry, Lord, if I speak” and King James “Oh let not the LORD be angry, and I will speak” keep the anger with the Hebrew.")],
  wisdom="Abraham fears to presume and presumes anyway; reverence and persistence are not opposites in prayer."),

 '18:31': plea('18:31', 20,
  "Abraham asked about twenty, and God promised not to destroy the city for twenty.",
  ("Twenty. Abraham repeats the formula of verse 27, I have undertaken to speak; the Greek says since I may speak; the Latin since I have begun. God’s "
   "answer in all is not to destroy, the Latin saying not to kill them. The city has been argued down from fifty to twenty."),
  ["Abraham has undertaken to speak to the Lord.", "Perhaps twenty will be found there.", "God will not destroy it for the sake of the twenty."],
  "God agreed to spare Sodom for twenty righteous.",
  [between("Hebrew hinneh-na ho’alti le-dabber, “look, I have undertaken to speak,” is Greek epeidē echō lalēsai, “since I may speak”; Latin semel coepi, “since I have begun,” and interficiam, “I will kill,” for destroy. King James “I have taken upon me to speak” follows the Hebrew.")]),

 '18:32': plea('18:32', 10,
  "Abraham asked once more, about ten, and God promised not to destroy the city for the sake of ten.",
  ("The last number: ten, and Abraham says this is his last word. The Hebrew again asks the Lord not to be angry; the Greek again has the elliptical "
   "please, Lord, if I may speak once more; the Latin I beg you, do not be angry. God promises not to destroy for ten. Abraham stops; the city will not "
   "have ten."),
  ["Abraham asked to speak just once more.", "Perhaps ten will be found there.", "God will not destroy it for the sake of the ten."],
  "God agreed to spare Sodom for ten righteous, and Abraham ceased.",
  [loses("Hebrew al-na yichar la-Adonai, “please do not let the Lord be angry,” is again absent from Greek mē ti, kyrie, ean lalēsō eti hapax, “please, Lord, if I may speak once more.”"),
   between("Latin “I beg You, do not be angry, Lord, if I speak once more” and King James “Oh let not the LORD be angry, and I will speak yet but this once” keep the anger with the Hebrew. Genesis 19 shows that not even ten were found.")],
  wisdom="Abraham stops at ten and God has conceded every number; the plea fails not because God refused but because the city had no ten."),

 '18:33': {
  'received': "When the Lord had finished speaking, he departed, and Abraham went home.",
  'explain': ("The dialogue ends quietly. The Lord goes his way when the speaking is done, and Abraham returns to his place. Nothing is said of what "
   "Abraham thinks; the next morning he will look toward the plain. The versions agree."),
  'shared': ["The Lord finished speaking to Abraham.", "The Lord departed.", "Abraham returned to his place."],
  'instructions': [ins(K, S, "The Lord departed and Abraham returned home after the intercession."), ins(W, R, "The intercessor goes home not knowing the outcome; prayer ends in waiting, and the answer comes in the morning smoke.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [between("Hebrew va-yelekh YHWH ka’asher killah, “YHWH departed when he had finished,” is Greek apēlthen de kyrios hōs epausato, “the Lord departed when he stopped”; Latin and King James agree in sense. Genesis 19:27 has Abraham return to this place.")]},
 }
}
