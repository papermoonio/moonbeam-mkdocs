---
title: Quickly Get Started
description: Everything you need to know to get started developing, deploying, and interacting with smart contracts on Moonbeam.
categories:
- Basics
url: https://docs.moonbeam.network/builders/get-started/quick-start/
word_count: 992
token_estimate: 4211
version_hash: sha256:3805cc4dc3fd7f3cd296413ed78798c9d216bbfbe0166c34b7ba44d5c427298d
last_updated: '2026-05-21T21:21:53+00:00'
---

# Quick Start Guide for Developing on Moonbeam

## Quick Overview {: #overview }

Moonbeam is a fully Ethereum-compatible smart contract platform on Polkadot. As such, you can interact with Moonbeam via the [Ethereum API](/moonbeam-mkdocs/builders/ethereum/) and [Substrate API](/moonbeam-mkdocs/builders/substrate/).

Although Moonbeam is a Substrate-based platform, it uses a [unified accounts](/moonbeam-mkdocs/learn/core-concepts/unified-accounts/) system, which replaces Substrate-style accounts and keys with Ethereum-style accounts and keys. As a result, you can interact with your Moonbeam account with [MetaMask](/moonbeam-mkdocs/tokens/connect/metamask/), [Ledger](/moonbeam-mkdocs/tokens/connect/ledger/), and other Ethereum-compatible wallets by simply adding Moonbeam's network configurations. Similarly, you can develop on Moonbeam using Ethereum [libraries](/moonbeam-mkdocs/builders/ethereum/libraries/) and [development environments](/moonbeam-mkdocs/builders/ethereum/dev-env/).

## Moonbeam Networks {: #moonbeam-networks }

To get started developing on Moonbeam, it's important to be aware of the various networks within the Moonbeam ecosystem.

