# -*- coding: utf-8 -*-
"""Generate YouTube descriptions from the same album data that builds the site
(the 'clone the website onto YouTube' step). Per-song + full-album descriptions
pulled from lyrics/scripture/study-layer. Video rendering is a later stage."""
import sys, importlib, os

SITE = "https://uncletheology.com"
MODS = {  # album-slug -> module name
    "that-nazarene": "that_nazarene", "sovereign-driver": "sovereign_driver",
    "common-grace": "common_grace", "roots-of-reason": "songs",
    "barn-dance": "barn_dance", "proverbs": "proverbs",
    "shadys-bach": "shadys_bach", "john-and-them": "john_and_them",
}

def song_desc(album, s):
    L = []
    L.append(f"{s['title']} — Uncle Theology (Official Lyric Video)")
    L.append("")
    L.append(s.get("about") or s.get("thesis") or "")
    L.append("")
    if s.get("refs"):
        L.append("\U0001F4D6 Scripture: " + " · ".join(s["refs"]))
    terms = s.get("terms") or []
    if terms:
        L.append("")
        L.append("\U0001F511 In this song:")
        for t in terms[:3]:
            L.append(f"• {t['term']} — {t['gloss']}")
    disc = s.get("discussion") or s.get("questions") or []
    if disc:
        L.append("")
        L.append("\U0001F4AC Discussion: " + disc[0])
    L.append("")
    L.append(f"\U0001F310 Lyrics, scripture & study notes: {SITE}/{album['slug']}/{s['slug']}")
    L.append(f"▶ Subscribe: https://youtube.com/@uncletheology\n▶ Full album playlist: [PLAYLIST URL]")
    L.append("\U0001F3A7 Stream everywhere (Spotify/Apple): [SMART LINK]")
    L.append("")
    tag = "".join(w.capitalize() for w in album['title'].split())
    L.append(f"#UncleTheology #{tag} #ChristianMusic #Lyrics #Theology")
    return "\n".join([x for x in L if x is not None]).strip()

def album_desc(album):
    L = [f"{album['title']} — Full Album (Uncle Theology)", "", album.get("blurb","").strip(), "",
         "Tracklist:"]
    for s in album["songs"]:
        L.append(f"[TIME]  {s['num']}. {s['title']}")
    L += ["", f"\U0001F310 Lyrics, scripture & full study notes for every song: {SITE}/{album['slug']}/",
          "\U0001F3A7 Stream everywhere: [SMART LINK]", "",
          "Uncle Theology turns the substance of expository preaching into music.",
          "#UncleTheology #FullAlbum #ChristianMusic"]
    return "\n".join(L).strip()

slug = sys.argv[1] if len(sys.argv) > 1 else "that-nazarene"
m = importlib.import_module(MODS[slug])
album = {**m.ALBUM, "songs": m.SONGS}
out = os.path.join("_youtube_build", slug)
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "_ALBUM.txt"), "w") as f: f.write(album_desc(album))
for s in album["songs"]:
    with open(os.path.join(out, f"{s['num']:02d}-{s['slug']}.txt"), "w") as f:
        f.write(song_desc(album, s))
print(f"wrote {len(album['songs'])} song descriptions + 1 album description to _youtube_build/{slug}/\n")
print("="*70, "\nSAMPLE — track 2:\n", "="*70, sep="")
print(song_desc(album, album["songs"][1]))
