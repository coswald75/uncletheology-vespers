# -*- coding: utf-8 -*-
"""
Uncle Theology — static-site generator for uncletheology.com.

Multi-album discography:
  public/index.html                       → discography landing (album cards)
  public/about.html                       → about page
  public/<album-slug>/index.html          → one album page (hero + whole-album
                                            player + "Study the songs" tracklist)
  public/<album-slug>/<song-slug>.html    → one song page

Each album can override the base palette (album["theme"]) for its own identity.
Audio is served from R2 at sermons-cdn.sermonsteward.com/uncle-theology/<prefix>/.

    python3 build.py
"""

import html
import json
import os
import re
import shutil

from albums import ALBUMS

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
SRC_ASSETS = os.path.join(HERE, "assets")

AUDIO_ROOT = "https://sermons-cdn.sermonsteward.com/uncle-theology"
SITE_NAME = "Uncle Theology"
SITE_URL = "https://uncletheology.com"
DEFAULT_OG_IMAGE = SITE_URL + "/assets/john-and-them/cover.png"

# Translation for the hover-tooltip Scripture text (Logos RefTagger).
# Switch to "NIV" to use the NIV instead — RefTagger handles the licensing.
BIBLE_VERSION = "ESV"

# ─────────────────────────── shared chrome ───────────────────────────

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&'
    'family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
)

