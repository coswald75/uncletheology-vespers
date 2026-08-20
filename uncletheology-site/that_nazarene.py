# -*- coding: utf-8 -*-
"""
That Nazarene — album data.

Shoegaze meets the Laurel Canyon (a Lord Huron–style reverb-drenched folk-rock
mashup): doubt turned to worship, the risen Carpenter King, and faithfulness
that holds through the drifting and the fall. Lyrics from the "That Nazarene"
Google Doc (production directions dropped; section labels kept). Two tracks
rework Isaac Watts / John Wesley hymns (credited on the page).
"""

ALBUM = {
    "title": "That Nazarene",
    "slug": "that-nazarene",
    "order": 7,
    "tagline": "Uncle Theology · Lyrics & Scripture",
    "blurb": (
        "Shoegaze meets the Laurel Canyon — a reverb-drenched, golden-hour record "
        "in the vein of Lord Huron: doubt turned to worship, the risen Carpenter "
        "King who drew near, and the faithfulness that holds through the drifting "
        "and the fall."
    ),
    "cover": "/assets/that-nazarene/cover.jpg",
    "audio_prefix": "that-nazarene",
    # Golden-hour California identity — warm sepia night, amber sunset, dusty teal.
    "theme": {
        "--bg": "#1d1712",
        "--bg-2": "#241d16",
        "--surface": "#2b231a",
        "--surface-2": "#372c20",
        "--rule": "#48392a",
        "--ink": "#f5ecdc",
        "--ink-soft": "#d8cbb4",
        "--ink-faint": "#9c8e78",
        "--green": "#6fa49b",
        "--green-deep": "#467269",
        "--gold": "#e8ad5e",
        "--gold-deep": "#c0863a",
        "--link": "#e8ad5e",
        "--glow-a": "rgba(232,173,94,0.13)",
        "--glow-b": "rgba(111,164,155,0.07)",
    },
    # UncleTheology Radio episode: the whole album played straight through
    # with a spoken intro before each song (chapter markers baked into the MP3).
    "episode": {
        "order": 1,
        "title": "That Nazarene — the whole album, sung and explained",
        "guid": "utr-that-nazarene-2026-07-22",
        "pubDate": "Wed, 15 Jul 2026 12:00:00 -0500",
        "duration": "32:08",
        "length": 46445299,
        "audio_url": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/that-nazarene.mp3",
        "image": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/that-nazarene-art.jpg",
        "summary": (
            "That Nazarene played end to end — shoegaze meets the Laurel Canyon — with a short "
            "spoken introduction before every song telling you the Scripture and the story "
            "underneath it. Six songs, six intros, one continuous listen: the risen Carpenter "
            "King, worship in the middle of doubt, two Isaac Watts hymns made new, and the "
            "faithfulness that holds through the drifting and the fall."
        ),
        "chapters": [
            ("0:00", "Intro — Shovel, Sword, Headphones"),
            ("1:00", "Shovel, Sword, Headphones"),
            ("3:49", "Intro — That Nazarene"),
            ("4:47", "That Nazarene"),
            ("9:05", "Intro — God Knows"),
            ("9:52", "God Knows"),
            ("14:28", "Intro — I'll Praise My Maker"),
            ("15:07", "I'll Praise My Maker"),
            ("20:05", "Intro — Faithful"),
            ("20:49", "Faithful"),
            ("24:45", "Intro — Blessed Are"),
            ("25:35", "Blessed Are"),
        ],
    },
}

