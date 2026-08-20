#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Canonical UncleTheology Radio episode assembler.

Given an album config (JSON), interleaves talk intros + songs into one MP3 with
chapter markers and an embedded cover, and drops the Providence Community Church
sponsor spot at the MIDPOINT of the album (after the middle song). The pilot
That Nazarene episode was built before the sponsor existed and is intentionally
left without it — every album assembled through this script carries it.

    python3 assemble_episode.py <config.json>

Config shape:
{
  "album_slug":  "common-grace",
  "album_title": "Common Grace",
  "cover":       "public/assets/common-grace/cover.jpg",   # or the 1500 podcast art
  "out":         "_audio_build/common-grace-episode.mp3",
  "segments": [                                             # album order
    {"intro_title": "Intro — Song One", "talk": "/abs/tts_...mp3",
     "song_title":  "Song One",         "song": "_audio_build/common-grace/song-one.mp3"},
    ...
  ]
}
`talk` paths are the ElevenLabs `tts_*.mp3` files captured when voicing the intros.
"""
import os, sys, json, math, subprocess, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SPONSOR = os.path.join(HERE, "_audio_build/sponsor-providence.mp3")
SPONSOR_CHAPTER = "A word from our sponsor — Providence Community Church"

GAP_AFTER_TALK = 0.4   # intro → its song
GAP_AFTER_SONG = 0.9   # song → next intro (and around the sponsor)


def dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=noprint_wrappers=1:nokey=1", path],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def norm(src, dst):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src,
                    "-ar", "44100", "-ac", "2", dst], check=True)


def silence(seconds, dst):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi",
                    "-i", "anullsrc=r=44100:cl=stereo", "-t", str(seconds), dst], check=True)


def fmt(t):
    return f"{int(t // 60)}:{int(t % 60):02d}"


def main(cfg_path):
    with open(cfg_path, encoding="utf-8") as f:
        cfg = json.load(f)
    segments = cfg["segments"]
    n = len(segments)
    # Sponsor drops after the ceil(n/2)-th song → the true midpoint.
    sponsor_after = math.ceil(n / 2)  # 1-based song number
    if not os.path.exists(SPONSOR):
        sys.exit(f"Sponsor spot missing: {SPONSOR}")

    tmp = tempfile.mkdtemp(prefix="utr_")
    sil_talk = os.path.join(tmp, "sil_talk.wav"); silence(GAP_AFTER_TALK, sil_talk)
    sil_song = os.path.join(tmp, "sil_song.wav"); silence(GAP_AFTER_SONG, sil_song)
    sponsor_w = os.path.join(tmp, "sponsor.wav"); norm(SPONSOR, sponsor_w)

    seq, chapters, t = [], [], 0.0
    for i, seg in enumerate(segments):
        talk_w = os.path.join(tmp, f"{i}_talk.wav"); norm(seg["talk"], talk_w)
        song_w = os.path.join(tmp, f"{i}_song.wav"); norm(seg["song"], song_w)

        chapters.append((t, seg["intro_title"]))
        seq.append(talk_w); t += dur(talk_w)
        seq.append(sil_talk); t += GAP_AFTER_TALK

        chapters.append((t, seg["song_title"]))
        seq.append(song_w); t += dur(song_w)

        song_no = i + 1
        if song_no == sponsor_after and song_no != n:
            seq.append(sil_song); t += GAP_AFTER_SONG
            chapters.append((t, SPONSOR_CHAPTER))
            seq.append(sponsor_w); t += dur(sponsor_w)
        if song_no != n:
            seq.append(sil_song); t += GAP_AFTER_SONG

    total = t

    # concat
    listfile = os.path.join(tmp, "list.txt")
    with open(listfile, "w") as f:
        for p in seq:
            f.write(f"file '{p}'\n")
    concat_wav = os.path.join(tmp, "episode.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", listfile, "-c", "copy", concat_wav], check=True)

    # chapters + tags
    meta = os.path.join(tmp, "meta.txt")
    with open(meta, "w") as f:
        f.write(";FFMETADATA1\n")
        f.write(f"title={cfg['album_title']}\n")
        f.write("artist=Uncle Theology\n")
        f.write("album=UncleTheology Radio\n")
        f.write("genre=Podcast\n")
        for idx, (start, title) in enumerate(chapters):
            end = chapters[idx + 1][0] if idx + 1 < len(chapters) else total
            safe = str(title).replace("\\", "\\\\").replace("=", "\\=").replace(";", "\\;").replace("#", "\\#")
            f.write("[CHAPTER]\nTIMEBASE=1/1000\n")
            f.write(f"START={int(start * 1000)}\nEND={int(end * 1000)}\ntitle={safe}\n")

    out = cfg["out"] if os.path.isabs(cfg["out"]) else os.path.join(HERE, cfg["out"])
    cover = cfg["cover"] if os.path.isabs(cfg["cover"]) else os.path.join(HERE, cfg["cover"])
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", concat_wav, "-i", meta, "-i", cover,
        "-map", "0:a", "-map", "2:v", "-map_metadata", "1",
        "-c:a", "libmp3lame", "-b:a", "192k", "-ar", "44100",
        "-c:v", "mjpeg", "-disposition:v", "attached_pic",
        "-metadata:s:v", "title=Album cover", "-id3v2_version", "3", "-write_id3v1", "1",
        out,
    ], check=True)
    shutil.rmtree(tmp, ignore_errors=True)

    print(f"wrote: {out} ({os.path.getsize(out) / 1e6:.1f} MB, {fmt(total)})")
    print(f"sponsor after song #{sponsor_after} of {n}")
    print("\nCHAPTERS (for the album's episode block):")
    for start, title in chapters:
        print(f'            ("{fmt(start)}", "{title}"),')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python3 assemble_episode.py <config.json>")
    main(sys.argv[1])
