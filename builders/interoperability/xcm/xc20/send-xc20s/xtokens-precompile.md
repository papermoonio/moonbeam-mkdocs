---
title: Send XC-20s to Other Chains
description: Learn how to send assets cross-chain via Cross-Consensus Messaging (XCM) using the X-Tokens Precompile with familiar Ethereum libraries like Ethers and Web3.
categories:
- Precompiles
- XC-20
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/interoperability/xcm/xc20/send-xc20s/xtokens-precompile/
word_count: 4776
token_estimate: 8686
version_hash: sha256:955b5fb9c52753b8c3167dbba82e911f42a81b752a686c0959b3419edb92a8e6
last_updated: '2026-05-21T21:21:53+00:00'
---

# Using the X-Tokens Precompile To Send XC-20s

## Introduction {: #introduction }

Building an XCM message for fungible asset transfers is not an easy task. Consequently, there are wrapper functions and pallets that developers can leverage to use XCM features on Polkadot and Kusama. One example of such wrappers is the [Polkadot XCM](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/xcm-pallet/) Pallet, which provides different methods to transfer fungible assets via XCM.

The [Polkadot XCM Pallet](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/xcm-pallet/) is coded in Rust and is normally not accessible from the Ethereum API side of Moonbeam. However, the [XCM Precompile](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/eth-api/) and the X-Tokens Precompile allow you to interact directly with the Polkadot XCM pallet to send XC-20s from a Solidity interface.

This guide will show you how to leverage the X-Tokens Precompile to send [XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/) from a Moonbeam-based network to other chains in the ecosystem (relay chain/parachains) using Ethereum libraries like Ethers and Web3.

**Developers must understand that sending incorrect XCM messages can result in the loss of funds.** Consequently, it is essential to test XCM features on a TestNet before moving to a production environment.

## X-Tokens Precompile Contract Address {: #contract-address }

The X-Tokens Precompile is located at the following addresses:

=== "Moonbeam"

     ```text
     0x0000000000000000000000000000000000000804
     ```

=== "Moonriver"

     ```text
     0x0000000000000000000000000000000000000804
     ```

=== "Moonbase Alpha"

     ```text
     0x0000000000000000000000000000000000000804
     ```

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## The X-Tokens Solidity Interface {: #xtokens-solidity-interface }

[Xtokens.sol](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xtokens/Xtokens.sol) is an interface through which developers can interact with the X-Tokens Pallet using the Ethereum API.

