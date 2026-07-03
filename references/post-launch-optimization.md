# Post-Launch Optimization

Use this reference when the site is ready to publish, already published, or the user asks how to improve conversion after launch.

## Rule

Do not claim the page is "conversion optimized" forever. Treat launch as version 1.

A good handoff includes:

- what was checked;
- what data is missing;
- what to measure;
- what to test next;
- what not to change without evidence.

## Measurement Setup

Confirm or request:

- Yandex.Metrika ID;
- SOHO metrika;
- goals for CTA/payment/order clicks;
- UTM passthrough;
- thank-you or order confirmation path if available;
- traffic source;
- campaign period;
- target action.

If analytics IDs are missing, mark `данных нет` and use placeholders.

## Suggested Goals

Use only goals relevant to the page:

- hero CTA click;
- tariff CTA click;
- final CTA click;
- payment/order link click;
- Telegram click;
- FAQ opened;
- program section reached;
- application form submitted;
- thank-you page reached.

Do not fire fake success events before real navigation/submission.

## First 72 Hours After Launch

Check:

- page loads on production domain;
- SSL and redirects work;
- mobile first viewport renders correctly;
- all CTA links work;
- UTM parameters survive;
- analytics receives visits and goals;
- no 404 assets;
- no broken payment links;
- no hidden overlays/sticky CTA issues.

## First Optimization Pass

After enough traffic exists, inspect:

- hero scroll depth;
- CTA click rate by section;
- tariff block engagement;
- payment link click-through;
- drop-off before form/payment;
- mobile vs desktop behavior;
- traffic source quality.

If traffic is too small, do not overfit. Use qualitative review and session recordings if available.

## Hypothesis Bank

Offer 3-5 hypotheses in this format:

```text
Hypothesis: [change] will improve [metric] because [reason].
Change: [specific section/component].
Metric: [goal/click/scroll/form].
Risk: [what could get worse].
```

Good hypotheses:

- sharpen hero headline for a specific audience;
- move artifact preview higher;
- add proof before tariff;
- simplify tariff cards;
- add "what happens after payment";
- make sticky CTA label more specific;
- split page for cold vs warm traffic;
- add FAQ answer for price/access/payment objection;
- replace abstract image with real screenshot.

Bad hypotheses:

- make it prettier;
- add more animation;
- change colors because they feel boring;
- add fake urgency;
- hide price to increase curiosity.

## A/B Testing Caution

For small traffic, do not run formal A/B tests too early. Prefer:

- clear fixes first;
- one major change per version;
- before/after metric notes;
- qualitative feedback;
- recording/session review.

Use A/B only when traffic and measurement are sufficient.

## Optimization Handoff

For every production handoff, include:

- current page URL;
- primary conversion;
- analytics/goals present;
- unverified items;
- first 3 measurement checks;
- first 3 improvement hypotheses.
