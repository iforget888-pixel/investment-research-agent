# MVP Implementation Plan

**Status**: Draft  
**Last updated**: 2026-07-05

## First Vertical Slice

Build the smallest loop that can support real research:

```text
watchlist item -> raw material -> evidence -> weekly brief
```

The first implementation phase only creates the backend foundation and the first two resources:

- watchlist items
- raw materials

Evidence extraction and weekly brief generation come next, once storage and API boundaries are stable.

## Backend Boundary

The API should be boring and reliable:

- store watchlist scope
- store raw research material
- expose CRUD endpoints
- preserve source attribution
- keep local-first data ownership

The agent layer should be separate:

- fetch sources
- parse PDFs/screenshots
- extract evidence
- compare evidence to thesis
- generate weekly briefs
- record decisions

## Initial API Resources

### Watchlist Item

Tracks a public equity, private company context item, theme, or industry.

Initial fields:

- name
- asset_type
- ticker
- exchange
- industry
- theme
- status
- thesis
- key_metrics
- notes

### Raw Material

Stores one input artifact before interpretation.

Initial fields:

- watchlist_item_id
- material_type
- title
- source_name
- source_url
- content_text
- published_at
- status
- metadata_json

## Next Resources

### Evidence

One extracted claim, metric, risk, catalyst, quote, or observation with source citation.

### Thesis

One investment hypothesis tied to a watchlist item.

### Weekly Brief

The first memo format. It should summarize what changed this week and how it affects active theses.
