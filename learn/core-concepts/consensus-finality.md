---
title: Consensus & Finality
description: The main differences that Ethereum developers should understand in terms of consensus and finality on Moonbeam and how it differs from Ethereum.
categories:
- Basics
url: https://docs.moonbeam.network/learn/core-concepts/consensus-finality/
word_count: 3260
token_estimate: 5162
version_hash: sha256:28483b9cdbe7bf276424d92f8ad824320068cee69241c63df179192a654e931a
last_updated: '2026-05-21T21:21:53+00:00'
---

# Moonbeam Consensus & Finality

## Introduction {: #introduction }

While Moonbeam strives to be compatible with Ethereum's Web3 API and EVM, there are some important Moonbeam differences that developers should know and understand in terms of consensus and finality.

In short, consensus is a way for different parties to agree on a shared state. As blocks are created, nodes in the network must decide which block will represent the next valid state. Finality defines when that valid state cannot be altered or reversed.

Ethereum began by using a consensus protocol based on [Proof-of-Work (PoW)](https://ethereum.org/developers/docs/consensus-mechanisms/pow/), which provides probabilistic finality. However, in 2022, Ethereum switched to [Proof-of-Stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/), which provides deterministic finality, and no longer uses PoW. In contrast, Moonbeam uses a hybrid consensus protocol based on Delegated Proof-of-Stake (DPoS), which also provides deterministic finality. DPoS is an evolution of Polkadot's [Nominated Proof of Stake (NPoS)](https://docs.polkadot.com/reference/polkadot-hub/consensus-and-security/pos-consensus/) concept, that puts more power into the hands of token holders by allowing delegators to choose which collator candidate they want to support and in what magnitude.

This guide will outline some of these main differences around consensus and finality, and what to expect when using Moonbeam for the first time.

## Ethereum Consensus and Finality {: #ethereum-consensus-and-finality }

Ethereum currently uses a PoS consensus protocol, in which validators stake ETH in the network and are responsible for producing blocks and checking the validity of new blocks. The timing of block production is fixed and is divided into 12 second slots and 32 slot epochs. One validator per slot is randomly selected to produce a block and broadcast it to the network. There is a randomly selected committee of validators per slot that is responsible for determining the validity of the block. The greater the stake in the network, the greater the chance the validator will be chosen to produce or validate a block.

Finality is deterministic in Ethereum's PoS consensus protocol and is achieved through "checkpoint" blocks. Validators agree on the state of a block at particular checkpoint blocks, which are always the first block in an epoch, and if two-thirds of the validators agree, the block is finalized. Block finality can be reverted; however, there are strong economic incentives in place so validators do not attempt to collude to revert a block. You can find out more information in Vitalik's [On Settlement Finality](https://blog.ethereum.org/2016/05/09/on-settlement-finality) blog, under the Finality in Casper section.

## Moonbeam Consensus and Finality {: #moonbeam-consensus-and-finality }

In Polkadot, there are collators and validators. [Collators](https://wiki.polkadot.com/learn/learn-collator/) maintain parachains (in this case, Moonbeam) by collecting transactions from users and producing state transition proofs for the relay chain [validators](https://wiki.polkadot.com/learn/learn-validator/). The collator set (nodes that produce blocks) is selected based on the stake they have in the network.

For finality, Polkadot and Kusama rely on [GRANDPA](https://docs.polkadot.com/reference/polkadot-hub/consensus-and-security/pos-consensus/#finality-gadget-grandpa). GRANDPA provides deterministic finality for any given transaction (block). In other words, when a block or transaction is marked as final, it can't be reverted except via on-chain governance or forking. Moonbeam follows this deterministic finality.

## Main Differences Between PoS and DPoS {: #main-differences }

In terms of consensus, Moonbeam is based on Delegated Proof-of-Stake, while Ethereum relies on a standard Proof-of-Stake system, which is slightly different. Although both mechanisms rely on the use of stake to validate and create new blocks, there are some key differences.

With PoS on Ethereum, validators are selected to produce and validate blocks based on their own stake in the network. As long as a validator has placed a validator deposit, they can be selected to produce and validate blocks. However, as previously mentioned, the greater the stake in the network, the higher the chances a validator has to be selected to produce and validate blocks.

On the other hand, with DPoS on Moonbeam, collators become eligible to produce blocks based on their own stake plus their delegated stake in the network. Any token holder can choose to delegate their stake to a collator candidate. The top collator candidates by stake, including delegations, join the active set. The number of candidates in the active set is subject to [governance](/moonbeam-mkdocs/learn/features/governance/). Once in the active set, collators are randomly selected to produce blocks using the Nimbus Consensus Framework. It is important to note that once a collator is in the active set, their total stake does not impact their chances of being selected to produce blocks.

In terms of finality, blocks on Ethereum can take quite a bit longer to finalize than on Moonbeam due to the checkpoint finality system it uses. In Ethereum, validators determine finality at checkpoint blocks, which are always the first block in an epoch. Since an epoch has 32 slots and each slot is 12 seconds, it'll take at least 384 seconds, or 6.4 minutes for a block to be finalized.

Moonbeam does not use checkpoint blocks and instead relies on Polkadot's GRANDPA finality gadget, where the finality process is completed in parallel to block production. In addition, the finality process incorporates the blockchain's structure, which allows the relay chain validators to vote on the highest block that they think is valid. In this scenario, the vote would apply to all of the blocks leading up to the one that is finalized, which speeds up the finalization process. After a block has been included in the relay chain, a block can be finalized within one block on Moonbeam.

## Check Transaction Finality with Ethereum RPC Endpoints {: #check-tx-finality-with-ethereum-rpc-endpoints }

Although the finality gadgets differ, you can use the same, fairly simple strategy to check for transaction finality on both Ethereum and Moonbeam:

 1. You ask the network for the hash of the latest finalized block
 2. You retrieve the block number using the hash
 3. You compare it with the block number of your transaction. If your transaction was included in a previous block, it is finalized
 4. As a safety check, retrieve the block by number and verify that the given transaction hash is in the block

The snippets below follow this strategy to check transaction finality. It uses the `finalized` option for the [default block parameter](https://ethereum.org/developers/docs/apis/json-rpc/#default-block) to get the latest finalized block.

To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
!!! note
    The code snippets presented in the following sections are not meant for production environments. Please make sure you adapt it for each use-case.

=== "Ethers.js"

    ```js
    import { ethers } from 'ethers';

    // Define the transaction hash to check finality
    const txHash = 'INSERT_TX_HASH';

    // Define the RPC of the provider for Moonbeam
    // This can be adapted for Moonriver or Moonbase Alpha
    const providerRPC = {
      moonbeam: {
        name: 'moonbeam',
        rpc: 'INSERT_RPC_API_ENDPOINT',
        chainId: 1284,
      }
    };

    // Define the Web3 provider
    const web3Provider = new ethers.JsonRpcProvider(providerRPC.moonbeam.rpc, {
      chainId: providerRPC.moonbeam.chainId,
      name: providerRPC.moonbeam.name,
    });

    const main = async () => {
      // Get the last finalized block
      const finalizedBlockHeader = await web3Provider.getBlock('finalized');
      const finalizedBlockNumber = finalizedBlockHeader.number;

      // Get the transaction receipt of the given transaction hash
      const txReceipt = await web3Provider.getTransactionReceipt(txHash);

      // If block number of receipt is not null, compare it against finalized head
      if (txReceipt)`);
        console.log(
          `Your transaction in block ${txBlockNumber} is finalized? ${
            finalizedBlockNumber >= txBlockNumber
          }`
        );
        console.log(
          `Your transaction is indeed in block ${txBlockNumber}? ${txBlock.transactions.includes(
            txHash
          )}`
        );
      } else {
        console.log(
          'Your transaction has not been included in the canonical chain'
        );
      }
    };

    main();
    ```

=== "Web3.js"

    ```js
    import { Web3 } from 'web3';

    // Define the transaction hash to check finality
    const txHash = 'INSERT_TX_HASH';

    // Define the Web3 provider for Moonbeam
    // This can be adapted for Moonriver or Moonbase Alpha
    const web3Provider = new Web3('INSERT_RPC_API_ENDPOINT');

    const main = async () => {
      // Get the last finalized block
      const finalizedBlockHeader = await web3Provider.eth.getBlock('finalized');
      const finalizedBlockNumber = finalizedBlockHeader.number;

      // Get the transaction receipt of the given transaction hash
      const txReceipt = await web3Provider.eth.getTransactionReceipt(txHash);

      // If block number of receipt is not null, compare it against finalized head
      if (txReceipt)`);
        console.log(
          `Your transaction in block ${txBlockNumber} is finalized? ${
            finalizedBlockNumber >= txBlockNumber
          }`
        );
        console.log(
          `Your transaction is indeed in block ${txBlockNumber}? ${txBlock.transactions.includes(
            txHash
          )}`
        );
      } else {
        console.log(
          'Your transaction has not been included in the canonical chain'
        );
      }
    };

    main();
    ```

=== "Web3.py"

    ```py
    from web3 import Web3

    # Define the transaction hash to check finality
    tx_hash = "INSERT_TX_HASH"

    # Define the Web3 provider for Moonbeam
    # This can be adapted for Moonriver or Moonbase Alpha
    web3_provider = Web3(Web3.HTTPProvider("INSERT_RPC_API_ENDPOINT"))

    if __name__ == "__main__":
        # Get the latest finalized block
        finalized_block_header = web3_provider.eth.get_block("finalized")
        finalized_block_number = finalized_block_header.number

        # Get the transaction receipt of the given transaction hash
        tx_receipt = web3_provider.eth.get_transaction_receipt(tx_hash)

        # If block number of receipt is not null, compare it against finalized head
        if tx_receipt is not None:
            tx_block_number = tx_receipt.blockNumber

            # As a safety check, get given block to check if transaction is included
            tx_block = web3_provider.eth.get_block(tx_block_number)
            is_in_block = False
            for tx in tx_block.transactions:
                if tx_hash == web3_provider.to_hex(tx):
                    is_in_block = True

            print(f"Current finalized block number is { str(finalized_block_number) }")
            print(
                f"Your transaction in block { str(tx_block_number) } is finalized? { str(finalized_block_number >= tx_block_number) }"
            )
            print(
                f"Your transaction is indeed in block { str(tx_block_number) }? { is_in_block }"
            )
        else:
            print("Your transaction has not been included in the canonical chain")
    ```

## Check Transaction Finality with Moonbeam RPC Endpoints {: #check-tx-finality-with-moonbeam-rpc-endpoints }

Moonbeam has added support for two custom RPC endpoints, `moon_isBlockFinalized` and `moon_isTxFinalized`, that can be used to check whether an on-chain event is finalized. These methods are a bit more straightforward, as you don't need to compare block numbers to ensure your transaction is finalized.

For more information, you can go to the [Finality RPC Endpoints](/moonbeam-mkdocs/builders/ethereum/json-rpc/moonbeam-custom-api/#rpc-methods) section of the Moonbeam Custom API page.

You can modify the scripts from the Ethereum RPC section above to use `moon_isBlockFinalized` and `moon_isTxFinalized`. To do this, you can make custom calls to the Substrate JSON-RPC using the `send` method of both [Web3.js](https://web3js.readthedocs.io) and [Ethers.js](https://docs.ethers.org/v6). Custom RPC requests are also possible using [Web3.py](https://web3py.readthedocs.io) with the `make_request` method. You'll need to pass in the method name and the parameters to the custom request, which you can find on the [Moonbeam Custom API](/moonbeam-mkdocs/builders/ethereum/json-rpc/moonbeam-custom-api/) page.

???+ code "moon_isBlockFinalized"

    === "Ethers.js"

        ```js
        import { ethers } from 'ethers';

        // Define the block hash to check finality
        const blockHash = 'INSERT_BLOCK_HASH';

        // Define the RPC of the provider for Moonbeam
        // This can be adapted for Moonriver or Moonbase Alpha
        const providerRPC = {
          moonbeam: {
            name: 'moonbeam',
            rpc: 'INSERT_RPC_API_ENDPOINT',
            chainId: 1284,
          },
        };

        // Define the Web3 provider
        const web3Provider = new ethers.JsonRpcProvider(providerRPC.moonbeam.rpc, {
          chainId: providerRPC.moonbeam.chainId,
          name: providerRPC.moonbeam.name,
        });

        // Define the function for the custom web3 request
        const customWeb3Request = async (web3Provider, method, params) => {
          try {
            return await web3Provider.send(method, params);
          } catch (error)
        };

        const main = async () => {
          // Check if the block has been finalized
          const isFinalized = await customWeb3Request(
            web3Provider,
            'moon_isBlockFinalized',
            [blockHash]
          );
          console.log(`Block is finalized? ${isFinalized}`);
        };

        main();
        ```

    === "Web3.js"

        ```js
        import { Web3 } from 'web3';

        // Define the block hash to check finality
        const blockHash = 'INSERT_BLOCK_HASH';

        // Define the Web3 provider for Moonbeam
        // This can be adapted for Moonriver or Moonbase Alpha
        const web3Provider = new Web3('INSERT_RPC_API_ENDPOINT');

        // Define the function for the custom Web3 request
        const customWeb3Request = async (web3Provider, method, params) => {
          try {
            return await requestPromise(web3Provider, method, params);
          } catch (error)
        };

        // In Web3.js you need to return a promise
        const requestPromise = async (web3Provider, method, params) => {
          return new Promise((resolve, reject) => {
            web3Provider.send(
              {
                jsonrpc: '2.0',
                id: 1,
                method,
                params,
              },
              (error, result) => {
                if (error) else {
                  if (result.error)
                  resolve(result);
                }
              }
            );
          });
        };

        const main = async () => {
          // Check if the block has been finalized
          const isFinalized = await customWeb3Request(
            web3Provider.currentProvider,
            'moon_isBlockFinalized',
            [blockHash]
          );

          console.log(JSON.stringify(isFinalized));
          console.log(`Block is finalized? ${isFinalized.result}`);
        };

        main();
        ```

    === "Web3.py"

        ```py
        from web3 import Web3

        # Define the block hash to check finality
        block_hash = 'INSERT_BLOCK_HASH'

        # Set the RPC_address for Moonbeam
        # This can also be adapted for Moonriver or Moonbase Alpha
        RPC_address = 'INSERT_RPC_API_ENDPOINT'

        # Define the Web3 provider
        web3_provider = Web3(Web3.HTTPProvider(RPC_address))

        # Asynchronous JSON-RPC API request
        def custom_web3_request(method, params):
            response = web3_provider.provider.make_request(method, params)
            return response

        if __name__ == "__main__":
            # Check if the block has been finalized
            is_finalized = custom_web3_request(
               'moon_isBlockFinalized', [block_hash])
            print(
                f'Block is finalized? { is_finalized["result"] }')
        ```

??? code "moon_isTxFinalized"

    === "Ethers.js"

        ```js
        import { ethers } from 'ethers';

        // Define the transaction hash to check finality
        const txHash = 'INSERT_TRANSACTION_HASH';

        // Define the RPC of the provider for Moonbeam
        // This can be adapted for Moonriver or Moonbase Alpha
        const providerRPC = {
          moonbeam: {
            name: 'moonbeam',
            rpc: 'INSERT_RPC_API_ENDPOINT',
            chainId: 1284,
          },
        };

        // Define the Web3 provider
        const web3Provider = new ethers.JsonRpcProvider(providerRPC.moonbeam.rpc, {
          chainId: providerRPC.moonbeam.chainId,
          name: providerRPC.moonbeam.name,
        });

        // Define the function for the custom web3 request
        const customWeb3Request = async (web3Provider, method, params) => {
          try {
            return await web3Provider.send(method, params);
          } catch (error)
        };

        const main = async () => {
          // Check if the transaction has been finalized
          const isFinalized = await customWeb3Request(
            web3Provider,
            'moon_isTxFinalized',
            [txHash]
          );
          console.log(`Transaction is finalized? ${isFinalized}`);
        };

        main();
        ```

    === "Web3.js"

        ```js
        import Web3 from 'web3';

        // Define the transaction hash to check finality
        const txHash = 'INSERT_TRANSACTION_HASH';

        // Define the Web3 provider for Moonbeam
        // This can be adapted for Moonriver or Moonbase Alpha
        const web3Provider = new Web3('INSERT_RPC_API_ENDPOINT');

        // Define the function for the custom Web3 request
        const customWeb3Request = async (web3Provider, method, params) => {
          try {
            return await requestPromise(web3Provider, method, params);
          } catch (error)
        };

        // In Web3.js you need to return a promise
        const requestPromise = async (web3Provider, method, params) => {
          return new Promise((resolve, reject) => {
            web3Provider.send(
              {
                jsonrpc: '2.0',
                id: 1,
                method,
                params,
              },
              (error, result) => {
                if (error) else {
                  if (result.error)
                  resolve(result);
                }
              }
            );
          });
        };

        const main = async () => {
          // Check if the transaction has been finalized
          const isFinalized = await customWeb3Request(
            web3Provider.currentProvider,
            'moon_isTxFinalized',
            [txHash]
          );

          console.log(JSON.stringify(isFinalized));
          console.log(`Transaction is finalized? ${isFinalized}`);
        };

        main();
        ```

    === "Web3.py"

        ```py
        from web3 import Web3

        # Define the transaction hash to check finality
        tx_hash = 'INSERT_BLOCK_HASH'

        # Set the RPC_address for Moonbeam
        # This can also be adapted for Moonriver or Moonbase Alpha
        RPC_address = 'INSERT_RPC_API_ENDPOINT'

        # Define the Web3 provider
        web3_provider = Web3(Web3.HTTPProvider(RPC_address))

        # Asynchronous JSON-RPC API request
        def custom_web3_request(method, params):
            response = web3_provider.provider.make_request(method, params)
            return response

        if __name__ == "__main__":
            # Check if the transaction has been finalized
            is_finalized = custom_web3_request(
               'moon_isTxFinalized', [tx_hash])
            print(
                f'Transaction is finalized? { is_finalized["result"] }')
        ```

## Check Transaction Finality with Substrate RPC Endpoints {: #check-tx-finality-with-substrate-rpc-endpoints }

Using the following three RPC requests from the Substrate JSON-RPC, you can fetch the current finalized block and compare it with the block number of the transaction you want to check finality for:

- `chain_getFinalizedHead` - the first request gets the block hash of the last finalized block
- `chain_getHeader` - the second request gets the block header for a given block hash
- `eth_getTransactionReceipt` - this retrieves the transaction receipt given the transaction hash

The [Polkadot.js API package](/moonbeam-mkdocs/builders/substrate/libraries/polkadot-js-api/) and [Python Substrate Interface package](/moonbeam-mkdocs/builders/substrate/libraries/py-substrate-interface/) provide developers with a way to interact with Substrate chains using JavaScript and Python.

You can find more information about Polkadot.js and the Substrate JSON-RPC in the [official Polkadot.js documentation site](https://polkadot.js.org/docs/substrate/rpc), and more about Python Substrate Interface in the [official PySubstrate documentation site](https://jamdottech.github.io/py-polkadot-sdk/).

=== "Polkadot.js"

    ```js
    import { ApiPromise, WsProvider } from '@polkadot/api';
    import { types } from 'moonbeam-types-bundle';

    // Define the transaction hash to check finality
    const txHash = 'INSERT_TX_HASH';

    // Define the provider for Moonbeam
    // This can be adapted for Moonriver or Moonbase Alpha
    const wsProvider = new WsProvider('INSERT_WSS_API_ENDPOINT');

    const main = async () => {
      // Create the provider using Moonbeam types
      const polkadotApi = await ApiPromise.create({
        provider: wsProvider,
        typesBundle: types,
      });
      await polkadotApi.isReady;

      // Get the latest finalized block of the Substrate chain
      const finalizedHeadHash = (
        await polkadotApi.rpc.chain.getFinalizedHead()
      ).toJSON();

      // Get finalized block header to retrieve number
      const finalizedBlockHeader = (
        await polkadotApi.rpc.chain.getHeader(finalizedHeadHash)
      ).toJSON();

      // Get the transaction receipt of the given tx hash
      const txReceipt = (
        await polkadotApi.rpc.eth.getTransactionReceipt(txHash)
      ).toJSON();

      // You can not verify if the tx is in the block because polkadotApi.rpc.eth.getBlockByNumber
      // does not return the list of tx hashes

      // If block number of receipt is not null, compare it against finalized head
      if (txReceipt)`
        );
        console.log(
          `Your transaction in block ${txReceipt.blockNumber} is finalized? ${
            finalizedBlockHeader.number >= txReceipt.blockNumber
          }`
        );
      } else {
        console.log(
          'Your transaction has not been included in the canonical chain'
        );
      }

      polkadotApi.disconnect();
    };

    main();
    ```

=== "py-substrate-interface"

    ```py
    from substrateinterface import SubstrateInterface

    # Define the Ethereum transaction hash to check finality
    tx_hash = "INSERT_TX_HASH"

    # Point API provider to Moonbeam
    # This can be adapted for Moonriver or Moonbase Alpha
    moonbeam_API_provider = SubstrateInterface(
        url="INSERT_WSS_API_ENDPOINT",
    )

    if __name__ == "__main__":
        # Get the latest finalized block header of the chain
        finalized_block_header = moonbeam_API_provider.get_block_header(finalized_only=True)
        # Get the finalized block number from the block header
        finalized_block_number = finalized_block_header["header"]["number"]
        # Get the transaction receipt of the given transaction hash through a
        # custom RPC request
        tx_receipt = moonbeam_API_provider.rpc_request(
            "eth_getTransactionReceipt", [tx_hash]
        )

        # Check if tx_receipt is null
        if tx_receipt is None:
            print("The transaction hash cannot be found in the canonical chain.")
        else:
            # Get the block number of the transaction
            tx_block_number = int(tx_receipt["result"]["blockNumber"], 16)
            # Get the transaction block through a custom RPC request
            tx_block = moonbeam_API_provider.rpc_request(
                "eth_getBlockByNumber", [tx_block_number, False]
            )

            print(f"Current finalized block number is { str(finalized_block_number) }")
            print(
                f"Your transaction in block { str(tx_block_number) } is finalized? { str(finalized_block_number >= tx_block_number) }"
            )
            print(
                f'Your transaction is indeed in block { str(tx_block_number) }? { str(tx_hash in tx_block["result"]["transactions"]) }'
            )
    ```

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