CSS = """
  :root {
    --bg:         #0d0f0c;
    --bg-2:       #14170f;
    --surface:    #1a1e15;
    --surface-2:  #222719;
    --rule:       #333a28;
    --ink:        #f3efe2;
    --ink-soft:   #cfcab4;
    --ink-faint:  #8f9079;
    --green:      #3bb24a;
    --green-deep: #1f7a33;
    --gold:       #f4c430;
    --gold-deep:  #c9962a;
    --link:       #f4c430;
    --glow-a:     rgba(59,178,74,0.10);
    --glow-b:     rgba(244,196,48,0.06);
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0; padding: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: "Fraunces", "Iowan Old Style", Georgia, serif;
    font-size: 18px; line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }
  body {
    background:
      radial-gradient(1200px 600px at 50% -8%, var(--glow-a), transparent 60%),
      radial-gradient(900px 500px at 90% 0%, var(--glow-b), transparent 55%),
      var(--bg);
    min-height: 100vh;
  }
  .ui { font-family: "Inter", system-ui, -apple-system, sans-serif; }
  a { color: var(--link); text-underline-offset: 2px; }

  .flag-rule { height: 4px; border: 0; margin: 0;
    background: linear-gradient(90deg, var(--green) 0 50%, var(--gold) 50% 100%); }

  /* header */
  .site-header { border-bottom: 1px solid var(--rule); background: rgba(13,15,12,0.7);
    backdrop-filter: blur(6px); position: sticky; top: 0; z-index: 10; }
  .site-header-inner { max-width: 1040px; margin: 0 auto; padding: 14px 24px;
    display: flex; align-items: center; justify-content: space-between; gap: 18px; }
  .site-brand { font-weight: 700; font-size: 19px; letter-spacing: -0.01em;
    color: var(--ink); text-decoration: none; }
  .site-brand .dot { color: var(--gold); }
  .site-nav { display: flex; gap: 22px; }
  .site-nav a { font-family: "Inter", sans-serif; font-size: 13px; font-weight: 500;
    color: var(--ink-soft); text-decoration: none; letter-spacing: 0.02em; }
  .site-nav a:hover { color: var(--gold); }

  main { max-width: 820px; margin: 0 auto; padding: 44px 24px 120px; }

  /* ───── discography landing ───── */
  .disco-intro { margin-bottom: 40px; }
  .disco-eyebrow { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.18em; color: var(--gold); margin-bottom: 12px; }
  .disco-title { font-size: 52px; line-height: 1.02; font-weight: 700; letter-spacing: -0.02em;
    margin: 0 0 14px; }
  .disco-blurb { font-size: 19px; color: var(--ink-soft); margin: 0; max-width: 56ch; }
  /* Radio page */
  .sub-row { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 26px; }
  .sub-btn { display: inline-flex; align-items: center; gap: 8px; font-family: "Inter", sans-serif;
    font-size: 14px; font-weight: 600; letter-spacing: 0.01em; padding: 12px 20px;
    border-radius: 999px; border: 1px solid transparent; cursor: pointer; text-decoration: none;
    color: #fff; }
  .sub-btn .sub-ico { font-size: 15px; }
  .sub-btn.apple { background: #9933cc; }
  .sub-btn.apple:hover { background: #8a1fc4; }
  .sub-btn.spotify { background: #1db954; color: #06210f; }
  .sub-btn.spotify:hover { background: #1ed760; }
  .sub-btn.spotify.soon { background: transparent; color: var(--ink-faint);
    border-color: var(--rule); cursor: default; }
  .sub-btn.rss { background: transparent; color: var(--ink-soft); border-color: var(--rule); }
  .sub-btn.rss:hover { border-color: var(--gold); color: var(--gold); }
  .sub-note { min-height: 20px; margin-top: 12px; font-size: 13px; color: var(--ink-faint);
    word-break: break-all; }

  .ep-list { display: flex; flex-direction: column; gap: 26px; margin-top: 8px; }
  .ep-card { background: var(--surface); border: 1px solid var(--rule); border-radius: 16px;
    padding: 22px 24px; }
  .ep-head { display: flex; gap: 20px; align-items: flex-start; }
  .ep-art { width: 130px; height: 130px; border-radius: 10px; object-fit: cover; flex: 0 0 auto;
    box-shadow: 0 6px 20px rgba(0,0,0,0.35); }
  .ep-meta { flex: 1 1 auto; min-width: 0; }
  .ep-eyebrow { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.14em; }
  .ep-title { font-size: 27px; line-height: 1.08; font-weight: 700; margin: 6px 0 10px; }
  .ep-summary { font-size: 15px; color: var(--ink-soft); margin: 0 0 10px; }
  .ep-studylink { font-size: 13px; font-weight: 600; color: var(--gold); text-decoration: none; }
  .ep-studylink:hover { text-decoration: underline; }
  .ep-audio { width: 100%; margin-top: 18px; }
  .ch-label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em;
    color: var(--ink-faint); margin: 18px 0 8px; }
  .ep-chapters { list-style: none; margin: 0; padding: 0; display: grid;
    grid-template-columns: repeat(2, 1fr); gap: 2px 18px; }
  .ep-chapters .ch { display: flex; align-items: baseline; gap: 12px; width: 100%; text-align: left;
    background: none; border: 0; cursor: pointer; padding: 7px 8px; border-radius: 7px;
    color: var(--ink); font-family: inherit; }
  .ep-chapters .ch:hover { background: var(--surface-2); }
  .ep-chapters .ch.playing { background: var(--surface-2); }
  .ep-chapters .ch.playing .ch-title { color: var(--gold); }
  .ch-t { font-size: 12px; color: var(--ink-faint); flex: 0 0 46px; }
  .ch-title { font-size: 14px; }
  .ch-intro .ch-title { color: var(--ink-faint); font-style: italic; }
  @media (max-width: 620px) {
    .ep-head { flex-direction: column; }
    .ep-art { width: 96px; height: 96px; }
    .ep-chapters { grid-template-columns: 1fr; }
  }
  .disco { display: grid; gap: 24px; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); }
  .album-card { display: block; text-decoration: none; color: var(--ink);
    border: 1px solid var(--rule); border-radius: 14px; overflow: hidden; background: var(--surface);
    transition: transform 0.15s, border-color 0.15s, box-shadow 0.15s; }
  .album-card:hover { transform: translateY(-3px); box-shadow: 0 16px 40px rgba(0,0,0,0.45); }
  .album-card .card-art { aspect-ratio: 1 / 1; overflow: hidden; }
  .album-card .card-art img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .album-card .card-body { padding: 16px 18px 18px; }
  .album-card .card-meta { font-family: "Inter", sans-serif; font-size: 11px;
    text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 6px; }
  .album-card .card-title { font-size: 24px; font-weight: 700; letter-spacing: -0.01em; margin: 0 0 8px; }
  .album-card .card-blurb { font-size: 14px; color: var(--ink-soft); margin: 0; line-height: 1.5; }

  /* ───── album hero ───── */
  .hero { display: grid; grid-template-columns: 280px 1fr; gap: 34px; align-items: center;
    margin-bottom: 48px; }
  .hero-art { width: 100%; aspect-ratio: 1 / 1; border-radius: 14px; overflow: hidden;
    border: 1px solid var(--rule); box-shadow: 0 18px 50px rgba(0,0,0,0.5); }
  .hero-art img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .eyebrow { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.18em; color: var(--gold); margin-bottom: 12px; }
  .album-title { font-size: 52px; line-height: 1.02; font-weight: 700; letter-spacing: -0.02em;
    margin: 0 0 14px; }
  .album-tagline { font-family: "Inter", sans-serif; font-size: 14px; color: var(--ink-faint);
    letter-spacing: 0.02em; margin-bottom: 18px; }
  .album-blurb { font-size: 19px; color: var(--ink-soft); margin: 0; }

  /* ───── liner notes ───── */
  .liner { max-width: 68ch; margin: 40px auto 8px; padding: 30px 0 0; border-top: 1px solid var(--rule); }
  .liner-label { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.14em; color: var(--gold); margin-bottom: 18px; }
  .liner p { font-size: 18px; line-height: 1.72; color: var(--ink-soft); margin: 0 0 18px; }
  .liner p:first-of-type { color: var(--ink); }
  .liner em { color: var(--ink); font-style: italic; }
  .liner strong { color: var(--gold); font-weight: 600; }

  /* ───── tracklist ───── */
  .tracklist { list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--rule); }
  .track { border-bottom: 1px solid var(--rule); }
  .track a { display: flex; align-items: center; gap: 16px; padding: 15px 12px;
    text-decoration: none; color: var(--ink); transition: background 0.15s; }
  .track a:hover { background: var(--surface); }
  .track-num { font-family: "Inter", sans-serif; font-size: 13px; color: var(--ink-faint);
    width: 26px; flex-shrink: 0; text-align: right; font-variant-numeric: tabular-nums; }
  .track-play { width: 34px; height: 34px; border-radius: 50%; flex-shrink: 0;
    background: var(--surface-2); border: 1px solid var(--rule); color: var(--gold);
    display: flex; align-items: center; justify-content: center; }
  .track a:hover .track-play { background: var(--green-deep); color: #fff; border-color: var(--green); }
  .track-title { font-size: 20px; font-weight: 600; letter-spacing: -0.01em; flex: 1; }
  .track-arrow { color: var(--ink-faint); font-family: "Inter", sans-serif; }

  /* ───── song page ───── */
  .breadcrumb { font-family: "Inter", sans-serif; font-size: 12px; text-transform: uppercase;
    letter-spacing: 0.12em; color: var(--ink-faint); margin-bottom: 16px; }
  .breadcrumb a { color: var(--ink-faint); text-decoration: none; }
  .breadcrumb a:hover { color: var(--gold); }
  h1.song-title { font-size: 46px; line-height: 1.06; font-weight: 700; letter-spacing: -0.02em;
    margin: 0 0 10px; }
  .song-cite { font-family: "Inter", sans-serif; font-size: 14px; color: var(--ink-faint);
    margin-bottom: 26px; }
  .song-cite span + span::before { content: "·"; margin: 0 8px; color: var(--rule); }

  .audio-player { background: var(--surface); border: 1px solid var(--rule); border-radius: 12px;
    padding: 16px 18px; display: flex; align-items: center; gap: 16px; margin-bottom: 30px; }
  .play-button { width: 52px; height: 52px; border-radius: 50%; flex-shrink: 0; cursor: pointer;
    background: var(--gold); border: 0; color: #11140d; display: flex; align-items: center;
    justify-content: center; transition: transform 0.1s, background 0.15s; }
  .play-button:hover { background: var(--green); color: #fff; transform: scale(1.05); }
  .player-body { flex: 1; min-width: 0; }
  .player-label { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.12em; color: var(--gold); margin-bottom: 8px; }
  .player-body audio { width: 100%; height: 38px; }

  .about { border-left: 3px solid var(--green); background: var(--bg-2);
    padding: 16px 20px; border-radius: 0 10px 10px 0; margin-bottom: 34px;
    color: var(--ink-soft); font-size: 18px; }
  .about .about-label { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.14em; color: var(--ink-faint); display: block;
    margin-bottom: 6px; }

  .attribution { border: 1px solid var(--rule); background: var(--surface);
    padding: 16px 20px; border-radius: 10px; margin-bottom: 34px;
    color: var(--ink-soft); font-size: 16px; line-height: 1.55; }
  .attribution .attr-label { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.14em; color: var(--gold); display: block;
    margin-bottom: 6px; }
  .attribution .attr-links { font-family: "Inter", sans-serif; font-size: 13px; margin-top: 10px;
    display: flex; flex-wrap: wrap; gap: 18px; }
  .attribution .attr-links a { color: var(--gold); text-decoration: none; }
  .attribution .attr-links a:hover { text-decoration: underline; }

  /* lyrics */
  .lyrics { margin: 0 0 44px; }
  .stanza { margin: 0 0 26px; }
  .stanza p { margin: 0; line-height: 1.5; }
  .stanza-label { font-family: "Inter", sans-serif; font-size: 11px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.12em; color: var(--gold); margin-bottom: 8px; }
  .lyrics.prose .stanza p { line-height: 1.62; color: var(--ink-soft); }
  .lyrics-pending { color: var(--ink-faint); font-style: italic; margin: 0 0 44px; }

  /* scripture refs */
  .refs { border-top: 1px solid var(--rule); padding-top: 22px; }
  .refs h2 { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.14em; color: var(--ink-faint); margin: 0 0 16px; }
  .refs ol { font-family: "Inter", sans-serif; font-size: 13.5px; color: var(--ink-soft);
    columns: 2; column-gap: 40px; margin: 0; padding: 0; list-style: none; }
  .refs li { margin-bottom: 7px; break-inside: avoid; }
  .refs .rn { color: var(--ink-faint); margin-right: 6px; }
  .refs a { color: var(--ink-soft); text-decoration: none; border-bottom: 1px dotted var(--gold-deep); }
  .refs a:hover { color: var(--gold); }

  .page-nav { display: flex; justify-content: space-between; gap: 16px; margin-top: 44px;
    font-family: "Inter", sans-serif; font-size: 14px; }
  .page-nav a { color: var(--gold); text-decoration: none; }
  .page-nav a:hover { text-decoration: underline; }
  .page-nav .spacer { flex: 1; }

  .site-footer { border-top: 1px solid var(--rule); margin-top: 40px;
    padding: 28px 24px; text-align: center; font-family: "Inter", sans-serif;
    font-size: 12px; color: var(--ink-faint); }

  /* ───── whole-album player ───── */
  .album-player { background: var(--surface); border: 1px solid var(--rule);
    border-radius: 14px; padding: 18px 20px; margin: 0 0 30px; }
  .album-player-label { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.14em; color: var(--gold); margin-bottom: 14px; }
  .ap-row { display: flex; align-items: center; gap: 16px; }
  .ap-btn { width: 56px; height: 56px; border-radius: 50%; flex-shrink: 0; cursor: pointer;
    background: var(--gold); border: 0; color: #11140d; display: flex; align-items: center;
    justify-content: center; transition: transform 0.1s, background 0.15s; }
  .ap-btn:hover { background: var(--green); color: #fff; transform: scale(1.05); }
  .ap-skip { background: none; border: 0; color: var(--ink-soft); cursor: pointer; padding: 6px;
    display: flex; align-items: center; }
  .ap-skip:hover { color: var(--gold); }
  .ap-main { flex: 1; min-width: 0; }
  .ap-now { font-family: "Inter", sans-serif; font-size: 11px; letter-spacing: 0.1em;
    text-transform: uppercase; color: var(--ink-faint); margin-bottom: 2px; }
  .ap-track { font-size: 18px; font-weight: 600; letter-spacing: -0.01em; white-space: nowrap;
    overflow: hidden; text-overflow: ellipsis; }
  .ap-seekwrap { display: flex; align-items: center; gap: 10px; margin-top: 8px; }
  .ap-time { font-family: "Inter", sans-serif; font-size: 11px; color: var(--ink-faint);
    font-variant-numeric: tabular-nums; flex-shrink: 0; }
  .ap-seek { flex: 1; accent-color: var(--gold); height: 4px; cursor: pointer; }

  /* ───── section heading (Study the songs) ───── */
  .section-head { margin: 4px 0 6px; }
  .section-head h2 { font-size: 30px; font-weight: 700; letter-spacing: -0.01em; margin: 0; }
  .section-sub { font-family: "Inter", sans-serif; font-size: 14px; color: var(--ink-faint);
    margin: 0 0 16px; }

  /* ───── teaching aids (study layer) ───── */
  blockquote.thesis-hero { font-family: "Fraunces", Georgia, serif; font-size: 23px;
    line-height: 1.4; color: var(--ink); border: 0; border-left: 3px solid var(--gold);
    background: var(--bg-2); margin: 0 0 26px; padding: 18px 24px; border-radius: 0 10px 10px 0; }
  blockquote.thesis-hero .thesis-label { display: block; font-family: "Inter", sans-serif;
    font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.14em;
    color: var(--gold); margin-bottom: 8px; }
  .facts-strip { display: flex; flex-wrap: wrap; gap: 0; border: 1px solid var(--rule);
    border-radius: 10px; overflow: hidden; margin: 0 0 34px; }
  .fact { flex: 1; min-width: 140px; padding: 12px 16px; border-right: 1px solid var(--rule); }
  .fact:last-child { border-right: 0; }
  .fact-label { font-family: "Inter", sans-serif; font-size: 10px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.12em; color: var(--ink-faint); margin-bottom: 3px; }
  .fact-value { font-size: 15px; color: var(--ink); }
  .study { border-top: 1px solid var(--rule); padding-top: 26px; margin-top: 8px; }
  .study > h2 { font-size: 26px; font-weight: 700; margin: 0 0 4px; }
  .study-sub { font-family: "Inter", sans-serif; font-size: 13px; color: var(--ink-faint);
    margin: 0 0 26px; }
  .aid { margin: 0 0 30px; }
  .aid > h3 { font-family: "Inter", sans-serif; font-size: 12px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.13em; color: var(--gold); margin: 0 0 14px; }
  .move { display: flex; gap: 14px; margin-bottom: 16px; }
  .move-n { font-family: "Inter", sans-serif; font-weight: 600; color: var(--green);
    flex-shrink: 0; width: 22px; font-variant-numeric: tabular-nums; }
  .move-body .move-label { font-weight: 600; color: var(--ink); }
  .move-body .move-text { color: var(--ink-soft); font-size: 16.5px; line-height: 1.5; }
  .terms { list-style: none; margin: 0; padding: 0; }
  .terms li { margin-bottom: 14px; color: var(--ink-soft); font-size: 16.5px; line-height: 1.5; }
  .terms .term { font-weight: 600; color: var(--gold); font-style: italic; }
  .questions { margin: 0; padding-left: 22px; }
  .questions li { color: var(--ink-soft); margin-bottom: 12px; line-height: 1.5; }
  .further { list-style: none; margin: 0; padding: 0; font-size: 14px; }
  .further li { margin-bottom: 10px; }
  .further a { color: var(--gold); text-decoration: none; }
  .further a:hover { text-decoration: underline; }

  @media (max-width: 680px) {
    .hero { grid-template-columns: 1fr; gap: 22px; }
    .album-title, .disco-title { font-size: 38px; }
    h1.song-title { font-size: 34px; }
    .refs ol { columns: 1; }
    .facts-strip { flex-direction: column; }
    .fact { border-right: 0; border-bottom: 1px solid var(--rule); }
    .fact:last-child { border-bottom: 0; }
  }
"""

