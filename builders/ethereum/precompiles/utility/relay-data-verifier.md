---
title: Relay Data Verifier Precompile Contract
description: Learn how to verify data availability and authenticity on the relay chain via a Solidity interface with Moonbeam's Relay Data Verifier Precompile contract.
categories:
- Precompiles
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/precompiles/utility/relay-data-verifier/
word_count: 2063
token_estimate: 3497
version_hash: sha256:60f951f194507c0e8ada312ec531626055d6082818d2b5eb53d3a79eb9d3f593
last_updated: '2026-05-21T21:21:53+00:00'
---

# Interacting with the Relay Data Verifier Precompile

## Introduction {: #introduction }

Polkadot relies on state proofs to guarantee data integrity at a particular time. A state proof is a concise, cryptographic data structure representing a specific subset of transactions or state data within a trie. It consists of a set of hashes that form a path from the target data to the root hash stored in the block header.

A client can independently reconstruct the root hash and compare it with the original stored in the block header by providing a state proof. If the reconstructed root hash matches the original, it confirms the target data's authenticity, validity, and inclusion within the blockchain.

Polkadot's unique architecture and parachain block validation process means blockchains like Moonbeam have the relay chain storage root hash in their state. Consequently, Moonbeam can provide a mechanism to verify a relay chain state by checking the proof against the stored storage root hash.

Moonbeam's [relay data verifier precompiled](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/relay-data-verifier/RelayDataVerifier.sol) contract provides an easy way for smart contracts to programmatically build functions that rely on verifying relay chain state in contract calls. Consequently, no oracles are needed to feed relay chain data to Moonbeam. This functionality is readily available at the following contract addresses:

=== "Moonbeam"

     ```text
     0x0000000000000000000000000000000000000819
     ```

=== "Moonriver"

     ```text
     0x0000000000000000000000000000000000000819
     ```

=== "Moonbase Alpha"

     ```text
     0x0000000000000000000000000000000000000819
     ```

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## The Relay Data Verifier Solidity Interface {: #the-relay-data-verifier-solidity-interface }

