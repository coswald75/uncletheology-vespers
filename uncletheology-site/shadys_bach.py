# -*- coding: utf-8 -*-
"""
Shady's Bach — album data (Oswald Records).

Classical-meets-street: apologetics and doctrine in an Eminem cadence over a
marble-bust-in-the-alley aesthetic. Lyrics from Shady's Bach Lyrics.md.

- "Solfeggeitto" is the same song as the Proverbs cut (reused intentionally).
- "Divergent Mix // 2 Books" is a remix of track 1 — same lyric.
- "The Nations" lyrics are still being tracked down — published with a
  placeholder until Chris locates them (try DistroKid "Plain lyrics" / Suno).
"""

# Reused lyric (track 1 and its remix, track 7).
_TWO_BOOKS_BLOCKS = [
    {"label": "Verse 1", "lines": [
        "Yo, look up at the Raki’a — that’s the sky, the expanse,",
        "the heavens recounting glory in a cosmic dance.",
        "It’s a narrative, a story that they telling us,",
        "not ontological but active and continuous.",
        "Day to day it gushes speech, pouring out the text,",
        "night to night declares the knowledge of what’s coming next.",
        "But check the frequency, there isn’t any sound heard —",
        "no speech, no language, not a single spoken word.",
        "It’s visual, a silent voice across the earth,",
        "universal broadcast announcing the worth.",
        "The sun is the bridegroom coming out the tent,",
        "like a strong man running races, energy is spent.",
        "Nothing hides from the heat, yeah, the coverage is global,",
        "a rudimental knowledge for the peasant and the noble.",
        "But wait — Heisenberg said it, take a sip of the science:",
        "first gulp turns you atheist, forming an alliance",
        "with naturalism — but drink it to the bottom of the glass,",
        "and God is waiting there when the skepticism pass.",
        "This is General Revelation, distinct from the specific:",
        "God reveals His nature, yeah, the view is terrific.",
        "But nature can’t save you, it’s only the foundation,",
        "insufficient for the healing of a broken nation.",
    ]},
    {"label": "Hook", "lines": [
        "The world is the theater, the Word is the script,",
        "General Revelation, yeah, the mystery is ripped.",
        "But we need the Special, the specific intervention,",
        "to rescue humanity from the sinful dimension.",
        "Creation speaks the power, Scripture speaks the grace —",
        "two different ways that we seeing His face.",
    ]},
    {"label": "Verse 2", "lines": [
        "Now switch the lens, zoom in, we getting precise:",
        "General is the broad view, Special is the price.",
        "The Enlightenment critics tried to view it with suspicion,",
        "downplaying the divine to elevate the human vision.",
        "But we need the Incarnation, the Word made flesh,",
        "Jesus in the history, making it fresh.",
        "See, the Torah of Yahweh is perfect and complete,",
        "restoring the soul, making the brokenness retreat.",
        "The testimony is sure, making the simple wise,",
        "commandments are pure, enlightening the eyes,",
        "more desirable than gold, yeah, the finest of the fine,",
        "sweeter than the honey dripping right off the vine.",
        "Natural law is written on the heart, that’s a fact,",
        "but the noetic effect of sin made the mind crack.",
        "Our reasoning is distorted, we can’t see it clear,",
        "we need the Special Revelation to help us to steer.",
        "We got the Law of Nature based in creature-Creator relations,",
        "but the Gospel brings the covenant to all the generations.",
    ]},
    {"label": "Bridge", "lines": [
        "Who can discern his errors? Who can see the flaws,",
        "when we staring in the mirror breaking all the laws?",
        "Cleanse me from the hidden faults, the stuff I don’t see,",
        "the unintentional wandering away from Thee.",
        "Keep back your servant from the willful sin,",
        "don’t let ’em rule me, don’t let the pride begin.",
        "Then I’ll be blameless, innocent and free",
        "of the great transgression and the mutiny.",
    ]},
    {"label": "Outro", "lines": [
        "Let the words of my mouth, the meditation of my heart,",
        "be pleasing in your sight right from the start.",
        "Not just acceptable, like I passed a test,",
        "but pleasing, Lord, giving you my very best.",
        "Creation is the rock, redemption is the roll —",
        "Yahweh, my Rock and Redeemer of my soul.",
    ]},
]

_TWO_BOOKS_REFS = ["Psalm 19", "Romans 1:18–20", "Psalm 19:7–14"]

