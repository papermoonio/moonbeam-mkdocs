---
title: Subscribe to Ethereum-style Events on Moonbeam
description: Take a look at the non-standard Ethereum JSON-RPC methods supported on Moonbeam that offer publish-subscribe functionality for specific events.
categories:
- JSON-RPC APIs
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/json-rpc/pubsub/
word_count: 2174
token_estimate: 4094
version_hash: sha256:c08ae408ddf4bf6a9a0f5cc62cea3655c4804a6b8e9f44c767ca1cac9444f3c1
last_updated: '2026-05-21T21:21:53+00:00'
---

# Subscribe to Events

## Introduction {: #introduction }

Moonbeam supports event subscriptions for Ethereum-style events, which allows you to wait for events and handle them accordingly instead of polling for them.

It works by subscribing to particular events; an ID is returned for each subscription. For each event that matches the subscription, a notification with relevant data is sent together with the subscription ID.

In this guide, you will learn how to subscribe to event logs, incoming pending transactions, and incoming block headers on Moonbase Alpha. This guide can also be adapted for Moonbeam or Moonriver.

## Supported Pubsub JSON-RPC Methods {: #filter-rpc-methods }

Please note that the examples in this section require installing [wscat](https://github.com/websockets/wscat).

???+ function "eth_subscribe"

    Creates a subscription for a given subscription name.

    === "Parameters"

        - `subscription_name` *string* - the type of the event to subscribe to. The [supported subscription](https://geth.ethereum.org/docs/interacting-with-geth/rpc/pubsub#supported-subscriptions) types are:
            - [`newHeads`](https://geth.ethereum.org/docs/interacting-with-geth/rpc/pubsub#newheads) — triggers a notification each time a new header is appended to the chain
            - [`logs`](https://geth.ethereum.org/docs/interacting-with-geth/rpc/pubsub#logs) — returns logs that are included in new imported blocks and match a given filter criteria
            - [`newPendingTransactions`](https://geth.ethereum.org/docs/interacting-with-geth/rpc/pubsub#newpendingtransactions) — returns the hash for all transactions that are added to the pending state
            - [`syncing`](https://geth.ethereum.org/docs/interacting-with-geth/rpc/pubsub#syncing) — indicates when the node starts or stops synchronizing with the network

    === "Returns"

        The `result` returns the subscription ID.

    === "Example"

        ```bash
        wscat -c wss://wss.api.moonbase.moonbeam.network -x '
          {
            "jsonrpc": "2.0", 
            "id": 1, 
            "method": "eth_subscribe", 
            "params": ["INSERT_SUBSCRIPTION_NAME"]
          }'
        ```

???+ function "eth_unsubscribe"

    Cancels an existing subscription given its subscription ID.

    === "Parameters"

        - `subscription_id` *string* - the subscription ID
  
    === "Returns"

        The `result` returns a boolean indicating whether or not the subscription was successfully canceled.

    === "Example"

        ```bash
        wscat -c wss://wss.api.moonbase.moonbeam.network -x '
          {
            "jsonrpc": "2.0", 
            "id": 1, 
            "method": "eth_unsubscribe", 
            "params": ["INSERT_SUBSCRIPTION_ID"]
          }'
        ```

## Subscribe to Events Using Ethereum Libraries {: #subscribe-to-events }

This section will show you how to use [Ethereum libraries](/moonbeam-mkdocs/builders/ethereum/libraries/), like [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/), to programmatically subscribe to events on Moonbeam.

### Checking Prerequisites {: #checking-prerequisites }

The examples in this guide are based on an Ubuntu 22.04 environment. You will also need the following:

- MetaMask installed and [connected to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/)
- An account with funds.
  You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
- To deploy your own ERC-20 token on Moonbase Alpha. You can do this by following [our Remix tutorial](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) while first pointing MetaMask to Moonbase Alpha
- Ethers.js or the Ethereum library of your choice installed. You can install Ethers.js via npm:

    ```bash
    npm install ethers
    ```

### Subscribe to Event Logs {: #subscribing-to-event-logs-in-moonbase-alpha }

Any contract that follows the ERC-20 token standard emits an event related to a token transfer, that is, `event Transfer(address indexed from, address indexed to, uint256 value)`. In this section, you'll learn how to subscribe to these events using the Ethers.js library.

Use the following code snippet to set up a subscription to listen for token transfer events:

```js
const { ethers } = require('ethers');

const provider = new ethers.WebSocketProvider(
  'wss://wss.api.moonbase.moonbeam.network'
);

const tokenAddress = 'INSERT_CONTRACT_ADDRESS';
const abi = [
  'event Transfer(address indexed from, address indexed to, uint256 value)',
];
const iface = new ethers.Interface(abi);
const transferTopic = ethers.id('Transfer(address,address,uint256)');

const filter = {
  address: tokenAddress,
  topics: [transferTopic],
};

const main = async () => {
  console.log('🕔 Subscription set up. Waiting for new logs');

  provider.on(filter, (log) => {
    const parsed = iface.parseLog(log);

    console.log({
      from: parsed.args.from,
      to: parsed.args.to,
      value: parsed.args.value.toString(),
      blockNumber: log.blockNumber,
      txHash: log.transactionHash,
    });
  });
};

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

!!! note
    Make sure to replace `'INSERT_CONTRACT_ADDRESS'` with the actual address of the ERC-20 token contract that you should have already deployed (as a [prerequisite](#checking-prerequisites)).

In the provided code:

- A WebSocket provider is used to listen for the `Transfer` event and parse the log with the contract ABI
- The listener filters for the `Transfer` event by signature, which can be calculated as follows:

    ```js
    EventSignature = keccak256(Transfer(address,address,uint256))
    ```

    This translates to `0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef` and is used as the first topic in the subscription filter.

If you do not provide any topics, you subscribe to all events emitted by the contract. More information about topics can be found in the [Understanding event logs on the Ethereum blockchain](https://medium.com/mycrypto/understanding-event-logs-on-the-ethereum-blockchain-f4ae7ba50378) Medium post.

By executing this code, you'll establish a subscription to monitor ERC-20 token transfer events on Moonbeam. New events will be logged to the terminal as they occur.

<div id="termynal" data-termynal>
  <span data-ty="input"><span class="file-path"></span> node contract-events.js</span>
  <span data-ty>0x35547a6f7777444f35306f5353556271</span>
</div>
#### Understanding Event Logs {: #understanding-event-logs }

To illustrate the process, assume that an ERC-20 token transfer has been sent with the following parameters:

 - **From address** - `0x44236223aB4291b93EEd10E4B511B37a398DEE55`
 - **To address** - `0x8841701Dba3639B254D9CEe712E49D188A1e941e`
 - **Value (tokens)** - `1000000000000000000` (1 DEV in Wei)

The event logs emitted by the transaction are as follows:

<div id="termynal" data-termynal>
  <span data-ty="input"><span class="file-path"></span> node contract-events.js</span>
  <span data-ty>0x35547a6f7777444f35306f5353556271</span>
  <span data-ty>{</span>
  <span data-ty>  address: '0xCc17F1FAEAab9Fe70Dc2D616Ea768a4336f3c506',</span>
  <span data-ty>  blockHash: '0x12d1f37db14f8d4efa2540ecb63d7f8b95236bb11c405e58691a45070d2c7e7f',</span>
  <span data-ty>  blockNumber: 16736,</span>
  <span data-ty>  data: '0x0000000000000000000000000000000000000000000000000d0b6b3a7640000',</span>
  <span data-ty>  logIndex: 0,</span>
  <span data-ty>  removed: false,</span>
  <span data-ty>  topics: [</span>
  <span data-ty>    '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',</span>
  <span data-ty>    '0x00000000000000000000000044236223ab4291b93eed10e4b511b37a398dee55',</span>
  <span data-ty>    '0x0000000000000000000000008841701dba3639b254d9cee712e49d188a1e941e'</span>
  <span data-ty>  ],</span>
  <span data-ty>  transactionHash: '0xd53891693a731e0bca3287adc6375d04fe3b6605d00b186a669c6bbc8d22e88d',</span>
  <span data-ty>  transactionIndex: 0,</span>
  <span data-ty>  transactionLogIndex: '0x0',</span>
  <span data-ty>  id: 'log_83c933b0'</span>
  <span data-ty>}</span>
</div>
If you look at the `topics` array, there are a total of three topics present (in this order):

1. The event signature of the `Transfer` event
2. The `from` address
3. The `to` address

As there are a total of three topics (the maximum is four), this corresponds to the LOG3 opcode:

![Description of LOG3](/moonbeam-mkdocs/images/builders/ethereum/json-rpc/pubsub/pubsub-1.webp)

Indexed topics, such as the `from` and `to` addresses, are typically represented by 256-bit (64 hexadecimal character) values. If necessary, they are padded with zeros to reach the full length.

Unindexed data, such as the value of tokens transferred, is not included in the `topics` array. Instead, it is returned within the logs' `data` field, encoded in bytes32/hex format. You can decode this value using Ethereum libraries such as Ethers.js (for example, with `AbiCoder`) and verify that the `data` corresponds to 1 DEV token formatted in Wei.

If the event returns multiple unindexed values, they will be appended one after the other in the same order the event emits them. Therefore, each value is obtained by deconstructing data into separate 32-byte (or 64-hex-character-long) pieces.

#### Use Wildcards and Conditional Formatting {: #using-wildcards-and-conditional-formatting }

Using the same example as in the previous section, you can subscribe to Transfer events while filtering by specific senders with the following code:

```js
const { ethers } = require('ethers');

const provider = new ethers.WebSocketProvider(
  'wss://wss.api.moonbase.moonbeam.network'
);

const tokenAddress = 'INSERT_CONTRACT_ADDRESS';
const abi = [
  'event Transfer(address indexed from, address indexed to, uint256 value)',
];
const contract = new ethers.Contract(tokenAddress, abi, provider);

// Listen for Transfer events where the "from" address matches either entry below
const fromAddresses = [
  '0x44236223aB4291b93EEd10E4B511B37a398DEE55',
  '0x8841701Dba3639B254D9CEe712E49D188A1e941e',
];

const filter = contract.filters.Transfer(fromAddresses, null);

const main = async () => {
  console.log('🕔 Subscription set up. Waiting for new logs');

  contract.on(filter, (from, to, value, event) => {
    console.log({
      from,
      to,
      value: value.toString(),
      blockNumber: event.blockNumber,
      txHash: event.transactionHash,
    });
  });
};

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

Here, the first indexed parameter (`from`) is filtered to the provided address list, while `to` is set to `null` to act as a wildcard. The contract filter handles topic formatting for you, so you don't need to manually pad the addresses.

<div id="termynal" data-termynal>
  <span data-ty="input"><span class="file-path"></span> node contract-events.js</span>
  <span data-ty>0x51583364703338703441507476516675</span>
  <span data-ty>{</span>
  <span data-ty>  address: '0xCc17F1FAEAab9Fe70Dc2D616Ea768a4336f3c506',</span>
  <span data-ty>  blockHash: '0xc7fa1139a35fb7a634514907feeb771e6aac7717906922a8589f029f709dcaef',</span>
  <span data-ty>  blockNumber: 16739,</span>
  <span data-ty>  data: '0x0000000000000000000000000000000000000000000000000de0b6b3a7640000',</span>
  <span data-ty>  logIndex: 0,</span>
  <span data-ty>  removed: false,</span>
  <span data-ty>  topics: [</span>
  <span data-ty>    '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',</span>
  <span data-ty>    '0x00000000000000000000000044236223ab4291b93eed10e4b511b37a398dee55',</span>
  <span data-ty>    '0x0000000000000000000000008841701dba3639b254d9cee712e49d188a1e941e'</span>
  <span data-ty>  ],</span>
  <span data-ty>  transactionHash: '0x84154ea6ee44a4ffc446acd17579966691105694ce370f01de09d3a9f1b9506',</span>
  <span data-ty>  transactionIndex: 0,</span>
  <span data-ty>  transactionLogIndex: '0x0',</span>
  <span data-ty>  id: 'log_188dbef1'</span>
  <span data-ty>}</span>
  <span data-ty>{</span>
  <span data-ty>  address: '0xCc17F1FAEAab9Fe70Dc2D616Ea768a4336f3c506',</span>
  <span data-ty>  blockHash: '0xf21ded1bc724d2be74bc97c2045e31754d5326f3964796d62a1cba3e1d06203',</span>
  <span data-ty>  blockNumber: 16740,</span>
  <span data-ty>  data: '0x0000000000000000000000000000000000000000000000000de0b6b3a7640000',</span>
  <span data-ty>  logIndex: 0,</span>
  <span data-ty>  removed: false,</span>
  <span data-ty>  topics: [</span>
  <span data-ty>    '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',</span>
  <span data-ty>    '0x0000000000000000000000008841701dba3639b254d9cee712e49d188a1e941e',</span>
  <span data-ty>    '0x00000000000000000000000044236223ab4291b93eed10e4b511b37a398dee55'</span>
  <span data-ty>  ],</span>
  <span data-ty>  transactionHash: '0x091b736bd31457a9b0725a98926dc3ebfb0608e71197c10d4d9ccb80de6d9ac3',</span>
  <span data-ty>  transactionIndex: 0,</span>
  <span data-ty>  transactionLogIndex: '0x0',</span>
  <span data-ty>  id: 'log_401c7925'</span>
  <span data-ty>}</span>
</div>
As shown, after you provided the two addresses with conditional formatting, you should have received two logs with the same subscription. Events emitted by transactions from different addresses will not throw any logs to this subscription.

This example showed how you could subscribe to just the event logs of a specific contract, but the same approach applies to other subscription types covered in the following sections.

### Subscribe to Incoming Pending Transactions {: #subscribe-to-incoming-pending-transactions }

To subscribe to pending transactions with Ethers.js, you can use a WebSocket provider and the `provider.on('pending')` event. The transaction hash of the pending transactions is returned, and you can optionally fetch full transaction details with `provider.getTransaction(hash)`.

<div id="termynal" data-termynal>
  <span data-ty="input"><span class="file-path"></span> node pending-tx.js</span>
  <span data-ty>0x3350757676747651354e4553724e7269</span>
  <span data-ty>0x5e3870e2c38274f4344cb86f3719dad84193b610a13b7e60c7ee65868b7ebc9a</span>
  <span data-ty>0x54a28da6915df1ec83af4aafeab57364bbf4239d5ba71b596faabc76ba355eab</span>
</div>
You can try this by sending a transaction and verifying that the transaction hash returned by the subscription is the same one returned by the development tool or wallet you are using.

### Subscribe to Incoming Block Headers {: #subscribe-to-incoming-block-headers }

You can also subscribe to new block headers using `provider.on('block')`, then fetch the block with `provider.getBlock(blockNumber)`. This subscription provides incoming block headers and can be used to track changes in the blockchain.

<div id="termynal" data-termynal>
  <span data-ty="input"><span class="file-path"></span> node block-headers.js</span>
  <span data-ty>0x6472456d30776b636c615a317158514e</span>
  <span data-ty>{</span>
  <span data-ty>  author: '0x0000000000000000000000000000000000000000',</span>
  <span data-ty>  difficulty: '0',</span>
  <span data-ty>  extraData: '0x',</span>
  <span data-ty>  gasLimit: 0,</span>
  <span data-ty>  gasUsed: 0,</span>
  <span data-ty>  hash: '0x1a28a9a7a176ed0d627f1bc521bda4eaca1e8186bf6642f089578067b713da43',</span>
  <span data-ty>  logsBloom: '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',</span>
  <span data-ty>  miner: '0x0000000000000000000000000000000000000000',</span>
  <span data-ty>  number: 16756,</span>
  <span data-ty>  parentHash: '0x89401a45d6226a5eb509fd3abfd90cb74aa5d7b5f747ef2506013d1afa36a418',</span>
  <span data-ty>  receiptsRoot: '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',</span>
  <span data-ty>  sealFields: [</span>
  <span data-ty>    '0x0000000000000000000000000000000000000000000000000000000000000000',</span>
  <span data-ty>    '0x0000000000000000'</span>
  <span data-ty>  ],</span>
  <span data-ty>  sha3Uncles: '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',</span>
  <span data-ty>  size: 509,</span>
  <span data-ty>  stateRoot: '0x92f3417ed90a81fecb2587fd820c1479f88f27228b8f508dfde601061d14371d',</span>
  <span data-ty>  timestamp: 1607710710159,</span>
  <span data-ty>  transactionsRoot: '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'</span>
  <span data-ty>}</span>
</div>
Note that only one block header is shown in the image. These messages are displayed for every block produced so they can quickly fill up the terminal.

### Check If a Node Is Synchronized with the Network {: #check-if-a-node-is-synchronized-with-the-network }

With pubsub, checking whether a particular node is currently synchronizing with the network is also possible. You can call the `eth_subscribe` RPC with `syncing` using your preferred library's low-level WebSocket request helper. This subscription will either return a boolean when `syncing` is false or an object describing the syncing progress when `syncing` is true, as seen below.

<div id="termynal" data-termynal>
  <span data-ty="input"><span class="file-path"></span> node syncing.js</span>
  <span data-ty>0x3252615570630563274436770446371</span>
  <span data-ty>{</span>
  <span data-ty>  syncing: true,</span>
  <span data-ty>  startingBlock: 120237,</span>
  <span data-ty>  currentBlock: 146952,</span>
  <span data-ty>  highestBlock: 2553484</span>
  <span data-ty>}</span>
</div>
!!! note
    The pubsub implementation in [Frontier](https://github.com/polkadot-evm/frontier) is still in active development. This current version allows users to subscribe to specific event types, but there may still be some limitations.
