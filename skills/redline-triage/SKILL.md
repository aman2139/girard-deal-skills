---
name: redline-triage
description: Triage an inbound contract redline (MSA, DPA, order form, SaaS agreement, NDA, or buyer paper) clause by clause into accept, negotiate, and do-not-sign, with the business reason and a suggested response position for each. Use this whenever someone mentions redlines, markup, a buyer's legal team sending changes back, buyer paper, an MSA or DPA to review, contract negotiation, "what should we push back on", or asks which clauses are standard versus unusual. Also use it when someone wants to know which changes are worth paying outside counsel to look at.
---

# Redline Triage

A small company usually cannot afford to send every redline to counsel, so redlines sit. This skill sorts the markup so the expensive review is aimed at the four clauses that matter, and everything else moves.

This is triage, not legal advice. The output names risk and business consequence so a founder can decide what to escalate. It never tells anyone a clause is safe to sign.

## Step 1: Establish the baseline

Triage is meaningless without something to triage against. Ask for whichever of these exists:

- The redlined document (docx with tracked changes, a clean-vs-marked pair, or pasted text)
- The company's own standard terms, if the buyer marked up the company's paper
- Any prior signed agreement with similar terms, which is the strongest available baseline
- Deal context: contract value, term length, what data the product touches, close date

If no baseline exists, say so and triage against market-standard positions instead, labelling the whole output as `NO INTERNAL BASELINE`. That label matters. Without it the user will read market-standard as company-approved.

## Step 2: Classify every changed clause

Read `references/clause-risk-map.md` for the clause-by-clause reference: what the market-standard position is, what a buyer normally asks for, and what makes a given ask unusual.

Assign each change exactly one classification:

| Class | Meaning |
| --- | --- |
| `ACCEPT` | Standard buyer ask, matches baseline or market position, no material new exposure |
| `NEGOTIATE` | Reasonable ask, but the current wording costs money, time, or optionality. Has a landing zone |
| `ESCALATE` | Material exposure, or outside what the company has agreed to before. Needs a named human decision |
| `DO NOT SIGN` | Uncapped or existential exposure, or a term that contradicts something already promised elsewhere |

Do not stretch to fill every class. A redline that is genuinely all `ACCEPT` should come back all `ACCEPT`.

## Step 3: Output

Always this shape:

```markdown
# Redline triage: [Counterparty] · [Document type]
Baseline: [company standard terms / prior signed agreement / NO INTERNAL BASELINE]
Changes reviewed: [n] · Accept: [n] · Negotiate: [n] · Escalate: [n] · Do not sign: [n]

## Do not sign
| Clause | What changed | Exposure | Suggested response |

## Escalate
| Clause | What changed | Why it needs a decision | Who should decide |

## Negotiate
| Clause | What changed | Cost of accepting as written | Landing zone |

## Accept
[One line per clause. No table. These exist to show they were reviewed, not to be discussed]

## What to send counsel
[The short list, ranked. If the whole redline is accept and negotiate, say counsel is not needed for this one and why]

## Deleted or weakened
[Anything removed from the original that the tracked-changes view makes easy to miss: caps, carve-outs, notice periods, survival clauses]
```

The "deleted or weakened" section catches the highest-cost failure mode in redline review. Deletions read as absence, and absence is invisible. Populate it before anything else.

## Step 4: Give landing zones, not just objections

For every `NEGOTIATE` item, write a specific counter-position, not "push back". A landing zone is a sentence the user can paste into a reply:

**Weak:** "The liability cap is too low, negotiate it."

**Usable:** "Cap is at 3 months of fees. Ask for 12 months of fees paid in the prior year, with the standard carve-outs for confidentiality breach and IP indemnity sitting outside the cap. 12 months is where most deals of this size land."

## Rules

- Quote the actual changed language when it matters. Paraphrase changes their meaning, and clause wording is the entire subject here.
- Distinguish what the clause says from what the user is worried it says. Say both when they differ.
- Flag every clause that conflicts with something the company has already told this buyer, in a proposal, a security questionnaire, or a prior agreement. Contradictions between documents surface late and cost weeks.
- Currency, governing law, and notice addresses are boring and frequently wrong. Check them.
- Auto-renewal, price-increase caps, and termination for convenience are the three terms most often accepted without thought and most often regretted. Never file them under `ACCEPT` silently.
- Close with the same line every time: this is triage to focus a review, not legal advice, and a lawyer signs off on anything in `ESCALATE` or `DO NOT SIGN`.
