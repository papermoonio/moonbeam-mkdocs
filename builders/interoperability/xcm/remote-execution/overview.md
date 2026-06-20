---
title: Remote Execution Overview
description: Learn the basics of remote execution via XCM messages, which allow users to execute actions on other blockchains using accounts they control remotely via XCM.
categories:
- XCM Remote Execution
- Basics
url: https://docs.moonbeam.network/builders/interoperability/xcm/remote-execution/overview/
word_count: 919
token_estimate: 1344
version_hash: sha256:ae8aa736fa28cf8beda59e6d4a42d0c2af3e0b3889b2fdb2f390aedf8a72dc81
last_updated: '2026-05-21T21:21:53+00:00'
---

# Remote Execution via XCM

## Introduction {: #introduction }

The [Cross-Consensus Message (XCM)](https://wiki.polkadot.com/learn/learn-xcm/) format defines how messages can be sent between interoperable blockchains. This format opens the door to sending an XCM message that executes an arbitrary set of bytes in a Moonbeam-based network, the relay chain, or other parachains in the Polkadot/Kusama ecosystems.

Remote execution via XCM opens a new set of possibilities for cross-chain interactions, from chains executing actions on other chains to users performing remote actions without switching chains.

This page covers the fundamentals of XCM remote execution. If you want to learn how to perform remote execution via XCM, please refer to the [Remote Execution via the Substrate API](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/substrate-calls/xcm-transactor-pallet/) or the [Remote Execution via the Ethereum API](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/xtokens-precompile/) guides.

## Execution Origin {: #execution-origin }

Generally speaking, all transactions have an origin, which is where a call comes from. Ethereum transactions have only one origin type, the `msg.sender`, which is the account that initiated the transaction.

Substrate-based transactions are more complex, as they can have different origins with different privilege levels. This is similar to having an EVM smart contract call with a specific `require` statement in which the call must come from an allowed address. In contrast, these privilege levels are programmed in the Substrate-based runtime itself.

Origins are super important across different components of the Substrate runtime and, hence, the Moonbeam runtime. For example, they define the authority level they inherit in the [on-chain governance implementation](/moonbeam-mkdocs/learn/features/governance/).

During the execution of an XCM message, the origin defines the context in which the XCM is being executed. By default, the XCM is executed by the source chain's Sovereign account in the destination chain. This Polkadot-specific property of having remote origins that are calculated when executing XCM is known as [Computed Origins](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/computed-origins/) (formerly known as Multilocation Derivative Accounts).

Depending on the destination chain's configuration, including the `DescendOrigin` XCM instruction can mutate the origin from which the XCM message is executed. This property is significant for remote XCM execution, as the action being executed considers the context of the newly mutated origin and not the source chain's Sovereign account.

## XCM Instructions for Remote Execution {: #xcm-instructions-remote-execution }

The core XCM instructions required to perform remote execution on Moonbeam (as an example) via XCM are the following:

 - [`DescendOrigin`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#descend-origin) - (optional) gets executed in Moonbeam. Mutates the origin to create a new Computed Origin that represents a keyless account controlled via XCM by the sender in the source chain
 - [`WithdrawAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#withdraw-asset) - gets executed in Moonbeam. Takes funds from the Computed Origin
 - [`BuyExecution`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#buy-execution) - gets executed in Moonbeam. Uses the funds taken by the previous XCM instruction to pay for the XCM execution, including the remote call
 - [`Transact`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#transact) - gets executed in Moonbeam. Executes the arbitrary bytes provided in the XCM instruction

The XCM instructions detailed above can be complemented by other XCM instructions to handle certain scenarios, like failure on execution, more accurately. One example is the inclusion of [`SetAppendix`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#set-appendix), [`RefundSurplus`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#refund-surplus), and [`Deposit`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#deposit-asset).

## General Remote Execution via XCM Flow {: #general-remote-execution-via-xcm-flow }

A user initiates a transaction in the source chain through a pallet that builds the XCM with at least the [required XCM instructions for remote execution](#xcm-instructions-remote-execution). The transaction is executed in the source chain, which sends an XCM message with the given instructions to the destination chain.

The XCM message arrives at the destination chain, which executes it. It is executed with the source chain's Sovereign account as a Computed Origin by default. One example that uses this type of origin is when chains open or accept an HRMP channel on the relay chain.

If the XCM message included a [`DescendOrigin`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#descend-origin) instruction, the destination chain may mutate the origin to calculate a new Computed Origin (as is the case with Moonbeam-based networks).

Next, [`WithdrawAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#withdraw-asset) takes funds from the Computed Origin (either a Sovereign account or mutated), which are then used to pay for the XCM execution through the [`BuyExecution`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#buy-execution) XCM instruction. Note that on both instructions, you need to specify which asset you want to use. In addition, you must include the bytes to be executed in the amount of execution to buy.

Lastly, [`Transact`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#transact) executes an arbitrary set of bytes that correspond to a pallet and function in the destination chain. You have to specify the type of origin to use (typically `SovereignAccount`) and the weight required to execute the bytes (similar to gas in the Ethereum realm).

![Diagram of the XCM instructions executed on the destination chain for remote execution.](/moonbeam-mkdocs/images/builders/interoperability/xcm/remote-execution/overview/overview-1.webp)
