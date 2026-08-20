# -*- coding: utf-8 -*-
"""
Proverbs — album data.

Comic, ’80s-pop-culture-soaked rides through the book of Proverbs. Lyrics
reformatted from ProVerbs Lyrics.md: production directions dropped, section
labels kept, the run-on "Plastic Love" text broken back into stanzas.

NancyPlease is a deliberate throwaway — per Chris, no exegesis or teaching
aids, just a note. (It's the 27-second "Double Pleasey / Nacho Cheesy" bit.)
"""

ALBUM = {
    "title": "Proverbs",
    "slug": "proverbs",
    "order": 4,
    "tagline": "Uncle Theology · Lyrics & Scripture",
    "blurb": (
        "The book of Proverbs as a comic-book romp — friendship and folly, the "
        "ant and the sluggard, antithetic parallelism as an ’80s action movie, "
        "and Agur’s prayer for neither riches nor poverty."
    ),
    "cover": "/assets/proverbs/cover.jpg",
    "audio_prefix": "proverbs",
    # Comic-collage identity — warm dark olive, golden ochre + olive green.
    "theme": {
        "--bg": "#12130c",
        "--bg-2": "#181a10",
        "--surface": "#1f2114",
        "--surface-2": "#282b1a",
        "--rule": "#3b3e28",
        "--ink": "#f6f1e2",
        "--ink-soft": "#d7d3bd",
        "--ink-faint": "#979577",
        "--green": "#8a9e42",
        "--green-deep": "#5f7030",
        "--gold": "#e8a93a",
        "--gold-deep": "#bf852a",
        "--link": "#e8a93a",
        "--glow-a": "rgba(232,169,58,0.13)",
        "--glow-b": "rgba(138,158,66,0.08)",
    },
    "episode": {
        "order": 4,
        "title": "Proverbs — the whole album, sung and explained",
        "guid": "utr-proverbs-2026-07-22",
        "pubDate": "Sat, 18 Jul 2026 12:00:00 -0500",
        "duration": "34:58",
        "length": 50570287,
        "audio_url": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/proverbs.mp3",
        "image": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/proverbs-art.jpg",
        "summary": (
            "Proverbs played end to end — the book of Proverbs as a comic-book romp — with a short "
            "spoken intro before every song. Wisdom you have to eat daily, the friends you choose, "
            "Agur's prayer for neither riches nor poverty, antithetic parallelism as an '80s action "
            "movie, the ant and the sluggard, the quiet diligence Proverbs praises, and Lady Folly's "
            "counterfeit love."
        ),
        "chapters": [
            ("0:00", "Intro — Ready To Go Pro"),
            ("0:56", "Ready To Go Pro"),
            ("3:36", "Intro — Friends You Choose"),
            ("4:18", "Friends You Choose"),
            ("8:53", "Intro — Neither Rich Nor Poor"),
            ("9:34", "Neither Rich Nor Poor"),
            ("13:37", "Intro — Ultimate Showdown"),
            ("14:19", "Ultimate Showdown"),
            ("17:00", "Intro — Solfeggietto"),
            ("17:35", "Solfeggietto"),
            ("20:04", "A word from our sponsor — Providence Community Church"),
            ("20:22", "Intro — Clean or Die"),
            ("21:03", "Clean or Die"),
            ("24:09", "Intro — Squeaky Wheel"),
            ("24:45", "Squeaky Wheel"),
            ("29:02", "Intro — NancyPlease"),
            ("29:26", "NancyPlease"),
            ("29:54", "Intro — Plastic Love"),
            ("30:40", "Plastic Love"),
        ],
    },
}

