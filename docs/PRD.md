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

## 4. Information Inputs

MVP inputs:

- URLs and RSS feeds
- pasted text notes
- PDFs and screenshots
- company filings and earnings materials
- interview / call notes
- manually entered financial metrics

Later inputs:

- market data APIs
- transcript APIs
- structured industry datasets
- broker / portfolio exports
- vector search over historical notes and memos

## 5. Core Workflows

### 5.1 Set Research Scope

The user creates a watchlist:

- company or asset
- ticker if available
- industry / theme
- current thesis
- key metrics to monitor
- important sources

### 5.2 Collect Information

The system collects and stores raw material:

- source metadata
- original text or file reference
- publication date
- fetched / ingested date
- linked company, industry, theme, or thesis when known

### 5.3 Extract Evidence

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

### 5.4 Update Thesis View

The agent compares new evidence against active theses:

- strengthens thesis
- weakens thesis
- contradicts thesis
- neutral but worth tracking
- opens a new research question

### 5.5 Produce Memos

The product should generate:

- daily or weekly change brief
- company update memo
- industry / theme memo
- earnings or filing memo
- thesis review memo
- decision memo

Each memo must preserve citations and separate facts from interpretation.

## 6. MVP Scope

The first build should include:

- local Docker backend
- frontend research workspace shell
- watchlist CRUD
- manual information ingestion
- PDF / screenshot text extraction
- evidence extraction with citations
- simple thesis objects
- weekly brief generation
- decision log

The MVP can defer:

- automated trading integration
- complex portfolio analytics
- paid market-data integrations
- multi-user permissions
- mobile UI
- full knowledge graph visualization

## 7. Product Principles

- Evidence first: every important claim needs a source.
- Human final judgment: the agent assists, but does not decide.
- Separate fact, inference, and action.
- Prefer fewer high-quality signals over noisy coverage.
- Preserve raw material for later re-interpretation.
- Make changes to a thesis explicit over time.

## 8. Open Product Questions

- Is the first domain still AI companies, or should the system be industry-neutral from day one?
- Should the MVP focus on public equities only, or include private companies and themes?
- Should financial data be manually entered first, or connected to APIs early?
- What is the first memo format: weekly brief, company memo, or decision memo?
- How much local-only privacy is required for interview notes and personal research?

## 9. Suggested Next Step

Agree on the MVP research loop before designing database tables:

```text
watchlist -> raw material -> evidence -> thesis impact -> memo -> decision log
```
