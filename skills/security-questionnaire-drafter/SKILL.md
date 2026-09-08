---
name: security-questionnaire-drafter
description: Draft first-pass answers to a buyer's security questionnaire (SIG, SIG Lite, CAIQ, VSA, or a custom spreadsheet) using the company's own policy documents, past completed questionnaires, and audit reports as the only sources. Use this whenever someone mentions a security questionnaire, vendor security review, security assessment, SIG, CAIQ, VSAQ, due diligence questions, a customer's InfoSec spreadsheet, or says a buyer sent hundreds of security questions and they do not know where to start. Also use it when the request is to reuse or update answers from a previous questionnaire for a new buyer.
---

# Security Questionnaire Drafter

Security review is where deals sit still. A 30 to 150 person vendor typically has the answers scattered across a SOC 2 report, a handful of policy documents, an architecture diagram, and one engineer's memory. This skill turns that scatter into a completed first pass that a human reviews rather than writes.

The value is not speed alone. A wrong answer in a security questionnaire is a contractual representation. So the working rule is: **every answer traces to a source the user supplied, or it is marked as unanswered.** Never fill a gap with a plausible-sounding security claim.

## Step 1: Take inventory before drafting

Ask for whatever is missing, in one message, then proceed with what exists:

- The questionnaire itself (xlsx, csv, docx, pdf, or pasted text)
- Evidence sources: SOC 2 Type II or ISO 27001 report, security or infosec policy, data protection or privacy policy, BCDR plan, subprocessor list, architecture or data-flow diagram, pen test summary
- Past completed questionnaires (the highest-value input by far, reuse beats regeneration)
- The buyer's name and what data the product will touch, which changes how several answers must be scoped

If the user has none of the above, do not draft. Say what is missing, and offer to produce the question list grouped by which document would answer each one, so they can go collect it. That output is genuinely useful on its own.

Read `references/evidence-sources.md` for the standard mapping of question themes to source documents.

## Step 2: Parse and group

Extract every question with its original row or section identifier. Preserve the buyer's numbering exactly; procurement teams match on it.

Group questions by theme (access control, encryption, data retention, subprocessors, incident response, BCDR, secure development, personnel, physical, AI and subprocessing of model data). Grouping matters because one source document usually answers a whole cluster, and because it lets the user route unanswered clusters to the right owner in one message rather than twelve.

## Step 3: Draft with a confidence tier on every answer

Assign exactly one tier per question:

| Tier | Meaning | What to write |
| --- | --- | --- |
| `SOURCED` | The answer is stated in a supplied document or a past questionnaire | The answer, plus the document name and section |
| `DERIVED` | The answer follows from a supplied document but is not stated verbatim | The answer, the source, and one line on the inference made |
| `UNANSWERED` | No supplied source covers it | No answer. Name the likely owner and the document that would settle it |

Never produce a fourth tier and never soften `UNANSWERED` into a hedged answer. A hedge is what gets forwarded to a buyer by accident.

Match the questionnaire's own answer format. If it wants Yes / No / N/A with a comment field, write that, not prose. If a control is genuinely not applicable, say `N/A` and give the one-line reason, because unexplained N/A is the most common trigger for a follow-up round, and a follow-up round costs another week.

## Step 4: Output

Produce two artifacts.

**A. The filled questionnaire** in the format supplied. If it came as a spreadsheet, write a spreadsheet back with the original columns intact plus two added columns: `Confidence` and `Source`. If it came as text, mirror the original structure.

**B. A review brief**, always in this exact shape:

```markdown
# Security questionnaire: [Buyer name]
Questions: [n] · Sourced: [n] · Derived: [n] · Unanswered: [n]

## Send-blockers
[Questions that must be answered by a human before this goes back, one line each, with the named owner]

## Answers to verify before sending
[DERIVED answers, one line each, with the inference made]

## Answers that commit us to something
[Any answer that states a control, an SLA, a retention period, or a timeline the company will now be held to]

## Gaps worth fixing permanently
[Themes where nothing existed. These recur on every deal, so fixing the document once removes the question forever]
```

The "answers that commit us to something" section is the one people skip and regret. Populate it even when it is short.

## Rules

- Do not invent a certification, an audit date, a control, a retention period, or a subprocessor. Not having SOC 2 is a normal, survivable answer. Claiming SOC 2 you do not have is fraud.
- Do not upgrade "we intend to" into "we do".
- Where a past questionnaire and a policy document disagree, flag both and do not pick a winner. That disagreement is a real finding.
- Scope every answer to the product the buyer is actually buying, not the whole company, unless the question asks about the company.
- Where a question asks about AI, model training, or data used for model improvement, answer it exactly as narrowly as the supplied sources allow. This is the fastest-growing questionnaire section and the one where vague answers cause the most damage.
- The final artifact is a draft for human review. Say so in the brief. Never describe it as ready to send.
