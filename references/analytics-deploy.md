# Analytics, UTM, Deploy

## Mandatory Analytics For School Landing Pages

Add SOHO metrika to every Fin Academy / Master CFO landing page when the user confirms it is a school page:

```html
<script src="https://metrika.soholms.com/watch.js?org_id=199347" async></script>
```

Add Yandex.Metrika when a counter ID is provided. Use a unique ID per landing unless the user explicitly says to reuse one.

Minimum Yandex settings:

```js
ym(ID, "init", {
  webvisor: true,
  clickmap: true,
  accurateTrackBounce: true,
  trackLinks: true,
});
```

If no Yandex ID is provided, leave a clear placeholder and report `данных нет`.

## UTM Passthrough

Preserve these query params:

```text
utm_source, utm_medium, utm_campaign, utm_content, utm_term, gcpc, yclid, gclid, fbclid
```

Patch:

- payment links;
- order links;
- cross-sell links between public excursion sites;
- dynamically generated CTA links.

Static helper pattern:

```js
const UTM_KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "gcpc", "yclid", "gclid", "fbclid"];
const pageParams = new URLSearchParams(window.location.search);
const utmPairs = UTM_KEYS.flatMap((key) => {
  const value = pageParams.get(key);
  return value ? [`${encodeURIComponent(key)}=${encodeURIComponent(value)}`] : [];
});
const utmString = utmPairs.join("&");
window.appendUtm = function appendUtm(url) {
  if (!utmString || !url) return url;
  return url + (url.includes("?") ? "&" : "?") + utmString;
};
```

For React, implement the same logic in a small helper and use it inside CTA components.

## Link Goals

On payment/order click, fire goals only if the analytics object exists:

```js
try {
  if (window.soho_metrika) window.soho_metrika.reachGoal("registration");
} catch (error) {}
try {
  if (typeof ym === "function") ym(ID, "reachGoal", "registration");
} catch (error) {}
```

Do not block navigation if analytics fails.

## Static Hosting Rules

For static/Vite output:

- deploy built `dist/` or a checked `index.html`, not source files;
- ensure `index.html` has no-cache when serving an SPA;
- cache hashed assets for a long time;
- enable gzip for JS/CSS/HTML;
- ensure `.git`, `.env`, service folders, Chrome profiles, and credential files are not in webroot;
- localize fonts where possible.

## Production Verification

Before saying "ready":

```bash
curl -I https://example.com
curl -s https://example.com | grep -E "metrika.soholms|ym\\("
```

Also verify:

- DNS points to the intended server before deploy;
- `http://` redirects to `https://`;
- SSL certificate is valid;
- root path returns 200;
- key assets return 200;
- source maps and secrets are not exposed;
- page renders in browser at desktop and 390px mobile.

If production cannot be checked, report exactly what was not verified.

## Public Repository Safety

Before publishing a skill or site template publicly:

- run secret scan;
- remove private repo URLs, IPs, internal host aliases, private invite links, exports, logs, screenshots with personal data;
- keep public examples to public URLs only;
- use placeholders for analytics IDs unless the ID is intentionally public in deployed HTML.