|                                          Network                                          | Network Type  |                                   Relay Chain                                    | Native Asset Symbol | Native Asset Decimals |
|:-----------------------------------------------------------------------------------------:|:-------------:|:--------------------------------------------------------------------------------:|:-------------------:|:---------------------:|
|           [Moonbeam](/moonbeam-mkdocs/builders/get-started/networks/moonbeam/)            |    MainNet    |                 [Polkadot](https://polkadot.com)                 |        GLMR         |          18           |
|          [Moonriver](/moonbeam-mkdocs/builders/get-started/networks/moonriver/)           |    MainNet    |                 [Kusama](https://kusama.network)                 |        MOVR         |          18           |
|        [Moonbase Alpha](/moonbeam-mkdocs/builders/get-started/networks/moonbase/)         |    TestNet    |                           Alphanet relay (Westend-based)                         |         DEV         |          18           |
| [Moonbeam Development Node](/moonbeam-mkdocs/builders/get-started/networks/moonbeam-dev/) | Local TestNet |                                       None                                       |         DEV         |          18           |

!!! note
    A Moonbeam development node doesn't have a relay chain as its purpose is to be your own personal development environment where you can get started developing quickly without the overhead of a relay chain.

### Network Configurations {: #network-configurations }

When working with developer tools, depending on the tool, you might need to configure Moonbeam to interact with the network. To do so, you can use the following information:

=== "Moonbeam"

    |    Variable     |                                                 Value                                                  |
    |:---------------:|:------------------------------------------------------------------------------------------------------:|
    |    Chain ID     |                           <pre>```1284```</pre>                            |
    | Public RPC URLs | <pre>```https://rpc.api.moonbeam.network```</pre>  <pre>```https://moonbeam.unitedbloc.com```</pre> |
    | Public WSS URLs |                           <pre>```wss://wss.api.moonbeam.network```</pre>                           |

=== "Moonriver"

    |    Variable     |                                                  Value                                                   |
    |:---------------:|:--------------------------------------------------------------------------------------------------------:|
    |    Chain ID     |                            <pre>```1285```</pre>                            |
    | Public RPC URLs | <pre>```https://rpc.api.moonriver.moonbeam.network```</pre>  <pre>```https://moonriver.unitedbloc.com```</pre> |
    | Public WSS URLs |                           <pre>```wss://wss.api.moonriver.moonbeam.network```</pre>                            |

=== "Moonbase Alpha"

    |    Variable     |                                                    Value                                                    |
    |:---------------:|:-----------------------------------------------------------------------------------------------------------:|
    |    Chain ID     |                              <pre>```1287```</pre>                              |
    | Public RPC URLs | <pre>```https://rpc.api.moonbase.moonbeam.network```</pre> |
    | Public WSS URLs |  <pre>```wss://wss.api.moonbase.moonbeam.network```</pre>  |

=== "Moonbeam Dev Node"

    |   Variable    |                        Value                         |
    |:-------------:|:----------------------------------------------------:|
    |   Chain ID    | <pre>```1281```</pre> |
    | Local RPC URL | <pre>```http://127.0.0.1:9944```</pre>  |
    | Local WSS URL | <pre>```ws://127.0.0.1:9944```</pre>  |

!!! note
    You can create your own endpoint suitable for development or production from one of the [supported RPC providers](/moonbeam-mkdocs/builders/get-started/endpoints/#endpoint-providers).

### Block Explorers {: #explorers }

Moonbeam provides two different kinds of explorers: ones to query the Ethereum API, and others dedicated to the Substrate API. All EVM-based transactions are accessible via the Ethereum API whereas the Substrate API can be relied upon for Substrate-native functions such as governance, staking, and some information about EVM-based transactions. For more information on each explorer, please check out the [Block Explorers](/moonbeam-mkdocs/builders/get-started/explorers/) page.

=== "Moonbeam"
    | Block Explorer |   Type    |                                                                  URL                                                                  |
    |:--------------:|:---------:|:-------------------------------------------------------------------------------------------------------------------------------------:|
    |    Moonscan    |    EVM    |                            [https://moonbeam.moonscan.io/](https://moonbeam.moonscan.io)                             |
    |   Expedition   |    EVM    |  [https://moonbeam-explorer.netlify.app/?network=Moonbeam](https://moonbeam-explorer.netlify.app/?network=Moonbeam)  |
    |    Subscan     | Substrate |                             [https://moonbeam.subscan.io/](https://moonbeam.subscan.io)                              |
    |  Polkadot.js   | Substrate | [https://polkadot.js.org/apps/#/explorer](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbeam.network#/explorer) |

=== "Moonriver"
    | Block Explorer |   Type    |                                                                       URL                                                                       |
    |:--------------:|:---------:|:-----------------------------------------------------------------------------------------------------------------------------------------------:|
    |    Moonscan    |    EVM    |                                [https://moonriver.moonscan.io/](https://moonriver.moonscan.io)                                 |
    |   Expedition   |    EVM    |      [https://moonbeam-explorer.netlify.app/?network=Moonriver](https://moonbeam-explorer.netlify.app/?network=Moonriver)      |
    |    Subscan     | Substrate |                                 [https://moonriver.subscan.io/](https://moonriver.subscan.io)                                  |
    |  Polkadot.js   | Substrate | [https://polkadot.js.org/apps/#/explorer](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonriver.moonbeam.network#/explorer) |

=== "Moonbase Alpha"
    | Block Explorer |   Type    |                                                                      URL                                                                       |
    |:--------------:|:---------:|:----------------------------------------------------------------------------------------------------------------------------------------------:|
    |    Moonscan    |    EVM    |                                 [https://moonbase.moonscan.io/](https://moonbase.moonscan.io)                                 |
    |   Expedition   |    EVM    | [https://moonbeam-explorer.netlify.app/?network=MoonbaseAlpha](https://moonbeam-explorer.netlify.app/?network=MoonbaseAlpha)  |
    |    Subscan     | Substrate |                                  [https://moonbase.subscan.io/](https://moonbase.subscan.io)                                  |
    |  Polkadot.js   | Substrate | [https://polkadot.js.org/apps/#/explorer](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#/explorer) |

=== "Moonbeam Dev Node"
    | Block Explorer |   Type    |                                                                        URL                                                                        |
    |:--------------:|:---------:|:-------------------------------------------------------------------------------------------------------------------------------------------------:|
    |   Expedition   |    EVM    | [https://moonbeam-explorer.netlify.app/?network=MoonbeamDevNode](https://moonbeam-explorer.netlify.app/?network=MoonbeamDevNode) |
    |  Polkadot.js   | Substrate |     [https://polkadot.js.org/apps/#/explorer](https://polkadot.js.org/apps/?rpc=wss://ws%3A%2F%2F127.0.0.1%3A9944#/explorer)      |
## Funding TestNet Accounts {: #testnet-tokens }

To get started developing on one of the TestNets, you'll need to fund your account with DEV tokens to send transactions. Please note that DEV tokens have no real value and are for testing purposes only.

|                                          TestNet                                          |                                                                           Where To Get Tokens From                                                                           |
|:-----------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|        [Moonbase Alpha](/moonbeam-mkdocs/builders/get-started/networks/moonbase/)         | The [Moonbase Alpha Faucet](https://faucet.moonbeam.network) website. <br> The faucet dispenses 1.1 DEV tokens every 24 hours |
| [Moonbeam Development Node](/moonbeam-mkdocs/builders/get-started/networks/moonbeam-dev/) | Any of the [ten pre-funded accounts](/moonbeam-mkdocs/builders/get-started/networks/moonbeam-dev/#pre-funded-development-accounts) that come with your <br> development node |

## Development Tools {: #development-tools }

As Moonbeam is a Substrate-based chain that is fully Ethereum-compatible, you can use Substrate-based tools and Ethereum-based tools.

### JavaScript Tools {: #javascript }

=== "Ethereum"

    |                                   Tool                                   |      Type       |
    |:------------------------------------------------------------------------:|:---------------:|
    |   [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/)    |     Library     |
    |      [Hardhat](/moonbeam-mkdocs/builders/ethereum/dev-env/hardhat/)      | Dev Environment |
    |        [Remix](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/)        | Dev Environment |

=== "Substrate"

    |                                       Tool                                        |  Type   |
    |:---------------------------------------------------------------------------------:|:-------:|
    | [Polkadot.js API](/moonbeam-mkdocs/builders/substrate/libraries/polkadot-js-api/) | Library |

### Python Tools {: #python }

=== "Ethereum"

    |                              Tool                               |      Type       |
    |:---------------------------------------------------------------:|:---------------:|
    | [Web3.py](/moonbeam-mkdocs/builders/ethereum/libraries/web3py/) |     Library     |

=== "Substrate"

    |                                              Tool                                               |  Type   |
    |:-----------------------------------------------------------------------------------------------:|:-------:|
    | [Py Substrate Interface](/moonbeam-mkdocs/builders/substrate/libraries/py-substrate-interface/) | Library |
