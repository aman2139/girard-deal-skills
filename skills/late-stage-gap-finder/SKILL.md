---
name: late-stage-gap-finder
description: Check a near-final contract, order form, or SOW against the terms that are commonly missing or internally inconsistent before signature, covering SLAs, data residency, liability caps, notice periods, auto-renewal, subprocessors, and cross-document contradictions. Use this whenever someone is close to signature and wants a final check, mentions procurement review or a contract about to be signed, asks what they might have missed, wants to know what procurement or legal will catch, or is assembling an order form, SOW, or DPA package for execution.
---

# Late Stage Gap Finder

A term that surfaces in week eleven costs ten to twenty-one days. The same term surfaced in week two costs an email. This skill is the week-two check run at whatever week the user is actually in.

Two distinct jobs, both required:

1. **Missing terms.** Things that should be in a contract of this type and are not.
2. **Contradictions.** Places where the contract disagrees with itself, with the order form, with the DPA, or with what the company already told this buyer in a proposal or a security questionnaire.

The second job is the one that catches the expensive problems, because a contradiction between two documents is invisible while reading either one.

## Step 1: Gather the whole package

A single document cannot be gap-checked properly. Ask for everything that will be signed or has already been sent:

- The main agreement (MSA, SaaS agreement, or buyer paper)
- Order form or quote
- DPA and any security exhibit
- SOW or implementation scope
- SLA
- The proposal or pricing document sent earlier
- Completed security questionnaire responses, if one was returned to this buyer

Whatever is missing, note it and check what exists. Then say explicitly which documents were not reviewed, because a gap check that silently skipped the order form is worse than no gap check.

Read `references/gap-checklist.md` for the full checklist to run, organised by document type.

## Step 2: Run the checklist, then the cross-check

Work the checklist first, then run the cross-document comparison. Compare every one of these across all supplied documents, since they routinely disagree:

- Price, quantity, and billing frequency
- Contract start date, end date, and term length
- Legal entity names on every document
- Notice periods, stated in each place they appear
- Data retention and deletion periods
- Security controls promised in the questionnaire versus committed in the agreement
- SLA targets in the SLA versus referenced in the agreement
- Anything numeric that appears in more than one document

Numeric disagreement between an order form and an MSA is the single most common late-stage finding, and the easiest to prevent.

## Step 3: Rank by what it costs

Do not output a flat list. Rank findings by the cost of finding them later:

| Severity | Meaning |
| --- | --- |
| `BLOCKER` | Do not sign. Contradiction, uncapped exposure, or a commitment the company cannot meet |
| `WILL BE CAUGHT` | Procurement or legal will find this and send it back, adding a round trip |
| `FIX NOW, CHEAP` | Missing but trivial to add before signature |
| `ACCEPTED RISK` | Genuinely missing, arguably fine at this deal size, name it so the choice is deliberate |

`ACCEPTED RISK` is not padding. Naming a risk the company chooses to run is the difference between a decision and an oversight.

## Step 4: Output

```markdown
# Pre-signature check: [Counterparty]
Documents reviewed: [list] · Not reviewed: [list] · Deal value: [value] · Target signature: [date]

## Blockers
| Finding | Where | Why it blocks | Fix |

## Procurement will catch this
| Finding | Where | Expected round-trip cost | Fix |

## Fix now, cheap
[One line each, with the suggested language]

## Accepted risk
[One line each. Present so the team is choosing, not missing]

## Contradictions between documents
| Term | Document A says | Document B says |

## What to fix in the template
[Findings that will recur on every future deal. Fixing the template once removes them permanently]
```

## Rules

- Quote the exact clause and its location for every finding. "Section 8.2 caps liability at 3 months of fees" is actionable. "The liability cap looks low" is not.
- Check the trivially wrong things first, because they are common and embarrassing: entity names, dates, signature blocks, exhibit references pointing at exhibits that do not exist, defined terms used but never defined.
- Where the contract commits the company to a control, certification, or SLA, ask whether the company actually delivers it today. A commitment the company cannot meet is a `BLOCKER` regardless of how standard the wording is.
- Do not rewrite the contract. Findings and suggested language only.
- This is a completeness and consistency check, not legal advice. State that once, at the end, and route anything in `BLOCKER` to a lawyer.