# Shared study layer for "2 Books" and its remix "Divergent Mix // 2 Books".
_TWO_BOOKS_AIDS = {
    "thesis": (
        "The heavens (book one) and Scripture (book two) both reveal God — "
        "creation speaks His power, Scripture speaks His grace — but only the "
        "second book can heal a broken nation."
    ),
    "facts": [
        ("Doctrine", "General & Special Revelation"),
        ("Anchor text", "Psalm 19 · Romans 1"),
        ("Form", "Boom-bap"),
        ("Voices", "—"),
    ],
    "moves": [
        {"label": "The cosmic broadcast", "text": "The heavens pour out speech with no words — a universal, silent voice; general revelation, terrific but insufficient (Psalm 19:1–6; Romans 1:20)."},
        {"label": "Heisenberg’s glass", "text": "“First gulp turns you atheist… but drink it to the bottom and God is waiting there” (Romans 1:19–21)."},
        {"label": "The Word made fresh", "text": "The Torah of Yahweh is perfect, reviving the soul; we still need the specific intervention — the Incarnation (Psalm 19:7–9; John 1:14)."},
        {"label": "Cleanse the hidden faults", "text": "The noetic effect of sin cracks our reasoning; so, “let the words of my mouth be pleasing” (Psalm 19:12–14)."},
    ],
    "terms": [
        {"term": "the “two books”", "gloss": "The classic image (Augustine, Francis Bacon, Belgic Confession Art. 2) of God’s two books: the book of nature (general revelation) and the book of Scripture (special revelation)."},
        {"term": "Heisenberg’s glass", "gloss": "A saying often attributed to physicist Werner Heisenberg: “The first gulp from the glass of natural science will make you an atheist, but at the bottom of the glass God is waiting for you.”"},
        {"term": "the Raki’a", "gloss": "Hebrew raqia — the “expanse” or firmament of Genesis 1 and Psalm 19:1, the sky that “declares the glory of God.”"},
        {"term": "the noetic effect of sin", "gloss": "The theological term (prominent in Reformed thought) for how sin damages the mind itself, so our reasoning about God is “distorted, we can’t see it clear.”"},
        {"term": "general vs. special revelation", "gloss": "The song’s spine: general revelation (creation, conscience) shows God’s nature to all; special revelation (Scripture, Christ) reveals saving grace."},
    ],
    "discussion": [
        "Both books reveal God, but only one saves. Why isn’t general revelation (nature, conscience) enough?",
        "The Heisenberg line says science taken halfway makes atheists, but taken all the way finds God. Have you seen that pattern?",
        "“The noetic effect of sin” — how does sin distort not just our wills but our very thinking about God?",
    ],
    "contemplation": [
        "When you look at the sky, do you actually hear the “silent voice” announcing God’s worth?",
        "Where has your reasoning about God been “distorted,” needing Scripture to help you steer?",
        "Could “let the words of my mouth… be pleasing” be your prayer today?",
    ],
}

ALBUM = {
    "title": "Shady’s Bach",
    "slug": "shadys-bach",
    "order": 5,
    "tagline": "Oswald Records · Lyrics & Scripture",
    "blurb": (
        "Bach fused with hip-hop — both father (J.S.) and son (C.P.E.) — under "
        "classical apologetics in an Eminem cadence: the two books of "
        "revelation, Aquinas’s First Mover, the new earth, and the meaning of "
        "“foreknown.”"
    ),
    "cover": "/assets/shadys-bach/cover.jpg",
    "audio_prefix": "shadys-bach",
    # Concrete & marble identity — cool charcoal, marble-white ink, chrome/steel accent.
    "theme": {
        "--bg": "#16181b",
        "--bg-2": "#1c1f23",
        "--surface": "#21252a",
        "--surface-2": "#2b3037",
        "--rule": "#3b424b",
        "--ink": "#f2f1ec",
        "--ink-soft": "#c8cace",
        "--ink-faint": "#878d95",
        "--green": "#6f8196",
        "--green-deep": "#4a5969",
        "--gold": "#b8c6d6",
        "--gold-deep": "#8fa0b3",
        "--link": "#b8c6d6",
        "--glow-a": "rgba(184,198,214,0.10)",
        "--glow-b": "rgba(111,129,150,0.07)",
    },
    "episode": {
        "order": 3,
        "title": "Shady's Bach — the whole album, sung and explained",
        "guid": "utr-shadys-bach-2026-07-22",
        "pubDate": "Fri, 17 Jul 2026 12:00:00 -0500",
        "duration": "26:01",
        "length": 37598275,
        "audio_url": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/shadys-bach.mp3",
        "image": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/shadys-bach-art.jpg",
        "summary": (
            "Shady's Bach played end to end — Bach fused with hip-hop, classical apologetics in an "
            "Eminem cadence — with a short spoken intro before every song. The two books of "
            "revelation, the sun's circuit to the unreached nations, the new earth renewed rather "
            "than annihilated, C.P.E. Bach's étude as a theology of formation, Aquinas's arguments "
            "for God, and the meaning of 'foreknown.'"
        ),
        "chapters": [
            ("0:00", "Intro — 2 Books"),
            ("0:54", "2 Books"),
            ("3:37", "Intro — The Nations"),
            ("4:23", "The Nations"),
            ("7:12", "Intro — How Much Is The Earf?"),
            ("8:00", "How Much Is The Earf?"),
            ("10:03", "Intro — Solfeggietto"),
            ("10:44", "Solfeggietto"),
            ("13:34", "A word from our sponsor — Providence Community Church"),
            ("13:52", "Intro — Shady's Bach"),
            ("14:33", "Shady's Bach"),
            ("17:51", "Intro — Prognostiko"),
            ("18:37", "Prognostiko"),
            ("21:36", "Intro — Divergent Mix // 2 Books"),
            ("22:13", "Divergent Mix // 2 Books"),
        ],
    },
}

