---
title: Moonbase Alpha Get Started Guide
description: The Moonbeam TestNet, named Moonbase Alpha, is the easiest way to get started with a Polkadot environment. Follow this tutorial to connect to the TestNet.
categories:
- Basics
url: https://docs.moonbeam.network/builders/get-started/networks/moonbase/
word_count: 1126
token_estimate: 2646
version_hash: sha256:ad7156ef1be674ea5bdf029fc4c69479dc28442adde49afdd54b43adfecc2711
last_updated: '2026-05-21T21:21:53+00:00'
---

# Get Started with Moonbase Alpha

## Network Endpoints {: #network-endpoints }

Moonbase Alpha has two types of endpoints available for users to connect to: one for HTTPS and one for WSS.

If you're looking for your own endpoints suitable for production use, you can check out the [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/#endpoint-providers) section of our documentation. Otherwise, to get started quickly you can use one of the following public HTTPS or WSS endpoints.

=== "HTTPS"
    |      Provider       |                              RPC URL                               |   Limits    |
    |:-------------------:|:------------------------------------------------------------------:|:-----------:|
    | Moonbeam Foundation |     <pre>```https://rpc.api.moonbase.moonbeam.network```</pre>     | 25 req/sec  |
    |     OnFinality      |  <pre>```https://moonbeam-alpha.api.onfinality.io/public```</pre>  | 40 req/sec  |
    |     UnitedBloc      |          <pre>```https://moonbase.unitedbloc.com```</pre>          | 32 req/sec  |

=== "WSS"
    |      Provider       |                              RPC URL                              |   Limits    |
    |:-------------------:|:-----------------------------------------------------------------:|:-----------:|
    | Moonbeam Foundation |     <pre>```wss://wss.api.moonbase.moonbeam.network```</pre>      | 25 req/sec  |
    |     OnFinality      | <pre>```wss://moonbeam-alpha.api.onfinality.io/public-ws```</pre> | 40 req/sec  |
    |     UnitedBloc      |          <pre>```wss://moonbase.unitedbloc.com```</pre>           | 32 req/sec  |


#### Relay Chain {: #relay-chain }

To connect to the Moonbase Alpha relay chain, you can use the following WS Endpoint:

| Provider |                          RPC URL                           |
|:--------:|:----------------------------------------------------------:|
| OpsLayer | <pre>```wss://relay.api.moonbase.moonbeam.network```</pre> |

## Quick Start {: #quick-start }

For the [Ethers.js library](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/), define the provider by using `ethers.JsonRpcProvider(providerURL, {object})` and setting the provider URL to Moonbase Alpha:

```js
const ethers = require('ethers'); // Load Ethers library

const providerURL = 'https://rpc.api.moonbase.moonbeam.network';
// Define provider
const provider = new ethers.JsonRpcProvider(providerURL, {
    chainId: 1287,
    name: 'moonbase-alphanet'
});
```

