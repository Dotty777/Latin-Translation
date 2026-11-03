K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
FORMULA = [between("The Latin, Greek and King James all have the speech formula; the divine name is rendered 'the Lord' outside the Hebrew.")]
SHEKEL = [loses("Hebrew 'shekels … sanctuary shekel' is lost."), keeps("Greek 'didrachmas … by the sacred weight'; the number is the same."), between("The Latin and King James have 'shekels of the sanctuary'.")]
JUB = [loses("Hebrew 'Jubilee' is lost."), keeps("Greek 'release'."), between("The Latin and King James have 'jubilee'.")]
FIFTH = [between("All four columns have the added fifth.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'leviticus', 'chapter': 27,
 'chapterNote': "The appendix on vows and valuations: a person vowed to YHWH is redeemed at a fixed price by age and sex (fifty shekels for a man of twenty to sixty, thirty for a woman, down to five and three for infants), or by the priest's judgment if poor; a vowed sacrificial animal is holy and cannot be swapped; an unclean animal or a house is valued by the priest and redeemed at a fifth more; a field is valued by its seed and the years to the Jubilee, forfeited to the priests if sold unredeemed, while a purchased field returns to its owner at the Jubilee; the sanctuary shekel is twenty gerahs; firstborn animals cannot be vowed since they are already God's; devoted things (herem) are never redeemed, and a devoted person dies; the tithe of land is holy, redeemable at a fifth, and the tithe of herd and flock is every tenth under the staff, not to be examined or exchanged. The book closes: these are the commandments YHWH gave Moses for Israel on Mount Sinai. The Greek has 'the valuation of his soul' for 'persons' (27:2), 'didrachmas … sacred weight' for shekels and 'obols' for gerahs (27:3–7, 25), one prohibition verb at 27:10, 'kor' for 'homer' (27:16), 'release' for Jubilee, 'when the release has passed' for 'when the field is released in the Jubilee' (27:21), 'from the year of release' for 'until the year of Jubilee' (27:23), adds 'and it shall be his' (27:27, 31) and 'in the count' (27:32), and at 27:33 lacks the prohibition on examining quality. The Latin has 'thirty modii' at 27:16.",
 'verses': {
  '27:1': v("YHWH speaks to Moses.", "All four columns agree.", ["YHWH speaks.", "To Moses.", "On vows."],
   "YHWH spoke on vows and valuations.", "After the colophon of 26:46, one more speech; the book did not quite end, since people kept promising God things and needed to know the price.", FORMULA, ['yhwh-yahweh', 'moses']),
  '27:2': v("Speak to Israel: if a man makes a special vow concerning persons to YHWH, by your valuation,",
   "The Hebrew 'concerning persons' generally; the Greek 'for the valuation of his soul', his own person.",
   ["A special vow.", "Concerning persons.", "By valuation."], "Persons vowed were redeemed by valuation.", "A person vowed to God, as Hannah vowed Samuel; the law lets the vow be paid in silver instead, and sets the rate.",
   [loses("Hebrew 'concerning persons' is lost."), keeps("Greek 'a vow for the valuation of his soul'."), between("The Latin and King James have 'the persons shall be for the Lord'.")], ['yhwh-yahweh']),
  '27:3': v("A male from twenty to sixty: fifty shekels of silver by the sanctuary shekel.", "The Hebrew shekels; the Greek didrachmas 'by the sacred weight'. The number agrees.",
   ["A male twenty to sixty.", "Fifty shekels.", "Sanctuary weight."], "The prime male was fifty shekels.", "Fifty shekels, the price of a man in his strength; the same sum Joseph's brothers did not get for him.", SHEKEL),
  '27:4': v("For a female, thirty shekels.", "All four columns agree on the number.", ["A female.", "Thirty shekels.", "Twenty to sixty."],
   "A woman was thirty shekels.", "Thirty: the valuation follows the labour market of the time, and Zechariah and the gospels will remember the figure for another sale.", SHEKEL),
  '27:5': v("From five to twenty: twenty shekels for a male, ten for a female.", "All four columns agree.",
   ["Five to twenty years.", "Twenty for a male.", "Ten for a female."], "Youths were valued lower.", "The young are worth less in silver, since the vow is paid in what a body can do; the law does not pretend otherwise.", SHEKEL),
  '27:6': v("From one month to five years: five shekels for a male, three for a female.", "All four columns agree; the Greek does not repeat 'silver' for the female.",
   ["One month to five years.", "Five for a male.", "Three for a female."], "Infants had a price.", "A month-old child can be vowed and redeemed for five shekels, the same sum that redeems a firstborn; the vowed infant is treated like a firstborn.", SHEKEL),
  '27:7': v("From sixty upward: fifteen shekels for a male, ten for a female.", "All four columns agree; the Greek adds 'silver'.",
   ["Sixty and upward.", "Fifteen for a male.", "Ten for a female."], "The old were valued low but not least.", "The old man is worth more than the boy and less than the man; the old woman's ten shekels do not fall from her youth. The scale is honest about strength and quiet about worth.", SHEKEL),
  '27:8': v("If he is too poor for the valuation, he is set before the priest, who values him by what the vower's hand can afford.", "All four columns agree; the Greek 'he shall stand'.",
   ["Too poor.", "Before the priest.", "Valued by his means."], "The poor paid what they could.", "The table bends for the poor: the priest looks at the man and his purse and names a price he can pay. A vow is not to ruin anyone.",
   [keeps("Greek 'he shall stand before the priest'."), between("The Latin and King James have 'present himself'.")], ['high-priest']),
  '27:9': v("If it is an animal of a kind offered to YHWH, whatever is given is holy.", "All four columns agree.",
   ["A sacrificial animal.", "Given to YHWH.", "Holy."], "Vowed clean animals were holy.", "A vowed lamb is holy from the word; it belongs to the altar before it reaches it.", [AGREE], ['yhwh-yahweh']),
  '27:10': v("He does not replace or exchange it, good for bad or bad for good; if he does, both are holy.", "The Hebrew two verbs; the Greek one.",
   ["No replacing.", "No exchanging.", "Both become holy."], "Swapping a vowed animal made both holy.", "Try to swap the fat lamb for a thin one and you lose both; the law's penalty for cleverness is doubling the gift.",
   [loses("Hebrew 'replace it or exchange it' is lost."), keeps("Greek 'he shall not exchange it'."), between("The Latin and King James have both verbs.")], [], "He shall not exchange it, good for bad or bad for good."),
  '27:11': v("If an unclean animal, not offered to YHWH, he sets it before the priest.", "All four columns agree.",
   ["An unclean animal.", "Not for the altar.", "Before the priest."], "Unclean animals were valued, not offered.", "A donkey vowed to God cannot be sacrificed, so it is priced; the vow is honoured in silver.", [AGREE], ['high-priest']),
  '27:12': v("The priest values it, good or bad; as the priest values it, so it is.", "All four columns agree; the Hebrew briefly addresses the priest as 'you'.",
   ["The priest values it.", "Good or bad.", "His word stands."], "The priest's valuation was final.", "'As you, the priest, value it': the law speaks to the priest directly for a moment, as the man whose word is the price.",
   [keeps("Greek third person 'as the priest values it'."), between("The Hebrew has 'as you, the priest'; the Latin and King James third person.")], ['high-priest']),
  '27:13': v("If he redeems it, he adds a fifth to the valuation.", "All four columns agree.",
   ["Redeeming it.", "Add a fifth.", "To the valuation."], "Redemption cost a fifth more.", "A fifth for taking back what was given; the surcharge on second thoughts.", FIFTH),
  '27:14': v("If a man consecrates his house to YHWH, the priest values it, good or bad; so it stands.", "The Hebrew, Greek and King James agree; the Latin 'sold at his price'.",
   ["Consecrating a house.", "The priest values it.", "It stands."], "Houses were valued like animals.", "A house given to God is a sum of silver in the priest's mouth; the vow turns bricks to shekels.",
   [between("The Latin has 'the priest examines it and it is sold at his price'; the Greek and King James 'the valuation stands'.")], ['yhwh-yahweh', 'high-priest']),
  '27:15': v("If the consecrator redeems his house, he adds a fifth of the valuation's silver and it is his.", "All four columns agree.",
   ["Redeeming the house.", "A fifth added.", "It is his."], "Houses could be bought back.", "The same fifth; the man who gave his house in a moment of zeal may live in it again, at a price.", FIFTH),
  '27:16': v("If a man consecrates part of his inherited field, the valuation follows its seed: fifty shekels for a homer of barley sown.", "The Hebrew homer and shekels; the Greek kor and didrachmas; the Latin 'thirty modii'.",
   ["Part of a field.", "Valued by seed.", "Fifty shekels per homer."], "Fields were valued by seed capacity.", "The field is measured by what it takes to sow it; its worth is the barley it swallows.",
   SHEKEL + [loses("Hebrew 'homer' is lost."), keeps("Greek 'a kor of barley'."), between("The Latin has 'thirty modii'; the King James 'homer'.")]),
  '27:17': v("If he consecrates it from the Jubilee year, it stands at the full valuation.", "All four columns agree.",
   ["From the Jubilee.", "Full valuation.", "It stands."], "A field vowed at Jubilee paid in full.", "Fifty years of harvests ahead, fifty shekels; the Jubilee is the zero from which every field is counted.", JUB),
  '27:18': v("If after the Jubilee, the priest calculates by the years left to the Jubilee and deducts from the valuation.", "All four columns agree; the Greek adds 'later'.",
   ["After the Jubilee.", "Years remaining counted.", "A deduction."], "Later vows were prorated.", "The arithmetic of chapter 25 applied to a gift to God: he too takes only the harvests that remain.", JUB, ['high-priest']),
  '27:19': v("If the consecrator redeems the field, he adds a fifth and it is confirmed as his.", "All four columns agree.",
   ["Redeeming the field.", "A fifth added.", "Confirmed as his."], "Fields were redeemable with a fifth.", "The fifth again; the field goes back to the family at a premium.", FIFTH),
  '27:20': v("If he does not redeem it and sells it to another, it can no longer be redeemed.", "All four columns agree; the sale's subject is debated.",
   ["Not redeemed.", "Sold to another.", "No more redemption."], "Selling a vowed field forfeited it.", "To vow a field and then sell it is to sell God's property; the right of redemption dies with the double dealing.", [AGREE]),
  '27:21': v("When the field is released in the Jubilee it is holy to YHWH like a devoted field; it becomes the priest's.",
   "The Hebrew 'when the field is released in the Jubilee'; the Greek 'when the release has passed', an anomaly the source leaves as is.",
   ["Released in the Jubilee.", "Holy like a devoted field.", "The priest's."], "Forfeited fields went to the priests.", "At the horn the field does not go home; it goes to the priests, as if devoted. The only land the Jubilee does not return is land God has already taken.",
   JUB + [loses("Hebrew 'when the field is released in the Jubilee' is lost."), keeps("Greek 'when the release has passed … like land set apart'.")], ['high-priest']),
  '27:22': v("If he consecrates a purchased field, not of his inheritance,", "All four columns agree.",
   ["A purchased field.", "Not inherited.", "Consecrated."], "Bought fields were a separate case.", "Bought land is only leased harvests; vowing it is vowing someone else's Jubilee.", [AGREE]),
  '27:23': v("The priest calculates the valuation until the Jubilee, and he gives it that day as holy to YHWH.", "The Hebrew 'until the year of Jubilee'; the Greek 'from the year of release'.",
   ["Calculated to the Jubilee.", "Given that day.", "Holy to YHWH."], "The purchased field's value was paid at once.", "He pays the harvests' worth in silver on the spot, since the field itself will leave him at the horn.",
   JUB + [loses("Hebrew 'until the year of Jubilee' is lost."), keeps("Greek 'from the year of release'.")], ['yhwh-yahweh']),
  '27:24': v("In the Jubilee the field returns to the one he bought it from, whose possession it is.", "All four columns agree.",
   ["In the Jubilee.", "Returns to the seller.", "His possession."], "Bought fields reverted at Jubilee.", "The land goes home to its family even over God's head; the vow cannot override the Jubilee's grant.", JUB),
  '27:25': v("Every valuation is by the sanctuary shekel; the shekel is twenty gerahs.", "The Hebrew shekel and gerah; the Greek didrachma and obol, retaining twenty.",
   ["By the sanctuary shekel.", "Twenty gerahs.", "A fixed weight."], "The shekel was defined.", "Twenty gerahs to the shekel: a standard weight so no priest can inflate the price and no vower shave it.",
   SHEKEL + [loses("Hebrew 'gerahs' is lost."), keeps("Greek 'the didrachma shall be twenty obols'."), between("The Latin and King James have 'gerahs' or 'obols'.")]),
  '27:26': v("No one consecrates a firstborn animal that is already YHWH's by birth; ox or sheep, it is YHWH's.", "All four columns agree.",
   ["Firstborn animals.", "Already YHWH's.", "Cannot be vowed."], "Firstborn could not be re-given.", "You cannot give God what is already his; the firstborn was claimed in Egypt and a vow adds nothing.", [AGREE], ['yhwh-yahweh', 'egypt']),
  '27:27': v("If an unclean animal, he ransoms it by valuation plus a fifth; if not redeemed, it is sold at valuation.", "All four columns agree; the Greek 'exchange' and adds 'and it shall be his'.",
   ["An unclean firstborn.", "Ransomed with a fifth.", "Or sold."], "Unclean firstborn were redeemed or sold.", "The firstborn donkey cannot go to the altar; it is bought back or sold for the sanctuary, as in Exodus 13.",
   FIFTH + [keeps("Greek 'he shall exchange it according to its valuation … and it shall be his'.")]),
  '27:28': v("Any devoted thing a man devotes to YHWH, person, animal or field, is neither sold nor redeemed; every devoted thing is most holy.", "All four columns agree.",
   ["A devoted thing.", "Person, animal or field.", "Never redeemed."], "Devoted things were irrevocable.", "Herem, the ban: beyond the vow and beyond redemption, given so completely that no silver reaches it. Jericho will be herem.", [AGREE], ['yhwh-yahweh'], "Every devoted thing is most holy to YHWH."),
  '27:29': v("No person devoted to destruction may be ransomed; he is put to death.", "All four columns agree; the Hebrew 'devoted to destruction' is contextual.",
   ["A devoted person.", "Not ransomed.", "Put to death."], "Devoted persons died.", "The law's hardest line: a person under the ban dies and cannot be bought back. Who may lay the ban is not said here, and the question has troubled readers since Jephthah.",
   [between("The Hebrew, Greek, Latin and King James agree; neither names who imposes the ban.")]),
  '27:30': v("Every tithe of the land, seed or fruit, is YHWH's; it is holy.", "All four columns agree.",
   ["Every tithe.", "Seed or fruit.", "Holy to YHWH."], "The tithe was God's.", "A tenth of everything that grows, holy before any vow; the land's rent, due to the landlord of 25:23.", [AGREE], ['yhwh-yahweh'], "Every tithe of the land is holy to YHWH."),
  '27:31': v("If a man redeems any of his tithe, he adds a fifth.", "All four columns agree; the Greek adds 'and it shall be his'.",
   ["Redeeming the tithe.", "A fifth added.", "Some of it."], "Tithes could be redeemed at a fifth.", "Even the tithe can be turned to silver, at the usual fifth; the law prefers goods but accepts coin.", FIFTH + [keeps("Greek 'and it shall be his'.")]),
  '27:32': v("Every tithe of herd and flock, every animal passing under the staff, the tenth is holy to YHWH.", "All four columns agree; the Greek 'in the count'.",
   ["Tithe of herd and flock.", "Under the staff.", "The tenth holy."], "Every tenth animal was tithed.", "The shepherd's rod counts the sheep through the gate and the tenth is marked; no choosing, just counting.", [keeps("Greek 'everything that comes under the staff in the count'.")], ['yhwh-yahweh']),
  '27:33': v("He does not examine good or bad or exchange it; if he exchanges, both are holy; not redeemed.", "The Hebrew forbids examining quality and all exchange; the Greek only 'good for bad' and leaves the original's holiness implicit.",
   ["No examining.", "No exchanging.", "Both holy, unredeemed."], "The tithed animal was taken as it came.", "Whatever the rod touches is God's, good or lame; the tithe is not a selection but a lot, and the tenth beast is beyond swapping or buying back.",
   [loses("Hebrew 'he shall not examine whether it is good or bad' is lost."), keeps("Greek 'you shall not exchange a good one for a bad one'."), between("The Latin and King James follow the Hebrew.")], [], "He shall not examine or exchange the tithed animal."),
  '27:34': v("These are the commandments YHWH commanded Moses for Israel on Mount Sinai.", "All four columns agree.",
   ["These are the commandments.", "Through Moses.", "On Mount Sinai."], "The book ended at Sinai.", "Leviticus closes where it has stood all along, at the foot of the mountain by the tent: the commandments, Moses, Israel, Sinai. Numbers will move the camp.", [AGREE], ['yhwh-yahweh', 'moses', 'sinai']),
 },
}
