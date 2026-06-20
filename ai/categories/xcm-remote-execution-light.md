---
category: XCM Remote Execution
description: How to make cross-chain calls with XCM.
page_count: 5
token_estimate: 1508
updated: '2026-06-20T05:24:27.156643+00:00'
---

## Computed Origin Accounts
https://docs.moonbeam.network/builders/interoperability/xcm/remote-execution/computed-origins.md

Learn about Computed Origin accounts, which can be used to execute remote cross-chain calls through a simple transaction, and how to calculate these accounts.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Origin Conversion {: #origin-conversion } `#the-origin-conversion-origin-conversion`
- How to Calculate the Computed Origin {: #calculate-computed-origin } `#how-to-calculate-the-computed-origin-calculate-computed-origin`
- Calculate the Computed Origin on a Moonbeam-based Network {: #calculate-the-computed-origin-on-moonbeam } `#calculate-the-computed-origin-on-a-moonbeam-based-network-calculate-the-computed-origin-on-moonbeam`

---

## Remote EVM Calls Through XCM
https://docs.moonbeam.network/builders/interoperability/xcm/remote-execution/remote-evm-calls.md

How to do remote calls to smart contracts on Moonbeam EVM through XCM from any Polkadot parachain that has an XCM channel established with Moonbeam.

### Sections
- Introduction {: #introduction} `#introduction-introduction`
- Differences between Regular and Remote EVM Calls through XCM {: #differences-regular-remote-evm} `#differences-between-regular-and-remote-evm-calls-through-xcm-differences-regular-remote-evm`
- Ethereum XCM Pallet Interface {: #ethereum-xcm-pallet-interface} `#ethereum-xcm-pallet-interface-ethereum-xcm-pallet-interface`
- Extrinsics {: #extrinsics } `#extrinsics-extrinsics`
- Building a Remote EVM Call Through XCM {: #build-remote-evm-call-xcm} `#building-a-remote-evm-call-through-xcm-build-remote-evm-call-xcm`
- Checking Prerequisites {: #ethereumxcm-check-prerequisites} `#checking-prerequisites-ethereumxcm-check-prerequisites`
- Ethereum XCM Transact Call Data {: #ethereumxcm-transact-data } `#ethereum-xcm-transact-call-data-ethereumxcm-transact-data`
- Estimate Weight Required at Most {: #estimate-weight-required-at-most } `#estimate-weight-required-at-most-estimate-weight-required-at-most`
- Building the XCM for Remote XCM Execution {: #build-xcm-remote-evm} `#building-the-xcm-for-remote-xcm-execution-build-xcm-remote-evm`
- Remote EVM Call Transaction by Hash {: #remote-evm-call-txhash} `#remote-evm-call-transaction-by-hash-remote-evm-call-txhash`

---

## Remote Execution Overview
https://docs.moonbeam.network/builders/interoperability/xcm/remote-execution/overview.md

Learn the basics of remote execution via XCM messages, which allow users to execute actions on other blockchains using accounts they control remotely via XCM.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Execution Origin {: #execution-origin } `#execution-origin-execution-origin`
- XCM Instructions for Remote Execution {: #xcm-instructions-remote-execution } `#xcm-instructions-for-remote-execution-xcm-instructions-remote-execution`
- General Remote Execution via XCM Flow {: #general-remote-execution-via-xcm-flow } `#general-remote-execution-via-xcm-flow-general-remote-execution-via-xcm-flow`

---

## The XCM Transactor Pallet
https://docs.moonbeam.network/builders/interoperability/xcm/remote-execution/substrate-calls/xcm-transactor-pallet.md

This guide provides an introduction to the XCM Transactor Pallet and explains how to send remote calls to another chain using some of the pallet's extrinsics.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- XCM Transactor Pallet Interface {: #xcm-transactor-pallet-interface} `#xcm-transactor-pallet-interface-xcm-transactor-pallet-interface`
- Extrinsics {: #extrinsics } `#extrinsics-extrinsics`
- Storage Methods {: #storage-methods } `#storage-methods-storage-methods`
- Pallet Constants {: #constants } `#pallet-constants-constants`
- XCM Instructions for Remote Execution {: #xcm-instructions-for-remote-execution } `#xcm-instructions-for-remote-execution-xcm-instructions-for-remote-execution`
- Transact through a Computed Origin Account {: #xcmtransactor-transact-through-signed } `#transact-through-a-computed-origin-account-xcmtransactor-transact-through-signed`
- Checking Prerequisites {: #xcmtransactor-signed-check-prerequisites } `#checking-prerequisites-xcmtransactor-signed-check-prerequisites`
- Building the XCM {: #xcm-transact-through-signed } `#building-the-xcm-xcm-transact-through-signed`
- Sending the XCM {: #sending-the-xcm } `#sending-the-xcm-sending-the-xcm`
- XCM Transact through Computed Origin Fees {: #transact-through-computed-origin-fees } `#xcm-transact-through-computed-origin-fees-transact-through-computed-origin-fees`

---

## The XCM Transactor Precompile
https://docs.moonbeam.network/builders/interoperability/xcm/remote-execution/substrate-calls/xcm-transactor-precompile.md

This guide describes the XCM Transactor Precompile and shows how to use some of its functions to send remote calls to other chains using Ethereum libraries.

### Sections
- XCM Transactor Precompile Contract Address {: #precompile-address } `#xcm-transactor-precompile-contract-address-precompile-address`
- The XCM Transactor Solidity Interface {: #xcmtrasactor-solidity-interface } `#the-xcm-transactor-solidity-interface-xcmtrasactor-solidity-interface`
- XCM Instructions for Remote Execution {: #xcm-instructions-for-remote-execution } `#xcm-instructions-for-remote-execution-xcm-instructions-for-remote-execution`
- Building the Precompile Multilocation {: #building-the-precompile-multilocation } `#building-the-precompile-multilocation-building-the-precompile-multilocation`
- Transact through a Computed Origin Account {: #xcmtransactor-transact-through-signed } `#transact-through-a-computed-origin-account-xcmtransactor-transact-through-signed`
- Checking Prerequisites {: #xcmtransactor-signed-check-prerequisites } `#checking-prerequisites-xcmtransactor-signed-check-prerequisites`
- Building the XCM {: #xcm-transact-through-signed } `#building-the-xcm-xcm-transact-through-signed`
- XCM Transact through Computed Origin Fees {: #transact-through-computed-origin-fees } `#xcm-transact-through-computed-origin-fees-transact-through-computed-origin-fees`
