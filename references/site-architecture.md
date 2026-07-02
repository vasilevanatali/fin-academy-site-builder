# Site Architecture

## Stack Choice

Choose the simplest stack that solves the task.

### Static HTML

Use for:

- one-off webinar/event pages;
- simple promo pages with one HTML file;
- pages where fast deployment and easy copying matter more than reusable code.

Rules:

- keep CSS and JS readable;
- use local font files;
- add analytics in `<head>`;
- avoid piling many unrelated helper scripts into the final production file;
- if page grows beyond maintainable size, move to Vite + React.

### Vite + React

Use for:

- product landing pages;
- multi-section pages with repeated components;
- tariffs, FAQ, reviews, sticky CTA, interactive previews;
- projects that need easy local build and static hosting.

Preferred shape:

```text
src/
  App.tsx
  components/
    Hero.tsx
    Stats.tsx
    Program.tsx
    Experts.tsx
    Tariffs.tsx
    FAQ.tsx
    FinalCTA.tsx
    MobileSticky.tsx
  content/
    site.ts
    tariffs.ts
    faq.ts
    program.ts
  assets/
```

Use `lucide-react` for icons, Tailwind or plain CSS variables for styling, and Framer Motion only when the motion has a clear role.

### Next.js

Use only when:

- the existing project already uses Next;
- metadata/font tooling is important;
- there are server-side needs.

For static school promo pages, Vite or plain HTML is usually simpler.

## Required Content Model

Before coding, capture:

- product name;
- audience;
- offer category: free webinar, paid recording, mini-course, flagship, consulting;
- date/time/timezone if event-based;
- price and access term if paid;
- CTA target and backup CTA;
- payment links;
- Yandex.Metrika ID if available;
- public contact links;
- legal/footer links;
- real proof assets: screenshots, reviews, student counts, company facts, author photos;
- production status: draft, preview, production.

## Section Order

Default commercial page:

1. Header / nav
2. Hero with offer and CTA
3. Proof strip or market/context
4. Who it is for
5. What the user gets
6. Program / lessons / format
7. Artifacts, bonuses, demos, screenshots
8. Authors / experts
9. Tariffs / payment
10. FAQ / objections
11. Final CTA
12. Footer

For short event registration pages, collapse sections but keep hero, proof/relevance, program, speaker, tariff/free registration, FAQ/footer.

## Content Separation

For React/Next, keep mutable business facts outside layout components when the page is more than a quick prototype:

- `content/site.ts`: title, meta, dates, nav, hero, footer;
- `content/tariffs.ts`: prices, features, payment links;
- `content/faq.ts`: questions/answers;
- `content/program.ts`: modules, lessons, schedule;
- `content/speakers.ts`: bios and photos.

This lets the business owner update facts without hunting through JSX.

## Build And Deployment Readiness

Static output must be self-contained:

- `index.html` exists;
- assets are local or intentionally external;
- production build has no source maps unless intentionally public;
- `.env`, credentials, local logs, screenshots, and temporary audit scripts are not in the published output.