SONGS = [
    {
        "num": 1,
        "title": "Shovel, Sword, Headphones",
        "slug": "shovel-sword-headphones",
        "about": (
            "Doubt and cynicism meet the ordinary tools of grace — a shovel to "
            "clear the mess, a sword to chase the snakes, and headphones to drown "
            "out the lies while God works through us."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "Will you really restore what I've ruined?",
                "Will you really wipe these tears away?",
                "I've been holding my breath till I'm blue in the face,",
                "to see if mercies are new but here to stay.",
            ]},
            {"label": "Chorus", "lines": [
                "But yeah, I've got some work to do.",
                "You work through us. That's nothing new.",
                "You gave me tools and an ancient plan:",
                "a shovel, a sword, and some headphone cans.",
                "A shovel to clear all the mess I made,",
                "a sword to chase the snakes away,",
                "and some headphones just to keep me sane,",
                "and drown out all the lies.",
            ]},
            {"label": "Verse 2", "lines": [
                "I've had so many false alarms,",
                "thought I had beat this sin'n.",
                "So Lord, I've got to add to your work —",
                "please fix this cynicism.",
            ]},
            {"label": "Chorus", "lines": [
                "And yeah, I've got some work to do.",
                "You work through us. That's nothing new.",
                "You gave me tools and an ancient plan:",
                "a shovel, a sword, and some headphone cans.",
                "A shovel to clear all the mess I made,",
                "a sword to chase the snakes away,",
                "and some headphones just to keep me sane,",
                "and drown out all the lies.",
            ]},
        ],
        "refs": ["Lamentations 3:22–23", "Nehemiah 4:17–18", "Ephesians 6:17", "Philippians 2:12–13"],
    },
    {
        "num": 2,
        "title": "That Nazarene",
        "slug": "that-nazarene",
        "about": (
            "The risen Carpenter King who drew near — His risen wounds curing all "
            "doubt; He knows my name, my hairs, my tomorrows, and death itself is "
            "just an empty tomb."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "I don't know how they live their lives without him.",
                "I don't know how they make it all make sense.",
                "His risen wounds",
                "are curin' all my doubt'n,",
                "and in me grows",
                "a godly happiness.",
            ]},
            {"label": "Chorus", "lines": [
                "That Nazarene",
                "drew near to me —",
                "Carpenter King,",
                "that man is dear to me.",
                "And by His blood,",
                "I am set free.",
            ]},
            {"label": "Verse 2", "lines": [
                "I don't know how they carry all that sorrow,",
                "I don't know how they face the empty room.",
                "He knows my name,",
                "my hairs and my tomorrows,",
                "and death itself",
                "is just an empty tomb.",
            ]},
            {"label": "Chorus", "lines": [
                "That Nazarene",
                "drew near to me —",
                "Carpenter King,",
                "that man is dear to me.",
                "And by His blood,",
                "I am set free.",
            ]},
            {"label": "Verse 3", "lines": [
                "I don't know how they face the world unbroken,",
                "I don't know how they bear the weight alone.",
                "He's kissed my head,",
                "and promises he's spoken",
                "come look'n for",
                "the one He's always known.",
            ]},
            {"label": "Final Chorus", "lines": [
                "That Nazarene",
                "drew near to me —",
                "Carpenter King,",
                "that man is dear to me.",
                "And by His blood,",
                "I am set free.",
                "Both sin and death have been de-feat-ed!!!",
                "And as a friend I am now greeted!",
                "Amazing love — how can they beat it?",
                "Amazing love — how can this be?",
            ]},
        ],
        "refs": ["John 20:24–29", "Mark 6:3", "Matthew 10:30", "1 Corinthians 15:54–57"],
    },
    {
        "num": 3,
        "title": "God Knows",
        "slug": "god-knows",
        "about": (
            "When you don't know what to do, worship through the questions — “is "
            "my faith really real? God knows.” The unanswered questions are cues "
            "to lift your eyes to the all-wise Maker."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "Hey you —",
                "do you know",
                "what you should do",
                "when you don't",
                "know what to do?",
                "You gotta worship through…",
                "all of the questions…",
            ]},
            {"label": "Chorus", "lines": [
                "Is my faith really real?",
                "God knows.",
                "Why do I have these feels?",
                "God knows.",
                "When will my enemies kneel?",
                "God knows.",
                "God knows.",
            ]},
            {"label": "Verse 2", "lines": [
                "Hey you —",
                "those questions",
                "are just cues",
                "to lift your eyes",
                "to the maker of the skies,",
                "to the one who's all wise —",
                "oh, God is all wise!",
            ]},
            {"label": "Chorus 2", "lines": [
                "Who's this in the mirror?",
                "God knows.",
                "Why can't my vision be clearer?",
                "God knows.",
                "Am I further or nearer?",
                "God knows.",
                "God knows.",
            ]},
            {"label": "Verse 3", "lines": [
                "Hey you,",
                "tossin' on your bed —",
                "why don't you try",
                "worshippin' instead?",
                "Let your brain begin to hum",
                "as you celebrate the one",
                "who sent his only Son (oooh).",
            ]},
            {"label": "Outro", "lines": [
                "Who can stand against His will?",
                "No one.",
                "Who can break the bond He sealed?",
                "No one.",
                "Who can take the love he feels",
                "toward you?",
                "No one. No one. No one.",
            ]},
        ],
        "refs": ["Psalm 42:5", "Romans 8:31–39", "Proverbs 3:5–6", "James 1:5"],
    },
    {
        "num": 4,
        "title": "I’ll Praise My Maker",
        "slug": "ill-praise-my-maker",
        "about": (
            "Isaac Watts's paraphrase of Psalm 146, reworked — I'll praise my "
            "Maker while I've breath, and also after I've tasted death; my lungs "
            "were made to be a horn for His majesty."
        ),
        "attribution": {
            "text": (
                "The verses are Isaac Watts's hymn “I'll Praise My Maker While "
                "I've Breath” (1719), a paraphrase of Psalm 146, as adapted by "
                "John Wesley; new outro by Chris Oswald."
            ),
            "links": [
                ("About Isaac Watts", "https://en.wikipedia.org/wiki/Isaac_Watts"),
            ],
        },
        "kind": "verse",
        "blocks": [
            {"label": None, "lines": [
                "I'll praise my Maker while I've breath,",
                "and also after I've tasted death.",
            ]},
            {"label": "Verse 1", "lines": [
                "Happy the man whose hopes rely",
                "on Israel's God! He made the sky,",
                "and earth, and seas, with all their train:",
                "His truth forever stands secure;",
                "He saves th' oppressed, He feeds the poor,",
                "and none shall find His promise vain.",
            ]},
            {"label": "Chorus", "lines": [
                "I'll praise my Maker while I've breath,",
                "and also after I've tasted death.",
            ]},
            {"label": "Verse 2", "lines": [
                "The Lord pours eyesight on the blind;",
                "the Lord supports the fainting mind;",
                "He sends the laboring conscience peace;",
                "He helps the stranger in distress,",
                "the widow and the fatherless,",
                "and grants the prisoner sweet release.",
            ]},
            {"label": "Chorus", "lines": [
                "I'll praise my Maker while I've breath,",
                "and also after I've tasted death.",
            ]},
            {"label": "Outro", "lines": [
                "Whether I'm in this life or the next,",
                "my job won't change;",
                "whether filled with earthly or heaven's breath,",
                "my lungs will always proclaim!",
                "My maker made me thus to be",
                "a horn to praise his majesty;",
                "and so both now and then I'll be",
                "worshipping the God who",
                "made and remade me,",
                "made and remade me,",
                "made and remade me.",
            ]},
        ],
        "refs": ["Psalm 146", "Psalm 104:33", "Psalm 150:6"],
    },
    {
        "num": 5,
        "title": "Faithful",
        "slug": "faithful",
        "about": (
            "When doubts arise and prayer has lost its voice, You are faithful "
            "through it all — faithful even on the cross, where love held fast at "
            "such a cost and mercy said it is done."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "When doubts arise and comforts fade,",
                "and prayer has lost its voice,",
                "my restless heart is sorely pressed",
                "by wounds of my own choice.",
            ]},
            {"label": "Chorus", "lines": [
                "You are faithful through it all —",
                "through the drifting,",
                "through the fall.",
                "When I cannot see tomorrow,",
                "You are faithful,",
                "faithful through it all.",
                "You are faithful,",
                "faithful through it all.",
            ]},
            {"label": "Verse 2", "lines": [
                "I walk the paths where others rest,",
                "yet peace escapes my sight;",
                "I bear the songs upon my lips",
                "but feel no true delight.",
            ]},
            {"label": "Chorus", "lines": [
                "You are faithful through it all —",
                "through the drifting,",
                "through the fall.",
                "When I cannot see tomorrow,",
                "You are faithful,",
                "faithful through it all.",
                "You are faithful,",
                "faithful through it all.",
            ]},
            {"label": "Bridge", "lines": [
                "I bring nothing but my failure,",
                "my righteousness is mud;",
                "even tears of my repentance",
                "need the washing of Your blood.",
                "But you are good,",
                "you won't let go (oh, You won't let go).",
            ]},
            {"label": "Chorus", "lines": [
                "You are faithful through it all —",
                "through the drifting,",
                "through the fall.",
                "When I cannot see tomorrow,",
                "You were faithful,",
                "faithful through it all.",
            ]},
            {"label": "Bridge", "lines": [
                "You were faithful on the cross,",
                "love held fast at such a cost;",
                "poured your wrath upon the son,",
                "and mercy says that it is done.",
            ]},
            {"label": "Chorus", "lines": [
                "You are faithful through it all —",
                "through the drifting,",
                "through the fall.",
                "When I cannot see tomorrow,",
                "You were faithful,",
                "faithful through it all.",
            ]},
        ],
        "refs": ["Lamentations 3:22–23", "2 Timothy 2:13", "Isaiah 53:5–6", "1 Corinthians 1:9"],
    },
    {
        "num": 6,
        "title": "Blessed Are",
        "slug": "blessed-are",
        "about": (
            "Isaac Watts's hymn on the Beatitudes, set to soaring shoegaze — the "
            "low ones rise, empty hands are the hands that hold, and through shame "
            "and flame comes glory and gold."
        ),
        "attribution": {
            "text": (
                "The numbered verses are Isaac Watts's hymn “Blessed Are the "
                "Humble Souls That See” (1707), a setting of the Beatitudes; new "
                "choruses and arrangement by Chris Oswald."
            ),
            "links": [
                ("About Isaac Watts", "https://en.wikipedia.org/wiki/Isaac_Watts"),
            ],
        },
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "Blessed are the humble souls that see",
                "their emptiness and poverty;",
                "treasures of grace to them are given,",
                "and crowns of joy laid up in heaven.",
            ]},
            {"label": "Verse 2", "lines": [
                "Blessed are the men of broken heart,",
                "who mourn for sin with inward smart;",
                "the blood of Christ divinely flows,",
                "a healing balm for all their woes.",
            ]},
            {"label": "Chorus 1", "lines": [
                "Blessed, blessed — the low ones rise,",
                "kingdom coming through the hallowed eyes.",
                "Empty hands are the hands that hold —",
                "blessed, blessed — the promise told.",
            ]},
            {"label": "Verse 3", "lines": [
                "Blessed are the meek, who stand afar",
                "from rage and passion, noise and war;",
                "God will secure their happy state,",
                "and plead their cause against the great.",
            ]},
            {"label": "Verse 4", "lines": [
                "Blessed are the souls that thirst for grace,",
                "hunger and long for righteousness,",
                "they shall be well supplied and fed",
                "with living streams and living bread.",
            ]},
            {"label": "Chorus 2", "lines": [
                "Blessed, blessed — the hungry fed,",
                "living water and living bread.",
                "Meek inherit what kings can't hold —",
                "blessed, blessed — the promise told.",
            ]},
            {"label": "Verse 5", "lines": [
                "Blessed are the men whose hearts move",
                "and melt with sympathy and love;",
                "from Christ the Lord shall they obtain",
                "like sympathy and love again.",
            ]},
            {"label": "Verse 6", "lines": [
                "Blessed are the pure, whose hearts are clean",
                "from the defiling powers of sin,",
                "with endless pleasure they shall see",
                "a God of spotless purity.",
            ]},
            {"label": "Chorus 3", "lines": [
                "Blessed, blessed — the pure will see",
                "the face of spotless purity.",
                "Mercy given comes back tenfold —",
                "blessed, blessed — the promise told.",
            ]},
            {"label": "Verse 7", "lines": [
                "Blessed are the men of peaceful life",
                "who quench the coals of growing strife,",
                "they shall be called the heirs of bliss,",
                "the sons of God, the God of peace.",
            ]},
            {"label": "Verse 8", "lines": [
                "Blessed are the sufferers who partake",
                "of pain and shame for Jesus' sake;",
                "their souls shall triumph in the Lord,",
                "glory and joy are their reward.",
            ]},
            {"label": "Final Chorus", "lines": [
                "Blessed, blessed — through shame and flame,",
                "triumph rising in Jesus' name.",
                "Sons of God when the story's told —",
                "blessed, blessed — glory and gold.",
                "Blessed, blessed — glory and gold.",
            ]},
        ],
        "refs": ["Matthew 5:3–12", "Luke 6:20–23"],
    },
]

# ── Study layer ──
# Drafted by the parallel agent workflow (see that_nazarene_aids.json) and merged
# into SONGS by slug. facts become (label, value) tuples; moves/terms/discussion/
# contemplation already match the render format in build.py.
import json as _json
import os as _os

_aids_file = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "that_nazarene_aids.json")
try:
    with open(_aids_file, encoding="utf-8") as _f:
        _AIDS = {a["slug"]: a for a in _json.load(_f)}
except FileNotFoundError:
    _AIDS = {}

for _s in SONGS:
    _a = _AIDS.get(_s["slug"])
    if not _a:
        continue
    _s["thesis"] = _a["thesis"]
    _s["facts"] = [(f["label"], f["value"]) for f in _a["facts"]]
    _s["moves"] = _a["moves"]
    _s["terms"] = _a["terms"]
    _s["discussion"] = _a["discussion"]
    _s["contemplation"] = _a["contemplation"]
