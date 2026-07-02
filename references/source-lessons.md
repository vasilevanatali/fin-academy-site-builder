# Source Lessons

Use these lessons as reusable patterns, not as code to copy verbatim.

## Projects Analyzed

- `codex.fin-academy.pro`: static HTML for Codex excursion, sticky CTA, UTM passthrough, payment links, quiz branch to ChatGPT excursion.
- ChatGPT/Claude/Codex excursion pages: event-style static pages with local fonts, SOHO/Yandex counters, payment/free order links, footer contacts.
- `combo.fin-academy.pro`: Vite + React product landing, simple component sections, two-tariff offer, content facts isolated from components.
- `vibe.fin-academy.pro` / `arcane-code-weave`: Vite + React + shadcn style, lazy-loaded long-form sections, interactive artifacts, course-program structure.
- `probudget.fin-academy.pro`: finance/webinar landing with hero, bonuses, author proof, testimonials, mobile sticky CTA, guide preview.
- `outsource.fin-academy.pro`: outsourcing/consulting offer, modular content files, strong section order, sticky CTA, premium typography and design audit notes.
- Deployment/fix notes: mandatory counters, UTM passthrough, DNS/server mismatch checks, gzip/no-cache, local fonts, no service files in webroot.

## Practices To Keep

1. **One clear first-viewport promise.** Hero must immediately say what the product is, who it is for, and the next action.
2. **CTA hierarchy.** Use one primary CTA, repeated after major sections. On mobile, add bottom sticky CTA after the first screen.
3. **Proof before complexity.** Put social proof, numbers, recognizable artifacts, screenshots, or real author credibility before long program detail.
4. **Content as data.** For React/Next pages, keep product facts, dates, prices, navigation, FAQ, tariffs, speakers, and reviews in `content/` files when practical.
5. **Modular sections.** Prefer named components: `Hero`, `Stats`, `Program`, `Experts`, `Tariffs`, `FAQ`, `FinalCta`, `Footer`, `StickyCta`.
6. **Layout variety with purpose.** Mix hero artifact previews, proof strips, timelines, tabs, before/after blocks, dark anchors, and sticky summaries when they help explain the offer.
7. **Local assets.** Host fonts and critical images locally. Avoid dependency on Google Fonts for Russian traffic.
8. **Analytics by default.** Add SOHO metrika and a unique Yandex.Metrika ID when available.
9. **UTM survival.** Preserve `utm_*`, `yclid`, `gclid`, `fbclid`, and `gcpc` when users click payment or cross-sell links.
10. **Production verification.** Verify the real domain, not just local build. Check DNS, HTTP status, SSL, counters, gzip, and rendered mobile view.

## Practices Not To Repeat

1. **Fake live seats.** Do not use random/localStorage counters to simulate demand.
2. **Fake urgency.** Do not add countdowns unless the event or deadline is real and confirmed.
3. **One-note decoration.** Do not rely on decorative gradient/orb backgrounds as the main design idea.
4. **Huge embedded base64 pages.** Avoid 5MB single HTML files with dozens of embedded images unless received as legacy input and explicitly approved.
5. **Same card repeated everywhere.** Do not make hero, proof, program, tariffs, FAQ, and final CTA all look like the same generic card grid.
6. **Lovable deploy assumptions.** If a project started in Lovable, do not assume Lovable is the production deploy path.
7. **Wrong-server deploy.** If a pushed/scp'ed file does not appear on prod, check DNS first.
8. **External font blocking.** Do not use `fonts.googleapis.com` / `fonts.gstatic.com` on school pages unless explicitly allowed.
9. **Horizontal mobile tariff tables.** Replace wide pricing tables with mobile tabs, cards, or accordions.
10. **Unverified claims.** Do not publish student counts, revenue, conversion, ROI, or "choice of majority" unless the user confirms the source.
