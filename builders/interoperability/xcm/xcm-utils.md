---
title: XCM Utilities Precompile Contract
description: Learn the various XCM related utility functions available to smart contract developers with Moonbeam's precompiled XCM Utilities contract.
categories:
- XCM
url: https://docs.moonbeam.network/builders/interoperability/xcm/xcm-utils/
word_count: 632
token_estimate: 1008
version_hash: sha256:f4f08c7151d832f301cdf6217c49dceb132262ab82e418ec703ccf29d071f1da
last_updated: '2026-05-21T21:21:53+00:00'
---

# Interacting with the XCM Utilities Precompile

## Introduction {: #xcmutils-precompile}

The XCM Utilities Precompile contract gives developers XCM-related utility functions directly within the EVM. This allows for easier transactions and interactions with other XCM-related precompiles.

Similar to other [precompile contracts](/moonbeam-mkdocs/builders/ethereum/precompiles/), the XCM Utilities Precompile is located at the following addresses:

=== "Moonbeam"

     ```text
     0x000000000000000000000000000000000000080C
     ```

=== "Moonriver"

     ```text
     0x000000000000000000000000000000000000080C
     ```

=== "Moonbase Alpha"

     ```text
     0x000000000000000000000000000000000000080C
     ```

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## The XCM Utilities Solidity Interface {: #xcmutils-solidity-interface }

[XcmUtils.sol](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-utils/XcmUtils.sol) is an interface to interact with the precompile.

!!! note
    The precompile will be updated in the future to include additional features. Feel free to suggest additional utility functions in the [Discord](https://discord.com/invite/PfpUATX).

The interface includes the following functions:

 - **multilocationToAddress**(*Multilocation memory* multilocation) — read-only function that returns the Computed Origin account from a given multilocation
 - **weightMessage**(*bytes memory* message) — read-only function that returns the weight that an XCM message will consume on the chain. The message parameter must be a SCALE encoded XCM versioned XCM message
 - **getUnitsPerSecond**(*Multilocation memory* multilocation) — read-only function that gets the units per second for a given asset in the form of a `Multilocation`. The multilocation must describe an asset that can be supported as a fee payment, such as an [external XC-20](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/#external-xc20s), or else this function will revert. 

    !!! note
        Note that this function still returns units per second data but units per second has been deprecated and replaced by the calculation of relative price. See [XC asset registration](/moonbeam-mkdocs/builders/interoperability/xcm/xc-registrationassets/#generate-encoded-calldata-for-asset-registration) for more details.

 - **xcmExecute**(*bytes memory* message, *uint64* maxWeight) - **available on Moonbase Alpha only** -  executes a custom XCM message given the SCALE encoded versioned message to be executed and the maximum weight to be consumed. This function *cannot* be called from a smart contract due to the nature of the `Transact` instruction
 - **xcmSend**(*Multilocation memory* dest, *bytes memory* message) - **available on Moonbase Alpha only** - sends a custom XCM message given the multilocation of the destination chain to send the message to and the SCALE encoded versioned message to be sent

The `Multilocation` struct in the XCM Utilities Precompile is built the same as the [XCM Transactor Precompile's](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/substrate-calls/xcm-transactor-precompile/#building-the-precompile-multilocation) `Multilocation`.

## Using the XCM Utilities Precompile {: #using-the-xcmutils-precompile }

The XCM Utilities precompile allows users to read data off of the Ethereum JSON-RPC instead of having to go through a Polkadot library. The functions are more for convenience, and less for smart contract use cases.

For `multilocationToAddress`, one example use case is being able to allow transactions that originate from other parachains by whitelisting their Computed Origin addresses. A user can whitelist a multilocation by calculating and storing an address. EVM transactions can originate from other parachains via [remote EVM calls](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/remote-evm-calls/).  

```solidity
// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >=0.8.3;

import "https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-utils/XcmUtils.sol";

contract MultilocationWhitelistExample {
    XcmUtils xcmutils = XcmUtils(0x000000000000000000000000000000000000080C);
    mapping(address => bool) public whitelistedAddresses;

    modifier onlyWhitelisted(address addr)

    function addWhitelistedMultilocation(
        XcmUtils.Multilocation calldata externalMultilocation
    ) external onlyWhitelisted(msg.sender)

    ...
}
```

To check out an example of how to use the `xcmExecute` function to execute a custom XCM message locally, please refer to the [Create and Execute Custom XCM Messages](/moonbeam-mkdocs/builders/interoperability/xcm/send-execute-xcm/#execute-xcm-utils-precompile) guide.
