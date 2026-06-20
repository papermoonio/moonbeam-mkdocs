---
title: XCM Instructions
description: When XCM instructions are combined, they form an XCM message that performs a cross-chain action. Take a look at some of the most common instructions.
categories:
- XCM
- Basics
url: https://docs.moonbeam.network/builders/interoperability/xcm/core-concepts/instructions/
word_count: 820
token_estimate: 1264
version_hash: sha256:44561e9974cc719cd76d9a0c533b60f171287856830e3898b78511a6656bb3bd
last_updated: '2026-05-21T21:21:53+00:00'
---

# XCM Instructions

## Introduction {: #introduction }

XCM messages contain a series of [actions and instructions](https://github.com/paritytech/xcm-format#5-the-xcvm-instruction-set) that are executed by the Cross-Consensus Virtual Machine (XCVM). An action (for example, transferring a token from one blockchain to another) consists of instructions that the XCVM partly executes in the origin and destination chains.

For example, an XCM message that transfers DOT from Polkadot to Moonbeam will include the following XCM instructions (in that order), some of which are executed on Polkadot and some of which are executed on Moonbeam:

 1. [TransferReserveAsset](#transfer-reserve-asset) — executed in Polkadot
 2. [ReserveAssetDeposited](#reserve-asset-deposited) — executed in Moonbeam
 3. [ClearOrigin](#clear-origin) — executed in Moonbeam
 4. [BuyExecution](#buy-execution) — executed in Moonbeam
 5. [DepositAsset](#deposit-asset) — executed in Moonbeam

Building the instructions for an XCM message from scratch is not an easy task. Consequently, there are wrapper functions and pallets that developers can leverage to use XCM features. The [Polkadot XCM](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/xcm-pallet/) and [XCM Transactor](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/substrate-calls/xcm-transactor-pallet/) Pallets provide functions with a predefined set of XCM instructions to either send [XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/) or remotely execute on other chains via XCM.

If you're interested in experimenting with different combinations of instructions, you can [use the Polkadot XCM Pallet to execute and send custom XCM messages](/moonbeam-mkdocs/builders/interoperability/xcm/send-execute-xcm/).

This guide provides an overview of some of the most commonly used XCM instructions, including those in the above example.

## Buy Execution {: #buy-execution }

The [`BuyExecution`](https://github.com/paritytech/xcm-format#buyexecution) instruction typically gets executed in the target chain. It takes assets from the holding register, a temporary position in the Cross-Consensus Virtual Machine (XCVM), to pay for execution fees. The target chain determines the fees to pay.

## Clear Origin {: #clear-origin }

The [`ClearOrigin`](https://github.com/paritytech/xcm-format#clearorigin) instruction gets executed in the target chain. It clears the origin of the XCM author, thereby ensuring that later XCM instructions cannot command the authority of the author.

## Deposit Asset {: #deposit-asset }

The [`DepositAsset`](https://github.com/paritytech/xcm-format#depositasset) instruction gets executed in the target chain. It removes the assets from the holding register, a temporary position in the Cross-Consensus Virtual Machine (XCVM), and sends them to a destination account on the target chain.

## Descend Origin {: #descend-origin }

The [`DescendOrigin`](https://github.com/paritytech/xcm-format#descendorigin) instruction gets executed in the target chain. It mutates the origin on the target chain to match the origin on the source chain, ensuring execution on the target chain occurs on behalf of the same entity initiating the XCM message on the source chain.

## Initiate Reserve Withdraw {: #initiate-reserve-withdraw }

The [`InitiateReserveWithdraw`](https://github.com/paritytech/xcm-format#initiatereservewithdraw) instruction gets executed in the source chain. It removes the assets from the holding register, a temporary position in the Cross-Consensus Virtual Machine (XCVM), (essentially burning them), and sends an XCM message to the reserve chain starting with the `WithdrawAsset` instruction.

## Refund Surplus {: #refund-surplus }

The [`RefundSurplus`](https://github.com/paritytech/xcm-format#refundsurplus) instruction typically gets executed in the target chain after the XCM is processed. This instruction will take any leftover assets from the `BuyExecution` instruction and put the assets into the holding register, a temporary position in the Cross-Consensus Virtual Machine (XCVM).

## Reserve Asset Deposited {: #reserve-asset-deposited }

The [`ReserveAssetDeposited`](https://github.com/paritytech/xcm-format#reserveassetdeposited-) instruction gets executed in the target chain. It takes a representation of the assets received in the Sovereign account and places them into the holding register, a temporary position in the Cross-Consensus Virtual Machine (XCVM).

## Set Appendix {: #set-appendix }

The [`SetAppendix`](https://github.com/paritytech/xcm-format#setappendix) instruction gets executed in the target chain. It sets the appendix register, which holds code that should be run after the current execution is finished.

## Transfer Reserve Asset {: #transfer-reserve-asset }

The [`TransferReserveAsset`](https://github.com/paritytech/xcm-format#transferreserveasset) instruction gets executed in the reserve chain. It moves assets from the origin account and deposits them into a destination account on the target chain. It then sends an XCM message to the target chain with the `ReserveAssetDeposited` instruction, followed by the XCM instructions that are to be executed.

## Transact {: #transact }

The [`Transact`](https://github.com/paritytech/xcm-format#transact) instruction gets executed in the target chain. It dispatches encoded call data from a given origin, allowing for the execution of specific operations or functions on the target chain.

## Withdraw Asset {: #withdraw-asset }

The [`WithdrawAsset`](https://github.com/paritytech/xcm-format#withdrawasset) instruction can be executed in either the source or target chain. It removes assets and places them into the holding register, a temporary position in the Cross-Consensus Virtual Machine (XCVM).
