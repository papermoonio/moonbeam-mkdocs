---
title: AI Resources
description: Download LLM-optimized files of the Moonbeam documentation, including full content and category-specific resources for AI agents.
url: https://docs.moonbeam.network/ai-resources/
word_count: 1484
token_estimate: 3756
version_hash: sha256:36323d4f5b1af2acb2fa0ca809795b51992622b54850ad4d65ba1d2a889e9317
---

# AI Resources

Moonbeam provides files to make documentation content available in a structure optimized for use with large language models (LLMs) and AI tools. These resources help build AI assistants, power code search, or enable custom tooling trained on Moonbeam's documentation.

## Access LLM Files

- **Quick navigation**: Use `llms.txt` to give models a high-level map of the site.
- **Lightweight context**: Use `site-index.json` for smaller context windows or when you only need targeted retrieval.
- **Full content**: Use `llms-full.jsonl` for large-context models or preparing data for RAG pipelines.
- **Focused bundles**: Use category files (e.g., `basics.md`, `reference.md`) to limit content to a specific theme or task for more focused responses.

These AI-ready files do not include any persona or system prompts. They are purely informational and can be used without conflicting with your existing agent or tool prompting.

### Full Site Files

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`llms.txt`](https://docs.moonbeam.network/llms.txt) | Markdown URL index for documentation pages, links to essential repos, and additional resources in the llms.txt standard format. | 10,505 |
| [`site-index.json`](https://docs.moonbeam.network/ai/site-index.json) | Lightweight site index of JSON objects (one per page) with metadata and content previews. | 76,334 |
| [`llms-full.jsonl`](https://docs.moonbeam.network/ai/llms-full.jsonl) | Full content of documentation site enhanced with metadata. | 784,674 |

> The `llms-full.jsonl` file may exceed the input limits of some language models due to its size. If you encounter limitations, consider using the smaller `site-index.json` or category bundle files instead.

### Category Files

#### Basics

Moonbeam's framework, architecture, and core components.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`basics.md`](https://docs.moonbeam.network/ai/categories/basics.md) | Full bundle — complete page content for all tagged pages. | 83,384 |
| [`basics-light.md`](https://docs.moonbeam.network/ai/categories/basics-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 6,449 |

#### Ethereum Toolkit

Useful tools and smart contracts to work with Moonbeam's EVM.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`ethereum-toolkit.md`](https://docs.moonbeam.network/ai/categories/ethereum-toolkit.md) | Full bundle — complete page content for all tagged pages. | 321,398 |
| [`ethereum-toolkit-light.md`](https://docs.moonbeam.network/ai/categories/ethereum-toolkit-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 12,443 |

#### Substrate Toolkit

Useful tools and smart contracts to work with Substrate.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`substrate-toolkit.md`](https://docs.moonbeam.network/ai/categories/substrate-toolkit.md) | Full bundle — complete page content for all tagged pages. | 167,109 |
| [`substrate-toolkit-light.md`](https://docs.moonbeam.network/ai/categories/substrate-toolkit-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 1,888 |

#### GMP Providers

How to use General Message Passing (GMP) for cross-chain communication.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`gmp-providers.md`](https://docs.moonbeam.network/ai/categories/gmp-providers.md) | Full bundle — complete page content for all tagged pages. | 158,216 |
| [`gmp-providers-light.md`](https://docs.moonbeam.network/ai/categories/gmp-providers-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 719 |

#### XCM

Learn about and use Cross-Consensus Messaging (XCM).

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`xcm.md`](https://docs.moonbeam.network/ai/categories/xcm.md) | Full bundle — complete page content for all tagged pages. | 193,173 |
| [`xcm-light.md`](https://docs.moonbeam.network/ai/categories/xcm-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 4,246 |

#### XC-20

Guides for interacting with XC-20 tokens.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`xc-20.md`](https://docs.moonbeam.network/ai/categories/xc-20.md) | Full bundle — complete page content for all tagged pages. | 169,131 |
| [`xc-20-light.md`](https://docs.moonbeam.network/ai/categories/xc-20-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 2,279 |

#### XCM Remote Execution

How to make cross-chain calls with XCM.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`xcm-remote-execution.md`](https://docs.moonbeam.network/ai/categories/xcm-remote-execution.md) | Full bundle — complete page content for all tagged pages. | 180,005 |
| [`xcm-remote-execution-light.md`](https://docs.moonbeam.network/ai/categories/xcm-remote-execution-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 1,508 |

#### Precompiles

Guides to using Moonbeam's precompiles.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`precompiles.md`](https://docs.moonbeam.network/ai/categories/precompiles.md) | Full bundle — complete page content for all tagged pages. | 235,027 |
| [`precompiles-light.md`](https://docs.moonbeam.network/ai/categories/precompiles-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 6,393 |

#### Libraries and SDKs

Resources for commonly used libraries and SDKs.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`libraries-and-sdks.md`](https://docs.moonbeam.network/ai/categories/libraries-and-sdks.md) | Full bundle — complete page content for all tagged pages. | 185,655 |
| [`libraries-and-sdks-light.md`](https://docs.moonbeam.network/ai/categories/libraries-and-sdks-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 2,798 |

#### Dev Environments

How to set up developer environments such as Hardhat and Foundry.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`dev-environments.md`](https://docs.moonbeam.network/ai/categories/dev-environments.md) | Full bundle — complete page content for all tagged pages. | 175,908 |
| [`dev-environments-light.md`](https://docs.moonbeam.network/ai/categories/dev-environments-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 1,529 |

#### JSON-RPC APIs

RPC usage and tracing.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`json-rpc-apis.md`](https://docs.moonbeam.network/ai/categories/json-rpc-apis.md) | Full bundle — complete page content for all tagged pages. | 156,804 |
| [`json-rpc-apis-light.md`](https://docs.moonbeam.network/ai/categories/json-rpc-apis-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 1,124 |

#### Node Operators and Collators

How to run a full node or a block-producing collator.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`node-operators-and-collators.md`](https://docs.moonbeam.network/ai/categories/node-operators-and-collators.md) | Full bundle — complete page content for all tagged pages. | 189,665 |
| [`node-operators-and-collators-light.md`](https://docs.moonbeam.network/ai/categories/node-operators-and-collators-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 3,644 |

#### Oracle Nodes

How to integrate with oracle node providers.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`oracle-nodes.md`](https://docs.moonbeam.network/ai/categories/oracle-nodes.md) | Full bundle — complete page content for all tagged pages. | 152,465 |
| [`oracle-nodes-light.md`](https://docs.moonbeam.network/ai/categories/oracle-nodes-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 514 |

#### Indexers and Queries

How to integrate with indexer and query node providers.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`indexers-and-queries.md`](https://docs.moonbeam.network/ai/categories/indexers-and-queries.md) | Full bundle — complete page content for all tagged pages. | 159,648 |
| [`indexers-and-queries-light.md`](https://docs.moonbeam.network/ai/categories/indexers-and-queries-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 828 |

#### Tokens and Accounts

How to manage tokens and accounts on Moonbeam.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`tokens-and-accounts.md`](https://docs.moonbeam.network/ai/categories/tokens-and-accounts.md) | Full bundle — complete page content for all tagged pages. | 184,518 |
| [`tokens-and-accounts-light.md`](https://docs.moonbeam.network/ai/categories/tokens-and-accounts-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 3,519 |

#### Staking

Guides to delegate and collate.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`staking.md`](https://docs.moonbeam.network/ai/categories/staking.md) | Full bundle — complete page content for all tagged pages. | 153,125 |
| [`staking-light.md`](https://docs.moonbeam.network/ai/categories/staking-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 1,034 |

#### Governance

Guides to governance including voting and treasury.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`governance.md`](https://docs.moonbeam.network/ai/categories/governance.md) | Full bundle — complete page content for all tagged pages. | 156,622 |
| [`governance-light.md`](https://docs.moonbeam.network/ai/categories/governance-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 1,166 |

#### Integrations

Guides to integrating Moonbeam with various tools such as wallets and analytics.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`integrations.md`](https://docs.moonbeam.network/ai/categories/integrations.md) | Full bundle — complete page content for all tagged pages. | 155,232 |
| [`integrations-light.md`](https://docs.moonbeam.network/ai/categories/integrations-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 565 |

#### Tutorials

Comprehensive, step-by-step, guided project builds.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`tutorials.md`](https://docs.moonbeam.network/ai/categories/tutorials.md) | Full bundle — complete page content for all tagged pages. | 152,605 |
| [`tutorials-light.md`](https://docs.moonbeam.network/ai/categories/tutorials-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 323 |

#### Reference

Reference material including network endpoints, JSON-RPC methods, and contract or token addresses.

| File | Description | Token Estimate |
|------|-------------|----------------|
| [`reference.md`](https://docs.moonbeam.network/ai/categories/reference.md) | Full bundle — complete page content for all tagged pages. | 70,726 |
| [`reference-light.md`](https://docs.moonbeam.network/ai/categories/reference-light.md) | Lightweight index — titles, URLs, previews, and section headings. | 2,425 |
