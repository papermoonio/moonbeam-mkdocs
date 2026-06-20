---
title: Transfer & Monitor Balances on Moonbeam
description: A description of the main differences that developers need to understand in terms of the different balance transfers available on Moonbeam compared to Ethereum.
categories:
- Basics
url: https://docs.moonbeam.network/learn/core-concepts/transfers-api/
word_count: 1218
token_estimate: 2009
version_hash: sha256:2875cfb6b5e32746ec89c5a37bc2e688dddd67472a51ba2916afedd17edb2fa1
last_updated: '2026-05-21T21:21:53+00:00'
---

# Balance Transfers on Moonbeam

## Introduction {: #introduction }

While Moonbeam strives to be compatible with Ethereum's Web3 API and EVM, there are some important Moonbeam differences that developers should know and understand in terms of balance transfers of the base network token (for example, GLMR and MOVR).

Token holders have two ways of initiating a balance transfer on Moonbeam. On the one hand, users can use the Ethereum API via apps like MetaMask, MathWallet, or any other tools that use the Ethereum JSON-RPC. On the other hand, users can use the Substrate API via the Polkadot.js Apps website or directly using the Substrate RPC.

Developers need to be aware that token holders can leverage both APIs to transfer the base-layer network token. Note that these comments do not apply to transfers of other assets, like ERC-20 based assets in the Moonriver or Moonbeam EVMs. Transfers of these assets are only done via the Ethereum APIs since these are smart contract interactions.

This guide will outline some of the main differences between both APIs for base-layer network token balance transfers and what to expect when using Moonbeam for the first time.

## Ethereum Transfers {: #ethereum-transfers }

A simple balance transfer using the Ethereum API relies on the `eth_sendRawTransaction` JSON-RPC. This can be done directly from one account to another or via a smart contract.

There are different strategies to listen for transfers or balance changes on Ethereum, which are not covered in this documentation. But they are all focused on different strategies using the Ethereum JSON-RPC.

## Moonbeam Transfers {: #moonbeam-transfers }

As stated before, Moonbeam enables token holders to execute base-layer network token transfers via both the Ethereum and Substrate API. There are multiple scenarios to trigger token transfers on Moonbeam. Consequently, to monitor all transfers, **you should use the Polkadot.js SDK** (Substrate API).

Before going over the different scenarios, there are two different elements associated with a block:

 - **Extrinsic** — refers to state changes that originated outside of the system itself. The most common form of extrinsic is a transaction. They are ordered by execution
 - **Events** — refers to logs generated from the extrinsic. There can be multiple events per extrinsic. They are ordered by execution

The different transfer scenarios are:

 - **Substrate transfer** — it will create an extrinsic, either `balances.transferAllowDeath` or `balances.transferKeepAlive`. It will trigger **one** `balances.Transfer` event
 - **Substrate feature** — some native Substrate features can create extrinsic that would send tokens to an address. For example, [Treasury](/moonbeam-mkdocs/learn/features/treasury/) can create an extrinsic such as `treasury.proposeSend`, which will trigger **one or multiple** `balances.Transfer` events
 - **Ethereum transfer** — it will create an `ethereum.transact` extrinsic with an empty input. It will trigger **one** `balances.Transfer` event
 - **Ethereum transfers via smart contracts** — it will create an `ethereum.transact` extrinsic with some data as input. It will trigger **one or multiple** `balances.Transfer` events

All the scenarios described above will effectively transfer base-layer network tokens. The easiest way to monitor them all is to rely on the `balances.Transfer` event.

## Monitor Native Token Balance Transfers {: #monitor-transfers }