PLAY_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
PLAY_SVG_SM = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
PLAY_SVG_LG = '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
PAUSE_SVG_LG = '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>'
PREV_SVG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M6 6h2v12H6zm3.5 6l8.5 6V6z"/></svg>'
NEXT_SVG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M16 6h2v12h-2zM6 6l8.5 6L6 18z"/></svg>'


def esc(s):
    return html.escape(s, quote=True)


def json_str(s):
    """Safe JS string literal (also escapes </script>)."""
    return json.dumps(s).replace("</", "<\\/")


def accent(album):
    """The album's primary accent color (the --gold slot), base gold if none."""
    theme = album.get("theme")
    return theme.get("--gold", "#f4c430") if theme else "#f4c430"


def theme_style(album):
    """Inline :root overrides for an album's palette (empty for the base theme)."""
    theme = album.get("theme")
    if not theme:
        return ""
    decls = " ".join(f"{k}: {v};" for k, v in theme.items())
    return f"\n<style>:root {{ {decls} }}</style>"


def header():
    return """<header class="site-header">
  <div class="site-header-inner">
    <a href="/" class="site-brand">Uncle Theology<span class="dot">.</span></a>
    <nav class="site-nav ui">
      <a href="/">Albums</a>
      <a href="/radio.html">Radio</a>
      <a href="/about.html">About</a>
    </nav>
  </div>
</header>
<hr class="flag-rule">"""


