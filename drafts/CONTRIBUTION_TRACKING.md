> **This document is not yet active.** It describes the contribution tracking system being developed for the community. When ready, its contents will be integrated into [How we work](../HOW_WE_WORK.md) and [Contributing guide](../CONTRIBUTING.md).

# Contribution tracking system

## Overview

The community tracks contributions through weekly self-reporting and peer recognition. This data serves three purposes:

1. **Recognition**: making visible the full range of work people do
2. **Authorship**: informing co-authorship decisions on research outputs
3. **Future equity**: if the community pursues funding, tokenization, or formalization into a legal entity, the accumulated contribution record will be the primary input for determining ownership shares

The specific formula for converting contribution records into ownership shares has not been decided. It will be proposed through the Tier 3 governance process when the need arises, with full community input. Until then, the data accumulates and is visible to all members.

## Weekly tracking cycle

1. On `[PLACEHOLDER: day]`, the contribution bot posts a reminder in `#contributions` asking members to log what they worked on that week
2. Members submit their contributions via the bot
3. The bot compiles and posts a summary table of all contributions for the week
4. Community members react to contributions they appreciate: :+1: (like, 1 point) or :heart: (heart, 3 points)
5. Points are tallied alongside self-reported hours and verified deliverables to build each member's contribution record

This data accumulates in the contribution ledger (Google Sheets) and will inform future decisions about ownership shares, authorship priority, and resource allocation.

## Contribution taxonomy

| Emoji | Category | Examples |
|-------|----------|----------|
| :computer: | Code & technical | Software development, bug fixes, infrastructure, tooling, CI/CD |
| :microscope: | Research & knowledge | Experimental design, data collection, evals, analysis, literature reviews |
| :memo: | Writing & documentation | Papers, preprints, blog posts, wiki pages, tutorials, guides |
| :mega: | Outreach & promotion | Social media posts, articles, podcast appearances, conference talks |
| :handshake: | Community building | Onboarding, moderation, organizing events, mentoring, recruiting |
| :briefcase: | Fundraising & strategy | Grant applications, partnership development, investor outreach, proposals |
| :mag: | Review & QA | Code review, peer review of research, testing, feedback on proposals |

This taxonomy adapts the [All Contributors](https://allcontributors.org/docs/en/emoji-key) specification to match the community's work.

## Non-code contribution logging

All non-code contributions are tracked through the weekly contribution cycle in the `#contributions` Discord channel:

1. **Log your work** when the weekly reminder bot posts (every `[PLACEHOLDER: day]`). Describe what you did in natural language. Include links to deliverables where applicable (published posts, submitted applications, wiki edits, etc.).
2. **Community recognition**: after the bot posts the weekly summary table, community members react with :+1: (1 point) or :heart: (3 points) to contributions they find valuable.
3. **Accumulation**: your points, self-reported hours, and verified deliverables accumulate in the contribution ledger over time.

## Contribution ledger structure

The contribution ledger (Google Sheets) has the following structure:

- **Sheet 1: "Raw log"** – columns: Week, Date submitted, Contributor (Discord handle), Category, Description (natural language), Evidence URL, Self-reported hours, Peer likes (bot-filled), Peer hearts (bot-filled), Points total (formula: likes × 1 + hearts × 3)
- **Sheet 2: "Running totals"** – pivot table by contributor showing cumulative hours, cumulative points, and contribution count per category
- **Sheet 3: "Weekly snapshots"** – auto-generated weekly summary

## Discord bot requirements

`[PLACEHOLDER: Build or configure the Discord contribution bot. Requirements:]`

- Posts a reminder message in `#contributions` every `[PLACEHOLDER: day]` at `[PLACEHOLDER: time]`
- Accepts contribution submissions (format TBD: slash command, form, or thread reply)
- Compiles and posts a formatted summary table in `#contributions` at end of submission window
- Reads :+1: and :heart: reactions on the summary and tallies points
- Exports data to the Google Sheet (or stores in its own database that syncs)
- Note: this bot needs to be built. Options: custom bot (Python/discord.py), a no-code automation (Zapier/Make connecting Discord to Google Sheets), or a temporary manual process until the bot is ready.

## Temporary manual fallback (if bot is not ready)

Each week, a designated person (rotate among admins) posts a reminder in `#contributions`:

> "**Weekly contributions**: reply to this thread with what you worked on this week. Include: category, description, hours, and links to deliverables if applicable."

After 48 hours, the same person manually compiles submissions into the Google Sheet and posts a summary table as a message in `#contributions` for reactions. Track reactions manually and enter into the sheet.

## Changes to existing documents when adopted

When this system is adopted, the following documents should be updated:

- **HOW_WE_WORK.md**: Add the "Contribution tracking cycle" section back, referencing the weekly rhythm
- **CONTRIBUTING.md**: Replace the "Under construction" note in the "Contribution tracking" section with the full tracking process and taxonomy
- **README.md**: Add Google Sheets to the Tools table
