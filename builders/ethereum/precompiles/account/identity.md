---
title: Identity Precompile
description: Learn all you need to know about the Identity Precompile, such as its address, Solidity interface, and how to interact with it using popular Ethereum libraries.
categories:
- Precompiles
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/precompiles/account/identity/
word_count: 4019
token_estimate: 10467
version_hash: sha256:f8d508d3db111a69d0afb38eaf729879bafe0caba6e27f79724e1af1c9e3072b
last_updated: '2026-05-21T21:21:53+00:00'
---

# Identity Precompile on Moonbeam

## Introduction {: #introduction }

The Identity Precompile is a Solidity interface that allows you to create, manage, and retrieve information on on-chain identities. Identities are attached to accounts and include personal information, such as your legal name, display name, website, Twitter handle, Riot (now known as Element) name, and more. You can also take advantage of custom fields to include any other relevant information.

The Identity Precompile interacts directly with Moonbeam's underlying Substrate Identity runtime logic to provide the functionality needed to create and manage identities. This pallet is coded in Rust and is normally not accessible from the Ethereum side of Moonbeam. However, the Identity Precompile allows you to access this functionality directly from the Solidity interface.

The Identity Precompile is located at the following address:

=== "Moonbeam"

     ```text
     0x0000000000000000000000000000000000000818
     ```

=== "Moonriver"

     ```text
     0x0000000000000000000000000000000000000818
     ```

=== "Moonbase Alpha"

     ```text
     0x0000000000000000000000000000000000000818
     ```

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## The Identity Precompile Solidity Interface {: #the-solidity-interface }

