---
name: fin-academy-site-builder
description: Build, improve, audit, and prepare visually polished, trend-aware, conversion-focused websites and landing pages for Fin Academy / Master CFO educational products, webinars, mini-courses, excursions, consulting offers, and static promotional pages. Use when creating or editing school/product sites such as ChatGPT, Claude, Codex, AI-combo, vibe-coding, finance/probudget, outsourcing/consulting, or similar Russian landing pages; when extracting a brief into site strategy, conversion structure, current-year design direction, stronger page composition, varied layout patterns, artifact previews, pricing sections, responsive design, accessibility, Core Web Vitals readiness, analytics, UTM passthrough, payment CTAs, sticky mobile CTA, public promo links, QA, post-launch optimization, or deployment-ready static/Vite/Next output.
---

# Fin Academy Site Builder

## Overview

Use this skill to turn a business brief into a usable, polished, trend-aware, conversion-oriented site for a Fin Academy / Master CFO product. It encodes patterns extracted from recent school sites: Codex, ChatGPT/Claude excursions, AI-combo, vibe-coding, probudget, outsourcing/consulting, and site deployment fixes.

## Non-Negotiables

1. Work in Russian by default for page copy, reports, and handoff notes.
2. Do not invent numbers, dates, student counts, conversion rates, prices, deadlines, bonuses, or testimonials. If data is missing, write `данных нет` and use placeholders.
3. Do not use fake urgency: no random seat counters, fake countdowns, or arbitrary "last chance" messaging.
4. Do not publish, deploy to production, change DNS, start sales, or send analytics events without explicit user approval.
5. Do not include secrets in code, repo, docs, screenshots, logs, or final output. Keep tokens only in `.env` or local credentials outside the repo.
6. Prefer static HTML or Vite + React for promo pages. Use Next.js only when the existing project already uses it or the task explicitly needs it.
7. Use real/generated visuals, real product screenshots, lesson previews, speaker photos, or branded media. Avoid generic abstract decoration as the main visual.
8. Verify mobile first. For these sites, 390px mobile is a primary viewport, not an afterthought.

## Workflow

1. **Collect brief.** Identify offer, audience, price, access term, date, CTA target, payment link, required legal/footer links, analytics IDs, source assets, and whether the page is draft or production.
2. **Choose stack.** For a one-off event or fast promo page, prefer static HTML or Vite SPA. For a larger modular page with many sections/content files, use Vite/React or existing Next structure. See [site-architecture.md](references/site-architecture.md).
3. **Choose strategy and design direction.** Pick a conversion goal, trust argument, visual direction, and 2-4 trend-aware tactics that fit the offer. See [conversion-playbook.md](references/conversion-playbook.md), [design-directions.md](references/design-directions.md), and [trend-radar-2026.md](references/trend-radar-2026.md).
4. **Design the conversion structure.** Build the page around hero -> proof -> pain/job -> program/contents -> artifacts/bonuses -> authors -> tariffs/payment -> FAQ -> final CTA. See [conversion-copy.md](references/conversion-copy.md).
5. **Apply visual system and layout patterns.** Use restrained, domain-specific design with strong first-viewport signal, local fonts, stable spacing, mobile sticky CTA, clear section rhythm, and non-repetitive layouts. See [design-qa.md](references/design-qa.md), [layout-patterns.md](references/layout-patterns.md), and [visual-swipe-file.md](references/visual-swipe-file.md).
6. **Add analytics and UTM.** Add SOHO metrika, Yandex.Metrika when an ID is provided, and UTM passthrough to payment/excursion links. See [analytics-deploy.md](references/analytics-deploy.md).
7. **Use public promo links only when appropriate.** Use known public examples and Telegram channels from [promo-links.md](references/promo-links.md); never include private invite links or internal exports.
8. **Run checks.** Build/lint if a project has scripts. Run `python3 scripts/site_audit.py <path-or-url>` against the output HTML or built folder. Run `python3 scripts/link_audit.py <path-or-url>` when links/anchors matter. For browser apps, inspect desktop, 390px mobile, and at least one CTA/payment path.
9. **Plan optimization.** For production or campaign pages, propose 3-5 measurable post-launch improvements instead of declaring conversion "done". See [post-launch-optimization.md](references/post-launch-optimization.md).
10. **Handoff clearly.** Report what was created/changed, where the files are, what was verified, what remains unverified, and what needs user approval before production.

## Source Patterns

Read [source-lessons.md](references/source-lessons.md) when you need examples of what was learned from prior sites and what not to repeat.

Read [layout-patterns.md](references/layout-patterns.md) when a page needs stronger visual composition, varied section layouts, artifact previews, interactive blocks, or a less generic landing-page feel.

Read [trend-radar-2026.md](references/trend-radar-2026.md) before proposing "trendy" design choices. Use trends only when they support clarity, trust, speed, or conversion.

Read [conversion-playbook.md](references/conversion-playbook.md) when the user asks for sales, leads, registration, payment, or conversion improvement.

Read [design-directions.md](references/design-directions.md) when starting a new site or redesign so the page has a coherent visual concept.

Read [visual-swipe-file.md](references/visual-swipe-file.md) when you need reusable high-performing section ideas without copying external websites.

Read [post-launch-optimization.md](references/post-launch-optimization.md) when a page is ready to publish or the user asks how to improve results after launch.

## Fast Prompts

Create a new landing:

```text
Use $fin-academy-site-builder to create a landing page for [product].
Audience: [who].
Offer: [what is sold/free].
Price/date/access: [facts only].
CTA link: [link or placeholder].
Choose a design direction and conversion hypothesis before coding.
Leave production deploy disabled until I approve.
```

Audit an existing site:

```text
Use $fin-academy-site-builder to audit this landing for conversion, mobile, analytics, UTM, fake claims, and deployment readiness: [path or URL].
Give prioritized fixes, trend/staleness risks, and post-launch hypotheses. Do not change production without approval.
```

Improve an existing page:

```text
Use $fin-academy-site-builder to improve this page using Fin Academy site patterns.
Keep the offer and facts unchanged. Improve section rhythm, layout variety, artifact previews, mobile CTA, typography, proof blocks, tariff section, analytics, and QA.
```
