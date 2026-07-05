# Investment Research Agent PRD

**Status**: Draft  
**Last updated**: 2026-07-05  
**Owner**: Personal project

## 1. Product Positioning

Investment Research Agent is a personal research operating system for turning public information, financial data, and self-collected field research into evidence-backed investment memos.

The product should help answer:

- What changed for a company, industry, or theme?
- Which evidence supports or weakens an existing investment thesis?
- What still needs to be verified?
- What should be remembered for the next decision cycle?

It should not behave like an auto-trading bot or a black-box stock picker. The core output is decision support with traceable evidence.

## 2. Primary User

The initial user is one individual investor / researcher.

Expected behavior:

- tracks a focused watchlist of companies, industries, and themes
- collects public information daily or weekly
- adds private notes from interviews, calls, meetings, and scattered observations
- wants periodic synthesis before making or revising investment decisions

## 3. Core Research Objects

The product should be organized around these objects:

- **Watchlist**: companies, industries, themes, and tickers under active tracking
- **Source**: news, filings, earnings calls, research reports, datasets, websites, interviews, notes
- **Evidence**: one extracted fact, claim, metric, quote, risk, or catalyst with source attribution
- **Thesis**: a structured investment hypothesis with supporting and opposing evidence
- **Question**: an unresolved issue that should guide future research
- **Memo**: a periodic or event-driven synthesis for human review
- **Decision log**: what changed, what was decided, and why

## 4. Product Decisions

The following decisions define the MVP direction:

- **Industry scope**: the system should be industry-neutral. AI can be used as the first test industry, but no core workflow or schema should depend on AI-specific categories.
- **Asset scope**: the MVP focuses on public equities. Important private firms inside a tracked industry can be followed as context, but they should remain lighter-weight unless they become IPO candidates or materially affect public-company theses.
- **Financial data**: financial and market data should come from APIs rather than manual entry as the default path. Manual entry can exist as a fallback for early testing or niche metrics.
- **First memo format**: start with weekly briefs. This keeps the first product loop useful without requiring heavy historical tracking from day one.
- **Privacy posture**: default to local-first storage for personal notes, interviews, and investment judgments. External LLM/API calls should be explicit and designed so sensitive material can be redacted or summarized before leaving the local environment.

## 5. Information Inputs

MVP inputs:

- URLs and RSS feeds
- pasted text notes
- PDFs and screenshots
- company filings and earnings materials
- interview / call notes
- financial and market data from APIs
- manually entered financial metrics as fallback

Later inputs:

- transcript APIs
- structured industry datasets
- broker / portfolio exports
- vector search over historical notes and memos

## 6. Core Workflows

### 6.1 Set Research Scope

The user creates a watchlist:

- company or asset
- ticker if available
- industry / theme
- current thesis
- key metrics to monitor
- important sources

### 6.2 Collect Information

The system collects and stores raw material:

- source metadata
- original text or file reference
- publication date
- fetched / ingested date
- linked company, industry, theme, or thesis when known

### 6.3 Extract Evidence

The agent converts raw material into structured evidence:

- fact / claim
- financial metric
- risk
- catalyst
- management commentary
- customer / channel signal
- competitor movement
- confidence and source quality
- citation back to original material

### 6.4 Update Thesis View

The agent compares new evidence against active theses:

- strengthens thesis
- weakens thesis
- contradicts thesis
- neutral but worth tracking
- opens a new research question

### 6.5 Produce Memos

The product should generate:

- weekly change brief
- company update memo
- industry / theme memo
- earnings or filing memo
- thesis review memo
- decision memo

Each memo must preserve citations and separate facts from interpretation.

## 7. MVP Scope

The first build should include:

- local Docker backend
- frontend research workspace shell
- watchlist CRUD
- manual information ingestion
- financial data API integration
- PDF / screenshot text extraction
- evidence extraction with citations
- simple thesis objects
- weekly brief generation
- decision log

The MVP can defer:

- automated trading integration
- complex portfolio analytics
- multi-user permissions
- mobile UI
- full knowledge graph visualization
- heavy private-company data modeling
- deep historical performance attribution

## 8. Product Principles

- Evidence first: every important claim needs a source.
- Human final judgment: the agent assists, but does not decide.
- Separate fact, inference, and action.
- Prefer fewer high-quality signals over noisy coverage.
- Preserve raw material for later re-interpretation.
- Make changes to a thesis explicit over time.
- Keep industry logic configurable, not hard-coded.
- Treat private notes and investment judgments as sensitive by default.

## 9. Privacy And Local-First Behavior

Local-only privacy means sensitive research material is stored and processed on infrastructure the user controls, rather than being silently synced to a third-party application backend.

For this product, the practical rule is:

- raw interview notes, personal judgments, and decision logs stay local-first
- API calls for financial data are expected and acceptable
- LLM calls are allowed, but should be explicit, logged, and designed for redaction when needed
- public information can be fetched from the internet and stored locally with source attribution

This does not mean the product can never use cloud services. It means the default architecture should not require personal research notes to live in a third-party backend before the user chooses that tradeoff.

## 10. Remaining Product Questions

- Which financial data API should be used first?
- Should the first watchlist use AI public equities as the test set?
- What exact fields should a weekly brief contain?
- How much interview-note processing should happen in the MVP?

## 11. Suggested Next Step

Agree on the MVP research loop before designing database tables:

```text
watchlist -> raw material -> evidence -> thesis impact -> memo -> decision log
```
