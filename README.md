# Uncle Theology + Vespers

Two sibling audio projects by Chris Oswald (Oswald Records), kept in one repo.

- **[`uncletheology-site/`](uncletheology-site/)** → [uncletheology.com](https://uncletheology.com) — sermon-based AI music: a multi-album discography plus **UncleTheology Radio**, a podcast that turns each album into a whole-album episode with spoken intros.
- **[`vespers-site/`](vespers-site/)** → [vesperstonight.com](https://vesperstonight.com) — a late-night "great ideas" talk podcast (the Syntopicon, Scripture, public-domain great books, a little jazz between segments). *"Small music, big talk"* — the nocturne sibling to UncleTheology Radio.

Both are plain-Python static-site generators (**no framework, standard library only**) deployed to **Cloudflare**. All audio is hosted on **Cloudflare R2** and is **not** stored in this repo.

## Quick start

```bash
# Uncle Theology
cd uncletheology-site && python3 build.py && npx wrangler deploy

# Vespers
cd vespers-site && python3 build.py && npx wrangler deploy
```

**Read [OPERATIONS.md](OPERATIONS.md)** for how everything actually works — the content model, build & deploy, audio hosting, and the YouTube lyric-video pipeline.