[`RelayDataVerifier.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/relay-data-verifier/RelayDataVerifier.sol) is a Solidity interface that allows developers to interact with the precompile's methods.

??? code "RelayDataVerifier.sol"

    ```solidity
    // SPDX-License-Identifier: GPL-3.0-only
    pragma solidity >=0.8.3;

    /// @dev The RelayDataVerifier contract's address.
    address constant RELAY_DATA_VERIFIER_ADDRESS = 0x0000000000000000000000000000000000000819;

    /// @dev The RelayDataVerifier contract's instance.
    RelayDataVerifier constant RELAY_DATA_VERIFIER_CONTRACT = RelayDataVerifier(
        RELAY_DATA_VERIFIER_ADDRESS
    );

    /// @author The Moonbeam Team
    /// @title Relay Proof Verifier Interface
    /// @dev The interface that Solidity contracts use to interact with the Relay Proof Verifier
    /// precompile.
    /// A typical workflow to verify relay chain data is the following:
    /// 1. Moonbeam RPC Call: Call `latestRelayBlockNumber` function to get the latest relay
    ///    block number tracked by the chain in `pallet-storage-root`.
    /// 2. Relay RPC Call: Call `chain_getBlockHash(blockNumber)` RPC method to get the relay block hash
    ///    for the block number obtained in step 1.
    /// 3. Relay RPC Call: Call `state_getReadProof(keys, at)` RPC method where `at`
    ///    is the relay block hash obtained in step 2 to get the 'ReadProof` of the entries.
    /// 4. Moonbeam RPC Call: Submit an ethereum transaction (directly or through a SC) to call the
    ///    `verifyEntry` or `verifyEntries` function to verify the data against the relay block
    ///    number. The call data contain the relay block number obtained in step 1, and the read
    ///    proof generated in step 3, along with the key/s to verify.
    /// @custom:address 0x0000000000000000000000000000000000000819
    interface RelayDataVerifier {
        /// @dev ReadProof struct returned by the `state_getReadProof` RPC method.
        struct ReadProof {
            // The block hash against which the proof is generated
            bytes32 at;
            /// The storage proof
            bytes[] proof;
        }

        /// @dev Verifies a storage entry in the Relay Chain using a relay block number and a storage
        /// proof. This function takes a relay block number, a storage proof, and the key of the storage
        /// entry to verify. It returns the value associated with the key if the verification is
        /// successful.
        /// @custom:selector 27001faa
        /// @param relayBlockNumber The relay block number against which the entry is being verified.
        /// @param readProof The storage proof used to verify the entry.
        /// @param key The key of the storage entry to verify.
        /// @return value The value associated with the key, returned as a bytes array.
        function verifyEntry(
            uint32 relayBlockNumber,
            ReadProof calldata readProof,
            bytes calldata key
        ) external returns (bytes memory value);

        /// @dev Verifies a set of entries in the Relay Chain and returns the corresponding values.
        /// This function takes a relay block number, a storage proof, and an array of keys for the
        /// storage entries to verify. It returns an array of values associated with the keys, in the
        /// same order as the keys.
        /// @custom:selector 2da33a45
        /// @param relayBlockNumber The relay block number for which the data is being verified.
        /// @param readProof The storage proof used to verify the data.
        /// @param keys The keys of the storage entries to verify.
        /// @return values The values associated with the keys, returned in the same order as the keys.
        function verifyEntries(
            uint32 relayBlockNumber,
            ReadProof calldata readProof,
            bytes[] calldata keys
        ) external returns (bytes[] memory values);

        /// @dev Returns the latest relay block number that has a storage root stored on-chain.
        /// @custom:selector aed36869
        /// @return relayBlockNumber the lastest relay block number
        function latestRelayBlockNumber()
            external
            view
            returns (uint32 relayBlockNumber);
    }
    ```

The interface includes the following functions:

???+ function "**latestRelayBlockNumber**() — retrieves the most recent relay chain block that has its storage root stored on the blockchain itself"

    === "Parameters"

        None

    === "Returns"

        The latest relay block number that has a storage root stored on-chain.

??? function "**verifyEntry**(_uint32_ relayBlockNumber, _ReadProof_ calldata readProof, _bytes_ callData key) — verifies a storage entry in the relay chain using a relay block number, a storage proof, and the storage key. It returns the value associated with the key if the verification is successful"

    === "Parameters"

        - `relayBlockNumber` - the relay block number for which the data is being verified. The latest relay block number can be obtained from the `latestRelayBlockNumber()` function
        - `readProof` - a struct defined in the precompile contract, containing the storage proof used to verify the data. The `ReadProof` struct is defined as:
          ```
          struct ReadProof {
              // The block hash against which the proof is generated
              bytes32 at;
              /// The storage proof
              bytes[] proof;
          }
          ```
        - `key` - the storage key for the generated proof
    
    === "Returns"

        When performing a [static call](https://docs.ethers.org/v6/api/contract/#BaseContractMethod-staticCall) on the `verifyEntry` function, you can view the returned value associated with the key in hexadecimal format.

        ```js
         
        '0x01000000040000000100000000000000f88ce384dca20000000000000000000000370589030a0000000000000000000000203d88792d0000000000000000000000000000000000000000000000000080'
        ```

??? function "**verifyEntries**(_uint32_ relayBlockNumber, _ReadProof_ calldata readProof, _bytes[]_ callData keys) — verifies a set of entries in the relay chain and returns the corresponding values. This function takes a relay block number, a storage proof, and an array of storage keys to verify. It returns an array of values associated with the keys, in the same order as the keys"

    === "Parameters"

        - `relayBlockNumber` - the relay block number for which the data is being verified. The latest relay block number can be obtained from the `latestRelayBlockNumber()` function
        - `readProof` - a struct defined in the precompile contract, containing the storage proof used to verify the data. The `ReadProof` struct is defined as:
        ```
        struct ReadProof {
            // The block hash against which the proof is generated
            bytes32 at;
            /// The storage proof
            bytes[] proof;
        }
        ```
        - `keys` - the storage keys for the generated proof

    === "Returns"

        When performing a [static call](https://docs.ethers.org/v6/api/contract/#BaseContractMethod-staticCall) on the `verifyEntries` function, you can view an array containing the corresponding values mapped to their respective keys, represented in hexadecimal format.

        ```js
         
        ['0x01000000040000000100000000000000f88ce384dca20000000000000000000000370589030a0000000000000000000000203d88792d0000000000000000000000000000000000000000000000000080']
        ```

## Interact with the Solidity Interface {: #interact-with-the-solidity-interface }

A typical workflow to verify relay chain data involves the following steps:

1. **Moonbeam RPC call** - call the `latestRelayBlockNumber` function to get the latest relay block number tracked by the chain in the `pallet-storage-root`
2. **Relay RPC call** - call the `chain_getBlockHash(blockNumber)` RPC method to get the relay block hash for the block number obtained in step one
3. **Relay RPC call** - call the `state_getReadProof(keys, at)` RPC method to retrieve the storage proof, where `at` is the relay block hash obtained in step two, and `keys` is an array of strings which contains the keys for target storage items. For `@polkadot/api`, it can be obtained via `api.query.module.key()` function
4. **Moonbeam RPC call** - submit an Ethereum transaction to call the `verifyEntry` or `verifyEntries` function to verify the data against the relay block number. The call data should contain the relay block number obtained in step one, the read proof generated in step three, and the key(s) to verify

The following sections will cover how to interact with the Relay Data Verifier Precompile using Ethereum libraries, such as Ethers.js and Web3.py. The examples in this guide will be on Moonbase Alpha.

### Checking Prerequisites {: #checking-prerequisites }

To follow along with this tutorial, you will need to have:

- Create or have an account on Moonbase Alpha to test out the different features in the precompile
- The account will need to be funded with `DEV` tokens. 
 You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
### Using Ethereum Libraries {: #using-ethereum-libraries }

To interact with the Solidity interface using an Ethereum library, you'll need the precompile's ABI (Application Binary Interface). The ABI for the Relay Chain Data Verifier Precompile is as follows:

??? code "Relay Data Verifier Precompile ABI"

    ```js
    [
      {
        inputs: [],
        name: 'latestRelayBlockNumber',
        outputs: [
          {
            internalType: 'uint32',
            name: 'relayBlockNumber',
            type: 'uint32',
          },
        ],
        stateMutability: 'view',
        type: 'function',
      },
      {
        inputs: [
          {
            internalType: 'uint32',
            name: 'relayBlockNumber',
            type: 'uint32',
          },
          {
            components: [
              {
                internalType: 'bytes32',
                name: 'at',
                type: 'bytes32',
              },
              {
                internalType: 'bytes[]',
                name: 'proof',
                type: 'bytes[]',
              },
            ],
            internalType: 'struct RelayDataVerifier.ReadProof',
            name: 'readProof',
            type: 'tuple',
          },
          {
            internalType: 'bytes[]',
            name: 'keys',
            type: 'bytes[]',
          },
        ],
        name: 'verifyEntries',
        outputs: [
          {
            internalType: 'bytes[]',
            name: 'values',
            type: 'bytes[]',
          },
        ],
        stateMutability: 'nonpayable',
        type: 'function',
      },
      {
        inputs: [
          {
            internalType: 'uint32',
            name: 'relayBlockNumber',
            type: 'uint32',
          },
          {
            components: [
              {
                internalType: 'bytes32',
                name: 'at',
                type: 'bytes32',
              },
              {
                internalType: 'bytes[]',
                name: 'proof',
                type: 'bytes[]',
              },
            ],
            internalType: 'struct RelayDataVerifier.ReadProof',
            name: 'readProof',
            type: 'tuple',
          },
          {
            internalType: 'bytes',
            name: 'key',
            type: 'bytes',
          },
        ],
        name: 'verifyEntry',
        outputs: [
          {
            internalType: 'bytes',
            name: 'value',
            type: 'bytes',
          },
        ],
        stateMutability: 'nonpayable',
        type: 'function',
      },
    ];
    ```

Once you have the ABI, you can interact with the precompile using the Ethereum library of your choice, such as [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/) or [Web3.py](/moonbeam-mkdocs/builders/ethereum/libraries/web3py/). The general steps are as follows:

1. Create a provider
2. Create a contract instance of the precompile
3. Interact with the precompile's functions

The provided code example demonstrates how to use the Ethers.js library to interact with the Moonbase Alpha network and its relay chain, verifying a data entry using the `verifyEntry` function.

!!! note
     The code snippets presented in the following sections are not meant for production environments. Please make sure you adapt it for each use case.

=== "Ethers.js"

     ```js
     // For reading local ABI file
     import * as fs from 'fs';
     // Import Ethers library, to interact with Moonbeam networks
     import { ethers } from 'ethers';
     // Import Polkadot library, to interact with relay chain
     import { ApiPromise, WsProvider } from '@polkadot/api';

     const abi = JSON.parse(fs.readFileSync('./RelayChainDataVerifierABI.json'));
     const privateKey = 'INSERT_PRIVATE_KEY';
     const precompileAddress = '0x0000000000000000000000000000000000000819';
     const moonbeamURL = 'https://rpc.api.moonbase.moonbeam.network';
     const relayURL = 'wss://relay.api.moonbase.moonbeam.network';

     // Create Ethers provider and signer
     const provider = new ethers.JsonRpcProvider(moonbeamURL);
     const signer = new ethers.Wallet(privateKey, provider);
     const precompileContract = new ethers.Contract(precompileAddress, abi, signer);

     async function run());

       // Get the storage key for a random account on relay chain
       const key = api.query.system.account.key(
         '5CBATpb3yvEM4mhX9Dw3tyuqiWKhq9YBG6ugSbodRUSbodoU'
       );
       // Find the latest available relay chain block number from Moonbeam
       const blockNum = await precompileContract.latestRelayBlockNumber();

       // Get the block hash and storage proof from relay chain
       const blockHash = await api.rpc.chain.getBlockHash(blockNum);
       const proof = await api.rpc.state.getReadProof([key], blockHash);

       // This tx will be rejected if the verification failed
       const receipt = await precompileContract.verifyEntry(blockNum, proof, key);
       await receipt.wait();
       console.log(receipt.hash);
     }

     await run();
     ```

=== "Web3.py"

     ```py
     # Import packages
     from eth_account import Account
     from substrateinterface import SubstrateInterface
     from web3 import Web3

     # Initialize variables
     abi = INSERT_ABI

     privateKey = "INSERT_PRIVATE_KEY"
     precompileAddress = "0x0000000000000000000000000000000000000819"
     moonbeamURL = "https://rpc.api.moonbase.moonbeam.network"
     relayURL = "wss://relay.api.moonbase.moonbeam.network"

     # Create provider for Moonbeam network
     web3 = Web3(Web3.HTTPProvider(moonbeamURL))
     account = Account.from_key(privateKey)
     precompileContract = web3.eth.contract(address=precompileAddress, abi=abi)

     # Create provider for relay chain
     substrate = SubstrateInterface(url=relayURL)

     # Get storage key
     key = substrate.generate_storage_hash(
         storage_module="System",
         storage_function="Account",
         params=["5CBATpb3yvEM4mhX9Dw3tyuqiWKhq9YBG6ugSbodRUSbodoU"],
     )

     # Find the latest available relay chain block number from Moonbeam
     blockNum = precompileContract.functions.latestRelayBlockNumber().call()

     # Get the block hash from relay chain
     blockHash = substrate.get_block_hash(blockNum)

     # Get the storage proof from relay chain
     response = substrate.rpc_request("state_getReadProof", [[key], blockHash])
     proof = response["result"]

     # Call smart contract
     tx = precompileContract.functions.verifyEntry(blockNum, proof, key).build_transaction(
         {
             "from": Web3.to_checksum_address(account.address),
             "nonce": web3.eth.get_transaction_count(
                 Web3.to_checksum_address(account.address)
             ),
         }
     )
     tx_create = web3.eth.account.sign_transaction(tx, privateKey)
     tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
     tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
     ```
