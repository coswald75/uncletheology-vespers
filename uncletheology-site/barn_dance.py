# -*- coding: utf-8 -*-
"""
Barn Dance — album data.

Warm folk / barn-dance settings of Scripture and classic hymns. Lyrics
reformatted from BarnDance Lyrics.md: studio/production directions
(“[whispered vocals]”, “[acoustic guitar]”, etc.) dropped, structural section
labels kept as stanza labels, garbled copy-paste cleaned up. Hymn-based tracks
carry attribution to their public-domain authors.

NOTE: cover art (assets/barn-dance/cover.png) pending from Chris. The lyrics
file also contains a 6th song (a Psalm 23 "The LORD my shepherd" setting) with
no matching MP3 yet — omitted here pending Chris's call.
"""

ALBUM = {
    "title": "Barn Dance",
    "slug": "barn-dance",
    "order": 3,
    "tagline": "Uncle Theology · Lyrics & Scripture",
    "blurb": (
        "Scripture and old hymns kicked up into a warm, string-lit barn dance — "
        "Isaiah's courtroom grace, the martyr-hymn's blood-red banner, Bonar's "
        "voice of Jesus, and Psalm 1's tree by the water."
    ),
    "cover": "/assets/barn-dance/cover.png",
    "audio_prefix": "barn-dance",
    # Warm barn-at-night identity — deep warm dark, amber string-light + barn-red ember.
    "theme": {
        "--bg": "#14110c",
        "--bg-2": "#1b1710",
        "--surface": "#221c14",
        "--surface-2": "#2b2317",
        "--rule": "#3e3324",
        "--ink": "#f7efe0",
        "--ink-soft": "#d8cdb8",
        "--ink-faint": "#9c9078",
        "--green": "#e0683a",
        "--green-deep": "#b04a26",
        "--gold": "#f0a93c",
        "--gold-deep": "#c8862a",
        "--link": "#f0a93c",
        "--glow-a": "rgba(240,169,60,0.13)",
        "--glow-b": "rgba(224,104,58,0.08)",
    },
    "episode": {
        "order": 2,
        "title": "Barn Dance — the whole album, sung and explained",
        "guid": "utr-barn-dance-2026-07-22",
        "pubDate": "Thu, 16 Jul 2026 12:00:00 -0500",
        "duration": "27:33",
        "length": 39791250,
        "audio_url": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/barn-dance.mp3",
        "image": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/barn-dance-art.jpg",
        "summary": (
            "Barn Dance played end to end — Scripture and old hymns kicked up into a warm, "
            "string-lit hoedown — with a short spoken intro before every song telling you the "
            "Scripture and the story underneath it. Isaiah's courtroom grace, the peace that tore "
            "down the dividing wall, a metrical Psalm 23, Reginald Heber's martyr-hymn, Horatius "
            "Bonar's threefold invitation, and Psalm 1's tree by the water."
        ),
        "chapters": [
            ("0:00", "Intro — Grace Has Come"),
            ("0:57", "Grace Has Come"),
            ("4:27", "Intro — We're So Glad"),
            ("5:13", "We're So Glad"),
            ("8:58", "Intro — Counting Sheep"),
            ("9:45", "Counting Sheep"),
            ("13:41", "A word from our sponsor — Providence Community Church"),
            ("13:59", "Intro — The Son of God Goes Forth to War"),
            ("14:44", "The Son of God Goes Forth to War"),
            ("18:56", "Intro — Come to Me"),
            ("19:37", "Come to Me"),
            ("23:15", "Intro — Psalm 1"),
            ("24:06", "Psalm 1"),
        ],
    },
}

