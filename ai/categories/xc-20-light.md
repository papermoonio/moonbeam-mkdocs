---
category: XC-20
description: Guides for interacting with XC-20 tokens.
page_count: 6
token_estimate: 2279
updated: '2026-06-20T05:24:27.156643+00:00'
---

## Interact with XC-20s
https://docs.moonbeam.network/builders/interoperability/xcm/xc20/interact.md

Check out the XC-20 Solidity interfaces, including the ERC-20 and ERC-20 Permit interfaces, and how to interact with external XC-20s using these interfaces.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- XC-20s Solidity Interface {: #xc20s-solidity-interface } `#xc-20s-solidity-interface-xc20s-solidity-interface`
- The ERC-20 Solidity Interface {: #the-erc20-interface } `#the-erc-20-solidity-interface-the-erc20-interface`
- The ERC-20 Permit Solidity Interface {: #the-erc20-permit-interface } `#the-erc-20-permit-solidity-interface-the-erc20-permit-interface`
- Interact with External XC-20s Using an ERC-20 Interface {: #interact-with-the-precompile-using-remix } `#interact-with-external-xc-20s-using-an-erc-20-interface-interact-with-the-precompile-using-remix`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Calculate External XC-20 Precompile Addresses {: #calculate-xc20-address } `#calculate-external-xc-20-precompile-addresses-calculate-xc20-address`
- Add & Compile the Interface {: #add-the-interface-to-remix } `#add-compile-the-interface-add-the-interface-to-remix`
- Access the Precompile {: #access-the-precompile } `#access-the-precompile-access-the-precompile`

---

## Register XC Assets
https://docs.moonbeam.network/builders/interoperability/xcm/xc-registration/assets.md

This guide includes everything you need to know to register local and external XC-20s so you can begin transferring assets cross-chain via XCM.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Register External XC-20s on Moonbeam {: #register-xc-20s } `#register-external-xc-20s-on-moonbeam-register-xc-20s`
- Create a Forum Post {: #create-a-forum-post } `#create-a-forum-post-create-a-forum-post`
- Calculate Relative Price {: #calculate-relative-price } `#calculate-relative-price-calculate-relative-price`
- Generate the Encoded Calldata for the Asset Registration {: #generate-encoded-calldata-for-asset-registration } `#generate-the-encoded-calldata-for-the-asset-registration-generate-encoded-calldata-for-asset-registration`
- Construct the Add Asset Call `#construct-the-add-asset-call`
- Submit the Preimage and Proposal for Asset Registration {: #submit-preimage-proposal } `#submit-the-preimage-and-proposal-for-asset-registration-submit-preimage-proposal`
- Test the Asset Registration on Moonbeam {: #test-asset-registration } `#test-the-asset-registration-on-moonbeam-test-asset-registration`
- Set XC-20 Precompile Bytecode {: #set-bytecode } `#set-xc-20-precompile-bytecode-set-bytecode`
- Register Moonbeam Assets on Another Chain {: #register-moonbeam-assets-on-another-chain } `#register-moonbeam-assets-on-another-chain-register-moonbeam-assets-on-another-chain`
- Register Moonbeam Native Assets on Another Chain {: #register-moonbeam-native-assets } `#register-moonbeam-native-assets-on-another-chain-register-moonbeam-native-assets`
- Register Local XC-20s on Another Chain {: #register-local-xc20 } `#register-local-xc-20s-on-another-chain-register-local-xc20`
- Managing XC Assets `#managing-xc-assets`
- Updating Foreign Asset XCM Location {: #updating-foreign-asset-xcm-location } `#updating-foreign-asset-xcm-location-updating-foreign-asset-xcm-location`
- Freezing a Foreign Asset {: #freezing-a--foreign-asset } `#freezing-a-foreign-asset-freezing-a-foreign-asset`
- Paying XCM Fees with Foreign Assets {: #paying-xcm-fees-with-foreign-assets } `#paying-xcm-fees-with-foreign-assets-paying-xcm-fees-with-foreign-assets`

---

## Send XC-20s to Other Chains
https://docs.moonbeam.network/builders/interoperability/xcm/xc20/send-xc20s/xcm-pallet.md

This guide introduces the Polkadot XCM Pallet and explains how to send XC-20s to another chain using some of the pallet's extrinsics.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Nomenclature {: #nomenclature } `#nomenclature-nomenclature`
- Polkadot XCM Pallet Interface {: #polkadotxcm-pallet-interface } `#polkadot-xcm-pallet-interface-polkadotxcm-pallet-interface`
- Extrinsics {: #extrinsics } `#extrinsics-extrinsics`
- Storage Methods {: #storage-methods } `#storage-methods-storage-methods`
- Pallet Constants {: #constants } `#pallet-constants-constants`
- Building an XCM Message with the Polkadot XCM Pallet {: #build-with-polkadotxcm-pallet} `#building-an-xcm-message-with-the-polkadot-xcm-pallet-build-with-polkadotxcm-pallet`
- Checking Prerequisites {: #polkadotxcm-check-prerequisites} `#checking-prerequisites-polkadotxcm-check-prerequisites`
- Polkadot XCM Transfer Assets Function {: #polkadotxcm-transfer-assets-function} `#polkadot-xcm-transfer-assets-function-polkadotxcm-transfer-assets-function`

---

## Send XC-20s to Other Chains
https://docs.moonbeam.network/builders/interoperability/xcm/xc20/send-xc20s/xtokens-precompile.md

Learn how to send assets cross-chain via Cross-Consensus Messaging (XCM) using the X-Tokens Precompile with familiar Ethereum libraries like Ethers and Web3.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- X-Tokens Precompile Contract Address {: #contract-address } `#x-tokens-precompile-contract-address-contract-address`
- The X-Tokens Solidity Interface {: #xtokens-solidity-interface } `#the-x-tokens-solidity-interface-xtokens-solidity-interface`
- Building the Precompile Multilocation {: #building-the-precompile-multilocation } `#building-the-precompile-multilocation-building-the-precompile-multilocation`
- Building an XCM Message {: #build-xcm-xtokens-precompile } `#building-an-xcm-message-build-xcm-xtokens-precompile`
- Checking Prerequisites {: #xtokens-check-prerequisites} `#checking-prerequisites-xtokens-check-prerequisites`
- Determining Weight Needed for XCM Execution {: #determining-weight } `#determining-weight-needed-for-xcm-execution-determining-weight`
- X-Tokens Precompile Transfer Function {: #precompile-transfer } `#x-tokens-precompile-transfer-function-precompile-transfer`
- X-Tokens Precompile Transfer Multiasset Function {: #precompile-transfer-multiasset} `#x-tokens-precompile-transfer-multiasset-function-precompile-transfer-multiasset`

---

## XC-20 Transfers Overview
https://docs.moonbeam.network/builders/interoperability/xcm/xc20/send-xc20s/overview.md

Explore the types of asset transfers and some of the fundamentals of remote asset transfers via XCM, including the XCM instructions for asset transfers.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- XCM Instructions for Asset Transfers {: #xcm-instructions-for-asset-transfers } `#xcm-instructions-for-asset-transfers-xcm-instructions-for-asset-transfers`
- Instructions to Transfer a Reserve Asset from the Reserve Chain {: #transfer-native-from-origin } `#instructions-to-transfer-a-reserve-asset-from-the-reserve-chain-transfer-native-from-origin`
- Instructions to Transfer a Reserve Asset back to the Reserve Chain {: #transfer-native-to-origin } `#instructions-to-transfer-a-reserve-asset-back-to-the-reserve-chain-transfer-native-to-origin`

---

## XC-20s and Cross-Chain Assets
https://docs.moonbeam.network/builders/interoperability/xcm/xc20/overview.md

Learn about the types of cross-chain assets on Moonbeam, in particular, local and external XC-20s, and view a list of the external XC-20s on Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Types of XC-20s {: #types-of-xc-20s } `#types-of-xc-20s-types-of-xc-20s`
- What are Local XC-20s? {: #local-xc20s } `#what-are-local-xc-20s-local-xc20s`
- What are External XC-20s? {: #external-xc20s } `#what-are-external-xc-20s-external-xc20s`
- Local XC-20s vs External XC-20s {: #local-xc-20s-vs-external-xc-20s } `#local-xc-20s-vs-external-xc-20s-local-xc-20s-vs-external-xc-20s`
- Asset Reserves {: #asset-reserves } `#asset-reserves-asset-reserves`
- Local Reserve Assets {: #local-reserve-assets } `#local-reserve-assets-local-reserve-assets`
- Remote Reserve Assets {: #remote-reserve-assets } `#remote-reserve-assets-remote-reserve-assets`
- Current List of External XC-20s {: #current-xc20-assets } `#current-list-of-external-xc-20s-current-xc20-assets`
- Retrieve List of External XC-20s and Their Metadata {: #list-xchain-assets } `#retrieve-list-of-external-xc-20s-and-their-metadata-list-xchain-assets`
- Retrieve Local XC-20 Metadata {: #retrieve-local-xc20-metadata } `#retrieve-local-xc-20-metadata-retrieve-local-xc20-metadata`
