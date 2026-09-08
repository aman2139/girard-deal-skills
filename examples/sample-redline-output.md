# Redline triage: [Buyer] · Master Services Agreement

Baseline: vendor standard terms
Changes reviewed: 11 · Accept: 1 · Negotiate: 3 · Escalate: 5 · Do not sign: 2

## Do not sign

| Clause | What changed | Exposure | Suggested response |
| --- | --- | --- | --- |
| 8.2 Exclusions from cap | Added "any breach of Supplier's obligations under this Agreement" to the carve-outs | This erases the cap. Every claim is a breach of some obligation, so a cap that excludes all breaches is not a cap. At $84K ACV the exposure is unbounded | "We can carve out confidentiality and the IP indemnity, which is standard. A general carve-out for any breach removes the cap entirely, so we cannot accept it. Proposed: carve-outs limited to Sections 9 and 10, with Section 9 subject to a super-cap of 2x annual fees." |
| 3.5 Service levels | Added 99.99% monthly uptime, with termination for cause after two consecutive misses and no cure period | 99.99% is 4.3 minutes of downtime per month. A miss is likely, and two misses hand the buyer a termination right nine months into a paid annual term | "We commit to 99.9% measured monthly with service credits. 99.99% is not a target we operate to and we will not represent that we do. Termination should follow the standard material breach and 30 day cure path in 12.2." |

## Escalate

| Clause | What changed | Why it needs a decision | Who should decide |
| --- | --- | --- | --- |
| 9.4 Breach notification | 72 hours reduced to 24 hours from awareness | This is an operational commitment, not a legal one. It requires detection, triage, and a notification path that runs inside one day, including weekends | Head of engineering |
| 9.7 Data residency | New EEA-only storage and processing requirement | Either the architecture delivers this today or it does not. If it does not, this is a build commitment with a date, not a contract term | Head of engineering |
| 9.9 Subprocessors | Notice replaced with prior written approval at the buyer's sole discretion | Sole discretion with no cure path means a single buyer can block a routine infrastructure change for the whole company | Founder, with engineering |
| 12.1 Term and renewal | Auto-renewal replaced with renewal only on written buyer confirmation | This is not a renewal mechanism, it is an annual re-sale. It changes the forecast treatment of the account | Founder |
| 14.2 Governing law | Delaware replaced with Republic of Ireland | Enforcement in a jurisdiction where the company has no counsel. Usually tradeable against something the buyer wants more | Founder |

## Negotiate

| Clause | What changed | Cost of accepting as written | Landing zone |
| --- | --- | --- | --- |
| 8.1 Limitation of liability | 12 months of fees paid, replaced with 3x total fees payable | Cap moves from roughly $84K to roughly $252K | 12 months of fees paid in the prior 12 months, standard carve-outs outside the cap. If movement is needed, 2x annual fees with a data-protection super-cap is a common landing point at this deal size |
| 5.2 Payment terms | Net 30 to Net 60 | 30 additional days of working capital on an $84K contract | Net 45, or Net 60 in exchange for annual prepay |
| 5.4 Price increases on renewal | 7% renewal cap struck entirely | Deleting the cap also deletes the express right to increase. Silence here most likely means fees are fixed unless separately agreed, which is worse than the 7% cap | Reinstate 5.4. If the buyer wants a lower number, 5% is worth more than an ambiguous silence |

## Accept

- 15.3 Publicity. Logo and name rights struck. Standard buyer position, worth one ask at signature and nothing more.

## What to send counsel

1. 8.2 carve-out language. This is the one clause where wording, not intent, decides the outcome.
2. 3.5 service levels, specifically whether termination rights can attach to SLA misses without a cure period.
3. 14.2 governing law, if the buyer holds on Ireland.

Everything else is a business decision, not a legal one.

## Deleted or weakened

- **5.4 price increase cap, struck entirely.** Reads as a concession to the vendor and is not one.
- **12.1 auto-renewal, removed.** The revenue mechanic of the contract changed, and the tracked-changes view shows it as one edited sentence.
- **9.9 notice mechanism, deleted** before the approval right was added. The deletion is the substantive change.
- **Annex B does not exist.** New Section 9.7 refers to "the Security Requirements set out in Annex B". No Annex B is attached to the document. Either the buyer intends to attach a security exhibit that has not been reviewed, or the reference is a drafting error. Resolve before signature, because an unreviewed security annex is where undeliverable control commitments enter a contract.

---

Triage to focus a review, not legal advice. A lawyer signs off on anything in `ESCALATE` or `DO NOT SIGN`.
