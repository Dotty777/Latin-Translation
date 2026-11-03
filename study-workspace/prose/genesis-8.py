# Study prose for Genesis 8 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 8,
 'chapterNote': (
  "The receding of the waters, the birds, the leaving of the ark and the first altar are the same story in every column. What varies "
  "is the calendar and a few images. The Hebrew keeps the seventeenth day for the ark’s landing, the tenth month for the mountain tops, "
  "a raven that goes out and back, a freshly plucked olive leaf, YHWH speaking “in his heart,” and summer and winter. The Greek keeps "
  "the twenty-seventh day, so that its flood lasts exactly a year, the eleventh month for the mountains, a raven sent “to see” that "
  "does not return, a dry piece with the olive leaf, the Lord God speaking “after reflecting” about human “works,” summer and spring, "
  "and the name Lord God or God where the Hebrew varies. The Latin alone names the mountains of Armenia and gives the dove a green "
  "olive branch; the King James follows the Hebrew throughout."),
 'verses': {

 '8:1': {
  'received': "God remembered Noah and the creatures with him, sent a wind over the earth, and the waters began to subside.",
  'explain': ("The turn of the flood is a single verb: God remembered. When God remembers, he acts, as he will remember his covenant "
   "in Egypt. A wind passes over the earth and the water goes down; the word for wind is the one used of the Spirit over the water in "
   "1:2, so the new beginning opens as the first did. The Greek adds birds and creeping things to the remembered creatures."),
  'shared': ["God remembered Noah and the animals in the ark.", "God sent a wind over the earth.", "The waters subsided."],
  'instructions': [ins(K, S, "God remembered Noah and began to end the flood."), ins(W, R, "To be remembered by God is to be acted for; the waiting in the ark ends with his remembering, not with Noah’s effort.")],
  'entries': ['noah', 'noahs-ark'],
  'lost': [
   keeps("An added kai pantōn tōn peteinōn kai pantōn tōn herpetōn, “and all the birds and all the creeping things,” to the remembered company; the Hebrew names the wild animals and livestock only."),
   between("Hebrew ruach and Greek pneuma both mean wind here, the word of 1:2. Latin and King James list the animals as the Hebrew does. Exodus 2:24 and Luke 1:54 and 1:72 take up God’s remembering."),
  ]},

 '8:2': {
  'received': "The springs of the deep and the windows of heaven were shut, and the rain was held back.",
  'explain': ("What opened in 7:11 now closes, from below and from above, and the rain stops. The Hebrew says the springs and windows "
   "were stopped; the Greek says the springs of the abyss and the floodgates of heaven were covered over. The ending of the inflow "
   "is the same in all."),
  'shared': ["The springs of the deep were closed.", "The windows of heaven were closed.", "The rain from heaven was restrained."],
  'instructions': [ins(K, S, "God closed the sources of the flood above and below.")],
  'entries': [],
  'lost': [between("Hebrew va-yissakheru, “were stopped,” is Greek epekalyphthēsan, “were covered over”; Hebrew arubbot, “windows,” is Greek katarraktai, “floodgates,” as in 7:11; Hebrew tehom, “deep,” is Greek abyssos. Latin “closed … floodgates” and King James “stopped … windows” divide.")]},

 '8:3': {
  'received': "The waters steadily receded from the earth and after a hundred and fifty days had gone down.",
  'explain': ("The receding is a process, and each language has its own way of saying so: the Hebrew doubles the verb, going and "
   "returning; the Greek says the water receded as it went; the Latin pictures it flowing back and forth. The hundred and fifty days "
   "of 7:24 are reached and the water is lower."),
  'shared': ["The waters receded from the earth.", "The receding was continuous.", "After a hundred and fifty days the waters had decreased."],
  'instructions': [ins(K, S, "The flood receded over a hundred and fifty days.")],
  'entries': [],
  'lost': [between("Hebrew halokh va-shov, “going and returning,” is Greek poreuomenon, “as it went”; Latin “flowing back and forth” and King James “returned … continually” each catch part of the idiom. The number agrees in all.")]},

 '8:4': {
  'received': "In the seventh month the ark came to rest on the mountains of Ararat.",
  'explain': ("The ark lands. The Hebrew, Latin and King James date it to the seventeenth day of the seventh month; the Greek to the "
   "twenty-seventh, continuing the ten-day difference of 7:11. The Hebrew verb is “rested,” from the root of Noah’s name; the Greek "
   "says “settled.” The mountains are plural in all. The Latin alone names them the mountains of Armenia. Ararat is the land known in old records as Urartu."),
  'shared': ["The ark came to rest.", "It was in the seventh month.", "It rested on the mountains of Ararat."],
  'instructions': [ins(K, S, "The ark rested on the mountains of Ararat in the seventh month."), ins(W, R, "The ark finds rest on a mountain while the earth is still under water; rest comes before the end of the trouble.")],
  'entries': ['ararat', 'noahs-ark'],
  'lost': [
   loses("Hebrew be-shiv‘ah-asar yom, “on the seventeenth day,” becomes Greek hebdomē kai eikadi, “on the twenty-seventh,” as at 7:11. Hebrew va-tanach, “rested,” from nuach, echoes Noah’s name; Greek ekathisen, “settled,” does not."),
   keeps("The Greek date keeps its own calendar consistent: landing five months to the day after the flood began."),
   between("Latin gives the twenty-seventh with the Greek but “mountains of Armenia” for Ararat; King James gives the seventeenth and Ararat with the Hebrew. 2 Kings 19:37 names the land."),
  ]},

 '8:5': {
  'received': "The waters kept falling until the tenth month, and on the first day of a month the mountain tops appeared.",
  'explain': ("The tops of the mountains come into view, with the verb of 1:9, where the dry land appeared. The Hebrew, Latin and King "
   "James date it to the first day of the tenth month; the Greek to the first day of the eleventh. This is a month’s difference in the "
   "stated date, not a question of translating a numeral."),
  'shared': ["The waters continued to decrease until the tenth month.", "On the first day of a month the tops of the mountains appeared.", "Land is seen again."],
  'instructions': [ins(K, S, "The mountain tops appeared as the waters fell.")],
  'entries': [],
  'lost': [
   loses("Hebrew ba-asiri, “in the tenth month,” for the appearance of the mountain tops becomes Greek tō hendekatō mēni, “in the eleventh month.” The Hebrew has the water decrease until the tenth month and the tops appear in that same month; the Greek puts the appearance a month later."),
   keeps("Greek ōphthēsan, “appeared,” is the verb of 1:9; the Greek, like the Hebrew, lets the land rise as on the third day."),
   between("Latin and King James give the tenth month with the Hebrew."),
  ]},

 '8:6': {
  'received': "After forty days Noah opened the window he had made in the ark.",
  'explain': ("Noah acts for the first time since entering. After forty days he opens the window. The word here is an ordinary Hebrew "
   "window, a different word from the disputed opening of 6:16, and Greek, Latin and King James all have a window. The Latin runs "
   "straight on to the raven, which the others keep for the next verse."),
  'shared': ["Forty days passed.", "Noah opened the window of the ark.", "It was the window he had made."],
  'instructions': [ins(K, S, "Noah opened the ark’s window after forty days.")],
  'entries': ['noah', 'noahs-ark'],
  'lost': [between("Hebrew challon and Greek thyris are both “window,” unlike the tsohar of 6:16. Latin adds “and released a raven” here; King James keeps the Hebrew division.")]},

 '8:7': {
  'received': "Noah sent out the raven, which went out and did not settle back until the waters had dried from the earth.",
  'explain': ("The first scout is a raven, an unclean bird under the law. The Hebrew says it went out and back, to and fro, until the "
   "waters dried; the Greek says it was sent to see whether the water had subsided, went out, and did not return until the earth was "
   "dry. Neither gives the bird a motive. God later feeds Elijah by ravens."),
  'shared': ["Noah sent out the raven.", "It went out.", "This continued until the waters dried from the earth."],
  'instructions': [ins(K, S, "The raven was the first bird sent from the ark."), ins(W, R, "The first messenger brings no news; waiting is part of the story of deliverance.")],
  'entries': [],
  'lost': [
   loses("Hebrew va-yetse yatso va-shov, “it went out, going out and returning,” has the raven come and go. Greek exelthōn ouch hypestrepsen, “having gone out it did not return,” states nonreturn. The Hebrew’s to-and-fro is gone."),
   keeps("An added tou idein ei kekopaken to hydōr, “to see whether the water had subsided,” giving the raven the purpose the Hebrew gives only to the dove in 8:8."),
   between("Latin “went out and did not return until the waters … had dried” follows the Greek; King James “went forth to and fro” follows the Hebrew. Leviticus 11:15 and Luke 12:24 take up the raven."),
  ]},

 '8:8': {
  'received': "Noah sent out the dove to see whether the waters had gone down from the ground.",
  'explain': ("The second scout is a dove, with a stated purpose. The Hebrew says Noah sent it “from him”; the Greek and Latin say "
   "“after it,” linking it to the raven. The dove will return at Jesus’ baptism, when the Spirit descends like a dove, a link "
   "Tertullian drew."),
  'shared': ["Noah sent out the dove.", "Its purpose was to see whether the waters had abated.", "The question was the face of the ground."],
  'instructions': [ins(K, S, "Noah sent the dove to learn whether the earth was dry."), ins(W, R, "Noah looks for evidence before leaving; faith is patient and observant.")],
  'entries': [],
  'lost': [between("Hebrew me-itto, “from him,” locates the sending with Noah; Greek opisō autou, “after it,” orders it after the raven. Latin “after it” follows the Greek; King James “from him” the Hebrew. Hebrew adamah, “ground,” is Greek gē, “earth.” Matthew 3:16 brings the dove back.")]},

 '8:9': {
  'received': "The dove found no resting place and returned, and Noah reached out and took it back into the ark.",
  'explain': ("The dove fails and comes home, and Noah receives it with his hand. Water still covers the whole earth. The Hebrew says "
   "the sole of its foot; the Greek its feet. The scene is tender and the versions agree in every detail that matters."),
  'shared': ["The dove found no place to rest.", "It returned to Noah in the ark because water covered the earth.", "Noah stretched out his hand and took it in."],
  'instructions': [ins(K, S, "The dove returned because the earth was still covered."), ins(W, R, "Noah takes back the bird that brings no news; the one who waits is also the one who shelters.")],
  'entries': ['noah'],
  'lost': [between("Hebrew le-khaf-raglah, “for the sole of its foot,” is Greek tois posin autēs, “for its feet.” Latin and King James give Noah’s full action as the Hebrew does. Hebrew ha-yonah is “the dove”; the Latin says “it.”")]},

 '8:10': {
  'received': "Noah waited another seven days and sent the dove out again.",
  'explain': ("The story keeps time in weeks: seven days before the rain in 7:4, and now two weeks of waiting here and in verse 12. Noah "
   "waits and tries again. All versions agree."),
  'shared': ["Noah waited another seven days.", "He sent the dove out again.", "He sent it from the ark."],
  'instructions': [ins(K, S, "Noah waited a week before sending the dove again."), ins(W, R, "Patience is measured in weeks here; Noah does not force the door.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James agree. Greek hēmeras hepta heteras, “another seven days,” recurs at 8:12.")]},

 '8:11': {
  'received': "The dove returned toward evening with an olive leaf in its beak, and Noah knew the waters had gone down.",
  'explain': ("The sign arrives. The dove comes back in the evening with something from an olive tree, and Noah understands. The Hebrew "
   "has a freshly plucked olive leaf; the Greek an olive leaf with a dry piece, an awkward addition; the Latin an olive branch with "
   "green leaves. The exact botany is left as each column has it. Trees are growing again."),
  'shared': ["The dove returned toward evening.", "It carried an olive leaf in its beak.", "Noah knew the waters had abated from the earth."],
  'instructions': [ins(K, S, "The olive leaf told Noah that the earth was recovering."), ins(W, R, "A small living thing is enough evidence; hope reads signs that are easy to miss.")],
  'entries': ['noah'],
  'lost': [
   loses("Hebrew aleh-zayit taraf, “a freshly plucked olive leaf,” with hinneh, “behold.” Greek phyllon elaias karphos, “an olive leaf, a dry piece,” adds karphos, a stalk or twig, in an unexplained apposition, and drops “behold.” The freshness is gone from the Greek."),
   between("Latin “an olive branch with green leaves” expands in the other direction; King James “an olive leaf pluckt off” follows the Hebrew."),
  ]},

 '8:12': {
  'received': "Noah waited another seven days and sent out the dove, and it did not return.",
  'explain': ("The third sending is the last. The dove does not come back, because it has found a place to live. Noah now knows the "
   "earth is habitable, though he still waits for God’s word to leave. The Greek repeats “again” before the sending; otherwise the "
   "versions agree."),
  'shared': ["Noah waited another seven days.", "He sent out the dove.", "It did not return to him again."],
  'instructions': [ins(K, S, "The dove’s not returning showed the earth was habitable."), ins(W, R, "Good news can come as an absence; the dove’s silence is the sign.")],
  'entries': [],
  'lost': [between("Greek adds palin, “again,” before the sending; the Hebrew, Latin and King James have the sending without it. All say it did not return.")]},

 '8:13': {
  'received': "On the first day of Noah’s six hundred and first year the waters had gone, and Noah removed the covering and saw the ground was drying.",
  'explain': ("A new year begins with the earth re-emerging. The date agrees in all: year 601, first month, first day, the date on "
   "which the tabernacle will later be raised. The Hebrew says the waters dried and the face of the ground was dry; the Greek says the "
   "water had left the earth. The Hebrew has Noah remove the covering; the Greek names the roof and adds that he had made the ark."),
  'shared': ["It was the first day of the first month of the six hundred and first year.", "The waters had gone from the earth.", "Noah removed the covering of the ark and looked out."],
  'instructions': [ins(K, S, "On New Year’s Day of the six hundred and first year Noah saw the earth drying."), ins(W, R, "The new world begins on the first day of the first month; a calendar restarts with the uncovered ark.")],
  'entries': ['noah', 'noahs-ark'],
  'lost': [
   loses("Hebrew charevu ha-mayim, “the waters dried,” and hinneh charevu pene ha-adamah, “behold, the face of the ground was dry,” become Greek exelipen to hydōr, “the water had left,” twice; the ground’s dryness becomes the water’s departure, and “behold” is dropped. Hebrew mikhseh, “covering,” is Greek stegē, “roof.”"),
   keeps("Greek specifies “of Noah’s life” and “that he had made,” tying the date and the ark back to 7:6 and 6:14."),
   between("Latin “opened the ark’s roof … saw that the surface of the ground was dry” stands between; King James “removed the covering … the face of the ground was dry” follows the Hebrew. Exodus 40:2 and 40:17 share the date."),
  ]},

 '8:14': {
  'received': "By the twenty-seventh day of the second month the earth was dry.",
  'explain': ("The flood ends on a date all the versions share: the twenty-seventh of the second month. Because the Greek began the "
   "flood on the twenty-seventh (7:11), its flood lasts exactly a year; the Hebrew, starting on the seventeenth, gives a year and ten "
   "days. The earth is dry, and the exit can be commanded."),
  'shared': ["It was the second month.", "It was the twenty-seventh day.", "The earth was dry."],
  'instructions': [ins(K, S, "The earth was fully dry on the twenty-seventh day of the second month.")],
  'entries': [],
  'lost': [between("Hebrew, Greek, Latin and King James all give the twenty-seventh of the second month. In the Greek calendar the flood runs from 27/2 to 27/2, one year exactly; in the Hebrew from 17/2 to 27/2, a year and ten days.")]},

 '8:15': {
  'received': "God spoke to Noah.",
  'explain': ("For the first time since 7:1 God speaks. The word comes before Noah moves. The Hebrew says God; the Greek the Lord God; "
   "the Latin and King James God. The verse is the hinge between dryness and departure."),
  'shared': ["God spoke.", "He spoke to Noah.", "What follows is his word."],
  'instructions': [ins(K, S, "Noah waited for God’s word before leaving the ark."), ins(W, R, "The earth was dry before the word came; Noah leaves on command, not on his own judgement.")],
  'entries': ['noah', 'lord-translation'],
  'lost': [
   loses("Hebrew Elohim, “God,” becomes Greek kyrios ho theos, “the Lord God.”"),
   between("Latin and King James say God with the Hebrew."),
  ]},

 '8:16': {
  'received': "God told Noah to go out of the ark with his wife, his sons and his sons’ wives.",
  'explain': ("The command to leave, with the household listed. Noah’s wife is named before the sons, in every version, a different "
   "order from the entry in 7:7. The eight who went in are the eight who come out."),
  'shared': ["Noah is to go out of the ark.", "His wife is to go with him.", "His sons and their wives are to go with him."],
  'instructions': [ins(C, S, "Go out from the ark with your household.")],
  'entries': ['noah', 'noahs-ark'],
  'lost': [between("Hebrew, Greek, Latin and King James agree in words and order: Noah, his wife, his sons, his sons’ wives.")]},

 '8:17': {
  'received': "Noah was to bring out every living creature with him so that they might increase and multiply on the earth.",
  'explain': ("The animals are released with a blessing like that of 1:22 and 1:28. The Hebrew speaks of the animals in the third "
   "person: that they may swarm, be fruitful and multiply. The Greek ends with plural commands addressed to the hearers, increase and "
   "multiply, and has no separate swarm verb. The Latin adds “go forth upon the earth.”"),
  'shared': ["Noah is to bring out every living creature with him.", "Birds, livestock and creeping things are included.", "They are to be fruitful and multiply on the earth."],
  'instructions': [ins(C, S, "Bring out every living thing from the ark."), ins(K, S, "The creatures were released to multiply on the earth again."), ins(W, R, "The blessing of creation is spoken again over a cleansed earth; the flood did not cancel God’s first intentions.")],
  'entries': ['noahs-ark'],
  'lost': [
   loses("Hebrew ve-shartsu … u-faru ve-ravu, “that they may swarm … be fruitful and multiply,” three verbs about the animals, become Greek auxanesthe kai plēthynesthe, two plural imperatives, “increase and multiply,” addressed to the hearers. The swarming is gone and the subject shifts."),
   between("Latin “Go forth upon the earth; increase and multiply upon it” adds a command and addresses the hearers like the Greek; King James “that they may breed abundantly … be fruitful, and multiply” follows the Hebrew."),
  ]},

 '8:18': {
  'received': "Noah went out with his wife, his sons and his sons’ wives.",
  'explain': ("The exit, as commanded. The Greek lists Noah’s wife first, matching the command of 8:16; the Hebrew, Latin and King James "
   "list the sons first, as at the entry in 7:7. The membership of the family is the same whichever way it is ordered."),
  'shared': ["Noah went out of the ark.", "His sons went out with him.", "His wife and his sons’ wives went out with him."],
  'instructions': [ins(K, S, "Noah and his household left the ark.")],
  'entries': ['noah'],
  'lost': [between("Hebrew Noach u-vanav ve-ishto, “Noah, his sons and his wife,” is Greek Nōe kai hē gynē autou kai hoi huioi autou, “Noah and his wife and his sons.” Latin and King James keep the Hebrew order; the Greek keeps the order of the command in 8:16.")]},

 '8:19': {
  'received': "All the animals, creeping things and birds left the ark by their kinds.",
  'explain': ("The creatures follow. The Hebrew lists wild animals, creeping things, birds and everything that moves, and says they went "
   "out by their families; the Greek lists wild animals, livestock, birds and creeping things, by their kinds. The Latin has no birds in "
   "its list. The earth is repopulated from one door."),
  'shared': ["Every animal went out of the ark.", "Every creeping thing and bird went out.", "They went out according to their kinds."],
  'instructions': [ins(K, S, "The animals left the ark in their kinds.")],
  'entries': ['noahs-ark'],
  'lost': [
   loses("Hebrew le-mishpechoteihem, “according to their families,” becomes Greek kata genos autōn, “according to their kinds,” the word of chapter 1. The Hebrew’s repeated “everything moving” is replaced in Greek by “all the livestock.”"),
   between("Latin lists wild animals, livestock and creeping things without birds; King James follows the Hebrew list and “after their kinds.”"),
  ]},

 '8:20': {
  'received': "Noah built an altar to the Lord and offered burnt offerings of clean animals and birds.",
  'explain': ("The first act in the new world is worship, and the first altar in Scripture is Noah’s. He takes from the clean animals and "
   "birds, the ones brought in sevens, and burns them whole. The Hebrew names YHWH; the Greek says God. The Greek word for the offerings "
   "makes the whole-burning explicit, the kind of offering later laid out in Leviticus 1."),
  'shared': ["Noah built an altar to the Lord.", "He took from every clean animal and bird.", "He offered burnt offerings on the altar."],
  'instructions': [ins(K, S, "Noah’s first act after the flood was to offer sacrifice."), ins(W, R, "Thanksgiving comes before building a house; the new world is dedicated before it is settled.")],
  'entries': ['altar', 'noah', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew la-YHWH, “to YHWH,” becomes Greek tō theō, “to God.”"),
   keeps("Greek holokarpōseis, “whole burnt offerings,” spells out what Hebrew olot implies: offerings wholly consumed. Thysiastērion, “altar,” is the first in Scripture, the word of Hebrews 13:10."),
   between("Latin “to the Lord … whole burnt offerings” and King James “unto the LORD … burnt offerings” keep the Hebrew name."),
  ]},

 '8:21': {
  'received': "The Lord accepted the offering and resolved never again to curse the ground or strike all life because of human evil.",
  'explain': ("God receives the sacrifice and makes a resolution. The Hebrew says YHWH smelled the pleasing aroma and said in his heart; "
   "the Greek says the Lord God said after reflecting. The reason is the same in all and surprising: because the human heart is bent on "
   "evil from youth, not although. The Hebrew says he will not curse the ground because of humankind; the Greek because of human works. The promise stands despite enduring evil."),
  'shared': ["The Lord smelled the pleasing aroma.", "He will never again curse the ground because of humankind.", "He will never again strike every living thing as he has done."],
  'instructions': [ins(K, S, "God promised never again to destroy all life as in the flood."), ins(W, R, "God’s patience rests on his knowledge of the heart’s evil, not on hope that it will improve; mercy is given with eyes open.")],
  'entries': ['yhwh-yahweh', 'lord-translation'],
  'lost': [
   loses("Hebrew va-yomer YHWH el-libbo, “YHWH said in his heart,” becomes Greek eipen kyrios ho theos dianoētheis, “the Lord God said after reflecting”; Hebrew ba‘avur ha-adam, “because of humankind,” becomes dia ta erga tōn anthrōpōn, “because of human works”; Hebrew yetser lev ha-adam, “the inclination of the human heart,” becomes hē dianoia tou anthrōpou enkeitai epimelōs, “the human mind is intently set.”"),
   keeps("An added dia touto, “therefore,” making the inference between the two promises explicit. The Greek reads God’s inner speech as reflection, as it did in 6:6."),
   between("Latin “said … because of human beings … inclinations and thoughts … prone to evil” and King James “said in his heart … for man’s sake … imagination of man’s heart” keep the Hebrew frame, the Latin with its own phrasing."),
  ]},

 '8:22': {
  'received': "For all the earth’s days, seedtime and harvest, cold and heat, summer and winter, day and night will not cease.",
  'explain': ("The promise is spelled out as the steadiness of the seasons. Sowing and harvest, cold and heat, the two halves of the year, "
   "and day and night will go on. The Hebrew pairs summer with winter; the Greek pairs summer with spring. In the Hebrew day and night "
   "are among the things that will not cease; in the Greek they are adverbs, “by day or by night.” Paul tells the Lystrans that rain and fruitful seasons are God’s witness."),
  'shared': ["The promise holds for all the days of the earth.", "Seedtime and harvest, cold and heat will not cease.", "The seasons and day and night will continue."],
  'instructions': [ins(K, S, "God pledged the regular order of seasons and days while the earth lasts."), ins(W, R, "The ordinary turning of the year is a promise kept daily; it is where God’s faithfulness is most seen and least noticed.")],
  'entries': [],
  'lost': [
   loses("Hebrew qayits va-choref, “summer and winter,” becomes Greek theros kai ear, “summer and spring.” Hebrew yom va-lailah, “day and night,” are subjects that “shall not cease”; Greek hēmeran kai nykta are accusatives, “by day or by night.” The Hebrew winter is not in the Greek."),
   between("Latin “summer and winter, night and day” and King James “summer and winter, and day and night” keep the Hebrew pairs. Acts 14:17 makes the seasons God’s witness."),
  ]},
 }
}