SONGS = [
    {
        "num": 1,
        "title": "Grace Has Come",
        "slug": "grace-has-come",
        "about": (
            "Isaiah's courtroom invitation — “come now, let us reason together” — "
            "over a barn-dance shuffle: though your sins are scarlet, grace has "
            "come through the Son."
        ),
        "thesis": (
            "Isaiah’s courtroom invitation — “come now, let us reason together” — "
            "turns the sinner’s scarlet to snow: grace has come through the Son "
            "who bore our straying."
        ),
        "facts": [
            ("Doctrine", "Justification · Grace"),
            ("Anchor text", "Isaiah 1:18 · Isaiah 53:6"),
            ("Form", "Barn-dance shuffle"),
            ("Voices", "The prophet Isaiah"),
        ],
        "moves": [
            {"label": "Come and reason", "text": "The Holy One’s courtroom summons isn’t to condemn but to cleanse: “come now, let us reason together” (Isaiah 1:18)."},
            {"label": "Scarlet to snow", "text": "Though sins are scarlet and crimson, they’ll be white as snow and wool — a permanent dye undone (Isaiah 1:18)."},
            {"label": "The straying laid on Him", "text": "“All we like sheep have gone astray… the Lord did send the Son to pay” (Isaiah 53:6)."},
            {"label": "Grace has come", "text": "The verdict — through the Son; the cross proves God’s readiness to forgive (2 Corinthians 5:18–21)."},
        ],
        "terms": [
            {"term": "“Come now, let us reason together”", "gloss": "Isaiah 1:18 (KJV cadence) — a legal “let’s settle this in court” summons that ends not in sentence but in pardon."},
            {"term": "“scarlet… crimson… snow… wool”", "gloss": "Isaiah 1:18’s color imagery; scarlet and crimson dyes were famously permanent, which makes the whitening a miracle."},
            {"term": "“all we like sheep”", "gloss": "Isaiah 53:6 — the Suffering Servant bearing the iniquity of the strays (the line Handel’s Messiah made famous)."},
            {"term": "“God is more ready to forgive than you are to be forgiven”", "gloss": "A sentiment common in Puritan devotion; the song’s spoken coda adds, “and the cross proves it.”"},
        ],
        "discussion": [
            "Isaiah frames forgiveness as a courtroom “reasoning.” How does picturing it as a legal settlement — not just a feeling — change the gospel for you?",
            "“God is more ready to forgive than you are to be forgiven.” Do you actually believe that? Where do we resist being forgiven?",
            "Scarlet dye was permanent. What “permanent” stain do people assume is beyond grace?",
        ],
        "contemplation": [
            "What scarlet are you carrying that you doubt can become snow?",
            "Are you more reluctant to be forgiven than God is to forgive you?",
            "Sit with “the Lord did send the Son to pay.” What does that cost say about the love?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Intro", "lines": [
                "Come now and reason with me,",
                "come now and reason with me —",
                "that’s what the Holy One’s broadcasting.",
            ]},
            {"label": "Verse 1", "lines": [
                "Though your sins are like scarlet,",
                "they will be white as snow;",
                "though they be red like crimson,",
                "they shall be as wool.",
            ]},
            {"label": None, "lines": [
                "Come now and reason with me —",
                "are you hearing what He’s saying?",
            ]},
            {"label": "Verse 2", "lines": [
                "All we like sheep have gone astray,",
                "each of us turned to his own way,",
                "but the Lord — oh, the Lord —",
                "but the Lord — oh, the Lord —",
                "did send the Son to pay.",
            ]},
            {"label": "Chorus", "lines": [
                "Grace has come, through the Son.",
                "Grace has come, through the Son.",
                "Grace has come, through the Son.",
                "Grace has come, through the Son.",
            ]},
            {"label": "Coda — Spoken Word", "lines": [
                "Someone once said that God is more ready to forgive than you are to be forgiven — and the cross proves it. Come now, let us reason together… Grace has come. Through the Son…",
            ]},
        ],
        "refs": [
            "Isaiah 1:18",
            "Isaiah 53:6",
            "2 Corinthians 5:18–21",
        ],
    },
    {
        "num": 2,
        "title": "We’re So Glad",
        "slug": "were-so-glad",
        "about": (
            "A celebration of the gospel of peace: You preached peace to us who "
            "were far off, tore down the dividing wall — now every breath is a "
            "thank-you."
        ),
        "thesis": (
            "The gospel of peace turned strangers into family: He preached peace "
            "to those far off, tore down the dividing wall, and now every breath "
            "is a thank-you."
        ),
        "facts": [
            ("Doctrine", "Reconciliation · Gospel of peace"),
            ("Anchor text", "Ephesians 2:13–17"),
            ("Form", "Hand-clap gospel"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "Peace to the far off", "text": "He came and preached peace when we were far off, walked in our dust, and brought our hearts back home (Ephesians 2:13, 17)."},
            {"label": "The wall torn down", "text": "He tore down the walls standing in our way, carried our shame, wrote a brand-new day (Ephesians 2:14–15)."},
            {"label": "All the work done", "text": "He did all the work just to get us to this place; now all we have to do is get up and celebrate (Ephesians 2:8–9)."},
            {"label": "Every song is grace", "text": "He paid the price, made the way; now every song is grace on display (Hebrews 13:15)."},
        ],
        "terms": [
            {"term": "“preached peace when we were far off”", "gloss": "Ephesians 2:17, quoting Isaiah 57:19; the “far off” are the Gentiles, brought near by the blood of Christ."},
            {"term": "“tore down the walls”", "gloss": "Ephesians 2:14 — the “dividing wall of hostility,” an image drawn from the temple barrier that fenced Gentiles out."},
            {"term": "“come, find rest”", "gloss": "Matthew 11:28, the invitation humming under the celebration."},
            {"term": "“bring this offering… every breath a thank-you”", "gloss": "The “sacrifice of praise” of Hebrews 13:15 — worship as gratitude, not payment."},
        ],
        "discussion": [
            "The song is almost pure celebration. When does worship rightly become a party, and when do we make it too solemn?",
            "“He has done all the work… now all we have to do is celebrate.” How does that guard worship against works-righteousness?",
            "Who are the “far off” in your community that the gospel of peace is meant to bring near?",
        ],
        "contemplation": [
            "Do you live more like someone earning God’s favor or someone celebrating it?",
            "What “dividing wall” has Christ torn down in your own life?",
            "Could every breath today actually be “a thank-you”?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "You came and preached peace when we were far off,",
                "You didn’t give up, You didn’t lose hope,",
                "You walked in our dust, felt the weight we hold,",
                "You called us Your own, brought our hearts back home.",
            ]},
            {"label": "Chorus", "lines": [
                "We’re so blessed to get to bring this offering",
                "(ba-ba-ba-ba-ba-ba-ba-ba)",
                "We’re so blessed You’ve given what we need to sing",
                "(ba-ba-ba-ba-ba-ba-ba-ba)",
                "You have done all the work just to get us to this place,",
                "and now all we have to do is get up and celebrate.",
                "(da-da-da-da-da-da-da-da-da-da-da-da-da-da-da-da)",
            ]},
            {"label": "Verse 2", "lines": [
                "You tore down the walls standing in our way,",
                "You carried our shame, wrote a brand-new day,",
                "You opened the door, said “come, find rest,”",
                "now every breath we breathe is a thank-You, yes.",
            ]},
            {"label": "Chorus", "lines": [
                "We’re so blessed to get to bring this offering",
                "(ba-ba-ba-ba-ba-ba-ba-ba)",
                "We’re so blessed You’ve given what we need to sing",
                "(ba-ba-ba-ba-ba-ba-ba-ba)",
                "You have done all the work just to get us to this place,",
                "and now all we have to do is get up and celebrate.",
                "(da-da-da-da-da-da-da-da-da-da-da-da-da-da-da-da)",
            ]},
            {"label": "Bridge", "lines": [
                "You paid the price, You made the way,",
                "You changed our hearts, You taught us praise.",
                "You paid the price, You made the way,",
                "now every song is grace on display. (oh-oh)",
            ]},
            {"label": "Chorus", "lines": [
                "We’re so blessed to get to bring this offering",
                "(ba-ba-ba-ba-ba-ba-ba-ba)",
                "We’re so blessed You’ve given what we need to sing",
                "(ba-ba-ba-ba-ba-ba-ba-ba)",
                "You have done all the work just to get us to this place,",
                "and now all we have to do is get up and celebrate.",
                "(da-da-da-da-da-da-da-da-da-da-da-da-da-da-da-da)",
            ]},
        ],
        "refs": [
            "Ephesians 2:13–17",
            "Matthew 11:28",
            "Hebrews 13:15",
        ],
    },
    {
        "num": 3,
        "title": "Counting Sheep",
        "slug": "counting-sheep",
        "about": (
            "A metrical Psalm 23 with choruses woven from Isaiah 53, John 10, and "
            "1 Peter 2 — the wandering sheep gathered safely home by the Shepherd "
            "who lays down His life for them."
        ),
        "thesis": (
            "A metrical Psalm 23 whose choruses gather Isaiah 53, John 10, and "
            "1 Peter 2 — the strays counted and carried home by the Shepherd who "
            "lays down His life."
        ),
        "facts": [
            ("Doctrine", "Providence · Atonement · The Good Shepherd"),
            ("Anchor text", "Psalm 23 · John 10"),
            ("Form", "Country waltz"),
            ("Voices", "—"),
        ],
        "moves": [
            {"label": "The Shepherd guards", "text": "Psalm 23 in meter: green pastures, still waters, the valley, the table, the house of the Lord (Psalm 23)."},
            {"label": "The strays (Isaiah 53)", "text": "“We all like sheep have gone astray… the Lord laid all our guilt on Him” (Isaiah 53:6)."},
            {"label": "The Good Shepherd (John 10)", "text": "He gives His life for the sheep, knows their names, and leads them safely home (John 10:11–16)."},
            {"label": "Returned (1 Peter 2)", "text": "“You were like a wandering lamb, but now are safely led” to the Shepherd and Overseer of your souls (1 Peter 2:24–25)."},
        ],
        "terms": [
            {"term": "metrical psalm", "gloss": "The tradition (Scottish Psalter, Isaac Watts) of setting the Psalms to singable meter; “The LORD my shepherd guards my soul” echoes “The Lord’s My Shepherd.”"},
            {"term": "“we all like sheep have gone astray”", "gloss": "Isaiah 53:6 — the line Handel’s Messiah made famous, here the recurring chorus."},
            {"term": "“He knows their names”", "gloss": "John 10:3 — the shepherd calls his own sheep by name; they’re known, not just counted."},
            {"term": "“the Shepherd and Overseer of your souls”", "gloss": "1 Peter 2:25 — the wandering lamb returned to its keeper."},
            {"term": "rod and staff", "gloss": "Psalm 23:4 — the shepherd’s two tools, one for defense and one for guidance."},
        ],
        "discussion": [
            "The song layers Psalm 23 with Isaiah 53, John 10, and 1 Peter 2. How does seeing one psalm “answered” across the canon deepen it?",
            "“He knows their names.” What does being known by name — not just counted — mean for how you see yourself before God?",
            "Psalm 23 includes the valley of the shadow. How is the Shepherd’s care proven there, not only in green pastures?",
        ],
        "contemplation": [
            "Where have you “gone astray, each to his own way”?",
            "Can you hear the Shepherd calling you by name?",
            "Which line of Psalm 23 do you most need today — rest, restoration, the valley, the table, or the house of the Lord?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "The LORD my shepherd guards my soul;",
                "I shall not be in need.",
                "In pastures green He lets me rest,",
                "by waters calm He leads.",
            ]},
            {"label": "Chorus — Isaiah 53", "lines": [
                "We all like sheep have gone astray,",
                "each one has turned his way;",
                "the LORD laid all our guilt on Him,",
                "to make an end of all our sin.",
            ]},
            {"label": "Verse 2", "lines": [
                "He does restore my weary soul",
                "and guides me in His ways,",
                "for His own name and faithfulness,",
                "for righteousness and praise.",
            ]},
            {"label": "Chorus — John 10", "lines": [
                "The Shepherd gives His life for sheep,",
                "the flock He calls His own;",
                "He knows their names, they know His voice,",
                "and leads them safely home.",
            ]},
            {"label": "Verse 3", "lines": [
                "Though through death’s shadowed vale I walk,",
                "no evil will I fear;",
                "Your rod and staff, they comfort me,",
                "for You, O LORD, are near.",
            ]},
            {"label": "Chorus — Isaiah 53", "lines": [
                "We all like sheep have gone astray,",
                "each one has turned his way;",
                "the LORD laid all our guilt on Him,",
                "to make an end of all our sin.",
            ]},
            {"label": "Verse 4", "lines": [
                "You spread a feast before my foes;",
                "my head with oil You bless.",
                "My cup runs over — surely good",
                "and mercy shall me press.",
            ]},
            {"label": "Chorus — 1 Peter 2", "lines": [
                "For you were like a wandering lamb,",
                "but now are safely led;",
                "returned unto the Shepherd’s care,",
                "protected by His hand.",
            ]},
            {"label": "Verse 5", "lines": [
                "Your goodness and Your covenant love",
                "will surely follow me;",
                "I’ll dwell within the house of God",
                "through all eternity.",
            ]},
            {"label": "Final Chorus — John 10 (very soft)", "lines": [
                "The Shepherd gives His life for sheep,",
                "the flock He calls His own;",
                "He knows their names, they know His voice,",
                "and leads them safely home.",
            ]},
        ],
        "refs": [
            "Psalm 23",
            "Isaiah 53:6",
            "John 10:11–16",
            "1 Peter 2:24–25",
        ],
    },
    {
        "num": 4,
        "title": "The Son of God Goes Forth to War",
        "slug": "the-son-of-god-goes-forth-to-war",
        "about": (
            "Reginald Heber’s martyr-hymn recharged — the blood-red banner, "
            "Stephen the first martyr, the glorious band: who follows in His "
            "train?"
        ),
        "thesis": (
            "Reginald Heber’s martyr-hymn, recharged: the Son goes to war for a "
            "crown by way of the cross — and the question rings down the "
            "centuries, who follows in His train?"
        ),
        "facts": [
            ("Doctrine", "Discipleship · Martyrdom"),
            ("Anchor text", "Revelation 19 · Acts 7"),
            ("Form", "Anthemic stomp"),
            ("Voices", "Reginald Heber"),
        ],
        "moves": [
            {"label": "The blood-red banner", "text": "The Son goes forth to war, a crown to gain; but the way to the crown runs through the cup of woe (Revelation 19:11–14; Mark 10:38)."},
            {"label": "The martyr first", "text": "Stephen, “whose eagle eye could pierce beyond the grave,” praying for his killers with pardon on his tongue (Acts 7:54–60)."},
            {"label": "The glorious band", "text": "The twelve and the great cloud who “mocked the cross and flame,” bowing their necks to feel the death (Hebrews 12:1)."},
            {"label": "The global army", "text": "Men and boys, matron and maid, climbing the steep ascent of heaven — “to us may grace be given to follow in their train” (Revelation 7:9)."},
        ],
        "terms": [
            {"term": "Reginald Heber", "gloss": "Anglican bishop of Calcutta (1783–1826) who wrote this hymn — and also “Holy, Holy, Holy.”"},
            {"term": "“the martyr first, whose eagle eye”", "gloss": "Stephen, the first Christian martyr (Acts 7), who saw heaven opened and prayed for the men stoning him."},
            {"term": "“the tyrant’s brandished steel / the lion’s gory mane”", "gloss": "The arena martyrdoms of the early church — sword and beast."},
            {"term": "“who follows in His train?”", "gloss": "The hymn’s refrain; a king’s “train” is the procession or retinue that follows him."},
            {"term": "“the steep ascent of heaven”", "gloss": "Heber’s image for the costly, upward path of discipleship."},
        ],
        "discussion": [
            "Heber roots discipleship in martyrdom — “who best can drink His cup of woe.” Has comfortable Christianity lost this register?",
            "Stephen prayed for the men killing him. What does that kind of forgiveness require?",
            "The hymn ends pleading that “grace be given” to follow. Why grace, and not just resolve?",
        ],
        "contemplation": [
            "“Who follows in His train?” — what would following actually cost you?",
            "Where are you asked to “drink His cup of woe,” even in a small way, right now?",
            "Could you, like Stephen, pray for someone actively wronging you?",
        ],
        "attribution": {
            "text": (
                "The verses adapt Reginald Heber’s 1812 hymn “The Son of God "
                "Goes Forth to War” (public domain); the driving “Who follows?” "
                "chorus is added."
            ),
            "links": [
                ("About Reginald Heber", "https://en.wikipedia.org/wiki/Reginald_Heber"),
            ],
        },
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "The Son of God goes forth to war,",
                "a kingly crown to gain;",
                "His blood-red banner streams afar —",
                "who follows in His train?",
                "Who best can drink His cup of woe,",
                "triumphant over pain,",
                "who patient bears his cross below —",
                "he follows in His train.",
            ]},
            {"label": "Chorus", "lines": [
                "Who follows? Who follows?",
                "Who follows in His train?",
                "Through fire and sword and martyrs’ blood —",
                "who follows in His train?",
            ]},
            {"label": "Verse 2", "lines": [
                "The martyr first, whose eagle eye",
                "could pierce beyond the grave,",
                "who saw his Master in the sky",
                "and called on Him to save;",
                "like Him, with pardon on his tongue",
                "in midst of mortal pain,",
                "he prayed for them that did the wrong —",
                "who follows in his train?",
            ]},
            {"label": "Chorus", "lines": [
                "Who follows? Who follows?",
                "Who follows in His train?",
                "Through fire and sword and martyrs’ blood —",
                "who follows in His train?",
            ]},
            {"label": "Verse 3", "lines": [
                "A glorious band, the chosen few",
                "on whom the Spirit came,",
                "twelve valiant saints, their hope they knew",
                "and mocked the cross and flame;",
                "they met the tyrant’s brandished steel,",
                "the lion’s gory mane,",
                "they bowed their necks the death to feel —",
                "who follows in their train?",
            ]},
            {"label": "Chorus", "lines": [
                "Who follows? Who follows?",
                "Who follows in His train?",
                "Through fire and sword and martyrs’ blood —",
                "who follows in His train?",
            ]},
            {"label": "Verse 4", "lines": [
                "A global army, men and boys,",
                "the matron and the maid,",
                "around the Saviour’s throne rejoice",
                "in robes of light arrayed;",
                "they climbed the steep ascent of heaven",
                "through peril, toil, and pain —",
                "O God, to us may grace be given",
                "to follow in their train.",
            ]},
            {"label": "Final Chorus", "lines": [
                "Who follows? Who follows?",
                "Who follows in His train?",
                "Through fire and sword and martyrs’ blood —",
                "who follows in His train?",
            ]},
        ],
        "refs": [
            "Revelation 19:11–14",
            "Acts 7:54–60",
            "Matthew 16:24",
            "Hebrews 12:1",
        ],
    },
    {
        "num": 5,
        "title": "Come to Me",
        "slug": "come-to-me",
        "about": (
            "Horatius Bonar’s “I heard the voice of Jesus say” as a jazz duet — "
            "rest, living water, and light — answered by Christ’s own invitation: "
            "“Come to Me.”"
        ),
        "thesis": (
            "Horatius Bonar’s three invitations — rest, living water, light — "
            "answered by Christ’s own “Come to Me”: the weary lay down their "
            "burden and find a yoke that’s kind."
        ),
        "facts": [
            ("Doctrine", "Rest in Christ · Grace"),
            ("Anchor text", "Matthew 11:28–30"),
            ("Form", "Jazz duet"),
            ("Voices", "Horatius Bonar"),
        ],
        "moves": [
            {"label": "Come and rest", "text": "“I heard the voice of Jesus say, come unto Me and rest”; the weary and worn find a resting-place (Matthew 11:28)."},
            {"label": "Come and drink", "text": "The living water freely given to the thirsty; the soul revived (John 4:13–14; 7:37)."},
            {"label": "Come to the light", "text": "“I am this dark world’s light”; look to Him and the whole day grows bright (John 8:12)."},
            {"label": "The kind yoke", "text": "The chorus: My yoke is kind, My burden light, and rest is waiting there (Matthew 11:29–30)."},
        ],
        "terms": [
            {"term": "Horatius Bonar", "gloss": "Scottish minister (1808–1889), the “prince of Scottish hymn-writers,” who wrote “I Heard the Voice of Jesus Say” (1846)."},
            {"term": "three invitations", "gloss": "Bonar built the hymn on Christ’s threefold “come” — for rest, for living water, and for light — each met by the singer’s response."},
            {"term": "living water", "gloss": "John 4:13–14 (the woman at the well) and John 7:37, “if anyone thirsts, let him come to Me and drink.”"},
            {"term": "“this dark world’s light”", "gloss": "John 8:12 — “I am the light of the world.”"},
            {"term": "“My yoke is kind, My burden light”", "gloss": "Matthew 11:30; the song renders Jesus’ “easy” yoke as “kind.”"},
        ],
        "discussion": [
            "Bonar pairs each invitation with a response (“I came… I drank… I looked”). Why does the song insist on our response, not just Christ’s offer?",
            "Jesus offers a “yoke” as rest. How is taking on a yoke restful rather than burdensome?",
            "Where do weary people today look for rest, water, and light instead of Christ?",
        ],
        "contemplation": [
            "Which of the three do you need most right now — rest, water, or light?",
            "What weight are you carrying that He’s inviting you to lay down?",
            "Have you “come,” or are you still admiring the invitation from a distance?",
        ],
        "attribution": {
            "text": (
                "The verses are Horatius Bonar’s 1846 hymn “I Heard the Voice of "
                "Jesus Say” (public domain); the “Come to Me” chorus draws on "
                "Jesus’ words in Matthew 11."
            ),
            "links": [
                ("About Horatius Bonar", "https://en.wikipedia.org/wiki/Horatius_Bonar"),
            ],
        },
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1 — female jazz singer", "lines": [
                "I heard the voice of Jesus say,",
                "“Come unto Me and rest;",
                "lay down, thou weary one, lay down",
                "thy head upon My breast.”",
                "I came to Jesus as I was,",
                "weary and worn and sad;",
                "I found in Him a resting-place,",
                "and He has made me glad.",
            ]},
            {"label": "Chorus — male singer", "lines": [
                "Come to Me, you weary souls,",
                "lay down the weight you bear;",
                "My yoke is kind, My burden light,",
                "and rest is waiting there.",
            ]},
            {"label": "Verse 2 — female jazz singer", "lines": [
                "I heard the voice of Jesus say,",
                "“Behold, I freely give",
                "the living water; thirsty one,",
                "stoop down, and drink, and live.”",
                "I came to Jesus, and I drank",
                "of that life-giving stream;",
                "my thirst was quenched, my soul revived,",
                "and now I live in Him.",
            ]},
            {"label": "Chorus — male singer", "lines": [
                "Come to Me, you weary souls,",
                "lay down the weight you bear;",
                "My yoke is kind, My burden light,",
                "and rest is waiting there.",
            ]},
            {"label": "Verse 3 — female jazz singer", "lines": [
                "I heard the voice of Jesus say,",
                "“I am this dark world’s light;",
                "look unto Me, thy morn shall rise,",
                "and all thy day be bright.”",
                "I looked to Jesus, and I found",
                "in Him my star, my sun;",
                "and in that light of life I’ll walk",
                "till traveling days are done.",
            ]},
            {"label": "Chorus — male singer", "lines": [
                "Come to Me, you weary souls,",
                "lay down the weight you bear;",
                "My yoke is kind, My burden light,",
                "and rest is waiting there.",
            ]},
        ],
        "refs": [
            "Matthew 11:28–30",
            "John 4:13–14",
            "John 8:12",
        ],
    },
    {
        "num": 6,
        "title": "Psalm 1",
        "slug": "psalm-1",
        "about": (
            "Psalm 1 as a barn-dance romp — the blessed man like a tree by the "
            "water against the wicked like chaff: be a person of roots, not of "
            "wind."
        ),
        "thesis": (
            "Psalm 1’s two ways set to a barn-dance: the blessed are a tree by the "
            "water, the wicked are chaff in the wind — so be a person of roots, "
            "not of wind."
        ),
        "facts": [
            ("Doctrine", "The two ways · Wisdom"),
            ("Anchor text", "Psalm 1 · Jeremiah 17:7–8"),
            ("Form", "Hoedown"),
            ("Voices", "Isaac Watts (the closing turn)"),
        ],
        "moves": [
            {"label": "The blessed man’s “no”", "text": "He won’t walk, stand, or sit with the scornful; his delight is the law, muttered day and night (Psalm 1:1–2)."},
            {"label": "The tree transplanted", "text": "Planted by the stream, bearing fruit in season, leaf evergreen, prospering in all he does (Psalm 1:3; Jeremiah 17:8)."},
            {"label": "Chaff in the wind", "text": "The wicked have no root or ground; like chaff, they won’t stand when judgment rises (Psalm 1:4–5)."},
            {"label": "The roots prayer", "text": "“Plant me where Your waters run… a tree that bends but will not break” (Psalm 1:6)."},
        ],
        "terms": [
            {"term": "the two ways", "gloss": "Psalm 1’s structure — the way of the righteous versus the way of the wicked — a doorway framing the whole Psalter."},
            {"term": "“he turns it day and night” (muttering the law)", "gloss": "Psalm 1:2; the Hebrew hagah means to mutter or murmur under the breath — an ancient way of meditating on Scripture."},
            {"term": "“tree planted by streams of water”", "gloss": "Psalm 1:3, paired here with Jeremiah 17:7–8’s identical image of the one who trusts the Lord."},
            {"term": "“chaff the wind drives away”", "gloss": "Psalm 1:4 — chaff is the worthless husk blown off when grain is threshed."},
            {"term": "the “Watts turn”", "gloss": "The final verse turns to prayer in the manner of Isaac Watts, who famously paraphrased the Psalms into English hymns."},
        ],
        "discussion": [
            "Psalm 1 says delight — not just duty — in God’s word is the root of the blessed life. How do you cultivate delight, not only discipline?",
            "The wicked aren’t painted as villains, just rootless “chaff.” How is rootlessness its own kind of judgment?",
            "“Roots, not wind.” What practices actually put roots down deep?",
        ],
        "contemplation": [
            "Are you currently more “tree” or “chaff” — rooted, or blown about?",
            "What are you “muttering… day and night”? What fills your idle thoughts?",
            "Where do you need to be “transplanted… beside the channeled stream”?",
        ],
        "kind": "verse",
        "blocks": [
            {"label": "Verse 1", "lines": [
                "That man is blessed who will not walk",
                "where godless counselors lead,",
                "that man is blessed who will not walk",
                "where godless counselors lead,",
                "who will not stand where sinners gather",
                "or sit where cynics feed.",
                "His joy is in the law of God,",
                "he turns it day and night —",
                "he mutters truth beneath his breath",
                "and finds it his delight.",
            ]},
            {"label": "Verse 2", "lines": [
                "He shall be like a tree transplanted",
                "beside the channeled stream,",
                "that bears its fruit in every season,",
                "its leaf an evergreen.",
                "And everything he sets his hand to",
                "shall prosper by God’s will —",
                "a life of roots and ordered harvest,",
                "of water, deep and still.",
            ]},
            {"label": "Chorus", "lines": [
                "Blessed is the man, blessed is the man,",
                "whose roots drink deep and hold —",
                "the LORD knows the way of the righteous,",
                "and the wicked way grows cold.",
            ]},
            {"label": "Verse 3", "lines": [
                "The wicked are not built like this —",
                "they have no root or ground.",
                "Like chaff the threshing floor discards them,",
                "like dust the wind has found.",
                "They will not stand when judgment rises",
                "or sit among the just —",
                "their confidence, their name, their standing",
                "returns to scattered dust.",
            ]},
            {"label": "Chorus", "lines": [
                "Blessed is the man, blessed is the man,",
                "whose roots drink deep and hold —",
                "the LORD knows the way of the righteous,",
                "and the wicked way grows cold.",
            ]},
            {"label": "Verse 4 — Guardrail / Watts Turn", "lines": [
                "So let me be a man of roots",
                "and not a man of wind,",
                "who feeds on what will last forever",
                "and starves what feeds on sin.",
                "LORD, plant me where Your waters run,",
                "and let me grow down deep —",
                "a tree that bends but will not break,",
                "whose fruit is Yours to reap.",
            ]},
            {"label": "Final Chorus", "lines": [
                "Blessed is the man, blessed is the man,",
                "whose roots drink deep and hold —",
                "the LORD knows the way of the righteous,",
                "and the wicked way grows cold.",
            ]},
        ],
        "refs": [
            "Psalm 1",
            "Jeremiah 17:7–8",
        ],
    },
]
