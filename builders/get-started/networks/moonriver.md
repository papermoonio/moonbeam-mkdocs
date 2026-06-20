---
title: Moonriver Get Started Guide
description: Learn how to connect to Moonriver via RPC and WSS endpoints, how to connect MetaMask to Moonriver, and about the available Moonriver block explorers.
categories:
- Basics
url: https://docs.moonbeam.network/builders/get-started/networks/moonriver/
word_count: 498
token_estimate: 1236
version_hash: sha256:95ee64790a9b70ee7b7108cc681c7c9ca0cf5fbb429dec73c53966f1cb90fbd8
last_updated: '2026-05-21T21:21:53+00:00'
---

# Get Started with Moonriver

## Network Endpoints {: #network-endpoints }

Moonriver has two types of endpoints available for users to connect to: one for HTTPS and one for WSS.

If you're looking for your own endpoints suitable for production use, you can check out the [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/#endpoint-providers) section of our documentation. Otherwise, to get started quickly you can use one of the following public HTTPS or WSS endpoints:

=== "HTTPS"
    |      Provider       |                             RPC URL                             |   Limits    |
    |:-------------------:|:---------------------------------------------------------------:|:-----------:|
    | Moonbeam Foundation |   <pre>```https://rpc.api.moonriver.moonbeam.network```</pre>   | 25 req/sec  |
    |     OnFinality      |    <pre>```https://moonriver.api.onfinality.io/public```</pre>  | 40 req/sec  |
    |     UnitedBloc      |         <pre>```https://moonriver.unitedbloc.com```</pre>       | 32 req/sec  |

=== "WSS"
    |      Provider       |                            RPC URL                            |   Limits    |
    |:-------------------:|:-------------------------------------------------------------:|:-----------:|
    | Moonbeam Foundation |   <pre>```wss://wss.api.moonriver.moonbeam.network```</pre>   | 25 req/sec  |
    |     OnFinality      | <pre>```wss://moonriver.api.onfinality.io/public-ws```</pre>  | 40 req/sec  |
    |     UnitedBloc      |        <pre>```wss://moonriver.unitedbloc.com```</pre>        | 32 req/sec  |

## Quick Start {: #quick-start }

Before getting started, make sure you've retrieved your own endpoint and API key from one of the custom [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/). For the [Ethers.js library](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/), define the provider by using `ethers.JsonRpcProvider(providerURL, {object})` and setting the provider URL to Moonriver:

```js
const ethers = require('ethers'); // Load Ethers library

const providerURL = 'INSERT_RPC_API_ENDPOINT'; // Insert your RPC URL here

// Define provider
const provider = new ethers.JsonRpcProvider(providerURL, {
    chainId: 1285,
    name: 'moonriver'
});
```

Any Ethereum wallet should be able to generate a valid address for Moonbeam (for example, [MetaMask](https://metamask.io)).

## Chain ID {: #chain-id }

Moonriver chain ID is: `1285`, or `0x505` in hex.
## Block Explorers {: #block-explorers }

For Moonriver, you can use any of the following block explorers:

 - **Ethereum API (Etherscan Equivalent)** — [Moonscan](https://moonriver.moonscan.io)
 - **Ethereum API JSON-RPC based** — [Moonbeam Basic Explorer](https://moonbeam-explorer.netlify.app/?network=Moonriver)
 - **Substrate API** — [Subscan](https://moonriver.subscan.io) or [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonriver.moonbeam.network#/explorer)
 
For more information on each of the available block explorers, please head to the [Block Explorers](/moonbeam-mkdocs/builders/get-started/explorers/) section of the documentation.

## Connect MetaMask {: #connect-metamask }

If you already have MetaMask installed, you can easily connect MetaMask to Moonriver:

<div class="button-wrapper">
    <a href="#" class="md-button connectMetaMask" value="moonriver">Connect MetaMask</a>
</div>

!!! note
    MetaMask will popup asking for permission to add Moonriver as a custom network. Once you approve permissions, MetaMask will switch your current network to Moonriver.

If you do not have MetaMask installed, or would like to follow a tutorial to get started, please check out the [Interacting with Moonbeam using MetaMask](/moonbeam-mkdocs/tokens/connect/metamask/) guide.

## Configuration {: #configuration }

Please note the following gas configuration parameters. These values are subject to change in future runtime upgrades.

|       Variable        |                    Value                    |
|:---------------------:|:-------------------------------------------:|
|   Minimum gas price   | 0.3125 Gwei |
|   Target block time   | 6 seconds |
|    Block gas limit    |     60,000,000      |
| Transaction gas limit |       52,000,000       |
