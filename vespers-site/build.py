# -*- coding: utf-8 -*-
"""
Vespers — static-site generator for vesperstonight.com.

A late-night webcast for the great ideas: the Syntopicon, Scripture studies,
and public-domain great books, with a little jazz between the segments.
"Small music, big talk" — the nocturne counterpart to UncleTheology Radio.

    python3 build.py           → writes public/

Structure mirrors the UncleTheology generator so episodes/a listen page can be
grown in later. For now it renders the landing + about.
"""

import html
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
SRC_ASSETS = os.path.join(HERE, "assets")

SITE_NAME = "Vespers"
SITE_URL = "https://vesperstonight.com"
TAGLINE = "Welcome to Vespers, where we take up the last hour of your day."
OG_IMAGE = SITE_URL + "/assets/cover.jpg"

DISCLAIMER = ("A survey of the great ideas — not necessarily an endorsement of any one "
              "contribution.")

# Episodes, newest first.
EPISODES = [
    {
        "slug": "the-severed-head",
        "idea": "The Severed Head",
        "lane": "The Surprise",
        "day": "Thursday",
        "date_display": "August 27, 2026",
        "sub": "The Surprise · headship, hierarchy, and the body — walking around Lewis’s That Hideous Strength",
        "duration": "50 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/the-severed-head.mp3",
        "length": 72730066,
        "lede": "Hierarchy is a word our age says through clenched teeth. Tonight we take it out of "
                "quarantine — what the catechisms meant by superiors, inferiors, and equals; what the "
                "apostles meant by the head and the body; and what happens in a college, a country, or a "
                "marriage when the head abdicates and a usurper takes its place. The map is Lewis’s "
                "That Hideous Strength.",
        "body": [
            "A long walk around the last of C. S. Lewis’s science-fiction trilogy — a book that "
            "is, under all its machinery, about headship: the head and the body, what a head owes, and "
            "what happens when the head is severed. Lewis is within living memory, so the evening walks "
            "around his pages rather than through them and lets the older voices read. It begins with the "
            "boy who learned about headship the hard way — a father’s failure of attention after "
            "a mother’s death — and moves out to the grammar of order itself: the Westminster "
            "Larger Catechism on superiors, inferiors, and equals; Absalom at the gate, stealing the "
            "hearts of Israel; and the one body of 1 Corinthians 12, where the members cannot say to one "
            "another, I have no need of thee.",
            "Then the head that is worth having — the head of Ephesians and Colossians “from which "
            "all the body… increaseth,” and the head of Mark 10 and Philippians 2 who came not to "
            "be ministered unto but to minister, who descended before he was exalted. Edwards on the "
            "excellency of Christ, the admirable conjunction of lion and lamb, infinite highness and "
            "infinite condescension. The severed head is the abdicated or the usurped one; the true head "
            "bows lowest. Closing with Matthew Bridges’ “Crown Him with Many Crowns,” read whole.",
        ],
        "walk": [
            ("Exodus 20:12 · Westminster Larger Catechism", "Scripture · KJV · 1647",
             "“Honour thy father and thy mother” read as the catechism reads it — the duties "
             "of superiors, inferiors, and equals; the grammar of order our age has forgotten."),
            ("2 Samuel 15 · Absalom at the gate", "Scripture · KJV",
             "The usurper who “stole the hearts of the men of Israel” — headship seized by "
             "flattery, the counterfeit of a head that serves."),
            ("1 Corinthians 12 · the body", "Scripture · KJV",
             "Many members, one body — “the eye cannot say unto the hand, I have no need of "
             "thee”; the honour spent on the parts that lack it."),
            ("Ephesians 4–5 · Colossians 2", "Scripture · KJV",
             "The head “from which all the body by joints and bands… increaseth with the increase "
             "of God” — headship as nourishment, not domination."),
            ("Mark 10:42–45 · Philippians 2", "Scripture · KJV",
             "“Whosoever will be chief… shall be servant of all” — the head who descends "
             "before he is exalted; the mind of Christ."),
            ("Jonathan Edwards · The Excellency of Christ", "public domain",
             "The admirable conjunction of lion and lamb — infinite highness and infinite condescension "
             "meeting in one person."),
            ("The commonplace stones · Equality & Subordination", "Collacon · public domain",
             "Old handbook sayings on equality, subordination, and authority — read as bare "
             "attributions, the tradition’s cross-talk on rank."),
            ("C. S. Lewis · That Hideous Strength", "1945 · paraphrased",
             "Walked around, not read — the abolition of hierarchy that abolishes the man; why nobody "
             "is looking after anybody once the head is gone."),
            ("Matthew Bridges · “Crown Him with Many Crowns”", "1851",
             "The close, read whole — the many crowns of the head who was first crowned with thorns."),
        ],
    },
    {
        "slug": "the-compass-and-the-cross",
        "idea": "The Compass and the Cross",
        "lane": "The Surprise",
        "day": "Thursday",
        "date_display": "August 20, 2026",
        "sub": "The Surprise · 2 Timothy — why ease is no proof of the right road",
        "duration": "30 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/the-compass-and-the-cross.mp3",
        "length": 42997597,
        "lede": "There is an instrument most of us carry without knowing it — a compass that reads "
                "comfort as true north and discomfort as a wrong turn. Tonight’s readings gather around "
                "a letter from a Roman prison, in which an old man tells the son he loves not “stay "
                "safe” but “come share this suffering with me” — and the whole tradition "
                "circles that sentence.",
        "body": [
            "A meditation on comfort as a false compass — the needle that swings toward ease and calls "
            "it the right road — set against the logic of Paul’s last letter. From a Roman prison, "
            "awaiting execution, the apostle writes to Timothy not “I love you, therefore stay safe,” "
            "but “I love you, therefore come share this suffering.” The moralists and philosophers "
            "circle it: Seneca on the good man whom God tests as a father tests a son; Epictetus on "
            "struggling with circumstances and the labours of Hercules; Bunyan’s Hill Difficulty, and "
            "Timorous and Mistrust running back down it at the sight of the lions.",
            "Then the Scriptures make the paradox a doctrine: “faithful are the wounds of a friend”; "
            "the chastening of Hebrews 12 as the mark of sonship, not abandonment; the Psalmist’s “it "
            "is good for me that I have been afflicted.” Pink on the faithfulness and the love of God; "
            "Spurgeon’s “Song of the Steadfast.” And the road ends where the letter ends — "
            "“I have fought a good fight… henceforth there is laid up for me a crown” — "
            "closing with Cowper’s “’Tis my happiness below not to live without the cross.”",
        ],
        "walk": [
            ("2 Timothy 1", "Scripture · KJV",
             "The letter itself — “God hath not given us the spirit of fear”; “be thou "
             "partaker of the afflictions of the gospel.” Love that calls into hard country, not away "
             "from it."),
            ("The false compass", "host framing",
             "The instrument between heart and conscience that reads comfort as true north — nearly "
             "always trusted, and the whole evening stands against it."),
            ("Seneca · Of Providence", "Stewart translation · PD",
             "Why good men suffer — God “disciplines those whom he approves, whom he loves”; "
             "the father who tests the son."),
            ("Epictetus · Discourses I", "Long translation · PD",
             "How we should struggle with circumstances — and the labours of Hercules, who was not "
             "made great by ease."),
            ("Bunyan · The Pilgrim’s Progress", "public domain",
             "The Hill Difficulty, and Timorous and Mistrust turning back at the lions — comfort as a "
             "compass, dramatised."),
            ("Proverbs 27:6 · Hebrews 12 · Psalm 119", "Scripture · KJV",
             "“Faithful are the wounds of a friend”; chastening as the mark of sonship; “it is "
             "good for me that I have been afflicted.”"),
            ("A. W. Pink · The Attributes of God", "1930",
             "The faithfulness and the love of God — a love that wills our good over our ease."),
            ("Spurgeon · Treasury of David", "public domain",
             "The Song of the Steadfast — read against the counsel to flee; “corn is cleaned with "
             "wind.”"),
            ("2 Timothy 4 · the crown", "Scripture · KJV",
             "“I have fought a good fight, I have finished my course” — the crown at the end of "
             "the hard road."),
            ("William Cowper · hymn", "as printed by Spurgeon · PD",
             "“’Tis my happiness below not to live without the cross” — the closing stanzas."),
        ],
    },
    {
        "slug": "beauty",
        "idea": "Beauty",
        "lane": "Great Ideas",
        "day": "Tuesday",
        "date_display": "August 18, 2026",
        "sub": "Great Ideas · No. 6 — what beauty is, where it lives, what it is for, and what it costs",
        "duration": "30 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/beauty.mp3",
        "length": 42945676,
        "lede": "The sixth great idea. Beauty enters Scripture as a commandment — priestly garments "
                "“for glory and for beauty” — and the tradition circles it all night: Plato’s "
                "ladder, Aristotle’s magnitude and order, Augustine’s “Too late loved I Thee,” "
                "Aquinas’s wholeness, proportion, and radiance, down to Isaiah’s two hardest sayings "
                "and a schoolmaster’s hymn on a hill above Bath.",
        "body": [
            "A survey of the sixth of the hundred and two great ideas, read through the canon it indexes. "
            "Beauty enters the story early and as a command — “holy garments… for glory and for "
            "beauty” — and the Psalms turn the word toward God himself: the one thing David desired, "
            "to behold the beauty of the LORD. Among the Greeks the great account is Diotima’s ladder in "
            "the Symposium, climbing from a fair body to beauty absolute; Aristotle answers with the "
            "measuring rod — “beauty depends on magnitude and order.” Augustine picks the ladder "
            "and climbs it weeping. Aquinas gives the medieval definition in a single breath: integrity, "
            "proportion, brightness — wholeness, proportion, radiance — each with its likeness in the Son.",
            "Then the commonplace books and the Puritans, wary and unwearied: Quarles’s warning, "
            "Bacon’s “no excellent beauty that hath not some strangeness in the proportion,” "
            "Watson’s “well-coloured dirt” set against “grace is our best beauty,” "
            "Emerson’s kosmos, Spurgeon slowing over David’s one desire. And Isaiah, who holds the "
            "two hardest sayings together — “no beauty that we should desire him,” and “thine "
            "eyes shall see the king in his beauty” — and lets them interpret one another: the beauty "
            "was there all along; the failure was in the eyes. Closing with Folliott Pierpoint’s “For "
            "the Beauty of the Earth,” in its original wording.",
        ],
        "walk": [
            ("Exodus 28 · the Psalms · Ecclesiastes 3:11", "Scripture · KJV",
             "Beauty enters as a commandment — priestly garments “for glory and for beauty” — "
             "and David’s one desire, to behold the beauty of the LORD; the Preacher’s “every "
             "thing beautiful in his time.”"),
            ("Plato · Symposium — Diotima’s ladder", "Jowett translation",
             "Love of a beautiful body is only the first rung; the climb ends in “beauty absolute, "
             "separate, simple, and everlasting.”"),
            ("Aristotle · Poetics", "Butcher translation",
             "The measuring rod against the ladder — “beauty depends on magnitude and order”; a "
             "thing big enough to see and small enough to hold."),
            ("Augustine · Confessions X", "Pusey translation",
             "“Too late loved I Thee, O Thou Beauty of ancient days, yet ever new” — the ladder "
             "become a person, the climb become a rescue."),
            ("Aquinas · Summa Theologica I, Q39", "Dominican Fathers translation",
             "Beauty’s three conditions — integrity, proportion, clarity; wholeness, proportion, "
             "radiance, each with its likeness in the Son."),
            ("The commonplace stones", "Collacon · public domain",
             "Clarendon, Cervantes, Quarles’s warning, Milton’s tempter — and the answers: "
             "Porter, Upham, Greville’s test, “true beauty increases on examination.”"),
            ("Francis Bacon · Of Beauty", "Essays",
             "“There is no excellent beauty, that hath not some strangeness in the proportion” — "
             "and beauty as summer fruit, easy to corrupt."),
            ("Thomas Watson · Body of Divinity", "public domain",
             "From beauty to a Maker — the painting implies an artist — and from “well-coloured "
             "dirt” to “grace is our best beauty.”"),
            ("Emerson · Nature, ch. III", "1836",
             "The Greeks called the world kosmos, beauty; nature medicinal to the cramped eye; “beauty is "
             "the mark God sets upon virtue.”"),
            ("Spurgeon on Psalm 27 · Isaiah 53 & 33:17", "public domain · KJV",
             "“The King in his beauty” — Isaiah’s two hardest sayings held together: no "
             "beauty we should desire him, and eyes that shall see the King in his beauty."),
            ("Folliott Pierpoint · “For the Beauty of the Earth”", "1864",
             "Written on a hill above Bath — a hymn of thanksgiving for beauty itself, in its original "
             "wording."),
        ],
    },
    {
        "slug": "the-earthy-piety-of-providence",
        "idea": "The Earthy Piety of Providence",
        "lane": "The Scriptures",
        "day": "Friday",
        "date_display": "August 7, 2026",
        "sub": "The Scriptures · Ecclesiastes 9 — work, wine, wife, and worship",
        "duration": "39 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/the-earthy-piety-of-providence.mp3",
        "length": 56664270,
        "lede": "The earthy piety of providence — Ecclesiastes read as a laboratory notebook. The "
                "four things fitting for a man under the sun — work, wine, wife, and worship — the "
                "maze that is “not without a plan,” and the one verdict the Preacher hands over "
                "without its ground: “for God now accepteth thy works.”",
        "body": [
            "Ecclesiastes taken as the record of an experiment — “time and chance happeneth to them "
            "all,” a film of vanity lying over the whole world like dust. The Preacher's answer to "
            "the uncertainty is not to solve it but to tend what is yours: the four categories that "
            "run through the book — work, wine, wife, and worship — lived out in front of God's "
            "face. Alexander Pope's “mighty maze, but not without a plan” concedes the maze; "
            "Augustine's ordered love answers it — “pay special regard to those who, by the "
            "accidents of time, or place, or circumstance, are brought into closer connection with "
            "you.”",
            "Against that stands the busybody — the self-appointed bishop of other men's business "
            "Peter files beside felons, and the metaphysical version who tries to run heaven's "
            "books from a folding chair. The cure is Eden's own programming, which the fall made "
            "harder but did not revoke: dress it and keep it, do your work, love your companion, "
            "eat your bread with joy. Earthy, not earthly — a faith you can get under your "
            "fingernails — and providence as the Westminster divines define it, governing all "
            "creatures and all their actions. The ground the Preacher lacked, Ephesians supplies: "
            "“he hath made us accepted in the beloved.” Closing with John Keble's “Morning.”",
        ],
        "walk": [
            ("Ecclesiastes 9", "Scripture · KJV",
             "“The race is not to the swift… but time and chance happeneth to them all” — the "
             "Preacher's notebook, and his four categories: work, wine, wife, and worship."),
            ("Ecclesiastes 9:7–10", "Scripture · KJV",
             "“Go thy way, eat thy bread with joy… for God now accepteth thy works” — the verdict "
             "handed over without its ground."),
            ("Alexander Pope · An Essay on Man", "1733",
             "“A mighty maze! but not without a plan” — the Christian position in six words; it "
             "concedes the maze."),
            ("Augustine on ordered love", "On Christian Doctrine · Confessions",
             "The shape of our concern — “pay special regard to those who, by the accidents of "
             "time, or place, or circumstance, are brought into closer connection with you.”"),
            ("The busybody · 1 & 2 Thessalonians · 1 Peter · Proverbs 26", "Scripture · KJV",
             "“Study to be quiet, and to do your own business” — and the overseer of what belongs "
             "to another, filed in a lineup with felons."),
            ("Thomas Fuller · Marcus Aurelius", "public domain",
             "“Curiosity is a kernel of the forbidden fruit”; and the cure — “work at that which "
             "is before thee… without allowing anything else to distract thee.”"),
            ("Genesis 2–3 · the garden and the curse", "Scripture · KJV",
             "Dress it and keep it — the programming the fall made harder but did not revoke. Do "
             "Eden anyway."),
            ("Earthy, not earthly · James 3 · Colossians 3", "Scripture · KJV",
             "Not the world set up as a rival to God, but Adam from the adamah — a dirt creature "
             "God called very good; a faith you can get under your fingernails."),
            ("Providence · Westminster · Proverbs 16 · South · Flavel", "public domain",
             "“The lot is cast into the lap; but the whole disposing thereof is of the LORD” — “he "
             "that will watch providence shall never want a providence to watch.”"),
            ("Ephesians 2 · John Keble · “Morning”", "Scripture · KJV · 1827",
             "“By grace are ye saved… we are his workmanship” — “the trivial round, the common "
             "task, would furnish all we ought to ask.”"),
        ],
    },
    {
        "slug": "when-god-gives-us-what-we-demand",
        "idea": "When God Gives Us What We Demand",
        "lane": "The Surprise",
        "day": "Thursday",
        "date_display": "August 6, 2026",
        "sub": "The Surprise · Israel's demand for a king, and the discipline of answered prayer",
        "duration": "38 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/when-god-gives-us-what-we-demand.mp3",
        "length": 55901180,
        "lede": "The moment an entire nation looked at what God had given and asked for something "
                "else — Israel's demand for a king — and the terrifying mercy of a God who "
                "sometimes says yes: “he gave them their request; but sent leanness into their soul.”",
        "body": [
            "First Samuel read at length: the elders at Ramah — “make us a king… like all the "
            "nations” — the demand God hears as a rejection of himself, the warning of the king who "
            "will take and take, and the thunder Samuel calls down in the dry of wheat harvest. "
            "Psalm 106 names the pattern, Hosea writes the epitaph — “I gave thee a king in mine "
            "anger” — and Matthew Henry the hard phrase: God “gratifies us in wrath.”",
            "Then the old moralists on pride, covetousness, ambition and contentment; A. W. Pink on "
            "the sovereignty, patience and love of God, with Spurgeon's “men will allow God to be "
            "everywhere except on his throne”; and Habakkuk's man who has nothing and rejoices "
            "still — content, “the jewel which no Indian mines can buy.” Closing with Cowper's "
            "“God Moves in a Mysterious Way.”",
        ],
        "walk": [
            ("1 Samuel 8", "Scripture · KJV",
             "“Make us a king… like all the nations” — the demand Samuel hears as a rejection of "
             "God, and the warning of the king who will take."),
            ("1 Samuel 12", "Scripture · KJV",
             "Samuel's farewell, and the thunder in wheat harvest: “ye have added unto all our sins "
             "this evil, to ask us a king.”"),
            ("Psalm 106 · Hosea 13", "Scripture · KJV",
             "“He gave them their request; but sent leanness into their soul”; “I gave thee a king "
             "in mine anger, and took him away in my wrath.”"),
            ("Matthew Henry · on 1 Samuel", "1710",
             "“God sometimes opposes us from loving-kindness; so at other times he gratifies us in "
             "wrath.”"),
            ("The moralists on pride & discontent", "South · Jeremy Taylor · Fielding · Tillotson",
             "“Discontent… to be something they are not, and have something they have not, is the "
             "root of all immorality.”"),
            ("The moralists on ambition", "Bacon · Machiavelli · Landor",
             "“However high we reach we are never satisfied” — the demand for freedom that ends, in "
             "Plato's Republic, in the tyrant."),
            ("A. W. Pink · The Attributes of God", "1930 · public domain",
             "The sovereignty of God, patience that “bears with the sin,” and a love that “will not "
             "wink at sin, even in his own people.”"),
            ("Spurgeon · on the sovereignty of God", "quoted in Pink",
             "“Men will allow God to be everywhere except on his throne” — First Samuel in one "
             "sentence."),
            ("Habakkuk 3 · the moralists on contentment", "Scripture · KJV · Sterne · Fuller · Spencer",
             "“Although the fig tree shall not blossom… yet I will rejoice in the Lord” — content, "
             "the jewel no mine can buy."),
            ("William Cowper · “God Moves in a Mysterious Way”", "1773 · read whole",
             "“Behind a frowning providence he hides a smiling face.”"),
        ],
    },
    {
        "slug": "four-hundred-to-one",
        "idea": "Four Hundred to One",
        "lane": "Pastor Politics",
        "day": "Wednesday",
        "date_display": "August 5, 2026",
        "sub": "Pastor Politics · Micaiah before Ahab — the lone honest voice in a room of paid agreement",
        "duration": "34 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/four-hundred-to-one.mp3",
        "length": 49054278,
        "lede": "The lone honest voice in a room of paid agreement — Micaiah before Ahab, four "
                "hundred prophets speaking with one mouth — and the court prophet as every pastor's "
                "standing temptation: what truth costs, and what a man becomes when he decides it "
                "costs too much.",
        "body": [
            "The third of the Pastor Politics questions, after the mandate to speak and the manner "
            "of the speech: the cost. The account is old and told at length, so we hear it at "
            "length — Ahab's four hundred with their iron horns, Jehoshaphat asking whether there "
            "is yet a prophet, and Micaiah handing back the house answer until the king himself "
            "cannot bear to hear it. Amos told to “eat bread” elsewhere; Jeremiah on the prophets "
            "who “steal my words every one from his neighbour.”",
            "Then the psalms that put the court on trial — the mortal “gods” of the eighty-second, "
            "the kings warned in the second — with Spurgeon on the clerical sycophant “fit to be a "
            "scullion in the devil's kitchen”; the old moralists on flattery, the majority, and "
            "courage; Watson's dial and sun; and Milton's Abdiel, “among the faithless faithful "
            "only he.” Closing with Lowell's “The Present Crisis.”",
        ],
        "walk": [
            ("1 Kings 22 · Micaiah before Ahab", "Scripture · KJV · read at length",
             "Four hundred prophets with one mouth, and the one man the king hates “for he doth not "
             "prophesy good concerning me, but evil.”"),
            ("Amos 7 · Jeremiah 23", "Scripture · KJV",
             "“Go, flee… and there eat bread”; the prophets “that steal my words every one from his "
             "neighbour” — the copyist, not the inventor."),
            ("Psalm 82 · Psalm 2", "Scripture · KJV",
             "The court itself put on trial — “ye shall die like men”; and the psalm the church "
             "prayed at power: “Be wise now therefore, O ye kings.”"),
            ("Spurgeon · Treasury of David, Psalm 2", "1869–85 · w/ Trapp, Adams, Henry",
             "“A clerical sycophant is only fit to be a scullion in the devil's kitchen” — bold "
             "rebukes even in the royal presence."),
            ("The moralists on flattery", "Raleigh · Penn · Chesterfield · Sidney · Johnson",
             "“Flatterers are the worst kind of traitors” — and why the flattery works even on "
             "those clear-eyed enough to see through it."),
            ("On the majority", "Beecher · Bovee · Horace Mann",
             "Four sentences that will not agree — “it is better to be wrong with the majority than "
             "right with the minority.”"),
            ("On courage & conscience", "Colton · Chapin · Gerson · Philip Henry",
             "Moral courage “which despises all opinion” — kept from curdling by the guard rail of "
             "meekness."),
            ("Thomas Watson · Milton's Abdiel", "public domain",
             "“The heart and tongue should go together, as the dial goes exactly with the sun”; "
             "“among the faithless faithful only he.”"),
            ("James Russell Lowell · “The Present Crisis”", "1845 · read at length",
             "“Truth forever on the scaffold, Wrong forever on the throne” — the brave man who "
             "chooses while the coward stands aside."),
        ],
    },
    {
        "slug": "art",
        "idea": "Art",
        "lane": "Great Ideas",
        "day": "Tuesday",
        "date_display": "August 4, 2026",
        "sub": "Great Idea №4 · the knowing hand",
        "duration": "37 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/art.mp3",
        "length": 53170083,
        "lede": "Not the museum's word but the old one — art as skill, the knowing hand — walked "
                "through the great voices: Scripture's craftsmen filled with the Spirit for gold "
                "and brass, Plato's suspicion and Aristotle's answer, Augustine's cunning hands, "
                "and Dante's art that is “God's grandchild.”",
        "body": [
            "The fourth of Adler's great ideas, taken in the old width — art means making, the art "
            "of the shipwright and the poet and the man who can shoe a horse. Scripture puts the "
            "arts early and in an unexpected line: Cain's sons with the tent, the harp and the "
            "forge; then Bezaleel, the first man of whom it is said that God filled him with his "
            "Spirit — and the filling is for craftsmanship. The second commandment stands as "
            "counterweight, and Isaiah's carpenter shows the power turned the wrong way.",
            "Then the philosophers: Plato's three beds, the artist “thrice removed from the truth”; "
            "Aristotle taking the same fact and finding a root, not a defect; Augustine's honest "
            "paragraph on the beauty that passes through a man's hands; Aquinas' “right reason "
            "about things to be made”; Dante's art that is God's grandchild; Browne's “Nature is "
            "the Art of God”; and Reynolds and Ruskin on the training of the hand. Closing on "
            "Keats's “Ode on a Grecian Urn.”",
        ],
        "walk": [
            ("Genesis 4 · Exodus 31, 35, 36", "Scripture · KJV",
             "The arts begin in Cain's line — tent, harp, forge — and the first man “filled with "
             "the spirit of God” is filled for craftsmanship: Bezaleel."),
            ("Exodus 20 · Isaiah 44", "Scripture · KJV",
             "The second commandment as counterweight — and the carpenter who warms his supper with "
             "half the log and asks the other half to save him."),
            ("Plato · Republic X", "c. 375 BC · trans. Jowett",
             "The three beds — God's, the carpenter's, the painter's — the imitator “thrice removed "
             "from the truth.” The oldest serious charge against art."),
            ("Aristotle · Poetics IV", "c. 335 BC · trans. Butcher",
             "The same fact, the opposite verdict: “the instinct of imitation is implanted in man” "
             "— “Ah, that is he,” the sound of a mind learning."),
            ("Augustine · Confessions X", "c. 397 · trans. Pusey",
             "“Those beautiful patterns which through men's souls are conveyed into their cunning "
             "hands, come from that Beauty which is above our souls.”"),
            ("Aquinas · Summa Theologica I-II, Q57", "c. 1270 · Dominican trans.",
             "“Art is nothing else but the right reason about certain works to be made” — it makes "
             "a good workman, not a good man."),
            ("Dante · Inferno XI", "c. 1320 · trans. Longfellow",
             "“Your art is, as it were, God's grandchild” — the same distance Plato counts as a "
             "fall, Dante counts as a lineage."),
            ("Sir Thomas Browne · Religio Medici", "1643",
             "“All things are artificial; for Nature is the Art of God” — the made maker, doing on "
             "his small scale what was done to him."),
            ("Reynolds · Discourses · Ruskin · “The Nature of Gothic”", "1770s · 1853",
             "“He corrects nature by herself”; and “you must either make a tool of the creature, or "
             "a man of him. You cannot make both.”"),
            ("John Keats · “Ode on a Grecian Urn”", "1819 · read whole",
             "The made thing that outlives the maker — “Beauty is truth, truth beauty,” that is all "
             "ye know on earth, and all ye need to know."),
        ],
    },
    {
        "slug": "ecclesiastes-12",
        "idea": "Remember Now Thy Creator",
        "lane": "The Scriptures",
        "day": "Monday",
        "date_display": "August 3, 2026",
        "sub": "The Scriptures · Ecclesiastes 12 — the text behind the sermon",
        "duration": "38 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/ecclesiastes-12.mp3",
        "length": 54186996,
        "lede": "The last chapter of Ecclesiastes — remember now thy Creator in the days of thy "
                "youth — read whole and walked through the old expositors: the allegory of failing "
                "age, the keepers of the house and the almond tree and the silver cord, and the two "
                "returns the Preacher sets side by side and does not explain.",
        "body": [
            "The text behind the sermon that closes the book and the series, read straight and "
            "then opened by the whole shelf of commentators — Barnes, Jamieson-Fausset-Brown, "
            "Poole, Gill and Matthew Henry — on the one command the Preacher leaves for the young: "
            "remember thy Creator now, before the evil days come, while there is strength to serve "
            "him with more than the dregs of a life.",
            "Then the great riddle-picture of old age — the keepers of the house that tremble, the "
            "strong men that bow, the almond tree in blossom, the grasshopper a burden — read "
            "through the Cambridge and Pulpit commentaries and Keil-Delitzsch; the moralists on age "
            "and youth from Day's old encyclopædia; Longfellow's “Morituri Salutamus”; and the "
            "Preacher's own conclusion, fear God and keep his commandments. Closing with Isaac "
            "Watts's paraphrase of the ninetieth Psalm.",
        ],
        "walk": [
            ("Ecclesiastes 11:7 – 12", "Scripture · KJV · read whole",
             "“Remember now thy Creator in the days of thy youth, while the evil days come not” — "
             "the last chapter of the book, read entire."),
            ("Barnes · JFB · Poole · Gill · Henry", "on “Remember now thy Creator”",
             "“Remember that thou art not thine own, but God's property” — the best of thy days "
             "owed to him, not the dregs of them."),
            ("Cambridge & Pulpit · the allegory of age", "the keepers of the house; the almond tree",
             "The trembling legs, the failing arms, the fear of that which is high — and the "
             "“early-waking tree,” the insomnia of the old."),
            ("The silver cord & the golden bowl", "Cambridge · Pulpit · Benson · Keil-Delitzsch",
             "The lamp of life hung by a chain, and death the snapping of it — the dust returning "
             "to the earth, and the spirit to God who gave it."),
            ("The moralists on age & youth", "Tholuck · Bulwer · Owen · Young · Richter · de Gasparin",
             "“Woe to the man who becomes old without becoming wise” — the old man walking beside a "
             "narrowing river, wife and son on the far bank with arms outstretched."),
            ("Longfellow · “Morituri Salutamus”", "1875 · read at length",
             "The gladiators' salute, written for a fiftieth class reunion: “age is opportunity no "
             "less than youth itself… as the evening twilight fades away the sky is filled with "
             "stars.”"),
            ("The goads and the nails", "Cambridge · Matthew Henry",
             "“The words of the wise are as goads, and as nails fastened” — given from one "
             "Shepherd; the sting that is for good and not for evil."),
            ("“The conclusion of the whole matter”", "Pulpit · Cambridge · Gill · Henry",
             "“Fear God, and keep his commandments: for this is the whole duty of man” — literally, "
             "in the Hebrew, “this is every man.”"),
            ("Isaac Watts · Psalm 90 paraphrase", "1719 · read whole",
             "“Our God, our help in ages past, our hope for years to come” — all nine stanzas; man "
             "frail, and God eternal."),
        ],
    },
    {
        "slug": "the-bishop-and-the-candlesticks",
        "idea": "The Bishop and the Candlesticks",
        "lane": "Fiction's Most Famous Passages",
        "day": "Friday",
        "date_display": "July 31, 2026",
        "sub": "Fiction's Most Famous Passages · Hugo's Les Misérables — the mercy that arrives before repentance",
        "duration": "38 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/the-bishop-and-the-candlesticks.mp3",
        "length": 55104922,
        "lede": "The most famous act of mercy in the European novel — Bishop Bienvenu and the stolen "
                "silver — read whole from Hugo, then followed into its hard corners: grace that "
                "arrives before repentance, a bishop who lies to the police, and the candlesticks "
                "that burn in a thief's hands for the rest of his life.",
        "body": [
            "Fiction's Most Famous Passages turns to Victor Hugo. First the provenance — Besançon, "
            "the exile on Guernsey, the preface signed from Hauteville House in eighteen sixty-two "
            "— then the two chapters read whole in Isabel Hapgood's eighteen eighty-seven "
            "translation: Jean Valjean over the sleeping Bishop, “hesitating between the two "
            "abysses,” and the morning question that undoes the theft — “was that silver ours?”",
            "Then the quiet work underneath it: Paul on the goodness that leadeth to repentance, "
            "Watson's dewdrops on the thistle, the coals of fire of Romans twelve, Peter on the "
            "blood that is the right currency where silver is the wrong one, and Zacchaeus running "
            "the same story the opposite way. The Bishop's lie to the gendarmes is named, not "
            "smoothed over. Closing with George Herbert's “Love (III).”",
        ],
        "walk": [
            ("Victor Hugo · Les Misérables (Hapgood)", "1862 · trans. 1887 · public domain",
             "Born at Besançon, exiled to Guernsey, where he wrote the book — and a preface that "
             "tells you in advance he is not writing to entertain you."),
            ("The theft — “The Fall”", "Hugo · read whole",
             "Valjean over the sleeping Bishop with an iron candlestick, “hesitating between the "
             "two abysses” — and the crucifix that reaches to both, “a benediction for one and "
             "pardon for the other.”"),
            ("The morning after", "Hugo · read whole",
             "“And, in the first place, was that silver ours?” — the Bishop who cannot be robbed "
             "because he owned nothing, pressing the candlesticks on the thief before the gendarmes."),
            ("Romans 2 · Ephesians 2 · Luke 6", "Scripture · KJV",
             "“The goodness of God leadeth thee to repentance” — mercy arriving first, while the "
             "man is still a thief; “kind unto the unthankful and to the evil.”"),
            ("Thomas Watson · A Body of Divinity", "1620–1686",
             "“Sweet dewdrops are on the thistle, as well as on the rose” — and “God's holiness "
             "makes him illustrious; his mercy makes him endearing.”"),
            ("Romans 12 · 1 Peter 1 · Titus 2", "Scripture · KJV",
             "“Heap coals of fire on his head” — the candlesticks exactly; the currency that "
             "redeems is “not silver and gold, but the precious blood of Christ.”"),
            ("Luke 19 · Zacchaeus", "Scripture · KJV",
             "The other thief — who gives back. Restitution that does not purchase salvation but "
             "announces it, after grace has walked in the door."),
            ("The commonplaces on conscience", "Milton · Valerius Maximus · E. Hopkins",
             "“It is more beautiful to overcome injury by the power of kindness than to oppose to "
             "it the obstinacy of hatred.”"),
            ("George Herbert · “Love (III)”", "The Temple, 1633 · read whole",
             "“Love bade me welcome: yet my soul drew back” — the door on the latch, by day and by "
             "night. Bienvenu means welcome."),
        ],
    },
    {
        "slug": "the-manner-of-the-dispute",
        "idea": "The Manner of the Dispute",
        "lane": "Pastor Politics",
        "day": "Wednesday",
        "date_display": "July 29, 2026",
        "sub": "Pastor Politics · how a Christian carries himself in political controversy",
        "duration": "36 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/the-manner-of-the-dispute.mp3",
        "length": 51512389,
        "lede": "Not whether a Christian should speak of public things, but how — the temper of the "
                "tongue when the subject is political and the room is divided. Scripture's rule for "
                "the contest, John Newton's letter on controversy, and a New England pastor "
                "preaching to the magistrates' faces on election day.",
        "body": [
            "Pastor Politics asks the nearer question: the manner of the dispute. We begin where "
            "the church begins — James on the wisdom that is first pure then peaceable, the "
            "Proverbs' soft answer, the apostles' speech alway with grace and seasoned with salt — "
            "and then hear most of John Newton's letter “On Controversy,” his three warnings on the "
            "opponent, the public, and the self: pray for the man before you set pen against him.",
            "Then a shelf of old voices on how a dispute is lost by winning it — Herbert, "
            "Montaigne, Locke, Hooker — the Epistle to Diognetus on a God who came “seeking to "
            "persuade, not to compel,” and John Davenport's sixteen sixty-nine Boston election "
            "sermon, frankness and tenderness in the same breath, spoken to power in love. Under it "
            "all the Lord's own hard saying — love your enemies — and Paul's “overcome evil with "
            "good.” Closing with Whittier's “Dear Lord and Father of Mankind.”",
        ],
        "walk": [
            ("James 3 · Proverbs 15, 25, 18", "Scripture · KJV",
             "“The wisdom that is from above is first pure, then peaceable” — and the soft answer "
             "that turneth away wrath; the temper Scripture prescribes for the contest."),
            ("Colossians 4 · 2 Timothy 2 · 1 Peter 3", "Scripture · KJV",
             "“Let your speech be alway with grace, seasoned with salt”; the servant of the Lord "
             "must not strive, but give his answer with meekness and fear."),
            ("John Newton · “On Controversy”", "letter, c. 1770s · public domain",
             "The converted slave-trader writes to a friend before the pamphlet goes to press — "
             "the opponent, the public, and the self; pray for the man before you set pen against him."),
            ("The commonplaces on argument", "Anacharsis · Herbert · Montaigne · Locke · Hooker",
             "“Be calm in arguing; for fierceness makes error a fault, and truth discourtesy” — a "
             "shelf of old voices on how a dispute is lost by winning it."),
            ("The Epistle to Diognetus", "2nd century · trans. Roberts–Donaldson",
             "What the soul is in the body, Christians are in the world — and God himself came "
             "“seeking to persuade, not to compel; for violence has no place in the character of God.”"),
            ("John Davenport · Boston election sermon", "May 19, 1669",
             "A pastor preaching to the magistrates' faces on election day: “he that ruleth over "
             "men must be just” — frankness and tenderness together, spoken to power in love."),
            ("Matthew 5 · Romans 12", "Scripture · KJV",
             "“Love your enemies… bless them that curse you”; “be not overcome of evil, but "
             "overcome evil with good.” The political opponent is inside that commandment."),
            ("Buck & Bates · on candor", "public domain",
             "“A temper of mind unsoured by envy, unruffled by malice, and unseduced by prejudice” "
             "— and, in four words, “be candid, but not rude.”"),
            ("Whittier · “Dear Lord and Father of Mankind”", "1872 · read whole",
             "The prayer against feverishness of every kind — “drop thy still dews of quietness, "
             "till all our strivings cease.”"),
        ],
    },
    {
        "slug": "aristocracy",
        "idea": "Aristocracy",
        "lane": "Great Ideas",
        "day": "Tuesday",
        "date_display": "July 28, 2026",
        "sub": "Great Idea №3 · the rule of the best",
        "duration": "34 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/aristocracy.mp3",
        "length": 49802699,
        "lede": "The word is Greek, and it means the rule of the best — and the whole evening "
                "turns on that one word “best”: who they are, how you would know them, whether "
                "their sons are anything like them, and what becomes of the idea in a kingdom "
                "where the last are made first.",
        "body": [
            "Great Idea number three, following the map onward from Angel and Animal. If someone "
            "must rule, who ought it to be? We open where Scripture opens it — the Lord who "
            "raiseth up the poor out of the dust to set them among princes — and then hand the "
            "question to the philosophers: Plato's city of the trained and the just, Aristotle's "
            "rule of the most worthy and its corruptions, and the ancients worrying the old gap "
            "between noble blood and noble men.",
            "Aquinas sets it inside the story of Israel and its seventy elders “in virtue, not in "
            "acreage”; Bacon, Pascal, and the wits weigh birth against worth. Then across the "
            "ocean, Jefferson and Adams spend their retirement arguing the natural aristocracy of "
            "virtue and talent against the artificial one of wealth and birth; Tocqueville sings "
            "the elegy of the aristocratic world as the democratic age comes in; and Spurgeon "
            "takes up the psalm we began with, before Burns closes it in his own Scots — a man's "
            "a man for a' that.",
        ],
        "walk": [
            ("Proverbs, Ecclesiastes, Hannah's Prayer & Psalm 113", "Scripture · KJV",
             "“By me kings reign” — and the Lord who raiseth up the poor out of the dust and the "
             "beggar from the dunghill, to set them among princes."),
            ("Plato · The Republic IV & VIII", "c. 375 BC · trans. Jowett",
             "Aristocracy not as a class of families but as the city ruled by the trained and "
             "the just — and how it first begins to die."),
            ("Aristotle · Politics III", "c. 350 BC · trans. Ellis",
             "The rule of the most worthy, its corruption into oligarchy, and the doubt that has "
             "haunted the idea ever since: every party thinks its own claim to rule the just one."),
            ("The ancients on blood vs. worth", "Euripides · Seneca · Juvenal · Homer",
             "“Few sons attain the praise of their great sires” — the long complaint that noble "
             "birth and noble men are not the same thing."),
            ("Aquinas · Summa Theologica I-II, Q105 a1", "c. 1270 · English Dominican trans.",
             "Israel's mixed constitution — kingdom, aristocracy, and democracy together — and "
             "the seventy elders chosen “in virtue,” not in acreage."),
            ("Bacon · Of Nobility", "1612 · Essays",
             "The ancient noble house as “a fair timber tree, sound and perfect” — and the warning "
             "that nobility of birth commonly abateth industry."),
            ("Jefferson & Adams · the 1813 letters", "October–November 1813",
             "Two old rivals arguing the natural aristocracy of virtue and talent against the "
             "artificial one of wealth and birth — the wheat from the chaff."),
            ("Tocqueville · Democracy in America", "1840 · trans. Reeve",
             "The elegy at the book's close: the aristocratic world giving way to the democratic, "
             "judged at last by the eye of God, to whom “the greater well-being of all” is most "
             "pleasing."),
            ("1 Corinthians 1 & James 2", "Scripture · KJV",
             "God hath chosen the base things of the world to confound the mighty — and the church "
             "warned against the gold ring and the goodly apparel."),
            ("Spurgeon · Treasury of David, Psalm 113", "1834–1892 · public domain",
             "“It is worth while to be cast down, to be so divinely raised from the dust” — all "
             "his people made princes."),
            ("Robert Burns · “A Man's a Man for A' That”", "1795 · read whole",
             "The ploughman's answer, sung in Scots: the rank is but the guinea's stamp; the "
             "man's the gowd for a' that."),
        ],
    },
    {
        "slug": "the-sowing-chapter",
        "idea": "The Sowing Chapter",
        "lane": "The Scriptures",
        "day": "Monday",
        "date_display": "July 27, 2026",
        "sub": "The Scriptures · Ecclesiastes 11 — the text behind the sermon",
        "duration": "43 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/the-sowing-chapter.mp3",
        "length": 62441892,
        "lede": "The sowing chapter — Ecclesiastes eleven — read whole and walked through the old "
                "expositors: cast your bread on the waters though you cannot know; sow though you "
                "cannot read the weather; and “rejoice, O young man, in thy youth,” remembering "
                "the judgment that makes the feast honest.",
        "body": [
            "The text behind this week's sermon, read straight and then opened by the whole shelf "
            "of the old commentators — Poole, Benson, Gill, Delitzsch, Matthew Henry, and the "
            "Cambridge, Pulpit and Jamieson-Fausset-Brown commentaries — on the Preacher's "
            "four-fold “thou knowest not” and his four-fold command to act anyway: cast, give, "
            "sow, withhold not thine hand.",
            "Then the old collections' long shelves on the “waiting sickness” and on opportunity; "
            "Marcus Aurelius on the shortness of the days; and the turn to youth and judgment — "
            "“rejoice, O young man… but know thou that God will bring thee into judgment” — carried "
            "at length by Alexander MacLaren's New Year sermon (rejoice, reflect, remember) and "
            "J. C. Ryle's Thoughts for Young Men, with the witnesses of Proverbs, James and "
            "Isaiah. Closing with Longfellow's “A Psalm of Life.”",
        ],
        "walk": [
            ("Ecclesiastes 11", "Scripture · KJV",
             "“Cast thy bread upon the waters… In the morning sow thy seed” — four times “thou "
             "knowest not,” four times a command to act anyway."),
            ("The commentators on “cast thy bread”", "Poole · Benson · Cambridge · Pulpit · Delitzsch",
             "Chardin on rice sown in flood-water; Theognis' “sowing the sea”; Goethe; Rabbi "
             "Akiba's loaf — “if the fish know it not, yet the Creator knows.”"),
            ("“He that observeth the wind shall not sow”", "Benson · Gill · Delitzsch · Pulpit",
             "The farmer who never plants — “probability is the guide of life”; Gregory the Great "
             "on the wind and clouds as the fearful soul."),
            ("Matthew Henry", "on the sowing chapter",
             "“Wherever we are, we may find good work to do… Be not weary in well-doing, for in "
             "due season you shall reap.”"),
            ("The old collections — delay & opportunity", "Hall · Butler · Channing · Foster · Bacon · Seneca",
             "The “waiting sickness” and its cure — with Thomas Brooks on the delays that are "
             "God's, not ours."),
            ("Marcus Aurelius · Meditations (Casaubon)", "c. 175",
             "“…as one who, for aught thou knowest, may at this very present depart out of this "
             "life.”"),
            ("Ecclesiastes 11:7 – 12:1", "Scripture · KJV",
             "“Rejoice, O young man, in thy youth… but know thou, that for all these things God "
             "will bring thee into judgment.”"),
            ("The commentators on “Rejoice, O young man”", "Henry · Poole · Barnes · Gill · Ellicott · JFB · Cambridge",
             "Sincere counsel or irony? — the feast made honest; Herodotus' coffin-image carried "
             "round the Egyptian table."),
            ("Alexander MacLaren", "the New Year sermon",
             "Rejoice · Reflect · Remember — “all your life a seed-time, all your life a "
             "harvest-time too”; deeds hardening into a house for the soul."),
            ("J. C. Ryle · Thoughts for Young Men", "1886, lightly modernized",
             "“What youth sows, old age must reap”; habits like trees strengthened by age; "
             "footprints hardened in the rock."),
            ("Proverbs 27 · James 4 · John 9 · Psalm 90 · Isaiah 40", "Scripture · KJV",
             "“Boast not thyself of tomorrow”; life “a vapour”; “the night cometh, when no man "
             "can work”; “they that wait upon the LORD shall renew their strength.”"),
            ("Longfellow · “A Psalm of Life”", "1838",
             "The close — the footprints turned to the other use: “Let us, then, be up and "
             "doing… learn to labor and to wait.”"),
        ],
    },
    {
        "slug": "the-ravens-and-the-lilies",
        "idea": "The Ravens and the Lilies",
        "lane": "The Surprise",
        "day": "Saturday",
        "date_display": "July 25, 2026",
        "sub": "The Surprise · anxiety, and the God who feeds the birds",
        "duration": "32 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/the-ravens-and-the-lilies.mp3?v=2",
        "length": 46816984,
        "lede": "The anxious mind at the end of the day — met by the ravens and the lilies, "
                "diagnosed by the philosophers, quieted by the old divines, and finally answered "
                "by the Father who feeds the birds and gives His beloved sleep.",
        "body": [
            "Tonight's wildcard is drawn from Chris's own preaching — a sermon on Jesus' command "
            "not to be anxious — and grown into the great public-domain voices that stand behind "
            "it, drawn from a new library of sources: A. W. Pink on the goodness of God toward all "
            "His creatures, the Stoics on the futility of worry, the old moralists on the quiet "
            "soul, and the poets on the folly of borrowing trouble from tomorrow.",
            "From Luke's ravens and lilies through Pink, Seneca, Epictetus and Marcus Aurelius; "
            "the moralists Crabb, Sterne and the Puritan Thomas Brooks; the Scriptures on casting "
            "our care and God's mercies new every morning — closing on “Come unto me”, "
            "the cross as the ground of all comfort, and Scriven's “What a Friend We Have in "
            "Jesus.”",
        ],
        "walk": [
            ("Luke 12:22–34", "Scripture · KJV",
             "“Consider the ravens… consider the lilies… how much more will he clothe "
             "you, O ye of little faith?”"),
            ("A. W. Pink · The Attributes of God", "1930",
             "The goodness of God toward all His creatures — “The eyes of all wait upon "
             "Thee; and Thou givest them their meat in due season.”"),
            ("Seneca · Epictetus · Marcus Aurelius", "the Stoics on worry",
             "“The mind that is anxious about the future is miserable”; “men are "
             "disturbed not by things, but by the views which they take of them.”"),
            ("The moralists — via Day's Collacon", "Crabb · Cave · Sterne · Thomas Brooks",
             "“The still and quiet soul is like a ship that lies quiet in the harbour”; "
             "“in every man's cup… there are some cordial drops.”"),
            ("The poets — via Hoyt's Cyclopedia", "Cowper · Beaumont & Fletcher · Lucretius",
             "“Nature too unkind, that made no medicine for a troubled mind”; care that "
             "“nestles in the breast of kings.”"),
            ("Matthew 6 · Philippians 4 · 1 Peter 5", "Scripture · KJV",
             "“Take no thought for the morrow”; “be careful for nothing”; "
             "“casting all your care upon him; for he careth for you.”"),
            ("Psalm 127 · Lamentations 3", "Scripture · KJV",
             "“He giveth his beloved sleep”; “his compassions… are new every "
             "morning: great is thy faithfulness.”"),
            ("Romans 8:32 · Matthew 11:28–30", "Scripture · KJV",
             "“He that spared not his own Son… how shall he not… freely give us all "
             "things?”; “Come unto me… and I will give you rest.”"),
            ("Joseph Scriven · “What a Friend We Have in Jesus”", "1855",
             "The close — “O what peace we often forfeit… all because we do not carry "
             "everything to God in prayer.”"),
        ],
    },
    {
        "slug": "the-threefold-cord",
        "idea": "The Threefold Cord",
        "lane": "The Surprise",
        "day": "Thursday",
        "date_display": "July 23, 2026",
        "sub": "The Surprise · friendship, from the Preacher to the threefold cord",
        "duration": "35 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/the-threefold-cord.mp3",
        "length": 50653208,
        "lede": "The great and ordinary good of friendship — read from the Preacher's plain "
                "arithmetic, through the philosophers and poets who kept arriving at the same "
                "truth, up to the Friend who lays down his life, and the threefold cord that was "
                "tied before the world.",
        "body": [
            "Tonight's wildcard is drawn from Chris's own preaching — a sermon on Ecclesiastes and "
            "friendship — and grown into the great public-domain voices that stand behind it: the "
            "Preacher's case that two are better than one, the philosophers' agreement that no one "
            "would live without friends, and the Scriptures' own portrait of the friend who "
            "sticketh closer than a brother.",
            "From Ecclesiastes through Aristotle, Cicero, Bacon and Emerson; the poets on faithful "
            "friends and the testing of adversity; the Proverbs, and the friendships of David and "
            "Jonathan, Ruth and Naomi — closing on Christ's “I have called you friends,” the "
            "threefold cord of the Trinity, and Fawcett's hymn.",
        ],
        "walk": [
            ("Ecclesiastes 4:7–12", "Scripture · KJV",
             "“Two are better than one… a threefold cord is not quickly broken.”"),
            ("Aristotle · Nicomachean Ethics", "c. 340 BC",
             "Friendship is “most necessary for life” — no one would live without friends; the "
             "three kinds; the perfect friendship of the good who wish one another's good for "
             "their sakes."),
            ("Cicero · On Friendship (Laelius)", "44 BC",
             "“Friendship… enhances the lustre of prosperity, and by dividing and sharing "
             "adversity lessens its burden.”"),
            ("Francis Bacon · Of Friendship", "1625",
             "“It redoubleth joys, and cutteth griefs in halves”; friendship “maketh daylight in "
             "the understanding.”"),
            ("Stanford Encyclopedia of Philosophy · Friendship", "quoted with credit",
             "Friendship as a concern “for the welfare of the other, for the other's sake.”"),
            ("Emerson · Friendship", "1841",
             "“A friend is a person with whom I may be sincere… a friend may well be reckoned the "
             "masterpiece of nature.”"),
            ("The poets — via Hoyt's Cyclopedia", "Shakespeare · Ovid · Young · Longfellow",
             "“Faithful friends are hard to find”; “Prosperity makes friends, and adversity tries "
             "them”; “A friend is worth all hazards we can run.”"),
            ("Proverbs 17, 18, 27", "Scripture · KJV",
             "“A friend loveth at all times”; “faithful are the wounds of a friend”; “iron "
             "sharpeneth iron”; “a friend that sticketh closer than a brother.”"),
            ("David & Jonathan · Ruth & Naomi", "Scripture · KJV",
             "“The soul of Jonathan was knit with the soul of David”; “whither thou goest, I will "
             "go… if ought but death part thee and me.”"),
            ("John 15:13–15", "Scripture · KJV",
             "“Greater love hath no man than this… I have called you friends.”"),
            ("John Fawcett · “Blest Be the Tie That Binds”", "1782",
             "The close — “the fellowship of kindred minds… we share our mutual woes, our mutual "
             "burdens bear.”"),
        ],
    },
    {
        "slug": "the-long-road-home",
        "idea": "The Long Road Home",
        "lane": "The Surprise",
        "day": "Wednesday",
        "date_display": "July 22, 2026",
        "sub": "The Surprise · endurance, from Peter to the pilgrim's song",
        "duration": "24 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/the-long-road-home.mp3",
        "length": 34406210,
        "lede": "The pilgrim's road through the wilderness between deliverance and home — and the "
                "endurance that is fueled not by our own strength but by the One who endured first.",
        "body": [
            "Tonight's wildcard is drawn from Chris's own preaching — a sermon on 1 Peter and "
            "Christian endurance — and grown into the great public-domain voices that stand behind "
            "it: the Exodus wilderness, the cloud of witnesses, the martyrs' training-ground, and "
            "the pilgrim's long walk home.",
            "From Peter's charge to gird up the mind, through Paul reading the wilderness as a "
            "warning, to Hebrews' company of strangers who died still walking, to Tertullian and "
            "Augustine, Bunyan's Valiant-for-truth and the psalms of the road — closing with "
            "Christina Rossetti and the pilgrim's own song.",
        ],
        "walk": [
            ("1 Peter 1:13–19", "Scripture · KJV",
             "“Gird up the loins of your mind… redeemed with the precious blood of Christ, as of a "
             "lamb without blemish.”"),
            ("Exodus 32", "Scripture · KJV",
             "The golden calf — reversion in the wilderness while Moses is up the mountain in the "
             "cloud of God."),
            ("1 Corinthians 10:1–13", "Scripture · KJV",
             "The wilderness written as our example — “let him that thinketh he standeth take heed "
             "lest he fall.”"),
            ("Hebrews 3–4", "Scripture · KJV",
             "“Harden not your hearts… let us labour therefore to enter into that rest.”"),
            ("Hebrews 11", "Scripture · KJV",
             "The strangers and pilgrims who died in faith — “they desire a better country… he "
             "hath prepared for them a city.”"),
            ("Hebrews 12:1–3", "Scripture · KJV",
             "The cloud of witnesses — “looking unto Jesus… who for the joy set before him endured "
             "the cross.”"),
            ("Tertullian · To the Martyrs", "c. 197",
             "The prison as a training-ground; the athlete pressed and worn out for the contest."),
            ("Augustine · On Patience", "c. 418",
             "Patience is the love of God, holding on — the strength to endure is itself a gift."),
            ("2 Corinthians 4:8–18", "Scripture · KJV",
             "“Our light affliction… worketh for us a far more exceeding and eternal weight of "
             "glory.”"),
            ("Bunyan · The Pilgrim's Progress", "1684",
             "Valiant-for-truth at the river — “my marks and scars I carry with me… all the "
             "trumpets sounded for him on the other side.”"),
            ("Psalms 84 & 121", "Scripture · KJV",
             "The pilgrim psalms — “they go from strength to strength”; “he that keepeth thee will "
             "not slumber.”"),
            ("John Newton · “Amazing Grace”", "1779",
             "“Through many dangers, toils, and snares… grace will lead me home.”"),
            ("Revelation 7:13–17", "Scripture · KJV",
             "“These are they which came out of great tribulation… God shall wipe away all tears "
             "from their eyes.”"),
            ("Rossetti “Up-Hill” · Bunyan's pilgrim song", "1858 · 1684",
             "The close: “beds for all who come,” and “Who would true valour see… to be a "
             "pilgrim.”"),
        ],
    },
    {
        "slug": "animal",
        "idea": "Animal",
        "lane": "Great Ideas",
        "day": "Tuesday",
        "date_display": "July 21, 2026",
        "sub": "Great Idea №2 · following the map onward from Angel",
        "duration": "31 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/animal.mp3?v=2",
        "length": 45258376,
        "lede": "The season turns the page from Angel to Animal — the creature just below the "
                "angels and just above the dust.",
        "body": [
            "We are walking this season through the great ideas one at a time, following the map "
            "Mortimer Adler drew when he indexed the Western canon under a hundred and two headings. "
            "Last week the map opened at Angel; tonight it turns to the animal — the beasts of the "
            "field and the fowl of the air, the lion in his den and the cat on the hearth, the horse "
            "that laughs among the trumpets and the ant that lays up its grain against the winter.",
            "What are they? What do they know? And what are we, that we should be set among them and "
            "yet told we are not merely one of them? From the fifth day of creation to Darwin's "
            "entangled bank, we listen to Jerusalem and Athens and the long argument in between — "
            "with a little jazz to change the light before each new movement begins.",
        ],
        "walk": [
            ("Genesis 1:20–25, 30", "Scripture · KJV",
             "The earth brings forth the living creature “after his kind.”"),
            ("Job 39", "Scripture · KJV",
             "God's animal catechism out of the whirlwind — the wild ass, the ostrich, and the "
             "war-horse who says “Ha, ha” among the trumpets."),
            ("Psalm 104:19–30", "Scripture · KJV",
             "The young lions seeking their meat from God; leviathan made to play."),
            ("Aristotle · On the Parts of Animals I.5", "c. 350 BC · trans. Ogle",
             "Even in the kitchen, divinities are present — in every creature, “something natural "
             "and something beautiful.”"),
            ("Basil of Caesarea · Hexaemeron IX", "c. 370 · trans. Jackson",
             "The beasts as our teachers: the ant's foresight, the dog's syllogism at the "
             "crossroads, and the head that was made to look up."),
            ("Aquinas · Summa Theologica I, Q75 a3", "c. 1270 · English Dominican trans.",
             "Whether the souls of brute animals are subsistent — truly ensouled, but bound to the "
             "body as the eye is bound to the light."),
            ("Montaigne · Apology for Raymond Sebond", "1580 · trans. Cotton",
             "“When I play with my cat, who knows whether I do not make her more sport than she "
             "makes me?”"),
            ("Descartes · Discourse on Method, Part V", "1637 · trans. Veitch",
             "The two tests, and the beast as machine — a clock that keeps better time than its "
             "maker, and knows nothing of the hour."),
            ("Darwin · On the Origin of Species", "1859 · first edition",
             "The entangled bank, and “grandeur in this view of life… endless forms most "
             "beautiful” — life “breathed” into being, the verb he kept when he took the "
             "Creator back out."),
            ("Spurgeon · Autobiography & Metropolitan Tabernacle Pulpit", "1834–1892 · public domain",
             "The missing links that never close the chain — resemblances granted, then laid "
             "at “the one great master-mind of God”; and the ox that shames us, who knows the "
             "hand that feeds him."),
            ("Christopher Smart · “For I will consider my Cat Jeoffry”", "c. 1760s · Jubilate Agno",
             "The close: a poem written in a madhouse with no company but a cat — praise folded "
             "into a wet nose and a glaring eye."),
        ],
    },
    {
        "slug": "ecclesiastes-9-10",
        "idea": "One Sinner & a Dead Fly",
        "lane": "The Scriptures",
        "day": "Monday",
        "date_display": "July 20, 2026",
        "sub": "The Scriptures · Ecclesiastes 9–10",
        "duration": "43 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/ecclesiastes-9-10.mp3",
        "length": 62488059,
        "lede": "A little folly, like a dead fly in the perfumer's ointment, can spoil the whole — "
                "and one sinner destroys much good.",
        "body": [
            "Tonight the Scriptures bring us to the close of Ecclesiastes 9 and the opening of "
            "chapter 10, and to one of the Preacher's sharpest images: dead flies that turn a whole "
            "jar of sweet ointment rancid. So, he says, does a little folly outweigh wisdom and "
            "honour — and one sinner destroys much good.",
            "We follow the thought down through Achan, who hid a single Babylonish garment and "
            "troubled all Israel; through Charles Spurgeon on the deadliness of the “little” sin — "
            "the lone Scottish thistle that overran a whole continent; and out to the last, quiet "
            "warning: that every fence we trust — conscience, grace, eternal hopes and fears — can "
            "be blown quite away by one cunning bosom sin.",
        ],
        "walk": [
            ("Ecclesiastes 10:1", "Scripture · KJV",
             "“Dead flies cause the ointment of the apothecary to send forth a stinking savour: so "
             "doth a little folly.”"),
            ("Ecclesiastes 9:18", "Scripture · KJV",
             "“One sinner destroyeth much good.” — the hinge of the whole meditation."),
            ("The flies of death", "Hebrew note",
             "The phrase behind the verse: small, poisonous things — deadly out of all proportion "
             "to their size."),
            ("Achan", "Joshua 7 · KJV",
             "“I have sinned against the LORD.” — the hidden Babylonish garment and the wedge of "
             "gold that troubled all Israel."),
            ("C. H. Spurgeon", "1834–1892",
             "On the deadliness of little sins — the single Scottish thistle that overran "
             "Australia; “Satan always begins with us as he did with Achan.”"),
            ("Ecclesiastes 10:12", "Scripture · KJV",
             "“The fool's lips swallow up himself.”"),
            ("The close", "public domain verse",
             "One cunning bosom sin blows every fence away — conscience, angels, grace, and all."),
        ],
    },
    {
        "slug": "angel",
        "idea": "Angel",
        "lane": "Great Ideas",
        "day": "Saturday",
        "date_display": "July 18, 2026",
        "sub": "Great Idea №1 · the unseen host",
        "duration": "29 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/angel.mp3?v=2",
        "length": 42297969,
        "lede": "The list of the great ideas begins — wonderfully — not with Being or God or Truth, "
                "but with Angel: the oldest witness that the darkness is not empty, and the quiet "
                "room a good deal more crowded than it looks.",
        "body": [
            "The debut of the Tuesday lane, reworked at length. In 1952 Mortimer Adler and his "
            "readers indexed the Western canon under a hundred and two great ideas, from Angel to "
            "World; on these nights we walk that list in order, reading the old books it points to "
            "— and it opens, of all places, with the messengers.",
            "From Aquinas on whether a purely spiritual creature can exist, through the ranks and "
            "names of heaven — the seraphim and cherubim, Gabriel and Michael, Milton's lone "
            "faithful Abdiel — the war in heaven, the numberless host that sang at creation and "
            "stands at the throne, their ceaseless worship and their guard over frightened people "
            "(Elisha's chariots of fire; the guardian-angel of the old divines), to the one mercy "
            "the angels only lean down to look into. Closing on Jacob's ladder and Francis "
            "Thompson's poem.",
        ],
        "walk": [
            ("Aquinas · Summa Theologica", "13th c. · Dominican trans.",
             "Whether an incorporeal creature exists — “the perfection of the universe requires "
             "it” — and their “exceeding great number.”"),
            ("Colossians 1:16 · Isaiah 6 · Genesis 3:24", "Scripture · KJV, w/ Nuttall on the orders",
             "The ranks of heaven — thrones and dominions; the seraphim who “guard with veiled "
             "faces the Divine glory”; the cherubim at Eden's gate."),
            ("The named angels · the war in heaven", "Nuttall · Milton · Rev. 12 · Jude 6",
             "Gabriel “the strength of God,” Michael “Who is like God?”, and Abdiel who alone "
             "“withstood Satan in his revolt” — the third of heaven cast out."),
            ("Daniel 7 · Job 38 · Revelation 5", "Scripture · KJV",
             "The multitude — “ten thousand times ten thousand”; “the morning stars sang "
             "together”; the ceaseless “Holy, holy, holy.”"),
            ("Milton · Paradise Lost", "1667",
             "“Millions of spiritual creatures walk the earth unseen”; and Raphael sent to Adam "
             "“as friend with friend.”"),
            ("Psalm 91 · Psalm 34 · 2 Kings 6", "Scripture · KJV",
             "The guard — “he shall give his angels charge over thee”; “encampeth round about”; "
             "the mountain “full of horses and chariots of fire.”"),
            ("The guardian angel — via Day's Collacon", "Jones of Nayland · Jean Paul Richter",
             "“Every sincere believer is under the constant care… of the highest of the angels”; "
             "the guardian who “always is looking down upon us.”"),
            ("Hebrews 2:16 · 1 Peter 1:12 · Luke 15:10", "Scripture · KJV",
             "The one mercy not theirs — “he took not on him the nature of angels”; “which things "
             "the angels desire to look into”; their joy “over one sinner that repenteth.”"),
            ("Luke 2 · the angels and the life of Christ", "Scripture · KJV",
             "The host at Bethlehem; the angel in Gethsemane; the stone rolled away — from the "
             "manger to the throne, the honour guard of the King."),
            ("Genesis 28 · John 1:51 · Francis Thompson", "Scripture · KJV · 1913",
             "Jacob's ladder — fulfilled in the Son of man — and the close: “The angels keep their "
             "ancient places — turn but a stone, and start a wing!”"),
        ],
    },
    {
        "slug": "a-tale-of-two-cities",
        "idea": "A Tale of Two Cities",
        "lane": "Fiction's Most Famous Passages",
        "day": "Saturday",
        "date_display": "July 18, 2026",
        "sub": "Fiction's Most Famous Passages · Dickens' opening, and the quiet work underneath it",
        "duration": "31 min",
        "audio_url": "https://sermons-cdn.sermonsteward.com/vespers/episodes/a-tale-of-two-cities.mp3?v=3",
        "length": 43992615,
        "lede": "The most famous opening sentence in English — the age that thought itself settled "
                "for ever, while the Woodman and the Farmer went silently about their work — read "
                "whole, then followed through the great voices on change, fortune, judgment, and "
                "the one Teller who is inside his own story.",
        "body": [
            "Fiction's Most Famous Passages opens with Dickens. First an entry point — who he was, "
            "the grief behind the book, the magazine it ran in, the plot — then Chapter the First "
            "read whole: “the best of times, the worst of times,” the lords certain that “things "
            "in general were settled for ever,” and the silent Woodman-Fate and Farmer-Death "
            "already growing the guillotine's timber and parking the tumbrels of the Revolution.",
            "Then the hour turns on what is buried inside it: Ecclesiastes and Heraclitus on the "
            "turning of all things; Marcus Aurelius and Boethius' wheel of Fortune; the Scriptures' "
            "axe at the root and law of the harvest; Nebuchadnezzar's boast beside Shelley's "
            "“Ozymandias”; Augustine's two cities; and — by way of a songwriter on the teller who "
            "can only “shed light, not master” — the one Author who is inside his own story and "
            "has already published its end. Closing with “Abide with Me.”",
        ],
        "walk": [
            ("Dickens · A Tale of Two Cities, Ch. I “The Period”", "1859",
             "“It was the best of times…”; “things in general were settled for ever”; and the "
             "silent Woodman-Fate and Farmer-Death."),
            ("Ecclesiastes 1 & 3", "Scripture · KJV",
             "“There is no new thing under the sun”; “a time to plant, and a time to pluck up.”"),
            ("Heraclitus", "with SEP, credited",
             "The ever-living fire — “you cannot step twice into the same river.”"),
            ("Marcus Aurelius · Meditations; Boethius · Consolation", "the change of all things",
             "“All is ephemeral”; Lady Fortune's wheel — “inconstancy is my very essence.”"),
            ("Matthew 3 · Galatians 6", "Scripture · KJV",
             "The hand on the wheel — “the axe is laid unto the root”; “whatsoever a man soweth, "
             "that shall he also reap.”"),
            ("Daniel 4 · Shelley · “Ozymandias”", "Scripture · KJV · 1818",
             "Two kings, one boast — Nebuchadnezzar interrupted from heaven; the shattered king "
             "in the sand: “Look on my works, ye Mighty, and despair!”"),
            ("1 Thessalonians 5 · Revelation 14", "Scripture · KJV",
             "“When they shall say, Peace and safety; then sudden destruction”; “thrust in thy "
             "sickle, and reap.”"),
            ("Augustine · The City of God", "c. 426",
             "“Two cities have been formed by two loves” — the older, larger tale behind Dickens'."),
            ("Job 14 · Psalm 90 · Acts 17", "Scripture · KJV",
             "“We spend our years as a tale that is told”; God “hath determined the times… and "
             "will judge the world by that man… raised from the dead.” (w/ Robert Hunter, "
             "paraphrased — the teller who can “shed light, and not to master.”)"),
            ("Isaiah 40 · Henry Francis Lyte · “Abide with Me”", "Scripture · KJV · 1847",
             "“The word of our God shall stand for ever”; the close — “O thou who changest not, "
             "abide with me.”"),
        ],
    },
]


