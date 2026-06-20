---
title: GoldRush API
description: Learn how to use the GoldRush (formerly Covalent) API on Moonbeam and Moonriver for balances, transactions, logs, and related on-chain data.
categories:
- Indexers and Queries
url: https://docs.moonbeam.network/builders/integrations/indexers/covalent/
word_count: 979
token_estimate: 1785
version_hash: sha256:df248e8b85664373840d81b58bc0e4c93d0e349d5a0e8129863b0fba9a08041d
last_updated: '2026-05-21T21:21:53+00:00'
---

# Getting Started with the GoldRush API

## Introduction {: #introduction }

[GoldRush](https://goldrush.dev/), formerly known as Covalent, provides structured blockchain data APIs for developers building wallets, dashboards, analytics, and automation tooling. Instead of stitching data from many RPC calls, you can query balances, transactions, token transfers, logs, and chain metadata through REST endpoints.

On Moonbeam networks, GoldRush can be used to read both historical and current on-chain data for [Moonbeam](https://goldrush.dev/docs/chains/moonbeam) and [Moonriver](https://goldrush.dev/docs/chains/moonriver). This page is a concise integration guide focused on the most common setup values and endpoint groups.

<div class="intro-disclaimer">
  The information presented herein is for informational purposes only and has been provided by third parties. Moonbeam does not endorse any project listed and described on the Moonbeam docs website (https://docs.moonbeam.network/).
</div>
## Quick Start {: #quick-start }

To begin using GoldRush, create an API key from the [GoldRush dashboard](https://goldrush.dev/platform/auth/register/). Requests use the base URL:

```text
https://api.covalenthq.com/v1/
```

Use the following network values in path parameters:

=== "Moonbeam"

    |  Parameter  |                 Value                  |
    |:-----------:|:--------------------------------------:|
    | `chainName` |          `moonbeam-mainnet`            |
    |  `chainID`  | `1284`     |

=== "Moonriver"

    |  Parameter  |                  Value                   |
    |:-----------:|:----------------------------------------:|
    | `chainName` |          `moonbeam-moonriver`            |
    |  `chainID`  | `1285`      |

## API Usage {: #api-usage }

The following examples show typical request patterns for Moonbeam and Moonriver. Replace `INSERT_API_KEY` with your GoldRush key and `INSERT_WALLET_ADDRESS` with a wallet address for your use case.
You can use GoldRush through direct HTTP requests or through the TypeScript SDK, which wraps the same API endpoints.

### Direct API Calls (curl)

Use these `curl` requests to quickly validate connectivity and response format before integrating in an application.

=== "Moonbeam Mainnet"

    ```bash
    curl -X GET "https://api.covalenthq.com/v1/moonbeam-mainnet/address/INSERT_WALLET_ADDRESS/balances_v2/?key=INSERT_API_KEY"
    ```

=== "Moonriver"

    ```bash
    curl -X GET "https://api.covalenthq.com/v1/moonbeam-moonriver/address/INSERT_WALLET_ADDRESS/balances_v2/?key=INSERT_API_KEY"
    ```

### TypeScript SDK Usage {: #sdk-usage }

If you're building a service or frontend, the GoldRush SDK can simplify request construction and response handling.

=== "Moonbeam TypeScript SDK"

    ```typescript
    import { GoldRushClient } from '@covalenthq/client-sdk';

    async function main());
      console.log(resp);
    }

    main().catch(console.error);
    ```

=== "Moonriver TypeScript SDK"

    ```typescript
    import { GoldRushClient } from '@covalenthq/client-sdk';

    async function main());
      console.log(resp);
    }

    main().catch(console.error);
    ```

## Supported Foundational API Categories {: #supported-foundational-api-categories }

Moonbeam networks support a broad set of GoldRush Foundational API methods. Commonly used categories are listed in the following sections.
For the complete and most current endpoint list, refer to the [Foundational API overview](https://goldrush.dev/docs/goldrush-foundational-api/overview) and [API reference](https://goldrush.dev/docs/api-reference/).

### Wallet APIs

- [Get token balances for address](https://goldrush.dev/docs/api-reference/foundational-api/balances/get-token-balances-for-address)
- [Get native token balance for address](https://goldrush.dev/docs/api-reference/foundational-api/balances/get-native-token-balance)
- [Get historical portfolio value over time](https://goldrush.dev/docs/api-reference/foundational-api/balances/get-historical-portfolio-value-over-time)
- [Get ERC-20 token transfers for address](https://goldrush.dev/docs/api-reference/foundational-api/balances/get-erc20-token-transfers-for-address)

### Activity APIs

- [Get a transaction](https://goldrush.dev/docs/api-reference/foundational-api/transactions/get-a-transaction)
- [Get transaction summary for address](https://goldrush.dev/docs/api-reference/foundational-api/transactions/get-transaction-summary-for-address)
- [Get recent transactions for address (v3)](https://goldrush.dev/docs/api-reference/foundational-api/transactions/get-recent-transactions-for-address-v3)

### Utility and Explorer APIs

- [Get a block](https://goldrush.dev/docs/api-reference/foundational-api/utility/get-a-block)
- [Get gas prices](https://goldrush.dev/docs/api-reference/foundational-api/utility/get-gas-prices)
- [Get log events by contract address](https://goldrush.dev/docs/api-reference/foundational-api/utility/get-log-events-by-contract-address)
- [Get historical token prices](https://goldrush.dev/docs/api-reference/foundational-api/utility/get-historical-token-prices)

### Security APIs

- [Get token approvals for address](https://goldrush.dev/docs/api-reference/foundational-api/security/get-token-approvals-for-address)

## Additional Resources {: #additional-resources }

- [GoldRush docs](https://goldrush.dev/docs/)
- [GoldRush supported chains](https://goldrush.dev/chains/)
- [Moonbeam chain page on GoldRush](https://goldrush.dev/docs/chains/moonbeam)
- [Moonriver chain page on GoldRush](https://goldrush.dev/docs/chains/moonriver)

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
