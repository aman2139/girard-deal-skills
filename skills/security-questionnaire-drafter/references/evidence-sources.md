# Evidence source map

Which document normally answers which cluster of questions. Use this to group unanswered questions by the single document that would close them, so the user makes one request per owner instead of one per question.

| Question theme | Primary source | Secondary source | Usual owner |
| --- | --- | --- | --- |
| Access control, MFA, least privilege, offboarding | Access control policy | SOC 2 CC6 controls | Head of engineering or IT |
| Encryption at rest and in transit | Security policy, architecture diagram | Cloud provider config, SOC 2 CC6.7 | Engineering |
| Data retention and deletion | Data retention policy, DPA | Privacy policy | Legal or engineering |
| Subprocessors and fourth parties | Subprocessor list, DPA annex | Vendor register | Legal or ops |
| Incident response and breach notification | IR plan, DPA notification clause | SOC 2 CC7 | Engineering or legal |
| Business continuity and disaster recovery | BCDR plan, RTO/RPO targets | Cloud architecture doc | Engineering |
| Secure development lifecycle, code review | SDLC policy, PR and branch rules | SOC 2 CC8 | Engineering |
| Vulnerability management, pen testing | Pen test summary, scanning cadence doc | SOC 2 CC7.1 | Engineering or security |
| Personnel, background checks, training | HR policy, security awareness records | SOC 2 CC1 | People or ops |
| Physical security | Cloud provider attestation for remote-first companies | Office policy | Ops |
| Privacy, GDPR, CCPA, cross-border transfers | Privacy policy, DPA, SCCs | Records of processing | Legal |
| Insurance, financials, corporate | Certificate of insurance, cap table summary | Finance records | Finance or founder |
| AI, model training, model data handling | AI usage policy, subprocessor list, model provider terms | Product documentation | Engineering and legal |

## Notes on common traps

- **Remote-first companies and physical security.** Most physical questions are answered by the cloud provider's attestation plus a statement about device management. Answering them as though the company runs a data center produces obvious falsehoods.
- **SOC 2 in progress.** "Type II audit underway, report expected [date], Type I available now" is a real answer. "SOC 2 compliant" is not, unless a report exists.
- **Subprocessor questions.** These recur on every deal and are the most common source of a late-stage contract amendment. If no maintained subprocessor list exists, that is a permanent gap worth naming in the review brief.
- **AI questions.** Buyers increasingly ask whether their data trains models, whether output is retained by the model provider, and whether subprocessors include model vendors. Answer from the model provider's actual terms, not from general belief about how such tools work.
