# Security

This repository ships plain-text instructions that people load into an AI assistant and then point at their own contracts, security questionnaires, and pricing decisions. Those are sensitive documents, so the security properties of what is in here are worth stating precisely.

## What these skills do and do not do

Every skill in `skills/` is a markdown file. Verifiable by reading it:

- No skill declares `allowed-tools`, so none of them can run a command on your machine.
- No skill executes code, opens a network connection, or calls an external service.
- No skill contains telemetry, analytics, tracking pixels, or a callback of any kind.
- Girard receives nothing. We cannot see what you run through these, and there is no mechanism by which we could.
- Whatever you attach goes to your AI provider under the terms you already have with them, and nowhere else.

The only executable files in this repository are `scripts/validate_skills.py` and `scripts/package.sh`. Both run locally, only when you run them, and neither touches the network. `validate_skills.py` reads files and prints results. `package.sh` runs the validator and builds zip archives in `dist/`.

## Verify before you install

You are about to give these instructions to an assistant that will read your contracts. Treat them the way you would treat any dependency.

1. Read the `SKILL.md` you are installing. Each one is under 100 lines. Reading it takes two minutes and is the single best control available to you.
2. Install only from `github.com/aman2139/girard-deal-skills`. Forks, mirrors, zip files sent to you by someone else, and anything on an npm or PyPI name resembling this one are not ours.
3. Prefer a tagged release over `main` if you want a fixed, reviewable version.
4. Run `python3 scripts/validate_skills.py` after any edit. It checks frontmatter, naming, and that every referenced file exists.

## Handling sensitive documents

These skills are designed for contracts, questionnaires, and internal pricing records. Before you feed those to any assistant:

- Confirm your organisation's data terms with your AI provider cover the document class you are about to upload. Enterprise and business agreements usually differ from consumer ones on retention and training.
- Redact what you do not need. A redline triage does not require the buyer's legal entity details to be useful.
- Treat the output as a draft. Every skill in this pack states this in its own instructions, and two of them route their highest-severity findings to a lawyer.
- Nothing here is a substitute for legal, security, or compliance review, and nothing here is a certification of anything.

## Reporting a vulnerability

Report privately. Do not open a public issue for anything in the first table below.

| Report it | Examples |
| --- | --- |
| Instructions that would cause an assistant to exfiltrate, transmit, or leak the documents a user attaches | A skill file amended to include a URL, an email address, or a callback instruction |
| Injected or hidden content in any file | Text hidden in a reference file, an instruction embedded in the banner SVG, a commit that adds a directive nobody reviewed |
| Anything in `scripts/` that touches the network, writes outside the repository, or executes unexpected code | A modified `package.sh`, a dependency introduced into the validator |
| A repository, package, or domain impersonating this pack | Typosquatted repo names, a lookalike "official" download |
| Supply-chain compromise of this repository | Unexpected commits, a release you cannot attribute, an unexplained collaborator |

**How to report**

- Preferred: GitHub private vulnerability reporting, under the Security tab of this repository.
- Alternative: the contact form at https://usegirard.com/contact, with "security" in the subject.

**What to include:** the file and line, what an assistant or script would do as a result, and how you found it. A proof of concept helps but is not required.

**What to expect:** acknowledgement within 5 business days. This is a small team, so that is a commitment we can actually keep rather than a number that looks good. We will tell you what we plan to do and when, and we will credit you in the fix commit unless you prefer otherwise. There is no bug bounty.

**Disclosure:** please give us 30 days before publishing. If we have not responded in that window, publish. A repository that ignores a reporter deserves the disclosure.

## Out of scope

Report these elsewhere, or not at all:

| Not a vulnerability here | Where it goes |
| --- | --- |
| The assistant produced a wrong, incomplete, or badly formatted answer | A normal issue or pull request in this repository |
| A clause position in `clause-risk-map.md` does not match your market | A normal issue. These are market reference points, not legal advice, and they are meant to be argued with |
| A skill did not trigger when you expected it to | See the troubleshooting section of INSTALL.md |
| A flaw in Claude, another model, or an assistant product | The vendor of that product |
| Security of the Girard product at usegirard.com | https://usegirard.com/contact. It is a separate system with a separate reporting path. This repository is not part of it |

## Repository controls

Current state, so you can check it against what you see:

- No GitHub Actions workflows. Nothing in this repository runs automatically on a commit, a pull request, or a fork.
- No dependencies. Nothing to install, nothing to resolve, no lockfile, no transitive supply chain.
- No secrets, tokens, or credentials are stored here, and none are required to use anything in it.

If you find any of the above to be untrue, that is itself a finding. Report it.
