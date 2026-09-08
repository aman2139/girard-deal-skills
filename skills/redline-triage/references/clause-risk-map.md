# Clause risk map

Reference positions for triaging a B2B SaaS redline. These are common market positions for deals roughly in the $20K to $500K annual range, not legal advice and not company policy. Where a company's own standard terms exist, those win.

## Contents
- Liability and indemnity
- Data, privacy, security
- Commercial terms
- Term and termination
- Operational and boilerplate
- Asks that should always escalate

## Liability and indemnity

| Clause | Common market position | Typical buyer ask | Unusual, escalate |
| --- | --- | --- | --- |
| Liability cap | 12 months of fees paid | 2x to 3x fees, or 12 months plus carve-outs | Uncapped general liability |
| Carve-outs from the cap | Confidentiality breach, IP indemnity, gross negligence | Adding data breach to carve-outs | Carve-out for any breach of the agreement, which erases the cap |
| Consequential damages waiver | Mutual waiver | Mutual, with carve-outs | One-way waiver against the vendor |
| IP indemnity | Vendor indemnifies for third-party IP claims against the service | Adding defense costs | Indemnity covering the buyer's own use, however modified |
| Data breach liability | Sits inside the cap, or a separate super-cap | Super-cap at 2x to 5x fees | Uncapped data breach liability |

## Data, privacy, security

| Clause | Common market position | Typical buyer ask | Unusual, escalate |
| --- | --- | --- | --- |
| DPA | Vendor's standard DPA, SCCs where relevant | Buyer's DPA form | Buyer DPA with a security exhibit written for an enterprise vendor |
| Subprocessors | List, plus notice of changes | Approval rights over new subprocessors | Right to reject any subprocessor with no cure path |
| Data residency | Region of the deployed instance | Specific region commitment | Guaranteed residency the current architecture cannot deliver |
| Deletion on termination | 30 to 90 days | 30 days, with certification | Immediate deletion with certification inside 24 hours |
| Audit rights | Right to receive SOC 2, plus a questionnaire annually | Annual audit with notice | On-site audit on demand, or audit of subprocessors |
| Security requirements exhibit | Reference to the vendor security policy | Specific controls listed | Controls the company does not currently run, promised as present tense |

## Commercial terms

| Clause | Common market position | Typical buyer ask | Unusual, escalate |
| --- | --- | --- | --- |
| Payment terms | Net 30 | Net 45 or Net 60 | Net 90, or payment contingent on acceptance testing |
| Price increases | Capped at a percentage on renewal | Cap at CPI or a fixed percentage | Price locked for the life of the relationship |
| Most favoured nation | Not offered | Sometimes requested | Any MFN clause, always escalate, they bind future pricing |
| Fees for overage | Stated rate | Notice before overage billing | Overage waived entirely |
| Invoicing and PO | Invoice on signature, annual in advance | PO reference required | Payment only after buyer-side milestones |

## Term and termination

| Clause | Common market position | Typical buyer ask | Unusual, escalate |
| --- | --- | --- | --- |
| Initial term | 12 months | 12 months with a pilot period | Month to month at annual pricing |
| Auto-renewal | Auto-renews with 30 days notice to cancel | Notice extended to 60 days | Renewal only on written buyer confirmation, which is not a renewal |
| Termination for convenience | Not offered, or offered with a fee | 30 to 90 days notice | Termination for convenience with a pro-rata refund |
| Termination for cause | Material breach with a 30 day cure | 15 day cure | No cure period |
| Refunds | Pro-rata for vendor breach only | Pro-rata on any termination | Full refund on any termination |

## Operational and boilerplate

Frequently changed, frequently missed:

- **Governing law and venue.** A buyer moving venue to their home state is normal. Moving it to a country where the company has no counsel is not.
- **Notice provisions.** Email notice versus registered post changes how fast anything can happen.
- **Assignment.** Vendors need assignment on change of control. A buyer removing that clause can complicate an acquisition years later.
- **Publicity and logo rights.** Usually removed by the buyer. Worth one ask, never worth blocking a deal.
- **Survival.** Check that confidentiality, liability, and payment obligations survive termination. Deletion of a survival clause is easy to miss.
- **Insurance.** Specific coverage amounts, including cyber liability, may require buying a new policy. Price that before agreeing.
- **Service levels.** An SLA with credits is normal. An SLA with termination rights attached to a single miss is not.

## Asks that should always escalate

- Uncapped liability of any kind
- Any most favoured nation clause
- Source code escrow
- Buyer ownership of anything beyond buyer data, particularly of output, configurations, or feedback
- Non-compete or exclusivity language
- Unilateral amendment rights
- Any commitment to a control, certification, or date the company does not currently hold
