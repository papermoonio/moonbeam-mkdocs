---
category: XCM
description: Learn about and use Cross-Consensus Messaging (XCM).
page_count: 12
token_estimate: 4246
updated: '2026-06-20T05:24:27.156643+00:00'
---

## Cross-Consensus Messaging (XCM)
https://docs.moonbeam.network/builders/interoperability/xcm/overview.md

An overview of how cross-consensus messaging (XCM) works and how developers can leverage Polkadot/Kusama XCM to gain access to new assets.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- General XCM Definitions {: #general-xcm-definitions } `#general-xcm-definitions-general-xcm-definitions`
- Cross-Chain Transport Protocols via XCM {: #xcm-transport-protocols } `#cross-chain-transport-protocols-via-xcm-xcm-transport-protocols`
- Establishing Cross-Chain Communication {: #channel-registration } `#establishing-cross-chain-communication-channel-registration`
- XCM on Moonbeam {: #moonbeam-and-xcm } `#xcm-on-moonbeam-moonbeam-and-xcm`
- XCM Transfers between Moonbeam & Polkadot {: #transfers-moonbeam-polkadot } `#xcm-transfers-between-moonbeam-polkadot-transfers-moonbeam-polkadot`
- XCM Transfers between Moonbeam & Other Parachains {: #transfers-moonbeam-other-parachains } `#xcm-transfers-between-moonbeam-other-parachains-transfers-moonbeam-other-parachains`
- Remote Execution between Other Chains & Moonbeam {: #execution-chains-moonbeam } `#remote-execution-between-other-chains-moonbeam-execution-chains-moonbeam`

---

## Forum Templates for XCM Integrations
https://docs.moonbeam.network/builders/interoperability/xcm/xc-registration/forum-templates.md

Learn about and how to craft the two posts you need to make on the Moonbeam Community Forum when creating a cross-chain integration with Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- XCM Disclosures {: #xcm-disclosure } `#xcm-disclosures-xcm-disclosure`
- XCM Proposals {: #xcm-proposals } `#xcm-proposals-xcm-proposals`

---

## Moonbeam Routed Liquidity
https://docs.moonbeam.network/builders/interoperability/mrl.md

Learn how to receive Moonbeam Routed Liquidity after establishing a cross-chain integration with a Moonbeam-based network.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Prerequisites {: #prerequisites } `#prerequisites-prerequisites`
- MRL Through Wormhole {: #mrl-through-wormhole } `#mrl-through-wormhole-mrl-through-wormhole`
- Send Tokens Through Wormhole to a Parachain {: #sending-tokens-through-wormhole } `#send-tokens-through-wormhole-to-a-parachain-sending-tokens-through-wormhole`
- Send Tokens From a Parachain Back Through Wormhole {: #sending-tokens-back-through-wormhole } `#send-tokens-from-a-parachain-back-through-wormhole-sending-tokens-back-through-wormhole`
- Tokens Available Through Wormhole {: #tokens-available-through-wormhole } `#tokens-available-through-wormhole-tokens-available-through-wormhole`

---

## Open a Cross-Chain Channel
https://docs.moonbeam.network/builders/interoperability/xcm/xc-registration/xc-integration.md

Learn how to establish a cross-chain integration with a Moonbeam-based network. Including opening and accepting an HRMP channel and registering assets.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Moonbase Alpha XCM Integration Overview {: #moonbase-alpha-xcm } `#moonbase-alpha-xcm-integration-overview-moonbase-alpha-xcm`
- Sync a Node {: #sync-a-node } `#sync-a-node-sync-a-node`
- Calculate and Fund the Parachain Sovereign Account {: #calculate-and-fund-the-parachain-sovereign-account } `#calculate-and-fund-the-parachain-sovereign-account-calculate-and-fund-the-parachain-sovereign-account`
- Moonriver & Moonbeam XCM Integration Overview {: #moonriver-moonbeam } `#moonriver-moonbeam-xcm-integration-overview-moonriver-moonbeam`
- Create Forum Posts {: #create-forum-posts } `#create-forum-posts-create-forum-posts`
- Creating HRMP Channels {: #create-an-hrmp-channel } `#creating-hrmp-channels-create-an-hrmp-channel`
- Accept an HRMP Channel on Moonbeam {: #accept-an-hrmp-channel-on-moonbeam } `#accept-an-hrmp-channel-on-moonbeam-accept-an-hrmp-channel-on-moonbeam`
- Open HRMP Channels from Moonbeam {: #open-an-hrmp-channel-from-moonbeam } `#open-hrmp-channels-from-moonbeam-open-an-hrmp-channel-from-moonbeam`
- Batch Actions Into One {: #batch-actions-into-one } `#batch-actions-into-one-batch-actions-into-one`
- Additional Flags for XCM-Tools {: #additional-flags-xcm-tools } `#additional-flags-for-xcm-tools-additional-flags-xcm-tools`

---

## Self-Serve Asset Registration
https://docs.moonbeam.network/builders/interoperability/xcm/xc-registration/self-serve-asset-registration.md

This guide shows sibling parachains how to register native tokens as foreign assets on Moonbeam via ForeignAssetOwnerOrigin to unlock ERC-20 UX on Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Why a New Origin? {: #why-a-new-origin } `#why-a-new-origin-why-a-new-origin`
- Required Deposits {: #required-deposits } `#required-deposits-required-deposits`
- Prerequisites {: #prerequisites } `#prerequisites-prerequisites`
- Assemble Your Asset Details {: #assemble-your-asset-details } `#assemble-your-asset-details-assemble-your-asset-details`
- How to Calculate Asset ID {: #calculate-asset-id } `#how-to-calculate-asset-id-calculate-asset-id`
- Derive the XC-20 Address `#derive-the-xc-20-address`
- Generate the Encoded Call Data {: #generate-the-encoded-call-data } `#generate-the-encoded-call-data-generate-the-encoded-call-data`
- Dispatch the Call with XCM Transact {: #dispatch-the-call-with-xcm-transact } `#dispatch-the-call-with-xcm-transact-dispatch-the-call-with-xcm-transact`
- Managing an Existing Foreign Asset {: #managing-an-existing-foreign-asset } `#managing-an-existing-foreign-asset-managing-an-existing-foreign-asset`
- FAQs {: #faqs } `#faqs-faqs`
- How do I reclaim the deposit? `#how-do-i-reclaim-the-deposit`
- Can a normal EOA register an asset? `#can-a-normal-eoa-register-an-asset`
- What happens if my XCM location is outside my origin? `#what-happens-if-my-xcm-location-is-outside-my-origin`
- Is there a limit to how many assets can be created? `#is-there-a-limit-to-how-many-assets-can-be-created`

---

## Send, Execute and Test XCM Messages
https://docs.moonbeam.network/builders/interoperability/xcm/send-execute-xcm.md

Build a custom XCM message, verify its construction and integrity using the XCM Dry Run API, and then execute it locally on Moonbeam to observe the results.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Polkadot XCM Pallet Interface {: #polkadot-xcm-pallet-interface } `#polkadot-xcm-pallet-interface-polkadot-xcm-pallet-interface`
- Extrinsics {: #extrinsics } `#extrinsics-extrinsics`
- Storage Methods {: #storage-methods } `#storage-methods-storage-methods`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Execute an XCM Message Locally {: #execute-an-xcm-message-locally } `#execute-an-xcm-message-locally-execute-an-xcm-message-locally`
- Execute an XCM Message with the Polkadot.js API {: #execute-an-xcm-message-with-polkadotjs-api } `#execute-an-xcm-message-with-the-polkadotjs-api-execute-an-xcm-message-with-polkadotjs-api`
- Test an XCM Message with the Dry Run API {: #test-an-xcm-message-with-the-dry-run-api } `#test-an-xcm-message-with-the-dry-run-api-test-an-xcm-message-with-the-dry-run-api`
- Dry Run Call API Method {: #dry-run-call-api-method } `#dry-run-call-api-method-dry-run-call-api-method`
- Dry Run XCM API Method {: #dry-run-xcm-api-method } `#dry-run-xcm-api-method-dry-run-xcm-api-method`
- Execute an XCM Message with the XCM Utilities Precompile {: #execute-xcm-utils-precompile } `#execute-an-xcm-message-with-the-xcm-utilities-precompile-execute-xcm-utils-precompile`
- Generate the Encoded Calldata of an XCM Message {: #generate-encoded-calldata } `#generate-the-encoded-calldata-of-an-xcm-message-generate-encoded-calldata`
- Execute the XCM Message {: #execute-xcm-message } `#execute-the-xcm-message-execute-xcm-message`
- Send an XCM Message Cross-Chain {: #send-xcm-message } `#send-an-xcm-message-cross-chain-send-xcm-message`
- Send an XCM Message with the Polkadot.js API {: #send-xcm-message-with-polkadotjs-api } `#send-an-xcm-message-with-the-polkadotjs-api-send-xcm-message-with-polkadotjs-api`
- Send an XCM Message with the XCM Utilities Precompile {: #send-xcm-utils-precompile } `#send-an-xcm-message-with-the-xcm-utilities-precompile-send-xcm-utils-precompile`

---

## Sovereign Accounts and Reserve-Backed Transfers
https://docs.moonbeam.network/builders/interoperability/xcm/core-concepts/sovereign-accounts.md

Discover how sovereign accounts work on Moonbeam, how to calculate them, and their role in cross-chain asset transfers.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Calculating a Parachain Sovereign Account {: #calculating-sovereign } `#calculating-a-parachain-sovereign-account-calculating-sovereign`
- Learn More {: #learn-more } `#learn-more-learn-more`

---

## XCM Execution Fees
https://docs.moonbeam.network/builders/interoperability/xcm/core-concepts/weights-fees.md

Learn about the XCM instructions involved in handling XCM execution fee payments and how to calculate fees on Polkadot, Kusama, and Moonbeam-based networks.

### Sections
- Introduction {: #introduction} `#introduction-introduction`
- Payment of Fees {: #payment-of-fees } `#payment-of-fees-payment-of-fees`
- XCM Instructions {: #xcm-instructions } `#xcm-instructions-xcm-instructions`
- Relay Chain XCM Fee Calculation  {: #rel-chain-xcm-fee-calc } `#relay-chain-xcm-fee-calculation-rel-chain-xcm-fee-calc`
- Polkadot {: #polkadot } `#polkadot-polkadot`
- Kusama {: #kusama } `#kusama-kusama`
- Moonbeam-based Networks XCM Fee Calculation  {: #moonbeam-xcm-fee-calc } `#moonbeam-based-networks-xcm-fee-calculation-moonbeam-xcm-fee-calc`
- Fee Calculation for Reserve Assets {: #moonbeam-reserve-assets } `#fee-calculation-for-reserve-assets-moonbeam-reserve-assets`
- Fee Calculation for External Assets {: #fee-calc-external-assets } `#fee-calculation-for-external-assets-fee-calc-external-assets`
- Weight to Asset Fee Conversion {: #weight-to-asset-fee-conversion} `#weight-to-asset-fee-conversion-weight-to-asset-fee-conversion`
- XCM Payment API Expanded Examples {: #xcm-payment-api-exanded-examples } `#xcm-payment-api-expanded-examples-xcm-payment-api-exanded-examples`
- Query Acceptable Fee Payment Assets {: #query-acceptable-fee-payment-assets } `#query-acceptable-fee-payment-assets-query-acceptable-fee-payment-assets`
- Weight to Asset Fee Conversion {: #weight-to-asset-fee-conversion } `#weight-to-asset-fee-conversion-weight-to-asset-fee-conversion-2`
- Query XCM Weight {: #query-xcm-weight} `#query-xcm-weight-query-xcm-weight`

---

## XCM Instructions
https://docs.moonbeam.network/builders/interoperability/xcm/core-concepts/instructions.md

When XCM instructions are combined, they form an XCM message that performs a cross-chain action. Take a look at some of the most common instructions.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Buy Execution {: #buy-execution } `#buy-execution-buy-execution`
- Clear Origin {: #clear-origin } `#clear-origin-clear-origin`
- Deposit Asset {: #deposit-asset } `#deposit-asset-deposit-asset`
- Descend Origin {: #descend-origin } `#descend-origin-descend-origin`
- Initiate Reserve Withdraw {: #initiate-reserve-withdraw } `#initiate-reserve-withdraw-initiate-reserve-withdraw`
- Refund Surplus {: #refund-surplus } `#refund-surplus-refund-surplus`
- Reserve Asset Deposited {: #reserve-asset-deposited } `#reserve-asset-deposited-reserve-asset-deposited`
- Set Appendix {: #set-appendix } `#set-appendix-set-appendix`
- Transfer Reserve Asset {: #transfer-reserve-asset } `#transfer-reserve-asset-transfer-reserve-asset`
- Transact {: #transact } `#transact-transact`
- Withdraw Asset {: #withdraw-asset } `#withdraw-asset-withdraw-asset`

---

## XCM Multilocations
https://docs.moonbeam.network/builders/interoperability/xcm/core-concepts/multilocations.md

Learn everything there is to know about multilocations, their role in XCM, and how to format a multilocation to target a specific point in the ecosystem.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Defining a Multilocation {: #defining-a-multilocation } `#defining-a-multilocation-defining-a-multilocation`
- Junctions {: #junctions } `#junctions-junctions`
- Example Multilocations {: #example-multilocations } `#example-multilocations-example-multilocations`
- Target Moonbeam from Another Parachain {: #target-moonbeam-from-parachain } `#target-moonbeam-from-another-parachain-target-moonbeam-from-parachain`
- Target an Account on Moonbeam from Another Parachain {: #target-account-moonbeam-from-parachain } `#target-an-account-on-moonbeam-from-another-parachain-target-account-moonbeam-from-parachain`
- Target Moonbeam's Native Asset from Another Parachain {: #target-moonbeam-native-asset-from-parachain } `#target-moonbeams-native-asset-from-another-parachain-target-moonbeam-native-asset-from-parachain`
- Target Moonbeam from the Relay Chain {: #target-moonbeam-from-relay } `#target-moonbeam-from-the-relay-chain-target-moonbeam-from-relay`
- Target the Relay Chain from Moonbeam {: #target-relay-from-moonbeam } `#target-the-relay-chain-from-moonbeam-target-relay-from-moonbeam`
- Target an Account on the Relay Chain from Moonbeam {: #target-account-relay-from-moonbeam } `#target-an-account-on-the-relay-chain-from-moonbeam-target-account-relay-from-moonbeam`
- Target Another Parachain from Moonbeam {: #target-parachain-from-moonbeam } `#target-another-parachain-from-moonbeam-target-parachain-from-moonbeam`
- Location to Account API {: #location-to-account-api } `#location-to-account-api-location-to-account-api`

---

## XCM Precompile
https://docs.moonbeam.network/builders/interoperability/xcm/xc20/send-xc20s/eth-api.md

Learn about the XCM Precompile and how to use it to transfer assets from Moonbeam networks to other parachains.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The XCM Solidity Interface {: #the-xcm-solidity-interface } `#the-xcm-solidity-interface-the-xcm-solidity-interface`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Contract {: #access-the-contract } `#access-the-contract-access-the-contract`
- Send Tokens Over to Another EVM-Compatible Appchain {: #transfer-to-evm-chains } `#send-tokens-over-to-another-evm-compatible-appchain-transfer-to-evm-chains`
- Send Tokens Over to a Substrate Appchain {: #transfer-to-substrate-chains } `#send-tokens-over-to-a-substrate-appchain-transfer-to-substrate-chains`
- Send Tokens Over to the Relay Chain {: #transfer-to-relay-chain } `#send-tokens-over-to-the-relay-chain-transfer-to-relay-chain`
- Send Tokens Over Specific Locations {: #transfer-locations } `#send-tokens-over-specific-locations-transfer-locations`

---

## XCM Utilities Precompile Contract
https://docs.moonbeam.network/builders/interoperability/xcm/xcm-utils.md

Learn the various XCM related utility functions available to smart contract developers with Moonbeam's precompiled XCM Utilities contract.

### Sections
- Introduction {: #xcmutils-precompile} `#introduction-xcmutils-precompile`
- The XCM Utilities Solidity Interface {: #xcmutils-solidity-interface } `#the-xcm-utilities-solidity-interface-xcmutils-solidity-interface`
- Using the XCM Utilities Precompile {: #using-the-xcmutils-precompile } `#using-the-xcm-utilities-precompile-using-the-xcmutils-precompile`