SONGS = [
    {
        "num": 1,
        "title": "Ready To Go Pro",
        "slug": "ready-to-go-pro",
        "about": (
            "A fifties dad’s origin story — mixtapes, BMX, and Adderall to a man "
            "finally “ready to go PRO VERBS,” passing on hard-won wisdom in cheesy "
            "songs."
        ),
        "thesis": (
            "A midlife dad turns from a loud, insecure know-it-all into a man "
            "finally “ready to go PRO VERBS” — because wisdom, like food, has to "
            "be eaten every single day."
        ),
        "facts": [
            ("Doctrine", "Wisdom · Discipleship"),
            ("Anchor text", "Proverbs 1:1–7"),
            ("Form", "Nostalgic boom-bap"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "The ’80s kid", "text": "Mixtapes, BMX, Zelda, “they said I needed Adderall” — loud but insecure, strutting like an amateur."},
            {"label": "Wisdom is exuding", "text": "In his fifties now: the body fades but wisdom grows — gray hair as a crown found in righteousness (Proverbs 16:31)."},
            {"label": "Eat them every day", "text": "Like the Gauntlet wizard needing the turkey leg, you gotta eat the proverbs daily; a price is paid (Proverbs 4:7)."},
            {"label": "Protein, not cotton candy", "text": "What he chased was “cotton candy empty space”; wisdom is a protein shake of truth and grace (Proverbs 1:7)."},
        ],
        "terms": [
            {"term": "the purpose of Proverbs", "gloss": "Proverbs 1:1–7 states the book’s aim — prudence for the simple, knowledge for the young — and its motto: “the fear of the LORD is the beginning of knowledge.”"},
            {"term": "“Gauntlet… wizard… turkey leg”", "gloss": "The 1985 arcade game Gauntlet, where a character’s strength drained over time and was refilled by on-screen food (the famous “Wizard needs food badly”) — the song’s picture of needing wisdom daily."},
            {"term": "Nestlé · VHS · Zelda · BMX", "gloss": "’80s childhood markers that ground the dad’s testimony in a specific generation."},
            {"term": "“wisdom is exuding… belly is protruding”", "gloss": "A wink at Proverbs 16:31 — gray hair (and age) as “a crown of glory” gained in the way of righteousness."},
            {"term": "“PRO VERBS”", "gloss": "The pun the whole album hangs on: “ready to go pro” (turn professional) = ready to actually live the book of Proverbs."},
        ],
        "discussion": [
            "The song treats wisdom like food eaten daily, not a trophy won once. How does that reframe spiritual growth?",
            "He spent his youth “strutting like an amateur.” Where does insecurity hide behind loudness?",
            "What’s the difference between “cotton candy” pursuits and “protein” ones in your life?",
        ],
        "contemplation": [
            "What “cotton candy empty space” have you been chasing?",
            "Are you eating wisdom daily, or running on fumes?",
            "What would “going pro” — actually living the Proverbs — look like for you this week?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "I grew up on mixtapes, BMX and wrestling,",
                "VHS and Zelda, all my milk was Nestlé.",
                "Now I’m in my fifties, belly is protruding,",
                "hairline is receding, but wisdom is exuding.",
                "Way back when I knew it all, they said I needed Adderall —",
                "I was loud but insecure, strutting like an amateur.",
            ]},
            {"label": "Chorus", "lines": [
                "But now I’m ready to go PRO VERBS!",
                "Got some smarts although my back hurts.",
                "Now I’m ready to pass them on",
                "in the form of cheesy songs.",
                "Nacho typical dad move,",
                "but where I go I bring the groove.",
            ]},
            {"label": "Verse 2", "lines": [
                "Saturdays spent in the arcade,",
                "Gauntlet wizard strength would fade",
                "until he ate a turkey leg.",
                "These PRO VERBS work in the same way —",
                "you gotta eat them every day,",
                "get God’s wisdom, a price is paid.",
                "They work like friendship bracelet braids.",
                "All the stuff I used to chase was cotton candy empty space,",
                "but wisdom’s like a protein shake, it makes you strong with truth and grace.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "Way back when I knew it all, they said I needed Adderall,",
                "chasing all the devil’s lures, strutting like an amateur.",
            ]},
            {"label": "Chorus", "lines": [
                "But now I’m ready to go PRO VERBS!",
                "Got some smarts although my back hurts.",
                "Now I’m ready to pass them on",
                "in the form of cheesy songs.",
                "Not your typical dad move,",
                "but where I go I bring the groove.",
            ]},
            {"label": "Outro", "lines": [
                "All the stuff I used to chase was cotton candy empty space,",
                "but wisdom’s like a protein shake, it makes you strong with truth and grace.",
            ]},
        ],
        "refs": ["Proverbs 1:1–7", "Proverbs 4:7", "Proverbs 9:9"],
    },
    {
        "num": 2,
        "title": "Friends You Choose",
        "slug": "friends-you-choose",
        "about": (
            "Proverbs’ first lesson — the company you keep shapes where your "
            "story ends; and the family you didn’t choose helps you choose the "
            "friends you do."
        ),
        "thesis": (
            "Proverbs’ first lesson is the company you keep — run with fools and "
            "break, walk with the wise and rise; and the family you didn’t choose "
            "is meant to help you choose the friends you do."
        ),
        "facts": [
            ("Doctrine", "Wisdom · Friendship · Family"),
            ("Anchor text", "Proverbs 13:20 · 1:8–19"),
            ("Form", "Coming-of-age rap"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "The wrong crowd looks cool", "text": "At thirteen the rule-breakers looked like the embodiment of cool — till Proverbs “read me like a bio” (Proverbs 1:10–19)."},
            {"label": "Walk with the wise", "text": "Run with fools and you’ll be broken; walk with the wise and you’ll ascend (Proverbs 13:20)."},
            {"label": "Standard-issue family", "text": "The friends you didn’t choose — parents, siblings — had the vantage to protect you from the goofs (Proverbs 1:8)."},
            {"label": "Faithful wounds", "text": "Real friends sharpen, they don’t dull you; “better honest wounds than sweet pretend” (Proverbs 27:6, 17)."},
        ],
        "terms": [
            {"term": "“walk with the wise / companion of fools”", "gloss": "Proverbs 13:20, the song’s backbone: “whoever walks with the wise becomes wise, but the companion of fools will suffer harm.”"},
            {"term": "“faithful are the wounds of a friend”", "gloss": "Proverbs 27:6 — “better honest wounds than sweet pretend”; the friend’s honest wound vs. the enemy’s profuse kisses."},
            {"term": "“iron sharpens iron”", "gloss": "Proverbs 27:17, behind “real friends sharpen, never dull you.”"},
            {"term": "“my son, hear… do not walk with them”", "gloss": "Proverbs 1:8–19 — the father’s opening plea against being enticed by bad company."},
            {"term": "“ride-or-dies went zero”", "gloss": "The fair-weather friend exposed the moment trouble comes (cf. Proverbs 18:24)."},
        ],
        "discussion": [
            "The song says the friends you didn’t choose (family) help you choose the ones you do. How has that worked — or not — in your story?",
            "“Better honest wounds than sweet pretend.” When did a friend’s hard truth help you? When have you withheld one?",
            "How do you tell a “ride-or-die” from a fair-weather friend before the storm hits?",
        ],
        "contemplation": [
            "Who are you “walking with” — and where are they leading you?",
            "Is there a faithful wound you’ve been resenting that you should actually receive?",
            "Are you the kind of friend who sharpens, or one who just flatters?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "I was thirteen with a ratty backpack,",
                "Walkman headphones blasting track-by-track.",
                "Thought the kids who broke the rules",
                "were the embodiment of cool.",
                "But Proverbs read me like a bio,",
                "wisdom hit me like a ton of bricks:",
                "the wrong crowd’ll wreck your tomorrow —",
                "wisdom’s first lesson is simply this.",
            ]},
            {"label": "Chorus", "lines": [
                "The first lesson in the book",
                "is about choosing your friends —",
                "the ones you run with",
                "shape how your story ends.",
                "And the friends you didn’t choose",
                "(yeah, mom and dad came standard-issue),",
                "turns out the ones who raised you",
                "are the ones who help you choose",
                "who you let inside your ride,",
                "who you hand your keys to.",
            ]},
            {"label": "Hook", "lines": [
                "“Let the friends you didn’t choose",
                "help you choose the friends you do.”",
            ]},
            {"label": "Verse 2", "lines": [
                "I had bros who bragged like heroes,",
                "but vanished fast when the sky turned gray.",
                "All the “ride-or-dies” went zero",
                "soon as trouble came my way.",
                "But a real friend speaks with truth and grace,",
                "not two-face smiles when they walk away.",
                "Better honest wounds than sweet pretend —",
                "yeah, I learned that the harder way.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "Took years of falling on my face",
                "to see what Proverbs says is true:",
                "some friends will lead to your disgrace,",
                "a real one walks the storm with you.",
            ]},
            {"label": "Chorus", "lines": [
                "The first lesson in the book",
                "is about choosing your friends —",
                "run with fools and you’ll be broken,",
                "walk with wise and you’ll ascend.",
                "And the friends I didn’t choose",
                "(yeah, mom and dad are built-in proof),",
                "were the ones who had the vantage",
                "to protect me from the goofs —",
                "they knew better than I knew.",
            ]},
            {"label": "Hook", "lines": [
                "“Let the friends you didn’t choose",
                "help you choose the friends you do.”",
            ]},
            {"label": "Chorus", "lines": [
                "The first lesson in the book",
                "is about choosing your friends —",
                "the ones you run with",
                "shape how your story bends.",
                "And the ones I didn’t always feel",
                "(yeah, siblings are a package deal),",
                "they were rough around the edges,",
                "but they taught me what is real —",
                "who will stand beside your failures,",
                "who will love you when you’re blue.",
                "Use the brothers you were born with",
                "to pick the brothers you pursue.",
            ]},
            {"label": "Bridge", "lines": [
                "I’ve chased crowds that felt like safety",
                "till their masks lit up in flames.",
                "Had hype-men turn to strangers",
                "when they couldn’t get their way.",
                "But the wounds from someone faithful?",
                "That’s the forge that makes you true.",
                "Real friends sharpen — never dull you —",
                "iron cutting through the lies in you.",
            ]},
            {"label": "Final Chorus", "lines": [
                "The first lesson in the book",
                "is about choosing your friends —",
                "who you trust with your identity",
                "shapes the way your story ends.",
                "And the friends I didn’t choose",
                "were the compass God first used —",
                "to show me who is for my soul",
                "and who is just here to use.",
            ]},
            {"label": "Gang vocal", "lines": [
                "“Let the friends you didn’t choose",
                "help you choose the friends you do!”",
            ]},
            {"label": "Tag / Outro", "lines": [
                "Bad company kills slowly,",
                "but good friends make you strong.",
                "Proverbs wrote the warning,",
                "that I’m writing it in song.",
            ]},
        ],
        "refs": ["Proverbs 13:20", "Proverbs 1:8–19", "Proverbs 27:6", "Proverbs 27:17", "1 Corinthians 15:33"],
    },
    {
        "num": 3,
        "title": "Neither Rich Nor Poor",
        "slug": "neither-rich-nor-poor",
        "about": (
            "Agur’s prayer set to song — give me neither poverty nor riches, just "
            "daily bread, lest I forget the Lord or quit the race."
        ),
        "thesis": (
            "Agur’s prayer for the middle road — neither poverty nor riches, just "
            "daily bread — because too-easy reward makes me forget God, and "
            "too-slow reward makes me quit."
        ),
        "facts": [
            ("Doctrine", "Contentment · Providence"),
            ("Anchor text", "Proverbs 30:7–9"),
            ("Form", "Half-time soul"),
            ("Voices", "Agur"),
        ],
        "moves": [
            {"label": "Two failure modes", "text": "Too-easy reward, I squander it and feel I’ve “got it made”; too-slow, I lose heart and quit before I try (Proverbs 13:12)."},
            {"label": "You filled the gaps", "text": "Ebbing and flowing, all-in then slack — but the Lord kept the whole thing on the track (Proverbs 16:9)."},
            {"label": "Agur’s prayer", "text": "“Make me neither rich nor poor, lest I forget You, forget Your law” (Proverbs 30:8–9)."},
            {"label": "The ox and the plow", "text": "Give daily bread, not a throne; don’t starve the ox that pulls the line, but don’t let comfort rot the spine (Deuteronomy 25:4; Matthew 6:11)."},
        ],
        "terms": [
            {"term": "Agur’s prayer", "gloss": "Proverbs 30:7–9, the only personal prayer in Proverbs: “give me neither poverty nor riches… lest I be full and deny You… or be poor and steal.”"},
            {"term": "“hope deferred makes the heart sick”", "gloss": "Proverbs 13:12, behind “delayed hope makes me lousy.”"},
            {"term": "“daily bread”", "gloss": "Matthew 6:11, the Lord’s Prayer petition, woven into Agur’s request for “the food that is needful for me.”"},
            {"term": "“don’t starve the ox”", "gloss": "Deuteronomy 25:4, “you shall not muzzle an ox while it treads out the grain” — the picture of needing just enough to keep working."},
            {"term": "“lest I forget You”", "gloss": "Deuteronomy 8:11–18 — the warning that prosperity quietly breeds forgetfulness of God."},
        ],
        "discussion": [
            "Agur asks for neither poverty nor riches. Why might both extremes be spiritually dangerous?",
            "The song names two opposite failures — squandering ease and quitting under delay. Which are you more prone to?",
            "What would “enough” actually look like for you — and why is that so hard to name?",
        ],
        "contemplation": [
            "Are you asking God for a throne, or for daily bread?",
            "Where has prosperity (or the hope of it) made you forget the Lord?",
            "Where has delayed hope tempted you to quit before the finish?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "When the reward comes too easy",
                "I squander it away,",
                "start believing all the lies",
                "that say I’ve got it made.",
                "But if the prize comes too slowly",
                "my heart just sinks inside —",
                "delayed hope makes me lousy,",
                "and I quit before I try.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "I’ve ebbed and flowed,",
                "gone all in and then gone slack,",
                "burned myself out",
                "then laid right back.",
                "But You, O Lord,",
                "You filled the gaps",
                "and kept the whole thing",
                "on the track.",
            ]},
            {"label": "Chorus", "lines": [
                "If I get it all too easy",
                "I’ll throw it all away,",
                "but I quit before the finish",
                "if I work all day with no pay.",
                "So make me neither rich nor poor,",
                "lest I forget You, forget Your law.",
                "Just give me what I need today,",
                "enough to walk, enough to stay.",
            ]},
            {"label": "Verse 2", "lines": [
                "When the reward comes too easy",
                "I confuse grace with pride,",
                "start thinking I deserve it",
                "like life was on my side.",
                "But if the prize comes too slowly",
                "I start losing heart —",
                "hope deferred just breaks me down",
                "before I even start.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "I’ve chased the rush,",
                "I’ve feared the grind,",
                "wanted proof",
                "before the time.",
                "But You’ve been steady,",
                "kind, and true",
                "when I didn’t know",
                "what else to do.",
            ]},
            {"label": "Chorus", "lines": [
                "If I get it all too easy",
                "I’ll throw it all away,",
                "but I quit before the finish",
                "if I work all day with no pay.",
                "So make me neither rich nor poor,",
                "lest I forget You, forget Your law.",
                "Just give me what I need today,",
                "enough to walk, enough to stay.",
            ]},
            {"label": "Bridge", "lines": [
                "Give me daily bread, not a throne,",
                "just enough to pull this plow back home.",
                "Don’t starve the ox that pulls the line,",
                "but don’t let comfort rot my spine.",
                "I’m learning how to pace this race,",
                "trust the work, enjoy the grace.",
            ]},
            {"label": "Final Chorus", "lines": [
                "If I get it all too easy",
                "I’ll throw it all away,",
                "but I quit before the finish",
                "if I work all day with no pay.",
                "So make me neither rich nor poor,",
                "lest I forget You, forget Your law.",
                "Give me just enough to move along,",
                "’cause I’m an ox — and I’m not that strong.",
            ]},
            {"label": "Outro", "lines": [
                "Neither rich nor poor,",
                "neither rich nor poor.",
                "Daily bread — just enough.",
                "Daily bread — just enough.",
            ]},
        ],
        "refs": ["Proverbs 30:7–9", "Proverbs 13:12", "Matthew 6:11"],
    },
    {
        "num": 4,
        "title": "Ultimate Showdown",
        "slug": "ultimate-showdown",
        "about": (
            "Antithetic parallelism as an ’80s action movie — wisdom on the "
            "right, folly on the left, two lines throwing elbows till the meaning "
            "gets clear."
        ),
        "thesis": (
            "Antithetic parallelism — the wise-vs-fool contrast that runs through "
            "Proverbs — staged as an ’80s action movie: two lines throwing elbows "
            "until the meaning gets clear."
        ),
        "facts": [
            ("Doctrine", "Wisdom literature · Biblical poetry"),
            ("Anchor text", "Proverbs 10–15"),
            ("Form", "’80s action-movie rap"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "Two horns on the head", "text": "Line A says this, line B says that — righteous vs. wicked, humble vs. proud (Proverbs 10:1)."},
            {"label": "Compare and contrast", "text": "The meaning gets clear when you set the opposites side by side (Proverbs 15:1)."},
            {"label": "The wise stay calm", "text": "“The wise stay calm, but the fool blows fast; hard work brings profit, lazy bones get nada” (Proverbs 14:23; 29:11)."},
            {"label": "Only wisdom wins", "text": "A “holy rap battle” where wisdom always takes the belt (Proverbs 3:13–18)."},
        ],
        "terms": [
            {"term": "antithetic parallelism", "gloss": "The Hebrew poetic device dominating Proverbs 10–15: two lines stating opposite truths (usually joined by “but”) so each one sharpens the other."},
            {"term": "the ’80s barrage", "gloss": "The song name-checks Superman (the “Chris Reeve cape”), Magnum P.I., Pee-wee’s Big Adventure (“genie in the mirror”), The Fall Guy, Star Wars (“princess versus Jabba”), T.J. Hooker, The Six Million Dollar Man, Knight Rider, and The Goonies — pop-culture “collisions” mirroring the colliding lines of the proverbs."},
            {"term": "“the wise stay calm, the fool blows fast”", "gloss": "Proverbs 29:11 — “a fool gives full vent to his spirit, but a wise man quietly holds it back.”"},
            {"term": "“gentle words heal, harsh ones slap”", "gloss": "Proverbs 15:1 — “a soft answer turns away wrath, but a harsh word stirs up anger.”"},
            {"term": "“technicolor sweater / friendship bracelets”", "gloss": "The song’s images for how the contrasting proverbs “weave together.”"},
        ],
        "discussion": [
            "The song teaches a Bible-study tool (antithetic parallelism) through movie mayhem. How does noticing the “but” in a proverb change the way you read it?",
            "Proverbs constantly contrasts wise and foolish. Why is contrast such an effective way to teach wisdom?",
            "Pick a favorite contrast proverb — how do its two halves sharpen each other?",
        ],
        "contemplation": [
            "In today’s choices, which line are you living — the wise one or the foolish one?",
            "“The wise stay calm, but the fool blows fast.” Where do you give “full vent to your spirit”?",
            "Where do you need a “soft answer” instead of a harsh one?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Intro", "lines": [
                "We got the folly on the left,",
                "we got the wisdom on the right.",
                "We got the folly on the left, we got the wisdom on the right.",
                "We got the folly on the left, we got the wisdom on the right.",
                "Yo!  Yeah!",
            ]},
            {"label": "Verse 1", "lines": [
                "I’m flipping through Proverbs like an eight-track tape,",
                "old school unfurled like the Chris Reeve cape.",
                "Magnum rolling out, teaching moral collisions,",
                "heroes versus villains and contrasted decisions.",
                "Antithetic? What? It’s a literary flex —",
                "line A says this, line B says that.",
                "Righteous versus wicked, humble versus proud,",
                "two lines throwing elbows like the Pistons for the crowd.",
            ]},
            {"label": "Chorus", "lines": [
                "Compare, contrast, the meaning gets clear,",
                "like Pee-wee’s genie floating in the mirror.",
                "Like friendship bracelets, the proverbs weave together,",
                "comparing and contrasting like a technicolor sweater.",
            ]},
            {"label": "Verse 2", "lines": [
                "You got wisdom on the left, she’s baking moral muffins,",
                "then folly on the right, eating glue and learning nothing.",
                "The lines collide together like a Fall Guy scene,",
                "slow-motion karate — what does it even mean?",
                "My proverbs be dropping those compare and contrast:",
                "the wise stay calm, but the fool blows fast.",
                "Hard work brings profit, lazy bones get nada —",
                "opposites collide like the princess versus Jabba.",
                "Each pair with loaded tension like a monster truck spring,",
                "T.J. Hooker in the hood, yellin’ “Freeze, punk, freeze!”",
                "It’s moral kung-fu, but literary clean,",
                "antithetic bars, sharp enough to cut your jeans.",
            ]},
            {"label": "Chorus", "lines": [
                "Like friendship bracelets, the proverbs weave together,",
                "comparing and contrasting like a technicolor sweater.",
            ]},
            {"label": "Verse 3", "lines": [
                "Take a truth on the left and its opposite on the right,",
                "put ’em side by side and you see the light.",
                "Like the righteous stand firm, but wicked collapse,",
                "gentle words heal, harsh ones slap.",
                "It’s a holy rap battle where only wisdom wins,",
                "Six Million Dollar Man when explosions begin.",
                "Proverbs got moves, Knight Rider chase scene,",
                "snuffing out the punks like they sticks of nicotine.",
                "Wisdom versus foolishness, the theme runs deep,",
                "like The Goonies adventure with a treasure to keep.",
            ]},
            {"label": "Chorus", "lines": [
                "Like friendship bracelets, the proverbs weave together,",
                "comparing and contrasting like a technicolor sweater.",
            ]},
            {"label": "Outro", "lines": [
                "We got the folly on the left,",
                "we got the wisdom on the right.",
                "We got the folly on the left,",
                "we got the wisdom on the right.",
                "We got the folly on the left, we got the wisdom on the right.",
                "We got the folly on the left, we got the wisdom on the right.",
            ]},
        ],
        "refs": ["Proverbs 10:1", "Proverbs 14:1", "Proverbs 15:1", "Proverbs 29:11"],
    },
    {
        "num": 5,
        "title": "Solfeggietto",
        "slug": "solfeggietto",
        "about": (
            "C.P.E. Bach’s finger-exercise as a theology of formation — no "
            "shortcuts to glory; you’re refined over time, the practice room "
            "shaping forever’s tempo."
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
            {"term": "Solfeggietto", "gloss": "A famous, finger-twisting keyboard étude in C minor by Carl Philipp Emanuel Bach — son of J.S. Bach — built almost entirely from racing scales and arpeggios. (Reused from the Shady’s Bach album.)"},
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
                "SOL-FE-GE-O,",
                "SOL-FE-GE-O,",
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
        "refs": ["Romans 2:6–8", "Proverbs 13:4", "Proverbs 21:5", "Galatians 6:9"],
    },
    {
        "num": 6,
        "title": "Clean or Die",
        "slug": "clean-or-die",
        "about": (
            "A messy-room teenager meets the ant of Proverbs 6 — no master, no "
            "motivation playlist, just tiny legs pushing through the universe."
        ),
        "thesis": (
            "A messy-room teenager is sent to the ant of Proverbs 6: no boss, no "
            "hype, no motivation playlist — just tiny legs pushing through the "
            "universe, doing the work."
        ),
        "facts": [
            ("Doctrine", "Diligence · Sloth"),
            ("Anchor text", "Proverbs 6:6–11"),
            ("Form", "Funky pop-punk"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "Clean or die", "text": "The dumpster room, fossilized taquitos, and the parental ultimatum (cf. Proverbs 24:30–31)."},
            {"label": "Consider the ant", "text": "No master, no overseer, yet it stores its food — “calories already pre-captured” (Proverbs 6:6–8)."},
            {"label": "The sluggard’s anthem", "text": "“A little sleep, a little slumber”… and poverty comes like a robber (Proverbs 6:9–11)."},
            {"label": "Tiny legs", "text": "No announcements, no playlist — just insect hustle pushing through the universe (Proverbs 6:6)."},
        ],
        "terms": [
            {"term": "“Look to the ant, you sluggard”", "gloss": "Proverbs 6:6–8 — the ant has “no chief, officer, or ruler,” yet provides its food: a model of self-starting diligence."},
            {"term": "“a little sleep, a little slumber”", "gloss": "Proverbs 6:9–11 (and 24:33–34) — the sluggard’s refrain that ends in poverty coming “like an armed man.”"},
            {"term": "“the Bible says with laughter”", "gloss": "Scripture’s wry tone toward the sluggard, who’s almost comic in his excuses — “there is a lion in the road!” (Proverbs 26:13–16)."},
            {"term": "“no motivation playlist to rehearse”", "gloss": "The modern crutch the ant doesn’t need — diligence over hype."},
            {"term": "entomology", "gloss": "The study of insects — the teen’s punning excuse for not knowing how the ant works (and not cleaning his room)."},
        ],
        "discussion": [
            "The ant works with “no chief, officer, or ruler.” Where do you only work when someone’s watching?",
            "Proverbs almost mocks the sluggard (“a lion in the road!”). Why use humor to confront laziness?",
            "The song contrasts “insect hustle” with a “motivation playlist.” Where do we substitute hype for actual work?",
        ],
        "contemplation": [
            "What’s your version of “a little sleep, a little slumber”?",
            "Where do you need to just do the work with “no big announcements”?",
            "Is there a “dumpster room” in your life you keep avoiding?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "It’s true my room’s a dumpster",
                "with fossilized taquitos ’neath my bed.",
                "And it’s clear my parents",
                "have indicated that soon I may be dead.",
                "They said the next day that ends in “why”",
                "I must choose to clean or die.",
                "So why can’t I,",
                "oh why can’t I?",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "Maybe it’s ’cuz (whoa whoa whoa)",
                "I don’t know entomology.",
                "If I looked at the ant,",
                "then I might begin to see.",
            ]},
            {"label": "Chorus", "lines": [
                "He just does his work,",
                "no big announcements to come first.",
                "Just insect hustle,",
                "no “motivation playlist” to rehearse —",
                "just tiny legs (tiny legs)",
                "pushin’ through the universe.",
                "Just tiny legs (tiny legs)",
                "pushin’ through the universe.",
            ]},
            {"label": "Bridge", "lines": [
                "Look to the ant,",
                "the Bible says with laughter:",
                "he has no master",
                "to tell him what to do",
                "or what to get after,",
                "yet his calories (calories)",
                "are already pre-captured.",
            ]},
            {"label": "Verse 2 — Rap", "lines": [
                "How long will you lie there, O you sluggard?",
                "Your motivation’s such a bummer.",
                "A little sleep, a little rest,",
                "a little video game fest,",
                "and you’ll wind up like a fool",
                "who never figured out what to do.",
            ]},
            {"label": "Bridge", "lines": [
                "Look to the ant,",
                "the Bible says with laughter:",
                "he has no master",
                "to tell him what to do",
                "or what to get after,",
                "yet his calories (calories)",
                "are already pre-captured.",
                "Yes, his calories (Micky D’s)",
                "are already pre-captured.",
            ]},
            {"label": "Chorus", "lines": [
                "He just does his work,",
                "no big announcements to come first.",
                "Just insect hustle,",
                "no “motivation playlist” to rehearse —",
                "just tiny legs (tiny legs)",
                "pushin’ through the universe.",
                "Just tiny legs (tiny legs)",
                "pushin’ through the universe.",
            ]},
        ],
        "refs": ["Proverbs 6:6–11", "Proverbs 26:13–16"],
    },
    {
        "num": 7,
        "title": "Squeaky Wheel",
        "slug": "squeaky-wheel",
        "about": (
            "An anthem for the unflashy — not lighting up every room or turning "
            "pain into a brand, just showing up on time in a spotlight-stealing "
            "world."
        ),
        "thesis": (
            "An anthem for the unflashy: in a spotlight-stealing world, let "
            "another praise you — show up on time, love in the dark, and let your "
            "character do the talking."
        ),
        "facts": [
            ("Doctrine", "Humility · Faithfulness"),
            ("Anchor text", "Proverbs 27:2 · 17:27–28"),
            ("Form", "Laid-back groove"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "No flexing", "text": "“I don’t light up every room, don’t talk big just to talk again” — I just show up to work on time (Proverbs 27:2)."},
            {"label": "No pain-as-brand", "text": "Not dressing like a headline act or turning pain into a brand; staying when it’s hard (Proverbs 17:27)."},
            {"label": "The quiet jungle cat", "text": "More laid-back than the loud crowd — restraint over noise (Proverbs 17:28)."},
            {"label": "Faithful in the dark", "text": "Knowing how to “love in the dark” — the unseen faithfulness the diligent hand is built on (Proverbs 12:24)."},
        ],
        "terms": [
            {"term": "“the squeaky wheel gets the grease”", "gloss": "The modern American proverb the song pushes against — it refuses to be loudest just to get attention."},
            {"term": "“let another praise you, and not your own mouth”", "gloss": "Proverbs 27:2 — the song’s core text on self-promotion."},
            {"term": "“even a fool who keeps silent is considered wise”", "gloss": "Proverbs 17:28 (with 17:27) — restraint of words is itself a mark of wisdom."},
            {"term": "“the hand of the diligent will rule”", "gloss": "Proverbs 12:24 — quiet, faithful showing-up, not noise, is what lasts."},
            {"term": "“flex-appeal / spotlight stealin’”", "gloss": "The song’s name for the attention economy it deliberately opts out of."},
        ],
        "discussion": [
            "Our culture says “the squeaky wheel gets the grease.” Proverbs says “let another praise you.” How do you live the second in a world built on the first?",
            "“I know how to love in the dark.” Why is unseen faithfulness so undervalued — and so important?",
            "Where’s the line between humble reticence and failing to speak up when you should?",
        ],
        "contemplation": [
            "Do you crave the spotlight, or are you content to “love in the dark”?",
            "Where are you tempted to “turn pain into a brand”?",
            "Could you let your conduct, not your mouth, do the praising this week?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "I don’t light up every room I’m in,",
                "don’t talk big just to talk again.",
                "I don’t sell you a perfect line,",
                "but I show up to work on time.",
            ]},
            {"label": "Chorus / Hook", "lines": [
                "That’s how I plan on deal’n",
                "with this squeaky-wheel,’n,",
                "flex-appeal’n,",
                "spotlight-stealin’, feel’n world.",
                "That’s how I’m deal’n.",
            ]},
            {"label": "Verse 2", "lines": [
                "I don’t dress like a headline act,",
                "I don’t turn pain into a brand like that.",
                "But I know how to stay when it’s hard,",
                "I know how to love in the dark.",
            ]},
            {"label": "Chorus / Hook", "lines": [
                "That’s how I plan on deal’n",
                "with this squeaky-wheel,’n,",
                "flex-appeal’n,",
                "spotlight-stealin’, feel’n world.",
                "That’s how I’m deal’n.",
            ]},
            {"label": "Verse 3", "lines": [
                "Lots of dudes like getting loud,",
                "like to stand in front of the crowd.",
                "Ah, but I’m more laid back than that,",
                "just like a quiet jungle cat (PURRRR).",
            ]},
            {"label": "Chorus / Hook", "lines": [
                "That’s how I plan on deal’n",
                "with this squeaky-wheel,’n,",
                "flex-appeal’n,",
                "spotlight-stealin’, feel’n world.",
                "That’s how I’m deal’n.",
            ]},
        ],
        "refs": ["Proverbs 27:2", "Proverbs 17:27–28", "Proverbs 12:24"],
    },
    {
        "num": 8,
        "title": "NancyPlease",
        "slug": "nancyplease",
        "about": (
            "This is literally just a dumb thing that reminded Chris of how silly "
            "talk has some value."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Spoken intro", "lines": [
                "“Hey Nancy, you’re like… pretty good at singing. You wanna close out this album with one more song?”",
            ]},
            {"label": "Nancy", "lines": [
                "Double Pleasey,",
                "Nacho Cheesy,",
                "Lemon Squeezy,",
                "Slimy Sneezy,",
                "Biting Fleas — EEE,",
                "Please!!!",
            ]},
            {"label": None, "lines": [
                "(…and a 30-second musical interlude to close the album.)",
            ]},
        ],
        "refs": [],
    },
    {
        "num": 9,
        "title": "Plastic Love",
        "slug": "plastic-love",
        "about": (
            "A warning against counterfeit love — the easy, lab-grown kind that "
            "scratches the itch but taxes the soul. Real love waits to grow."
        ),
        "thesis": (
            "A warning in the key of Proverbs’ seductress: counterfeit love is "
            "easy, lab-grown, and quick — it scratches the itch but taxes the "
            "soul. Real love waits to grow."
        ),
        "facts": [
            ("Doctrine", "Purity · Wisdom · Desire"),
            ("Anchor text", "Proverbs 5 · 7 · 9:13–18"),
            ("Form", "Synth-noir"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "Hungry and undiscerning", "text": "Wake up starving and you grab whatever’s on the table; the same hunger lives in the heart (Proverbs 9:13–18)."},
            {"label": "Plastic love", "text": "Lab-grown, built to feel good fast, then fade and leave guilt; it taxes the soul (Proverbs 5:3–5)."},
            {"label": "The smarter fake", "text": "The one that whispers, “no one will know, you’ve earned this” — a soft voice guarding a gate (Proverbs 7:21–23)."},
            {"label": "Real love waits", "text": "Don’t rent your heart or trade your soul; what lasts takes time, what’s true is whole (Proverbs 5:15–19)."},
        ],
        "terms": [
            {"term": "“Plastic Love”", "gloss": "The title nods to the cult Japanese city-pop song, but here it means counterfeit, synthetic love — the opposite of the real thing."},
            {"term": "Lady Folly", "gloss": "Proverbs 9:13–18, the foolish woman who calls out “stolen water is sweet”; the seductress of Proverbs 5 and 7 stands behind the whole song."},
            {"term": "“it feels easy for way too long”", "gloss": "The Proverbs warning that folly’s path is smooth and downhill — “as an ox goes to the slaughter” (Proverbs 7:21–23)."},
            {"term": "“scratches the itch but won’t make you whole”", "gloss": "Echoes Proverbs 25:16 — eat honey, but not so much “that you have your fill of it and vomit.”"},
            {"term": "“drink water from your own cistern”", "gloss": "Proverbs 5:15–19, the positive counterpart: faithful, covenant love that satisfies."},
        ],
        "discussion": [
            "The song says fake love’s danger is that “it feels easy for way too long.” Why is the smooth, gradual path more dangerous than the obviously wrong one?",
            "“It’s letting someone aim [your desire] for you.” How do voices and algorithms aim our desires today?",
            "Proverbs personifies both Wisdom and Folly as women calling out. What does each “call” sound like now?",
        ],
        "contemplation": [
            "Where are you settling for “plastic love” — a quick relief that taxes your soul?",
            "Whose “soft voice guarding a gate” have you been listening to?",
            "What in your life “takes time” but is “whole” — and are you willing to wait for it?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Intro", "lines": [
                "One day you’ll wake up early,",
                "earlier than you planned,",
                "and you’ll be starving,",
                "hungrier than you can stand.",
            ]},
            {"label": "Verse 1", "lines": [
                "And when that happens",
                "you don’t read labels,",
                "you don’t ask questions,",
                "you grab whatever’s on the table.",
                "That’s normal, that’s human,",
                "but here’s what no one tells you:",
                "that same hunger lives in your heart —",
                "lonely, curious, wanting to be wanted,",
                "and fake love knows that part.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "Eat the wrong thing,",
                "you’ll be fine by noon.",
                "Love the wrong thing,",
                "it gets inside you,",
                "teaches your heart",
                "a broken tune.",
            ]},
            {"label": "Chorus", "lines": [
                "If it’s quick, be slow,",
                "if it’s loud, say no.",
                "Real love waits to grow,",
                "fake love comes and goes.",
            ]},
            {"label": "Verse 2", "lines": [
                "Some fake love doesn’t knock,",
                "it just shows up,",
                "not asking for your whole heart,",
                "just a little touch-up.",
                "Just a moment, just enough",
                "to take the edge off when life feels rough.",
                "PLASTIC love — lab-grown,",
                "built to feel good fast, then fade, leave guilt.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "It scratches the itch,",
                "but it won’t make you whole.",
                "Feels like relief,",
                "but it taxes your soul.",
                "And the danger isn’t that it feels wrong —",
                "it’s that it feels easy for way too long.",
            ]},
            {"label": "Chorus", "lines": [
                "If it’s quick, be slow,",
                "if it’s loud, say no.",
                "Real love waits to grow,",
                "fake love comes and goes.",
            ]},
            {"label": "Bridge", "lines": [
                "Then there’s a smarter fake love —",
                "not loud, not rushed.",
                "This one whispers, never shoves:",
                "“No one will know.”",
                "“You’ve earned this.”",
                "“It’s just the way nature goes.”",
                "Step by step, with every choice,",
                "your future shrinks behind that voice.",
                "The problem isn’t desire — that part’s true.",
                "It’s letting someone aim it for you.",
                "That’s not romance, that’s not fate,",
                "that’s a soft voice guarding a gate.",
            ]},
            {"label": "Final Chorus", "lines": [
                "If it’s quick, be slow,",
                "if it’s loud, say no.",
                "Real love waits to grow,",
                "fake love comes and goes.",
                "Don’t rent your heart,",
                "don’t trade your soul.",
                "What lasts takes time,",
                "what’s true is whole.",
            ]},
            {"label": "Outro", "lines": [
                "And one day you’ll meet someone —",
                "this won’t be sparks that flash and flee,",
                "this will be someone who walks with thee.",
                "You’re not killing desire,",
                "you’re teaching it why.",
                "You’re not late, you’re not behind —",
                "you’re finishing right.",
            ]},
        ],
        "refs": ["Proverbs 5:1–14", "Proverbs 7:1–27", "Proverbs 9:13–18", "Proverbs 25:16"],
    },
]
