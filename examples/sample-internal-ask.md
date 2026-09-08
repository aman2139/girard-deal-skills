# Fixture: buyer objection forwarded inward

Synthetic input used to verify `objection-to-internal-ask`. Deal context supplied with the fixture: $84,000 ACV, security review stage, buyer is a 4,000 person insurer, signature targeted in 9 days. Team list supplied: Sanjit (engineering), Aman (GTM), no legal on staff.

Buyer email, from the buyer's InfoSec reviewer to the AE:

> Thanks for the questionnaire responses. Two items are blocking sign-off from our side. First, our data protection standard requires that all customer data remain within the EEA. Your response indicates US-East hosting. Second, our vendor policy requires notification of a security incident within 24 hours, and your DPA specifies 72. Our legal team will not sign with 72.
>
> I should mention we are also evaluating an alternative that already meets both requirements. I need a written response by Friday to keep you in this cycle. Happy to jump on a call if that's easier.

---

# Output (185 words)

**Ask:** Decide whether we commit to EEA-only hosting and 24 hour breach notification for this account, or hold.
**Owner:** Sanjit
**Needed by:** Thursday, so a written answer goes back Friday. Missing Friday drops us from the evaluation cycle, not just the date.

**Context:** $84K insurer, in security review, signature targeted in 9 days. Their InfoSec reviewer says two things block sign-off: EEA-only residency (we answered US-East) and a 24 hour breach notification window (our DPA says 72). They name a competitor that meets both.

**Options**

1. Commit to both. Unblocks the deal. Costs an EU deployment we have not built plus a weekend-capable notification path. No precedent found.
2. Commit to 24 hours, offer EEA hosting as a dated commitment with a contractual backstop. Tests whether residency is policy or default.
3. Hold at 72 and US-East. Likely loses this cycle.

**Recommendation:** Option 2. One operational change instead of an infrastructure build, and it surfaces which requirement is real before we spend anything.

**If we do nothing:** No written response by Friday and we are out. The $84K moves to next fiscal year at best.

---

Note: the first run of this test came back at 251 words. The skill now states the one-line-per-option constraint explicitly and permits cutting to two options, which brings a realistic three-option case inside the limit.
