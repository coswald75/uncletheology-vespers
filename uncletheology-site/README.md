# Uncle Theology — uncletheology.com

Static site hosting Chris Oswald's sermon-rooted AI music. Each album is a set
of song pages built in the Sermon Steward player/layout style, in a distinct
dark "reggae-roots" identity.

First album: **Roots of Reason** (12 tracks).

## How it works

- `songs.py` — the album data: per-song title, slug, source `.wav` (for the R2
  upload mapping), an "About" note, verbatim lyrics, and verbatim Scripture
  references (exactly as printed in the booklet).
- `build.py` — renders `public/index.html`, `public/about.html`, and
  `public/songs/<slug>.html`. Run it after any edit to `songs.py`:

  ```sh
  python3 build.py
  ```

- `public/` — the deployable static tree (generated; safe to delete and rebuild).
- `assets/cover.jpg` — album cover (extracted from the booklet PDF); copied into
  `public/assets/` on build.

## Audio

Song audio is served from the existing Cloudflare R2 bucket `sermon-steward-audio`
(public base `https://sermons-cdn.sermonsteward.com`) under the prefix
`uncle-theology/roots-of-reason/<slug>.mp3`.

Upload (one track) with an authenticated wrangler:

```sh
wrangler r2 object put \
  sermon-steward-audio/uncle-theology/roots-of-reason/<slug>.mp3 \
  --file=<local>.mp3 --content-type=audio/mpeg --remote
```

Convert a source `.wav` to web MP3 first:

```sh
ffmpeg -i "Source.wav" -codec:a libmp3lame -b:a 192k "<slug>.mp3"
```

## Deploy

Cloudflare Worker-on-assets (no Worker logic): `wrangler deploy`, or wire the
GitHub repo to a Cloudflare Pages/Workers project with build command
`python3 build.py` and output directory `public`. Bind the custom domain
`uncletheology.com`.
