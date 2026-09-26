# Product plan

## ICP and JTBD

**ICP:** U.S. first-time engagement-ring buyers, 25–40, buying a lab-grown stone online or from an independent jeweler within two weeks.
**JTBD:** “When I have a quote but cannot tell whether it is fair or verifiable, help me understand the evidence and questions before I commit thousands of dollars.”

## MVP

1. Structured ring and quote intake.
2. Transparent comparison band with assumptions.
3. Certificate, inscription, return-policy, and price-risk flags.
4. Copyable dealer-question brief.
5. Optional paid 24-hour human review after validation.

This prototype ships the first four as a deterministic demo. It does not authenticate stones, scrape live prices, or provide financial/appraisal advice.

## Data model

- `Quote`: shape, carat, setting, amount, issuer, report number, timestamp.
- `Benchmark`: shape, carat bucket, low/high wholesale proxy, provenance, observed date.
- `Audit`: verdict, comparison band, assumptions, flags, questions, engine version.
- `Evidence` (future): report lookup, inscription photo, invoice, return policy, reviewer.
- `Outcome` (future): negotiated amount, purchase/refund, buyer confidence, dealer response.

## Architecture and model strategy

The Next.js static client runs the same explainable fixture math used by the FastAPI domain operation. The backend validates inputs and returns an audit contract; it is runnable locally and tested in CI, but not deployed. Production would centralize versioned benchmarks and immutable audit provenance. AI may extract quote PDFs and summarize policies later, but never invent a price or verification claim. Every extracted field requires source highlighting and human confirmation.

## Economics

- Wedge price: $49 per 24-hour audit.
- Early target: <$15 acquisition cost from high-intent search/community partnerships; <$12 reviewer labor using structured intake; >45% gross margin before support.
- Upsells: $99 document + live review; $199 local independent inspection coordination.
- Kill criteria: fewer than 15% of qualified quote-holders pay $49, refund rate above 10%, or median demonstrated savings/confidence lift fails to justify the fee.

## Validation

1. Observe eight current workflows.
2. Sell 20 manual audits before building live price ingestion.
3. Measure quote-to-purchase time, negotiated dollars, refunds, and unaided task completion.
4. Compare $29/$49/$79 pricing with identical service quality.
5. Interview jewelers only after buyer willingness to pay is demonstrated.

## Moat

Generic calculators are copyable. The potential moat is a consented dataset connecting quote attributes, verified evidence, dealer responses, negotiated outcomes, and return events—plus a trusted independent-review network. Without outcome data, this is a feature, not a company.

## Risks

- Stale or biased benchmarks create false confidence.
- “Verification” may be misread as appraisal or authenticity certification.
- Fraudulent reports, edited PDFs, affiliate conflicts, and reviewer inconsistency.
- Jewelers bundle services that make raw price comparisons misleading.
- High-intent SEO can be expensive and community promotion can erode trust.

## 30 / 60 / 90 days

- **30:** 8 observations, 20 manual audits, explicit disclaimers, benchmark provenance, price test.
- **60:** 75 paid audits, dual-review QA, report-issuer integrations, outcome follow-up, refund policy.
- **90:** 200 audits, two independent jeweler partners, calibration dashboard, decide concierge business vs. verification network.
