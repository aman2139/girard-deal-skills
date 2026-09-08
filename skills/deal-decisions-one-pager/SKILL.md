---
name: deal-decisions-one-pager
description: Turn scattered past decisions about pricing, discounts, contract terms, and security exceptions into one reference page a sales team can actually use, built from Slack threads, email, closed contracts, approval messages, and meeting notes. Use this whenever someone says reps keep asking the same pricing or terms questions, that different reps quote different discounts, that nobody knows what has been approved before, that decisions live in Slack, that they need a deal desk or an approval matrix or a discount policy, or that they want to write down what the company has already agreed to.
---

# Deal Decisions One Pager

Companies under about 150 people rarely lack decisions. They lack a place decisions live. The same discount question gets asked, escalated, answered, and forgotten roughly once a quarter, and each round costs days.

This skill reconstructs what has already been decided from raw evidence and compresses it into one page. It is an archaeology job, and the discipline is the same as archaeology: report what the evidence supports, mark what it does not.

## Step 1: Collect evidence

Ask for whatever exists. Volume helps here, so encourage a dump rather than a curated set:

- Exported Slack or Teams threads from deal, pricing, or approvals channels
- Email threads where an exception was requested or granted
- Signed contracts and order forms, especially non-standard ones
- Pricing pages, rate cards, discount matrices, however outdated
- CRM notes on closed-won and closed-lost deals
- Any existing policy doc, even a half-finished one

If a connector is available for the source system, use it to pull the threads directly rather than asking the user to paste. Ask before reading anything outside the channels or folders named.

## Step 2: Extract decisions, not discussion

A decision has four parts. Reject anything missing the first two:

1. **The question** that was being answered
2. **The answer** that was given
3. **Who** gave it
4. **When**, and on which deal

Discussion is not decision. "I think we could probably go to 20%" is not a decision. "Approved 20% for Acme, 3-year term only" is. Where the thread is ambiguous, capture it as an open question rather than promoting it.

Read `references/term-taxonomy.md` for the standard set of terms to group decisions under, so the page has the same shape every time it is rebuilt.

## Step 3: Detect conflicts before writing

Sort each term's decisions by date. Then look for:

- **Contradictions.** Two decisions on the same term that cannot both be true. Report both with dates and let the human resolve it.
- **Drift.** A discount floor that moved three times in six months without anyone announcing a change.
- **Precedent risk.** A one-off exception granted for a named account that reps have since started treating as standard.

Conflicts are the most valuable output of this skill. A clean page that hides a contradiction is worse than a messy page that surfaces it.

## Step 4: Output

Always this shape. Keep it to one page of real content. If it runs to three, the specifics have been over-collected and the rules under-extracted.

```markdown
# Deal decisions: [Company]
Built from [n] sources · Covering [date range] · Last updated [date]

## Standard position
| Term | What we do | Decided by | Date | Source |

## Approved exceptions
| Term | Exception | Conditions it required | Who approved | Deal | Date |

## Needs approval, and from whom
| Situation | Who signs off |

## Open, never actually decided
[Questions the evidence shows were raised and never resolved. These are the next four things worth deciding, before the next deal forces them at speed]

## Conflicts found
[Where two decisions disagree, both stated, both dated. No resolution offered]
```

## Step 5: Tell the user how to keep it alive

The page decays. Close with two lines: who owns it, and the trigger for updating it (typically, any exception approved outside the standard position gets added the same day). A page nobody owns is stale within a quarter, and a stale decisions page is worse than none because people trust it.

## Rules

- Attribute every line. An unattributed rule is unenforceable, and reps will not risk a discount on an anonymous claim.
- Never invent a policy to fill a category. An empty section labelled "never decided" is the correct and useful output.
- Preserve the exact numbers. "Around 15%" becomes "15% (Acme, 2025-03-11)".
- Distinguish a floor from a target from a one-off. These get conflated constantly and the conflation is what causes margin leak.
- Where a decision was clearly conditional, keep the condition attached. "20% approved" and "20% approved on a 3-year prepay" are different rules, and dropping the condition is how a discount floor quietly collapses.
- Redact nothing on your own initiative, but flag anything that looks like it should not be in a document reps can see, such as customer-specific commercial terms subject to confidentiality.