SONGS = [
    {
        "num": 1,
        "title": "2 Books",
        "slug": "2-books",
        "about": (
            "The two books of revelation — the heavens (General Revelation) and "
            "Scripture (Special Revelation). Creation speaks the power; Scripture "
            "speaks the grace."
        ),
        **_TWO_BOOKS_AIDS,
        "kind": "verse",
        "blocks": _TWO_BOOKS_BLOCKS,
        "refs": _TWO_BOOKS_REFS,
    },
    {
        "num": 2,
        "title": "The Nations",
        "slug": "the-nations",
        "about": (
            "The missions sequel to “2 Books”: the sun’s circuit (general "
            "revelation) reaches everyone, but the unreached peoples still need "
            "the second book — they see the glory in the sky but haven’t heard "
            "the gospel."
        ),
        "thesis": (
            "The sun’s circuit reaches everyone (general revelation), but the "
            "unreached peoples still have only book one — they see the glory in "
            "the sky without hearing the gospel. So take the second book to every "
            "neighborhood."
        ),
        "facts": [
            ("Doctrine", "Missions · Revelation"),
            ("Anchor text", "Psalm 19:4 · Romans 10:13–15"),
            ("Form", "Missions anthem"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "The double view vs. book one", "text": "We have both books, but the nations only have the sky; the sun circuit hits everyone, no one exempt (Psalm 19:4; Romans 1:20)."},
            {"label": "Treated with contempt", "text": "6,000 people groups still unreached — “not by God but by us, because we haven’t said the word” (Romans 10:14)."},
            {"label": "Take the second book", "text": "To every neighborhood, campus to tribe, city to bush — a missionary mindset, a gospel push (Matthew 28:19; Romans 10:15)."},
            {"label": "Creating the thirst", "text": "The Psalm 19:14 prayer reprised: we play our part, the Bible the water, bringing home every lost son and daughter (Luke 15)."},
        ],
        "terms": [
            {"term": "“book one, not two”", "gloss": "Ties straight to “2 Books”: the nations have general revelation (the sky) but not special revelation (the gospel)."},
            {"term": "“the sun circuit”", "gloss": "Psalm 19:4–6 — the sun’s “circuit to the end” of the heavens; nothing is hidden from its heat, picturing general revelation’s global reach."},
            {"term": "“6,000 people groups”", "gloss": "A common missiological estimate of the world’s “unreached” peoples with little or no access to the gospel."},
            {"term": "“how will they hear without a preacher?”", "gloss": "Romans 10:14–15 — the engine of the song’s missionary push."},
            {"term": "“know there’s a creator, but don’t know if He is good”", "gloss": "The limit of general revelation: it reveals power and divinity (Romans 1:20) but not saving grace."},
        ],
        "discussion": [
            "The song says the nations are “treated with contempt, not by God but by us.” Is unreached-ness a failure of mission?",
            "General revelation tells people “there’s a creator but not if He is good.” Why does that make the gospel urgent, not optional?",
            "“From the campus to the tribe, from the city to the bush.” Who are the “nations” near you with only book one?",
        ],
        "contemplation": [
            "Do you have a “missionary mindset,” or do you keep the second book to yourself?",
            "Whom could you “say the word” to this week?",
            "Are you “creating the thirst that the Bible gives the water” in the people around you?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "We got the knowledge, we got the double view,",
                "but what about the nations who only have book one, not two?",
                "The sun circuit hits everybody, no one exempt,",
                "but 6,000 people groups are treated with contempt —",
                "not by God but by us, because we haven’t said the word.",
                "They see the glory in the sky, but the gospel isn’t heard.",
                "They know there’s a creator, but don’t know if He is good.",
            ]},
            {"label": "Hook", "lines": [
                "We gotta take the second book to every neighborhood,",
                "from the campus to the tribe, from the city to the bush.",
                "We need a missionary mindset, a gospel push.",
                "The first book you need to know.",
            ]},
            {"label": "Outro", "lines": [
                "Let the words of my mouth and meditation of my heart",
                "be acceptable to you as we play our part",
                "in creation, creating the thirst that the Bible gives the water,",
                "bringing home every lost son and every lost daughter.",
            ]},
        ],
        "refs": ["Psalm 19:4", "Romans 10:13–15", "Romans 1:18–21", "Matthew 28:19", "Revelation 7:9", "Psalm 19:14"],
    },
    {
        "num": 3,
        "title": "How Much Is The Earf?",
        "slug": "how-much-is-the-earf",
        "about": (
            "Not annihilation but renovation — 2 Peter’s “melting” is "
            "purification, and we’re the earth-renewal taskforce preparing for "
            "the New Heaven and New Earth."
        ),
        "thesis": (
            "The end isn’t annihilation but renovation — 2 Peter’s “melting” means "
            "purification, not a cosmic trash bin. God is renewing the earth and "
            "the nations, and we’re the earth-renewal taskforce."
        ),
        "facts": [
            ("Doctrine", "Eschatology · New creation"),
            ("Anchor text", "2 Peter 3:10–13 · Revelation 21"),
            ("Form", "Conscious hip-hop"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "Translation twist", "text": "“Burn to a crisp” misreads 2 Peter; the word means stripped and exposed, not erased (2 Peter 3:10)."},
            {"label": "Purification, not annihilation", "text": "Melting the rot to heal the foundation — holy renovation, not divine frustration (2 Peter 3:13)."},
            {"label": "Bodies, not ghosts", "text": "Philippians 3: a body like Christ’s, risen and proud; He ate the fish and the honeycomb (Philippians 3:20–21; Luke 24:42–43)."},
            {"label": "Heaven comes down", "text": "Revelation 21: the city descends, God with His people, every tear wiped; we’re the taskforce preparing the ground (Revelation 21:1–4)."},
        ],
        "terms": [
            {"term": "“burn to a crisp” vs. “translation twist”", "gloss": "2 Peter 3:10: many translations read the earth will be “burned up,” but key manuscripts read heurethēsetai — “will be found / laid bare.” Exposed, not annihilated."},
            {"term": "annihilation vs. renovation", "gloss": "The debate over whether the present cosmos is destroyed and replaced, or purified and renewed. The song argues renewal (Romans 8:21)."},
            {"term": "“float like a ghost in the clouds”", "gloss": "A pushback on the disembodied-heaven idea (cf. “Solid Ground” on Roots of Reason); Philippians 3:21 promises a transformed body."},
            {"term": "“ate the fish, ate honeycomb”", "gloss": "The risen Jesus eating before the disciples (Luke 24:41–43) — proof of a physical resurrection."},
            {"term": "“making every enemy a footstool”", "gloss": "Psalm 110:1, the present reign of Christ behind “He reigns right now.”"},
        ],
        "discussion": [
            "Does it change anything to picture the future as a renewed earth rather than an escape to the clouds?",
            "“He’s renewing the earth and the nations.” How should that shape how Christians treat creation and culture now?",
            "If we’re the “earth-renewal taskforce,” what does “preparing the ground” look like in practice?",
        ],
        "contemplation": [
            "Have you pictured heaven as “floating like a ghost”? How does a bodily resurrection change your hope?",
            "The curse is being reversed, “every fractured part.” Where do you long to see that?",
            "What would it mean to live as part of the “taskforce” today?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "I got a text to decode, gotta lighten the load,",
                "blowin’ up myths that you’ve usually told",
                "about the end of the world, how the story unfolds —",
                "it isn’t a bomb or a nuclear cold.",
                "You heard the preacher say it’s gonna burn to a crisp,",
                "but Second Peter flips the script — translation twist.",
                "The word don’t mean erased, don’t mean abyss,",
                "it means stripped and exposed — don’t miss this.",
            ]},
            {"label": "Chorus", "lines": [
                "It isn’t annihilation, it’s purification,",
                "melting down the rot to heal the foundation.",
                "God ain’t scrapping the plan of creation,",
                "He’s renewing the earth and the nations.",
                "Not a cosmic trash bin, not divine frustration —",
                "it’s repair, restore, holy renovation.",
            ]},
            {"label": "Verse 2", "lines": [
                "You ain’t gonna float like a ghost in the clouds,",
                "Philippians Three says it clear and loud:",
                "we get a body like Christ, risen and proud,",
                "no funeral shroud, no drifting around.",
                "Jesus stood up with flesh and bone,",
                "asked for the fish, ate honeycomb.",
                "If he’s embodied, seated on the throne,",
                "then we won’t be spirits when we’re finally home.",
            ]},
            {"label": "Verse 3", "lines": [
                "Heaven ain’t up, it’s coming down here,",
                "Revelation Twenty-One makes the vision clear:",
                "the city descends, the people cheer,",
                "God with His people, every wiped tear.",
                "Renovated planet, not a brand-new start,",
                "restoring the world to the Father’s heart.",
                "Curse reversed, every fractured part,",
                "saints and the Savior — never apart.",
            ]},
            {"label": "Bridge", "lines": [
                "So why the delay? Why the wait?",
                "He reigns right now, ruling the state,",
                "making every enemy a footstool laid,",
                "turning foes to sons before Judgment Day.",
                "That’s commission, that’s patient grace,",
                "gathering sheep from every place.",
            ]},
            {"label": "Outro", "lines": [
                "We’re the earth-renewal taskforce, called by His name,",
                "Spirit in the heart, fanning the flame,",
                "preparing the ground for the Kingdom claim —",
                "New Heaven, New Earth — it’s the ultimate aim.",
            ]},
        ],
        "refs": ["2 Peter 3:10–13", "Philippians 3:20–21", "Revelation 21:1–4", "Acts 3:21", "Psalm 110:1"],
    },
    {
        "num": 4,
        "title": "Solfeggeitto",
        "slug": "solfeggeitto",
        "about": (
            "A reprise of the Proverbs cut — C.P.E. Bach’s finger-exercise as a "
            "theology of formation: no shortcuts to glory; you’re refined over "
            "time."
        ),
        "thesis": (
            "C.P.E. Bach’s finger-exercise becomes a theology of formation: there "
            "are no shortcuts into glory — you’re refined over time, every scale a "
            "prayer, the practice room shaping eternity’s tempo."
        ),
        "facts": [
            ("Doctrine", "Sanctification · Perseverance"),
            ("Anchor text", "Romans 2:6–8 · Galatians 6:9"),
            ("Form", "Baroque-trap"),
            ("Voices", "C.P.E. Bach"),
        ],
        "moves": [
            {"label": "Get to work-O", "text": "“Solfeggietto” is a keyboard exercise for dexterity — but the idea “carries farther into eternity.”"},
            {"label": "Nursery and harvest", "text": "This world is the nursery where we plant our seeds; the next is where the harvest reads (Galatians 6:7–9)."},
            {"label": "No shortcuts", "text": "You don’t stumble into glory — you’re refined over time; the sweat is the sacrament, the labor the liturgy (Romans 5:3–4)."},
            {"label": "Grace and effort", "text": "Grace isn’t opposed to effort, it’s opposed to the flex; we grind in the minor to rejoice in the major (Philippians 2:12–13)."},
        ],
        "terms": [
            {"term": "Solfeggietto", "gloss": "A finger-twisting keyboard étude in C minor by Carl Philipp Emanuel Bach — son of J.S. Bach — built almost entirely from racing scales and arpeggios. (Also appears on the Proverbs album.)"},
            {"term": "“little Bach Jr.”", "gloss": "C.P.E. Bach, drilled by his father; the cramping fingers and callouses become a parable of slow formation."},
            {"term": "“the practice room… the stage”", "gloss": "The song’s controlling frame: this life is rehearsal, the next is the performance."},
            {"term": "“grace ain’t opposed to effort, it’s opposed to the flex”", "gloss": "A line associated with Dallas Willard: “grace is not opposed to effort, it is opposed to earning.”"},
            {"term": "“render to each according to his works”", "gloss": "The spoken outro quotes Romans 2:6–8 verbatim — patient well-doing rewarded with eternal life."},
        ],
        "discussion": [
            "“No shortcuts coded into the moral design.” Where do we look for spiritual shortcuts?",
            "Willard’s idea — grace opposes earning, not effort. How do people confuse the two?",
            "The song calls boring repetition “forging fidelity.” What unglamorous practice is forming you right now?",
        ],
        "contemplation": [
            "What “scales” is God asking you to practice in the dark, where no one sees?",
            "Are you trying to “stumble into glory” rather than be refined over time?",
            "Is your effort an attempt to earn, or a response to grace?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": None, "lines": [
                "Solfeggietto,",
                "an Italian word",
                "for “get to work-O.”",
                "It’s a keyboard exercise",
                "for dexterity,",
                "but that idea carries farther",
                "into eternity.",
            ]},
            {"label": None, "lines": [
                "You see, this world is a nursery",
                "where we plant our seeds,",
                "and the next world to come",
                "is where the harvest reads.",
                "This world ain’t the place",
                "just to coast along,",
                "’cause this life’s short",
                "and the next one’s long.",
            ]},
            {"label": None, "lines": [
                "When little Bach Jr. sat down at the keys,",
                "his dad made him practice well beyond his ease.",
                "His fingers would cramp",
                "and callouses formed,",
                "but the end result lived",
                "way outside the norm.",
            ]},
            {"label": None, "lines": [
                "No shortcuts coded in",
                "to the moral design.",
                "You don’t stumble into glory —",
                "you’re refined over time.",
                "Every scale is a prayer,",
                "every miss is a plea,",
                "every hour in the dark",
                "is eternity’s seed.",
            ]},
            {"label": None, "lines": [
                "The sweat is the sacrament,",
                "the labor the liturgy.",
                "Formation feels boring,",
                "but it’s forging fidelity.",
                "You don’t drift into virtue —",
                "you rehearse it slow.",
                "Heaven hears every rep",
                "in the SOL-FE-GE-O.",
            ]},
            {"label": None, "lines": [
                "Grace ain’t opposed to effort,",
                "it’s opposed to the flex.",
                "It don’t cancel the work,",
                "it redeems what’s next.",
                "So we grind in the minor",
                "to rejoice in the major.",
                "This life is the practice room,",
                "the next one’s the stage, sir.",
            ]},
            {"label": None, "lines": [
                "SOL-FE-GE-O,",
                "hear the doctrine echo.",
                "Little exercises now",
                "shape forever’s tempo.",
            ]},
            {"label": "Spoken Outro", "lines": [
                "He will render to each one according to his works: to those who by patience in well-doing seek for glory and honor and immortality, He will give eternal life; but for those who are self-seeking and do not obey the truth, but obey unrighteousness, there will be wrath and fury.",
            ]},
        ],
        "refs": ["Romans 2:6–8", "Proverbs 13:4", "Galatians 6:9"],
    },
    {
        "num": 5,
        "title": "Shady’s Bach",
        "slug": "shadys-bach",
        "about": (
            "Aquinas’s cosmological arguments as an Eminem parody — “will the "
            "real First Mover please stand up?” The Unmoved Mover, the First "
            "Cause, the Necessary Being, the Maximum Perfection: we call Him God."
        ),
        "thesis": (
            "Aquinas’s cosmological arguments rapped as an Eminem parody — “will "
            "the real First Mover please stand up?” Motion, causation, "
            "contingency, and degrees of perfection all point past themselves to "
            "one uncaused, necessary, maximal Being: we call Him God."
        ),
        "facts": [
            ("Doctrine", "Natural theology · Apologetics"),
            ("Anchor text", "Romans 1:20 · Acts 17"),
            ("Form", "Eminem-parody battle rap"),
            ("Voices", "Thomas Aquinas"),
        ],
        "moves": [
            {"label": "The First Way — motion", "text": "Everything that moves was moved by another; no infinite regress, so there must be an Unmoved Mover (Acts 17:28)."},
            {"label": "The Second Way — causation", "text": "Every effect has a cause; nothing causes itself; so there must be a First Cause, uncaused (Romans 1:20)."},
            {"label": "The Third Way — contingency", "text": "Contingent things might not exist; if all were contingent, nothing would be; so there must be a Necessary Being (Exodus 3:14)."},
            {"label": "The Fourth Way — degrees", "text": "We see degrees of good, true, and beautiful; that implies a maximum, the source of all perfection (James 1:17). “We call Him God.”"},
        ],
        "terms": [
            {"term": "Aquinas’s Five Ways", "gloss": "Thomas Aquinas (1225–1274), in the Summa Theologica, offered five logical arguments for God’s existence; the song raps four — motion, causation, contingency, and degrees of perfection."},
            {"term": "“will the real First Mover please stand up?”", "gloss": "A parody of Eminem’s “The Real Slim Shady” (“will the real Slim Shady please stand up?”), with the album title punning on Slim Shady + Bach."},
            {"term": "the Unmoved Mover", "gloss": "The First Way’s conclusion (and Aristotle’s term): the source of all motion that is not itself moved."},
            {"term": "the Necessary Being", "gloss": "The Third Way: a being whose existence is essential, not contingent — sustaining everything that “might not exist.” It echoes God’s self-naming “I AM” (Exodus 3:14)."},
            {"term": "Maximum Being / summum bonum", "gloss": "The Fourth Way: degrees of perfection imply a maximum, the cause of all goodness, truth, and beauty — “the Father of lights” (James 1:17)."},
        ],
        "discussion": [
            "Aquinas argues from the world (motion, cause, contingency) up to God. How do these “from creation” arguments complement faith in Scripture?",
            "The song ends “metaphysical nature, not just faith in the dark.” Fair balance, or does it overstate what reason can prove?",
            "Which of the four “ways” do you find most compelling, and why?",
        ],
        "contemplation": [
            "When you trace any chain — of motion, cause, or being — back far enough, do you arrive at God?",
            "“We call Him God.” Is the God of the arguments the God you actually worship?",
            "Where do you need “logic that makes it plain” to steady a wavering faith?",
        ],
        "attribution": {
            "text": (
                "Riffs on Thomas Aquinas’s “Five Ways” (four of them here) from "
                "the Summa Theologica, in the cadence of Eminem’s “The Real Slim "
                "Shady.”"
            ),
            "links": [
                ("About Aquinas’s Five Ways", "https://en.wikipedia.org/wiki/Five_Ways_(Aquinas)"),
            ],
        },
        "kind": "verse",
        "blocks": [
            {"label": "Intro", "lines": [
                "Will the real First Mover please stand up?",
                "I said, will the real First Mover please stand up?",
                "Atheists gonna have a problem in here.",
            ]},
            {"label": "First Way — Motion", "lines": [
                "I’m coming at you via a classical lane:",
                "four ways to see why there’s a God via logic that makes it plain.",
                "I’m locking in the First Way, listen to the motion sway —",
                "everything moves ’cause a mover pushed it into play.",
                "Nothing moves itself, nah, that’s a logical health hazard,",
                "check the physics, nothing is its own master.",
                "But hold up, wait a minute, look at the chain:",
                "you can’t have an infinite regress inside of the brain.",
                "No infinite chain of movers causing the spin,",
                "you need a spot where the motion has gotta begin.",
                "Unmoved itself, initiating the pace —",
                "that’s the First Mover, God, the uncaused cause of space.",
            ]},
            {"label": "Second Way — Causation", "lines": [
                "Switch gears, Second Way, efficient causality:",
                "every effect has a cause in this reality.",
                "Nothing causes itself, that’s a logical crime —",
                "you’d have to exist before your own start time.",
                "Can’t be an infinite list of the causes in line,",
                "or the first cause is gone, and the others decline.",
                "So we strip it back, attack the track, no flaw:",
                "there must be a First Cause, uncaused, raw.",
                "Source of all causation, the boss of the station —",
                "God is the name of this foundation.",
            ]},
            {"label": "Third Way — Contingency", "lines": [
                "Third Way, check the mic, is it on? Possibility.",
                "Things in the world got a contingency liability,",
                "meaning they might not exist, yeah, they contingent —",
                "here today, gone tomorrow, survival is stringent.",
                "If everything was contingent, snap, back to the past,",
                "there’d be a time when nothing existed, nothing would last.",
                "And if nothing was there, then nothing would be here right now —",
                "but we exist, so wipe the sweat off your brow.",
                "There must be a Necessary Being, not a “maybe” or “might,”",
                "whose existence is essential, burning ever so bright.",
                "Sustaining the contingent, keeping atoms in check —",
                "Necessary Being is God, put respect on the deck.",
            ]},
            {"label": "Fourth Way — Degrees of Perfection", "lines": [
                "Fourth Way, Shady’s Bach is back, degrees of the best:",
                "we see the good, true, and beautiful put to the test.",
                "Varying degrees implies a standard, a height —",
                "a maximum perfection shining blindingly bright.",
                "Most good, most true, the cause of the quality,",
                "Maximum Being, defining the morality.",
                "Source of all perfections, the standard, the rod —",
                "that maximum being?",
            ]},
            {"label": "Hook", "lines": [
                "We call Him God.",
                "We call Him God.",
                "We call Him God.",
            ]},
            {"label": "Outro", "lines": [
                "Yeah. Metaphysical nature, not just faith in the dark —",
                "observations of the world leaving a logical mark.",
                "C.P.E. Bach, fade it out. Thomas Aquinas. Summa Theologica. I’m out.",
            ]},
        ],
        "refs": ["Romans 1:20", "Acts 17:24–28", "Exodus 3:14", "Hebrews 1:3"],
    },
    {
        "num": 6,
        "title": "Prognostiko",
        "slug": "prognostiko",
        "about": (
            "The Greek proginōskō (“foreknow”) isn’t God peeking down the "
            "corridor of time — it’s covenant love set on a people before the "
            "world began. To be foreknown is to be fore-loved."
        ),
        "thesis": (
            "The Greek proginōskō (“foreknow”) isn’t God peeking down the corridor "
            "of time to see what you’d do — it’s covenant love set on a person "
            "before the world began. To be foreknown is to be fore-loved."
        ),
        "facts": [
            ("Doctrine", "Election · Foreknowledge"),
            ("Anchor text", "Romans 8:29 · 1 Peter 1:20"),
            ("Form", "Didactic boom-bap"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "Define the Greek", "text": "Proginōskō isn’t foresight or a scan of the future; it’s the whom, not the what (Romans 8:29)."},
            {"label": "“You only have I known”", "text": "Amos 3:2 and Christ “foreknown before the foundation” prove foreknowledge means set love, not data (Amos 3:2; 1 Peter 1:20)."},
            {"label": "Not a reaction to the man", "text": "If God merely foresaw your faith, grace becomes a response — reversing the order (Romans 9:16)."},
            {"label": "Five times, always personal", "text": "Romans 8:29, 11:2, 1 Peter 1:2: He foreknew people; “to be foreknown is to be fore-loved” (Romans 11:2)."},
        ],
        "terms": [
            {"term": "proginōskō", "gloss": "The Greek verb usually translated “foreknow.” The song argues it carries the Hebrew sense of “know” as covenant intimacy (yada), not bare prediction."},
            {"term": "“You only have I known”", "gloss": "Amos 3:2 — God obviously had data on every nation, so “known” here means specially chosen and loved. The key to reading “foreknow.”"},
            {"term": "“Christ foreknown before the foundation”", "gloss": "1 Peter 1:20 — Christ wasn’t merely foreseen but foreordained, which fixes the word’s meaning for believers too."},
            {"term": "“the corridor of time”", "gloss": "The view (often called prescient or Arminian) that God elects based on foreseeing who would believe; the song argues this “reverses the order” of grace."},
            {"term": "“not of him who wills or runs”", "gloss": "Romans 9:16 — “but of God who shows mercy.” The song’s hammer-line against grace as a reaction to the creature."},
        ],
        "discussion": [
            "The song hangs everything on one Greek word. Why does “know” so often mean “set love on” in Scripture (Adam “knew” Eve; “I never knew you”)?",
            "“If God just foresaw your faith…” — how does that “reverse the order” of grace? Does it matter pastorally?",
            "Romans 9:16 says mercy isn’t “of him who wills or runs.” How do you hold that together with human responsibility?",
        ],
        "contemplation": [
            "Does it change anything to hear that you were “fore-loved,” not merely foreseen?",
            "Is your assurance built on your faith, or on the love that “appointed you”?",
            "Sit with “affection set, grace met.” What does it mean that God set His love on you first?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "Listen to the Greek, gotta get the definition right:",
                "proginōskō isn’t vision, isn’t foresight, isn’t sight.",
                "It is never mere awareness of a human decision,",
                "it is covenantal love, it is sovereign precision.",
                "It’s the whom, not the what — check the text, Romans 8,",
                "not a scan of the potential or the merit or the fate.",
                "Paul didn’t say He saw the faith that you would show,",
                "he said He knew the person — that’s the way the blessings flow.",
                "It’s a relationship, a bond, distinct and divine,",
                "not a gathering of facts from the end of the line.",
            ]},
            {"label": "Verse 2", "lines": [
                "Go to Amos 3:2, see the families of the earth:",
                "“You only have I known” — is that a lack of data’s worth?",
                "Does He lack the information on the pagan and the lost?",
                "No, it means He set His love, and He covered up the cost.",
                "Now look at 1st Peter, chapter 1, verse 20:",
                "Christ was foreknown, and the proof is plenty.",
                "Did the Father look ahead? Did He wait? Did He see",
                "what the Son would go and do? Was it probability?",
                "No! He ordained Him! He appointed the Son!",
                "Before the world began, the redeeming work was done.",
                "So if Christ was foreknown as the Plan and the Way,",
                "then foreknowledge is the choice, not a scan of the day.",
            ]},
            {"label": "Verse 3", "lines": [
                "If you think He looked down the corridor of time",
                "just to see if you believed, then you minimize the Prime.",
                "That makes the grace a response, a reaction to the man,",
                "conditioned on the creature — that is not the Master Plan.",
                "That reverses the order, undermines the decree,",
                "shifts the cause from the Lord to the will of you and me.",
                "But Romans 9:16 cuts the pride with a knife:",
                "not of him that wills or runs, but the Lord of Life.",
                "Mercy is the source, it is not the result",
                "of a foreseen action in the human adult.",
            ]},
            {"label": "Verse 4", "lines": [
                "Five times in the text, let me run it, let me flex:",
                "Romans 8:29, knowing people — that’s the specs.",
                "Romans 11:2, Israel’s not cast away,",
                "He foreknew the people, relational display.",
                "1 Peter 1:2, the elect, the select,",
                "according to the knowledge that the Father will project.",
                "It is never an event! It is never just a fact!",
                "It is never just a decision that He watches us enact.",
                "It is always the person! It is redemptive context!",
                "It is setting affection — no need to be perplexed.",
            ]},
            {"label": "Bridge", "lines": [
                "To be foreknown is to be fore-loved!",
                "Initiated from the throne above!",
                "Not a data mine, not a sterile view,",
                "but the sovereign grace that appointed you.",
            ]},
            {"label": "Tag", "lines": [
                "Proginōskō.",
                "Affection set.",
                "Grace met.",
                "Stop.",
            ]},
        ],
        "refs": ["Romans 8:29", "Amos 3:2", "1 Peter 1:20", "1 Peter 1:2", "Romans 11:2", "Romans 9:16"],
    },
    {
        "num": 7,
        "title": "Divergent Mix // 2 Books",
        "slug": "divergent-mix-2-books",
        "about": (
            "A divergent remix of “2 Books” — same two-books theme (the heavens "
            "and the Scripture), different groove."
        ),
        **_TWO_BOOKS_AIDS,
        "kind": "verse",
        "blocks": _TWO_BOOKS_BLOCKS,
        "refs": _TWO_BOOKS_REFS,
    },
]