??? code "Xtokens.sol"

    ```solidity
    // SPDX-License-Identifier: GPL-3.0-only
    pragma solidity >=0.8.3;

    /// @dev The Xtokens contract's address.
    address constant XTOKENS_ADDRESS = 0x0000000000000000000000000000000000000804;

    /// @dev The Xtokens contract's instance.
    Xtokens constant XTOKENS_CONTRACT = Xtokens(XTOKENS_ADDRESS);

    /// @author The Moonbeam Team
    /// @title Xtokens Interface
    /// @dev The interface through which solidity contracts will interact with xtokens pallet
    /// @custom:address 0x0000000000000000000000000000000000000804
    interface Xtokens {
        // A multilocation is defined by its number of parents and the encoded junctions (interior)
        struct Multilocation {
            uint8 parents;
            bytes[] interior;
        }

        // A MultiAsset is defined by a multilocation and an amount
        struct MultiAsset {
            Multilocation location;
            uint256 amount;
        }

        // A Currency is defined by address and the amount to be transferred
        struct Currency {
            address currencyAddress;
            uint256 amount;
        }

        /// Transfer a token through XCM based on its currencyId
        ///
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param currencyAddress The ERC20 address of the currency we want to transfer
        /// @param amount The amount of tokens we want to transfer
        /// @param destination The Multilocation to which we want to send the tokens
        /// @param weight The weight we want to buy in the destination chain 
        /// (uint64::MAX means Unlimited weight)
        /// @custom:selector b9f813ff
        function transfer(
            address currencyAddress,
            uint256 amount,
            Multilocation memory destination,
            uint64 weight
        ) external;

        /// Transfer a token through XCM based on its currencyId specifying fee
        ///
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param currencyAddress The ERC20 address of the currency we want to transfer
        /// @param amount The amount of tokens we want to transfer
        /// @param destination The Multilocation to which we want to send the tokens
        /// @param weight The weight we want to buy in the destination chain 
        /// (uint64::MAX means Unlimited weight)
        /// @custom:selector 3e506ef0
        function transferWithFee(
            address currencyAddress,
            uint256 amount,
            uint256 fee,
            Multilocation memory destination,
            uint64 weight
        ) external;

        /// Transfer a token through XCM based on its MultiLocation
        ///
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param asset The asset we want to transfer, defined by its multilocation.
        /// Currently only Concrete Fungible assets
        /// @param amount The amount of tokens we want to transfer
        /// @param destination The Multilocation to which we want to send the tokens
        /// @param weight The weight we want to buy in the destination chain 
        /// (uint64::MAX means Unlimited weight)
        /// @custom:selector b4f76f96
        function transferMultiasset(
            Multilocation memory asset,
            uint256 amount,
            Multilocation memory destination,
            uint64 weight
        ) external;

        /// Transfer a token through XCM based on its MultiLocation specifying fee
        ///
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param asset The asset we want to transfer, defined by its multilocation.
        /// Currently only Concrete Fungible assets
        /// @param amount The amount of tokens we want to transfer
        /// @param destination The Multilocation to which we want to send the tokens
        /// @param weight The weight we want to buy in the destination chain 
        /// (uint64::MAX means Unlimited weight)
        /// @custom:selector 150c016a
        function transferMultiassetWithFee(
            Multilocation memory asset,
            uint256 amount,
            uint256 fee,
            Multilocation memory destination,
            uint64 weight
        ) external;

        /// Transfer several tokens at once through XCM based on its address specifying fee
        ///
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param currencies The currencies we want to transfer, defined by their address and amount.
        /// @param feeItem Which of the currencies to be used as fee
        /// @param destination The Multilocation to which we want to send the tokens
        /// @param weight The weight we want to buy in the destination chain 
        /// (uint64::MAX means Unlimited weight)
        /// @custom:selector ab946323
        function transferMultiCurrencies(
            Currency[] memory currencies,
            uint32 feeItem,
            Multilocation memory destination,
            uint64 weight
        ) external;

        /// Transfer several tokens at once through XCM based on its location specifying fee
        ///
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param assets The assets we want to transfer, defined by their location and amount.
        /// @param feeItem Which of the currencies to be used as fee
        /// @param destination The Multilocation to which we want to send the tokens
        /// @param weight The weight we want to buy in the destination chain 
        /// (uint64::MAX means Unlimited weight)
        /// @custom:selector 797b45fd
        function transferMultiAssets(
            MultiAsset[] memory assets,
            uint32 feeItem,
            Multilocation memory destination,
            uint64 weight
        ) external;
    }
    ```

The interface includes the following functions:

