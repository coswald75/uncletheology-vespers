// uncletheology.com — thin Worker in front of the static assets.
//
// Only job: redirect the legacy single-album URLs (when the site was just
// "Roots of Reason" at the root) to their new album-namespaced paths, so any
// links already shared keep working. Everything else is served from assets.

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Old Roots of Reason song pages: /songs/<slug>.html → /roots-of-reason/<slug>.html
    if (url.pathname.startsWith("/songs/")) {
      const rest = url.pathname.slice("/songs/".length);
      return Response.redirect(`${url.origin}/roots-of-reason/${rest}`, 301);
    }

    return env.ASSETS.fetch(request);
  },
};
