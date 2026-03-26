> **This document is not yet active.** It is being prepared for adoption once the community has established its initial operations. When adopted, it will replace the current interim admin structure described in the [README](../README.md).

# Governance

This document defines how decisions are made, who makes them, and how the structure can change.

## Steering council

The steering council provides overall direction, resolves disputes, and makes decisions when community consensus cannot be reached.

| Member | Handle | Role |
|--------|--------|------|
| Jordan McKinney | @jordanmmck | Founding council member |
| Jáchym Fibír | @kluck77 | Founding council member |
| Bradley Stephenson | @orphiceye | Founding council member |

**Responsibilities**: setting research direction and priorities, resolving contribution and authorship disputes, managing community infrastructure access (GitHub org admin, Discord admin), approving IP-related decisions, enforcing the Code of Conduct, and amending governance documents.

**Quorum**: at least 2 of 3 council members must participate for any formal decision.

**Non-responsiveness rule**: in any decision requiring a council vote, if a council member has been notified of the vote and does not respond within 72 hours, the remaining council members may proceed and vote without them.

## Decision-making tiers

Most activity in this community does not require permission. Decision-making scales in formality based on impact:

### Tier 1: just do it
Routine work. Start coding, writing, researching, posting, reviewing. Inform others in the relevant Discord channel or GitHub issue. No approval needed.

**Examples**: fixing a bug, writing a blog post, adding a wiki page, reviewing a PR, running an experiment, posting on social media.

### Tier 2: lazy consensus (72 hours)
Moderate decisions affecting shared resources or community direction. Post your proposal in `#governance` or the relevant GitHub Discussion. State clearly: "I plan to do X. I'll proceed in 72 hours unless someone objects." Silence equals consent. Objections must include a reason and a proposed alternative.

**Examples**: adding a new Discord channel, adopting a new tool, proposing a new workstream, changing a workflow, inviting a batch of new members.

### Tier 3: council discussion (7 days)
Significant decisions. Open a GitHub Discussion with the `governance` label. Minimum 7-day comment window. If community consensus emerges, the council ratifies it. If not, the council decides by simple majority.

**Examples**: major changes to project scope, spending shared funds, entering partnerships, publishing under the community name, removing a member.

### Tier 4: formal vote
Constitutional-level changes. Explicit vote by the steering council with a 7-day public comment period beforehand. Amendments to the Charter or Governance document require a two-thirds supermajority of the full council. All other Tier 4 decisions require simple majority.

**Examples**: amending the Charter or Governance document, changing the governance structure, adding or removing council members, altering IP or licensing policy.

## Joining and leaving the council

**Adding a member**: any current council member may nominate a candidate. The nomination is posted in `#governance` with a 7-day comment period. If no council member objects, the candidate joins. If objections arise, the existing council votes (simple majority).

**Voluntary departure**: written notice in `#governance`. The departing member's responsibilities transfer to remaining council members until a replacement is nominated.

**Removal for inactivity**: if a council member is unresponsive for 3 consecutive months, the remaining council members may vote to remove them by simple majority.

**Removal for cause**: even without inactivity, a council member may be removed for justified reason by a unanimous vote of all remaining council members. This rule does not apply when there are only 3 council members (to prevent 2-against-1 power plays at minimum council size).

**Minimum council size**: 3 members. If the council drops below 3, appointing new members becomes the top priority and follows an expedited 72-hour nomination process.

## Workstream leads

Each workstream may have a lead who coordinates work, manages the relevant project board, and makes Tier 1/2 decisions within their domain. Workstream leads are nominated by the council or self-nominated with council approval. They do not need to be council members.

`[PLACEHOLDER: Initial workstream lead assignments, to be decided on first community call]`

## Infrastructure access

| Resource | Admin(s) | How to get access |
|----------|---------|-------------------|
| GitHub organization | Steering council | Request on weekly call or DM a council member |
| GitHub repository write access | Steering council + repo maintainers | Same as above |
| GitHub Projects (task boards) | Steering council | Same as above |
| Discord server admin | Steering council | Council decision only |
| Discord moderation | Steering council + designated moderators | Nominated by council |
| Contribution ledger | Steering council | View access by default; edit access by request |
| Social media accounts | `[PLACEHOLDER: who manages these]` | Council approval required |

## Intellectual property

Unless otherwise decided through the council (via Tier 3 discussion), all code produced by the community is open source and released under Apache 2.0. All research, documentation, and content are released under CC-BY-SA 4.0. Exceptions (e.g. a member or commercial partner contributing proprietary components that interface with community infrastructure) require explicit council approval and documentation.

Individual members retain the right to build upon collective work within the terms of these licenses. Members may not claim sole ownership of community-produced work. Attribution follows the contribution tracking record and the co-authorship policy in [CONTRIBUTING.md](../CONTRIBUTING.md).

## Amendment

Both this Governance document and the [Charter](../CHARTER.md) may be amended through the Tier 4 process: a two-thirds supermajority vote of the full steering council, with a 7-day public comment period beforehand.

`[DRAFT STATUS: This governance document has not yet been formally ratified by the community. Until ratification occurs at [PLACEHOLDER: date/event], the amendment process above does not apply, and the founding council may revise this document directly.]`

## See also

- [Charter](../CHARTER.md): Mission and scope
- [Code of conduct](../CODE_OF_CONDUCT.md): Enforcement contacts and process
- [Contributing guide](../CONTRIBUTING.md): How to participate