[`Identity.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/identity/Identity.sol) is a Solidity interface that allows developers to interact with the precompile's methods.

??? code "Identity.sol"

    ```solidity
    // SPDX-License-Identifier: GPL-3.0-only
    pragma solidity >=0.8.3;

    /// @dev The Identity contract's address.
    address constant IDENTITY_ADDRESS = 0x0000000000000000000000000000000000000818;

    /// @dev The Identity contract's instance.
    Identity constant IDENTITY_CONTRACT = Identity(IDENTITY_ADDRESS);

    /// @author The Moonbeam Team
    /// @title Pallet Identity Interface
    /// @title The interface through which solidity contracts will interact with the Identity pallet
    /// @custom:address 0x0000000000000000000000000000000000000818
    interface Identity {
        /// @dev Associated raw data.
        struct Data {
            /// Is `true` if it represents data, else the absence of data is represented by `false`.
            bool hasData;
            /// The contained value.
            bytes value;
        }

        /// @dev The super-identity of an alternative "sub" identity.
        struct SuperOf {
            /// Is `true` if the struct is valid, `false` otherwise.
            bool isValid;
            /// The super account.
            address account;
            /// The associated data.
            Data data;
        }

        /// @dev Alternative "sub" identities of an account.
        struct SubsOf {
            /// The deposit against this identity.
            uint256 deposit;
            /// The sub accounts
            address[] accounts;
        }

        /// @dev Registrar judgements are limited to attestations on these fields.
        struct IdentityFields {
            /// Set to `true` if the display field is supported, `false` otherwise.
            bool display;
            /// Set to `true` if the legal field is supported, `false` otherwise.
            bool legal;
            /// Set to `true` if the web field is supported, `false` otherwise.
            bool web;
            /// Set to `true` if the riot field is supported, `false` otherwise.
            bool riot;
            /// Set to `true` if the email field is supported, `false` otherwise.
            bool email;
            /// Set to `true` if the PGP Fingerprint field is supported, `false` otherwise.
            bool pgpFingerprint;
            /// Set to `true` if the image field is supported, `false` otherwise.
            bool image;
            /// Set to `true` if the twitter field is supported, `false` otherwise.
            bool twitter;
        }

        /// @dev Registrar info.
        struct Registrar {
            /// Is `true` if the struct is valid, `false` otherwise.
            bool isValid;
            /// The registrar's index.
            uint32 index;
            /// The account address.
            address account;
            /// Amount required to be given to the registrar for them to provide judgement.
            uint256 fee;
            /// Relevant fields for this registrar.
            IdentityFields fields;
        }

        /// @dev Represents an additional field in identity info.
        struct Additional {
            /// The assciated key.
            Data key;
            /// The assciated value.
            Data value;
        }

        /// @dev The identity information set for an account.
        struct IdentityInfo {
            /// Represents the additional fields for the identity.
            Additional[] additional;
            /// Represents the display info for the identity.
            Data display;
            /// Represents the legal info for the identity.
            Data legal;
            /// Represents the web info for the identity.
            Data web;
            /// Represents the riot info for the identity.
            Data riot;
            /// Represents the email info for the identity.
            Data email;
            /// Set to `true` if `pgpFingerprint` is set, `false` otherwise.
            bool hasPgpFingerprint;
            /// Represents a 20-byte the PGP fingerprint info for the identity.
            bytes pgpFingerprint;
            /// Represents the image info for the identity.
            Data image;
            /// Represents the twitter info for the identity.
            Data twitter;
        }

        /// @dev Judgement provided by a registrar.
        struct Judgement {
            /// The default value; no opinion is held.
            bool isUnknown;
            /// No judgement is yet in place, but a deposit is reserved as payment for providing one.
            bool isFeePaid;
            /// The deposit reserved for providing a judgement.
            uint256 feePaidDeposit;
            /// The data appears to be reasonably acceptable in terms of its accuracy.
            bool isReasonable;
            /// The target is known directly by the registrar and the registrar can fully attest to it.
            bool isKnownGood;
            /// The data was once good but is currently out of date.
            bool isOutOfDate;
            /// The data is imprecise or of sufficiently low-quality to be problematic.
            bool isLowQuality;
            /// The data is erroneous. This may be indicative of malicious intent.
            bool isErroneous;
        }

        /// @dev Judgement item provided by a registrar.
        struct JudgementInfo {
            /// The registrar's index that provided this judgement.
            uint32 registrarIndex;
            /// The registrar's provided judgement.
            Judgement judgement;
        }

        /// @dev Registrar info.
        struct Registration {
            /// Is `true` if the struct is valid, `false` otherwise.
            bool isValid;
            /// The judgments provided on this identity.
            JudgementInfo[] judgements;
            /// Amount required to be given to the registrar for them to provide judgement.
            uint256 deposit;
            /// The associated identity info.
            IdentityInfo info;
        }

        /// @dev Alternative "sub" identity of an account.
        struct SubAccount {
            /// The account address.
            address account;
            /// The associated data.
            Data data;
        }

        /// @dev Retrieve identity information for an account.
        /// @custom:selector f0eb5e54
        /// @param who The requested account
        function identity(address who) external view returns (Registration memory);

        /// @dev Retrieve super account for an account.
        /// @custom:selector c18110d6
        /// @param who The requested account
        function superOf(address who) external view returns (SuperOf memory);

        /// @dev Retrieve sub accounts for an account.
        /// @custom:selector 3f08986b
        /// @param who The requested account
        function subsOf(address who) external view returns (SubsOf memory);

        /// @dev Retrieve the registrars.
        /// @custom:selector e88e512e
        function registrars() external view returns (Registrar[] memory);

        /// @dev Set identity info for the caller.
        /// @custom:selector 7e08b4cb
        /// @param info The identity info
        function setIdentity(IdentityInfo memory info) external;

        /// @dev Set sub accounts for the caller.
        /// @custom:selector 5a5a3591
        /// @param subs The sub accounts
        function setSubs(SubAccount[] memory subs) external;

        /// @dev Clears identity of the caller.
        /// @custom:selector 7a6a10c7
        function clearIdentity() external;

        /// @dev Requests registrar judgement on caller's identity.
        /// @custom:selector d523ceb9
        /// @param regIndex The registrar's index
        /// @param maxFee The maximum fee the caller is willing to pay
        function requestJudgement(uint32 regIndex, uint256 maxFee) external;

        /// @dev Cancels the caller's request for judgement from a registrar.
        /// @custom:selector c79934a5
        /// @param regIndex The registrar's index
        function cancelRequest(uint32 regIndex) external;

        /// @dev Sets the registrar's fee for providing a judgement. Caller must be the account at the index.
        /// @custom:selector a541b37d
        /// @param regIndex The registrar's index
        /// @param fee The fee the registrar will charge
        function setFee(uint32 regIndex, uint256 fee) external;

        /// @dev Sets the registrar's account. Caller must be the account at the index.
        /// @custom:selector 889bc198
        /// @param regIndex The registrar's index
        /// @param newAccount The new account to set
        function setAccountId(uint32 regIndex, address newAccount) external;

        /// @dev Sets the registrar's identity fields. Caller must be the account at the index.
        /// @custom:selector 05297450
        /// @param regIndex The registrar's index
        /// @param fields The identity fields
        function setFields(uint32 regIndex, IdentityFields memory fields) external;

        /// @dev Provides judgement on an accounts identity.
        /// @custom:selector cd7663a4
        /// @param regIndex The registrar's index
        /// @param target The target account to provide judgment for
        /// @param judgement The judgement to provide
        /// @param identity The hash of the identity info
        function provideJudgement(
            uint32 regIndex,
            address target,
            Judgement memory judgement,
            bytes32 identity
        ) external;

        /// @dev Add a "sub" identity account for the caller.
        /// @custom:selector 98717196
        /// @param sub The sub account
        /// @param data The associated data
        function addSub(address sub, Data memory data) external;

        /// @dev Rename a "sub" identity account of the caller.
        /// @custom:selector 452df561
        /// @param sub The sub account
        /// @param data The new associated data
        function renameSub(address sub, Data memory data) external;

        /// @dev Removes a "sub" identity account of the caller.
        /// @custom:selector b0a323e0
        /// @param sub The sub account
        function removeSub(address sub) external;

        /// @dev Removes the sender as a sub-account.
        /// @custom:selector d5a3c2c4
        function quitSub() external;

        /// @dev An identity was set or reset (which will remove all judgements).
        /// @custom:selector 3839f7832b2a6263aa1fd5040f37d10fd4f9e9c4a9ef07ec384cb1cef9fb4c0e
        /// @param who Address of the target account
        event IdentitySet(address who);

        /// @dev An identity was cleared, and the given balance returned.
        /// @custom:selector 3839f7832b2a6263aa1fd5040f37d10fd4f9e9c4a9ef07ec384cb1cef9fb4c0e
        /// @param who Address of the target account
        event IdentityCleared(address who);

        /// @dev A judgement was asked from a registrar.
        /// @custom:selector 3839f7832b2a6263aa1fd5040f37d10fd4f9e9c4a9ef07ec384cb1cef9fb4c0e
        /// @param who Address of the requesting account
        /// @param registrarIndex The registrar's index
        event JudgementRequested(address who, uint32 registrarIndex);

        /// @dev A judgement request was retracted.
        /// @custom:selector 3839f7832b2a6263aa1fd5040f37d10fd4f9e9c4a9ef07ec384cb1cef9fb4c0e
        /// @param who Address of the target account.
        /// @param registrarIndex The registrar's index
        event JudgementUnrequested(address who, uint32 registrarIndex);

        /// @dev A judgement was given by a registrar.
        /// @custom:selector 3839f7832b2a6263aa1fd5040f37d10fd4f9e9c4a9ef07ec384cb1cef9fb4c0e
        /// @param target Address of the target account
        /// @param registrarIndex The registrar's index
        event JudgementGiven(address target, uint32 registrarIndex);

        /// @dev A sub-identity was added to an identity and the deposit paid.
        /// @custom:selector 3839f7832b2a6263aa1fd5040f37d10fd4f9e9c4a9ef07ec384cb1cef9fb4c0e
        /// @param sub Address of the sub account
        /// @param main Address of the main account
        event SubIdentityAdded(address sub, address main);

        /// @dev A sub-identity was removed from an identity and the deposit freed.
        /// @custom:selector 3839f7832b2a6263aa1fd5040f37d10fd4f9e9c4a9ef07ec384cb1cef9fb4c0e
        /// @param sub Address of the sub account
        /// @param main Address of the main account
        event SubIdentityRemoved(address sub, address main);

        /// @dev A sub-identity was cleared and the given deposit repatriated from the main identity account to the sub-identity account
        /// @custom:selector 3839f7832b2a6263aa1fd5040f37d10fd4f9e9c4a9ef07ec384cb1cef9fb4c0e
        /// @param sub Address of the sub account
        event SubIdentityRevoked(address sub);
    }
    ```

The Identity Precompile contains some functions that can be called by anyone and some judgment-related functions that can only be called by a registrar. The functions that can be called by anyone are as follows:

??? function "**identity**(*address* who) - returns registration information for a given account"

    === "Parameters"

        - `who` - address of the account to query the identity information for

??? function "**superOf**(*address* who) - retrieves the super account for a sub-account. If the given account is not a sub-account, the address returned is `0x0000000000000000000000000000000000000000`"

    === "Parameters"

        - `who` - address of the account to query the super-account for

??? function "**subsOf**(*address* who) - returns the sub-accounts for a given account. If the given account doesn't have any sub-accounts, an empty array is returned (`[]`)"

    === "Parameters"

        - `who` - address of the account to query the sub-accounts for

??? function "**registrars**() - returns the list of registrars"

    === "Parameters"

        None.

??? function "**setIdentity**(*IdentityInfo memory* info) - sets the identity for the caller"

    === "Parameters"

        - `info` - IdentityInfo memory struct containing the identity information to be set

??? function "**setSubs**(*SubAccount[] memory* subs) - sets the sub-accounts for the caller"

    === "Parameters"

        - `subs` - SubAccount[] memory array containing the sub-accounts to be set

??? function "**clearIdentity**() - clears the identity for the caller"

    === "Parameters"

        None.

??? function "**requestJudgement**(*uint32* regIndex, *uint256* maxFee) - requests judgment from a given registrar along with the maximum fee the caller is willing to pay"

    === "Parameters"

        - `regIndex` - uint32 index of the registrar to request judgment from
        - `maxFee` - uint256 maximum fee the caller is willing to pay for the judgment

??? function "**cancelRequest**(*uint32* regIndex) - cancels the caller's request for judgment from a given registrar"

    === "Parameters"

        - `regIndex` - uint32 index of the registrar to cancel the judgment request from

??? function "**addSub**(*address* sub, *Data memory* data) - adds a sub-identity account for the caller"

    === "Parameters"

        - `sub` - address of the sub-account to add
        - `data` - Data memory struct containing the sub-account information

??? function "**renameSub**(*address* sub, *Data memory* data) - renames a sub-identity account for the caller"

    === "Parameters"

        - `sub` - address of the sub-account to rename
        - `data` - Data memory struct containing the new sub-account information

??? function "**removeSub**(*address* sub) - removes a sub identity account for the caller"

    === "Parameters"

        - `sub` - address of the sub-account to remove

??? function "**quitSub**(*address* sub) - removes the caller as a sub-identity account"

    === "Parameters"

        - `sub` - address of the sub-account to quit



The judgment-related functions that must be called by a registrar and the caller must be the registrar account that corresponds to the `regIndex` are:

??? function "**setFee**(*uint32* regIndex, *uint256* fee) - sets the fee for a registrar"

    === "Parameters"

        - `regIndex` - uint32 index of the registrar setting the fee
        - `fee` - uint256 new fee amount to be set for the registrar

??? function "**setAccountId**(*uint32* regIndex, *address* newAccount) - sets a new account for a registrar"

    === "Parameters"

        - `regIndex` - uint32 index of the registrar being updated
        - `newAccount` - address of the new account to be set for the registrar

??? function "**setFields**(*uint32* regIndex, *IdentityFields memory* fields) - sets the registrar's identity"

    === "Parameters"

        - `regIndex` - uint32 index of the registrar setting their identity fields
        - `fields` - IdentityFields memory struct containing the identity fields to be set

??? function "**provideJudgement**(*uint32* regIndex, *address* target, *Judgement memory* judgement, *bytes32* identity) - provides judgment on an account's identity"

    === "Parameters"

        - `regIndex` - uint32 index of the registrar providing the judgment
        - `target` - address of the account receiving the judgment
        - `judgement` - Judgement memory struct containing the judgment details
        - `identity` - bytes32 hash of the identity information being judged


## Interact with the Solidity Interface {: #interact-with-interface }

The following sections will cover how to interact with the Identity Precompile using [Ethereum libraries](/moonbeam-mkdocs/builders/ethereum/libraries/), such as [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/) and [Web3.py](/moonbeam-mkdocs/builders/ethereum/libraries/web3py/).

The examples in this guide will be on Moonbase Alpha.
To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
### Using Ethereum Libraries {: #use-ethereum-libraries }

To interact with the Identity Precompile's Solidity interface with an Ethereum library, you'll need the Identity Precompile's ABI.

??? code "Identity Precompile ABI"

    ```js
    [
    	{
    		"anonymous": false,
    		"inputs": [
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "who",
    				"type": "address"
    			}
    		],
    		"name": "IdentityCleared",
    		"type": "event"
    	},
    	{
    		"anonymous": false,
    		"inputs": [
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "who",
    				"type": "address"
    			}
    		],
    		"name": "IdentitySet",
    		"type": "event"
    	},
    	{
    		"anonymous": false,
    		"inputs": [
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "target",
    				"type": "address"
    			},
    			{
    				"indexed": false,
    				"internalType": "uint32",
    				"name": "registrarIndex",
    				"type": "uint32"
    			}
    		],
    		"name": "JudgementGiven",
    		"type": "event"
    	},
    	{
    		"anonymous": false,
    		"inputs": [
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "who",
    				"type": "address"
    			},
    			{
    				"indexed": false,
    				"internalType": "uint32",
    				"name": "registrarIndex",
    				"type": "uint32"
    			}
    		],
    		"name": "JudgementRequested",
    		"type": "event"
    	},
    	{
    		"anonymous": false,
    		"inputs": [
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "who",
    				"type": "address"
    			},
    			{
    				"indexed": false,
    				"internalType": "uint32",
    				"name": "registrarIndex",
    				"type": "uint32"
    			}
    		],
    		"name": "JudgementUnrequested",
    		"type": "event"
    	},
    	{
    		"anonymous": false,
    		"inputs": [
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "sub",
    				"type": "address"
    			},
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "main",
    				"type": "address"
    			}
    		],
    		"name": "SubIdentityAdded",
    		"type": "event"
    	},
    	{
    		"anonymous": false,
    		"inputs": [
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "sub",
    				"type": "address"
    			},
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "main",
    				"type": "address"
    			}
    		],
    		"name": "SubIdentityRemoved",
    		"type": "event"
    	},
    	{
    		"anonymous": false,
    		"inputs": [
    			{
    				"indexed": false,
    				"internalType": "address",
    				"name": "sub",
    				"type": "address"
    			}
    		],
    		"name": "SubIdentityRevoked",
    		"type": "event"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "address",
    				"name": "sub",
    				"type": "address"
    			},
    			{
    				"components": [
    					{
    						"internalType": "bool",
    						"name": "hasData",
    						"type": "bool"
    					},
    					{
    						"internalType": "bytes",
    						"name": "value",
    						"type": "bytes"
    					}
    				],
    				"internalType": "struct Identity.Data",
    				"name": "data",
    				"type": "tuple"
    			}
    		],
    		"name": "addSub",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "uint32",
    				"name": "regIndex",
    				"type": "uint32"
    			}
    		],
    		"name": "cancelRequest",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [],
    		"name": "clearIdentity",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "address",
    				"name": "who",
    				"type": "address"
    			}
    		],
    		"name": "identity",
    		"outputs": [
    			{
    				"components": [
    					{
    						"internalType": "bool",
    						"name": "isValid",
    						"type": "bool"
    					},
    					{
    						"components": [
    							{
    								"internalType": "uint32",
    								"name": "registrarIndex",
    								"type": "uint32"
    							},
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "isUnknown",
    										"type": "bool"
    									},
    									{
    										"internalType": "bool",
    										"name": "isFeePaid",
    										"type": "bool"
    									},
    									{
    										"internalType": "uint256",
    										"name": "feePaidDeposit",
    										"type": "uint256"
    									},
    									{
    										"internalType": "bool",
    										"name": "isReasonable",
    										"type": "bool"
    									},
    									{
    										"internalType": "bool",
    										"name": "isKnownGood",
    										"type": "bool"
    									},
    									{
    										"internalType": "bool",
    										"name": "isOutOfDate",
    										"type": "bool"
    									},
    									{
    										"internalType": "bool",
    										"name": "isLowQuality",
    										"type": "bool"
    									},
    									{
    										"internalType": "bool",
    										"name": "isErroneous",
    										"type": "bool"
    									}
    								],
    								"internalType": "struct Identity.Judgement",
    								"name": "judgement",
    								"type": "tuple"
    							}
    						],
    						"internalType": "struct Identity.JudgementInfo[]",
    						"name": "judgements",
    						"type": "tuple[]"
    					},
    					{
    						"internalType": "uint256",
    						"name": "deposit",
    						"type": "uint256"
    					},
    					{
    						"components": [
    							{
    								"components": [
    									{
    										"components": [
    											{
    												"internalType": "bool",
    												"name": "hasData",
    												"type": "bool"
    											},
    											{
    												"internalType": "bytes",
    												"name": "value",
    												"type": "bytes"
    											}
    										],
    										"internalType": "struct Identity.Data",
    										"name": "key",
    										"type": "tuple"
    									},
    									{
    										"components": [
    											{
    												"internalType": "bool",
    												"name": "hasData",
    												"type": "bool"
    											},
    											{
    												"internalType": "bytes",
    												"name": "value",
    												"type": "bytes"
    											}
    										],
    										"internalType": "struct Identity.Data",
    										"name": "value",
    										"type": "tuple"
    									}
    								],
    								"internalType": "struct Identity.Additional[]",
    								"name": "additional",
    								"type": "tuple[]"
    							},
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "hasData",
    										"type": "bool"
    									},
    									{
    										"internalType": "bytes",
    										"name": "value",
    										"type": "bytes"
    									}
    								],
    								"internalType": "struct Identity.Data",
    								"name": "display",
    								"type": "tuple"
    							},
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "hasData",
    										"type": "bool"
    									},
    									{
    										"internalType": "bytes",
    										"name": "value",
    										"type": "bytes"
    									}
    								],
    								"internalType": "struct Identity.Data",
    								"name": "legal",
    								"type": "tuple"
    							},
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "hasData",
    										"type": "bool"
    									},
    									{
    										"internalType": "bytes",
    										"name": "value",
    										"type": "bytes"
    									}
    								],
    								"internalType": "struct Identity.Data",
    								"name": "web",
    								"type": "tuple"
    							},
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "hasData",
    										"type": "bool"
    									},
    									{
    										"internalType": "bytes",
    										"name": "value",
    										"type": "bytes"
    									}
    								],
    								"internalType": "struct Identity.Data",
    								"name": "riot",
    								"type": "tuple"
    							},
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "hasData",
    										"type": "bool"
    									},
    									{
    										"internalType": "bytes",
    										"name": "value",
    										"type": "bytes"
    									}
    								],
    								"internalType": "struct Identity.Data",
    								"name": "email",
    								"type": "tuple"
    							},
    							{
    								"internalType": "bool",
    								"name": "hasPgpFingerprint",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "pgpFingerprint",
    								"type": "bytes"
    							},
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "hasData",
    										"type": "bool"
    									},
    									{
    										"internalType": "bytes",
    										"name": "value",
    										"type": "bytes"
    									}
    								],
    								"internalType": "struct Identity.Data",
    								"name": "image",
    								"type": "tuple"
    							},
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "hasData",
    										"type": "bool"
    									},
    									{
    										"internalType": "bytes",
    										"name": "value",
    										"type": "bytes"
    									}
    								],
    								"internalType": "struct Identity.Data",
    								"name": "twitter",
    								"type": "tuple"
    							}
    						],
    						"internalType": "struct Identity.IdentityInfo",
    						"name": "info",
    						"type": "tuple"
    					}
    				],
    				"internalType": "struct Identity.Registration",
    				"name": "",
    				"type": "tuple"
    			}
    		],
    		"stateMutability": "view",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "uint32",
    				"name": "regIndex",
    				"type": "uint32"
    			},
    			{
    				"internalType": "address",
    				"name": "target",
    				"type": "address"
    			},
    			{
    				"components": [
    					{
    						"internalType": "bool",
    						"name": "isUnknown",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "isFeePaid",
    						"type": "bool"
    					},
    					{
    						"internalType": "uint256",
    						"name": "feePaidDeposit",
    						"type": "uint256"
    					},
    					{
    						"internalType": "bool",
    						"name": "isReasonable",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "isKnownGood",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "isOutOfDate",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "isLowQuality",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "isErroneous",
    						"type": "bool"
    					}
    				],
    				"internalType": "struct Identity.Judgement",
    				"name": "judgement",
    				"type": "tuple"
    			},
    			{
    				"internalType": "bytes32",
    				"name": "identity",
    				"type": "bytes32"
    			}
    		],
    		"name": "provideJudgement",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [],
    		"name": "quitSub",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [],
    		"name": "registrars",
    		"outputs": [
    			{
    				"components": [
    					{
    						"internalType": "bool",
    						"name": "isValid",
    						"type": "bool"
    					},
    					{
    						"internalType": "uint32",
    						"name": "index",
    						"type": "uint32"
    					},
    					{
    						"internalType": "address",
    						"name": "account",
    						"type": "address"
    					},
    					{
    						"internalType": "uint256",
    						"name": "fee",
    						"type": "uint256"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "display",
    								"type": "bool"
    							},
    							{
    								"internalType": "bool",
    								"name": "legal",
    								"type": "bool"
    							},
    							{
    								"internalType": "bool",
    								"name": "web",
    								"type": "bool"
    							},
    							{
    								"internalType": "bool",
    								"name": "riot",
    								"type": "bool"
    							},
    							{
    								"internalType": "bool",
    								"name": "email",
    								"type": "bool"
    							},
    							{
    								"internalType": "bool",
    								"name": "pgpFingerprint",
    								"type": "bool"
    							},
    							{
    								"internalType": "bool",
    								"name": "image",
    								"type": "bool"
    							},
    							{
    								"internalType": "bool",
    								"name": "twitter",
    								"type": "bool"
    							}
    						],
    						"internalType": "struct Identity.IdentityFields",
    						"name": "fields",
    						"type": "tuple"
    					}
    				],
    				"internalType": "struct Identity.Registrar[]",
    				"name": "",
    				"type": "tuple[]"
    			}
    		],
    		"stateMutability": "view",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "address",
    				"name": "sub",
    				"type": "address"
    			}
    		],
    		"name": "removeSub",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "address",
    				"name": "sub",
    				"type": "address"
    			},
    			{
    				"components": [
    					{
    						"internalType": "bool",
    						"name": "hasData",
    						"type": "bool"
    					},
    					{
    						"internalType": "bytes",
    						"name": "value",
    						"type": "bytes"
    					}
    				],
    				"internalType": "struct Identity.Data",
    				"name": "data",
    				"type": "tuple"
    			}
    		],
    		"name": "renameSub",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "uint32",
    				"name": "regIndex",
    				"type": "uint32"
    			},
    			{
    				"internalType": "uint256",
    				"name": "maxFee",
    				"type": "uint256"
    			}
    		],
    		"name": "requestJudgement",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "uint32",
    				"name": "regIndex",
    				"type": "uint32"
    			},
    			{
    				"internalType": "address",
    				"name": "newAccount",
    				"type": "address"
    			}
    		],
    		"name": "setAccountId",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "uint32",
    				"name": "regIndex",
    				"type": "uint32"
    			},
    			{
    				"internalType": "uint256",
    				"name": "fee",
    				"type": "uint256"
    			}
    		],
    		"name": "setFee",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "uint32",
    				"name": "regIndex",
    				"type": "uint32"
    			},
    			{
    				"components": [
    					{
    						"internalType": "bool",
    						"name": "display",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "legal",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "web",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "riot",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "email",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "pgpFingerprint",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "image",
    						"type": "bool"
    					},
    					{
    						"internalType": "bool",
    						"name": "twitter",
    						"type": "bool"
    					}
    				],
    				"internalType": "struct Identity.IdentityFields",
    				"name": "fields",
    				"type": "tuple"
    			}
    		],
    		"name": "setFields",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"components": [
    					{
    						"components": [
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "hasData",
    										"type": "bool"
    									},
    									{
    										"internalType": "bytes",
    										"name": "value",
    										"type": "bytes"
    									}
    								],
    								"internalType": "struct Identity.Data",
    								"name": "key",
    								"type": "tuple"
    							},
    							{
    								"components": [
    									{
    										"internalType": "bool",
    										"name": "hasData",
    										"type": "bool"
    									},
    									{
    										"internalType": "bytes",
    										"name": "value",
    										"type": "bytes"
    									}
    								],
    								"internalType": "struct Identity.Data",
    								"name": "value",
    								"type": "tuple"
    							}
    						],
    						"internalType": "struct Identity.Additional[]",
    						"name": "additional",
    						"type": "tuple[]"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "hasData",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "value",
    								"type": "bytes"
    							}
    						],
    						"internalType": "struct Identity.Data",
    						"name": "display",
    						"type": "tuple"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "hasData",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "value",
    								"type": "bytes"
    							}
    						],
    						"internalType": "struct Identity.Data",
    						"name": "legal",
    						"type": "tuple"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "hasData",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "value",
    								"type": "bytes"
    							}
    						],
    						"internalType": "struct Identity.Data",
    						"name": "web",
    						"type": "tuple"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "hasData",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "value",
    								"type": "bytes"
    							}
    						],
    						"internalType": "struct Identity.Data",
    						"name": "riot",
    						"type": "tuple"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "hasData",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "value",
    								"type": "bytes"
    							}
    						],
    						"internalType": "struct Identity.Data",
    						"name": "email",
    						"type": "tuple"
    					},
    					{
    						"internalType": "bool",
    						"name": "hasPgpFingerprint",
    						"type": "bool"
    					},
    					{
    						"internalType": "bytes",
    						"name": "pgpFingerprint",
    						"type": "bytes"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "hasData",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "value",
    								"type": "bytes"
    							}
    						],
    						"internalType": "struct Identity.Data",
    						"name": "image",
    						"type": "tuple"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "hasData",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "value",
    								"type": "bytes"
    							}
    						],
    						"internalType": "struct Identity.Data",
    						"name": "twitter",
    						"type": "tuple"
    					}
    				],
    				"internalType": "struct Identity.IdentityInfo",
    				"name": "info",
    				"type": "tuple"
    			}
    		],
    		"name": "setIdentity",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"components": [
    					{
    						"internalType": "address",
    						"name": "account",
    						"type": "address"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "hasData",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "value",
    								"type": "bytes"
    							}
    						],
    						"internalType": "struct Identity.Data",
    						"name": "data",
    						"type": "tuple"
    					}
    				],
    				"internalType": "struct Identity.SubAccount[]",
    				"name": "subs",
    				"type": "tuple[]"
    			}
    		],
    		"name": "setSubs",
    		"outputs": [],
    		"stateMutability": "nonpayable",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "address",
    				"name": "who",
    				"type": "address"
    			}
    		],
    		"name": "subsOf",
    		"outputs": [
    			{
    				"components": [
    					{
    						"internalType": "uint256",
    						"name": "deposit",
    						"type": "uint256"
    					},
    					{
    						"internalType": "address[]",
    						"name": "accounts",
    						"type": "address[]"
    					}
    				],
    				"internalType": "struct Identity.SubsOf",
    				"name": "",
    				"type": "tuple"
    			}
    		],
    		"stateMutability": "view",
    		"type": "function"
    	},
    	{
    		"inputs": [
    			{
    				"internalType": "address",
    				"name": "who",
    				"type": "address"
    			}
    		],
    		"name": "superOf",
    		"outputs": [
    			{
    				"components": [
    					{
    						"internalType": "bool",
    						"name": "isValid",
    						"type": "bool"
    					},
    					{
    						"internalType": "address",
    						"name": "account",
    						"type": "address"
    					},
    					{
    						"components": [
    							{
    								"internalType": "bool",
    								"name": "hasData",
    								"type": "bool"
    							},
    							{
    								"internalType": "bytes",
    								"name": "value",
    								"type": "bytes"
    							}
    						],
    						"internalType": "struct Identity.Data",
    						"name": "data",
    						"type": "tuple"
    					}
    				],
    				"internalType": "struct Identity.SuperOf",
    				"name": "",
    				"type": "tuple"
    			}
    		],
    		"stateMutability": "view",
    		"type": "function"
    	}
    ]
    ```

Once you have the ABI, you can interact with the precompile using the Ethereum library of your choice. Generally speaking, you'll take the following steps:

1. Create a provider
2. Create a contract instance of the Identity Precompile
3. Interact with the Identity Precompile's functions

In the examples below, you'll learn how to assemble the data required to set an identity, how to set an identity, and how to retrieve the identity information once it's been set.

!!! remember
    The following snippets are for demo purposes only. Never store your private keys in a JavaScript or Python file.

=== "Ethers.js"

    ```js
    import { ethers } from 'ethers'; // Import Ethers library
    import ABI from './identityPrecompileABI.js'; // Import Identity Precompile ABI

    const privateKey = 'INSERT_PRIVATE_KEY';
    const identityPrecompileAddress = '0x0000000000000000000000000000000000000818';

    // Create Ethers provider and signer
    const provider = new ethers.JsonRpcProvider(
      'https://rpc.api.moonbase.moonbeam.network'
    );
    const signer = new ethers.Wallet(privateKey, provider);

    // Create interface for the Identity Precompile
    const identityPrecompile = new ethers.Contract(
      identityPrecompileAddress,
      ABI,
      signer
    );

    // Interact with the Precompile Registry
    const setIdentity = async () => {
      // Assemble identity info
      const identityInfo = {
        additional: [],
        display: {
          hasData: true,
          value: '0x416c696365', // Alice in hex
        },
        legal: {
          hasData: false,
          value: '0x',
        },
        web: {
          hasData: false,
          value: '0x',
        },
        riot: {
          hasData: false,
          value: '0x',
        },
        email: {
          hasData: false,
          value: '0x',
        },
        hasPgpFingerprint: false,
        pgpFingerprint: '0x',
        image: {
          hasData: false,
          value: '0x',
        },
        twitter: {
          hasData: false,
          value: '0x',
        },
      };

      // Set the identity
      const submitIdentity = await identityPrecompile.setIdentity(identityInfo);
      console.log(`Identity set. Transaction hash: ${submitIdentity.hash}`);

      // Retrieve the identity
      const identity = await identityPrecompile.identity(signer.address);
      console.log(`Identity is valid: ${identity[0]}`);
      console.log(`Judgements provided for this identity: ${identity[1]}`);
      console.log(`Deposit paid for this identity: ${identity[2]}`);
      console.log(`Identity information: ${identity[3]}`);
      console.log(`Display name: ${ethers.toUtf8String(identity[3][1][1])}`);
    };

    setIdentity();
    ```

=== "Web3.py"

    ```py
    from web3 import Web3

    # Paste or import the Identity Precompile ABI
    abi = "INSERT_IDENTITY_PRECOMPILE_ABI"
    account_from = {
        "private_key": "INSERT_PRIVATE_KEY",
        "address": "INSERT_ADDRESS",
    }
    identity_precompile_address = "0x0000000000000000000000000000000000000818"

    # Create provider
    web3 = Web3(Web3.HTTPProvider("https://rpc.api.moonbase.moonbeam.network"))

    # Create interface for the Precompile Registry
    identity_precompile = web3.eth.contract(address=identity_precompile_address, abi=abi)


    def set_identity():
        # Assemble identity info
        identity_info = {
            "additional": [],
            "display": {
                "hasData": True,
                "value": "0x416c696365",  # Alice in hex
            },
            "legal": {
                "hasData": False,
                "value": "0x",
            },
            "web": {
                "hasData": False,
                "value": "0x",
            },
            "riot": {
                "hasData": False,
                "value": "0x",
            },
            "email": {
                "hasData": False,
                "value": "0x",
            },
            "hasPgpFingerprint": False,
            "pgpFingerprint": "0x",
            "image": {
                "hasData": False,
                "value": "0x",
            },
            "twitter": {
                "hasData": False,
                "value": "0x",
            },
        }

        # Set the identity
        submit_identity = identity_precompile.functions.setIdentity(
            identity_info
        ).build_transaction(
            {
                "from": Web3.to_checksum_address(account_from["address"]),
                "nonce": web3.eth.get_transaction_count(
                    Web3.to_checksum_address(account_from["address"])
                ),
            }
        )
        # Sign and send the transaction to set the identity
        tx_create = web3.eth.account.sign_transaction(
            submit_identity, account_from["private_key"]
        )
        tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Identity set. Transaction hash: { tx_receipt.transactionHash.hex() }")

        # Retrieve the identity
        identity = identity_precompile.functions.identity(account_from["address"]).call()
        print(f"Identity is valid: { identity[0] }")
        print(f"Judgements provided for this identity: { identity[1] }")
        print(f"Deposit paid for this identity: { identity[2] }")
        print(f"Identity information: { identity[3] }")
        print(f"Display name: { web3.to_text(identity[3][1][1]) }")


    set_identity()
    ```