???+ function "**transfer**(*address* currencyAddress, *uint256* amount, *Multilocation* *memory* destination, *uint64* weight) — transfer a currency, given the contract address of the currency"

    === "Parameters"

        - `currencyAddress` - the address of the asset to transfer
            - For [External XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/#external-xc20s), provide the [XC-20 precompile address](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/#current-xc20-assets)
            - For native tokens (i.e., GLMR, MOVR, and DEV), provide the [ERC-20 precompile](/moonbeam-mkdocs/builders/ethereum/precompiles/ux/erc20/#the-erc20-interface) address, which is `0x0000000000000000000000000000000000000802`
            - For [Local XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/#local-xc20s), provide the token's address
        - `amount` - the number of tokens that are going to be sent via XCM
        - `destination` - the multilocation of the destination address for the tokens being sent via XCM. It supports different address formats, such as 20- or 32-byte addresses (Ethereum or Substrate). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
        - `weight` - the weight to be purchased to pay for XCM execution on the destination chain, which is charged from the transferred asset

??? function "**transferWithFee**(*address* currencyAddress, *uint256* amount, *uint256* fee, *Multilocation* *memory* destination, *uint64* weight) — transfer a currency, defined as either the native token (self-reserved) or the asset ID, and specify the fee separately from the amount"

    === "Parameters"

        - `currencyAddress` - the address of the asset to transfer
            - For [External XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/#external-xc20s), provide the [XC-20 precompile address](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/#current-xc20-assets)
            - For native tokens (i.e., GLMR, MOVR, and DEV), provide the [ERC-20 precompile](/moonbeam-mkdocs/builders/ethereum/precompiles/ux/erc20/#the-erc20-interface) address, which is `0x0000000000000000000000000000000000000802`
            - For [Local XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/#local-xc20s), provide the token's address
        - `amount` - the number of tokens that are going to be sent via XCM
        - `fee` — the amount to be spent to pay for the XCM execution in the target (destination) chain. If this value is not high enough to cover execution costs, the assets will be trapped in the destination chain
        - `destination` - the multilocation of the destination address for the tokens being sent via XCM. It supports different address formats, such as 20- or 32-byte addresses (Ethereum or Substrate). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
        - `weight` - the weight to be purchased to pay for XCM execution on the destination chain, which is charged from the transferred asset

??? function "**transferMultiasset**(*Multilocation* *memory* asset, *uint256* amount, *Multilocation* *memory* destination, *uint64* weight) — transfer a fungible asset, defined by its multilocation"

    === "Parameters"

        - `asset` - the multilocation of the asset to transfer. The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
        - `amount` - the number of tokens that are going to be sent via XCM
        - `destination` - the multilocation of the destination address for the tokens being sent via XCM. It supports different address formats, such as 20- or 32-byte addresses (Ethereum or Substrate). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
        - `weight` - the weight to be purchased to pay for XCM execution on the destination chain, which is charged from the transferred asset

??? function "**transferMultiassetWithFee**(*Multilocation* *memory* asset, *uint256* amount, *uint256* fee, *Multilocation* *memory* destination, *uint64* weight) — transfer a fungible asset, defined by its multilocation, and pay the fee with a different asset, also defined by its multilocation"

    === "Parameters"

        - `asset` - the multilocation of the asset to transfer. The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
        - `amount` - the number of tokens that are going to be sent via XCM
        - `fee` — the amount to be spent to pay for the XCM execution in the target (destination) chain. If this value is not high enough to cover execution costs, the assets will be trapped in the destination chain
        - `destination` - the multilocation of the destination address for the tokens being sent via XCM. It supports different address formats, such as 20- or 32-byte addresses (Ethereum or Substrate). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
        - `weight` - the weight to be purchased to pay for XCM execution on the destination chain, which is charged from the transferred asset

??? function "**transferMulticurrencies**(*Currency[]* *memory* currencies, *uint32* feeItem, *Multilocation* *memory* destination, *uint64* weight) — transfer different currencies, specifying which is used as the fee. Each currency is defined as either the native token (self-reserved) or the asset ID"

    === "Parameters"

        - `currencies` - an array of the currencies to send, which are identified by their currency address, and the amount to send
        - `feeItem` — an index to define the asset position of an array of assets being sent, used to pay for the XCM execution in the target chain. For example, if only one asset is being sent, the `feeItem` would be `0`
        - `destination` - the multilocation of the destination address for the tokens being sent via XCM. It supports different address formats, such as 20- or 32-byte addresses (Ethereum or Substrate). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
        - `weight` - the weight to be purchased to pay for XCM execution on the destination chain, which is charged from the transferred asset

??? function "**transferMultiassets**(*MultiAsset[]* *memory* assets, *uint32* feeItem, *Multilocation* *memory* destination, *uint64* weight) — transfer several fungible assets, defined by their multilocation, and pay the fee with one of the assets, also defined by its multilocation"

    === "Parameters"

        - `assets` - an array of the multilocations of each asset to transfer. The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
        - `feeItem` — an index to define the asset position of an array of assets being sent, used to pay for the XCM execution in the target chain. For example, if only one asset is being sent, the `feeItem` would be `0`
        - `destination` - the multilocation of the destination address for the tokens being sent via XCM. It supports different address formats, such as 20- or 32-byte addresses (Ethereum or Substrate). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
        - `weight` - the weight to be purchased to pay for XCM execution on the destination chain, which is charged from the transferred asset

## Building the Precompile Multilocation {: #building-the-precompile-multilocation }

[Multilocations](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/multilocations/) define a specific point in the entire relay chain/parachain ecosystem relative to a given origin. They are frequently used by the X-Tokens Precompile to define the location of assets and destination chains and accounts.

Multilocations need to be formatted in a specific way that precompiles can understand, which is different than the format seen when interacting with pallets. In the X-Tokens Precompile interface, the `Multilocation` structure is defined as follows:

```solidity
 struct Multilocation {
    uint8 parents;
    bytes[] interior;
}
```

As with a standard [multilocation](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/multilocations/), there are `parents` and `interior` elements. However, instead of defining the multilocation as an object, with Ethereum libraries, the struct is defined as an array, which contains a `uint8` for the `parents` as the first element and a bytes array for the `interior` as the second element.

The normal values you would see for the `parents` element are:

|   Origin    | Destination | Parents Value |
|:-----------:|:-----------:|:-------------:|
| Parachain A | Parachain A |       0       |
| Parachain A | Relay Chain |       1       |
| Parachain A | Parachain B |       1       |

For the `interior` element, the number of fields you need to drill down to in the target chain to reach the exact location of the target, such as the specific asset or account, represents the size of the bytes array:

|    Array     | Size | Interior Value |
|:------------:|:----:|:--------------:|
|      []      |  0   |      Here      |
|    [XYZ]     |  1   |       X1       |
|  [XYZ, ABC]  |  2   |       X2       |
| [XYZ, ... N] |  N   |       XN       |

!!! note
    Interior value `Here` is often used for the relay chain (either as a destination or to target the relay chain asset).

Each field required to reach the exact location of the target needs to be defined as a hex string. The first byte (2 hexadecimal characters) corresponds to the selector of the field. For example:

| Byte Value |    Selector    | Data Type |
|:----------:|:--------------:|-----------|
|    0x00    |   Parachain    | bytes4    |
|    0x01    |  AccountId32   | bytes32   |
|    0x02    | AccountIndex64 | u64       |
|    0x03    |  AccountKey20  | bytes20   |
|    0x04    | PalletInstance | byte      |
|    0x05    |  GeneralIndex  | u128      |
|    0x06    |   GeneralKey   | bytes[]   |

Next, depending on the selector and its data type, the following bytes correspond to the actual data being provided. Note that for `AccountId32`, `AccountIndex64`, and `AccountKey20`, the optional `network` field is appended at the end. For example:

|    Selector    |       Data Value       |             Represents             |
|:--------------:|:----------------------:|:----------------------------------:|
|   Parachain    |    "0x00+000007E7"     |         Parachain ID 2023          |
|  AccountId32   | "0x01+AccountId32+00"  | AccountId32, Network(Option) Null  |
|  AccountId32   | "0x01+AccountId32+03"  |   AccountId32, Network Polkadot    |
|  AccountKey20  | "0x03+AccountKey20+00" | AccountKey20, Network(Option) Null |
| PalletInstance |       "0x04+03"        |         Pallet Instance 3          |

!!! note
    The `interior` data usually needs to be wrapped around quotes, or you might get an `invalid tuple value` error.
The following code snippet goes through some examples of multilocation structures, as they would need to be fed into the X-Tokens Precompile functions:

```js
// Multilocation targeting the relay chain or its asset from a parachain
[
  1, // parents = 1
  [], // interior = here
]

// Multilocation targeting Moonbase Alpha DEV token from another parachain
[
  1, // parents = 1
  [  // interior = X2 (the array has a length of 2)
    '0x00000003E8', // Parachain selector + Parachain ID 1000 (Moonbase Alpha)
    '0x0403', // Pallet Instance selector + Pallet Instance 3 (Balances Pallet)
  ],
]

// Multilocation targeting Alice's account on the relay chain from Moonbase Alpha
[
  1, // parents = 1
  [  // interior = X1 (the array has a length of 1)
     // AccountKey32 selector + AccountId32 address in hex + Network(Option) Null
    '0x01c4db7bcb733e117c0b34ac96354b10d47e84a006b9e7e66a229d174e8ff2a06300', 
  ],
]
```

## Building an XCM Message {: #build-xcm-xtokens-precompile }

This guide covers the process of building an XCM message using the X-Tokens Precompile, more specifically, with the `transfer` and `transferMultiasset` functions. Nevertheless, these two cases can be extrapolated to the other functions of the precompile, especially once you become familiar with multilocations.

You'll be transferring xcUNIT tokens, which are the [XC-20](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/) representation of the Alphanet relay chain token, UNIT. You can adapt this guide for any other XC-20.

### Checking Prerequisites {: #xtokens-check-prerequisites}

To follow along with the examples in this guide, you need to have the following:

- The ABI of the X-Tokens Precompile

    ??? code "X-Tokens Precompile ABI"

        ```js
        export default [
          {
            inputs: [
              {
                internalType: 'address',
                name: 'currencyAddress',
                type: 'address',
              },
              {
                internalType: 'uint256',
                name: 'amount',
                type: 'uint256',
              },
              {
                components: [
                  {
                    internalType: 'uint8',
                    name: 'parents',
                    type: 'uint8',
                  },
                  {
                    internalType: 'bytes[]',
                    name: 'interior',
                    type: 'bytes[]',
                  },
                ],
                internalType: 'struct Xtokens.Multilocation',
                name: 'destination',
                type: 'tuple',
              },
              {
                internalType: 'uint64',
                name: 'weight',
                type: 'uint64',
              },
            ],
            name: 'transfer',
            outputs: [],
            stateMutability: 'nonpayable',
            type: 'function',
          },
          {
            inputs: [
              {
                components: [
                  {
                    components: [
                      {
                        internalType: 'uint8',
                        name: 'parents',
                        type: 'uint8',
                      },
                      {
                        internalType: 'bytes[]',
                        name: 'interior',
                        type: 'bytes[]',
                      },
                    ],
                    internalType: 'struct Xtokens.Multilocation',
                    name: 'location',
                    type: 'tuple',
                  },
                  {
                    internalType: 'uint256',
                    name: 'amount',
                    type: 'uint256',
                  },
                ],
                internalType: 'struct Xtokens.MultiAsset[]',
                name: 'assets',
                type: 'tuple[]',
              },
              {
                internalType: 'uint32',
                name: 'feeItem',
                type: 'uint32',
              },
              {
                components: [
                  {
                    internalType: 'uint8',
                    name: 'parents',
                    type: 'uint8',
                  },
                  {
                    internalType: 'bytes[]',
                    name: 'interior',
                    type: 'bytes[]',
                  },
                ],
                internalType: 'struct Xtokens.Multilocation',
                name: 'destination',
                type: 'tuple',
              },
              {
                internalType: 'uint64',
                name: 'weight',
                type: 'uint64',
              },
            ],
            name: 'transferMultiAssets',
            outputs: [],
            stateMutability: 'nonpayable',
            type: 'function',
          },
          {
            inputs: [
              {
                components: [
                  {
                    internalType: 'address',
                    name: 'currencyAddress',
                    type: 'address',
                  },
                  {
                    internalType: 'uint256',
                    name: 'amount',
                    type: 'uint256',
                  },
                ],
                internalType: 'struct Xtokens.Currency[]',
                name: 'currencies',
                type: 'tuple[]',
              },
              {
                internalType: 'uint32',
                name: 'feeItem',
                type: 'uint32',
              },
              {
                components: [
                  {
                    internalType: 'uint8',
                    name: 'parents',
                    type: 'uint8',
                  },
                  {
                    internalType: 'bytes[]',
                    name: 'interior',
                    type: 'bytes[]',
                  },
                ],
                internalType: 'struct Xtokens.Multilocation',
                name: 'destination',
                type: 'tuple',
              },
              {
                internalType: 'uint64',
                name: 'weight',
                type: 'uint64',
              },
            ],
            name: 'transferMultiCurrencies',
            outputs: [],
            stateMutability: 'nonpayable',
            type: 'function',
          },
          {
            inputs: [
              {
                components: [
                  {
                    internalType: 'uint8',
                    name: 'parents',
                    type: 'uint8',
                  },
                  {
                    internalType: 'bytes[]',
                    name: 'interior',
                    type: 'bytes[]',
                  },
                ],
                internalType: 'struct Xtokens.Multilocation',
                name: 'asset',
                type: 'tuple',
              },
              {
                internalType: 'uint256',
                name: 'amount',
                type: 'uint256',
              },
              {
                components: [
                  {
                    internalType: 'uint8',
                    name: 'parents',
                    type: 'uint8',
                  },
                  {
                    internalType: 'bytes[]',
                    name: 'interior',
                    type: 'bytes[]',
                  },
                ],
                internalType: 'struct Xtokens.Multilocation',
                name: 'destination',
                type: 'tuple',
              },
              {
                internalType: 'uint64',
                name: 'weight',
                type: 'uint64',
              },
            ],
            name: 'transferMultiasset',
            outputs: [],
            stateMutability: 'nonpayable',
            type: 'function',
          },
          {
            inputs: [
              {
                components: [
                  {
                    internalType: 'uint8',
                    name: 'parents',
                    type: 'uint8',
                  },
                  {
                    internalType: 'bytes[]',
                    name: 'interior',
                    type: 'bytes[]',
                  },
                ],
                internalType: 'struct Xtokens.Multilocation',
                name: 'asset',
                type: 'tuple',
              },
              {
                internalType: 'uint256',
                name: 'amount',
                type: 'uint256',
              },
              {
                internalType: 'uint256',
                name: 'fee',
                type: 'uint256',
              },
              {
                components: [
                  {
                    internalType: 'uint8',
                    name: 'parents',
                    type: 'uint8',
                  },
                  {
                    internalType: 'bytes[]',
                    name: 'interior',
                    type: 'bytes[]',
                  },
                ],
                internalType: 'struct Xtokens.Multilocation',
                name: 'destination',
                type: 'tuple',
              },
              {
                internalType: 'uint64',
                name: 'weight',
                type: 'uint64',
              },
            ],
            name: 'transferMultiassetWithFee',
            outputs: [],
            stateMutability: 'nonpayable',
            type: 'function',
          },
          {
            inputs: [
              {
                internalType: 'address',
                name: 'currencyAddress',
                type: 'address',
              },
              {
                internalType: 'uint256',
                name: 'amount',
                type: 'uint256',
              },
              {
                internalType: 'uint256',
                name: 'fee',
                type: 'uint256',
              },
              {
                components: [
                  {
                    internalType: 'uint8',
                    name: 'parents',
                    type: 'uint8',
                  },
                  {
                    internalType: 'bytes[]',
                    name: 'interior',
                    type: 'bytes[]',
                  },
                ],
                internalType: 'struct Xtokens.Multilocation',
                name: 'destination',
                type: 'tuple',
              },
              {
                internalType: 'uint64',
                name: 'weight',
                type: 'uint64',
              },
            ],
            name: 'transferWithFee',
            outputs: [],
            stateMutability: 'nonpayable',
            type: 'function',
          },
        ];
        ```

- An account with funds.
 You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
- Some xcUNIT tokens. To obtain xcUNIT tokens, contact us on Discord and we will be happy to help you

    !!! note
        You can adapt this guide to transfer another [external XC-20 or a local XC-20](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/). For external XC-20s, you'll need the asset ID and the number of decimals the asset has. For local XC-20s, you'll need the contract address.

    To check your xcUNIT balance, you can add the XC-20's [precompile address](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/interact/#calculate-xc20-address) to MetaMask with the following address:

    ```text
    0xFfFFfFff1FcaCBd218EDc0EbA20Fc2308C778080
    ```

!!! note
    To test out the examples on Moonbeam or Moonriver, you can replace the RPC URL with your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).

### Determining Weight Needed for XCM Execution {: #determining-weight }

To determine the weight needed for XCM execution on the destination chain, you'll need to know which XCM instructions are executed on the destination chain. You can find an overview of the XCM instructions used in the [XCM Instructions for Transfers via X-Tokens](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/overview/#xcm-instructions-for-asset-transfers) guide.

!!! note
    Some weights include database reads and writes; for example, the `WithdrawAsset` and `DepositAsset` instructions include both one database read and one write. To get the total weight, you'll need to add the weight of any required database reads or writes to the base weight of the given instruction.

    For Westend-based relay chains, like Alphanet, you can get the weight cost for read and write database operations for [Rocks DB](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.10.0/polkadot/runtime/westend/constants/src/weights/rocksdb_weights.rs#L27-L31) (which is the default database) in the [polkadot-sdk](https://github.com/paritytech/polkadot-sdk) repository on GitHub.

Since Alphanet is a Westend-based relay chain, you can refer to the instruction weights defined in the [Westend runtime code](https://github.com/paritytech/polkadot-sdk/tree/polkadot-v1.10.0/polkadot/runtime/westend), which are broken up into two types of instructions: [fungible](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.10.0/polkadot/runtime/westend/src/weights/xcm/pallet_xcm_benchmarks_fungible.rs) and [generic](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.10.0/polkadot/runtime/westend/src/weights/xcm/pallet_xcm_benchmarks_generic.rs).

It's important to note that each chain defines its own weight requirements. To determine the weight required for each XCM instruction on a given chain, please refer to the chain's documentation or reach out to a member of their team. To learn how to find the weights required by Moonbeam, Polkadot, or Kusama, you can refer to our documentation on [Weights and Fees](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/weights-fees/).

### X-Tokens Precompile Transfer Function {: #precompile-transfer }

To use the `transfer` function of the X-Tokens Precompile, you'll take these general steps:

1. Create a provider using a Moonbase Alpha RPC endpoint
2. Create a signer to send the transaction. This example uses a private key to create the signer and is for demo purposes only. **Never store your private key in a JavaScript file**
3. Create a contract instance of the X-Tokens Precompile using the address and ABI of the precompile
4. Assemble the arguments for the `transfer` function:

    - `currencyAddress` - the address for xcUNIT: `0xFfFFfFff1FcaCBd218EDc0EbA20Fc2308C778080`
    - `amount` - 1 xcUNIT. Since xcUNIT has 12 decimals, you can use: `1000000000000`
    - `destination` - the multilocation of the destination, which targets Alice's account on the relay chain: `'0x01c4db7bcb733e117c0b34ac96354b10d47e84a006b9e7e66a229d174e8ff2a06300'`
    - `weight` - the [weight](#determining-weight) to purchase for the XCM execution on the destination chain: `305,986,000`

5. Create the `transfer` function, passing in the arguments
6. Sign and send the transaction

=== "Ethers.js"

    ```js
    import { ethers } from 'ethers'; // Import Ethers library
    import abi from './xtokensABI.js'; // Import the X-Tokens ABI

    const privateKey = 'INSERT_PRIVATE_KEY';

    // Create Ethers provider and signer
    const provider = new ethers.JsonRpcProvider(
      'https://rpc.api.moonbase.moonbeam.network'
    );
    const signer = new ethers.Wallet(privateKey, provider);

    // Create X-Tokens contract instance
    const xTokens = new ethers.Contract(
      '0x0000000000000000000000000000000000000804',
      abi,
      signer
    );

    // Arguments for the transfer function
    const currencyAddress = '0xFfFFfFff1FcaCBd218EDc0EbA20Fc2308C778080'; // xcUNIT address
    const amount = 1000000000000;
    const destination = [
      // Target the relay chain from Moonbase Alpha
      1,
      // Target Alice's 32-byte relay chain account
      ['0x01c4db7bcb733e117c0b34ac96354b10d47e84a006b9e7e66a229d174e8ff2a06300'],
    ];
    const weight = 305986000;

    // Sends 1 xcUNIT to the relay chain using the transfer function
    async function transferToAlice()

    transferToAlice();
    ```

=== "Web3.js"

    ```js
    import Web3 from 'web3'; // Import Web3 library
    import abi from './xtokensABI.js'; // Import the X-Tokens ABI

    const privateKey = 'INSERT_PRIVATE_KEY';

    // Create Web3 provider
    const web3 = new Web3('https://rpc.api.moonbase.moonbeam.network'); // Change to network of choice

    // Create contract instance
    const xTokens = new web3.eth.Contract(
      abi,
      '0x0000000000000000000000000000000000000804',
      { from: web3.eth.accounts.privateKeyToAccount(privateKey).address } // 'from' is necessary for gas estimation
    );

    // Arguments for the transfer function
    const currencyAddress = '0xFfFFfFff1FcaCBd218EDc0EbA20Fc2308C778080'; // xcUNIT address
    const amount = 1000000000000;
    const destination = [
      // Target the relay chain from Moonbase Alpha
      1,
      // Target Alice's 32-byte relay chain account
      ['0x01c4db7bcb733e117c0b34ac96354b10d47e84a006b9e7e66a229d174e8ff2a06300'],
    ];
    const weight = 305986000;

    // Sends 1 xcUNIT to the relay chain using the transfer function
    async function transferToAlice(),
        privateKey
      );

      // Send signed transaction
      const sendTx = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
      console.log(sendTx);
    }

    transferToAlice();
    ```

=== "Web3.py"

    ```py
    from web3 import Web3

    abi = "INSERT_XTOKENS_ABI"  # Paste or import the x-tokens ABI
    private_key = "INSERT_PRIVATE_KEY"  # This is for demo purposes, never store your private key in plain text
    address = "INSERT_ADDRESS"  # The wallet address that corresponds to your private key

    # Create Web3 provider
    web3 = Web3(Web3.HTTPProvider("https://rpc.api.moonbase.moonbeam.network"))

    # Create contract instance
    x_tokens = web3.eth.contract(
        address="0x0000000000000000000000000000000000000804", abi=abi
    )

    # Arguments for the transfer function
    currencyAddress = "0xFfFFfFff1FcaCBd218EDc0EbA20Fc2308C778080" # xcUNIT address
    amount = 1000000000000
    destination = [
        # Target the relay chain from Moonbase Alpha
        1,
        # Target Alice's 32-byte relay chain account
        ["0x01c4db7bcb733e117c0b34ac96354b10d47e84a006b9e7e66a229d174e8ff2a06300"],
    ]
    weight = 305986000

    # Sends 1 xcUNIT to the relay chain using the transfer function
    def transfer_to_alice():
        # Create transaction
        transferTx = x_tokens.functions.transfer(
            currencyAddress, amount, destination, weight
        ).build_transaction(
            {
                "from": address,
                "nonce": web3.eth.get_transaction_count(address),
            }
        )

        # Sign transaction
        signedTx = web3.eth.account.sign_transaction(transferTx, private_key)

        # Send tx and wait for receipt
        hash = web3.eth.send_raw_transaction(signedTx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(hash)
        print(f"Tx successful with hash: { receipt.transactionHash.hex() }")


    transfer_to_alice()
    ```

### X-Tokens Precompile Transfer Multiasset Function {: #precompile-transfer-multiasset}

To use the `transfer` function of the X-Tokens Precompile, you'll take these general steps:

1. Create a provider using a Moonbase Alpha RPC endpoint
2. Create a signer to send the transaction. This example uses a private key to create the signer and is for demo purposes only. **Never store your private key in a JavaScript file**
3. Create a contract instance of the X-Tokens Precompile using the address and ABI of the precompile
4. Assemble the arguments for the `transferMultiasset` function:

    - `asset` - the multilocation for xcUNIT: `[1, []]`
    - `amount` - 1 xcUNIT. Since xcUNIT has 12 decimals, you can use: `1000000000000`
    - `destination` - the multilocation of the destination, which targets Alice's account on the relay chain: `'0x01c4db7bcb733e117c0b34ac96354b10d47e84a006b9e7e66a229d174e8ff2a06300'`
    - `weight` - the [weight](#determining-weight) to purchase for the XCM execution on the destination chain: `305986000`

5. Create the `transferMultiasset` function, passing in the arguments
6. Sign and send the transaction

=== "Ethers.js"

    ```js
    import { ethers } from 'ethers'; // Import Ethers library
    import abi from './xtokensABI.js'; // Import the X-Tokens ABI

    const privateKey = 'INSERT_PRIVATE_KEY';

    // Create Ethers provider and signer
    const provider = new ethers.JsonRpcProvider(
      'https://rpc.api.moonbase.moonbeam.network'
    );
    const signer = new ethers.Wallet(privateKey, provider);

    // Create X-Tokens contract instance
    const xTokens = new ethers.Contract(
      '0x0000000000000000000000000000000000000804',
      abi,
      signer
    );

    // Arguments for the transfer multiasset function
    const asset = [1, []]; // Multilocation targeting the relay chain
    const amount = 1000000000000;
    const dest = [
      // Target the relay chain from Moonbase Alpha
      1,
      // Target Alice's 32-byte relay chain account
      ['0x01c4db7bcb733e117c0b34ac96354b10d47e84a006b9e7e66a229d174e8ff2a06300'],
    ];
    const weight = 305986000;

    // Sends 1 xcUNIT to the relay chain using the transferMultiasset function
    async function transferMultiassetToAlice()

    transferMultiassetToAlice();
    ```

=== "Web3.js"

    ```js
    import Web3 from 'web3'; // Import Web3 library
    import abi from './xtokensABI.js'; // Import the X-Tokens ABI

    const privateKey = 'INSERT_PRIVATE_KEY';

    // Create Web3 provider
    const web3 = new Web3('https://rpc.api.moonbase.moonbeam.network'); // Change to network of choice

    // Create contract instance
    const xTokens = new web3.eth.Contract(
      abi,
      '0x0000000000000000000000000000000000000804',
      { from: web3.eth.accounts.privateKeyToAccount(privateKey).address } // 'from' is necessary for gas estimation
    );

    // Arguments for the transfer multiasset function
    const asset = [1, []]; // Multilocation targeting the relay chain
    const amount = 1000000000000;
    const dest = [
      // Target the relay chain from Moonbase Alpha
      1,
      // Target Alice's 32-byte relay chain account
      ['0x01c4db7bcb733e117c0b34ac96354b10d47e84a006b9e7e66a229d174e8ff2a06300'],
    ];
    const weight = 305986000;

    // Sends 1 xcUNIT to the relay chain using the transferMultiasset function
    async function transferMultiassetToAlice(),
        privateKey
      );

      // Send signed transaction
      const sendTx = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
      console.log(sendTx);
    }

    transferMultiassetToAlice();
    ```

=== "Web3.py"

    ```py
    from web3 import Web3

    abi = "INSERT_XTOKENS_ABI"  # Paste or import the x-tokens ABI
    private_key = "INSERT_PRIVATE_KEY"  # This is for demo purposes, never store your private key in plain text
    address = "INSERT_ADDRESS"  # The wallet address that corresponds to your private key

    # Create Web3 provider
    web3 = Web3(Web3.HTTPProvider("https://rpc.api.moonbase.moonbeam.network"))

    # Create contract instance
    x_tokens = web3.eth.contract(
        address="0x0000000000000000000000000000000000000804", abi=abi
    )

    # Arguments for the transfer function
    asset = [1, []]  # Multilocation targeting the relay chain
    amount = 1000000000000
    dest = [
        # Target the relay chain from Moonbase Alpha
        1,
        # Target Alice's 32-byte relay chain account
        ["0x01c4db7bcb733e117c0b34ac96354b10d47e84a006b9e7e66a229d174e8ff2a06300"],
    ]
    weight = 305986000


    # Sends 1 xcUNIT to the relay chain using the transferMultiasset function
    def transfer_multiasset_to_alice():
        # Create transaction
        transferTx = x_tokens.functions.transferMultiasset(
            asset, amount, dest, weight
        ).build_transaction(
            {
                "from": address,
                "nonce": web3.eth.get_transaction_count(address),
            }
        )

        # Sign transaction
        signedTx = web3.eth.account.sign_transaction(transferTx, private_key)

        # Send tx and wait for receipt
        hash = web3.eth.send_raw_transaction(signedTx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(hash)
        print(f"Tx successful with hash: { receipt.transactionHash.hex() }")


    transfer_multiasset_to_alice()
    ```
