---
title: GMP Precompile
description: Learn about the GMP precompile on Moonbeam and how to use it with the Moonbeam Routed Liquidity program provided by bridges like Wormhole.
categories:
- Precompiles
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/precompiles/interoperability/gmp/
word_count: 1774
token_estimate: 2883
version_hash: sha256:4392521b132a633de1bc19e9c4c764e0a68f6e5c8da12c5fd94dceaa6b4ec86b
last_updated: '2026-05-21T21:21:53+00:00'
---

# Interacting with the GMP Precompile

## Introduction {: #introduction }

Moonbeam Routed Liquidity (MRL) refers to Moonbeam’s use case as the port parachain for liquidity from origin chains into other Polkadot parachains. This is possible because of general message passing (GMP), where messages with arbitrary data and tokens can be sent across non-parachain blockchains through [chain-agnostic GMP protocols](/moonbeam-mkdocs/builders/interoperability/protocols/). These GMP protocols can combine with [Polkadot's XCM messaging system](/moonbeam-mkdocs/builders/interoperability/xcm/overview/) to allow for seamless liquidity routing.  

The GMP precompile acts as an interface for Moonbeam Routed Liquidity, acting as a middleman between token-bearing messages from GMP protocols and parachains connected to Moonbeam via [XCMP](/moonbeam-mkdocs/builders/interoperability/xcm/overview/#xcm-transport-protocols). Currently, the GMP Precompile only supports the relaying of liquidity through the [Wormhole GMP protocol](/moonbeam-mkdocs/builders/interoperability/protocols/wormhole/).  

The GMP Precompile is located at the following address:  

=== "Moonbeam"

     ```text
     0x0000000000000000000000000000000000000816
     ```

=== "Moonriver"

     ```text
     0x0000000000000000000000000000000000000816
     ```

=== "Moonbase Alpha"

     ```text
     0x0000000000000000000000000000000000000816
     ```

In practice, it is unlikely that a developer will have to directly interact with the precompile. GMP protocols' relayers interact with the precompile to complete cross-chain actions, so the origin chain that the cross-chain action originates is where the developer has the responsibility to ensure that the GMP precompile is used *eventually*.  

## The GMP Solidity Interface {: #the-gmp-solidity-interface }

[`Gmp.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/gmp/Gmp.sol) is a Solidity interface that allows developers to interact with the precompile.   

??? code "Gmp.sol"

    ```solidity
    // SPDX-License-Identifier: GPL-3.0-only
    pragma solidity >=0.8.3;

    /// @dev The Gmp contract's address.
    address constant GMP_ADDRESS = 0x0000000000000000000000000000000000000816;

    /// @dev The Gmp contract's instance.
    Gmp constant GMP_CONTRACT = Gmp(GMP_ADDRESS);

    /// @author The Moonbeam Team
    /// @title Gmp precompile
    /// @dev Provides an endpoint to Gmp protocols which can automatically forward to XCM
    /// @custom:address 0x0000000000000000000000000000000000000816
    interface Gmp {
        // TODO: Here we would specify the endpoints for each GMP protocol on a case by case basis.
        //       These endpoints are basically the hand offs for each protocol -- where they delegate to
        //       the target contract.
        //
        //       This design should allow users to interact with this precompile with no changes to the
        //       underlying GMP protocols by simply specifying the correct precompile as the target.

        /// Receive a wormhole VAA and process it
        ///
        /// @custom:selector f53774ab
        function wormholeTransferERC20(bytes memory vaa) external;
    }
    ```

The GMP precompile has one method: 

- **wormholeTransferERC20**(*bytes memory* vaa) - receives a Wormhole bridge transfer [verified action approval (VAA)](https://wormhole.com/docs/protocol/infrastructure/vaas/), mints tokens via the Wormhole token bridge, and forwards the liquidity to the custom payload’s [multilocation](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/multilocations/). The payload is expected to be a precompile-specific SCALE encoded object, as explained in this guide's [Building the Payload for Wormhole](#building-the-payload-for-wormhole) section

VAAs are payload-containing packages generated after origin-chain transactions and are discovered by Wormhole [Guardians](https://wormhole.com/docs/protocol/infrastructure/guardians/).

The most common instance in which a user will have to interact with the precompile is during a recovery, where a relayer doesn’t complete an MRL transaction. For example, a user must search for the VAA that comes with their origin chain transaction and manually invoke the `wormholeTransferERC20` function.

## Building the Payload for Wormhole {: #building-the-payload-for-wormhole }

Currently, the GMP precompile only supports sending liquidity with Wormhole, through Moonbeam, and into other parachains. The GMP precompile does not assist with a route from parachains back to Moonbeam and subsequently, Wormhole-connected chains.    

To send liquidity from a Wormhole-connected origin chain like Ethereum, users must invoke the [`transferTokensWithPayload` method](https://wormhole.com/docs/protocol/infrastructure/vaas/#token--message) on the [origin-chain's deployment](https://wormhole.com/docs/protocol/infrastructure/core-contracts/#token-bridge) of the [WormholeTokenBridge smart contract](https://github.com/wormhole-foundation/wormhole/blob/main/ethereum/contracts/bridge/interfaces/ITokenBridge.sol). This function requires a bytes payload, which must be formatted as a SCALE encoded multilocation object wrapped within [another precompile-specific versioned type](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4302/precompiles/gmp/src/types.rs#L53-L76).

You may be unfamiliar with SCALE encoding and multilocations if you are unfamiliar with the Polkadot ecosystem. [SCALE encoding](https://docs.polkadot.com/reference/parachains/data-encoding/) is a compact form of encoding that Polkadot uses. The [`MultiLocation` type](https://wiki.polkadot.com/learn/learn-xcvm/) is used to define a relative point in Polkadot, such as a specific account on a specific parachain (Polkadot blockchain).  

Moonbeam’s GMP protocol requires a multilocation to represent the destination for liquidity routing, which most likely means an account on another parachain. Whatever it is, this destination must be expressed as relative to Moonbeam.  

!!! remember
    Multilocations being relative is important, because a parachain team may erroneously give you a multilocation relative to their own chain, which can be different. Providing an incorrect multilocation can result in **loss of funds**!

Each parachain will have its specific methods of interpreting a multilocation, and should confirm with the project that the multilocation that you formed is correct. However, you will most likely be forming a multilocation with an account.

Multiple types of accounts can be included in a multilocation, which you must know beforehand when constructing your multilocation. The two most common are:

- **AccountKey20** — an account ID that is 20-bytes in length, including Ethereum-compatible account IDs such as those on Moonbeam
- **AccountId32** — an account ID that is 32-bytes in length, standard in Polkadot and its parachains

The following multilocation templates target accounts on other parachains with Moonbeam as the relative origin. To use them, replace `INSERT_PARACHAIN_ID` with the parachain ID of the network you wish to send funds to and replace `INSERT_ADDRESS` with the address of the account you want to send funds to on that parachain.  

=== "AccountId32"

    ```js
    {
      V4: {
        parents: 1,
        interior: {
          X2: [
            { Parachain: 'INSERT_PARACHAIN_ID' },
            {
              AccountId32: {
                id: 'INSERT_ADDRESS',
              },
            },
          ],
        },
      },
    };
    ```

=== "AccountKey20"

    ```js
    {
      V4: {
        parents: 1,
        interior: {
          X2: [
            { Parachain: 'INSERT_PARACHAIN_ID' },
            {
              AccountKey20: {
                key: 'INSERT_ADDRESS',
              },
            },
          ],
        },
      }
    };
    ```

It can be challenging to correctly SCALE encode the entire payload without the right tools, mainly due to the [custom types expected by the precompile](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4302/precompiles/gmp/src/types.rs#L53-L76). Fortunately, the Polkadot.js API can assist with this.

The versioned user action expected by the precompile accepts two versions: V1 and V2. V1 accepts the `XcmRoutingUserAction` type, which attempts to route the transferred assets to the destination defined by the multilocation. V2 accepts the `XcmRoutingUserActionWithFee` type, which also attempts to route the transferred assets to the destination and allows a fee to be paid. Relayers can use V2 to specify a fee on Moonbeam to relay the transaction to the given destination.

The following script shows how to create a `Uint8Array` that can be used as a payload for the GMP precompile:  

=== "V1"

    ```typescript
    import { ApiPromise, WsProvider } from '@polkadot/api';

    enum MRLTypes {
      // Runtime defined MultiLocation. Allows for XCM versions 2, 3, and 4
      XcmVersionedLocation = 'XcmVersionedLocation',
      // MRL payload (V1) that only defines the destination MultiLocation
      XcmRoutingUserAction = 'XcmRoutingUserAction',
      // Wrapper object for the MRL payload
      VersionedUserAction = 'VersionedUserAction',
    }

    // Parachain IDs of each parachain
    enum Parachain {
      MoonbaseBeta = 888,
      // Insert additional parachain IDs
    }

    // List of parachains that use ethereum (20) accounts
    const ETHEREUM_ACCOUNT_PARACHAINS = [Parachain.MoonbaseBeta];

    // A function that creates a SCALE encoded payload to use with transferTokensWithPayload
    async function createMRLPayload(
      parachainId: Parachain,
      account: string
    ): Promise<Uint8Array> {
      // Create a multilocation object based on the target parachain's account type
      const isEthereumStyle = ETHEREUM_ACCOUNT_PARACHAINS.includes(parachainId);
      const multilocation = {
        V4: {
          parents: 1,
          interior: {
            X2: [
              { Parachain: parachainId },
              isEthereumStyle
                ? { AccountKey20: { key: account } }
                : { AccountId32: { id: account } },
            ],
          },
        },
      };

      // Creates an API for Moonbeam that defines MRL's special types
      const wsProvider = new WsProvider('wss://wss.api.moonbase.moonbeam.network');
      const api = await ApiPromise.create({
        provider: wsProvider,
        types: {
          [MRLTypes.XcmRoutingUserAction]: {
            destination: MRLTypes.XcmVersionedLocation,
          },
          [MRLTypes.VersionedUserAction]: {
            _enum: { V1: MRLTypes.XcmRoutingUserAction },
          },
        },
      });

      // Format multilocation object as a Polkadot.js type
      const versionedLocation = api.createType(
        MRLTypes.XcmVersionedLocation,
        multilocation
      );
      const userAction = api.createType(MRLTypes.XcmRoutingUserAction, {
        destination: versionedLocation,
      });

      // Wrap and format the MultiLocation object into the precompile's input type
      const versionedUserAction = api.createType(MRLTypes.VersionedUserAction, {
        V1: userAction,
      });

      // Disconnect the API
      api.disconnect();

      // SCALE encode resultant precompile formatted objects
      return versionedUserAction.toU8a();
    }
    ```

=== "V2"

    ```typescript
    import { ApiPromise, WsProvider } from '@polkadot/api';
    import { u256 } from '@polkadot/types';

    enum MRLTypes {
      // Runtime defined MultiLocation. Allows for XCM versions 2 and 3
      XcmVersionedLocation = 'XcmVersionedLocation',
      // MRL payload (V2) that defines the destination MultiLocation and a
      // fee for the relayer
      XcmRoutingUserActionWithFee = 'XcmRoutingUserActionWithFee',
      // Wrapper object for the MRL payload
      VersionedUserAction = 'VersionedUserAction',
    }

    // Parachain IDs of each parachain
    enum Parachain {
      MoonbaseBeta = 888,
      // Insert additional parachain IDs
    }

    // List of parachains that use ethereum (20) accounts
    const ETHEREUM_ACCOUNT_PARACHAINS = [Parachain.MoonbaseBeta];

    // A function that creates a SCALE encoded payload to use with
    // transferTokensWithPayload
    async function createMRLPayload(
      parachainId: Parachain,
      account: string,
      fee: u256
    ): Promise<Uint8Array> {
      // Create a multilocation object based on the target parachain's account
      // type
      const isEthereumStyle = ETHEREUM_ACCOUNT_PARACHAINS.includes(parachainId);
      const multilocation = {
        V4: {
          parents: 1,
          interior: {
            X2: [
              { Parachain: parachainId },
              isEthereumStyle
                ? { AccountKey20: { key: account } }
                : { AccountId32: { id: account } },
            ],
          },
        },
      };

      // Creates an API for Moonbeam that defines MRL's special types
      const wsProvider = new WsProvider('wss://wss.api.moonbase.moonbeam.network');
      const api = await ApiPromise.create({
        provider: wsProvider,
        types: {
          [MRLTypes.XcmRoutingUserActionWithFee]: {
            destination: MRLTypes.XcmVersionedLocation,
            fee: 'U256',
          },
          [MRLTypes.VersionedUserAction]: {
            _enum: { V2: MRLTypes.XcmRoutingUserActionWithFee },
          },
        },
      });

      // Format multilocation object as a Polkadot.js type
      const versionedLocation = api.createType(
        MRLTypes.XcmVersionedLocation,
        multilocation
      );
      const userAction = api.createType(MRLTypes.XcmRoutingUserActionWithFee, {
        destination: versionedLocation,
        fee,
      });

      // Wrap and format the MultiLocation object into the precompile's input type
      const versionedUserAction = api.createType(MRLTypes.VersionedUserAction, {
        V2: userAction,
      });

        // Disconnect the API
        api.disconnect();

      // SCALE encode resultant precompile formatted objects
      return versionedUserAction.toU8a();
    }
    ```

## Restrictions {: #restrictions }

The GMP precompile is currently in its early stages. There are many restrictions, and it only supports a “happy path” into parachains. Here are some restrictions that you should be aware of:

- There is currently no fee mechanism. Relayers that run the forwarding of liquidity on Moonbeam to a parachain will be subsidizing transactions. This may change in the future
- The precompile does not check to ensure that the destination chain supports the token that is being sent to it. **Incorrect multilocations may result in loss of funds**
- Errors in constructing a multilocation will result in reverts, which will trap tokens and result in a loss of funds
- There is currently no recommended path backward, from parachains to other chains like Ethereum. There is additional protocol-level work that must be done before a one-click method can be realized
  - Due to a restriction with the ERC-20 XC-assets, the only way to send tokens from a parachain back through Moonbeam is to have xcGLMR on the origin parachain and use it as a fee asset when sending tokens back
