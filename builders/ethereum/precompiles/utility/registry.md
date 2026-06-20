---
title: Precompile Registry
description: Learn how to access and interact with the Precompile Registry on Moonbeam, which can be used to check if a given address is a precompile and if it is supported.
categories:
- Precompiles
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/precompiles/utility/registry/
word_count: 1483
token_estimate: 2600
version_hash: sha256:e5184a73710ad561e58d0ee053bd3abf0bcbcf15725cc88ecf23bdea9e2d28d2
last_updated: '2026-05-21T21:21:53+00:00'
---

# Precompile Registry on Moonbeam

## Introduction {: #introduction }

The Precompile Registry serves as a single source of truth for the available [precompiles on Moonbeam](/moonbeam-mkdocs/builders/ethereum/precompiles/overview/). The Precompile Registry can be used to determine if an address corresponds to a precompile and whether or not a precompile is active or deprecated. This is particularly useful when there are upstream changes within the Substrate and Polkadot ecosystems that result in backward-incompatible changes to precompiles. Developers can design an exit strategy to ensure their dApp recovers gracefully in these scenarios.

The Precompile Registry also serves an additional purpose, as it allows any user to set "dummy code" (`0x60006000fd`) for precompiles, which makes precompiles callable from Solidity. This is necessary as precompiles on Moonbeam, by default, don't have bytecode. The "dummy code" can bypass checks in Solidity that ensure contract bytecode exists and is non-empty.

The Registry Precompile is located at the following address:

=== "Moonbeam"

     ```text
     0x0000000000000000000000000000000000000815
     ```

=== "Moonriver"

     ```text
     0x0000000000000000000000000000000000000815
     ```

=== "Moonbase Alpha"

     ```text
     0x0000000000000000000000000000000000000815
     ```

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## The Precompile Registry Solidity Interface {: #the-solidity-interface }