def esc(s):
    return html.escape(str(s), quote=True)


# ─────────────────────────── chrome ───────────────────────────

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Spectral:ital,wght@0,300;0,400;0,500;0,600;1,400&'
    'family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
)

# Grain overlay (tiny SVG noise, data-URI) — the worn-vinyl texture from the cover.
GRAIN = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'>"
    "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' "
    "numOctaves='2' stitchTiles='stitch'/></filter>"
    "<rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.5'/></svg>"
)

CSS = """
  :root {
    --bg:        #090911;
    --bg-2:      #0c0c18;
    --surface:   #141426;
    --surface-2: #1b1b34;
    --rule:      #29294a;
    --ink:       #ece6d6;
    --ink-soft:  #b9b7cc;
    --ink-faint: #7c7b95;
    --indigo:    #7d79c4;
    --indigo-deep:#4b4a80;
    --blue:      #6f8fb6;
    --brass:     #c9a45c;
    --brass-deep:#a8853f;
    --link:      #c9a45c;
  }
  * { box-sizing: border-box; }
  html { -webkit-text-size-adjust: 100%; }
  body {
    margin: 0;
    font-family: "Spectral", Georgia, serif;
    color: var(--ink);
    background:
      radial-gradient(1100px 620px at 82% -8%, rgba(75,74,128,0.42), transparent 60%),
      radial-gradient(900px 700px at -6% 12%, rgba(46,45,90,0.34), transparent 55%),
      linear-gradient(180deg, #0b0b16 0%, #090911 44%, #070710 100%);
    background-attachment: fixed;
    min-height: 100vh;
    line-height: 1.6;
  }
  /* worn-vinyl grain over everything */
  body::before {
    content: ""; position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background-image: url("%GRAIN%"); background-size: 180px 180px;
    opacity: 0.05; mix-blend-mode: overlay;
  }
  body > * { position: relative; z-index: 1; }
  .ui { font-family: "Inter", system-ui, sans-serif; }
  a { color: var(--link); }

  main { max-width: 960px; margin: 0 auto; padding: 40px 24px 120px; }

  /* header */
  .site-header { border-bottom: 1px solid var(--rule); background: rgba(9,9,17,0.6);
    backdrop-filter: blur(6px); position: sticky; top: 0; z-index: 5; }
  .site-header-inner { max-width: 960px; margin: 0 auto; padding: 16px 24px;
    display: flex; align-items: center; justify-content: space-between; }
  .brand { font-family: "Inter", sans-serif; font-weight: 600; letter-spacing: 0.34em;
    text-transform: uppercase; font-size: 15px; color: var(--ink); text-decoration: none; }
  .brand .dot { color: var(--brass); }
  .site-nav { display: flex; gap: 24px; }
  .site-nav a { font-family: "Inter", sans-serif; font-size: 12.5px; font-weight: 500;
    letter-spacing: 0.06em; color: var(--ink-soft); text-decoration: none;
    text-transform: uppercase; }
  .site-nav a:hover { color: var(--brass); }
  .brass-rule { height: 1px; border: 0; margin: 0;
    background: linear-gradient(90deg, transparent, var(--brass-deep) 20%, var(--brass) 50%, var(--brass-deep) 80%, transparent);
    opacity: 0.55; }

  /* hero */
  .hero { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 46px;
    align-items: center; margin: 46px 0 30px; }
  .hero-eyebrow { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    letter-spacing: 0.22em; text-transform: uppercase; color: var(--indigo);
    margin-bottom: 20px; display: flex; align-items: center; gap: 12px; }
  .hero h1 { font-family: "Spectral", serif; font-weight: 300; font-size: 40px;
    line-height: 1.16; letter-spacing: -0.005em; margin: 0 0 20px; color: var(--ink); }
  .hero h1 em { font-style: italic; color: var(--brass); }
  .hero-lede { font-size: 18px; color: var(--ink-soft); margin: 0 0 18px; max-width: 52ch; }
  .hero-art { position: relative; }
  .hero-art img { width: 100%; border-radius: 12px; display: block;
    box-shadow: 0 30px 80px rgba(0,0,0,0.6), 0 0 0 1px rgba(125,121,196,0.18);
  }
  .hero-art::after { content: ""; position: absolute; inset: -14%;
    background: radial-gradient(circle at 50% 45%, rgba(125,121,196,0.28), transparent 62%);
    z-index: -1; }

  /* equalizer — a quiet jazz nod */
  .eq { display: inline-flex; align-items: flex-end; gap: 3px; height: 15px; }
  .eq span { width: 3px; background: var(--brass); border-radius: 2px;
    animation: eq 1.4s ease-in-out infinite; opacity: 0.85; }
  .eq span:nth-child(1){ height: 40%; animation-delay: 0s; }
  .eq span:nth-child(2){ height: 90%; animation-delay: 0.2s; }
  .eq span:nth-child(3){ height: 60%; animation-delay: 0.4s; }
  .eq span:nth-child(4){ height: 100%; animation-delay: 0.1s; }
  .eq span:nth-child(5){ height: 50%; animation-delay: 0.5s; }
  @keyframes eq { 0%,100% { transform: scaleY(0.4); } 50% { transform: scaleY(1); } }
  @media (prefers-reduced-motion: reduce) { .eq span { animation: none; } }

  /* sections */
  .section { margin: 62px 0 0; }
  .section-eyebrow { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    letter-spacing: 0.2em; text-transform: uppercase; color: var(--brass);
    margin-bottom: 8px; }
  .section h2 { font-family: "Spectral", serif; font-weight: 400; font-size: 27px;
    margin: 0 0 6px; color: var(--ink); }
  .section .section-sub { color: var(--ink-faint); font-size: 15px; margin: 0 0 26px;
    font-style: italic; }

  .programme { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
  .card { background: linear-gradient(180deg, var(--surface), var(--bg-2));
    border: 1px solid var(--rule); border-radius: 12px; padding: 16px 15px 17px; }
  .card .num { font-family: "Inter", sans-serif; font-size: 10.5px; letter-spacing: 0.11em;
    color: var(--indigo); text-transform: uppercase; margin-bottom: 9px; }
  .card h3 { font-family: "Spectral", serif; font-weight: 500; font-size: 18px;
    margin: 0 0 7px; color: var(--ink); }
  .card p { font-size: 13px; color: var(--ink-soft); margin: 0; line-height: 1.5; }
  .card .tag { display: inline-block; margin-top: 12px; font-family: "Inter", sans-serif;
    font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase;
    color: var(--ink-faint); border: 1px solid var(--rule); border-radius: 999px;
    padding: 3px 9px; }

  /* listen / coming soon */
  .listen { margin: 62px 0 0; padding: 34px 34px; border: 1px solid var(--rule);
    border-radius: 16px; background:
      radial-gradient(600px 300px at 90% -40%, rgba(75,74,128,0.3), transparent 60%),
      var(--bg-2); text-align: center; }
  .listen h2 { font-family: "Spectral", serif; font-weight: 400; font-size: 26px;
    margin: 0 0 10px; }
  .listen p { color: var(--ink-soft); max-width: 56ch; margin: 0 auto 22px; }
  .subs { display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; }
  .sub { font-family: "Inter", sans-serif; font-size: 13px; font-weight: 500;
    letter-spacing: 0.03em; padding: 11px 20px; border-radius: 999px;
    border: 1px solid var(--rule); color: var(--ink-faint); }
  .sub.soon { opacity: 0.85; }
  .archive { margin-top: 30px; padding-top: 22px; border-top: 1px solid var(--rule);
    text-align: left; }
  .arch-h { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 600;
    letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-faint);
    text-align: center; margin-bottom: 14px; }
  .arch-list { list-style: none; margin: 0 auto; padding: 0; max-width: 520px; }
  .arch-list li { border-bottom: 1px solid var(--rule); }
  .arch-list li:last-child { border-bottom: 0; }
  .arch-list a { display: flex; align-items: baseline; justify-content: space-between;
    gap: 14px; padding: 12px 4px; text-decoration: none; }
  .arch-list a:hover .arch-idea { color: var(--brass); }
  .arch-idea { font-family: "Spectral", serif; font-size: 18px; color: var(--ink); }
  .arch-meta { font-size: 11px; letter-spacing: 0.06em; text-transform: uppercase;
    color: var(--ink-faint); white-space: nowrap; }

  blockquote.pull { font-family: "Spectral", serif; font-style: italic; font-size: 21px;
    line-height: 1.5; color: var(--ink); border: 0; border-left: 2px solid var(--brass);
    margin: 60px 0 0; padding: 6px 0 6px 26px; max-width: 60ch; }
  blockquote.pull .who { display: block; margin-top: 12px; font-style: normal;
    font-family: "Inter", sans-serif; font-size: 12px; letter-spacing: 0.14em;
    text-transform: uppercase; color: var(--ink-faint); }

  .site-footer { border-top: 1px solid var(--rule); margin-top: 26px; padding: 30px 24px 40px;
    text-align: center; font-family: "Inter", sans-serif; font-size: 12.5px;
    letter-spacing: 0.04em; color: var(--ink-faint); }
  .site-footer .foot-mark { letter-spacing: 0.3em; text-transform: uppercase;
    color: var(--ink-soft); margin-bottom: 8px; }

  /* about page prose */
  .prose { max-width: 62ch; }
  .prose h1 { font-family: "Spectral", serif; font-weight: 300; font-size: 38px;
    margin: 30px 0 8px; }
  .prose .kicker { font-family: "Inter", sans-serif; font-size: 12px; letter-spacing: 0.2em;
    text-transform: uppercase; color: var(--brass); margin-bottom: 16px; }
  .prose p { font-size: 18px; color: var(--ink-soft); }
  .prose p.first::first-letter { font-size: 3.2em; float: left; line-height: 0.8;
    padding: 6px 10px 0 0; color: var(--brass); font-weight: 500; }
  .prose .closer { font-family: "Spectral", serif; font-style: italic; font-size: 22px;
    color: var(--ink); margin: 34px 0 0; padding-top: 22px; border-top: 1px solid var(--rule); }
  .back { margin-top: 40px; font-family: "Inter", sans-serif; font-size: 13px; }
  .back a { color: var(--brass); text-decoration: none; }

  /* episode page */
  .ep-head { margin: 24px 0 6px; }
  .ep-eyebrow { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    letter-spacing: 0.18em; text-transform: uppercase; color: var(--indigo); margin-bottom: 14px; }
  .ep-title { font-family: "Spectral", serif; font-weight: 300; font-size: 56px; line-height: 1;
    margin: 0 0 12px; color: var(--ink); }
  .ep-sub { font-size: 12.5px; letter-spacing: 0.05em; color: var(--ink-faint);
    text-transform: uppercase; }
  .ep-sub .dot { color: var(--brass); margin: 0 9px; }
  .ep-player { margin: 26px 0 6px; padding: 16px 18px; border: 1px solid var(--rule);
    border-radius: 12px; background: var(--bg-2); }
  .ep-player audio { width: 100%; display: block; }
  .ep-disclaimer { font-size: 12.5px; font-style: italic; color: var(--ink-faint);
    border-left: 2px solid var(--brass-deep); padding: 2px 0 2px 14px; margin: 18px 0 34px; }
  .ep-lede { font-family: "Spectral", serif; font-style: italic; font-size: 21px; color: var(--ink);
    margin: 0 0 20px; }
  .ep-body p { font-size: 17.5px; color: var(--ink-soft); }
  .walk { margin: 48px 0 0; }
  .walk-h { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    letter-spacing: 0.2em; text-transform: uppercase; color: var(--brass); margin-bottom: 4px; }
  .walk-sub { color: var(--ink-faint); font-style: italic; font-size: 15px; margin: 0 0 22px; }
  .walk-list { list-style: none; margin: 0; padding: 0; }
  .walk-item { display: flex; gap: 18px; padding: 17px 0; border-top: 1px solid var(--rule); }
  .walk-item:last-child { border-bottom: 1px solid var(--rule); }
  .walk-n { font-family: "Inter", sans-serif; font-size: 13px; color: var(--indigo);
    flex: 0 0 26px; padding-top: 4px; font-variant-numeric: tabular-nums; }
  .walk-src { font-family: "Spectral", serif; font-size: 19px; color: var(--ink); }
  .walk-cite { font-family: "Inter", sans-serif; font-size: 10.5px; letter-spacing: 0.09em;
    text-transform: uppercase; color: var(--ink-faint); margin-left: 12px; white-space: nowrap; }
  .walk-note { color: var(--ink-soft); font-size: 15px; margin-top: 5px; line-height: 1.55; }

  /* transcript */
  .transcript { margin: 44px 0 0; border-top: 1px solid var(--rule); }
  .transcript > summary { list-style: none; cursor: pointer; padding: 22px 0 6px;
    font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600; letter-spacing: 0.2em;
    text-transform: uppercase; color: var(--brass); display: flex; align-items: center; gap: 10px; }
  .transcript > summary::-webkit-details-marker { display: none; }
  .transcript > summary::after { content: "＋"; color: var(--ink-faint); font-weight: 400;
    margin-left: auto; font-size: 15px; }
  .transcript[open] > summary::after { content: "－"; }
  .transcript > summary:hover { color: var(--gold, var(--brass)); }
  .transcript-body { max-width: 62ch; padding-top: 8px; }
  .transcript-body p { font-size: 16.5px; color: var(--ink-soft); line-height: 1.62;
    margin: 0 0 15px; }
  .transcript-note { font-family: "Inter", sans-serif; font-size: 12px; font-style: italic;
    color: var(--ink-faint); margin: 0 0 18px; }

  @media (max-width: 760px) {
    .hero { grid-template-columns: 1fr; gap: 30px; }
    .ep-title { font-size: 42px; }
    .walk-cite { display: block; margin: 4px 0 0; white-space: normal; }
    .hero-art { order: -1; max-width: 340px; }
    .hero h1 { font-size: 32px; }
    .programme { grid-template-columns: 1fr; }
  }
""".replace("%GRAIN%", GRAIN)