The following code samples will demonstrate how to listen to both types of native token transfers, sent via the Substrate or Ethereum API, using either the [Polkadot.js API library](https://polkadot.js.org/docs/api/start/) or [Substrate API Sidecar](https://github.com/paritytech/substrate-api-sidecar). The following code snippets are for demo purposes only and should not be used without modification and further testing in a production environment.

### Using Polkadot.js API {: #using-polkadotjs-api }

The [Polkadot.js API package](https://polkadot.js.org/docs/api/start/) provides developers a way to interact with Substrate chains using JavaScript.

The following code snippet uses [`subscribeFinalizedHeads`](https://polkadot.js.org/docs/substrate/rpc/#subscribefinalizedheads-header) to subscribe to new finalized block headers, loops through extrinsics fetched from the block, and retrieves the events of each extrinsic. Then, it checks if any event corresponds to a `balances.Transfer` event. If so, it will extract the `from`, `to`, `amount`, and the `tx hash` of the transfer and display it on the console. Note that the `amount` is shown in the smallest unit (Wei).  You can find all the available information about Polkadot.js and the Substrate JSON-RPC on their [official documentation site](https://polkadot.js.org/docs/substrate/rpc).

```ts
import { typesBundlePre900 } from 'moonbeam-types-bundle';
import { ApiPromise, WsProvider } from '@polkadot/api';

// This script will listen to all GLMR transfers (Substrate & Ethereum) and extract the tx hash
// It can be adapted for Moonriver or Moonbase Alpha

const main = async () => {
  // Define the provider for Moonbeam
  const wsProvider = new WsProvider('wss://wss.api.moonbeam.network');
  // Create the provider using Moonbeam types
  const polkadotApi = await ApiPromise.create({
    provider: wsProvider,
    typesBundle: typesBundlePre900 as any,
  });

  // Subscribe to finalized blocks
  await polkadotApi.rpc.chain.subscribeFinalizedHeads(
    async (lastFinalizedHeader) => {
      const [{ block }, records] = await Promise.all([
        polkadotApi.rpc.chain.getBlock(lastFinalizedHeader.hash),
        polkadotApi.query.system.events.at(lastFinalizedHeader.hash),
      ]);

      block.extrinsics.forEach((extrinsic, index) => {
        const {
          method: { args, method, section },
        } = extrinsic;

        const isEthereum = section == 'ethereum' && method == 'transact';

        // Gets the transaction object
        const tx = args[0] as any;

        // Convert to the correct Ethereum Transaction format
        const ethereumTx =
          isEthereum &&
          ((tx.isLegacy && tx.asLegacy) ||
            (tx.isEip1559 && tx.asEip1559) ||
            (tx.isEip2930 && tx.asEip2930));

        // Check if the transaction is a transfer
        const isEthereumTransfer =
          ethereumTx &&
          ethereumTx.input.length === 0 &&
          ethereumTx.action.isCall;

        // Retrieve all events for this extrinsic
        const events = records.filter(
          ({ phase }) =>
            phase.isApplyExtrinsic && phase.asApplyExtrinsic.eq(index)
        );

        // This hash will only exist if the transaction was executed through Ethereum.
        let ethereumHash = '';

        if (isEthereum)) => {
            if (event.section == 'ethereum' && event.method == 'Executed')
          });
        }

        // Search if it is a transfer
        events.forEach(({ event }) => {
          if (event.section == 'balances' && event.method == 'Transfer') to ${to} of ${balance} (block #${lastFinalizedHeader.number})`
            );
            console.log(`  - Triggered by extrinsic: ${substrateHash}`);
            if (isEthereum)) hash: ${ethereumHash}`
              );
            }
          }
        });
      });
    }
  );
};

main();
```

In addition, you can find more sample code snippets related to more specific cases around balance transfers on this [GitHub page](https://gist.github.com/crystalin/b2ce44a208af60d62b5ecd1bad513bce).

### Using Substrate API Sidecar {: #using-substrate-api-sidecar }

Developers can also retrieve Moonbeam blocks and monitor transactions sent via both the Substrate and Ethereum APIs using [Substrate API Sidecar](https://github.com/paritytech/substrate-api-sidecar), a REST API service for interacting with blockchains built with the Substrate framework.

The following code snippet uses the Axios HTTP client to query the [Sidecar endpoint `/blocks/head`](https://paritytech.github.io/substrate-api-sidecar/dist) for the latest finalized block and then decodes the block for the `from`, `to`, `value`, `tx hash`, and `transaction status` of native token transfers at both the EVM and Substrate API level.

```js
import axios from 'axios';

// This script will decode all native token transfers (Substrate & Ethereum) in a given Sidecar block, and extract the tx hash. It can be adapted for any Moonbeam network.

// Endpoint to retrieve the latest block
const endpoint = 'http://127.0.0.1:8080/blocks/head';

async function main() else {
              console.log('Status: Failed');
            }
          }
        });
      }

      // Retrieve Substrate Transfers
      if (
        extrinsic.method.pallet === 'balances' &&
        (extrinsic.method.method === 'transferKeepAlive' ||
          extrinsic.method.method === 'transferAllowDeath')
      ) else {
              console.log('Status: Failed');
            }
          }
        });
      }
    });
  } catch (err)
}

main();
```

You can reference the [Substrate API Sidecar page](/moonbeam-mkdocs/builders/substrate/libraries/sidecar/) for information on installing and running your own Sidecar service instance, as well as more details on how to decode Sidecar blocks for Moonbeam transactions.
