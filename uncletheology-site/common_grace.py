# -*- coding: utf-8 -*-
"""
Common Grace — album data.

A warm, genre-hopping ode to common grace. Lyrics reformatted from the
"Common Grace Album" Google Doc (production-direction notes dropped; section
labels kept). Art Nouveau teal-and-gold identity to match the cover.

NOTE (pending): the doc also has "Transfiguration" (lyrics, but no audio file
yet) and "Your Calamity" (its doc lyrics duplicate "Gratitude Has Filled My
Plate" — likely a copy/paste). Both omitted until Chris confirms.
"""

ALBUM = {
    "title": "Common Grace",
    "slug": "common-grace",
    "order": 6,
    "tagline": "Uncle Theology · Lyrics & Scripture",
    "blurb": (
        "A warm, genre-hopping ode to common grace — the everyday kindness God "
        "pours on the whole human race: sun on the sinner, the strawberry made "
        "sweet, small-town love, and ordinary-day glory."
    ),
    "cover": "/assets/common-grace/cover.jpg",
    "audio_prefix": "common-grace",
    # Art Nouveau identity — deep teal night, ornament gold, a rose accent.
    "theme": {
        "--bg": "#1a2730",
        "--bg-2": "#21313b",
        "--surface": "#263943",
        "--surface-2": "#314951",
        "--rule": "#3f5761",
        "--ink": "#f2ece0",
        "--ink-soft": "#cdc9ba",
        "--ink-faint": "#8b9298",
        "--green": "#cf7368",
        "--green-deep": "#a8524a",
        "--gold": "#d9b168",
        "--gold-deep": "#b08c42",
        "--link": "#d9b168",
        "--glow-a": "rgba(217,177,104,0.12)",
        "--glow-b": "rgba(207,115,104,0.07)",
    },
    "episode": {
        "order": 5,
        "title": "Common Grace — the whole album, sung and explained",
        "guid": "utr-common-grace-2026-07-22",
        "pubDate": "Sun, 19 Jul 2026 12:00:00 -0500",
        "duration": "40:26",
        "length": 58514951,
        "audio_url": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/common-grace.mp3",
        "image": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/common-grace-art.jpg",
        "summary": (
            "Common Grace played end to end — a warm, genre-hopping ode to the everyday kindness God "
            "pours on the whole human race — with a short spoken intro before every song. Sun on the "
            "sinner, Kuyper's every-square-inch, Ecclesiastes' vapor and the love that makes an "
            "unchanging town new, marriage as gift, the goodness of matter, thanksgiving on an "
            "ordinary day, the cure for the curved-in self, Lady Wisdom's clap-back, and the "
            "Transfiguration by way of the cross."
        ),
        "chapters": [
            ("0:00", "Intro — Common Grace"),
            ("1:01", "Common Grace"),
            ("4:08", "Intro — Stay in Your Lane"),
            ("4:57", "Stay in Your Lane"),
            ("8:16", "Intro — If This Vanity"),
            ("8:59", "If This Vanity"),
            ("11:53", "Intro — Town That Never Changes"),
            ("12:38", "Town That Never Changes"),
            ("16:19", "Intro — Weekend Honeymoons"),
            ("16:57", "Weekend Honeymoons"),
            ("19:58", "A word from our sponsor — Providence Community Church"),
            ("20:16", "Intro — God Made It Good"),
            ("21:03", "God Made It Good"),
            ("24:58", "Intro — Gratitude Has Filled My Plate"),
            ("25:44", "Gratitude Has Filled My Plate"),
            ("28:56", "Intro — Psalm 147"),
            ("29:42", "Psalm 147"),
            ("31:53", "Intro — Your Calamity"),
            ("32:38", "Your Calamity"),
            ("35:41", "Intro — Transfiguration"),
            ("36:33", "Transfiguration"),
        ],
    },
}