Any Ethereum wallet should be able to generate a valid address for Moonbeam (for example, [MetaMask](https://metamask.io)).

## Chain ID {: #chain-id }

Moonbase Alpha TestNet chain ID is: `1287`, which is `0x507` in hex.
## Block Explorers

For Moonbase Alpha, you can use any of the following block explorers:

 - **Ethereum API (Etherscan Equivalent)** — [Moonscan](https://moonbase.moonscan.io)
 - **Ethereum API JSON-RPC based** — [Moonbeam Basic Explorer](https://moonbeam-explorer.netlify.app/?network=MoonbaseAlpha)
 - **Substrate API** — [Subscan](https://moonbase.subscan.io) or [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#/explorer)

For more information on each of the available block explorers, please head to the [Block Explorers](/moonbeam-mkdocs/builders/get-started/explorers/) section of the documentation.

## Connect MetaMask

If you already have MetaMask installed, you can easily connect MetaMask to the Moonbase Alpha TestNet:

<div class="button-wrapper">
    <a href="#" class="md-button connectMetaMask" value="moonbase">Connect MetaMask</a>
</div>

!!! note
    MetaMask will popup asking for permission to add Moonbase Alpha as a custom network. Once you approve permissions, MetaMask will switch your current network to Moonbase Alpha.

If you do not have MetaMask installed, or would like to follow a tutorial to get started, please check out the [Interacting with Moonbeam using MetaMask](/moonbeam-mkdocs/tokens/connect/metamask/) guide.

## Configuration {: #configuration }

Please note the following gas configuration parameters. These values are subject to change in future runtime upgrades.

|       Variable        |                   Value                    |
|:---------------------:|:------------------------------------------:|
|   Minimum gas price   | 0.03125 Gwei |
|   Target block time   | 6 seconds |
|    Block gas limit    |     60,000,000      |
| Transaction gas limit |       52,000,000       |

## Get Tokens {: #get-tokens }

To start building on Moonbase Alpha, you can get DEV tokens from the Moonbase Alpha Faucet. For specific amounts, you can always reach out directly to us via our community channels.

To request DEV tokens from the faucet, you can enter your address on the [Moonbase Alpha Faucet](https://faucet.moonbeam.network) website. The faucet dispenses 1.1 DEV tokens every 24 hours.

![Moonbase Alpha Faucet Website.](/moonbeam-mkdocs/images/builders/get-started/networks/moonbase/moonbase-1.webp)

!!! note
    Moonbase Alpha DEV tokens have no value. Please don't spam the faucet with unnecessary requests.

## Demo DApps {: #Demo-DApps }

There are a variety of DApps deployed to Moonbase Alpha enabling you to experiment with various apps and integrations. You can also acquire a variety of test tokens through the [Moonbase ERC20 Minter](https://moonbase-minterc20.netlify.app). In the below table, you'll find each sample DApp, its associated URL, and GitHub repository.

### Quick Links {: #quick-links }

|                                            DApp                                            |    Description     |                                                                            Repository                                                                            |
|:------------------------------------------------------------------------------------------:|:------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|     [Moonbase ERC-20 Minter](https://moonbase-minterc20.netlify.app)      |   ERC-20 Faucet    |                 [https://github.com/papermoonio/moonbase-mintableERC20](https://github.com/papermoonio/moonbase-mintableERC20)                  |
| [Moonbeam WalletConnect](https://moonbeam-walletconnect-demo.netlify.app) | WalletConnect Demo |            [https://github.com/papermoonio/moonbeam-walletconnect-demo](https://github.com/papermoonio/moonbeam-walletconnect-demo)             |
|              [MoonGas](https://moonbeam-gasinfo.netlify.app)              | Gas Price Tracker  |                    [https://github.com/albertov19/moonbeam-gas-station](https://github.com/albertov19/moonbeam-gas-station)                     |

!!! note
    These DApps are intended for demonstration purposes only and may be incomplete or unsuitable for production deployments.

### Moonbase ERC20 Minter {: #moonbase-erc20-minter }

The [Moonbase ERC-20 Minter](https://moonbase-minterc20.netlify.app) enables you to mint a variety of ERC-20 test tokens corresponding to the 8 planets of the solar system, and Pluto. To mint tokens, first press **Connect MetaMask** in the upper right hand corner. Then scroll to the **Mint Tokens** section and the choose desired ERC-20 contract. Press **Submit Tx** and confirm the transaction in MetaMask. Each mint will grant you 100 tokens, and you can mint tokens for each contract once per hour.

![ERC20 Minter](/moonbeam-mkdocs/images/builders/get-started/networks/moonbase/moonbase-2.webp)

### Moonbeam WalletConnect {: #moonbeam-walletconnect }

[Moonbeam WalletConnect](https://moonbeam-walletconnect-demo.netlify.app) shows how easy it is to integrate [WalletConnect](https://walletconnect.com) into your DApps and unlock support for a great variety of crypto wallets. Be sure to check out the [demo app repository](https://github.com/papermoonio/moonbeam-walletconnect-demo) to see exactly how the WalletConnect integration works. To get started, you can take the following steps:

1. Press **Connect Wallet**
2. Scan the QR code using a [wallet compatible with WalletConnect](https://walletguide.walletconnect.network/)

![Moonbeam WalletConnect](/moonbeam-mkdocs/images/builders/get-started/networks/moonbase/moonbase-3.webp)

### MoonGas {: #moongas }

[MoonGas](https://moonbeam-gasinfo.netlify.app) is a convenient dashboard for viewing the minimum, maximum, and average gas price of transactions in the prior block across all Moonbeam networks. Note, these statistics can fluctuate widely by block and occasionally include outlier values. You can check out the [repository for MoonGas](https://github.com/albertov19/moonbeam-gas-station).

You'll notice that the minimum gas price for Moonbeam is 31.25 Gwei, while the minimum for Moonriver is 0.3125 Gwei and Moonbase Alpha is 0.03125 Gwei. This difference stems from the [100 to 1 re-denomination of GLMR](https://moonbeam.network/news/moonbeam-foundation-announces-liquidity-programs-a-new-token-event-and-glmr-redenomination) and thus the 31.25 Gwei minimum on Moonbeam corresponds to a 0.3125 Gwei minimum on Moonriver and a 0.03125 Gwei on Moonbase.

![MoonGas](/moonbeam-mkdocs/images/builders/get-started/networks/moonbase/moonbase-4.webp)