def footer():
    return f"""<footer class="site-footer ui">
  <p>{esc(SITE_NAME)} — sermon-rooted theology in song.<br>
  Lyrics &amp; Scripture © Chris Oswald. Hover a reference to read the {esc(BIBLE_VERSION)} text.</p>
</footer>"""


def reftagger():
    """Logos RefTagger: turns Scripture references into hover-tooltip popups
    showing the full verse text in BIBLE_VERSION. Skips lyrics + headings."""
    return f"""<script>
var refTagger = {{ settings: {{
  bibleVersion: "{BIBLE_VERSION}",
  useTooltip: true,
  tagChapters: false,
  caseInsensitive: false,
  linksOpenNewWindow: true,
  noSearchClassNames: ["lyrics", "site-brand", "breadcrumb", "song-title", "album-title", "disco-title", "site-nav", "track-title", "card-title", "ep-title", "ep-summary", "ch-title"]
}} }};
(function(d, t) {{
  var g = d.createElement(t), s = d.getElementsByTagName(t)[0];
  g.src = "https://api.reftagger.com/v2/RefTagger.js";
  s.parentNode.insertBefore(g, s);
}}(document, "script"));
</script>"""


_DIMS_CACHE = {}


def _og_image_meta(url, alt):
    """secure_url + accurate width/height/type for an og:image, so scrapers
    render the image on the first pass instead of deferring it."""
    tags = [
        f'<meta property="og:image:secure_url" content="{esc(url)}">',
        f'<meta property="og:image:alt" content="{esc(alt)}">',
    ]
    if url not in _DIMS_CACHE:
        _DIMS_CACHE[url] = None
        try:
            from PIL import Image
            path = url[len(SITE_URL):] if url.startswith(SITE_URL) else url
            local = os.path.join(HERE, path.lstrip("/"))
            with Image.open(local) as im:
                _DIMS_CACHE[url] = (im.width, im.height, "image/" + (im.format or "JPEG").lower())
        except Exception:
            _DIMS_CACHE[url] = None
    d = _DIMS_CACHE[url]
    if d:
        tags.append(f'<meta property="og:image:width" content="{d[0]}">')
        tags.append(f'<meta property="og:image:height" content="{d[1]}">')
        tags.append(f'<meta property="og:image:type" content="{d[2]}">')
    return "\n".join(tags)