SONGS = [
    {
        "num": 1,
        "title": "Common Grace",
        "slug": "common-grace",
        "about": (
            "The everyday, non-saving grace God pours on the whole human race — "
            "sun on the sinner, rain on the saved — kindness meant to lead us to "
            "repentance."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "Woke up this mornin', sun on my face,",
                "didn't earn a drop of it — baby, that's grace.",
                "Not the saving kind that writes my name in the Book,",
                "just the everyday kind — go on, take a look.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "'Cause He sends the rain on the good and the mean,",
                "feeds the little sparrow and the sinner in between,",
                "holds back the worst of what our hearts would do —",
                "even for the folks who never say thank-you (ooh!)",
            ]},
            {"label": "Chorus", "lines": [
                "It's that com-mon grace (grace!)",
                "fallin' on the whole wide human race (race!)",
                "He don't have to, but He does it anyway —",
                "sun on the sinner, rain on the saved.",
                "It's that com-mon, com-mon grace.",
            ]},
            {"label": "Verse 2", "lines": [
                "The unbeliever paints a masterpiece,",
                "the pagan hums a tune that brings your soul some peace —",
                "now where'd they get the talent, where'd they get the eye?",
                "From the Giver of the good gifts sittin' up on high.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "Every perfect present, James chapter one:",
                "comes down from the Father of the moon and sun.",
                "No shadow, no turning, He's faithful and true —",
                "pourin' out the kindness on me and on you (ooh!)",
            ]},
            {"label": "Chorus", "lines": [
                "It's that com-mon grace (grace!)",
                "fallin' on the whole wide human race (race!)",
                "He don't have to, but He does it anyway —",
                "sun on the sinner, rain on the saved.",
                "It's that com-mon, com-mon grace.",
            ]},
            {"label": "Talk-Break / Bridge", "lines": [
                "Now hold up — don't you get it twisted, honey, listen close:",
                "this ain't the grace that raises up a heart that's cold.",
                "That's the special kind — the blood-bought, chosen embrace.",
                "But while you're still walkin' around? He's holdin' your place.",
                "Providence, y'all — Westminster, chapter five:",
                "He upholds every atom just to keep you alive.",
            ]},
            {"label": "Final Chorus", "lines": [
                "So it's that com-mon grace (grace!)",
                "restrainin' all the evil, settin' a slower pace,",
                "buildin' up the cities, keepin' order in the streets —",
                "kindness meant to lead ya to repentance at His feet.",
                "It's that com-mon grace — but oh, don't stop there,",
                "run and get the saving kind, 'cause that one's rare!",
                "Com-mon, com-mon grace.",
            ]},
        ],
        "refs": ["Matthew 5:45", "James 1:17", "Acts 14:17", "Romans 2:4"],
    },
    {
        "num": 2,
        "title": "Stay in Your Lane",
        "slug": "stay-in-your-lane",
        "about": (
            "Sphere sovereignty in a horn-driven anthem — family, government, and "
            "church each have their God-drawn lane, and Christ claims every square "
            "inch."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Intro — spoken", "lines": [
                "Uh-uh, honey. Every kingdom's got a king,",
                "and He drew the lines Himself — so don't go movin' anything.",
            ]},
            {"label": "Verse 1 — The Family", "lines": [
                "Started in the garden 'fore a thing went wrong,",
                "mama, papa, babies — that's the oldest song.",
                "Nobody handed down that love from City Hall,",
                "it grew up from the blood, baby — original, y'all.",
                "Even folks who never prayed still tuck their kids in tight —",
                "that's the common grace keepin' the household right.",
            ]},
            {"label": "Chorus", "lines": [
                "So stay in your lane! (stay, stay in your lane!)",
                "Every little sphere got its own domain.",
                "The state don't own the cradle, the crown don't run the pew —",
                "Christ is over all of it, and He's watchin' you.",
                "Stay-ay-ay in your lane. (ooh-ooh!)",
            ]},
            {"label": "Verse 2 — The Government", "lines": [
                "Now the sword came later, after Adam fell,",
                "somebody gotta keep the peace and ring the justice bell.",
                "Not from the preacher, not from the crowd's decree —",
                "that badge gets its power straight from the Almighty.",
                "Guard the weak, hold the line, keep the wicked slowed —",
                "but don't you swallow up my house, don't you take the whole road!",
            ]},
            {"label": "Chorus", "lines": [
                "So stay in your lane! (stay, stay in your lane!)",
                "Every little sphere got its own domain.",
                "The state don't own the cradle, the crown don't run the pew —",
                "Christ is over all of it, and He's watchin' you.",
                "Stay-ay-ay in your lane. (ooh-ooh!)",
            ]},
            {"label": "Bridge — The Church", "lines": [
                "Now here's where it's different, baby, lean in near:",
                "the other two run on common grace — but this one, oh, it's rare.",
                "No sword, no statute, just the Word and the water and the bread,",
                "the blood-bought special grace that raises sinners from the dead.",
                "Free church, free state — neither one's the other's throne,",
                "two hands of the same God, but each one stands alone.",
                "And the folks in the pews? They don't stay behind the door —",
                "they salt every sphere when they walk back out the floor. (whoo!)",
            ]},
            {"label": "Final Chorus", "lines": [
                "So stay in your lane! (stay, stay in your lane!)",
                "But carry the Kingdom everywhere you reign!",
                "Kuyper said it plain — there ain't a single square inch",
                "that Jesus doesn't claim and hold without a flinch.",
                "Family, crown, and church — three lanes, one Name,",
                "every sphere under Christ, and it's all His domain.",
                "Stay-ay-ay in your lane… ('cause He owns the whole terrain!)",
            ]},
        ],
        "refs": ["Romans 13:1–4", "Genesis 2:24", "Colossians 1:16–18", "Matthew 22:21"],
    },
    {
        "num": 3,
        "title": "If This Vanity",
        "slug": "if-this-vanity",
        "about": (
            "A horn-punchy kiss-off to hollow performance — if it's all vanity and "
            "a “home-cooked show,” I'm going home. (The “Home-Cooked Show” track.)"
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "How am I to know your raw intent,",
                "to know if this is time well spent,",
                "waiting 'round to be displayed",
                "like a model strat that's overplayed?",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "You want the vibe to carry you, but whata —",
                "whata whata do you wanna do?",
            ]},
            {"label": "Chorus", "lines": [
                "If vanity's all there's gonna be,",
                "I'm gonna go on home.",
                "You're play'n me like I'm in the front row seat",
                "of your own little home-cooked show.",
                "So if this vanity is all I'm gonna see,",
                "then I'm gonna go on home.",
            ]},
            {"label": "Verse 2", "lines": [
                "Oh boy, ya got me in",
                "with that practiced grin —",
                "I now suspect that you rehearsed",
                "in the rearview of your ex's hearse.",
                "(spoken: “she died of waiting for you!”)",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "You want the vibe to carry you, but whata —",
                "whata whata do you wanna do?",
            ]},
            {"label": "Chorus", "lines": [
                "If vanity's all there's gonna be,",
                "I'm gonna go on home.",
                "You're play'n me like I'm in the front row seat",
                "of your own little home-cooked show.",
                "But if this vanity is all I'm gonna see,",
                "then I'm gonna go on home.",
            ]},
            {"label": "Coda", "lines": [
                "You're default teasing,",
                "cuz your whole life's leading",
                "up to something that never comes —",
                "you've always just begun.",
                "So whata whata whata you gonna do?",
                "The rest is up to you.",
                "The rest is up to you.",
            ]},
        ],
        "refs": ["Ecclesiastes 1:2", "Ecclesiastes 2:11", "Ecclesiastes 4:4"],
    },
    {
        "num": 4,
        "title": "Town That Never Changes",
        "slug": "town-that-never-changes",
        "about": (
            "Young love in a small town that never changes — the same old diner, "
            "pews, and scoreboards made new by one hand in yours. (The “Brand New "
            "in a Town That Never Changes” track.)"
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "We were new to everything",
                "in a town that never changes.",
                "Same old sign at the city line —",
                "2A state champs back in eighty-nine.",
                "We met at the high school,",
                "same our parents went through.",
                "My whole life felt brand new",
                "as I fell in love with you.",
            ]},
            {"label": "Chorus", "lines": [
                "Brand new love in a place that never changes,",
                "same ol' diner with the same old faces,",
                "same old families in the Sunday pews —",
                "but your hand in mine made the world feel new.",
                "Yeah, we were brand new in a town that never changes,",
                "every hallway turning into someplace",
                "we'd never seen but somehow always knew.",
                "In that old high school, my life felt brand new.",
            ]},
            {"label": "Verse 2", "lines": [
                "Your letter jacket hanging",
                "on my thrift store bedroom door,",
                "dusty trophies in the lobby case —",
                "we never asked what they were for.",
                "We were skipping through the pages,",
                "everybody else already knew,",
                "but under those flickering scoreboards",
                "my life felt brand new.",
            ]},
            {"label": "Chorus", "lines": [
                "Brand new in a town that never changes,",
                "same last names on the parking spaces,",
                "same old story on the Friday news —",
                "but your laugh out loud cut the script in two.",
                "Yeah, we were brand new in a town that never changes,",
                "every back road became a brand new place",
                "we'd never seen but somehow always knew —",
                "this old place was built to build life anew.",
            ]},
            {"label": "Bridge", "lines": [
                "Maybe someday we'll drive past",
                "with kids in the backseat asking,",
                "“Did it always look this small?”",
                "And I'll smile through the flashing,",
                "'cause in that snapshot of me and you,",
                "everything old made us something true.",
            ]},
            {"label": "Chorus", "lines": [
                "Brand new in a town that never changes,",
                "same last names on the parking spaces,",
                "same old story on the Friday news —",
                "but one slow dance rewrote every rule.",
                "Yeah, we were brand new in a town that never changes,",
                "every goodbye turning into someway",
                "to stay a little longer there with you.",
                "In that old high school, my life felt brand new.",
            ]},
        ],
        "refs": ["Ecclesiastes 1:4", "Ecclesiastes 3:11", "Ecclesiastes 9:9"],
    },
    {
        "num": 5,
        "title": "Weekend Honeymoons",
        "slug": "weekend-honeymoons",
        "about": (
            "Newlyweds too poor to fly out and too happy to whine about it — "
            "portioning the chill and letting young love slowly build over summer "
            "weekend honeymoons."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "Hey Mister,",
                "we're a new thing,",
                "new thing with new rings.",
                "June wedding was a beautiful dream.",
            ]},
            {"label": "Turn", "lines": [
                "Too poor to fly out,",
                "too happy to whine about it.",
            ]},
            {"label": "Chorus", "lines": [
                "We're gonna drift",
                "into the deep end",
                "of this summer weekend.",
            ]},
            {"label": "Post-Chorus", "lines": [
                "Yeah, weekend honeymoons",
                "are what I'm gonna do with you.",
            ]},
            {"label": "Verse 2", "lines": [
                "Hey Mister,",
                "we're a new team,",
                "building out a whole new thing,",
                "shaking out our American dream.",
            ]},
            {"label": "Turn", "lines": [
                "Too poor to fly out,",
                "too happy to whine about it.",
            ]},
            {"label": "Chorus", "lines": [
                "We're gonna drift",
                "into the deep end",
                "of this summer weekend.",
            ]},
            {"label": "Post-Chorus", "lines": [
                "Yeah, weekend honeymoons",
                "are what I'm gonna do with you.",
            ]},
            {"label": "Final Chorus", "lines": [
                "We're gonna drift",
                "into the deep end",
                "of this summer weekend.",
            ]},
            {"label": "Outro", "lines": [
                "Oh, I'm so glad I met you,",
                "and I'm so glad I get to",
                "build something right beside you.",
                "Yeah, young love came with lots of bills,",
                "so we gotta portion our chill —",
                "let this love slowly build.",
            ]},
        ],
        "refs": ["Ecclesiastes 9:9", "Proverbs 5:18–19", "Song of Solomon 2:16"],
    },
    {
        "num": 6,
        "title": "God Made It Good",
        "slug": "god-made-it-good",
        "about": (
            "A rebuke to the “touch not, taste not” frown patrol — matter isn't "
            "evil; God made the strawberry sweet and the wine at Cana. Grace isn't "
            "a diet."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Intro", "lines": [
                "Uh — hold up, hold up…",
                "Miss Prim in the back with the pinched-up face,",
                "lemme school you on a little thing called grace.",
                "(Sha-la-la!)",
            ]},
            {"label": "Verse 1", "lines": [
                "There's a frown patrol with a clipboard and a rule,",
                "thinkin' every ounce of fun is a trick of the fool.",
                "Say the cake is a sin and the dancin' is worse,",
                "got a wag in the finger and a chip and a curse.",
                "Renounce and renounce 'til you're holy and gaunt —",
                "competitive misery, flauntin' what they DON'T.",
                "But the God up above with the sun and the rain",
                "made the strawberry sweet, and He ain't gonna complain!",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "“Touch not! Taste not! Handle not the good!”",
                "Frownin' at the flavor like a killjoy should —",
                "but baby, read your Bible, get it understood…",
            ]},
            {"label": "Chorus", "lines": [
                "Oh, God made it good, good, good!",
                "He made the taste buds — of course He would!",
                "Coffee in the mornin', honey on the bread,",
                "wine to make you merry like the good Book said.",
                "So take your touch-not, taste-not, frownin' in the pew —",
                "God made it good, and He made it for YOU!",
                "(Sha-la-la — for you!)",
            ]},
            {"label": "Verse 2", "lines": [
                "Now they called my Jesus a glutton and a wino",
                "'cause He sat with the sinners and He poured the good vino,",
                "turned the water to wine at the wedding in Cana —",
                "a hundred fifty gallons, now that's a Savior, mama!",
                "(That's a lot!) Coulda made it grape juice, weak and thin,",
                "but He brought the good stuff, let the joy begin.",
                "Ecclesiastes say it — eat your bread with cheer,",
                "drink your wine with a merry heart, the Lord is near!",
            ]},
            {"label": "Chorus", "lines": [
                "Oh, God made it good, good, good! (so good!)",
                "He made the taste buds — yes, He would!",
                "Coffee in the mornin', honey on the bread,",
                "wine to make you merry like the good Book said.",
                "So take your touch-not, taste-not, frownin' in the pew —",
                "God made it good, and He made it for YOU!",
                "(Sha-la-la — for you!)",
            ]},
            {"label": "Bridge", "lines": [
                "See the touch-not creed got an appearance of wise (ooh),",
                "but it's Gnostic in a Sunday-mornin' disguise.",
                "Matter ain't evil and the body ain't bad —",
                "it's the best good gift that a person ever had!",
                "Colossians called it “wisdom,” so-called, on the shelf,",
                "but it can't kill a sin — it just puffs up the self.",
                "So quit addin' rules to the finished, finished work —",
                "grace ain't a diet, and the joy ain't a quirk!",
            ]},
            {"label": "Final Chorus", "lines": [
                "Oh, God made it good, good, good! (so good!)",
                "He made the taste buds — yes, He would!",
                "Coffee in the mornin', honey on the bread,",
                "wine to make you merry like the good Book said.",
                "So take your touch-not, taste-not, frownin' in the pew —",
                "God made it good, and He made it for YOU!",
                "(Good, good, good — for you!)",
            ]},
            {"label": "Outro", "lines": [
                "So put down the clipboard, Miss Prim, take a seat,",
                "have a slice, crack a smile, come on tap your feet.",
                "God made it good — now go and finish your plate!",
                "(Good, good, good — it's a common grace!)",
            ]},
        ],
        "refs": ["1 Timothy 4:1–5", "Colossians 2:20–23", "Ecclesiastes 9:7", "John 2:1–11"],
    },
    {
        "num": 7,
        "title": "Gratitude Has Filled My Plate",
        "slug": "gratitude-has-filled-my-plate",
        "about": (
            "Ordinary-day glory — parking lots full of grace, tiny stupid miracles "
            "stacking up like receipts, and a man who can't stop laughing on the "
            "interstate."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "I was standing in the checkout line",
                "with a cart full of things I didn't need",
                "when it hit me like a chord change:",
                "life is mostly beautiful and free.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "And the fluorescent lights were humming B-flat,",
                "and the woman behind me smiled at that.",
            ]},
            {"label": "Chorus", "lines": [
                "Oh, everything is breaking open —",
                "every boring ordinary day,",
                "the parking lots are full of glory,",
                "and I can't stop laughing on the interstate.",
            ]},
            {"label": "Verse 2", "lines": [
                "I called my honey from the driveway,",
                "she said, “babe, your voice sounds really bright.”",
                "I said, “thank you, and also,",
                "I forgot how much I like to drive.”",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "And the neighbor's dog is barking in the key of C,",
                "and I think he might be harmonizing with me.",
            ]},
            {"label": "Chorus", "lines": [
                "Oh, everything is breaking open —",
                "every boring ordinary day,",
                "the parking lots are full of glory,",
                "and I can't stop laughing on the interstate.",
                "I can't stop laughing on the interstate.",
            ]},
            {"label": "Bridge", "lines": [
                "All the tiny stupid miracles",
                "stacking up like receipts in my coat.",
                "I don't need a lot, dear God —",
                "just the spirit and one good note.",
            ]},
            {"label": "Final Chorus", "lines": [
                "Oh, everything is breaking open —",
                "every boring ordinary day,",
                "the parking lots are full of glory,",
                "and I can't stop laughing on the interstate.",
                "I can't stop laughing on the interstate.",
                "OOOOH — gratitude has filled my plate.",
            ]},
        ],
        "refs": ["1 Thessalonians 5:16–18", "James 1:17", "Psalm 118:24"],
    },
    {
        "num": 8,
        "title": "Psalm 147",
        "slug": "psalm-147",
        "about": (
            "A doo-wop elevator out of narcissistic regret — put your eyes above "
            "on the God whose name is love, and get your mind off yourself "
            "completely. (The “One Hundred and Forty Six” track.)"
        ),
        "kind": "verse",
        "blocks": [
            {"label": None, "lines": [
                "What do you tell your busy mind",
                "as you're stuck doing the time",
                "that came with all your crimes?",
            ]},
            {"label": None, "lines": [
                "You've got to watch out for the lies",
                "that stir up all the pride",
                "that got you here to begin with.",
            ]},
            {"label": None, "lines": [
                "There is a kind of despair",
                "that keeps its focus there,",
                "on the human side of living.",
            ]},
            {"label": None, "lines": [
                "A narcissistic regret,",
                "an ego mourning event —",
                "but more self won't cure the wound.",
            ]},
            {"label": None, "lines": [
                "You've got to put your eyes above",
                "to the God whose name is love,",
                "and get your mind off you completely.",
            ]},
            {"label": None, "lines": [
                "One Hundred and Forty-Six Psalms later,",
                "this one's an elevator",
                "to get you off yourself",
                "into God.",
            ]},
        ],
        "refs": ["Psalm 147", "Psalm 146", "Colossians 3:1–2"],
    },
    {
        "num": 9,
        "title": "Your Calamity",
        "slug": "your-calamity",
        "about": (
            "Lady Wisdom claps back — you slept through her call, so now eat the "
            "fruit of your own way. “Your calamity is hilarity to me.” Proverbs 1, "
            "set to a marching-band stomp."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "I'm not your girl —",
                "not your safety net.",
                "You ghosted truth —",
                "that's your big regret.",
                "You're begging now,",
                "and that makes it clear",
                "you think girls like me",
                "commonly appear.",
            ]},
            {"label": "Pre-Chorus", "lines": [
                "Oh, you turned away when the truth was free —",
                "now you're down and out, on your hands and knees.",
                "But wisdom don't play hide-and-seek —",
                "you ignored me once, now the future's bleak.",
            ]},
            {"label": "Chorus", "lines": [
                "Lady Wisdom called",
                "and you slept right through it.",
                "You had your chance",
                "and you blew it.",
                "Eat, eat, eat",
                "the fruit of your way —",
                "fill up on the choices",
                "you made that day.",
            ]},
            {"label": "Verse 2", "lines": [
                "The terror of the storm",
                "brings second thoughts,",
                "so now you call,",
                "now you seek,",
                "as if I'm easy,",
                "as if I'm cheap.",
            ]},
            {"label": "Pre-Chorus 2", "lines": [
                "You chose to sleep, sleep, sleep",
                "through God's display",
                "of His truest kindness —",
                "He sent me walking your way,",
                "but you just kept on",
                "snoring away.",
            ]},
            {"label": "Chorus", "lines": [
                "Lady Wisdom called",
                "and you slept right through it.",
                "You had your chance",
                "and you blew it.",
                "Eat, eat, eat",
                "the fruit of your way —",
                "fill up on the choices",
                "you made that day.",
            ]},
            {"label": "Bridge", "lines": [
                "You shoulda listened —",
                "I wasn't whisperin'.",
                "I was bangin' on your door",
                "like a fire drill hittin'.",
                "You shut me out,",
                "thought you were steady —",
                "now the storm's here",
                "and you ain't ready.",
            ]},
            {"label": "Breakdown", "lines": [
                "Your calamity",
                "is hilarity",
                "to me.",
            ]},
            {"label": "Final Chorus", "lines": [
                "Lady Wisdom called,",
                "but you slept through the moment.",
                "Now you're stuck with the life",
                "'cause you're the one who chose it.",
            ]},
            {"label": "Marching-band breakdown", "lines": [
                "Your calamity, is hilarity, to me.",
                "Your calamity, is hilarity, to me.",
                "Your calamity, is hilarity, to me…",
            ]},
        ],
        "refs": ["Proverbs 1:24–33", "Proverbs 9:1–12", "Proverbs 8:1–11"],
    },
    {
        "num": 10,
        "title": "Transfiguration",
        "slug": "transfiguration",
        "about": (
            "Six days after “take up your cross,” Peter climbs the mountain, sees "
            "the Lord blaze, and loses his vocabulary — “three tents!” No: the "
            "glory was a preview, and the road to radiance runs through the cross."
        ),
        "kind": "verse",
        "blocks": [
            {"label": "Intro — spoken", "lines": [
                "Six days after “take up your cross” —",
                "Pete still tryna skip the dyin' part…",
                "so watch the man climb a mountain",
                "and lose his whole vocabulary.",
            ]},
            {"label": "Verse 1 — climbing, then the light", "lines": [
                "Up the mount, six days countin' from the cross-talk,",
                "three of 'em climbin' — Pete and the brothers, no soft walk.",
                "Then the Man metamorphoō right there in they sight,",
                "face bright as the sun, clothes flashin' white-white —",
                "not bleach-white, light-white, no fuller on the earth",
                "could touch the kinda clean that was leakin' through His shirt.",
                "Then two giants of the canon step up on the stage:",
                "Moses holdin' the Law, Elijah holdin' the page,",
                "and they ain't talkin' weather — peep the topic they choose:",
                "His exodus in Jerusalem — the Cross, then out tha tomb.",
            ]},
            {"label": "Chorus", "lines": [
                "Pete's foot in his mouth 'cause he saw the Lord on the mount,",
                "glory crackin' like thunder and he can't even count —",
                "“three tents!” — nah, the Father cut him off, said it proud:",
                "“This is My beloved Son — listen to HIM” — from the cloud.",
                "(say it again)",
                "Pete's foot in his mouth 'cause he saw the Lord on the mount —",
                "when the King ain't sayin' nothin', boy, that ain't your route;",
                "when the glory got you shook and you don't know how to pray,",
                "zip it — lift your eyes — and let the Father have His say.",
            ]},
            {"label": "Verse 2 — the blunder", "lines": [
                "Now Pete (bless him) got the spirit but the mouth on a hinge:",
                "“Lord, it's good to be here!” — then he oversteps the fringe —",
                "“lemme throw up three booths, three skēnas on the ridge,",
                "one for You, one for Moses, one for 'Lijah — I'll pitch!”",
                "Mark say the man didn't even know what he said,",
                "'cause the terror had him talkin' just to talk through the dread.",
                "But peep the little heresy hidin' in the plan:",
                "three matchin' tents put the servants on par with the Lamb.",
                "You wanna freeze the glory, throw a roof on the flame,",
                "set up camp on the summit — but that ain't why He came.",
                "And the tent you tryna build? Cousin, miss me with the canvas —",
                "the Word already eskēnōsen: pitched flesh as His tabernacle.",
            ]},
            {"label": "Bridge — big, half-time", "lines": [
                "So the cloud roll in and it swallow up the scene,",
                "and the Voice cut through everything that Peter tried to mean:",
                "“Not three — One. Not a booth — a throne.",
                "This is My Son. Now hush. And listen to HIM alone.”",
                "They dropped on they faces, He touched 'em: “rise, don't fear,”",
                "they looked up — Moses gone, Elijah disappeared.",
                "Iēsoun monon: Jesus only, nobody beside.",
                "Law and Prophets took a bow and they stepped to the side.",
            ]},
            {"label": "Verse 3 — coming down", "lines": [
                "Down-down, off the mount, no tent and no plaque, 'cause the",
                "glory was a preview, not a place you unpack. He said,",
                "“tell it to nobody till the Son come back,",
                "risen from the dead” — now watch the timeline crack:",
                "the shine on the summit was a leak from the tomb,",
                "a flash-forward flicker of the resurrection bloom,",
                "the face that lit the mountain gonna be marred in the gloom,",
                "the white no fuller could bleach gonna be stripped in the room —",
                "so the road to the radiance run straight through the pain,",
                "you don't tent on the high, you go low for the gain;",
                "he wanted Tabor frozen, but the path led to the skull —",
                "glory ain't a campsite, it's a Cross, then the pull.",
            ]},
            {"label": "Outro — piano + singing", "lines": [
                "Years down the line, old Pete put the pen to the page:",
                "“we ain't follow no myth, no cleverly-spun stage —",
                "we was eyewitness, saw the Majesty, heard the Voice come loud,",
                "we was with Him… on the holy mountain… in the cloud.”",
                "The man who couldn't shut it on the day of the light",
                "became the witness who could stand up and say it right.",
                "Foot fell outta his mouth — and the mouth told it true:",
                "“This is the Son. I heard it. And I'm tellin' it to you.”",
            ]},
        ],
        "refs": ["Matthew 17:1–8", "Mark 9:2–8", "Luke 9:28–36", "2 Peter 1:16–18", "John 1:14"],
    },
]

# ── Study layer ──
# Drafted by the parallel agent workflow (see common_grace_aids.json) and merged
# into SONGS by slug. facts become (label, value) tuples; moves/terms/discussion/
# contemplation already match the render format in build.py.
import json as _json
import os as _os

_aids_file = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "common_grace_aids.json")
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
