# Install and use

Six skills. Install all of them or just the one you need. Nothing to configure, nothing to run, no API key.

## Claude Code

Skills live in `.claude/skills/` inside a project, or `~/.claude/skills/` to make them available everywhere.

```bash
git clone https://github.com/aman2139/girard-deal-skills.git
cd girard-deal-skills

# this project only
mkdir -p /path/to/your/project/.claude/skills
cp -r skills/* /path/to/your/project/.claude/skills/

# or every project on this machine
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

Confirm they loaded with `/skills`.

## Claude desktop and web

1. Download this repository as a ZIP, or run `bash scripts/package.sh` to build one zip per skill in `dist/`.
2. Open Settings, then Capabilities, then Skills.
3. Upload the skill folder or its zip. Repeat for each skill you want.

Skills upload one at a time, so start with the one matching the deal you are stuck on. `security-questionnaire-drafter` and `redline-triage` are where most people start.

## Claude Projects

Add a skill to a project and everyone with access gets the same behaviour. Useful for a sales team, because consistent output is most of the value: reviewers learn where to look.

## Using them

Ask in plain English. The right skill picks itself up from what you say.

| What you say | What runs |
| --- | --- |
| "Here's the SIG Lite from [buyer], draft what you can from our SOC 2 and policies" | security-questionnaire-drafter |
| "Their counsel sent this back, what should we push on?" | redline-triage |
| "Pull our actual discount policy out of these Slack exports" | deal-decisions-one-pager |
| "Customer wants EEA-only hosting, I need to ask engineering" | objection-to-internal-ask |
| "Need the CEO to approve 22% on a two-year prepay" | escalation-drafter |
| "We sign Thursday, what's missing?" | late-stage-gap-finder |

Attach the relevant documents. These skills read what you give them and nothing else, which is the point.

### If a skill does not trigger

Name it: "use the redline-triage skill on this". Skills trigger on the description, and a very short prompt sometimes gets handled directly instead.

### What to attach

| Skill | Attach |
| --- | --- |
| security-questionnaire-drafter | The questionnaire, plus SOC 2 or ISO report, security and privacy policies, subprocessor list, any past completed questionnaire |
| redline-triage | The redlined document, plus your standard terms or a prior signed agreement |
| deal-decisions-one-pager | Slack or email exports, closed contracts, pricing pages, CRM notes. More is better here |
| objection-to-internal-ask | The buyer's message, plus deal value, stage, close date, and who does what on your team |
| escalation-drafter | The exception being requested, deal facts, the approver's name, and what happens if they say no |
| late-stage-gap-finder | Everything in the signature package: MSA, order form, DPA, SLA, SOW, and the proposal you sent earlier |

## Privacy

These skills are text instructions. They send nothing anywhere, store nothing, and call no external service. Whatever you attach goes to Claude under whatever data terms you already have with Anthropic, and nowhere else. Girard receives nothing.

## Modifying them

Every skill is a plain markdown file. Change the output template, add your own clause positions, put your company's actual discount bands into the reference files. That is the intended use.

After editing:

```bash
python3 scripts/validate_skills.py
```

It checks frontmatter, name and description limits, and that referenced files exist. Exit code 0 means every skill is valid.

## Troubleshooting

**The skill answered without reading my attachment.** Say the filename in the prompt.

**The output missed a section from the template.** Ask for the missing section by name. If it recurs, open an issue with the prompt you used.

**It refused to answer a questionnaire question.** That is designed behaviour. It marks a question unanswered when no supplied document covers it, rather than writing a plausible security claim. Supply the source document, or route the question to the owner it names.
