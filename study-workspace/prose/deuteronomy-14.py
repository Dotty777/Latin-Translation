K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
BIRDS = [between("The bird names are uncertain in every column; the Hebrew identifications are provisional and the Greek lists differ in order and number. The prose gives each column's list and does not map one onto the other.")]
NAME = [loses("Hebrew 'to make His name dwell there' is lost."), keeps("Greek 'for His name to be invoked there'."), between("The Latin and King James follow the Hebrew.")]
GATES = [between("The Greek has 'in your cities' for the Hebrew 'within your gates'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'deuteronomy', 'chapter': 14,
 'chapterNote': "Children of YHWH: mourning, food and tithe. No cutting or shaving for the dead, for you are his holy, treasured people. Eat nothing abominable: the clean beasts by divided hoof and cud, the forbidden camel, hare, hyrax and pig; fish by fins and scales; the unclean birds listed; no winged swarmers; no carcass (give it to the alien or sell to the foreigner); no kid boiled in its mother's milk. Tithe the yield yearly and eat it before YHWH at the place of his name with the firstborn, to learn to fear him; if far, turn it to silver and buy what you wish there, and rejoice with household and Levite. Every third year store the tithe at home for the Levite, alien, orphan and widow, that YHWH may bless your work. The Greek has an uncertain rite (phoibao) for 'cut yourselves' (14:1), 'calf, lamb, young goat' (14:4), 'giraffe' and other beasts for the Hebrew's uncertain species (14:5), different bird names, order and count (14:12–18, hawk moved to 14:17), 'lamb' for 'kid' (14:21), 'invoked' for the name dwelling (14:23–24), 'sell and take' (14:25), runs the Levite into 14:26 without 'do not abandon' (14:27), and 'in that year … in your cities' (14:28). The Latin at 14:28 has 'another tithe'.",
 'verses': {
  '14:1': v("You are children of YHWH your God; do not cut yourselves or make a bald patch between your eyes for the dead.", "The Hebrew 'cut yourselves'; the Greek phoibao, an uncertain rite, perhaps purification.",
   ["Children of YHWH.", "Do not cut yourselves.", "Nor shave for the dead."], "Sonship forbids pagan mourning.", "'Children of YHWH': the first time Deuteronomy calls Israel God's sons, and it is to forbid them the mourning rites of the nations. A child of this God grieves differently.",
   [loses("Hebrew 'cut yourselves' is lost."), keeps("Greek phoibao, a rare verb of uncertain sense, perhaps 'perform purification rites'."), between("The Latin and King James have 'cut yourselves'.")], ['yhwh-yahweh'], "Do not cut yourselves or shave for the dead."),
  '14:2': v("For you are a holy people to YHWH your God, and YHWH chose you to be his treasured people from all the peoples on earth.", "The Greek adds 'your God'.",
   ["A holy people.", "YHWH chose you.", "His treasured people."], "Holiness grounds the laws.", "7:6 repeated as the ground of the food laws: a treasured people eats like one. The diet is a mark of belonging, not of hygiene.", [keeps("Greek 'the Lord your God chose you'.")], ['yhwh-yahweh']),
  '14:3': v("Do not eat anything abominable.", "The Latin 'unclean things'.",
   ["Do not eat.", "Anything.", "Abominable."], "The food laws open.", "To'evah, the word for idolatry's abomination (7:26, 12:31), used of food: what is on the plate is in the same moral register as what is on the altar.", [between("The Latin has 'unclean things'; the Greek and Hebrew 'abominable'.")], [], "Do not eat anything abominable."),
  '14:4': v("These are the animals you may eat: cattle, sheep and goats,", "The Greek 'calf, lamb, young male goat'.",
   ["The animals you may eat.", "Cattle and sheep.", "Goats."], "The herd animals are clean.", "The three domestic kinds, the animals of the altar: what may be sacrificed may be eaten. The list begins with the familiar.", [between("The Greek has 'calf, lamb, young male goat'; the Hebrew the general kinds.")], []),
  '14:5': v("deer, gazelle, fallow deer, ibex, antelope, wild ox and mountain sheep.", "The species are uncertain; the Greek has 'giraffe' and other names.",
   ["Deer and gazelle.", "Ibex and antelope.", "Wild ox and mountain sheep."], "Seven wild kinds are clean.", "Seven wild kinds, several of whose names are guesses in every language. Game is clean by the same test as cattle, and the hunter eats with the herdsman.",
   [between("The Hebrew species are tentative; the Greek has 'bubalos, goat-stag, giraffe' among others; the Latin and King James make their own guesses.")], []),
  '14:6': v("Any animal with a divided hoof, split in two, that chews the cud, you may eat.", "All four columns agree.",
   ["A divided hoof.", "Chews the cud.", "You may eat."], "The rule for beasts.", "Two marks, both required: the cleft foot and the cud. The rule is simpler than the list, and the list exists for the cases the rule leaves doubtful.", [AGREE], []),
  '14:7': v("But of those that chew the cud or have a divided hoof you may not eat the camel, hare and hyrax; they chew the cud but do not divide the hoof; they are unclean for you.", "The Greek expands the hoof description.",
   ["Camel, hare, hyrax.", "They chew the cud.", "But do not divide the hoof."], "One mark is not enough.", "Camel, hare, hyrax: the ancient observation that they chew is kept as written; the law classifies by what the eye sees, not by modern anatomy.", [between("The Greek expands 'divide the hoof' into a fuller phrase.")], []),
  '14:8': v("And the pig, because it divides the hoof but does not chew the cud, is unclean for you; do not eat their flesh or touch their carcasses.", "The Greek expands the hoof description.",
   ["The pig.", "Divides the hoof, no cud.", "Do not eat or touch."], "The pig is the type case.", "The pig, with the right foot and the wrong stomach: the one animal whose exclusion became Israel's badge among the nations, from Antiochus to the Roman legions.", [AGREE], []),
  '14:9': v("Of all in the waters you may eat whatever has fins and scales.", "All four columns agree.",
   ["All in the waters.", "Fins and scales.", "You may eat."], "The rule for fish.", "Fins and scales: the fish of the lake and the sea, which the Galilee fishermen would sort on the shore (Matthew 13:48).", [AGREE], []),
  '14:10': v("Whatever has no fins and scales you may not eat; it is unclean for you.", "All four columns agree.",
   ["No fins and scales.", "Do not eat.", "Unclean."], "Shellfish and eels are out.", "The negative stated after the positive: eel, catfish, shellfish. The sea's unclean are the things that do not look like fish.", [AGREE], []),
  '14:11': v("Every clean bird you may eat.", "All four columns agree.",
   ["Every clean bird.", "You may eat.", "The rule for birds."], "Birds are clean by default.", "No rule of foot or stomach for birds; the law gives a list of exceptions and lets the rest be clean. Most of the air is permitted.", [AGREE], []),
  '14:12': v("These are the birds you may not eat: the eagle, the bearded vulture, the osprey,", "The Hebrew names are provisional; the Greek 'griffon' is an ancient bird-name.",
   ["Birds you may not eat.", "The eagle.", "Vulture and osprey."], "The raptors head the list.", "The great birds of prey first: eagle, vulture, osprey. The unclean birds are the eaters of flesh and carrion, by every ancient reading.", BIRDS, []),
  '14:13': v("the kite, the falcon and the buzzard by its kind,", "The Hebrew has three names, the Greek two; the identifications are tentative.",
   ["The kite.", "The falcon.", "The buzzard by its kind."], "More raptors.", "'By its kind': the list names a family and covers its relatives. Three Hebrew names, two Greek, and no one certain which bird is which.", BIRDS, []),
  '14:14': v("every raven by its kind,", "All four columns agree.",
   ["Every raven.", "By its kind.", "Unclean."], "The raven is unclean.", "The raven, carrion-eater and Noah's first scout: the one bird on the list every reader can picture.", [AGREE], []),
  '14:15': v("the ostrich, the night bird, the gull and the hawk by its kind,", "The Greek places the hawk at 14:17; tahmas is uncertain.",
   ["The ostrich.", "The night bird and gull.", "The hawk by its kind."], "Desert and shore birds.", "Ostrich, night bird, gull, hawk: the desert, the dark and the shore. The Hebrew tahmas is left as 'night bird' because no one knows.", BIRDS + [between("The Greek puts the hawk in 14:17.")], []),
  '14:16': v("the little owl, the great owl, the white owl,", "The Greek names differ materially from the conventional Hebrew owls.",
   ["The little owl.", "The great owl.", "The white owl."], "Three owls.", "Three words usually read as owls, and the Greek reads them as other birds entirely. The uncertainty is the honest state of the text.", BIRDS, []),
  '14:17': v("the pelican, the carrion vulture and the cormorant,", "The Greek has a different sequence and more names here, including the hawk and hoopoe.",
   ["The pelican.", "The carrion vulture.", "The cormorant."], "Water birds.", "Pelican, vulture, cormorant in the Hebrew; the Greek adds the hawk and hoopoe here. The two lists cannot be set side by side bird for bird.", BIRDS, []),
  '14:18': v("the stork, the heron by its kind, the hoopoe and the bat.", "The Greek sequence differs; both end with the bat.",
   ["The stork and heron.", "The hoopoe.", "And the bat."], "The list ends with the bat.", "The bat closes the list of birds: the ancient category is 'things that fly', and the bat flies. The law speaks the language of the eye.", BIRDS, []),
  '14:19': v("Every winged swarming thing is unclean for you; they shall not be eaten.", "The Greek addresses the eater directly.",
   ["Every winged swarmer.", "Unclean.", "Not to be eaten."], "Insects are out.", "The winged swarmers: Deuteronomy omits Leviticus 11's exception for the locust, and so is stricter than its source by silence.", [between("The Greek has 'you shall not eat'.")], []),
  '14:20': v("Every clean flying thing you may eat.", "The Latin 'everything clean'.",
   ["Every clean flying thing.", "You may eat.", "The permission closes."], "The air is mostly open.", "Permission repeated after the prohibitions: the law closes the bird section as it opened, with what may be eaten.", [between("The Latin has 'everything clean'; the Greek 'every clean flying creature'.")], []),
  '14:21': v("Do not eat any carcass; give it to the alien in your gates to eat or sell it to a foreigner, for you are a holy people to YHWH your God. Do not boil a kid in its mother's milk.", "The Greek 'lamb' for 'kid'; paroikos for the alien; both allow sale.",
   ["No carcass.", "Give or sell it to the foreigner.", "No kid in its mother's milk."], "Two more rules.", "The carcass may feed the alien and be sold to the foreigner: the holiness is Israel's, not a judgment on the meat. 'A kid in its mother's milk': the third time the Torah says it, and the root of the separation of meat and milk.",
   [loses("Hebrew 'a kid' is lost."), keeps("Greek 'a lamb in its mother's milk'."), between("The Latin and King James have 'kid'; the Greek paroikos is the resident alien.")], ['yhwh-yahweh'], "Do not eat any carcass; do not boil a kid in its mother's milk."),
  '14:22': v("Tithe all the yield of your seed that comes from the field year by year.", "The Greek specifies seed and field.",
   ["Tithe all the yield.", "Of your seed.", "Year by year."], "The annual tithe.", "A tenth of the field every year: in Deuteronomy the tithe is not only the Levites' due (Numbers 18) but the family's festival fund, as the next verses show.", [AGREE], [], "Tithe all the yield of your field year by year."),
  '14:23': v("Eat before YHWH your God at the place he chooses to make his name dwell the tithe of your grain, wine and oil and the firstborn of your cattle and flocks, that you may learn to fear YHWH your God always.", "The Greek adds 'bring' and 'invoked'.",
   ["Eat before YHWH.", "The tithe and the firstborn.", "To learn to fear YHWH always."], "The tithe is eaten at the sanctuary.", "'That you may learn to fear': the tithe as education. A family eating its own tenth before God at the one place learns, by feasting, whose the harvest is.", NAME, ['yhwh-yahweh', 'wheat', 'grapevine', 'olive-tree']),
  '14:24': v("If the way is too long to carry it, because the place YHWH your God chooses to put his name is far, when YHWH your God blesses you,", "The Greek 'invoked' and a future blessing.",
   ["If the way is too long.", "The place is far.", "When YHWH blesses you."], "Distance is allowed for.", "'When YHWH blesses you': a big harvest and a long road. The law foresees the farmer in Galilee who cannot drive his tenth to Jerusalem.", NAME, ['yhwh-yahweh']),
  '14:25': v("exchange it for silver, bind the silver in your hand, and go to the place YHWH your God chooses.", "The Greek 'sell and take'.",
   ["Exchange it for silver.", "Bind the silver in your hand.", "Go to the place."], "The tithe may travel as money.", "'Bind the silver in your hand': the tithe becomes coin for the journey and food again at the end. Holiness is portable.", [between("The Greek has 'sell it for silver and take the silver'; the Hebrew 'exchange … bind'.")], ['yhwh-yahweh']),
  '14:26': v("Spend the silver on whatever you desire, cattle, sheep, wine, strong drink, whatever you wish, and eat there before YHWH your God and rejoice, you and your household.", "The Greek carries the participants into the next verse.",
   ["Spend it on whatever you desire.", "Cattle, sheep, wine, strong drink.", "Eat and rejoice before YHWH."], "The tithe is a feast.", "'Wine, strong drink, whatever you wish': the tithe is spent on a party. Deuteronomy's holiness includes shekar at God's table, and commands the rejoicing.", [between("The Latin has 'feast'; the Greek runs on into 14:27.")], ['yhwh-yahweh'], "Eat before YHWH and rejoice, you and your household."),
  '14:27': v("Do not abandon the Levite in your gates, for he has no share or inheritance with you.", "The Greek lacks 'do not abandon' and joins the Levite to the rejoicing.",
   ["Do not abandon the Levite.", "In your gates.", "He has no share."], "The Levite shares the feast.", "The Levite again, at every feast: the landless man is invited by law to the landholder's table, every year.", [loses("Hebrew 'do not abandon the Levite' is lost."), keeps("Greek 'and the Levite … because he has no share' as part of the rejoicing.")] + GATES, [], "Do not abandon the Levite in your gates."),
  '14:28': v("At the end of three years bring out all the tithe of your produce in that year and store it in your gates.", "The Latin 'another tithe'; the Greek 'in that year … in your cities'.",
   ["At the end of three years.", "All the tithe.", "Store it in your gates."], "The third-year tithe stays home.", "Every third year the tenth does not travel: it stays in the town as a store. The feast tithe becomes a poor tithe, and the sanctuary yields to the neighbour.", [between("The Latin has 'set apart another tithe'; the Greek 'stored in that year in your cities'.")] + GATES, [], "Every third year store the tithe in your gates."),
  '14:29': v("The Levite, who has no share with you, and the alien, orphan and widow in your gates shall come and eat and be satisfied, that YHWH your God may bless you in all the work of your hand.", "The Greek 'newcomer', 'cities', lacks 'of your hand'.",
   ["Levite, alien, orphan, widow.", "Shall eat and be satisfied.", "That YHWH may bless your work."], "The four poor eat the tithe.", "Levite, stranger, orphan, widow: Deuteronomy's four, named together for the first time. The tithe that feeds them is the condition of the blessing on the field; the harvest's future depends on who ate the last one.", GATES + [between("The Greek lacks 'of your hand'.")], ['yhwh-yahweh'], "Let the Levite, alien, orphan and widow eat and be satisfied."),
 },
}