def doc(title, description, body, canonical, album=None):
    og_image = (SITE_URL + album["cover"]) if album else DEFAULT_OG_IMAGE
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{esc(canonical)}">
<link rel="alternate" type="application/rss+xml" title="UncleTheology Radio" href="{SITE_URL}/podcast.xml">
<meta property="og:type" content="music.album">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:site_name" content="{esc(SITE_NAME)}">
<meta property="og:image" content="{esc(og_image)}">
{_og_image_meta(og_image, title)}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{esc(og_image)}">
{FONTS}
<style>{CSS}</style>{theme_style(album) if album else ""}
</head>
<body>
{header()}
{body}
{footer()}
{reftagger()}
</body>
</html>
"""


# ─────────────────────────── pieces ───────────────────────────

def render_ref(ref):
    """A scripture citation as a plain-text <li> (RefTagger tags it on hover).

    Footnote style ('3. Psalm 20:7') keeps its number; a bare passage
    ('1 John 1:5-7') renders without one. En-dashes → hyphens for RefTagger."""
    m = re.match(r"\s*(\d+)\.\s*(.*)", ref)
    if m:
        rn = f'<span class="rn">{m.group(1)}.</span>'
        body = m.group(2)
    else:
        rn = ""
        body = ref.strip()
    text = body.replace("–", "-").replace("—", "-")
    return f"<li>{rn}{esc(text)}</li>"


def render_lyrics(song):
    if not song.get("blocks"):
        return '  <p class="lyrics-pending ui">Lyrics coming soon.</p>'
    if song["kind"] == "prose":
        inner = "\n".join(
            f'    <div class="stanza"><p>{esc(par)}</p></div>' for par in song["blocks"]
        )
        return f'  <div class="lyrics prose">\n{inner}\n  </div>'
    stanzas = []
    for stanza in song["blocks"]:
        if isinstance(stanza, dict):
            label = stanza.get("label")
            lines = stanza["lines"]
            lbl = f'<div class="stanza-label ui">{esc(label)}</div>' if label else ""
        else:
            lines = stanza
            lbl = ""
        body = "<br>\n      ".join(esc(line) for line in lines)
        stanzas.append(f'    <div class="stanza">{lbl}<p>{body}</p></div>')
    return '  <div class="lyrics">\n' + "\n".join(stanzas) + "\n  </div>"


def render_thesis_facts(song):
    out = []
    if song.get("thesis"):
        out.append(
            '    <blockquote class="thesis-hero">'
            '<span class="thesis-label ui">Big idea</span>'
            f'{esc(song["thesis"])}</blockquote>'
        )
    if song.get("facts"):
        cells = "".join(
            f'<div class="fact"><div class="fact-label ui">{esc(lbl)}</div>'
            f'<div class="fact-value">{esc(val)}</div></div>'
            for lbl, val in song["facts"]
        )
        out.append(f'    <div class="facts-strip">{cells}</div>')
    return "\n".join(out)


def render_study(song):
    if not any(song.get(k) for k in ("moves", "terms", "questions", "discussion", "contemplation", "further")):
        return ""
    parts = [
        '    <section class="study">',
        "      <h2>Study this song</h2>",
        '      <p class="study-sub ui">Teaching aids drawn from the song — for personal study or group discussion.</p>',
    ]
    if song.get("moves"):
        rows = "".join(
            f'<div class="move"><div class="move-n ui">{n}</div>'
            f'<div class="move-body"><div class="move-label">{esc(m["label"])}</div>'
            f'<div class="move-text">{esc(m["text"])}</div></div></div>'
            for n, m in enumerate(song["moves"], 1)
        )
        parts.append(f'      <div class="aid"><h3>How the song moves</h3>{rows}</div>')
    if song.get("terms"):
        items = "".join(
            f'<li><span class="term">{esc(t["term"])}</span> — {esc(t["gloss"])}</li>'
            for t in song["terms"]
        )
        parts.append(f'      <div class="aid"><h3>Key terms &amp; allusions</h3><ul class="terms">{items}</ul></div>')
    if song.get("questions"):
        items = "".join(f"<li>{esc(q)}</li>" for q in song["questions"])
        parts.append(f'      <div class="aid"><h3>Study questions</h3><ol class="questions">{items}</ol></div>')
    if song.get("discussion"):
        items = "".join(f"<li>{esc(q)}</li>" for q in song["discussion"])
        parts.append(f'      <div class="aid"><h3>Discussion questions</h3><ol class="questions">{items}</ol></div>')
    if song.get("contemplation"):
        items = "".join(f"<li>{esc(q)}</li>" for q in song["contemplation"])
        parts.append(f'      <div class="aid"><h3>For contemplation</h3><ol class="questions">{items}</ol></div>')
    if song.get("further"):
        items = "".join(
            f'<li><a href="{esc(url)}" target="_blank" rel="noopener">{esc(label)} →</a></li>'
            for label, url in song["further"]
        )
        parts.append(f'      <div class="aid"><h3>Go deeper</h3><ul class="further ui">{items}</ul></div>')
    parts.append("    </section>")
    return "\n".join(parts)


def render_attribution(song):
    attr = song.get("attribution")
    if not attr:
        return ""
    links = "".join(
        f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(label)} →</a>'
        for label, url in attr.get("links", [])
    )
    link_html = f'<div class="attr-links ui">{links}</div>' if links else ""
    return (
        '    <div class="attribution"><span class="attr-label ui">Source</span>'
        f'{esc(attr["text"])}{link_html}</div>'
    )


# ─────────────────────────── song page ───────────────────────────

def song_page(album, song, prev_song, next_song):
    base = f"/{album['slug']}"
    songs = album["songs"]
    audio_url = f"{AUDIO_ROOT}/{album['audio_prefix']}/{song['slug']}.mp3"
    if song.get("refs"):
        refs = "\n".join(render_ref(r) for r in song["refs"])
        refs_section = (
            '    <section class="refs">\n'
            "      <h2>Scripture References</h2>\n"
            f"      <ol>\n{refs}\n      </ol>\n"
            "    </section>"
        )
    else:
        refs_section = ""
    player_label = "Listen" if song["kind"] != "prose" else "Listen — spoken"
    attribution = render_attribution(song)
    thesis_facts = render_thesis_facts(song)
    study = render_study(song)

    nav_prev = (
        f'<a href="{base}/{prev_song["slug"]}.html">← {esc(prev_song["title"])}</a>'
        if prev_song else "<span></span>"
    )
    nav_next = (
        f'<a href="{base}/{next_song["slug"]}.html">{esc(next_song["title"])} →</a>'
        if next_song else "<span></span>"
    )

    body = f"""<main>
  <article class="song">
    <div class="breadcrumb ui"><a href="/">Uncle Theology</a> · <a href="{base}/">{esc(album['title'])}</a> · Track {song['num']}</div>
    <h1 class="song-title">{esc(song['title'])}</h1>
    <div class="song-cite ui"><span>{esc(album['title'])}</span><span>Track {song['num']} of {len(songs)}</span></div>

    <div class="audio-player">
      <button class="play-button" aria-label="Play {esc(song['title'])}" onclick="togglePlay(this)">{PLAY_SVG}</button>
      <div class="player-body">
        <div class="player-label ui">{player_label}</div>
        <audio controls preload="none" src="{esc(audio_url)}">
          Your browser does not support the audio element.
          <a href="{esc(audio_url)}">Download the MP3.</a>
        </audio>
      </div>
    </div>

    <div class="about"><span class="about-label ui">About this song</span>{esc(song['about'])}</div>

{attribution}

{thesis_facts}

{render_lyrics(song)}

{refs_section}

{study}

    <nav class="page-nav ui">
      {nav_prev}<span class="spacer"></span>{nav_next}
    </nav>
  </article>
