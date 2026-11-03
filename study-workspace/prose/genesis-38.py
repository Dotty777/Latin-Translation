# Study prose for Genesis 38 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 38,
 'chapterNote': (
  "Judah and Tamar: the Canaanite marriage, Er and Onan, the widow kept waiting, the veil at Enaim, the pledge, the sentence of burning, and the twins Perez and "
  "Zerah, from whom David comes. The columns agree on the story; the Hebrew keeps Shua as the father of Judah’s wife (“the daughter of Shua”), “he was at Chezib,” "
  "YHWH as the one who slew Er and Onan, Hirah as Judah’s “friend,” “wrapped herself,” “the entrance to Enaim,” “signet and cord,” “she was not given,” qedeshah in "
  "38:21, “this one came out first,” and “she is more in the right than I.” The Greek keeps Shua as the wife’s own name, “she was at Chasbi when she bore them,” "
  "“God” for YHWH, Hirah as Judah’s “shepherd,” “adorned herself,” “the gates of Ainan,” “ring and necklace,” “he had not given her,” an added “he did not recognise "
  "her,” “this one will come out first,” and “Tamar is more in the right.” One Hebrew-column rendering was corrected today. The Latin and King James follow the "
  "Hebrew; the Latin says “she stopped bearing” after Shelah and runs 38:27–28 together."),
 'verses': {

 '38:1': {
  'received': "At that time Judah left his brothers and turned aside to Hirah, an Adullamite.",
  'explain': ("Judah goes down from the brothers, away from the father’s grief and his own part in it, to the Canaanite lowland. The Hebrew says turned aside to; the Greek arrived as far as. The Hebrew-column rendering was corrected today."),
  'shared': ["It was at that time.", "Judah went down from his brothers.", "He turned aside to an Adullamite man named Hirah."],
  'instructions': [ins(K, S, "Judah left his brothers for Adullam."), ins(W, R, "Judah, who proposed the sale, goes down; the Joseph story pauses to follow the brother whose descendants will be kings, and finds him among Canaanites.")],
  'entries': [],
  'lost': [between("Hebrew va-yet ad-ish Adullami, “and turned aside to an Adullamite man,” is Greek kai aphiketo heōs pros anthrōpon tina Odollamitēn, “and arrived as far as a certain Adullamite man”; Latin and King James “turned aside / turned in.”")]},

 '38:2': {
  'received': "There Judah saw the daughter of a Canaanite named Shua, married her and went in to her.",
  'explain': ("The marriage Abraham forbade: a Canaanite wife, and the mother of Judah’s line. The Hebrew names the father Shua; the Greek reads the relative as feminine and names the woman Shua; the Latin and King James follow the Hebrew."),
  'shared': ["Judah saw there the daughter of a Canaanite man.", "The name was Shua.", "He took her as his wife and went in to her."],
  'instructions': [ins(K, S, "Judah married a Canaanite woman."), ins(W, R, "Judah marries into Canaan with no father to forbid it; the tribe of David begins in the marriage the patriarchs refused, and God will work with it.")],
  'entries': ['canaan'],
  'lost': [loses("Hebrew bat-ish Kena‘ani u-shmo Shua, “the daughter of a Canaanite man, and his name Shua,” becomes Greek thygatera anthrōpou Chananaiou hē onoma Saua, “a Canaanite man’s daughter whose name was Shua”; the name moves from father to daughter."), between("Latin “a Canaanite man named Shua” and King James “a certain Canaanite, whose name was Shuah” keep the father.")]},

 '38:3': {
  'received': "She conceived and bore a son, named Er.",
  'explain': ("The Hebrew says he named him; the Greek and Latin she, as for the next two."),
  'shared': ["She conceived.", "She bore a son.", "He was named Er."],
  'instructions': [ins(K, S, "Er was born to Judah.")],
  'entries': [],
  'lost': [between("Hebrew va-yiqra, “and he called,” masculine, is Greek ekalesen without subject, Latin “named him,” King James “he called his name Er.”")]},

 '38:4': {
  'received': "She conceived again and bore a son, named Onan.",
  'explain': ("The versions agree."),
  'shared': ["She conceived again.", "She bore a son.", "She named him Onan."],
  'instructions': [ins(K, S, "Onan was born to Judah.")],
  'entries': [],
  'lost': [AGREE]},

 '38:5': {
  'received': "She bore another son, Shelah; Judah was at Chezib when she bore him.",
  'explain': ("Three sons. The Hebrew says he was at Chezib when she bore him; the Greek she was at Chasbi when she bore them; the Latin she stopped bearing children."),
  'shared': ["She bore another son.", "She named him Shelah.", "The birth was at Chezib."],
  'instructions': [ins(K, S, "Shelah was born at Chezib.")],
  'entries': [],
  'lost': [between("Hebrew ve-hayah vi-Khziv be-lidtah oto, “and he was at Chezib when she bore him,” is Greek autē de ēn en Chasbi hēnika eteken autous, “she was at Chasbi when she bore them”; Latin “After his birth she stopped bearing children” substitutes; King James follows the Hebrew.")]},

 '38:6': {
  'received': "Judah took a wife for Er, his firstborn: Tamar.",
  'explain': ("Tamar, palm tree, enters; her origin is not given. The versions agree."),
  'shared': ["Judah took a wife for Er his firstborn.", "Her name.", "Tamar."],
  'instructions': [ins(K, S, "Tamar married Er.")],
  'entries': [],
  'lost': [AGREE]},

 '38:7': {
  'received': "Er was wicked in the Lord’s sight, and the Lord killed him.",
  'explain': ("No crime named. The Hebrew says YHWH twice; the Greek the Lord, then God; the Latin He."),
  'shared': ["Er, Judah’s firstborn, was wicked.", "It was in the Lord’s sight.", "The Lord put him to death."],
  'instructions': [ins(K, S, "The Lord slew Er for wickedness."), ins(W, R, "Er’s sin is not told, only judged; Scripture does not always explain a death, and Tamar is left a widow by a sentence she had no part in.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew YHWH in both clauses is Greek kyriou … ho theos, “the Lord … God”; Latin “the Lord’s sight, and He killed him”; King James “the LORD slew him.”")]},

 '38:8': {
  'received': "Judah told Onan to go in to his brother’s wife as her brother-in-law and raise up seed for his brother.",
  'explain': ("The levirate duty, yabbem, later law in Deuteronomy 25, already custom. The Greek says perform a brother-in-law’s duty; the Latin be joined to her; the King James marry her."),
  'shared': ["Go in to your brother’s wife.", "Perform the brother-in-law’s duty to her.", "Raise up seed for your brother."],
  'instructions': [ins(C, S, "Go in to your brother’s wife and raise up seed for your brother."), ins(W, R, "The duty is to the dead brother’s name, not to Tamar’s wishes; the custom protects the line and leaves the woman as its instrument, and the chapter watches what she does with that.")],
  'entries': [],
  'lost': [between("Hebrew ve-yabbem otah, “and do the levirate for her,” is Greek kai gambreusai autēn, “and act as brother-in-law to her”; Latin “be joined to her,” King James “marry her.”")]},

 '38:9': {
  'received': "Onan, knowing the seed would not be his, spilled it on the ground whenever he went to her, to give no seed to his brother.",
  'explain': ("Onan takes the wife and refuses the duty; his sin is against his brother’s name and Tamar’s future, not a general rule. The Latin says born in his brother’s name."),
  'shared': ["Onan knew the seed would not be his.", "Whenever he went in to his brother’s wife he spilled it on the ground.", "He would not give seed to his brother."],
  'instructions': [ins(K, S, "Onan refused to raise seed for his brother."), ins(W, R, "Onan wants the inheritance Er’s son would take; he uses Tamar and denies her the child. The sin is greed wearing the shape of duty.")],
  'entries': [],
  'lost': [between("Hebrew le-vilti netan-zera le-achiv, “so as not to give seed to his brother,” is Greek tou mē dounai sperma tō adelphō autou; Latin “so that children would not be born in his brother’s name”; King James “lest that he should give seed to his brother.”")]},

 '38:10': {
  'received': "What he did was wicked in the Lord’s sight, and He killed him too.",
  'explain': ("The second death. The Hebrew says YHWH; the Greek God; the Latin a detestable thing."),
  'shared': ["What he did was wicked in the Lord’s sight.", "He put him to death.", "Onan died also."],
  'instructions': [ins(K, S, "The Lord slew Onan too."), ins(W, R, "Two sons dead and Judah will blame the widow; the father reads the deaths as Tamar’s curse, and the narrator has told us they were his sons’ sins.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew be-ene YHWH, “in YHWH’s eyes,” is Greek enantion tou theou, “before God”; Latin “the Lord struck him down, because he did a detestable thing”; King James “displeased the LORD.”")]},

 '38:11': {
  'received': "Judah told Tamar to live as a widow in her father’s house until Shelah grew up, fearing he too would die; she went.",
  'explain': ("A promise Judah does not mean to keep; the narrator tells us his thought. The versions agree; the Latin for this reason."),
  'shared': ["Remain a widow in your father’s house until my son Shelah grows up.", "He thought, lest he also die like his brothers.", "Tamar went and lived in her father’s house."],
  'instructions': [ins(K, S, "Judah sent Tamar home with a promise of Shelah."), ins(W, R, "Judah sends Tamar away to protect his last son from her; she is made the danger. His fear is a father’s, and his promise is a lie, and she will hold him to it.")],
  'entries': [],
  'lost': [AGREE]},

 '38:12': {
  'received': "After a long time Judah’s wife died; comforted, he went up to his sheep-shearing at Timnah with his friend Hirah.",
  'explain': ("Shearing was a festival. The Hebrew says the daughter of Shua, his friend Hirah; the Greek Shua, his shepherd; the Latin daughter of Shua, shepherd of his flock."),
  'shared': ["After many days Judah’s wife died.", "When Judah was comforted, he went up to his sheep-shearers at Timnah.", "Hirah the Adullamite was with him."],
  'instructions': [ins(K, S, "Widowed Judah went to the shearing at Timnah."), ins(W, R, "Judah is comforted after his wife; Tamar has been a widow for years without comfort. The chapter measures the two griefs against each other without a word.")],
  'entries': [],
  'lost': [loses("Hebrew bat-Shua, “the daughter of Shua,” becomes Greek Saua, the wife named; Hebrew re‘ehu, “his friend,” becomes ho poimēn autou, “his shepherd.”"), between("Latin “the daughter of Shua … Hirah the Adullamite, shepherd of his flock” mixes; King James “the daughter of Shuah … his friend Hirah.”")]},

 '38:13': {
  'received': "Tamar was told her father-in-law was going up to Timnah to shear.",
  'explain': ("Tamar has watched Shelah grow and waited. The Greek adds his daughter-in-law."),
  'shared': ["It was reported to Tamar.", "Your father-in-law is going up to Timnah.", "He goes to shear his sheep."],
  'instructions': [ins(K, S, "Tamar learned of Judah’s journey.")],
  'entries': [],
  'lost': [keeps("An added hē nymphē autou, “his daughter-in-law,” after Tamar in the Greek."), between("Hebrew, Latin and King James “Tamar.”")]},

 '38:14': {
  'received': "She took off her widow’s clothes, veiled and wrapped herself, and sat at the entrance to Enaim on the Timnah road, for Shelah was grown and she had not been given to him.",
  'explain': ("Tamar acts, since Judah will not. Enaim, two springs, or an open place. The Hebrew says wrapped herself, she had not been given; the Greek adorned herself, the gates of Ainan, he had not given her; the Latin a fork in the road."),
  'shared': ["She removed her widow’s garments, covered herself with a veil and wrapped herself.", "She sat at the entrance to Enaim on the road to Timnah.", "Shelah had grown up and she had not been given to him."],
  'instructions': [ins(K, S, "Tamar disguised herself to confront Judah’s neglect."), ins(W, R, "The widow who was told to wait has waited; the veil is her claim on a promise. Tamar’s deception is the only one in Genesis the narrator calls righteous.")],
  'entries': [],
  'lost': [loses("Hebrew va-tit‘allaf, “and wrapped herself,” becomes Greek kai ekallōpisato, “and adorned herself”; Hebrew be-fetach Enayim, “at the opening of Enaim,” becomes pros tais pylais Ainan, “at the gates of Ainan”; Hebrew ve-hi lo-nittenah lo, “and she was not given to him,” becomes kai autos ouk edōken autēn autō, “and he had not given her to him.”"), between("Latin “at a fork in the road leading to Timnah” and King James “in an open place” render Enaim as a description.")]},

 '38:15': {
  'received': "Judah saw her and took her for a prostitute, because she had covered her face.",
  'explain': ("Zonah, a common prostitute. The Greek adds and he did not recognise her; the Latin so that she would not be recognised."),
  'shared': ["Judah saw her.", "He thought she was a prostitute.", "She had covered her face."],
  'instructions': [ins(K, S, "Judah mistook veiled Tamar for a prostitute."), ins(W, R, "He does not recognise her; recognition is the chapter’s word, hakker, from the coat in chapter 37 to the pledge in verse 25. Judah will learn to see.")],
  'entries': [],
  'lost': [keeps("An added kai ouk epegnō autēn, “and he did not recognise her,” in the Greek."), between("Latin “so that she would not be recognised” gives the purpose; King James follows the Hebrew.")]},

 '38:16': {
  'received': "He turned aside to her and asked to come in, not knowing she was his daughter-in-law; she asked what he would give.",
  'explain': ("The bargain; Tamar negotiates. The versions agree; the Latin to enjoy lying with me."),
  'shared': ["He turned aside to her by the road and said, Let me come in to you.", "He did not know she was his daughter-in-law.", "What will you give me if you come in to me?"],
  'instructions': [ins(K, S, "Judah solicited Tamar unknowingly."), ins(W, R, "Judah asks the price as he asked the profit in selling Joseph; the man of bargains is about to pledge his identity for a night.")],
  'entries': [],
  'lost': [AGREE]},

 '38:17': {
  'received': "He offered a kid from the flock; she asked for a pledge until it came.",
  'explain': ("A kid, as the brothers killed a kid for Joseph’s coat. The Latin expands her consent."),
  'shared': ["I will send you a young goat from the flock.", "She said.", "Will you give me a pledge until you send it?"],
  'instructions': [ins(K, S, "Tamar demanded a pledge.")],
  'entries': [],
  'lost': [between("Latin “I will allow what you wish if you give me a pledge” expands; Hebrew, Greek and King James “Wilt thou give me a pledge, till thou send it?”")]},

 '38:18': {
  'received': "She asked his signet, cord and staff; he gave them, went in to her, and she conceived by him.",
  'explain': ("Signet on its cord and staff: a man’s identity, as a sealed signature and a tribal badge. The Hebrew says signet and cord; the Greek ring and necklace; the Latin ring and bracelet, by one act."),
  'shared': ["What pledge shall I give you?", "Your signet, your cord and the staff in your hand.", "He gave them, went in to her, and she conceived by him."],
  'instructions': [ins(K, S, "Judah pledged his seal and staff and Tamar conceived."), ins(W, R, "Judah hands over the things that say who he is; Tamar holds his name in her hand, and the twins she conceives carry it to David.")],
  'entries': [],
  'lost': [loses("Hebrew chotamkha u-fetilekha, “your signet and your cord,” becomes Greek ton daktylion sou kai ton hormiskon, “your ring and your necklace.”"), between("Latin “your ring, your bracelet … by one act of intercourse the woman conceived” varies; King James “thy signet, and thy bracelets, and thy staff.”")]},

 '38:19': {
  'received': "She rose, went away, removed her veil and put on her widow’s clothes.",
  'explain': ("Back to widowhood, with the pledge. The Latin says the dress she had put on."),
  'shared': ["She arose and departed.", "She took off her veil.", "She put on her widow’s garments again."],
  'instructions': [ins(K, S, "Tamar resumed her widow’s dress.")],
  'entries': [],
  'lost': [AGREE]},

 '38:20': {
  'received': "Judah sent the kid by his friend the Adullamite to redeem the pledge, but he could not find her.",
  'explain': ("Judah keeps his word to a prostitute, as he did not to Tamar. The Hebrew says friend; the Greek and Latin shepherd."),
  'shared': ["Judah sent the young goat by the Adullamite.", "He was to recover the pledge from the woman.", "He did not find her."],
  'instructions': [ins(K, S, "The pledge could not be redeemed."), ins(W, R, "Judah pays a stranger promptly and forgets a daughter-in-law for years; honour among men and neglect of a woman sit in the same conscience.")],
  'entries': [],
  'lost': [between("Hebrew re‘ehu, “his friend,” is Greek tou poimenos autou, “his shepherd,” Latin “shepherd,” King James “friend.”")]},

 '38:21': {
  'received': "He asked the men of the place for the prostitute at Enaim; they said there had been none.",
  'explain': ("The Hebrew here says qedeshah, a consecrated woman, a cult prostitute, where verse 15 said zonah; the Greek and King James one word for both; the Latin the woman who sat at the fork."),
  'shared': ["He asked the men of that place.", "Where is the prostitute who was by the road at Enaim?", "There has been no prostitute here."],
  'instructions': [ins(K, S, "No one knew of the woman at Enaim.")],
  'entries': [],
  'lost': [between("Hebrew ha-qedeshah, “the consecrated woman,” is Greek hē pornē, “the prostitute,” as in 38:15; Hebrew ba-Enayim is Greek en Ainan; Latin “the woman who sat at the fork in the road”; King James “the harlot, that was openly by the way side.”")]},

 '38:22': {
  'received': "He reported to Judah: I could not find her, and the men say there was no prostitute there.",
  'explain': ("The versions agree; the Latin had ever sat there."),
  'shared': ["He returned to Judah.", "I did not find her.", "The men of the place said there is no prostitute here."],
  'instructions': [ins(K, S, "Hirah reported failure to Judah.")],
  'entries': [],
  'lost': [AGREE]},

 '38:23': {
  'received': "Judah said, Let her keep them, or we shall be laughed at; I sent the kid and you did not find her.",
  'explain': ("Judah drops it, for fear of ridicule, not of wrong. The Latin says she cannot accuse us of lying."),
  'shared': ["Let her keep them.", "Lest we become a laughingstock.", "I sent this kid and you did not find her."],
  'instructions': [ins(K, S, "Judah abandoned the pledge to avoid shame."), ins(W, R, "“Lest we be shamed”: Judah fears the town’s laughter more than the loss of his seal. The shame he dodges here will find him in public in verse 26.")],
  'entries': [],
  'lost': [between("Hebrew pen nihyeh la-vuz, “lest we become a contempt,” is Greek mēpote katagelasthōmen, “lest we be laughed at”; Latin “Certainly she cannot accuse us of lying”; King James “lest we be shamed.”")]},

 '38:24': {
  'received': "Three months later Judah was told Tamar had played the harlot and was pregnant; he said, Bring her out and burn her.",
  'explain': ("Burning, a penalty harsher than the later law; Judah speaks as head of the clan. The Latin says her womb appears to be swelling."),
  'shared': ["After three months it was reported to Judah.", "Tamar your daughter-in-law has played the prostitute and is pregnant by it.", "Bring her out and let her be burned."],
  'instructions': [ins(K, S, "Judah condemned Tamar to burning."), ins(W, R, "Judah sentences for the sin he committed with her; the judge is the partner, and does not know it yet. The verdict is swift because the woman is nothing to him.")],
  'entries': [],
  'lost': [between("Latin “her womb appears to be swelling” for Hebrew hinneh harah li-znunim, “behold, she is pregnant by harlotry”; Greek and King James follow the Hebrew.")]},

 '38:25': {
  'received': "As she was brought out she sent word to Judah: I am pregnant by the owner of these; recognise whose signet, cord and staff they are.",
  'explain': ("Tamar does not accuse; she asks him to recognise, as the brothers asked Jacob of the coat. The Hebrew says please recognise, signet, cords; the Greek ring, necklace; the Latin led to punishment."),
  'shared': ["As she was being brought out she sent word to her father-in-law.", "I am pregnant by the man to whom these belong.", "Recognise whose signet, cord and staff these are."],
  'instructions': [ins(K, S, "Tamar produced Judah’s pledge."), ins(W, R, "“Recognise whose these are”: the same word the brothers used of the coat. Judah who helped deceive his father with a garment is undeceived by his own seal.")],
  'entries': [],
  'lost': [between("Hebrew hakker-na, “please recognise,” ha-chotemet ve-ha-petilim, “the signet and the cords,” is Greek epignōthi … ho daktylios kai ho hormiskos, “the ring and the necklace”; Latin “ring, bracelet, and staff”; King James “the signet, and bracelets, and staff.”")]},

 '38:26': {
  'received': "Judah recognised them: She is more in the right than I, since I did not give her to Shelah. He did not know her again.",
  'explain': ("Tzadeqah mimmenni, she is righteous rather than I. Judah confesses in public and does not touch her again. The Greek names Tamar; the Latin yet."),
  'shared': ["Judah recognised them.", "She is more in the right than I, because I did not give her to Shelah my son.", "He did not know her again."],
  'instructions': [ins(K, S, "Judah admitted Tamar’s righteousness and his fault."), ins(W, R, "“She is more righteous than I” is the first confession in Genesis made by the guilty against himself in public; the Judah who will offer himself for Benjamin is born here, by a veiled woman’s pledge.")],
  'entries': [],
  'lost': [keeps("An added Thamar as subject in the Greek: “Tamar is more in the right.”"), between("Hebrew, Latin and King James “she”; Latin “Yet he did not know her again.”")]},

 '38:27': {
  'received': "At her delivery there were twins in her womb.",
  'explain': ("Twins, as for Rebekah; another struggle for precedence. The Latin runs on into the hand and thread."),
  'shared': ["It was the time of her delivery.", "Behold.", "Twins were in her womb."],
  'instructions': [ins(K, S, "Tamar bore twins.")],
  'entries': [],
  'lost': [between("Latin carries “one put out a hand, and the midwife tied a scarlet thread” from 38:28 into this verse; Hebrew, Greek and King James end at the twins.")]},

 '38:28': {
  'received': "One put out a hand; the midwife tied a scarlet thread on it, saying, This one came out first.",
  'explain': ("The scarlet thread, a mark of the firstborn. The Hebrew says this one came out first; the Greek will come out first; the Latin has only the saying here."),
  'shared': ["As she gave birth, one put out a hand.", "The midwife tied a scarlet thread on it.", "This one came out first."],
  'instructions': [ins(K, S, "The midwife marked the first hand with scarlet.")],
  'entries': [],
  'lost': [between("Hebrew zeh yatza rishonah, “this one came out first,” past, is Greek houtos exeleusetai proteros, “this one will come out first,” future; Latin has only the saying, the rest moved to 38:27; King James “This came out first.”")]},

 '38:29': {
  'received': "But he drew back his hand and his brother came out; she said, What a breach you have made! He was named Perez.",
  'explain': ("Perez, breach, the ancestor of David in Ruth 4:18. The younger comes first again. The Hebrew says what a breach you have made for yourself; the Greek why has a barrier been broken because of you, immediately; the Latin she named him."),
  'shared': ["As he drew back his hand, his brother came out.", "She said, What a breach you have made!", "He was named Perez."],
  'instructions': [ins(K, S, "Perez broke out first and was named for it."), ins(W, R, "The breach-maker is David’s ancestor; the royal line of Judah comes through a Canaanite marriage, a widow’s ruse, and a twin who pushed past his brother. Ruth 4 and Matthew 1 both write it down.")],
  'entries': [],
  'lost': [between("Hebrew mah-paratzta alekha paretz, “how you have breached for yourself a breach,” is Greek ti diekopē dia se phragmos, “why has a barrier been cut through because of you”; the Greek adds eutheōs, “immediately”; Latin “she named him Perez,” King James “How hast thou broken forth? this breach be upon thee.”")]},

 '38:30': {
  'received': "Then his brother came out with the scarlet thread on his hand; he was named Zerah.",
  'explain': ("Zerah, shining, perhaps for the scarlet. The versions agree; the Latin she called him."),
  'shared': ["Afterward his brother came out.", "The scarlet thread was on his hand.", "He was named Zerah."],
  'instructions': [ins(K, S, "Zerah was born second despite the scarlet thread."), ins(W, R, "The thread said first and the birth said second; as with Esau and Jacob, the marks of precedence are overruled, and Judah’s house begins with the oracle of 25:23 told again in miniature.")],
  'entries': [],
  'lost': [AGREE]},
 }
}
