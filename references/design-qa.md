# Design And QA

## Visual Direction

Sites for finance, education, outsourcing, and consulting should feel competent, premium, and usable. Avoid generic SaaS gradients and oversized decorative layouts.

Use:

- restrained palette with 2-3 neutral levels and one accent;
- clear section rhythm;
- varied layout mechanics instead of a repeated stack of identical cards;
- one explicit design direction from [design-directions.md](design-directions.md);
- 2-4 current-year tactics from [trend-radar-2026.md](trend-radar-2026.md) only when they serve clarity/trust/conversion;
- local fonts;
- real media: speaker photos, screenshots, product previews, lesson artifacts;
- strong typography hierarchy;
- sticky mobile CTA;
- generous but not empty spacing.

Avoid:

- pages dominated by one hue family;
- beige/brown/orange-only palettes without contrast;
- decorative orbs/bokeh as main visual language;
- cards inside cards;
- tiny gray text with low contrast;
- wide mobile tables;
- hero text in a card;
- fake counters and fake urgency.

For stronger section composition, use [layout-patterns.md](layout-patterns.md).

## Typography

Use a consistent type scale:

- H1: 34-56px depending on viewport and hero density;
- H2: 32-48px;
- lead: 18-22px;
- body: 16-18px;
- captions: 12-14px minimum.

Use tabular numbers for stats/prices. Do not use negative letter spacing as a crutch. Keep letter spacing at `0` unless using small uppercase eyebrow labels.

## Section Rhythm

Alternate section tones intentionally:

- calm light section;
- richer light/beige/cream section;
- dark anchor section for tariff/proof/final CTA;
- visual divider only when it marks a real act change.

For long pages, add 2-3 dark or high-contrast anchor moments instead of making every section similar.

## Mobile Rules

Primary mobile viewport: 390px.

Check:

- bottom sticky CTA does not cover content; add bottom spacer;
- buttons are at least 44px high;
- hero badges wrap, no `nowrap` on long Russian text;
- pricing is cards/tabs, not horizontal scroll;
- testimonial screenshots are large enough or openable;
- tables are converted to cards or accordions;
- text does not overflow buttons/cards;
- no section relies on hover only.

## Accessibility And Performance

Use WCAG 2.2 as the practical baseline where possible:

- interactive targets should be at least 24x24 CSS px, and primary CTAs should be comfortably larger;
- focus states must be visible;
- text and non-text UI contrast must be readable;
- keyboard navigation must not trap the user;
- motion should respect reduced-motion preferences.

Aim for Core Web Vitals readiness:

- LCP: keep hero media optimized and avoid render-blocking assets;
- INP: avoid heavy scripts and unnecessary interaction handlers;
- CLS: reserve dimensions for images, embeds, banners, and sticky UI.

## Motion

Use motion sparingly:

- reveal cards on scroll;
- small hover lift on desktop;
- optional number count-up for real stats;
- carousel only when content benefits from it.

Respect reduced-motion where practical. Do not animate every section.

## Media

Use real/generated assets that reveal the actual offer:

- product screenshot;
- lesson/player preview;
- prompt pack/workbook pages;
- dashboard preview;
- speaker portrait;
- webinar room/event photo.

Do not use dark blurred stock-like images if the user needs to understand the product.

## QA Checklist

Before delivery:

- desktop screenshot checked;
- mobile 390px screenshot checked;
- hero first viewport shows offer, CTA, and visual signal;
- long pages use several distinct section patterns, not one repeated card template;
- sticky CTA works and does not overlap footer;
- all CTAs point to correct URLs or explicit placeholders;
- footer has legal/contact links;
- analytics scripts present when IDs are provided;
- UTM passthrough works on payment/cross-sell links;
- Core Web Vitals risks reviewed: LCP, INP, CLS;
- accessibility risks reviewed: target size, focus states, contrast, reduced motion;
- no invented facts;
- no secrets in repo/output;
- build command passes if present.