</main>
<script>
function togglePlay(btn){{
  var audio = btn.parentElement.querySelector('audio');
  if(audio.paused){{ audio.play(); }} else {{ audio.pause(); }}
}}
</script>"""

    title = f"{song['title']} — {album['title']} · {SITE_NAME}"
    return doc(title, song["about"], body, f"{SITE_URL}{base}/{song['slug']}.html", album=album)


# ─────────────────────────── album page ───────────────────────────

def album_player(album):
    songs = album["songs"]
    base_audio = f"{AUDIO_ROOT}/{album['audio_prefix']}"
    tracks = ",\n      ".join(
        f'{{title: {json_str(s["title"])}, src: {json_str(base_audio + "/" + s["slug"] + ".mp3")}}}'
        for s in songs
    )
    return f"""  <div class="album-player">
    <div class="album-player-label ui">Listen to the whole album</div>
    <div class="ap-row">
      <button class="ap-skip" id="apPrev" aria-label="Previous track">{PREV_SVG}</button>
      <button class="ap-btn" id="apPlay" aria-label="Play album">{PLAY_SVG_LG}</button>
      <button class="ap-skip" id="apNext" aria-label="Next track">{NEXT_SVG}</button>
      <div class="ap-main">
        <div class="ap-now ui"><span id="apIdx">1</span> / {len(songs)} · {esc(album['title'])}</div>
        <div class="ap-track" id="apTitle">{esc(songs[0]['title'])}</div>
        <div class="ap-seekwrap">
          <span class="ap-time ui" id="apCur">0:00</span>
          <input type="range" class="ap-seek" id="apSeek" value="0" min="0" max="100" step="0.1" aria-label="Seek">
          <span class="ap-time ui" id="apDur">0:00</span>
        </div>
      </div>
    </div>
    <audio id="apAudio" preload="none"></audio>
  </div>
  <script>
  (function(){{
    var tracks = [
      {tracks}
    ];
    var a = document.getElementById('apAudio'),
        playBtn = document.getElementById('apPlay'),
        titleEl = document.getElementById('apTitle'),
        idxEl = document.getElementById('apIdx'),
        seek = document.getElementById('apSeek'),
        curEl = document.getElementById('apCur'),
        durEl = document.getElementById('apDur'),
        i = 0, seeking = false;
    var PLAY = {json_str(PLAY_SVG_LG)}, PAUSE = {json_str(PAUSE_SVG_LG)};
    function fmt(s){{ if(!s||isNaN(s)) return '0:00'; var m=Math.floor(s/60), x=Math.floor(s%60); return m+':'+(x<10?'0':'')+x; }}
    function load(n, play){{ i=(n+tracks.length)%tracks.length; a.src=tracks[i].src; titleEl.textContent=tracks[i].title; idxEl.textContent=i+1; if(play) a.play(); }}
    playBtn.addEventListener('click', function(){{ if(!a.src) load(0,false); if(a.paused) a.play(); else a.pause(); }});
    document.getElementById('apPrev').addEventListener('click', function(){{ load(i-1, !a.paused || a.currentTime>0); }});
    document.getElementById('apNext').addEventListener('click', function(){{ load(i+1, !a.paused || a.currentTime>0); }});
    a.addEventListener('play', function(){{ playBtn.innerHTML=PAUSE; }});
    a.addEventListener('pause', function(){{ playBtn.innerHTML=PLAY; }});
    a.addEventListener('ended', function(){{ if(i<tracks.length-1) load(i+1, true); else playBtn.innerHTML=PLAY; }});
    a.addEventListener('timeupdate', function(){{ if(!seeking && a.duration){{ seek.value=(a.currentTime/a.duration)*100; curEl.textContent=fmt(a.currentTime); }} }});
    a.addEventListener('loadedmetadata', function(){{ durEl.textContent=fmt(a.duration); }});
    seek.addEventListener('input', function(){{ seeking=true; curEl.textContent=fmt((seek.value/100)*(a.duration||0)); }});
    seek.addEventListener('change', function(){{ if(a.duration) a.currentTime=(seek.value/100)*a.duration; seeking=false; }});
    load(0, false);
  }})();
  </script>"""


def render_liner(album):
    """Long-form liner-notes essay (optional). Paragraphs are trusted, author-
    written HTML so emphasis (<em>/<strong>) and entities survive."""
    paras = album.get("liner")
    if not paras:
        return ""
    body = "\n      ".join(f"<p>{p}</p>" for p in paras)
    return (
        '  <section class="liner">\n'
        '      <div class="liner-label ui">Liner notes</div>\n'
        f"      {body}\n"
        "  </section>"
    )


def album_page(album):
    base = f"/{album['slug']}"
    rows = []
    for s in album["songs"]:
        rows.append(f"""    <li class="track">
      <a href="{base}/{s['slug']}.html">
        <span class="track-num ui">{s['num']}</span>
        <span class="track-play">{PLAY_SVG_SM}</span>
        <span class="track-title">{esc(s['title'])}</span>
        <span class="track-arrow ui">View →</span>
      </a>
    </li>""")
    tracklist = "\n".join(rows)

    body = f"""<main>
  <section class="hero">
    <div class="hero-art"><img src="{esc(album['cover'])}" alt="{esc(album['title'])} album cover"></div>
    <div class="hero-text">
      <div class="breadcrumb ui"><a href="/">Uncle Theology</a> · Album</div>
      <h1 class="album-title">{esc(album['title'])}</h1>
      <div class="album-tagline ui">{esc(album['tagline'])}</div>
      <p class="album-blurb">{esc(album['blurb'])}</p>
    </div>
  </section>

{album_player(album)}

{render_liner(album)}

  <div class="section-head" id="tracklist">
    <h2>Study the songs</h2>
  </div>
  <p class="section-sub ui">Listen to each song with the lyrics, scripture references, and additional teaching aids.</p>
  <ul class="tracklist">
{tracklist}
  </ul>
</main>"""

    return doc(
        f"{album['title']} — {SITE_NAME}",
        album["blurb"],
        body,
        f"{SITE_URL}{base}/",
        album=album,
    )


# ─────────────────────────── discography + about ───────────────────────────

def discography_page():
    cards = []
    for album in ALBUMS:
        cards.append(f"""    <a class="album-card" href="/{album['slug']}/" style="border-top: 3px solid {accent(album)};">
      <div class="card-art"><img src="{esc(album['cover'])}" alt="{esc(album['title'])} album cover"></div>
      <div class="card-body">
        <div class="card-meta ui" style="color: {accent(album)};">{len(album['songs'])} songs</div>
        <h2 class="card-title">{esc(album['title'])}</h2>
        <p class="card-blurb">{esc(album['blurb'])}</p>
      </div>
    </a>""")
    grid = "\n".join(cards)

    body = f"""<main>
  <section class="disco-intro">
    <div class="disco-eyebrow ui">Sermon-rooted theology in song</div>
    <h1 class="disco-title">Uncle Theology</h1>
    <p class="disco-blurb">Albums that turn the substance of expository preaching into music — every
    lyric anchored to Scripture, each with its own sound. Pick an album to listen and study.</p>
  </section>

  <div class="disco">
{grid}
  </div>