[`PrecompileRegistry.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/precompile-registry/PrecompileRegistry.sol) is a Solidity interface that allows developers to interact with the precompile's methods.

??? code "PrecompileRegistry.sol"

    ```solidity
    // SPDX-License-Identifier: GPL-3.0-only
    pragma solidity >=0.8.3;

    /// @dev The Precompile Registry contract's address.
    address constant PRECOMPILE_REGISTRY_ADDRESS = 0x0000000000000000000000000000000000000815;

    /// @dev The Precompile Registry contract's instance.
    PrecompileRegistry constant PRECOMPILE_REGISTRY_CONTRACT = PrecompileRegistry(PRECOMPILE_REGISTRY_ADDRESS);

    /// @author The Moonbeam Team
    /// @title Precompile Registry
    /// @dev Interface to the set of available precompiles.
    interface PrecompileRegistry {
        /// @dev Query if the given address is a precompile. Note that deactivated precompiles
        /// are still considered precompiles and will return `true`.
        /// @param a: Address to query
        /// @return output Is this address a precompile?
        /// @custom:selector 446b450e
        function isPrecompile(address a) external view returns (bool);

        /// @dev Query if the given address is an active precompile. Will return false if the
        /// address is not a precompile or if this precompile is deactivated.
        /// @param a: Address to query
        /// @return output Is this address an active precompile?
        /// @custom:selector 6f5e23cf
        function isActivePrecompile(address a) external view returns (bool);

        /// @dev Update the account code of a precompile address.
        /// As precompiles are implemented inside the Runtime, they don't have a bytecode, and
        /// their account code is empty by default. However in Solidity calling a function of a
        /// contract often automatically adds a check that the contract bytecode is non-empty.
        /// For that reason a dummy code (0x60006000fd) can be inserted at the precompile address
        /// to pass that check. This function allows any user to insert that code to precompile address
        /// if they need it.
        /// @param a: Address of the precompile.
        /// @custom:selector 48ceb1b4
        function updateAccountCode(address a) external;
    }
    ```

The interface includes the following functions:

??? function "**isPrecompile**(*address* a) - returns a boolean indicating whether a given address is a precompile or not. Returns `true` for active and deprecated precompiles"

    === "Parameters"

        - `a` - address to check if it is a precompile

    === "Returns"

        - `bool` whether the address is a precompile (active or deprecated)

??? function "**isActivePrecompile**(*address* a) - returns a boolean indicating whether a given address is an active precompile or not. Returns `false` if a precompile has been deprecated"

    === "Parameters"

        - `a` - address to check if it is an active precompile

    === "Returns"

        - `bool` whether the address is an active precompile

??? function "**updateAccountCode**(*address* a) - updates a given precompile's bytecode with dummy code (`0x60006000fd`) given the address of the precompile. Precompiles, by default, don't have bytecode associated with them. This function can be used to add dummy bytecode to bypass requirements in Solidity that check if a contract's bytecode is not empty before its functions can be called"

    === "Parameters"

        - `a` - address of the precompile to update with dummy bytecode

    === "Returns"

        None.

## Interact with the Precompile Registry Solidity Interface {: #interact-with-precompile-registry-interface }

The following sections will cover how to interact with the Registry Precompile from [Remix](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) and [Ethereum libraries](/moonbeam-mkdocs/builders/ethereum/libraries/), such as [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/) and [Web3.py](/moonbeam-mkdocs/builders/ethereum/libraries/web3py/).

The examples in this guide will be on Moonbase Alpha.
To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
### Use Remix to Interact with the Precompile Registry {: #use-remix }

To quickly get started with [Remix](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/), the [Precompile Registry contract has been loaded from GitHub](https://remix.ethereum.org/#url=https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/precompile-registry/PrecompileRegistry.sol). You can also create a new file in Remix and manually paste in the contents of the [`PrecompileRegistry.sol`](#the-solidity-interface) contract.

![Add the Precompile Registry Interface to Remix](/moonbeam-mkdocs/images/builders/ethereum/precompiles/utility/registry/registry-1.webp)

Then you can take the following steps to compile, deploy, and interact with the Precompile Registry:

1. From the **Compile** tab, click on **Compile PrecompileRegistry.sol** to compile the contract.  A green checkmark will appear upon successfully compiling the contract

    ![Compile the Precompile Registry contract](/moonbeam-mkdocs/images/builders/ethereum/precompiles/utility/registry/registry-2.webp)

2. From the **Deploy and run transactions** tab, you can load the Precompile Registry using its address:

    1. Make sure **Injected Provider - Metamask** is selected in the **ENVIRONMENT** drop down and you've connected MetaMask to Moonbase Alpha
    2. Ensure **PrecompileRegistry** is selected in the **CONTRACT** dropdown. Since this is a precompiled contract there is no need to deploy, instead you are going to provide the address of the Precompile in the **At Address** field
    3. Provide the address of the Precompile Registry for Moonbase Alpha: `0x0000000000000000000000000000000000000815` and click **At Address**
    4. The Precompile Registry will appear in the list of **Deployed Contracts**

    ![Access the Precompile Registry contract](/moonbeam-mkdocs/images/builders/ethereum/precompiles/utility/registry/registry-3.webp)

3. You can interact with any of the precompile's methods. Under **Deployed Contracts**, expand the Precompile Registry to view the list of methods. For example, you can use the **isPrecompile** function to check if an address is a precompile

    ![Interact with the Precompile Registry contract](/moonbeam-mkdocs/images/builders/ethereum/precompiles/utility/registry/registry-4.webp)

### Use Ethereum Libraries to Interact with the Precompile Registry {: #use-ethereum-libraries }

To interact with the Precompile Registry's Solidity interface with an Ethereum library, you'll need the Precompile Registry's ABI.

??? code "Precompile Registry ABI"

    ```js
    [
    	{
    		"inputs": [
    			{
    				"internalType": "address",
    				"name": "a",
    				"type": "address"
    			}
    		],
    		"name": "isActivePrecompile",
    		"outputs": [
    			{
    				"internalType": "bool",
    				"name": "",
    				"type": "bool"
    			}
    		],
    		"stateMutability": "view",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "address",
    				"name": "a",
    				"type": "address"
    			}
    		],
    		"name": "isPrecompile",
    		"outputs": [
    			{
    				"internalType": "bool",
    				"name": "",
    				"type": "bool"
    			}
    		],
    		"stateMutability": "view",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "address",
    				"name": "a",
    				"type": "address"
    			}
    		],
    		"name": "updateAccountCode",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	}
    ]
    ```

Once you have the ABI, you can interact with the Registry using the Ethereum library of your choice. Generally speaking, you'll take the following steps:

1. Create a provider
2. Create a contract instance of the Precompile Registry
3. Interact with the Precompile Registry's functions

!!! remember
    The following snippets are for demo purposes only. Never store your private keys in a JavaScript or Python file.

=== "Ethers.js"

    ```js
    import { ethers } from 'ethers'; // Import Ethers library
    import ABI from './precompileRegistryABI.js'; // Import Precompile Registry ABI

    const privateKey = 'INSERT_PRIVATE_KEY';

    // Create Ethers provider and signer
    const provider = new ethers.JsonRpcProvider(
      'https://rpc.api.moonbase.moonbeam.network'
    );
    const signer = new ethers.Wallet(privateKey, provider);

    // Create interface for the Precompile Registry
    const precompileRegistry = new ethers.Contract(
      '0x0000000000000000000000000000000000000815',
      ABI,
      signer
    );

    // Interact with the Precompile Registry
    const isActivePrecompile = async () => {
      const proxyPrecompile = '0x000000000000000000000000000000000000080b';

      // Check if the Proxy Precompile is a precompile
      const isPrecompile = await precompileRegistry.isPrecompile(proxyPrecompile);
      // Should return 'Address is a precompile: true'
      console.log(`Address is a precompile: ${isPrecompile}`);

      // Check if the Proxy Precompile is an active precompile
      const isActivePrecompile = await precompileRegistry.isActivePrecompile(
        proxyPrecompile
      );
      // Should return 'Address is an active precompile: true'
      console.log(`Address is an active precompile: ${isActivePrecompile}`);
    };

    isActivePrecompile();
    ```

=== "Web3.py"

    ```py
    from web3 import Web3

    abi = "INSERT_PRECOMPILE_REGISTRY_ABI"  # Paste or import the Precompile Registry ABI
    private_key = "INSERT_PRIVATE_KEY"

    # Create provider
    web3 = Web3(Web3.HTTPProvider("https://rpc.api.moonbase.moonbeam.network"))

    # Create interface for the Precompile Registry
    precompile_registry = web3.eth.contract(
        address="0x0000000000000000000000000000000000000815", abi=abi
    )


    # Interact with the Precompile Registry
    def is_active_precompile():
        proxy_precompile = "0x000000000000000000000000000000000000080b"

        # Check if the Proxy Precompile is a precompile
        is_precompile = precompile_registry.functions.isPrecompile(proxy_precompile).call()
        # Should return 'Address is a precompile: true'
        print("Address is a precompile: ", is_precompile)

        # Check if the Proxy Precompile is an active precompile
        is_active_precompile = precompile_registry.functions.isActivePrecompile(
            proxy_precompile
        ).call()
        # Should return 'Address is an active precompile: true'
        print("Address is an active precompile: ", is_active_precompile)


    is_active_precompile()
    ```
