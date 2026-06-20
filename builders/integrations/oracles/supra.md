---
title: Supra Oracles
description: Supra's Pull Oracle provides low-latency, on-demand price feed updates for a variety of use cases. Learn how to integrate Supra's oracle on Moonbeam.
categories:
- Oracle Nodes
url: https://docs.moonbeam.network/builders/integrations/oracles/supra/
word_count: 774
token_estimate: 1432
version_hash: sha256:531c23b7fb87f4f56f43655b8765eadb95bee84b82e44ee77e54624050eb02c6
last_updated: '2026-05-21T21:21:53+00:00'
---

# Supra Oracles

## Introduction {: #introduction }

[Supra](https://supra.com) is a novel, high-throughput oracle and intralayer: a vertically integrated toolkit of cross-chain solutions (data oracles, asset bridge, automation network, and more) that interlink all blockchains, public (L1s and L2s) or private (enterprises), including Moonbeam.

Supra provides decentralized oracle price feeds that can be used for on-chain and off-chain use cases such as spot and perpetual DEXes, lending protocols, and payment protocols.

This page provides everything you need to know to get started with Supra on Moonbeam.

<div class="intro-disclaimer">
  The information presented herein is for informational purposes only and has been provided by third parties. Moonbeam does not endorse any project listed and described on the Moonbeam docs website (https://docs.moonbeam.network/).
</div>
## How to use Supra's Price Feeds {: #price-feeds }

Supra uses a pull model as a customized approach that publishes price data upon request. It combines Web2 and Web3 methods to achieve low latency when sending data from Supra to destination chains. The process involves the following steps:

1. Web2 methods are used to retrieve price data from Supra.
2. Smart contracts are utilized for cryptographically verifying and writing the latest price data on-chain, where it lives on immutable ledgers, using [Supra's Pull Oracle V1](https://docs.supra.com/oracles/data-feeds/pull-oracle).
3. Once the data has been written on-chain, the most recently published price feed data will be available in Supra's Storage contract.

The addresses for Supra's contracts on Moonbeam are as follows:

=== "Moonbeam"

    |  Contract   |                                                               Address                                                               |
    |:-----------:|:-----------------------------------------------------------------------------------------------------------------------------------:|
    | Pull Oracle | [0x2FA6DbFe4291136Cf272E1A3294362b6651e8517](https://moonscan.io/address/0x2FA6DbFe4291136Cf272E1A3294362b6651e8517) |
    |   Storage   |     [0xD02cc7a670047b6b012556A88e275c685d25e0c9](https://moonscan.io/address/0xD02cc7a670047b6b012556A88e275c685d25e0c9)     |

=== "Moonbase Alpha"

    |  Contract   |                                                                   Address                                                                    |
    |:-----------:|:--------------------------------------------------------------------------------------------------------------------------------------------:|
    | Pull Oracle | [0xaa2f56843Cec7840F0C106F0202313d8d8CB13d6](https://moonbase.moonscan.io/address/0xaa2f56843Cec7840F0C106F0202313d8d8CB13d6) |
    |   Storage   |     [0x4591d1B110ad451d8220d82252F829E8b2a91B17](https://moonbase.moonscan.io/address/0x4591d1B110ad451d8220d82252F829E8b2a91B17)     |

!!! note
    Moonriver is not supported at this time.

### List of Available Price Feeds {: #list-of-available-price-feeds }

To view a complete list of the available data pairs provided by Supra, please check out their [data feeds catalog](https://docs.supra.com/oracles/data-feeds/data-feeds-index) on their documentation site.

To interact with any of these data pairs, you'll need to take note of the pair's **Pair ID**.

### Try It Out {: #try-it-out }

Try out a basic example of how to fetch price data using Supra's pull model by following the steps mentioned in the [previous section](#price-feeds) or by referencing the [Supra documentation](https://supra.com/developers/).

## Connect with Supra {: #connect-with-supra }

Still looking for answers? Supra's got them! Check out all the ways you can reach the Supra team:

- Visit [Supra's websites at supraoracles.com](https://supra.com).
- Read their [docs](https://docs.supra.com/oracles/overview).
- Chat with them on [Telegram](https://t.me/SupraOracles).
- Follow them on [X](https://x.com/SupraOracles).
- Join their [Discord](https://discord.com/invite/supraoracles).
- Check out their [Youtube](https://www.youtube.com/SupraOfficial).

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