</main>"""

    return doc(
        f"{SITE_NAME} — sermon-rooted theology in song",
        "Albums turning expository preaching into song, every lyric anchored to Scripture.",
        body,
        SITE_URL + "/",
    )


def about_page():
    album_lines = "".join(
        f'<li><a href="/{a["slug"]}/">{esc(a["title"])}</a> — {esc(a["tagline"])}</li>'
        for a in ALBUMS
    )
    body = f"""<main>
  <article class="song">
    <div class="breadcrumb ui"><a href="/">Uncle Theology</a> · About</div>
    <h1 class="song-title">About Uncle Theology</h1>
    <div class="about"><span class="about-label ui">What this is</span>
      Uncle Theology turns the substance of expository preaching into song — Reformed theology
      and the history of ideas, carried on everything from roots reggae to street-gospel hip-hop,
      with every lyric anchored to Scripture.</div>
    <p style="color:var(--ink-soft)">Each song page carries the track, a short note on what it's
    about, the full lyrics, the Scripture references behind every line (hover any reference to read
    the {esc(BIBLE_VERSION)} text), and — where built — a study layer of teaching aids.</p>
    <p style="color:var(--ink-soft)">Albums:</p>
    <ul style="color:var(--ink-soft); line-height:1.8;">{album_lines}</ul>
    <nav class="page-nav ui"><a href="/">← Back to the albums</a><span class="spacer"></span></nav>
  </article>
</main>"""
    return doc(f"About — {SITE_NAME}", "About Uncle Theology and its albums.",
               body, f"{SITE_URL}/about.html")


# ─────────────────────────── podcast feed ───────────────────────────

# One master feed: "UncleTheology Radio". Every album that declares an
# `episode` block (see the album modules) becomes one <item> — a whole-album
# episode with spoken intros before each song and chapter markers baked into
# the MP3. Written to public/podcast.xml and linked from every page's <head>.
RADIO = {
    "title": "UncleTheology Radio",
    "link": SITE_URL,
    "feed_url": SITE_URL + "/podcast.xml",
    "author": "Uncle Theology",
    "owner_name": "Chris Oswald",
    "owner_email": "chris@sovgracekc.org",
    "image": "https://sermons-cdn.sermonsteward.com/uncle-theology/podcast/utr-radio-cover.jpg",
    "summary": ("Chris Oswald's sermons, sung and explained. Each episode plays a whole "
                "Uncle Theology album straight through — but before every song, a short spoken "
                "intro tells you the Scripture and the story underneath it. Music and commentary, "
                "one continuous listen."),
    "category": "Religion &amp; Spirituality",
    "subcategory": "Christianity",
    # Distribution. Apple Podcasts opens ANY feed via the podcast:// URL scheme
    # (no directory listing needed) — works today on Mac/iOS. Spotify requires a
    # one-time submission through Spotify for Podcasters; drop the show URL here
    # once it's live and the button lights up automatically.
    "apple_url": "podcast://uncletheology.com/podcast.xml",
    "spotify_url": "",   # set to the Spotify show URL after submission
}


def xesc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def podcast_feed(episodes):
    """Return the UncleTheology Radio RSS 2.0 + iTunes feed XML."""
    items = []
    for ep in episodes:
        chapters = ""
        if ep.get("chapters"):
            lines = "".join(f"{t} {xesc(title)}\n" for t, title in ep["chapters"])
            chapters = f"\n\nChapters:\n{lines}"
        desc = ep["summary"] + chapters
        items.append(f"""  <item>
    <title>{xesc(ep['title'])}</title>
    <link>{xesc(ep['link'])}</link>
    <guid isPermaLink="false">{xesc(ep['guid'])}</guid>
    <pubDate>{ep['pubDate']}</pubDate>
    <description>{xesc(desc)}</description>
    <itunes:summary>{xesc(desc)}</itunes:summary>
    <itunes:author>{xesc(RADIO['author'])}</itunes:author>
    <itunes:duration>{ep['duration']}</itunes:duration>
    <itunes:image href="{xesc(ep['image'])}" />
    <itunes:explicit>false</itunes:explicit>
    <enclosure url="{xesc(ep['audio_url'])}" length="{ep['length']}" type="audio/mpeg" />
  </item>""")
    items_xml = "\n".join(items)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:content="http://purl.org/rss/1.0/modules/content/"
     xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{xesc(RADIO['title'])}</title>
  <link>{xesc(RADIO['link'])}</link>
  <atom:link href="{xesc(RADIO['feed_url'])}" rel="self" type="application/rss+xml" />
  <language>en-us</language>
  <description>{xesc(RADIO['summary'])}</description>
  <itunes:summary>{xesc(RADIO['summary'])}</itunes:summary>
  <itunes:author>{xesc(RADIO['author'])}</itunes:author>
  <itunes:type>episodic</itunes:type>
  <itunes:owner>
    <itunes:name>{xesc(RADIO['owner_name'])}</itunes:name>
    <itunes:email>{xesc(RADIO['owner_email'])}</itunes:email>
  </itunes:owner>
  <itunes:image href="{xesc(RADIO['image'])}" />
  <itunes:category text="{RADIO['category']}">
    <itunes:category text="{RADIO['subcategory']}" />
  </itunes:category>
  <itunes:explicit>false</itunes:explicit>
{items_xml}
</channel>
</rss>
"""


def _secs(ts):
    """'mm:ss' or 'h:mm:ss' → integer seconds."""
    parts = [int(p) for p in ts.split(":")]
    s = 0
    for p in parts:
        s = s * 60 + p
    return s


def radio_episodes():
    """Albums that have a podcast episode, newest first."""
    eps = [a for a in ALBUMS if a.get("episode")]
    eps.sort(key=lambda a: a["episode"].get("order", 0), reverse=True)
    return eps


