---
title: The XCM Transactor Precompile
description: This guide describes the XCM Transactor Precompile and shows how to use some of its functions to send remote calls to other chains using Ethereum libraries.
categories:
- XCM Remote Execution
url: https://docs.moonbeam.network/builders/interoperability/xcm/remote-execution/substrate-calls/xcm-transactor-precompile/
word_count: 8149
token_estimate: 14445
version_hash: sha256:1210f0d1a807a0c0493af2476db07c86dcb569b988aa4a2f49fe0af1b59a7203
last_updated: '2026-05-21T21:21:53+00:00'
---

# Using the XCM Transactor Precompile for Remote Execution

XCM messages are comprised of a [series of instructions](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/) that are executed by the Cross-Consensus Virtual Machine (XCVM). Combinations of these instructions result in predetermined actions such as cross-chain token transfers and, more interestingly, remote cross-chain execution. Remote execution involves executing operations or actions on one blockchain from another blockchain while maintaining the integrity of the sender's identity and permissions.

Typically, XCM messages are sent from the root origin (that is, SUDO or through governance), which is not ideal for projects that want to leverage remote cross-chain calls via a simple transaction. The [XCM Transactor Pallet](https://github.com/moonbeam-foundation/moonbeam/blob/master/pallets/xcm-transactor/src/lib.rs) makes it easy to transact on a remote chain through either the [Sovereign account](/moonbeam-mkdocs/builders/interoperability/xcm/overview/#general-xcm-definitions), which should only be allowed through governance, or a [Computed Origin account](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/computed-origins/) via a simple transaction from the source chain.

However, the XCM Transactor Pallet is coded in Rust and is normally not accessible from the Ethereum API side of Moonbeam. As such, Moonbeam introduced the XCM Transactor Precompile, which is a Solidity interface that allows you to interact directly with the Substrate pallet using the Ethereum API.

This guide will show you how to use the XCM Transactor Precompile to send XCM messages from a Moonbeam-based network to other chains in the ecosystem.

**Note that there are still limitations to what you can remotely execute through XCM messages**.

**Developers must understand that sending incorrect XCM messages can result in the loss of funds.** Consequently, it is essential to test XCM features on a TestNet before moving to a production environment.

## XCM Transactor Precompile Contract Address {: #precompile-address }

There are several versions of the XCM Transactor Precompile. **V1 will be deprecated in the near future**, so all implementations must migrate to the newer interfaces.

The XCM Transactor Precompiles are located at the following addresses:

=== "Moonbeam"

    | Version |                                Address                                 |
    |:-------:|:----------------------------------------------------------------------:|
    |   V1    | <pre>```0x0000000000000000000000000000000000000806```</pre> |
    |   V2    | <pre>```0x000000000000000000000000000000000000080d```</pre> |
    |   V3    | <pre>```0x0000000000000000000000000000000000000817```</pre> |

=== "Moonriver"
    | Version |                                 Address                                 |
    |:-------:|:-----------------------------------------------------------------------:|
    |   V1    | <pre>```0x0000000000000000000000000000000000000806```</pre> |
    |   V2    | <pre>```0x000000000000000000000000000000000000080d```</pre> |
    |   V3    | <pre>```0x0000000000000000000000000000000000000817```</pre> |

=== "Moonbase Alpha"

    | Version |                                Address                                 |
    |:-------:|:----------------------------------------------------------------------:|
    |   V1    | <pre>```0x0000000000000000000000000000000000000806```</pre> |
    |   V2    | <pre>```0x000000000000000000000000000000000000080d```</pre> |
    |   V3    | <pre>```0x0000000000000000000000000000000000000817```</pre> |

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## The XCM Transactor Solidity Interface {: #xcmtrasactor-solidity-interface }

The XCM Transactor Precompile is a Solidity interface through which developers can interact with the XCM Transactor Pallet using the Ethereum API.

??? code "XcmTransactorV1.sol"

    ```solidity
    // SPDX-License-Identifier: GPL-3.0-only
    pragma solidity >=0.8.3;

    /// @dev The XcmTransactorV1 contract's address.
    address constant XCM_TRANSACTOR_V1_ADDRESS = 0x0000000000000000000000000000000000000806;

    /// @dev The XcmTransactorV1 contract's instance.
    XcmTransactorV1 constant XCM_TRANSACTOR_V1_CONTRACT = XcmTransactorV1(
        XCM_TRANSACTOR_V1_ADDRESS
    );

    /// @author The Moonbeam Team
    /// @title Xcm Transactor Interface
    /// @dev The interface through which solidity contracts will interact with xcm transactor pallet
    /// @custom:address 0x0000000000000000000000000000000000000806
    interface XcmTransactorV1 {
        // A multilocation is defined by its number of parents and the encoded junctions (interior)
        struct Multilocation {
            uint8 parents;
            bytes[] interior;
        }

        /// Get index of an account in xcm transactor
        /// @custom:selector 3fdc4f36
        /// @param index The index of which we want to retrieve the account
        /// @return owner The owner of the derivative index
        ///
        function indexToAccount(uint16 index) external view returns (address owner);

        /// DEPRECATED, replaced by transactInfoWithSigned
        /// Get transact info of a multilocation
        /// @custom:selector d07d87c3
        /// @param multilocation The location for which we want to know the transact info
        /// @return transactExtraWeight The extra weight involved in the XCM message of using derivative
        /// @return feePerSecond The amount of fee charged for a second of execution in the dest
        /// @return maxWeight Maximum allowed weight for a single message in dest
        ///
        function transactInfo(Multilocation memory multilocation)
            external
            view
            returns (
                uint64 transactExtraWeight,
                uint256 feePerSecond,
                uint64 maxWeight
            );

        /// Get transact info of a multilocation
        /// @custom:selector b689e20c
        /// @param multilocation The location for which we want to know the transact info
        /// @return transactExtraWeight The extra weight involved in the XCM message of using derivative
        /// @return transactExtraWeightSigned The extra weight involved in the XCM message of using signed
        /// @return maxWeight Maximum allowed weight for a single message in dest
        ///
        function transactInfoWithSigned(Multilocation memory multilocation)
            external
            view
            returns (
                uint64 transactExtraWeight,
                uint64 transactExtraWeightSigned,
                uint64 maxWeight
            );

        /// Get fee per second charged in its reserve chain for an asset
        /// @custom:selector 906c9990
        /// @param multilocation The asset location for which we want to know the fee per second value
        /// @return feePerSecond The fee per second that the reserve chain charges for this asset
        ///
        function feePerSecond(Multilocation memory multilocation)
            external
            view
            returns (uint256 feePerSecond);

        /// Transact through XCM using fee based on its multilocation
        /// @custom:selector 94a63c54
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param transactor The transactor to be used
        /// @param index The index to be used
        /// @param feeAsset The asset in which we want to pay fees.
        /// It has to be a reserve of the destination chain
        /// @param weight The weight we want to buy in the destination chain
        /// @param innerCall The inner call to be executed in the destination chain
        function transactThroughDerivativeMultilocation(
            uint8 transactor,
            uint16 index,
            Multilocation memory feeAsset,
            uint64 weight,
            bytes memory innerCall
        ) external;

        /// Transact through XCM using fee based on its currencyId
        /// @custom:selector 02ae072d
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param transactor The transactor to be used
        /// @param index The index to be used
        /// @param currencyId Address of the currencyId of the asset to be used for fees
        /// It has to be a reserve of the destination chain
        /// @param weight The weight we want to buy in the destination chain
        /// @param innerCall The inner call to be executed in the destination chain
        function transactThroughDerivative(
            uint8 transactor,
            uint16 index,
            address currencyId,
            uint64 weight,
            bytes memory innerCall
        ) external;

        /// Transact through XCM using fee based on its multilocation through signed origins
        /// @custom:selector 71d31587
        /// @dev No token is burnt before sending the message. The caller must ensure the destination
        /// is able to understand the DescendOrigin message, and create a unique account from which
        /// dispatch the call
        /// @param dest The destination chain (as multilocation) where to send the message
        /// @param feeLocation The asset multilocation that indentifies the fee payment currency
        /// It has to be a reserve of the destination chain
        /// @param weight The weight we want to buy in the destination chain for the call to be made
        /// @param call The call to be executed in the destination chain
        function transactThroughSignedMultilocation(
            Multilocation memory dest,
            Multilocation memory feeLocation,
            uint64 weight,
            bytes memory call
        ) external;

        /// Transact through XCM using fee based on its erc20 address through signed origins
        /// @custom:selector 42ca339d
        /// @dev No token is burnt before sending the message. The caller must ensure the destination
        /// is able to understand the DescendOrigin message, and create a unique account from which
        /// dispatch the call
        /// @param dest The destination chain (as multilocation) where to send the message
        /// @param feeLocationAddress The ERC20 address of the token we want to use to pay for fees
        /// only callable if such an asset has been BRIDGED to our chain
        /// @param weight The weight we want to buy in the destination chain for the call to be made
        /// @param call The call to be executed in the destination chain
        function transactThroughSigned(
            Multilocation memory dest,
            address feeLocationAddress,
            uint64 weight,
            bytes memory call
        ) external;

        /// @dev Encode 'utility.as_derivative' relay call
        /// @custom:selector ff86378d
        /// @param transactor The transactor to be used
        /// @param index: The derivative index to use
        /// @param innerCall: The inner call to be executed from the derivated address
        /// @return result The bytes associated with the encoded call
        function encodeUtilityAsDerivative(uint8 transactor, uint16 index, bytes memory innerCall)
            external
            pure
            returns (bytes memory result);
    }
    ```

??? code "XcmTransactorV2.sol"

    ```solidity
    // SPDX-License-Identifier: GPL-3.0-only
    pragma solidity >=0.8.0;

    /// @dev The XcmTransactorV2 contract's address.
    address constant XCM_TRANSACTOR_V2_ADDRESS = 0x000000000000000000000000000000000000080D;

    /// @dev The XcmTransactorV2 contract's instance.
    XcmTransactorV2 constant XCM_TRANSACTOR_V2_CONTRACT = XcmTransactorV2(
        XCM_TRANSACTOR_V2_ADDRESS
    );

    /// @author The Moonbeam Team
    /// @title Xcm Transactor Interface
    /// The interface through which solidity contracts will interact with xcm transactor pallet
    /// @custom:address 0x000000000000000000000000000000000000080D
    interface XcmTransactorV2 {
        // A multilocation is defined by its number of parents and the encoded junctions (interior)
        struct Multilocation {
            uint8 parents;
            bytes[] interior;
        }

        /// Get index of an account in xcm transactor
        /// @custom:selector 3fdc4f36
        /// @param index The index of which we want to retrieve the account
        /// @return owner The owner of the derivative index
        ///
        function indexToAccount(uint16 index) external view returns (address owner);

        /// Get transact info of a multilocation
        /// @custom:selector b689e20c
        /// @param multilocation The location for which we want to know the transact info
        /// @return transactExtraWeight The extra weight involved in the XCM message of using derivative
        /// @return transactExtraWeightSigned The extra weight involved in the XCM message of using signed
        /// @return maxWeight Maximum allowed weight for a single message in dest
        ///
        function transactInfoWithSigned(Multilocation memory multilocation)
            external
            view
            returns (
                uint64 transactExtraWeight,
                uint64 transactExtraWeightSigned,
                uint64 maxWeight
            );

        /// Get fee per second charged in its reserve chain for an asset
        /// @custom:selector 906c9990
        /// @param multilocation The asset location for which we want to know the fee per second value
        /// @return feePerSecond The fee per second that the reserve chain charges for this asset
        ///
        function feePerSecond(Multilocation memory multilocation)
            external
            view
            returns (uint256 feePerSecond);

        /// Transact through XCM using fee based on its multilocation
        /// @custom:selector fe430475
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param transactor The transactor to be used
        /// @param index The index to be used
        /// @param feeAsset The asset in which we want to pay fees.
        /// It has to be a reserve of the destination chain
        /// @param transactRequiredWeightAtMost The weight we want to buy in the destination chain
        /// @param innerCall The inner call to be executed in the destination chain
        /// @param feeAmount Amount to be used as fee.
        /// @param overallWeight Overall weight to be used for the xcm message.
        ///
        function transactThroughDerivativeMultilocation(
            uint8 transactor,
            uint16 index,
            Multilocation memory feeAsset,
            uint64 transactRequiredWeightAtMost,
            bytes memory innerCall,
            uint256 feeAmount,
            uint64 overallWeight
        ) external;

        /// Transact through XCM using fee based on its currency_id
        /// @custom:selector 185de2ae
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param transactor The transactor to be used
        /// @param index The index to be used
        /// @param currencyId Address of the currencyId of the asset to be used for fees
        /// It has to be a reserve of the destination chain
        /// @param transactRequiredWeightAtMost The weight we want to buy in the destination chain
        /// @param innerCall The inner call to be executed in the destination chain
        /// @param feeAmount Amount to be used as fee.
        /// @param overallWeight Overall weight to be used for the xcm message.
        function transactThroughDerivative(
            uint8 transactor,
            uint16 index,
            address currencyId,
            uint64 transactRequiredWeightAtMost,
            bytes memory innerCall,
            uint256 feeAmount,
            uint64 overallWeight
        ) external;

        /// Transact through XCM using fee based on its multilocation through signed origins
        /// @custom:selector d7ab340c
        /// @dev No token is burnt before sending the message. The caller must ensure the destination
        /// is able to understand the DescendOrigin message, and create a unique account from which
        /// dispatch the call
        /// @param dest The destination chain (as multilocation) where to send the message
        /// @param feeLocation The asset multilocation that indentifies the fee payment currency
        /// It has to be a reserve of the destination chain
        /// @param transactRequiredWeightAtMost The weight we want to buy in the destination chain for the call to be made
        /// @param call The call to be executed in the destination chain
        /// @param feeAmount Amount to be used as fee.
        /// @param overallWeight Overall weight to be used for the xcm message.
        function transactThroughSignedMultilocation(
            Multilocation memory dest,
            Multilocation memory feeLocation,
            uint64 transactRequiredWeightAtMost,
            bytes memory call,
            uint256 feeAmount,
            uint64 overallWeight
        ) external;

        /// Transact through XCM using fee based on its erc20 address through signed origins
        /// @custom:selector b648f3fe
        /// @dev No token is burnt before sending the message. The caller must ensure the destination
        /// is able to understand the DescendOrigin message, and create a unique account from which
        /// dispatch the call
        /// @param dest The destination chain (as multilocation) where to send the message
        /// @param feeLocationAddress The ERC20 address of the token we want to use to pay for fees
        /// only callable if such an asset has been BRIDGED to our chain
        /// @param transactRequiredWeightAtMost The weight we want to buy in the destination chain for the call to be made
        /// @param call The call to be executed in the destination chain
        /// @param feeAmount Amount to be used as fee.
        /// @param overallWeight Overall weight to be used for the xcm message.
        function transactThroughSigned(
            Multilocation memory dest,
            address feeLocationAddress,
            uint64 transactRequiredWeightAtMost,
            bytes memory call,
            uint256 feeAmount,
            uint64 overallWeight
        ) external;

        /// @dev Encode 'utility.as_derivative' relay call
        /// @custom:selector ff86378d
        /// @param transactor The transactor to be used
        /// @param index: The derivative index to use
        /// @param innerCall: The inner call to be executed from the derivated address
        /// @return result The bytes associated with the encoded call
        function encodeUtilityAsDerivative(uint8 transactor, uint16 index, bytes memory innerCall)
            external
            pure
            returns (bytes memory result);
    }
    ```

??? code "XcmTransactorV3.sol"

    ```solidity
    // SPDX-License-Identifier: GPL-3.0-only
    pragma solidity >=0.8.0;

    /// @dev The XcmTransactorV3 contract's address.
    address constant XCM_TRANSACTOR_V3_ADDRESS = 0x0000000000000000000000000000000000000817;

    /// @dev The XcmTransactorV3 contract's instance.
    XcmTransactorV3 constant XCM_TRANSACTOR_V3_CONTRACT = XcmTransactorV3(
        XCM_TRANSACTOR_V3_ADDRESS
    );

    /// @author The Moonbeam Team
    /// @title Xcm Transactor Interface
    /// The interface through which solidity contracts will interact with xcm transactor pallet
    /// @custom:address 0x0000000000000000000000000000000000000817
    interface XcmTransactorV3 {
        // A multilocation is defined by its number of parents and the encoded junctions (interior)
        struct Multilocation {
            uint8 parents;
            bytes[] interior;
        }

        // Support for Weights V2
        struct Weight {
            uint64 refTime;
            uint64 proofSize;
        }

        /// Get index of an account in xcm transactor
        /// @custom:selector 3fdc4f36
        /// @param index The index of which we want to retrieve the account
        /// @return owner The owner of the derivative index
        ///
        function indexToAccount(uint16 index) external view returns (address owner);

        /// Get transact info of a multilocation
        /// @custom:selector b689e20c
        /// @param multilocation The location for which we want to know the transact info
        /// @return transactExtraWeight The extra weight involved in the XCM message of using derivative
        /// @return transactExtraWeightSigned The extra weight involved in the XCM message of using signed
        /// @return maxWeight Maximum allowed weight for a single message in dest
        ///
        function transactInfoWithSigned(Multilocation memory multilocation)
            external
            view
            returns (
                Weight memory transactExtraWeight,
                Weight memory transactExtraWeightSigned,
                Weight memory maxWeight
            );

        /// Get fee per second charged in its reserve chain for an asset
        /// @custom:selector 906c9990
        /// @param multilocation The asset location for which we want to know the fee per second value
        /// @return feePerSecond The fee per second that the reserve chain charges for this asset
        ///
        function feePerSecond(Multilocation memory multilocation)
            external
            view
            returns (uint256 feePerSecond);

        /// Transact through XCM using fee based on its multilocation
        /// @custom:selector bdacc26b
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param transactor The transactor to be used
        /// @param index The index to be used
        /// @param feeAsset The asset in which we want to pay fees.
        /// It has to be a reserve of the destination chain
        /// @param transactRequiredWeightAtMost The weight we want to buy in the destination chain
        /// @param innerCall The inner call to be executed in the destination chain
        /// @param feeAmount Amount to be used as fee.
        /// @param overallWeight Overall weight to be used for the xcm message. If uint64:MAX is passed 
        /// through refTime field, Unlimited variant will be used. 
        /// @param refund Indicates if RefundSurplus instruction will be appended
        function transactThroughDerivativeMultilocation(
            uint8 transactor,
            uint16 index,
            Multilocation memory feeAsset,
            Weight memory transactRequiredWeightAtMost,
            bytes memory innerCall,
            uint256 feeAmount,
            Weight memory overallWeight,
            bool refund
        ) external;

        /// Transact through XCM using fee based on its currency_id
        /// @custom:selector ca8c82d8
        /// @dev The token transfer burns/transfers the corresponding amount before sending
        /// @param transactor The transactor to be used
        /// @param index The index to be used
        /// @param currencyId Address of the currencyId of the asset to be used for fees
        /// It has to be a reserve of the destination chain
        /// @param transactRequiredWeightAtMost The weight we want to buy in the destination chain
        /// @param innerCall The inner call to be executed in the destination chain
        /// @param feeAmount Amount to be used as fee.
        /// @param overallWeight Overall weight to be used for the xcm message. If uint64:MAX is passed 
        /// through refTime field, Unlimited variant will be used. 
        /// @param refund Indicates if RefundSurplus instruction will be appended
        function transactThroughDerivative(
            uint8 transactor,
            uint16 index,
            address currencyId,
            Weight memory transactRequiredWeightAtMost,
            bytes memory innerCall,
            uint256 feeAmount,
            Weight memory overallWeight,
            bool refund
        ) external;

        /// Transact through XCM using fee based on its multilocation through signed origins
        /// @custom:selector 27b1d492
        /// @dev No token is burnt before sending the message. The caller must ensure the destination
        /// is able to understand the DescendOrigin message, and create a unique account from which
        /// dispatch the call
        /// @param dest The destination chain (as multilocation) where to send the message
        /// @param feeLocation The asset multilocation that indentifies the fee payment currency
        /// It has to be a reserve of the destination chain
        /// @param transactRequiredWeightAtMost The weight we want to buy in the destination chain for the call to be made
        /// @param call The call to be executed in the destination chain
        /// @param feeAmount Amount to be used as fee.
        /// @param overallWeight Overall weight to be used for the xcm message. If uint64:MAX is passed 
        /// through refTime field, Unlimited variant will be used. 
        /// @param refund Indicates if RefundSurplus instruction will be appended
        function transactThroughSignedMultilocation(
            Multilocation memory dest,
            Multilocation memory feeLocation,
            Weight memory transactRequiredWeightAtMost,
            bytes memory call,
            uint256 feeAmount,
            Weight memory overallWeight,
            bool refund
        ) external;

        /// Transact through XCM using fee based on its erc20 address through signed origins
        /// @custom:selector b18270cf
        /// @dev No token is burnt before sending the message. The caller must ensure the destination
        /// is able to understand the DescendOrigin message, and create a unique account from which
        /// dispatch the call
        /// @param dest The destination chain (as multilocation) where to send the message
        /// @param feeLocationAddress The ERC20 address of the token we want to use to pay for fees
        /// only callable if such an asset has been BRIDGED to our chain
        /// @param transactRequiredWeightAtMost The weight we want to buy in the destination chain for the call to be made
        /// @param call The call to be executed in the destination chain
        /// @param feeAmount Amount to be used as fee.
        /// @param overallWeight Overall weight to be used for the xcm message. If uint64:MAX is passed 
        /// through refTime field, Unlimited variant will be used. 
        /// @param refund Indicates if RefundSurplus instruction will be appended
        function transactThroughSigned(
            Multilocation memory dest,
            address feeLocationAddress,
            Weight memory transactRequiredWeightAtMost,
            bytes memory call,
            uint256 feeAmount,
            Weight memory overallWeight,
            bool refund
        ) external;

        /// @dev Encode 'utility.as_derivative' relay call
        /// @custom:selector ff86378d
        /// @param transactor The transactor to be used
        /// @param index: The derivative index to use
        /// @param innerCall: The inner call to be executed from the derivated address
        /// @return result The bytes associated with the encoded call
        function encodeUtilityAsDerivative(uint8 transactor, uint16 index, bytes memory innerCall)
            external
            pure
            returns (bytes memory result);
    }
    ```

!!! note
    The [XCM Transactor Precompile V1](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v1/XcmTransactorV1.sol) will be deprecated in the near future, so all implementations must migrate to the newer interfaces.

The interface varies slightly from version to version. You can find an overview of each version's interface below.

=== "V2"

    The V2 interface includes the following functions:

    ??? function "**transactInfoWithSigned**(*Multilocation* *memory* multilocation) — read-only function that returns the transact information for a given chain"

        === "Parameters"

            - `multilocation` - the multilocation of the chain to get the transact information for
        
        === "Returns"

            The transact information for:

              - The three XCM instructions associated with the external call execution (`transactExtraWeight`)
              - The extra weight information associated with the `DescendOrigin` XCM instruction for the transact through signed extrinsic (`transactExtraWeightSigned`)
              - The maximum allowed weight for the message in the given chain

            ```js
            [ 173428000n, 0n, 20000000000n ]
            ```

    ??? function "**feePerSecond**(*Multilocation* *memory* multilocation) — read-only function that returns units of tokens per second of the XCM execution that is charged as the XCM execution fee for a given asset. This is useful when, for a given chain, there are multiple assets that can be used for fee payment"

        === "Parameters"

            - `multilocation` - the multilocation of the asset to get the units per second value for
        
        === "Returns"
            
            The fee per second that the reserve chain charges for the given asset.

            ```js
            13764626000000n
            ```

    ??? function "**transactThroughSignedMultilocation**(*Multilocation* *memory* dest, *Multilocation* *memory* feeLocation, *uint64* transactRequiredWeightAtMost, *bytes* *memory* call, *uint256* feeAmount, *uint64* overallWeight) — sends an XCM message with instructions to remotely execute a call in the destination chain. The remote call will be signed and executed by a new account, called the [Computed Origin](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/computed-origins/) account, that the destination parachain must compute. Moonbeam-based networks follow [the Computed Origins standard set by Polkadot](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.17.1/polkadot/xcm/xcm-builder/src/location_conversion.rs). You need to provide the asset multilocation of the token that is used for fee payment instead of the address of the XC-20 token"

        === "Parameters"

            - `dest` - the multilocation of a chain in the ecosystem where the XCM message is being sent to (the target chain). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
            - `feeLocation` - the multilocation of the asset to use for fee payment. The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
            - `transactRequiredWeightAtMost` - the weight to buy in the destination chain for the execution of the call defined in the `Transact` instruction
            - `call` - the call to be executed in the destination chain, as defined in the `Transact` instruction 
            - `feeAmount` - the amount to be used as a fee
            - `overallWeight` - the total weight the extrinsic can use to execute all the XCM instructions, plus the weight of the `Transact` call (`transactRequiredWeightAtMost`). The `overallWeight` structure also contains `refTime` and `proofSize`. If you pass in the maximum value for a uint64 for the `refTime`, you'll allow for an unlimited amount of weight to be purchased, which removes the need to know exactly how much weight the destination chain requires to execute the XCM

    ??? function "**transactThroughSigned**(*Multilocation* *memory* dest, *address* feeLocationAddress, *uint64* transactRequiredWeightAtMost, *bytes* *memory* call, *uint256* feeAmount, *uint64* overallWeight) — sends an XCM message with instructions to remotely execute a call in the destination chain. The remote call will be signed and executed by a new account, called the [Computed Origin](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/computed-origins/) account, that the destination parachain must compute. Moonbeam-based networks follow [the Computed Origins standard set by Polkadot](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.17.1/polkadot/xcm/xcm-builder/src/location_conversion.rs). You need to provide the address of the XC-20 asset to be used for fee payment"

        === "Parameters"

            - `dest` - the multilocation of a chain in the ecosystem where the XCM message is being sent to (the target chain). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
            - `feeLocationAddress` - the [XC-20 address](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/#current-xc20-assets) of the asset to use for fee payment
            - `transactRequiredWeightAtMost` - the weight to buy in the destination chain for the execution of the call defined in the `Transact` instruction
            - `call` - the call to be executed in the destination chain, as defined in the `Transact` instruction 
            - `feeAmount` - the amount to be used as a fee
            - `overallWeight` - the total weight the extrinsic can use to execute all the XCM instructions, plus the weight of the `Transact` call (`transactRequiredWeightAtMost`). The `overallWeight` structure also contains `refTime` and `proofSize`. If you pass in the maximum value for a uint64 for the `refTime`, you'll allow for an unlimited amount of weight to be purchased, which removes the need to know exactly how much weight the destination chain requires to execute the XCM

=== "V3"

    The V3 interface adds support for Weights V2, which updates the `Weight` type to represent proof size in addition to computational time. As such, this requires that `refTime` and `proofSize` be defined, where `refTime` is the amount of computational time that can be used for execution and `proofSize` is the amount of storage in bytes that can be used. 
    
    The following struct was added to the XCM Transactor Precompile to support Weights V2:

    ```solidity
    struct Weight {
        uint64 refTime;
        uint65 proofSize;
    }
    ```

    Additionally, support for the [`RefundSurplus`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#refund-surplus) and [`DepositAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#deposit-asset) instructions was added. To append the `RefundSurplus` instruction to the XCM message, you can use the `refund` parameter, which will refund any leftover funds not used for the `Transact` if set to `true`.

    The V3 interface includes the following functions:

    ??? function "**transactInfoWithSigned**(*Multilocation* *memory* multilocation) — read-only function that returns the transact information for a given chain"

        === "Parameters"

            - `multilocation` - the multilocation of the chain to get the transact information for
        
        === "Returns"

            The transact information for:

              - The three XCM instructions associated with the external call execution (`transactExtraWeight`)
              - The extra weight information associated with the `DescendOrigin` XCM instruction for the transact through signed extrinsic (`transactExtraWeightSigned`)
              - The maximum allowed weight for the message in the given chain

            ```js
            [ 173428000n, 0n, 20000000000n ]
            ```

    ??? function "**feePerSecond**(*Multilocation* *memory* multilocation) — read-only function that returns units of token per second of the XCM execution that is charged as the XCM execution fee for a given asset. This is useful when, for a given chain, there are multiple assets that can be used for fee payment"

        === "Parameters"

            - `multilocation` - the multilocation of the asset to get the units per second value for
        
        === "Returns"
            
            The fee per second that the reserve chain charges for the given asset.

            ```js
            13764626000000n
            ```

    ??? function "**transactThroughSignedMultilocation**(*Multilocation* *memory* dest, *Multilocation* *memory* feeLocation, *Weight* transactRequiredWeightAtMost, *bytes* *memory* call, *uint256* feeAmount, *Weight* overallWeight, *bool* refund) — sends an XCM message with instructions to remotely execute a call in the destination chain. The remote call will be signed and executed by a new account, called the [Computed Origin](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/computed-origins/) account, that the destination parachain must compute. Moonbeam-based networks follow [the Computed Origins standard set by Polkadot](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.17.1/polkadot/xcm/xcm-builder/src/location_conversion.rs). You need to provide the asset multilocation of the token that is used for fee payment instead of the address of the XC-20 token"

        === "Parameters"

            - `dest` - the multilocation of a chain in the ecosystem where the XCM message is being sent to (the target chain). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
            - `feeLocation` - the multilocation of the asset to use for fee payment. The multilocation must be formatted in a particular way, which is described in the [following section](#building-the-precompile-multilocation)
            - `transactRequiredWeightAtMost` - the weight to buy in the destination chain for the execution of the call defined in the `Transact` instruction. The `transactRequiredWeightAtMost` structure contains the following:
                - `refTime` - the amount of computational time that can be used for execution
                - `proofSize` - the amount of storage in bytes that can be used
                It should be formatted as follows:
                ```js
                [ INSERT_REF_TIME, INSERT_PROOF_SIZE ]
                ```  
            - `call` - the call to be executed in the destination chain, as defined in the `Transact` instruction 
            - `feeAmount` - the amount to be used as a fee
            - `overallWeight` - the total weight the extrinsic can use to execute all the XCM instructions, plus the weight of the `Transact` call (`transactRequiredWeightAtMost`). The `overallWeight` structure also contains `refTime` and `proofSize`. If you pass in the maximum value for a uint64 for the `refTime`, you'll allow for an unlimited amount of weight to be purchased, which removes the need to know exactly how much weight the destination chain requires to execute the XCM
            - `refund` -  a boolean indicating whether or not to add the `RefundSurplus` and `DepositAsset` instructions to the XCM message to refund any leftover fees 

    ??? function "**transactThroughSigned**(*Multilocation* *memory* dest, *address* feeLocationAddress, *Weight* transactRequiredWeightAtMost, *bytes* *memory* call, *uint256* feeAmount, *Weight* overallWeight, *bool* refund) — sends an XCM message with instructions to remotely execute a call in the destination chain. The remote call will be signed and executed by a new account, called the [Computed Origin](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/computed-origins/) account, that the destination parachain must compute. Moonbeam-based networks follow [the Computed Origins standard set by Polkadot](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.17.1/polkadot/xcm/xcm-builder/src/location_conversion.rs). You need to provide the address of the XC-20 asset to be used for fee payment"

        === "Parameters"

            - `dest` - the multilocation of a chain in the ecosystem where the XCM message is being sent to (the target chain). The multilocation must be formatted in a particular way, which is described in the [Building the Precompile Multilocation](#building-the-precompile-multilocation) section
            - `feeLocationAddress` - the [XC-20 address](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/#current-xc20-assets) of the asset to use for fee payment
            - `transactRequiredWeightAtMost` - the weight to buy in the destination chain for the execution of the call defined in the `Transact` instruction. The `transactRequiredWeightAtMost` structure contains the following:
                - `refTime` - the amount of computational time that can be used for execution
                - `proofSize` - the amount of storage in bytes that can be used
                It should be formatted as follows:
                ```js
                [ INSERT_REF_TIME, INSERT_PROOF_SIZE ]
                ```
            - `call` - the call to be executed in the destination chain, as defined in the `Transact` instruction 
            - `feeAmount` - the amount to be used as a fee
            - `overallWeight` - the total weight the extrinsic can use to execute all the XCM instructions, plus the weight of the `Transact` call (`transactRequiredWeightAtMost`). The `overallWeight` structure also contains `refTime` and `proofSize`. If you pass in the maximum value for a uint64 for the `refTime`, you'll allow for an unlimited amount of weight to be purchased, which removes the need to know exactly how much weight the destination chain requires to execute the XCM
            - `refund` -  a boolean indicating whether or not to add the `RefundSurplus` and `DepositAsset` instructions to the XCM message to refund any leftover fees 

## XCM Instructions for Remote Execution {: #xcm-instructions-for-remote-execution }

The relevant [XCM instructions](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/) to perform remote execution through XCM are, but are not limited to:

 - [`DescendOrigin`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#descend-origin) - gets executed in the target chain. It mutates the origin on the target chain to match the origin on the source chain, ensuring execution on the target chain occurs on behalf of the same entity initiating the XCM message on the source chain
 - [`WithdrawAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#withdraw-asset) - gets executed in the target chain. Removes assets and places them into a holding register
 - [`BuyExecution`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#buy-execution) - gets executed in the target chain. Takes the assets from holding to pay for execution fees. The fees to pay are determined by the target chain
 - [`Transact`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#transact) - gets executed in the target chain. Dispatches encoded call data from a given origin, allowing for the execution of specific operations or functions

## Building the Precompile Multilocation {: #building-the-precompile-multilocation }

In the XCM Transactor Precompile interface, the `Multilocation` structure is defined as follows:

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
The following code snippet goes through some examples of `Multilocation` structures, as they would need to be fed into the XCM Transactor Precompile functions:

```js
// Multilocation targeting the relay chain asset from a parachain
[
  1, // parents = 1
  [], // interior = here
]

// Multilocation targeting Moonbase Alpha DEV token from another parachain
[
  1, // parents = 1
  [  // interior = X2 (the array has a length of 2)
    "0x00000003E8", // Parachain selector + Parachain ID 1000 (Moonbase Alpha)
    "0x0403", // Pallet Instance selector + Pallet Instance 3 (Balances Pallet)
  ],
]

// Multilocation targeting aUSD asset on Acala
[
  1, // parents = 1
  [  // interior = X2 (the array has a length of 2)
    "0x00000007D0", // Parachain selector + Parachain ID 2000 (Acala)
    "0x060001", // General Key selector + Asset Key
  ],
]
```

## Transact through a Computed Origin Account {: #xcmtransactor-transact-through-signed }

This section covers building an XCM message for remote execution using the XCM Transactor Pallet, specifically with the `transactThroughSigned` function. This function uses a [Computed Origin](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/computed-origins/) account on the destination chain to dispatch the remote call.

The example in this section uses a destination parachain that is not publicly available, so you won't be able to follow along exactly. You can modify the example as needed for your own use case.

!!! note
    You need to ensure that the call you are going to execute remotely is allowed in the destination chain!

### Checking Prerequisites {: #xcmtransactor-signed-check-prerequisites }

To be able to send the extrinsics in this section, you need to have:

- An account in the origin chain with [funds](/moonbeam-mkdocs/builders/get-started/networks/moonbase/#get-tokens)
- Funds in the Computed Origin account on the target chain. To learn how to calculate the address of the Computed Origin account, please refer to the [How to Calculate the Computed Origin](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/computed-origins/) documentation

For this example, the following accounts will be used:

- Alice's account in the origin parachain (Moonbase Alpha): `0x44236223aB4291b93EEd10E4B511B37a398DEE55`
- Her Computed Origin address in the target parachain (Parachain 888): `0x5c27c4bb7047083420eddff9cddac4a0a120b45c`

### Building the XCM {: #xcm-transact-through-signed }

For this example, you'll interact with the `transactThroughSigned` function of the XCM Transactor Precompile V3. To use this function, you'll take these general steps:

1. Create a provider using a Moonbase Alpha RPC endpoint
2. Create a signer to send the transaction. This example uses a private key to create the signer and is for demo purposes only. **Never store your private key in a JavaScript file**
3. Create a contract instance of the XCM Transactor V3 Precompile using the address and ABI of the precompile

    ??? code "XCM Transactor V3 ABI"

        ```js
        [
          {
            inputs: [
              {
                internalType: 'uint8',
                name: 'transactor',
                type: 'uint8',
              },
              {
                internalType: 'uint16',
                name: 'index',
                type: 'uint16',
              },
              {
                internalType: 'bytes',
                name: 'innerCall',
                type: 'bytes',
              },
            ],
            name: 'encodeUtilityAsDerivative',
            outputs: [
              {
                internalType: 'bytes',
                name: 'result',
                type: 'bytes',
              },
            ],
            stateMutability: 'pure',
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
                internalType: 'struct XcmTransactorV3.Multilocation',
                name: 'multilocation',
                type: 'tuple',
              },
            ],
            name: 'feePerSecond',
            outputs: [
              {
                internalType: 'uint256',
                name: 'feePerSecond',
                type: 'uint256',
              },
            ],
            stateMutability: 'view',
            type: 'function',
          },
          {
            inputs: [
              {
                internalType: 'uint16',
                name: 'index',
                type: 'uint16',
              },
            ],
            name: 'indexToAccount',
            outputs: [
              {
                internalType: 'address',
                name: 'owner',
                type: 'address',
              },
            ],
            stateMutability: 'view',
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
                internalType: 'struct XcmTransactorV3.Multilocation',
                name: 'multilocation',
                type: 'tuple',
              },
            ],
            name: 'transactInfoWithSigned',
            outputs: [
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'transactExtraWeight',
                type: 'tuple',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'transactExtraWeightSigned',
                type: 'tuple',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'maxWeight',
                type: 'tuple',
              },
            ],
            stateMutability: 'view',
            type: 'function',
          },
          {
            inputs: [
              {
                internalType: 'uint8',
                name: 'transactor',
                type: 'uint8',
              },
              {
                internalType: 'uint16',
                name: 'index',
                type: 'uint16',
              },
              {
                internalType: 'address',
                name: 'currencyId',
                type: 'address',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'transactRequiredWeightAtMost',
                type: 'tuple',
              },
              {
                internalType: 'bytes',
                name: 'innerCall',
                type: 'bytes',
              },
              {
                internalType: 'uint256',
                name: 'feeAmount',
                type: 'uint256',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'overallWeight',
                type: 'tuple',
              },
              {
                internalType: 'bool',
                name: 'refund',
                type: 'bool',
              },
            ],
            name: 'transactThroughDerivative',
            outputs: [],
            stateMutability: 'nonpayable',
            type: 'function',
          },
          {
            inputs: [
              {
                internalType: 'uint8',
                name: 'transactor',
                type: 'uint8',
              },
              {
                internalType: 'uint16',
                name: 'index',
                type: 'uint16',
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
                internalType: 'struct XcmTransactorV3.Multilocation',
                name: 'feeAsset',
                type: 'tuple',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'transactRequiredWeightAtMost',
                type: 'tuple',
              },
              {
                internalType: 'bytes',
                name: 'innerCall',
                type: 'bytes',
              },
              {
                internalType: 'uint256',
                name: 'feeAmount',
                type: 'uint256',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'overallWeight',
                type: 'tuple',
              },
              {
                internalType: 'bool',
                name: 'refund',
                type: 'bool',
              },
            ],
            name: 'transactThroughDerivativeMultilocation',
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
                internalType: 'struct XcmTransactorV3.Multilocation',
                name: 'dest',
                type: 'tuple',
              },
              {
                internalType: 'address',
                name: 'feeLocationAddress',
                type: 'address',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'transactRequiredWeightAtMost',
                type: 'tuple',
              },
              {
                internalType: 'bytes',
                name: 'call',
                type: 'bytes',
              },
              {
                internalType: 'uint256',
                name: 'feeAmount',
                type: 'uint256',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'overallWeight',
                type: 'tuple',
              },
              {
                internalType: 'bool',
                name: 'refund',
                type: 'bool',
              },
            ],
            name: 'transactThroughSigned',
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
                internalType: 'struct XcmTransactorV3.Multilocation',
                name: 'dest',
                type: 'tuple',
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
                internalType: 'struct XcmTransactorV3.Multilocation',
                name: 'feeLocation',
                type: 'tuple',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'transactRequiredWeightAtMost',
                type: 'tuple',
              },
              {
                internalType: 'bytes',
                name: 'call',
                type: 'bytes',
              },
              {
                internalType: 'uint256',
                name: 'feeAmount',
                type: 'uint256',
              },
              {
                components: [
                  {
                    internalType: 'uint64',
                    name: 'refTime',
                    type: 'uint64',
                  },
                  {
                    internalType: 'uint64',
                    name: 'proofSize',
                    type: 'uint64',
                  },
                ],
                internalType: 'struct XcmTransactorV3.Weight',
                name: 'overallWeight',
                type: 'tuple',
              },
              {
                internalType: 'bool',
                name: 'refund',
                type: 'bool',
              },
            ],
            name: 'transactThroughSignedMultilocation',
            outputs: [],
            stateMutability: 'nonpayable',
            type: 'function',
          },
        ];
        ```

4. Assemble the arguments for the `transactThroughSigned` function:

    - `dest` - the multilocation of the destination, which is parachain 888:

        ```js
        const dest = [
          1, // parents = 1
          [  // interior = X1 (the array has a length of 1)
            '0x0000000378', // Parachain selector + Parachain ID 888
          ],
        ];
        ```

    - `feeLocationAddress` - the address of the XC-20 to use for fees, which is parachain 888's native asset:

        ```js
        const feeLocationAddress = '0xFFFFFFFF1AB2B146C526D4154905FF12E6E57675';
        ```

    - `transactRequiredWeightAtMost` - the weight required to execute the call in the `Transact` instruction. You can get this information by using the [`paymentInfo` method of the Polkadot.js API](/moonbeam-mkdocs/builders/substrate/libraries/polkadot-js-api/#fees) on the call

        ```js
        const transactRequiredWeightAtMost = [1000000000n, 5000n];
        ```

    - `call` - the encoded call data of the pallet, method, and input to be called. It can be constructed in [Polkadot.js Apps](https://polkadot.js.org/apps) (which must be connected to the destination chain) or using the [Polkadot.js API](/moonbeam-mkdocs/builders/substrate/libraries/polkadot-js-api/). For this example, the inner call is a simple balance transfer of 1 token of the destination chain to Alice's account there:

        ```js
        const call =
          '0x030044236223ab4291b93eed10e4b511b37a398dee5513000064a7b3b6e00d';
        ```

    - `feeAmount` - the amount to use for fees

        ```js
        const feeAmount = 50000000000000000n;
        ```

    - `overallWeight` - the weight specific to the inner call (`transactRequiredWeightAtMost`) plus the weight needed to cover the execution costs for the XCM instructions in the destination chain: `DescendOrigin`, `WithdrawAsset`, `BuyExecution`, and `Transact`. It's important to note that each chain defines its own weight requirements. To determine the weight required for each XCM instruction on a given chain, please refer to the chain's documentation or reach out to a member of their team. Alternatively, you can pass in the maximum value for a uint64 for the `refTime` (the first index of the array). This will be interpreted as using an unlimited amount of weight, which removes the need to know exactly how much weight the destination chain requires to execute the XCM

        ```js
        const overallWeight = [18446744073709551615n, 10000n];
        ```

5. Create the `transactThroughSigned` function, passing in the arguments
6. Sign and send the transaction

=== "Ethers.js"

    ```js
    import { ethers } from 'ethers'; // Import Ethers library

    const abi = INSERT_ABI;
    const privateKey = 'INSERT_PRIVATE_KEY';

    // Create Ethers provider and signer
    const provider = new ethers.JsonRpcProvider(
      'https://rpc.api.moonbase.moonbeam.network'
    );
    const signer = new ethers.Wallet(privateKey, provider);
    // Create contract instance
    const xcmTransactorV3 = new ethers.Contract(
      '0x0000000000000000000000000000000000000817',
      abi,
      signer
    );

    // Arguments for the transactThroughSigned function
    const dest = [
      1, // parents = 1
      [
        // interior = X1 (the array has a length of 1)
        '0x0000000378', // Parachain selector + Parachain ID 888
      ],
    ];
    const feeLocationAddress = '0xFFFFFFFF1AB2B146C526D4154905FF12E6E57675';
    const transactRequiredWeightAtMost = [1000000000n, 5000n];
    const call = '0x030044236223ab4291b93eed10e4b511b37a398dee5513000064a7b3b6e00d';
    const feeAmount = 50000000000000000n;
    const overallWeight = [2000000000n, 10000n];
    const refund = true;

    // Sends 1 token to Alice's account on parachain 888
    async function transactThroughSigned()

    transactThroughSigned();
    ```

=== "Web3.js"

    ```js
    import Web3 from 'web3'; // Import Web3 library

    const abi = INSERT_ABI;
    const privateKey = 'INSERT_PRIVATE_KEY';

    // Create Web3 provider
    const web3 = new Web3('https://rpc.api.moonbase.moonbeam.network'); // Change to network of choice

    // Create contract instance
    const xcmTransactorV3 = new web3.eth.Contract(
      abi,
      '0x0000000000000000000000000000000000000817',
      { from: web3.eth.accounts.privateKeyToAccount(privateKey).address } // 'from' is necessary for gas estimation
    );

    // Arguments for the transactThroughSigned function
    const dest = [
      1, // parents = 1
      [
        // interior = X1 (the array has a length of 1)
        '0x0000000378', // Parachain selector + Parachain ID 888
      ],
    ];
    const feeLocationAddress = '0xFFFFFFFF1AB2B146C526D4154905FF12E6E57675';
    const transactRequiredWeightAtMost = [1000000000n, 5000n];
    const call = '0x030044236223ab4291b93eed10e4b511b37a398dee5513000064a7b3b6e00d';
    const feeAmount = 50000000000000000n;
    const overallWeight = [2000000000n, 10000n];
    const refund = true;

    // Sends 1 token to Alice's account on parachain 888
    async function transactThroughSigned(),
        privateKey
      );

      // Send signed transaction
      const sendTx = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
      console.log(sendTx);
    }

    transactThroughSigned();
    ```

=== "Web3.py"

    ```py
    from web3 import Web3

    abi = "INSERT_ABI"  # Paste or import the XCM Transactor V3 ABI
    private_key = "INSERT_PRIVATE_KEY"  # This is for demo purposes, never store your private key in plain text
    address = "INSERT_ADDRESS"  # The wallet address that corresponds to your private key

    # Create Web3 provider
    web3 = Web3(Web3.HTTPProvider("https://rpc.api.moonbase.moonbeam.network"))

    # Create contract instance
    xcm_transactor_v3 = web3.eth.contract(
        address="0x0000000000000000000000000000000000000817", abi=abi
    )

    # Arguments for the transactThroughSigned function
    dest = [
        1,  # parents = 1
        [
            # interior = X1 (the array has a length of 1)
            "0x0000000378",  # Parachain selector + Parachain ID 888
        ],
    ]
    feeLocationAddress = "0xFFFFFFFF1AB2B146C526D4154905FF12E6E57675"
    transactRequiredWeightAtMost = [1000000000, 5000]
    call = "0x030044236223ab4291b93eed10e4b511b37a398dee5513000064a7b3b6e00d"
    feeAmount = 50000000000000000
    overallWeight = [2000000000, 10000]
    refund = True


    # Sends 1 xcUNIT to the relay chain using the transferMultiasset function
    def transact_through_signed():
        # Create transaction
        transferTx = xcm_transactor_v3.functions.transactThroughSigned(
            dest,
            feeLocationAddress,
            transactRequiredWeightAtMost,
            call,
            feeAmount,
            overallWeight,
            refund,
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


    transact_through_signed()
    ```

### XCM Transact through Computed Origin Fees {: #transact-through-computed-origin-fees }

When [transacting through the Computed Origin account](#xcmtransactor-transact-through-signed), the transaction fees are paid by the same account from which the call is dispatched, which is a Computed Origin account in the destination chain. Consequently, the Computed Origin account must hold the necessary funds to pay for the entire execution. Note that the destination token, for which fees are paid, does not need to be registered as an XC-20 in the origin chain.

To estimate the amount of token Alice's Computed Origin account will need to have to execute the remote call, you need to check the transact information specific to the destination chain. You can use the following script to get the transact information for parachain 888:

```js
import { ethers } from 'ethers'; // Import Ethers library

const abi = INSERT_ABI;
const privateKey = 'INSERT_PRIVATE_KEY';

// Create Ethers wallet & contract instance
const provider = new ethers.JsonRpcProvider(
  'https://rpc.api.moonbase.moonbeam.network'
);
const signer = new ethers.Wallet(privateKey, provider);
const xcmTransactorV3 = new ethers.Contract(
  '0x0000000000000000000000000000000000000817',
  abi,
  signer
);

// Multilocation for parachain 888
const multilocation = [
  1, // parents = 1
  [  // interior = X1 (the array has a length of 1)
    '0x0000000378', // Parachain selector + Parachain ID 888
  ],
];

const main = async () => {
  const transactInfoWithSigned = await xcmTransactorV3.transactInfoWithSigned(
    multilocation
  );
  console.log(transactInfoWithSigned);
};

main();
```

The response shows that the `transactExtraWeightSigned` is `400,000,000`. This weight is needed to execute the four XCM instructions for this remote call in that specific destination chain. Next, you need to find out how much the destination chain charges per weight of XCM execution in reference to the asset's price. Previously, this was done by sourcing a units per second value. However, this method has been replaced by calculating a relative price. Relative price refers to how many units of the foreign asset correspond to one unit of the native token (GLMR or MOVR) from a value (i.e., price) perspective. For example, if the foreign asset is worth $5 and GLMR is worth $0.25, the relative price would be 0.05. However, we must scale the result to 18 decimals to correspond to the Wei units used. In this case, the relative price would be `50000000000000000`.

You can calculate the relative price with a script in the [XCM Tools repo](https://github.com/Moonsong-Labs/xcm-tools?tab=readme-ov-file#calculate-relative-price). The script is also reproduced below: 

??? code "Calculate Relative Price"
    ```typescript
    import axios from 'axios';
    import chalk from 'chalk';

    // CoinGecko IDs for the networks
    const NETWORK_IDS = {
      GLMR: 'moonbeam',
      MOVR: 'moonriver',
    };

    async function calculateRelativePrice(
      assetPrice: number,
      network: 'GLMR' | 'MOVR'
    ): Promise<string> {
      try {
        // Fetch the native token price from CoinGecko
        const response = await axios.get(
          `https://api.coingecko.com/api/v3/simple/price?ids=${NETWORK_IDS[network]}&vs_currencies=usd`
        );

        const nativeTokenPrice = response.data[NETWORK_IDS[network]].usd;

        // Calculate relative price with 18 decimal places
        // Formula: (nativeTokenPrice / assetPrice) * 10^18
        // This gives us how many units of the asset we need to equal 1 unit of native token
        const relativePrice = (nativeTokenPrice / assetPrice) * Math.pow(10, 18);

        // Return as string to preserve precision
        return relativePrice.toFixed(0);
      } catch (error)`);
        }
        throw error;
      }
    }

    function validateInput(
      price: string,
      network: string
    ): { assetPrice: number; network: 'GLMR' | 'MOVR' } {
      // Validate price
      const assetPrice = parseFloat(price);
      if (isNaN(assetPrice) || assetPrice <= 0)

      // Validate network
      const upperNetwork = network.toUpperCase() as 'GLMR' | 'MOVR';
      if (!['GLMR', 'MOVR'].includes(upperNetwork))

      return { assetPrice, network: upperNetwork };
    }

    function printUsage()

    async function main()

        // Check if required arguments are provided
        if (!price || !network)

        // Validate inputs
        const { assetPrice, network: validNetwork } = validateInput(price, network);

        console.log(
          `\nCalculating relative price for asset worth $${assetPrice} against ${validNetwork}...`
        );
        const relativePrice = await calculateRelativePrice(
          assetPrice,
          validNetwork
        );
        const nativeTokenPrice = (
          await axios.get(
            `https://api.coingecko.com/api/v3/simple/price?ids=${NETWORK_IDS[validNetwork]}&vs_currencies=usd`
          )
        ).data[NETWORK_IDS[validNetwork]].usd;

        const decimalRatio = nativeTokenPrice / assetPrice;

        console.log(`\nResults:`);
        console.log(`Asset Price: $${assetPrice}`);
        console.log(`Network: ${validNetwork}`);
        console.log(`Native Token Price (from CoinGecko): $${nativeTokenPrice}`);
        console.log(`\nRelative Price Analysis:`);
        console.log(
          `1 ${validNetwork} is equal to approximately ${decimalRatio.toFixed(
            3
          )} of your specified token.`
        );
        console.log(
          `With 18 decimals, 1 ${validNetwork} or in WEI, 1000000000000000000 is equal to a relative price of ${relativePrice} units of your token`
        );
        console.log(chalk.bold(`\nRelative Price: ${relativePrice}`));
        console.log(
          `\nThe relative price you should specify in asset registration steps is ${relativePrice}\n`
        );
      } catch (error)
    }

    main();
    ```

Note that the relative price value is related to the cost estimated in the [relay chain XCM fee calculation](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/weights-fees/#polkadot) section or to the one shown in the [units per weight](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/weights-fees/#moonbeam-reserve-assets) section if the target is another parachain. You'll need to find the correct value to ensure that the amount of tokens the Computed Origin account holds is correct. Calculating the associated XCM execution fee is as simple as multiplying the `transactExtraWeightSigned` times the `relativePrice` (for an estimation):

```text
XCM-Wei-Token-Cost = transactExtraWeightSigned * relativePrice
XCM-Token-Cost = XCM-Wei-Token-Cost / DecimalConversion
```

Therefore, the actual calculation for one XCM Transactor transact through derivative call is:

```text
XCM-Wei-Token-Cost = 400000000 * 50000000000000000
XCM-Token-Cost = 20000000000000 / 10^18
```

The cost of transacting through a Computed Origin is `0.00002 TOKEN`. **Note that this does not include the cost of the call being remotely executed, only XCM execution fees.**
