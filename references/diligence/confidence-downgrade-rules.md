<!--
[INPUT]: 依赖证据台账中的缺失、二手、冲突、访问失败与门禁状态
[OUTPUT]: 对外提供 claim、模块、总体置信度和 verdict 的强制降级上限
[POS]: references/diligence 的审慎约束，阻止叙事强度超过证据强度
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Confidence Downgrade Rules

Use these rules whenever evidence is incomplete, externally unverifiable, second-hand, or contradicted. The goal is to stop a polished memo from producing an overconfident verdict.

## Principle

> A conclusion can only be as strong as the weakest P0 evidence gate that could reverse it.

Do not average away missing critical evidence. A long deck with many P2 details cannot compensate for a missing P0 transaction, team, PMF, or legal gate.

## Evidence status labels

| Label | Meaning | Allowed use |
|---|---|---|
| Verified | Confirmed by source documents, data room files, direct interviews, or credible independent sources | Can support high-confidence claims |
| Provided-material claim | Stated in deck/memo/teaser but not independently verified | Can support low-to-medium confidence only |
| Inference | Analyst conclusion from available facts | Must be labeled as inference |
| Unknown | Not provided or not found | Must create a gap or request |
| Contradicted | Evidence conflicts with the claim | Must downgrade and explain |

## Automatic caps

| Missing or weak evidence | Maximum confidence / verdict | Required next check |
|---|---|---|
| Identifiable company but no external research attempted | Cannot call DD complete | Run external research log |
| External research attempted but blocked/incomplete | Overall confidence max medium; affected claims max low-to-medium | Record blocked searches and next sources |
| Material claim depends on one blocked/paywalled database | Affected claim remains Unknown or max low | Use claim-specific fallback ladder; do not retry the same source repeatedly |
| Financing terms only in memo, no term sheet/cap table | Verdict max Need more evidence | Request transaction docs |
| Lead investor claim unverified | Financing quality max low-to-medium | Request allocation / lead confirmation |
| Founder role unverified | Team confidence max medium | Role confirmation / interview / filings |
| Demo absent | Product maturity max concept/prototype | Request demo access |
| Benchmark/eval absent for AI performance claim | Technical confidence max low | Request eval methodology and reproducible benchmark |
| Customer contracts or paid pilots absent | PMF cannot be claimed | Request contracts, usage, retention, references |
| Competitor research only lists names | Competition coverage incomplete | Build same-dimension competitor landscape |
| AI strategy lists features without status/adoption/economics | AI strategy coverage incomplete | Build dated AI inventory and request usage, packaging, cost, and customer-outcome evidence |
| Data rights unclear | Legal/data risk high | Request licenses, consents, provenance, DPA |
| Indirect SPV/secondary structure unclear | Proceed blocked | Request SPV docs and underlying rights |

## Verdict caps

### Proceed requires all of these

- No unresolved P0 gate that could reverse the recommendation.
- External research completed when possible.
- Transaction structure and investor rights understood.
- Product, market, and team evidence match the claimed stage.
- Major risks have explicit mitigation or are acceptable for the price.

### Watch when

- The thesis is interesting, but one or more P0 gates remain open.
- Company exists and direction is plausible, but transaction, PMF, product, or valuation evidence is insufficient.
- Evidence suggests a real asset, but timing or price is not yet investable.

### Need more evidence when

- The memo contains high-materiality claims without source documents.
- External research cannot confirm key facts.
- The next step is clearly a data-room request, founder call, customer call, or technical review.

### Pass when

- A confirmed deal-breaker exists.
- The thesis depends on a claim that is contradicted by credible evidence.
- The company cannot provide P0 materials for a claim central to the investment.
- VC-fit is structurally absent and no alternative capital path is acceptable.

## Language rules

Replace overconfident language:

| Avoid | Use instead |
|---|---|
| The company has raised... | The memo states the company has raised... |
| The lead investors are... | The materials identify ... as lead investors; this remains unverified until allocation/term documents are reviewed. |
| The product works | A demo/product is claimed; functionality remains unverified without demo/benchmark/customer evidence. |
| PMF is proven | Current evidence suggests demand, but PMF is not proven without retention, expansion, or repeat usage. |
| This is a platform | The company claims platform potential; platform economics depend on runtime ownership, developer/customer adoption, and data/control rights. |

## Final report requirement

Every final verdict must include:

```markdown
### 置信度与降级原因

- 当前置信度：high / medium / low
- 哪些 P0 证据已经满足：...
- 哪些 P0 证据缺失：...
- 因此结论被限制为：Proceed / Watch / Pass / Need more evidence
- 哪一份证据会改变结论：...
```