def header():
    return """<header class="site-header">
  <div class="site-header-inner">
    <a href="/" class="brand ui">Vespers<span class="dot">.</span></a>
    <nav class="site-nav ui">
      <a href="/#listen">Listen</a>
      <a href="/about.html">About</a>
    </nav>
  </div>
</header>
<hr class="brass-rule">"""


def footer():
    return f"""<footer class="site-footer ui">
  <div class="foot-mark">Vespers</div>
  <div>{esc(TAGLINE)}</div>
</footer>"""


def doc(title, description, body, canonical):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{esc(canonical)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:site_name" content="{esc(SITE_NAME)}">
<meta property="og:image" content="{esc(OG_IMAGE)}">
<meta name="theme-color" content="#090911">
{FONTS}
<style>{CSS}</style>
</head>
<body>
{header()}
{body}
{footer()}
</body>
</html>
"""


# ─────────────────────────── pages ───────────────────────────

def home_page():
    latest = EPISODES[0]
    others = "".join(
        f"""<li><a href="/episodes/{e['slug']}">
        <span class="arch-idea">{esc(e['idea'])}</span>
        <span class="arch-meta ui">{esc(e['lane'])} · {esc(e['date_display'])}</span></a></li>"""
        for e in EPISODES[1:]
    )
    archive = f"""
    <div class="archive">
      <div class="arch-h ui">The archive</div>
      <ul class="arch-list">{others}</ul>
    </div>""" if others else ""
    body = f"""<main>
  <section class="hero">
    <div class="hero-copy">
      <div class="hero-eyebrow ui">Great ideas after dark
        <span class="eq"><span></span><span></span><span></span><span></span><span></span></span>
      </div>
      <h1>{esc(TAGLINE)}</h1>
      <p class="hero-lede">A late-night webcast for the great ideas — the last hour of your
      day, spent thinking. Mostly talk, with a little jazz to breathe between the movements.</p>
      <p class="hero-lede">Pour something warm, turn the lights low, and stay a while.</p>
    </div>
    <div class="hero-art">
      <img src="/assets/cover.jpg" alt="Vespers — a chair and a waveform in Blue Note blues">
    </div>
  </section>

  <section class="section">
    <div class="section-eyebrow ui">The programme</div>
    <div class="programme">
      <div class="card">
        <div class="num ui">I · Scripture</div>
        <h3>The Scriptures</h3>
        <p>Slow, unhurried studies through the books and themes of the Bible.</p>
        <span class="tag ui">Book by book</span>
      </div>
      <div class="card">
        <div class="num ui">II · Great Ideas</div>
        <h3>The Syntopicon</h3>
        <p>Mortimer Adler's index to the Great Ideas, taken in alphabetical order.</p>
        <span class="tag ui">A→Z</span>
      </div>
      <div class="card">
        <div class="num ui">III · Public domain</div>
        <h3>The Shelf</h3>
        <p>Classics in the common domain, read and discussed — Dickens and the shelf beyond.</p>
        <span class="tag ui">Public domain</span>
      </div>
      <div class="card">
        <div class="num ui">IV · Wildcard</div>
        <h3>The Surprise</h3>
        <p>Other things that are of interest to the Architect of Vespers.</p>
        <span class="tag ui">Wherever</span>
      </div>
    </div>
  </section>

  <section class="listen" id="listen">
    <div class="section-eyebrow ui" style="color:var(--indigo);">Latest broadcast · {esc(latest['lane'])} · {esc(latest['date_display'])}</div>
    <h2><a href="/episodes/{latest['slug']}" style="color:inherit;text-decoration:none;">{esc(latest['idea'])}</a></h2>
    <p>{esc(latest['lede'])}</p>
    <audio controls preload="none" src="{esc(latest['audio_url'])}"
      style="width:100%; max-width:540px; margin:6px auto 22px; display:block;"></audio>
    <div class="subs">
      <a class="sub ui" href="/episodes/{latest['slug']}"
        style="color:var(--brass); border-color:var(--brass-deep);">Episode notes →</a>
      <span class="sub soon ui">Apple Podcasts · soon</span>
      <span class="sub soon ui">Spotify · soon</span>
    </div>
{archive}
  </section>
</main>"""
    return doc(
        f"{SITE_NAME} — the last hour of your day",
        TAGLINE + " A late-night webcast for the great ideas: the Syntopicon, Scripture, "
        "and the great books, with jazz between the segments.",
        body,
        SITE_URL + "/",
    )


def about_page():
    body = f"""<main>
  <article class="prose">
    <div class="kicker ui">About</div>
    <h1>The last hour of your day</h1>
    <p class="first">Vespers is a webcast for the tail end of the day — the hour when the
    noise finally quiets and there's room to think about something big.</p>
    <p>Each episode takes up one big idea and stays with it. On some nights we work through
    Scripture, and on other nights, an entry in Mortimer Adler's <em>Syntopicon</em>, and
    others from the public bookshelf of our local libraries.</p>
    <p>The form is simple — mostly talk, with just a little jazz stitched between the segments,
    a nocturne to change the light before the next movement begins.</p>
    <p class="closer">Let us take up the last hour of your day.</p>
    <div class="back ui"><a href="/">← Back to Vespers</a></div>
  </article>
</main>"""
    return doc(
        f"About — {SITE_NAME}",
        "Vespers is a late-night webcast for the great ideas — the Syntopicon, Scripture, "
        "and the great books, with jazz between the segments.",
        body,
        SITE_URL + "/about.html",
    )


def episode_page(ep):
    walk_section = ""
    if ep.get("walk"):
        walk = "".join(
            f"""<li class="walk-item">
      <div class="walk-n ui">{i}</div>
      <div class="walk-body">
        <div class="walk-src">{esc(src)}<span class="walk-cite ui">{esc(cite)}</span></div>
        <div class="walk-note">{esc(note)}</div>
      </div>
    </li>"""
            for i, (src, cite, note) in enumerate(ep["walk"], 1)
        )
        walk_section = f"""
    <section class="walk">
      <div class="walk-h ui">Tonight's walk</div>
      <p class="walk-sub">One idea, read chronologically — Scripture and the philosophers, all in
      the public domain.</p>
      <ol class="walk-list">{walk}</ol>
    </section>"""
    transcript_section = ""
    tpath = os.path.join(HERE, "transcripts", ep["slug"] + ".txt")
    if os.path.exists(tpath):
        with open(tpath, encoding="utf-8") as tf:
            raw = tf.read().strip()
        note = ""
        if raw.startswith("[[NOTE]]"):
            first, _, rest = raw.partition("\n")
            note = f'<p class="transcript-note ui">{esc(first[len("[[NOTE]]"):].strip())}</p>'
            raw = rest.strip()
        paras = [p.strip() for p in raw.split("\n\n") if p.strip()]
        paras_html = "\n      ".join(f"<p>{esc(p)}</p>" for p in paras)
        transcript_section = f"""
    <details class="transcript">
      <summary class="ui">Transcript</summary>
      <div class="transcript-body">
      {note}{paras_html}
      </div>
    </details>"""
    body_html = "".join(f"<p>{esc(p)}</p>\n    " for p in ep["body"])
    body = f"""<main>
  <article>
    <div class="ep-head">
      <div class="ep-eyebrow ui">{esc(ep['lane'])} · {esc(ep['day'])} · {esc(ep['date_display'])}</div>
      <h1 class="ep-title">{esc(ep['idea'])}</h1>
      <div class="ep-sub ui">{esc(ep['sub'])}<span class="dot">·</span>{esc(ep['duration'])}</div>
    </div>

    <div class="ep-player">
      <audio controls preload="none" src="{esc(ep['audio_url'])}"></audio>
    </div>
    <p class="ep-disclaimer ui">{esc(DISCLAIMER)}</p>

    <p class="ep-lede">{esc(ep['lede'])}</p>
    <div class="ep-body">
    {body_html}</div>
{walk_section}
{transcript_section}
    <div class="back ui"><a href="/">← Back to Vespers</a></div>
  </article>
</main>"""
    return doc(
        f"{esc(ep['idea'])} — {SITE_NAME}",
        ep["lede"],
        body,
        f"{SITE_URL}/episodes/{ep['slug']}",
    )


# ─────────────────────────── build ───────────────────────────

def main():
    os.makedirs(PUBLIC, exist_ok=True)
    if os.path.isdir(SRC_ASSETS):
        shutil.copytree(SRC_ASSETS, os.path.join(PUBLIC, "assets"), dirs_exist_ok=True)
    with open(os.path.join(PUBLIC, "index.html"), "w", encoding="utf-8") as f:
        f.write(home_page())
    with open(os.path.join(PUBLIC, "about.html"), "w", encoding="utf-8") as f:
        f.write(about_page())
    ep_dir = os.path.join(PUBLIC, "episodes")
    os.makedirs(ep_dir, exist_ok=True)
    for ep in EPISODES:
        with open(os.path.join(ep_dir, f"{ep['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(episode_page(ep))
    print(f"Built Vespers landing + about + {len(EPISODES)} episode(s) into public/")


if __name__ == "__main__":
    main()
