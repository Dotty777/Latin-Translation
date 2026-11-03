# Study prose for Genesis 41 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 41,
 'chapterNote': (
  "Pharaoh’s two dreams, the cupbearer’s memory, Joseph brought from the pit to interpret and advise, his elevation over Egypt, his Egyptian name and wife, his "
  "two sons, and the famine. The columns agree on the whole; the Hebrew keeps the Nile, “scorched by the east wind,” “he slept” before the second dream, "
  "“magicians,” “my offences,” “me” in custody, “the captain of the guard,” the pit and Joseph shaving himself, “it is not in me,” the cry “Abrek,” “hand or foot,” "
  "Zaphenath-paneah and On, “Joseph went out over the land,” “by the handful,” “the famine prevailed in Egypt,” and “all the earth came.” The Greek keeps “the "
  "river,” “blighted by the wind,” “interpreters,” “my offence,” “us,” “the chief cook,” the fortress and others shaving him, “without God no answer bringing "
  "deliverance,” “today” in the appointment, a herald without the cry, “hand” alone, Psonthomphanech and Heliopolis, “sheaves,” and “all the countries.” Six "
  "Hebrew-column renderings were corrected today. The Latin and King James follow the Hebrew; the Latin renders the Egyptian name as “Saviour of the World.”"),
 'verses': {

 '41:1': {
  'received': "After two full years Pharaoh dreamed he stood by the Nile.",
  'explain': ("Two years of being forgotten. Ye’or, the Nile, Egypt’s life; the Greek and Latin say the river. Standing by the river, Pharaoh is where Egypt’s fortune is decided."),
  'shared': ["Two full years passed.", "Pharaoh dreamed.", "He was standing beside the river."],
  'instructions': [ins(K, S, "Pharaoh dreamed by the Nile after two years."), ins(W, R, "Two years of silence end not with the cupbearer’s conscience but with a king’s dream; God remembers Joseph by troubling Pharaoh.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew ha-Ye’or, “the Nile,” is Greek tou potamou, “the river,” Latin fluvium, King James “the river.”")]},

 '41:2': {
  'received': "Seven fine fat cows came up from the river and grazed in the reeds.",
  'explain': ("Cows from the Nile, as if the river bred them. Achu, reed-grass, an Egyptian loanword. The Latin says marshy places."),
  'shared': ["Seven cows came up out of the river.", "They were beautiful and fat.", "They grazed in the reed grass."],
  'instructions': [ins(K, S, "Seven fat cows rose from the Nile.")],
  'entries': [],
  'lost': [AGREE]},

 '41:3': {
  'received': "Seven other cows, ugly and gaunt, came up after them and stood by them on the bank.",
  'explain': ("The Hebrew says stood by the other cows; the Greek grazed beside them; the Latin grazed in the green places."),
  'shared': ["Seven other cows came up after them from the river.", "They were ugly and thin.", "They were beside the other cows on the riverbank."],
  'instructions': [ins(K, S, "Seven gaunt cows followed the fat ones.")],
  'entries': [],
  'lost': [between("Hebrew va-ta‘amodnah etzel ha-parot, “and they stood beside the cows,” is Greek kai enemonto para tas boas, “and they grazed beside the cows”; Latin “grazed in the green places,” King James “stood by the other kine.”")]},

 '41:4': {
  'received': "The gaunt cows ate the fat cows, and Pharaoh woke.",
  'explain': ("The impossible image, the omen. The Greek repeats seven. The versions agree."),
  'shared': ["The ugly, thin cows ate up the seven fat cows.", "Pharaoh woke.", "The first dream ended."],
  'instructions': [ins(K, S, "Lean cows devoured fat in Pharaoh’s dream.")],
  'entries': [],
  'lost': [AGREE]},

 '41:5': {
  'received': "He slept and dreamed again: seven plump good ears on one stalk.",
  'explain': ("The second dream, grain. The Hebrew says he slept and dreamed; the Greek lacks he slept; the Latin slept again."),
  'shared': ["He dreamed a second time.", "Seven ears of grain came up on one stalk.", "They were plump and good."],
  'instructions': [ins(K, S, "Pharaoh dreamed of seven good ears.")],
  'entries': [],
  'lost': [loses("Hebrew va-yishan, “and he slept,” is absent from the Greek, which has only kai enypniasthē to deuteron, “and he dreamed a second time.”"), between("Latin “then slept again” and King James “he slept and dreamed” keep it.")]},

 '41:6': {
  'received': "Seven thin ears, scorched by the east wind, sprang up after them.",
  'explain': ("The east wind, the sirocco from the desert; the Greek says blighted by the wind without direction; the Latin struck by blight."),
  'shared': ["Seven other ears sprang up after them.", "They were thin.", "They were scorched by the wind."],
  'instructions': [ins(K, S, "Seven blighted ears followed the good ones.")],
  'entries': [],
  'lost': [loses("Hebrew shedufot qadim, “scorched by the east wind,” becomes Greek anemophthoroi, “wind-blighted,” without the direction."), between("Latin “struck by blight” and King James “blasted with the east wind” vary.")]},

 '41:7': {
  'received': "The thin ears swallowed the seven full ears; Pharaoh woke, and it was a dream.",
  'explain': ("And behold, a dream: the Hebrew marks the waking. The Greek repeats the wind-blighted; the Latin after his rest."),
  'shared': ["The thin ears swallowed the seven plump, full ears.", "Pharaoh woke.", "It was a dream."],
  'instructions': [ins(K, S, "Thin ears swallowed full in the second dream."), ins(W, R, "Two dreams with one meaning, like the two dreams of chapter 37; God speaks twice to make certain, as Joseph will explain.")],
  'entries': [],
  'lost': [between("Greek repeats anemophthoroi, “wind-blighted,” and hepta, “seven,” of the thin ears; Latin “Pharaoh awoke after his rest” drops “behold, a dream”; King James follows the Hebrew.")]},

 '41:8': {
  'received': "In the morning his spirit was troubled; he summoned all Egypt’s magicians and wise men and told them, but none could interpret.",
  'explain': ("Chartummim, the magicians who will face Moses. The Hebrew says spirit, magicians, the dreams; the Greek soul, interpreters, the dream; the Latin terrified with dread."),
  'shared': ["In the morning his spirit was troubled.", "He sent for all Egypt’s magicians and wise men and told them his dream.", "No one could interpret it for Pharaoh."],
  'instructions': [ins(K, S, "Egypt’s wise men failed to interpret the dreams."), ins(W, R, "All the wisdom of Egypt cannot read Egypt’s dream; the prisoner can, because, as he will say, interpretations belong to God.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew rucho, “his spirit,” is Greek hē psychē autou, “his soul”; Hebrew chartumme, “magicians,” is Greek tous exēgētas, “the interpreters”; Hebrew otam, “them,” the dreams, is Greek auto, “it”; Latin “terrified with dread … interpreters,” King James “his spirit was troubled … magicians.”")]},

 '41:9': {
  'received': "The chief cupbearer said to Pharaoh, Today I remember my faults.",
  'explain': ("The forgotten memory returns, under the cover of confessing his own offence. The Hebrew says offences; the Greek offence; the Latin then at last."),
  'shared': ["The chief cupbearer spoke to Pharaoh.", "Today I remember.", "My faults."],
  'instructions': [ins(K, S, "The cupbearer remembered Joseph at last."), ins(W, R, "He remembers his fault, and Joseph only as its footnote; gratitude did not move him, but the king’s need did, and God used that.")],
  'entries': [],
  'lost': [between("Hebrew chata’ai, “my sins,” plural, is Greek tēn hamartian mou, singular; Latin “Then at last the chief cupbearer remembered and said, I confess my fault”; King James “my faults.”")]},

 '41:10': {
  'received': "Pharaoh was angry with his servants and put me in custody in the captain of the guard’s house, me and the chief baker.",
  'explain': ("The Hebrew says put me, the captain of the guard; the Greek put us, the chief cook; the Latin the prison of the commander of the soldiers."),
  'shared': ["Pharaoh was angry with his servants.", "He put me in custody in the house of the captain of the guard.", "Me and the chief baker."],
  'instructions': [ins(K, S, "The cupbearer recounted his imprisonment.")],
  'entries': [],
  'lost': [between("Hebrew va-yitten oti, “and put me,” is Greek etheto hēmas, “put us”; Hebrew sar ha-tabbachim, “chief of the guard,” is Greek tou archimageirou, “the chief cook”; Latin “commander of the soldiers,” King James “captain of the guard.”")]},

 '41:11': {
  'received': "We each dreamed one night, each a dream with its own meaning.",
  'explain': ("The Hebrew says according to the interpretation of his dream; the Greek each his own dream; the Latin foretelling the future."),
  'shared': ["We dreamed a dream in one night, he and I.", "Each had his own dream.", "Each with its meaning."],
  'instructions': [ins(K, S, "The cupbearer told of the two dreams.")],
  'entries': [],
  'lost': [loses("Hebrew ish ke-fitron chalomo, “each according to the interpretation of his dream,” is absent from the Greek, which has hekateros kata to hautou enypnion, “each according to his own dream.”"), between("Latin “a dream foretelling the future” and King James “each man according to the interpretation of his dream” keep a sense of meaning.")]},

 '41:12': {
  'received': "A young Hebrew, slave of the captain of the guard, was there; we told him and he interpreted each dream.",
  'explain': ("Joseph described from outside: young, Hebrew, slave. The Hebrew says servant of the captain of the guard, each according to his dream; the Greek of the chief cook, shorter; the Latin of that same commander."),
  'shared': ["A young Hebrew man was there with us, a servant of the captain of the guard.", "We told him our dreams.", "He interpreted them for us."],
  'instructions': [ins(K, S, "The cupbearer described Joseph to Pharaoh."), ins(W, R, "“A young Hebrew slave”: the recommendation that lifts Joseph names everything that should keep him down. God’s instrument is introduced by his disqualifications.")],
  'entries': [],
  'lost': [loses("Hebrew ish ka-chalomo patar, “each according to his dream he interpreted,” is absent from the Greek; Hebrew sar ha-tabbachim is Greek tou archimageirou, “the chief cook.”"), between("Latin “servant of that same commander of the soldiers” and King James “servant to the captain of the guard” follow the Hebrew.")]},

 '41:13': {
  'received': "It happened as he interpreted: I was restored and the other hanged.",
  'explain': ("The Hebrew says he restored me, he hanged him, Pharaoh the subject; the Greek passive; the Latin upon a cross."),
  'shared': ["As he interpreted for us, so it happened.", "I was restored to my office.", "The other was hanged."],
  'instructions': [ins(K, S, "The cupbearer vouched for Joseph’s accuracy.")],
  'entries': [],
  'lost': [between("Hebrew oti heshiv al-kanni ve-oto talah, “me he restored to my place and him he hanged,” active, is Greek eme te apokatastathēnai … ekeinon de kremasthēnai, passive; Latin “hung upon a cross,” King James “me he restored … him he hanged.”")]},

 '41:14': {
  'received': "Pharaoh sent for Joseph; they rushed him from the pit, he shaved and changed his clothes and came before Pharaoh.",
  'explain': ("From the pit to the throne room in a verse. The Hebrew says they hurried him from the pit, he shaved, changed; the Greek brought him out of the fortress, shaved him, changed his robe; the Latin immediately, cut his hair."),
  'shared': ["Pharaoh sent and called Joseph.", "They brought him hastily out of the pit.", "He shaved, changed his clothes, and came to Pharaoh."],
  'instructions': [ins(K, S, "Joseph was brought from prison to Pharaoh."), ins(W, R, "The bor, the pit, is the word for his brothers’ cistern; Joseph comes up out of a pit twice, each time into a stranger’s hands, and the second time the stranger is a king.")],
  'entries': [],
  'lost': [between("Hebrew min-ha-bor, “from the pit,” is Greek ek tou ochyrōmatos, “from the fortress”; Hebrew va-yegallach va-yechallef, “and he shaved and changed,” is Greek kai exyrēsan auton kai ēllaxan tēn stolēn autou, “and they shaved him and changed his robe”; Latin “they cut his hair, changed his clothing”; King James “he shaved himself, and changed his raiment.”")]},

 '41:15': {
  'received': "Pharaoh said: I have dreamed and none can interpret; I hear you can interpret a dream when you hear it.",
  'explain': ("Pharaoh states the problem and the reputation. The Greek says dreams, plural; the Latin most wisely."),
  'shared': ["I have dreamed a dream and no one can interpret it.", "I have heard it said of you.", "When you hear a dream you can interpret it."],
  'instructions': [ins(K, S, "Pharaoh asked Joseph to interpret.")],
  'entries': [],
  'lost': [between("Hebrew tishma chalom liftor oto, “you hear a dream to interpret it,” singular, is Greek akousanta se enypnia synkrinai auta, “hearing dreams you interpret them,” plural; Latin “you interpret them most wisely”; King James “understand a dream to interpret it.”")]},

 '41:16': {
  'received': "Joseph answered: it is not in me; God will give Pharaoh an answer of peace.",
  'explain': ("Joseph disclaims before he interprets, as in prison. The Hebrew says it is not in me, an answer of peace; the Greek without God no answer bringing deliverance will be given; the Latin it is beyond me, a favourable answer."),
  'shared': ["Joseph answered Pharaoh.", "It is not in me.", "God will give Pharaoh an answer of peace."],
  'instructions': [ins(K, S, "Joseph credited God before Pharaoh."), ins(W, R, "“It is not in me”: before the most powerful man in the world, a slave disowns the gift he is about to use. The disclaimer is the credential.")],
  'entries': ['elohim'],
  'lost': [loses("Hebrew bil‘adai Elohim ya‘aneh et-shelom Par‘oh, “apart from me, God will answer Pharaoh’s peace,” becomes Greek aneu tou theou ouk apokrithēsetai to sōtērion Pharaō, “without God the deliverance of Pharaoh will not be answered”; the disclaimer of self becomes a dependence on God."), between("Latin “It is beyond me; God will give Pharaoh a favourable answer” and King James “It is not in me: God shall give Pharaoh an answer of peace” follow the Hebrew.")]},

 '41:17': {
  'received': "Pharaoh told Joseph: in my dream I stood on the bank of the Nile,",
  'explain': ("The retelling begins. The Hebrew says behold, I was standing; the Greek it seemed to me that I stood; the Latin I thought I stood. The Hebrew-column rendering was corrected today."),
  'shared': ["Pharaoh spoke to Joseph.", "In my dream.", "I stood on the bank of the river."],
  'instructions': [ins(K, S, "Pharaoh retold the first dream.")],
  'entries': [],
  'lost': [between("Hebrew hineni omed, “behold, I was standing,” is Greek ōmēn hestanai, “I thought I stood”; Latin “I thought I stood”; King James “behold, I stood.”")]},

 '41:18': {
  'received': "seven fat fine cows came up from the river and grazed in the reeds,",
  'explain': ("The Greek says as it were, fed on the sedge; the Latin cropping the greenery in the marsh."),
  'shared': ["Seven cows came up out of the river.", "They were fat and beautiful.", "They grazed in the reed grass."],
  'instructions': [ins(K, S, "Pharaoh described the fat cows.")],
  'entries': [],
  'lost': [AGREE]},

 '41:19': {
  'received': "and seven others, poor, very ugly and thin, such as I never saw in all Egypt for badness.",
  'explain': ("Pharaoh adds his own judgment: never so bad. The Greek adds from the river; the Latin deformed."),
  'shared': ["Seven other cows came up after them.", "They were poor, very ugly and thin.", "I never saw such bad cows in all Egypt."],
  'instructions': [ins(K, S, "Pharaoh stressed the ugliness of the lean cows.")],
  'entries': ['egypt'],
  'lost': [keeps("An added ek tou potamou, “from the river,” in the Greek."), between("Latin “so deformed and thin” and King James “poor and very ill favoured and leanfleshed” follow the Hebrew.")]},

 '41:20': {
  'received': "The thin ugly cows ate the first seven fat cows,",
  'explain': ("The Greek adds seven and good to the lean cows and the fat. The Hebrew-column rendering was corrected today."),
  'shared': ["The thin, ugly cows ate.", "They ate the first seven cows.", "The fat ones."],
  'instructions': [ins(K, S, "Pharaoh retold the devouring.")],
  'entries': [],
  'lost': [keeps("Greek hai hepta boes hai aischrai kai leptai … tas hepta boas tas prōtas tas kalas kai eklektas, “the seven ugly thin cows … the first seven good and choice cows,” adds the number and the adjectives."), between("Hebrew, Latin and King James without them.")]},

 '41:21': {
  'received': "but when they had eaten them no one could tell; they were as ugly as before. Then I woke.",
  'explain': ("A detail not in the first telling: the eaten made no difference. The Greek adds and went back to sleep; the Latin no sign of being satisfied."),
  'shared': ["They went into their bellies.", "It could not be told that they had eaten them; they were as ugly as at first.", "I awoke."],
  'instructions': [ins(K, S, "The lean cows were unchanged by eating."), ins(W, R, "Pharaoh adds what he noticed: the famine will not be fattened by the plenty before it. Pharaoh half reads his own dream.")],
  'entries': [],
  'lost': [keeps("An added kai koimētheis, “and having gone to sleep,” in the Greek after I awoke."), between("Latin “showed no sign of being satisfied … I awoke, then fell asleep again” also adds the sleep; King James “So I awoke.”")]},

 '41:22': {
  'received': "I saw in my dream seven full good ears on one stalk,",
  'explain': ("The Greek says again in my sleep; the Latin very beautiful."),
  'shared': ["I saw in my dream.", "Seven ears came up on one stalk.", "They were full and good."],
  'instructions': [ins(K, S, "Pharaoh retold the second dream.")],
  'entries': [],
  'lost': [keeps("An added palin en tō hypnō mou, “again in my sleep,” in the Greek."), between("Hebrew, Latin and King James “I saw in my dream.”")]},

 '41:23': {
  'received': "and seven withered thin ears, scorched by the east wind, sprang up after them,",
  'explain': ("The Hebrew says withered, east wind, after them; the Greek wind-blasted, right next to them; the Latin struck by blight."),
  'shared': ["Seven other ears sprang up.", "They were thin and blighted by the wind.", "They came after the first."],
  'instructions': [ins(K, S, "Pharaoh described the blighted ears.")],
  'entries': [],
  'lost': [loses("Hebrew tzenumot … shedufot qadim … achareihen, “withered … scorched by the east wind … after them,” becomes Greek leptoi kai anemophthoroi … echomenoi autōn, “thin and wind-blighted … adjoining them.”"), between("Latin “thin and struck by blight” and King James “withered, thin, and blasted with the east wind” vary.")]},

 '41:24': {
  'received': "and the thin ears swallowed the seven good ears. I told the magicians, but none could explain.",
  'explain': ("The Greek adds fuller descriptions and says interpreters; the Latin there is no one."),
  'shared': ["The thin ears swallowed the seven good ears.", "I told the magicians.", "No one could explain it to me."],
  'instructions': [ins(K, S, "Pharaoh ended with the magicians’ failure.")],
  'entries': [],
  'lost': [between("Hebrew ha-chartummim, “the magicians,” is Greek tois exēgētais, “the interpreters,” with the ears again described as anemophthoroi; Latin “interpreters,” King James “magicians.”")]},

 '41:25': {
  'received': "Joseph said: Pharaoh’s dream is one; God has shown Pharaoh what He is about to do.",
  'explain': ("One dream, and God’s doing. The Hebrew says told; the Greek and Latin shown."),
  'shared': ["Pharaoh’s dream is one.", "God has shown Pharaoh.", "What He is about to do."],
  'instructions': [ins(K, S, "Joseph declared the two dreams one message from God."), ins(W, R, "“God has shown Pharaoh”: Joseph tells the king of Egypt that Egypt’s god did not send this. Interpretation here is also proclamation.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew higgid, “told,” is Greek edeixen, “showed”; Latin “shown,” King James “shewed.”")]},

 '41:26': {
  'received': "The seven good cows are seven years, and the seven good ears seven years: it is one dream.",
  'explain': ("The Greek repeats Pharaoh; the Latin adds years of plenty."),
  'shared': ["The seven good cows are seven years.", "The seven good ears are seven years.", "The dream is one."],
  'instructions': [ins(K, S, "Joseph read the sevens as years.")],
  'entries': [],
  'lost': [between("Greek to enypnion Pharaō hen estin, “Pharaoh’s dream is one,” repeats the name; Latin “seven years of plenty” anticipates; King James “the dream is one.”")]},

 '41:27': {
  'received': "The seven thin ugly cows and the seven empty wind-scorched ears are seven years of famine.",
  'explain': ("The Hebrew says empty, east wind; the Greek thin, wind-blighted; the Latin scorching wind."),
  'shared': ["The seven thin, ugly cows that came after are seven years.", "The seven empty ears scorched by the east wind.", "They are seven years of famine."],
  'instructions': [ins(K, S, "Joseph read the lean sevens as famine.")],
  'entries': [],
  'lost': [between("Hebrew reqot shedufot ha-qadim, “empty, scorched by the east wind,” is Greek leptoi kai anemophthoroi, “thin and wind-blighted”; Latin “thin ears struck by the scorching wind”; King James “empty ears blasted with the east wind.”")]},

 '41:28': {
  'received': "This is what I said to Pharaoh: God has shown Pharaoh what He is about to do.",
  'explain': ("The Hebrew, Greek and King James repeat verse 25; the Latin replaces it with they shall be fulfilled in this order."),
  'shared': ["This is the thing I have spoken to Pharaoh.", "What God is about to do.", "He has shown to Pharaoh."],
  'instructions': [ins(K, S, "Joseph repeated that God had revealed the future.")],
  'entries': ['elohim'],
  'lost': [between("Latin “They shall be fulfilled in this order” replaces Hebrew hu ha-davar asher dibbarti el-Par‘oh, “this is the word I have spoken to Pharaoh”; Greek and King James follow the Hebrew.")]},

 '41:29': {
  'received': "Seven years of great plenty are coming throughout Egypt.",
  'explain': ("The versions agree."),
  'shared': ["Behold, seven years are coming.", "They are years of great abundance.", "Throughout all the land of Egypt."],
  'instructions': [ins(K, S, "Seven years of plenty were foretold.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '41:30': {
  'received': "Then seven years of famine will follow; all the plenty will be forgotten and the famine will consume the land.",
  'explain': ("The versions agree."),
  'shared': ["Seven years of famine will arise after them.", "All the abundance will be forgotten in Egypt.", "The famine will consume the land."],
  'instructions': [ins(K, S, "Seven years of famine were foretold."), ins(W, R, "“All the plenty shall be forgotten”: the lean cows looked no fatter. Joseph tells Egypt that good years do not store themselves, which is the whole of his policy.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '41:31': {
  'received': "The plenty will not be known for the famine after it, so severe will it be.",
  'explain': ("The Latin says scarcity shall destroy the greatness of plenty."),
  'shared': ["The abundance will not be known in the land.", "Because of the famine following it.", "It will be very severe."],
  'instructions': [ins(K, S, "The famine would erase memory of the plenty.")],
  'entries': [],
  'lost': [between("Latin “the greatness of scarcity shall destroy the greatness of plenty” paraphrases; Hebrew, Greek and King James “the plenty shall not be known … for it shall be very grievous.”")]},

 '41:32': {
  'received': "The dream was doubled because the matter is fixed by God, and God will do it soon.",
  'explain': ("Why two dreams: certainty and haste. The Hebrew says the matter is established; the Greek the word from God will be true; the Latin a sign of certainty."),
  'shared': ["The dream was repeated to Pharaoh twice.", "The matter is established by God.", "God will hasten to do it."],
  'instructions': [ins(K, S, "The doubled dream meant certainty and speed."), ins(W, R, "Joseph had two dreams too, and they were doubly sure; the interpreter knows from his own life what a repeated dream means.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew nakhon ha-davar me-im ha-Elohim, “the matter is established from God,” is Greek alēthes estai to rhēma to para tou theou, “the word from God will be true”; Latin “a sign of certainty, because God’s word shall come to pass”; King James “the thing is established by God.”")]},

 '41:33': {
  'received': "Let Pharaoh find a discerning wise man and set him over Egypt.",
  'explain': ("Interpretation becomes counsel, unasked. The Hebrew says let Pharaoh look; the Greek addresses him, look; the Latin let the king provide."),
  'shared': ["Now therefore let Pharaoh look for a man.", "He should be discerning and wise.", "Set him over the land of Egypt."],
  'instructions': [ins(K, S, "Joseph advised appointing a wise administrator."), ins(W, R, "Joseph does not say choose me; he describes the man, and the description fits the speaker. Wisdom in Genesis is practical, and here it is also a job application.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew yere Par‘oh, “let Pharaoh look,” is Greek skepsai, “look,” addressed directly; Latin “let the king provide,” King James “let Pharaoh look out.”")]},

 '41:34': {
  'received': "Let Pharaoh appoint overseers and take a fifth of Egypt’s produce in the seven years of plenty.",
  'explain': ("A twenty per cent levy for seven years. The Greek says local governors, collect; the Latin throughout all the regions."),
  'shared': ["Let Pharaoh act and appoint overseers over the land.", "Let them take a fifth of Egypt’s produce.", "During the seven years of abundance."],
  'instructions': [ins(K, S, "Joseph proposed a fifth of the harvest be stored."), ins(W, R, "A fifth in the good years to live through the bad: the plan is simple arithmetic and no one in Egypt had thought of it. Revelation and prudence are one gift here.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew peqidim, “overseers,” is Greek toparchas, “local governors”; Hebrew ve-chimmesh, “and take a fifth,” is Greek kai apopemptōsatōsan panta ta genēmata, “let them take a fifth of all the produce”; Latin “overseers throughout all the regions,” King James “officers over the land.”")]},

 '41:35': {
  'received': "Let them gather the food of these good years and store grain under Pharaoh’s hand in the cities.",
  'explain': ("Centralised, royal, urban storage. The Greek adds seven; the Latin storehouses."),
  'shared': ["Let them gather all the food of these good years.", "Let grain be stored under Pharaoh’s hand.", "Let food be kept in the cities."],
  'instructions': [ins(K, S, "Grain was to be stored in the cities under Pharaoh.")],
  'entries': [],
  'lost': [keeps("An added hepta, “seven,” before good years in the Greek."), between("Latin “into storehouses … under Pharaoh’s authority” and King James “under the hand of Pharaoh” follow the Hebrew.")]},

 '41:36': {
  'received': "That food will be a reserve for the seven years of famine, so the land is not cut off.",
  'explain': ("The Hebrew says cut off; the Greek utterly destroyed; the Latin consumed by scarcity. The Hebrew-column rendering was corrected today."),
  'shared': ["That food shall be a reserve for the land.", "Against the seven years of famine in Egypt.", "So that the land is not cut off by the famine."],
  'instructions': [ins(K, S, "The reserve would save Egypt from the famine.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew ve-lo-tikkaret ha-aretz, “and the land will not be cut off,” is Greek kai ouk ektribēsetai hē gē, “and the land will not be utterly destroyed”; Latin “not consumed by scarcity,” King James “that the land perish not.”")]},

 '41:37': {
  'received': "The plan pleased Pharaoh and all his servants.",
  'explain': ("The Hebrew says the thing was good; the Greek the words were pleasing. The Hebrew-column rendering was corrected today."),
  'shared': ["The thing was good.", "In the eyes of Pharaoh.", "In the eyes of all his servants."],
  'instructions': [ins(K, S, "Pharaoh and his court approved Joseph’s plan.")],
  'entries': [],
  'lost': [between("Hebrew va-yitav ha-davar, “and the thing was good,” singular, is Greek ēresen de ta rhēmata, “and the words pleased,” plural; Latin “the counsel pleased,” King James “the thing was good.”")]},

 '41:38': {
  'received': "Pharaoh asked his servants: can we find a man like this, with the Spirit of God in him?",
  'explain': ("A pagan king names the Spirit of God. The Greek says all his servants; the Latin full of the Spirit."),
  'shared': ["Pharaoh said to his servants.", "Shall we find such a man as this?", "The Spirit of God is in him."],
  'instructions': [ins(K, S, "Pharaoh recognised God’s Spirit in Joseph."), ins(W, R, "Potiphar saw the Lord with Joseph, the jailer trusted him, Pharaoh names the Spirit of God; Egyptians see it at every stage, and his brothers never did.")],
  'entries': ['spirit-god-lord'],
  'lost': [keeps("An added pasin, “all,” before his servants in the Greek."), between("Latin “full of the Spirit of God,” Hebrew, Greek and King James “in whom the Spirit of God is.”")]},

 '41:39': {
  'received': "Pharaoh told Joseph: since God has shown you all this, none is so discerning and wise as you.",
  'explain': ("Joseph described in his own words of verse 33. The Latin makes it a question."),
  'shared': ["Since God has made all this known to you.", "No one is as discerning.", "No one is as wise as you."],
  'instructions': [ins(K, S, "Pharaoh judged Joseph the wisest man."), ins(W, R, "Pharaoh uses Joseph’s own words, “discerning and wise,” for Joseph; the description was heard as the interpreter meant it.")],
  'entries': ['elohim'],
  'lost': [between("Latin “can I find anyone wiser or like you?” makes a question; Hebrew, Greek and King James “there is none so discreet and wise as thou art.”")]},

 '41:40': {
  'received': "You shall be over my house, and all my people shall obey you; only the throne will be above you.",
  'explain': ("The dream of 37:8, shall you reign over us, answered by Pharaoh: yes, over Egypt. The versions agree."),
  'shared': ["You shall be over my house.", "All my people shall obey your word.", "Only in the throne will I be greater than you."],
  'instructions': [ins(K, S, "Pharaoh made Joseph second in Egypt."), ins(W, R, "“Over my house”: Potiphar’s words, the jailer’s practice, now Pharaoh’s decree. The same sentence is said three times at three heights, and the last is a kingdom.")],
  'entries': [],
  'lost': [AGREE]},

 '41:41': {
  'received': "Pharaoh said: I have set you over all the land of Egypt.",
  'explain': ("The Greek adds today; the Latin again."),
  'shared': ["Pharaoh said to Joseph.", "See, I have set you.", "Over all the land of Egypt."],
  'instructions': [ins(K, S, "Joseph was appointed over all Egypt.")],
  'entries': ['egypt'],
  'lost': [keeps("An added sēmeron, “today,” in the Greek."), between("Latin “said again … I have appointed you” and King James “See, I have set thee” follow the Hebrew.")]},

 '41:42': {
  'received': "Pharaoh gave Joseph his signet ring, fine linen robes and a gold chain.",
  'explain': ("Ring, linen, gold: the insignia of office. Joseph’s third set of clothes, after the coat and Potiphar’s robe. The Greek says a golden collar; the Hebrew chain."),
  'shared': ["Pharaoh took his signet ring and put it on Joseph’s hand.", "He clothed him in fine linen.", "He put a gold chain around his neck."],
  'instructions': [ins(K, S, "Joseph received the insignia of authority."), ins(W, R, "Stripped of a coat by brothers and a robe by a woman, Joseph is dressed by a king; the garments of his story go from envy to accusation to honour.")],
  'entries': [],
  'lost': [between("Hebrew bigde-shesh, “garments of fine linen,” is Greek stolēn byssinēn, “a robe of fine linen”; Hebrew revid ha-zahav, “the gold chain,” is Greek kloion chrysoun, “a golden collar”; Latin and King James follow the Hebrew.")]},

 '41:43': {
  'received': "He had him ride in his second chariot, and they cried before him, Abrek! and set him over all Egypt.",
  'explain': ("Abrek, an untranslated cry, Egyptian or Hebrew, perhaps bow the knee or attention. The Hebrew keeps it; the Greek says a herald proclaimed, without the word; the Latin that all should bend the knee and know."),
  'shared': ["He had him ride in his second chariot.", "They called out before him.", "He set him over all the land of Egypt."],
  'instructions': [ins(K, S, "Joseph rode in state as ruler of Egypt."), ins(W, R, "Sheaves bowed in the dream; now a herald calls for bowing before Joseph’s chariot. The dream is fulfilled in a word no one can translate.")],
  'entries': ['egypt'],
  'lost': [loses("Hebrew va-yiqre’u lefanav Avrekh, “and they called before him, Abrek,” the cry itself, becomes Greek kai ekēryxen emprosthen autou kēryx, “and a herald proclaimed before him,” the word lost."), between("Latin “a herald proclaiming that all should bend the knee before him” interprets; King James “Bow the knee.”")]},

 '41:44': {
  'received': "I am Pharaoh; without you no one shall lift hand or foot in all Egypt.",
  'explain': ("Total delegation. The Hebrew says hand or foot; the Greek hand alone; the Latin without your command."),
  'shared': ["I am Pharaoh.", "Without you no one will lift a hand.", "In all the land of Egypt."],
  'instructions': [ins(K, S, "Pharaoh gave Joseph total authority."), ins(W, R, "“I am Pharaoh”: the king keeps his name and gives Joseph everything else. The second dream’s sun and moon bow in the only way a king can, by delegation.")],
  'entries': ['egypt'],
  'lost': [loses("Hebrew yado ve-et-raglo, “his hand or his foot,” becomes Greek tēn cheira autou, “his hand,” alone."), between("Latin “no one shall move hand or foot” and King James “lift up his hand or foot” keep both.")]},

 '41:45': {
  'received': "Pharaoh named him Zaphenath-paneah and gave him Asenath, daughter of Potiphera priest of On; and Joseph went out over Egypt.",
  'explain': ("An Egyptian name, Egyptian wife, priestly father-in-law, Heliopolis the sun-god’s city. The Greek says Psonthomphanech, Heliopolis, and lacks the going out; the Latin Saviour of the World; the Hebrew Zaphenath-paneah, On."),
  'shared': ["Pharaoh named Joseph with an Egyptian name.", "He gave him Asenath, daughter of Potiphera, priest of On, as wife.", "Joseph went out over the land of Egypt."],
  'instructions': [ins(K, S, "Joseph received an Egyptian name and wife."), ins(W, R, "Joseph becomes Egyptian in name and marriage; the Hebrew slave is hidden under a court name, and his brothers will not know him. The disguise is honour, and it keeps the story.")],
  'entries': ['egypt'],
  'lost': [loses("Hebrew va-yetze Yosef al-eretz Mitzrayim, “and Joseph went out over the land of Egypt,” is absent from the Greek; Hebrew Tzafenat Pa‘neach … On is Greek Psonthomphanēch … Hēlioupoleōs."), between("Latin “in the Egyptian language, Saviour of the World … priest of Heliopolis” interprets the name; King James “Zaphnathpaaneah … priest of On.”")]},

 '41:46': {
  'received': "Joseph was thirty when he stood before Pharaoh; he went out from Pharaoh through all Egypt.",
  'explain': ("Thirty: thirteen years since the pit at Dothan. The Latin compresses."),
  'shared': ["Joseph was thirty years old when he stood before Pharaoh, king of Egypt.", "He went out from Pharaoh’s presence.", "He journeyed through all the land of Egypt."],
  'instructions': [ins(K, S, "Joseph was thirty at his elevation."), ins(W, R, "Thirteen years from seventeen to thirty, slave and prisoner; the age of David’s accession and of another beginning. The dreamer’s apprenticeship is counted and done.")],
  'entries': ['egypt'],
  'lost': [between("Latin “he was thirty years old when he stood before King Pharaoh—and travelled through all the regions of Egypt” compresses; Hebrew, Greek and King James keep “went out from the presence of Pharaoh.”")]},

 '41:47': {
  'received': "In the seven plenteous years the land produced by the handful.",
  'explain': ("Li-qmatzim, by handfuls, bursting; the Greek sheaves; the Latin gathered into storehouses."),
  'shared': ["The seven years of abundance came.", "The earth produced.", "It produced abundantly."],
  'instructions': [ins(K, S, "The seven years of plenty came as foretold.")],
  'entries': [],
  'lost': [between("Hebrew li-qmatzim, “by handfuls,” is Greek dragmata, “sheaves”; Latin “gathered into sheaves … collected in Egypt’s storehouses”; King James “by handfuls.”")]},

 '41:48': {
  'received': "He gathered all the food of the seven years in Egypt and stored it in the cities, each city’s surrounding fields within it.",
  'explain': ("The Greek adds in which there was abundance and says plains; the Latin compresses to each city. The Hebrew-column rendering was corrected today."),
  'shared': ["He gathered all the food of the seven years in the land of Egypt.", "He stored the food in the cities.", "The food of each city’s surrounding fields he stored within it."],
  'instructions': [ins(K, S, "Joseph stored each region’s grain in its city.")],
  'entries': ['egypt'],
  'lost': [keeps("An added en hois ēn hē euthēnia, “in which there was abundance,” in the Greek; Hebrew sedeh ha-ir, “the field of the city,” is Greek tōn pediōn tēs poleōs, “the plains of the city.”"), between("Latin “All the abundance of produce was stored in each city” compresses; King James follows the Hebrew.")]},

 '41:49': {
  'received': "Joseph stored grain like the sand of the sea, until he stopped counting, for it was beyond count.",
  'explain': ("Sand of the sea, the simile of Abraham’s seed, now for grain. The Hebrew says he stopped counting; the Greek they could not count; the Latin exceeded measure."),
  'shared': ["Joseph stored grain like the sand of the sea.", "It was so much that counting stopped.", "It was beyond counting."],
  'instructions': [ins(K, S, "Joseph’s stores were beyond counting."), ins(W, R, "Grain as the sand of the sea: the promise’s simile is spent on bread. The seed of Abraham is kept alive by a storehouse counted in the words of the covenant.")],
  'entries': [],
  'lost': [between("Hebrew ad ki-chadal lispor, “until he ceased to count,” is Greek heōs ouk ēdynanto arithmēsai, “until they could not count”; Latin “its quantity exceeded measure,” King James “until he left numbering.”")]},

 '41:50': {
  'received': "Before the famine two sons were born to Joseph by Asenath, daughter of Potiphera priest of On.",
  'explain': ("The Hebrew says before the year of famine; the Greek the seven years, Heliopolis; the Latin before the famine."),
  'shared': ["Two sons were born to Joseph.", "It was before the famine came.", "Asenath, daughter of Potiphera, priest of On, bore them."],
  'instructions': [ins(K, S, "Joseph had two sons before the famine.")],
  'entries': [],
  'lost': [between("Hebrew shenat ha-ra‘av, “the year of famine,” is Greek ta hepta etē tou limou, “the seven years of famine”; Hebrew On is Greek Hēlioupoleōs; Latin “Heliopolis,” King James “On.”")]},

 '41:51': {
  'received': "He named the firstborn Manasseh: God has made me forget all my toil and my father’s house.",
  'explain': ("Manasseh, from nashah, forget. The Hebrew says all my father’s house; the Greek all the affairs of my father; the Latin my father’s house."),
  'shared': ["Joseph named the firstborn Manasseh.", "God has made me forget all my toil.", "And all my father’s house."],
  'instructions': [ins(K, S, "Manasseh was named for forgetting."), ins(W, R, "“God has made me forget my father’s house”: Joseph says it, and the next chapters prove it untrue. The name is a hope, and the hope is undone by ten men at a grain counter.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew kol-bet avi, “all my father’s house,” is Greek pantōn tōn tou patros mou, “all the things of my father”; Latin and King James “my father’s house.”")]},

 '41:52': {
  'received': "The second he named Ephraim: God has made me fruitful in the land of my affliction.",
  'explain': ("Ephraim, from parah, be fruitful. The Hebrew says made me fruitful, affliction; the Greek increased me, humiliation; the Latin poverty."),
  'shared': ["He named the second Ephraim.", "God has made me fruitful.", "In the land of my affliction."],
  'instructions': [ins(K, S, "Ephraim was named for fruitfulness in affliction."), ins(W, R, "Fruitful in the land of affliction: Joseph names his son with the promise to Jacob, 35:11, and calls Egypt what it is. Both names are prayers, one to forget, one to grow.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew hifrani, “made me fruitful,” the root of Ephraim, is Greek ēuxēsen me, “increased me”; Hebrew onyi, “my affliction,” is Greek tapeinōseōs mou, “my humiliation”; Latin “my poverty,” King James “my affliction.”")]},

 '41:53': {
  'received': "The seven years of plenty in Egypt ended.",
  'explain': ("The versions agree."),
  'shared': ["The seven years of abundance.", "They were in the land of Egypt.", "They ended."],
  'instructions': [ins(K, S, "The years of plenty ended.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '41:54': {
  'received': "The seven years of famine began, as Joseph said; there was famine in all lands, but in Egypt there was bread.",
  'explain': ("The Hebrew says all lands; the Greek all the land; the Latin the whole world."),
  'shared': ["The seven years of famine began, as Joseph had said.", "There was famine in all the lands.", "In all Egypt there was bread."],
  'instructions': [ins(K, S, "Famine came everywhere but Egypt had bread."), ins(W, R, "Bread in Egypt alone: the stage is set for Jacob’s sons. The famine that will bring them is the one Joseph has already fed.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew be-khol ha-aratzot, “in all the lands,” plural, is Greek en pasē tē gē, “in all the land”; Latin “throughout the whole world,” King James “in all lands.”")]},

 '41:55': {
  'received': "When Egypt hungered the people cried to Pharaoh, and he said, Go to Joseph and do what he tells you.",
  'explain': ("Go to Joseph: Pharaoh’s whole policy. The versions agree."),
  'shared': ["All the land of Egypt hungered and the people cried to Pharaoh for bread.", "Pharaoh said to all the Egyptians, Go to Joseph.", "Whatever he says to you, do."],
  'instructions': [ins(K, S, "Pharaoh directed Egypt to Joseph for bread."), ins(W, R, "“Go to Joseph”: the king sends his people to the Hebrew for bread. The Church has heard in it a figure, and Egypt heard in it dinner.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '41:56': {
  'received': "The famine was over all the earth; Joseph opened the stores and sold to the Egyptians, as the famine grew severe in Egypt.",
  'explain': ("Sold, not gave: the state’s grain is bought. The Hebrew ends the famine prevailed in Egypt; the Greek lacks the clause and says granaries; the Latin grew daily."),
  'shared': ["The famine was over the face of all the earth.", "Joseph opened all the storehouses and sold to the Egyptians.", "The famine was severe in Egypt."],
  'instructions': [ins(K, S, "Joseph sold grain as the famine deepened.")],
  'entries': ['egypt'],
  'lost': [loses("Hebrew va-yechezaq ha-ra‘av be-eretz Mitzrayim, “and the famine was strong in the land of Egypt,” is absent from the Greek, which has sitobolōnas, “granaries,” for the stores."), between("Latin “for famine oppressed them also” and King James “the famine waxed sore in the land of Egypt” keep it.")]},

 '41:57': {
  'received': "All the earth came to Egypt to buy from Joseph, for the famine was severe everywhere.",
  'explain': ("The Hebrew says all the earth came; the Greek all the countries; the Latin all the provinces. The Hebrew-column rendering was corrected today."),
  'shared': ["All the earth came to Egypt to buy.", "They bought from Joseph.", "The famine prevailed in all the earth."],
  'instructions': [ins(K, S, "The nations came to Joseph for grain."), ins(W, R, "All the earth comes to Joseph for bread, and the dream of stars bowing widens past his family to the nations; Abraham’s seed feeds the world a generation before it is a nation.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew ve-khol-ha-aretz ba’u, “and all the earth came,” is Greek kai pasai hai chōrai ēlthon, “and all the countries came”; Latin “all the provinces,” King James “all countries.”")]},
 }
}
