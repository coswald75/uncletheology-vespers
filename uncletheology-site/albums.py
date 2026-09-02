# -*- coding: utf-8 -*-
"""Aggregate every album into one ALBUMS list for the generator.

Each album module exposes ALBUM (metadata dict) and SONGS (list). Here we
attach the songs to the album record and sort by display `order`.
"""

import songs as roots_of_reason
import john_and_them
import barn_dance
import proverbs
import shadys_bach
import common_grace
import that_nazarene
import sovereign_driver
import android_agent

_MODULES = [roots_of_reason, john_and_them, barn_dance, proverbs, shadys_bach, common_grace, that_nazarene, sovereign_driver, android_agent]

ALBUMS = sorted(
    [{**m.ALBUM, "songs": m.SONGS} for m in _MODULES],
    key=lambda a: a.get("order", 99),
)