def radio_page():
    albums = radio_episodes()
    cards = []
    for album in albums:
        ep = album["episode"]
        acc = accent(album)
        chapters = ""
        if ep.get("chapters"):
            rows = []
            for ts, title in ep["chapters"]:
                intro = title.lower().startswith("intro")
                rows.append(
                    f'<li><button class="ch{" ch-intro" if intro else ""}" '
                    f'data-t="{_secs(ts)}"><span class="ch-t ui">{esc(ts)}</span>'
                    f'<span class="ch-title">{esc(title)}</span></button></li>'
                )
            chapters = ('<div class="ch-label ui">Chapters — tap to jump</div>\n'
                        f'    <ol class="ep-chapters">{"".join(rows)}</ol>')
        cards.append(f"""  <article class="ep-card" style="border-top:3px solid {acc};">
    <div class="ep-head">
      <img class="ep-art" src="{esc(ep.get('image', album['cover']))}" alt="{esc(album['title'])} cover">
      <div class="ep-meta">
        <div class="ep-eyebrow ui" style="color:{acc};">Episode · {esc(ep['duration'])}</div>
        <h2 class="ep-title">{esc(ep.get('title', album['title']))}</h2>
        <p class="ep-summary">{esc(ep['summary'])}</p>
        <a class="ep-studylink ui" href="/{album['slug']}/">Lyrics &amp; study for this album →</a>
      </div>
    </div>
    <audio class="ep-audio" controls preload="none" src="{esc(ep['audio_url'])}"></audio>
    {chapters}
  </article>""")
    grid = "\n".join(cards)

    # Subscribe buttons.
    apple = (f'<a class="sub-btn apple" href="{esc(RADIO["apple_url"])}">'
             f'<span class="sub-ico"></span> Apple Podcasts</a>')
    if RADIO.get("spotify_url"):
        spotify = (f'<a class="sub-btn spotify" href="{esc(RADIO["spotify_url"])}" '
                   f'target="_blank" rel="noopener">Spotify</a>')
    else:
        spotify = ('<button class="sub-btn spotify soon" type="button" '
                   'data-soon="1">Spotify · coming soon</button>')
    rss = (f'<button class="sub-btn rss" type="button" '
           f'data-feed="{esc(RADIO["feed_url"])}">Copy RSS feed</button>')

    body = f"""<main>
  <section class="disco-intro">
    <div class="disco-eyebrow ui" style="color:var(--gold);">🎙 UncleTheology Radio</div>
    <h1 class="disco-title">Radio</h1>
    <p class="disco-blurb">Every Uncle Theology album, played straight through — with a short spoken
    intro before each song telling you the Scripture and the story underneath it. Listen right here,
    or subscribe and take it with you.</p>
    <div class="sub-row">{apple}{spotify}{rss}</div>
    <div class="sub-note ui" id="subNote"></div>
  </section>

  <div class="ep-list">
{grid}
  </div>

  <script>
  (function() {{
    // Tap a chapter → seek that card's audio and play.
    document.querySelectorAll('.ch').forEach(function(btn) {{
      btn.addEventListener('click', function() {{
        var card = btn.closest('.ep-card');
        var audio = card.querySelector('.ep-audio');
        if (!audio) return;
        audio.currentTime = parseFloat(btn.getAttribute('data-t')) || 0;
        audio.play().catch(function() {{}});
        card.querySelectorAll('.ch').forEach(function(b) {{ b.classList.remove('playing'); }});
        btn.classList.add('playing');
      }});
    }});
    // Copy RSS feed to clipboard.
    var note = document.getElementById('subNote');
    document.querySelectorAll('.sub-btn.rss').forEach(function(btn) {{
      btn.addEventListener('click', function() {{
        var feed = btn.getAttribute('data-feed');
        navigator.clipboard.writeText(feed).then(function() {{
          note.textContent = 'Feed copied — paste it into any podcast app: ' + feed;
        }}, function() {{
          note.textContent = 'Copy this feed into any podcast app: ' + feed;
        }});
      }});
    }});
    // Spotify not yet submitted.
    document.querySelectorAll('.sub-btn.soon').forEach(function(btn) {{
      btn.addEventListener('click', function() {{
        note.textContent = 'Spotify listing is on the way. For now, use Apple Podcasts or the RSS feed.';
      }});
    }});
  }})();
  </script>
</main>"""
    return doc(
        "UncleTheology Radio — the albums, sung and explained",
        "Every Uncle Theology album played straight through with spoken intros before each song. "
        "Listen on the site or subscribe on Apple Podcasts, Spotify, or by RSS.",
        body,
        SITE_URL + "/radio.html",
    )


# ─────────────────────────── build ───────────────────────────

def main():
    os.makedirs(PUBLIC, exist_ok=True)
    dest_assets = os.path.join(PUBLIC, "assets")
    if os.path.isdir(SRC_ASSETS):
        shutil.copytree(SRC_ASSETS, dest_assets, dirs_exist_ok=True)

    with open(os.path.join(PUBLIC, "index.html"), "w", encoding="utf-8") as f:
        f.write(discography_page())
    with open(os.path.join(PUBLIC, "about.html"), "w", encoding="utf-8") as f:
        f.write(about_page())
    with open(os.path.join(PUBLIC, "radio.html"), "w", encoding="utf-8") as f:
        f.write(radio_page())

    total_songs = 0
    for album in ALBUMS:
        album_dir = os.path.join(PUBLIC, album["slug"])
        os.makedirs(album_dir, exist_ok=True)
        with open(os.path.join(album_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(album_page(album))
        songs = album["songs"]
        for i, song in enumerate(songs):
            prev_song = songs[i - 1] if i > 0 else None
            next_song = songs[i + 1] if i < len(songs) - 1 else None
            with open(os.path.join(album_dir, f"{song['slug']}.html"), "w", encoding="utf-8") as f:
                f.write(song_page(album, song, prev_song, next_song))
            total_songs += 1

    # UncleTheology Radio feed — one episode per album that declares one.
    episodes = []
    for album in ALBUMS:
        ep = album.get("episode")
        if not ep:
            continue
        episodes.append({
            "title": ep.get("title", album["title"]),
            "link": f"{SITE_URL}/{album['slug']}/",
            "guid": ep["guid"],
            "pubDate": ep["pubDate"],
            "summary": ep["summary"],
            "duration": ep["duration"],
            "length": ep["length"],
            "audio_url": ep["audio_url"],
            "image": ep.get("image", RADIO["image"]),
            "chapters": ep.get("chapters"),
            "_sort": ep.get("order", 0),
        })
    episodes.sort(key=lambda e: e["_sort"], reverse=True)  # newest first
    with open(os.path.join(PUBLIC, "podcast.xml"), "w", encoding="utf-8") as f:
        f.write(podcast_feed(episodes))

    print(f"Built discography ({len(ALBUMS)} albums), about, {total_songs} song pages, "
          f"and podcast.xml ({len(episodes)} episode(s)) into public/")


if __name__ == "__main__":
    main()
