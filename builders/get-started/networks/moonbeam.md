---
title: Get Started with Moonbeam
description: Learn how to connect to Moonbeam via RPC and WSS endpoints, how to connect MetaMask to Moonbeam, and about the available Moonbeam block explorers.
categories:
- Basics
url: https://docs.moonbeam.network/builders/get-started/networks/moonbeam/
word_count: 515
token_estimate: 1289
version_hash: sha256:4e7af2709d28065781d1440d94d3b544478eb64f3dead122c919b40cac13944c
last_updated: '2026-05-21T21:21:53+00:00'
---

# Get Started with Moonbeam

## Network Endpoints {: #network-endpoints }

Moonbeam has two types of endpoints available for users to connect to: one for HTTPS and one for WSS.

If you're looking for your own endpoints suitable for production use, you can check out the [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/#endpoint-providers) section of our documentation. Otherwise, to get started quickly you can use one of the following public HTTPS or WSS endpoints:

=== "HTTPS"
    |      Provider       |                            RPC URL                             |   Limits    |
    |:-------------------:|:--------------------------------------------------------------:|:-----------:|
    |        1RPC         |             <pre>```https://1rpc.io/glmr```</pre>              | 10k req/day |
    | Moonbeam Foundation |       <pre>```https://rpc.api.moonbeam.network```</pre>        | 25 req/sec  |
    |     OnFinality      |   <pre>```https://moonbeam.api.onfinality.io/public```</pre>   | 40 req/sec  |
    |     UnitedBloc      |        <pre>```https://moonbeam.unitedbloc.com```</pre>        | 32 req/sec  |



=== "WSS"
    |      Provider       |                           RPC URL                            |   Limits    |
    |:-------------------:|:------------------------------------------------------------:|:-----------:|
    |        1RPC         |            <pre>```wss://1rpc.io/glmr```</pre>               | 10k req/day |
    | Moonbeam Foundation |      <pre>```wss://wss.api.moonbeam.network```</pre>         | 25 req/sec  |
    |     OnFinality      | <pre>```wss://moonbeam.api.onfinality.io/public-ws```</pre>  | 40 req/sec  |
    |     UnitedBloc      |       <pre>```wss://moonbeam.unitedbloc.com```</pre>         | 32 req/sec  |

## Quick Start {: #quick-start }

Before getting started, make sure you've retrieved your own endpoint and API key from one of the custom [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/). For the [Ethers.js library](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/), define the provider by using `ethers.JsonRpcProvider(providerURL, {object})` and setting the provider URL to Moonbeam:

```js
const ethers = require('ethers'); // Load Ethers library

const providerURL = 'INSERT_RPC_API_ENDPOINT'; // Insert your RPC URL here

// Define provider
const provider = new ethers.JsonRpcProvider(providerURL, {
    chainId: 1284,
    name: 'moonbeam'
});
```

Any Ethereum wallet should be able to generate a valid address for Moonbeam (for example, [MetaMask](https://metamask.io)).

## Chain ID {: #chain-id }

Moonbeam chain ID is: `1284`, or `0x504` in hex.
## Block Explorers {: #block-explorers }

For Moonbeam, you can use any of the following block explorers:

 - **Ethereum API (Etherscan Equivalent)** — [Moonscan](https://moonbeam.moonscan.io)
 - **Ethereum API JSON-RPC based** — [Moonbeam Basic Explorer](https://moonbeam-explorer.netlify.app/?network=Moonbeam)
 - **Substrate API** — [Subscan](https://moonbeam.subscan.io) or [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbeam.network#/explorer)

For more information on each of the available block explorers, please head to the [Block Explorers](/moonbeam-mkdocs/builders/get-started/explorers/) section of the documentation.

## Connect MetaMask {: #connect-metamask }

If you already have MetaMask installed, you can easily connect MetaMask to Moonbeam:

<div class="button-wrapper">
    <a href="#" class="md-button connectMetaMask" value="moonbeam">Connect MetaMask</a>
</div>

!!! note
    MetaMask will popup asking for permission to add Moonbeam as a custom network. Once you approve permissions, MetaMask will switch your current network to Moonbeam.

If you do not have MetaMask installed, or would like to follow a tutorial to get started, please check out the [Interacting with Moonbeam using MetaMask](/moonbeam-mkdocs/tokens/connect/metamask/) guide.

## Configuration {: #configuration }

Please note the following gas configuration parameters. These values are subject to change in future runtime upgrades.


|       Variable        |                   Value                    |
|:---------------------:|:------------------------------------------:|
|   Minimum gas price   | 31.25 Gwei |
|   Target block time   | 6 seconds |
|    Block gas limit    |     60,000,000      |
| Transaction gas limit |       52,000,000       |
