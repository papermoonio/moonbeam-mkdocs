---
title: Cross-Consensus Messaging (XCM)
description: An overview of how cross-consensus messaging (XCM) works and how developers can leverage Polkadot/Kusama XCM to gain access to new assets.
categories:
- Basics
- XCM
url: https://docs.moonbeam.network/builders/interoperability/xcm/overview/
word_count: 2687
token_estimate: 3758
version_hash: sha256:f263b87b374121c41d8039cfb4beddd60f1def6a27ce3b66eff3ec9c07766388
last_updated: '2026-05-21T21:21:53+00:00'
---

# Cross-Consensus Messaging (XCM)

## Introduction {: #introduction }

[Polkadot's architecture](https://wiki.polkadot.com/learn/learn-architecture/) allows parachains to natively interoperate with each other, enabling cross-blockchain transfers of any type of data or asset.

To do so, a [Cross-Consensus Message (XCM)](https://wiki.polkadot.com/learn/learn-xcm/) format defines a language around how the message transfer between two interoperating blockchains should be performed. XCM is not specific to Polkadot, as it aims to be a generic and extensible language between different consensus systems.

This page is a brief introduction and overview of XCM and other related elements. More information can be found in [Polkadot's Wiki](https://wiki.polkadot.com/learn/learn-xcm/).

If you want to jump to more XCM-related content, feel free to check out the following pages:

- [**Core XCM Concepts**](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/) - learn topics related to [XCM Instructions](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/), [Multilocations](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/multilocations/), and [XCM Fees](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/weights-fees/)
- [**XC Registration**](/moonbeam-mkdocs/builders/interoperability/xcm/xc-registration/) - go through the process of [Opening an XCM Channel with Moonbeam](/moonbeam-mkdocs/builders/interoperability/xcm/xc-registration/xc-integration/) and how to [Register Polkadot Native Assets as XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc-registrationassets/)
- [**XC-20s**](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/) - read an [Overview](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/) of this Moonbeam-only asset class and learn how to [Interact with XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/interact/) and how to [Send them via XCM](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/)
- [**Remote Execution via XCM**](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/) - grasp all concepts related to remote execution via XCM, starting with a [High-Level Overview](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/overview/), then [Computed Origins](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/computed-origins/) and wrapping up with [Remote Calls via XCM](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/substrate-calls/) and [Remote EVM Calls via XCM](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/remote-evm-calls/)
- [**XCM SDK**](https://moonbeam-foundation.github.io/xcm-sdk/latest/) - learn how to [Use Moonbeam's XCM SDK](https://moonbeam-foundation.github.io/xcm-sdk/latest/example-usage/xcm/)
- **XCM Debugging and Tools** - learn how to test some XCM scenarios by  [Sending and Executing Generic XCM Messages](/moonbeam-mkdocs/builders/interoperability/xcm/send-execute-xcm/), or how to use the [XCM Utilities Precompile](/moonbeam-mkdocs/builders/interoperability/xcm/xcm-utils/) to access XCM_related utility functions directly within the EVM

## General XCM Definitions {: #general-xcm-definitions }

 - **XCM** — stands for Cross-Consensus Message. It is a general way for consensus systems to communicate with each other
 - **VMP** — stands for Vertical Message Passing, one of the transport methods for XCMs. It allows parachains to exchange messages with the relay chain. *UMP* (Upward Message Passing) enables parachains to send messages to their relay chain, while *DMP* (Downward Message Passing) enables the relay chain to pass messages down to one of their parachains
 - **XCMP** — stands for Cross-Consensus Message Passing, one of the transport methods for XCMs. It allows parachains to exchange messages with other parachains on the same relay chain
 - **HRMP** — stands for Horizontal Relay-routed Message Passing, a stop-gap protocol while a full XCMP implementation is launched. It has the same interface as XCMP, but messages are stored on the relay chain
 - **Sovereign account** —  an account each chain in the ecosystem has, one for the relay chain and the other for other parachains. It is calculated as the `blake2` hash of a specific word and parachain ID concatenated (`blake2(para+ParachainID)` for the Sovereign account in the relay chain, and `blake2(sibl+ParachainID)` for the Sovereign account in other parachains), truncating the hash to the correct length. The account is owned by root and can only be used through SUDO (if available) or [governance (referenda)](/moonbeam-mkdocs/learn/features/governance/). The Sovereign account typically signs XCM messages in other chains in the ecosystem
 - **Multilocation** —  a way to specify a point in the entire relay chain/parachain ecosystem relative to a given origin. For example, it can be used to specify a specific parachain, asset, account, or even a pallet inside a parachain. In general terms, a multilocation is defined with a `parents` and an `interior`:
 
    - `parents` - refers to how many "hops" into a parent blockchain you need to take from a given origin
    - `interior` - refers to how many fields you need to define the target point. 
    
    For example, to target a parachain with ID `1000` from another parachain, the multilocation would be `{ "parents": 1, "interior": { "X1": [{ "Parachain": 1000 }]}}`
## Cross-Chain Transport Protocols via XCM {: #xcm-transport-protocols }

XCM implements two cross-consensus or transport protocols for acting on XCM messages between its constituent parachains, Moonbeam being one of them:

- **Vertical Message Passing (VMP)** — once a project is onboarded as a parachain, it automatically has a bi-directional communication channel with the relay chain. Therefore, there is no need for chain registration. VMP is divided into two kinds of message-passing transport protocols:

    * **Upward Message Passing (UMP)** — allows parachains to send messages to their relay chain, for example, from Moonbeam to Polkadot
    * **Downward Message Passing (DMP)** — allows the relay chain to pass messages down to one of their parachains, for example, from Polkadot to Moonbeam

- **Cross-Chain Message Passing (XCMP)** — allows two parachains to exchange messages as long as they are connected to the same relay chain. Cross-chain transactions are resolved using a simple queuing mechanism based on a Merkle tree to ensure fidelity. Collators exchange messages between parachains, while the relay chain validators will verify that the message transmission happened

!!! note
    Currently, while XCMP is being developed, a stop-gap protocol is implemented called Horizontal Relay-routed Message Passing (HRMP), in which the messages are stored in and read from the relay chain. This will be deprecated in the future for the full XCMP implementation.

![Vertical Message Passing and Cross-chain Message Passing Overview](/moonbeam-mkdocs/images/builders/interoperability/xcm/overview/overview-1.webp)

## Establishing Cross-Chain Communication {: #channel-registration }

Before two chains can start communicating, a messaging channel must be opened. Channels are unidirectional, meaning that a channel from chain A to chain B will only pass messages from A to B. Therefore, two channels must be opened to send messages back and forth.

A channel for XCMs between the relay chain and parachain is automatically opened when a connection is established. However, when parachain A wants to open a communication channel with parachain B, parachain A must send an open channel extrinsic to its network. This extrinsic is an XCM as well!

Even though parachain A has expressed its intentions of opening an XCM channel with parachain B, the latter has not signaled to the relay chain its intentions to receive messages from parachain A. Therefore, to have an established channel, parachain B must send an extrinsic (an XCM) to the relay chain. The accepting channel extrinsic is similar to the previous one. However, the encoded call data only includes the new method (accept channel) and the parachain ID of the sender (parachain A in this example). Once both parachains have agreed, the channel is opened within the following epoch.

To learn more about the channel registration process, please refer to the [How to Establish an XC Integration with Moonbeam](/moonbeam-mkdocs/builders/interoperability/xcm/xc-registration/xc-integration/) guide.

![XCM Channel Registration Overview](/moonbeam-mkdocs/images/builders/interoperability/xcm/overview/overview-2.webp)

Once the channel is established, cross-chain messages can be sent between parachains. For asset transfers, assets need to be registered before being transferred through XCMs, either by being baked into the runtime as a constant or through a pallet. Moonbeam relies on a Substrate pallet to handle asset registration without the need for runtime upgrades, making the process a lot simpler.

To learn how to register an asset on Moonbeam and the information necessary to add Moonbeam assets to another chain, please refer to the [How to Register Cross-Chain Assets](/moonbeam-mkdocs/builders/interoperability/xcm/xc-registrationassets/) guide.

## XCM on Moonbeam {: #moonbeam-and-xcm }

As Moonbeam is a parachain within the Polkadot ecosystems, one of the most direct implementations of XCM is to enable asset transfer from Polkadot and other parachains from/to Moonbeam. This allows users to bring their tokens to Moonbeam and all its dApps.

To this end, Moonbeam has introduced [XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/), which expand on Moonbeam's unique Ethereum compatibility features. XC-20s allow Polkadot native assets to be represented via a standard [ERC-20 interface](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/balances-erc20/ERC20.sol) through a precompiled contract. When these assets are registered on Moonbeam, they can be set as XCM execution fee assets. Consequently, when a user transfers such an asset to Moonbeam, a small part of the amount will be used to cover the XCM execution fees.

In addition, ERC-20s that are deployed to Moonbeam can be sent to other chains in the Polkadot ecosystem via XCM. Consequently, from a developer's perspective, XC-20s are ERC-20 tokens with the added benefit of being an XCM cross-chain asset, and dApps can easily support them through a familiar ERC-20 interface.

![Moonbeam XC-20 XCM Integration With Polkadot](/moonbeam-mkdocs/images/builders/interoperability/xcm/overview/overview-3.webp)

To send XC-20s across the Polkadot ecosystem from Moonbeam, developers need to use the [Polkadot XCM Pallet](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/xcm-pallet/) for transfers via the Substrate API and the [X-Tokens Precompile](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/xtokens-precompile/) or the [XCM Precompile](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/eth-api/) for transfers via the Ethereum API.

Another unique feature of Moonbeam is the ability to initiate XCM actions from EVM smart contracts or to call its EVM through XCM messages via remote execution. This unlocks a new set of possibilities, where contracts on Moonbeam can access parachain-specific functionalities via XCM, or other parachain ecosystems can use EVM smart contracts on Moonbeam to expand their functions.

The following sections provide a high-level overview of the main use cases mentioned before.

### XCM Transfers between Moonbeam & Polkadot {: #transfers-moonbeam-polkadot }

As Moonbeam is a parachain within the Polkadot ecosystem, a straightforward implementation of XCM + VMP is DOT transfers from/to Polkadot/Moonbeam. To this end, DOT was registered as [_xcDOT_](https://moonscan.io/token/0xffffffff1fcacbd218edc0eba20fc2308c778080) on Moonbeam.

Alice (Polkadot) wants to transfer a certain amount of DOT from Polkadot to her account on Moonbeam, named Alith. Therefore, she initiates an XCM that expresses her intentions. For such transfers, Moonbeam owns a Sovereign account on Polkadot.

Consequently, the XCM message execution on Polkadot will transfer the amount of DOT to Moonbeam's Sovereign account on Polkadot. Once the assets are deposited, the second part of the message is sent to Moonbeam.

Moonbeam will locally execute the action the XCM message is programmed to do. In this case, it is to mint and transfer the same amount of _xcDOT_ to the account defined by Alice, which in this case is Alith. The fee to execute the XCM in the target parachain is paid in the asset being transferred (_xcDOT_ for this example).

![Transfers from the Relay Chain to Moonbeam](/moonbeam-mkdocs/images/builders/interoperability/xcm/overview/overview-4.webp)

Note the following:

- The Alice and Alith accounts can be different. For example, Polkadot's accounts are SR25519 (or ED25519), while Moonbeam's are ECDSA (Ethereum-styled) accounts. They can also have different owners
- There is a certain degree of trust where one chain relies on the other to execute its part of the XCM message. This is programmed at a runtime level so that it can be easily verified
- For this example, _xcDOT_ is a wrapped representation of the original DOT being held in Moonbeam's Sovereign account on Polkadot. _xcDOT_ can be transferred within Moonbeam at any time, and they can be redeemed for DOT on a 1:1 basis as well (minus some fees)

Alith deposited her _xcDOT_ in a liquidity pool. Next, Charleth acquires some _xcDOT_ by swapping against that liquidity pool, and he wants to transfer some _xcDOT_ to Charley's Polkadot account. Therefore, he initiates an XCM that expresses his intentions.

Consequently, the XCM message execution on Moonbeam will burn the number of _xcDOT_. Once the assets are burned, the second part of the message is sent to Polkadot.

Polkadot will execute the action the XCM message is programmed to do locally. In this case, it is to transfer the same amount of _xcDOT_ burned from the Moonbeam Sovereign account to the account defined by Charleth, which in this case is Charley.

![Transfers Back from Moonbeam to the Relay Chain](/moonbeam-mkdocs/images/builders/interoperability/xcm/overview/overview-5.webp)

### XCM Transfers between Moonbeam & Other Parachains {: #transfers-moonbeam-other-parachains }

Since Moonbeam is a parachain within the Polkadot ecosystem, a straightforward implementation of XCM and XCMP asset transfers from and to Moonbeam and other parachains. This section gives a high-level overview of the main differences compared to XCMs from Polkadot/Moonbeam.

The first requirement is that a bidirectional channel between the parachains must exist, and the asset being transferred must be registered in the target parachain. Only when both conditions are met can XCMs be sent between parachains.

Then, when Alith (Moonbeam) transfers a certain amount of GLMR from Moonbeam to another account (Alice) in a target parachain, tokens are sent to a Sovereign Account owned by that target parachain on Moonbeam.

As the XCM message is executed in the target parachain, it is expected that this will mint and transfer the same amount of _xcGLMR_ (cross-chain GLMR) to the account defined by Alith, which in this case is Alice. The fee to execute the XCM in the target parachain is paid in the transferred asset (_xcGLMR_ for this example).

![Transfers from Moonbeam to another Parachain](/moonbeam-mkdocs/images/builders/interoperability/xcm/overview/overview-6.webp)

As explained in the previous section, the process is similar for _xcGLMR_ to move back to Moonbeam. First, the XCM message execution burns the number of _xcGLMR_ returned to Moonbeam. Once burned, the remnant part of the message is sent to Moonbeam via the relay chain. Moonbeam will locally execute the XCM message's and transfer GLMR (the same amount of burned _xcGLMR_) from the target parachain Sovereign account to the specified address.

### Remote Execution between Other Chains & Moonbeam {: #execution-chains-moonbeam }

As mentioned before, XCM also enables remote execution from/to Moonbeam to other chains in the Polkadot ecosystem.

Similarly to the other use cases, it is necessary for XCM-specific channels to be established before remote execution can happen between the chains. Channels are general-purpose, so they can be used for both asset transfers and remote execution.

Another important component is the asset for which the remote execution fees are paid. On Moonbeam, when an XC-20 is registered, it can be set as an XCM execution fee asset. Consequently, when transferring that XC-20 to Moonbeam, the XCM execution fee is deducted from the amount being transferred. For remote execution, users can include a small amount of tokens in the XCM message to cover XCM execution fees.

Alice (Polkadot) wants to perform a certain remote action through a smart contract on Moonbeam. Therefore, she initiates an XCM that expresses her intentions; she must have previously funded the XCM execution account she owns on Moonbeam with either GLMR or _xcDOT_.

Moonbeam will locally execute the action the XCM message is programmed to do. In this case, it is to withdraw the asset decided by Alice for the XCM execution fee and buy some execution time on Moonbeam to execute the smart contract call on Moonbeam's EVM.

You can read more about the flow in detail on the [Remote Execution](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/overview/) page.
