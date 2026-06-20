---
category: Precompiles
description: Guides to using Moonbeam's precompiles.
page_count: 19
token_estimate: 6393
updated: '2026-06-20T05:24:27.156643+00:00'
---

## Batch Precompile Contract
https://docs.moonbeam.network/builders/ethereum/precompiles/ux/batch.md

Learn how to transact multiple transfers and contract interactions at once via a Solidity interface with Moonbeam's Batch Precompile contract.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Batch Solidity Interface {: #the-batch-interface } `#the-batch-solidity-interface-the-batch-interface`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Example Contract {: #example-contract} `#example-contract-example-contract`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Precompile {: #access-the-precompile } `#access-the-precompile-access-the-precompile`
- Deploy Example Contract {: #deploy-example-contract } `#deploy-example-contract-deploy-example-contract`
- Send Native Currency via Precompile {: #send-native-currency-via-precompile } `#send-native-currency-via-precompile-send-native-currency-via-precompile`
- Find a Contract Interaction's Call Data {: #find-a-contract-interactions-call-data } `#find-a-contract-interactions-call-data-find-a-contract-interactions-call-data`
- Function Interaction via Precompile {: #function-interaction-via-precompile } `#function-interaction-via-precompile-function-interaction-via-precompile`
- Combining Subtransactions {: combining-subtransactions } `#combining-subtransactions-combining-subtransactions`
- Ethereum Development Libraries {: #ethereum-development-libraries } `#ethereum-development-libraries-ethereum-development-libraries`

---

## Call Permit Precompile Contract
https://docs.moonbeam.network/builders/ethereum/precompiles/ux/call-permit.md

Learn how to use the Call Permit Precompile contract on Moonbeam to sign a permit for any EVM call that can be dispatched by anyone or any smart contract.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Call Permit Solidity Interface {: #the-call-permit-interface } `#the-call-permit-solidity-interface-the-call-permit-interface`
- Setup the Contracts {: #setup-the-example-contract } `#setup-the-contracts-setup-the-example-contract`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Example Contract {: #example-contract } `#example-contract-example-contract`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile & Deploy the Example Contract {: #compile-deploy-example-contract } `#compile-deploy-the-example-contract-compile-deploy-example-contract`
- Compile & Access the Call Permit Precompile {: #compile-access-call-permit } `#compile-access-the-call-permit-precompile-compile-access-call-permit`
- Generate Call Permit Signature {: #generate-call-permit-signature} `#generate-call-permit-signature-generate-call-permit-signature`
- The Call Permit Arguments {: #call-permit-arguments } `#the-call-permit-arguments-call-permit-arguments`
- Use the Browser {: #use-the-browser } `#use-the-browser-use-the-browser`
- Use MetaMask's JS Signing Library {: #use-metamasks-signing-library } `#use-metamasks-js-signing-library-use-metamasks-signing-library`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Dispatch a Call {: #dispatch-a-call } `#dispatch-a-call-dispatch-a-call`

---

## Canonical Contract Addresses on Moonbeam
https://docs.moonbeam.network/builders/ethereum/canonical-contracts.md

Overview of the canonical contracts available on Moonbeam, Moonriver, & Moonbase Alpha, including common-good contracts and precompiles.

### Sections
- Common-good Contracts {: #common-goods-contracts } `#common-good-contracts-common-goods-contracts`
- Precompiled Contracts {: #precompiled-contracts } `#precompiled-contracts-precompiled-contracts`
- Ethereum MainNet Precompiles {: #ethereum-mainnet-precompiles } `#ethereum-mainnet-precompiles-ethereum-mainnet-precompiles`
- Non-Moonbeam Specific nor Ethereum Precompiles {: #non-moonbeam-specific-nor-ethereum-precompiles } `#non-moonbeam-specific-nor-ethereum-precompiles-non-moonbeam-specific-nor-ethereum-precompiles`
- Moonbeam-Specific Precompiles {: #moonbeam-specific-precompiles } `#moonbeam-specific-precompiles-moonbeam-specific-precompiles`

---

## Collective Precompile Contract
https://docs.moonbeam.network/builders/ethereum/precompiles/features/governance/collective.md

Learn how to use the Moonbeam Collective Precompile to perform democracy functions through any of the collectives on Moonbeam, such as the Treasury Council.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Collective Solidity Interface {: #the-call-permit-interface } `#the-collective-solidity-interface-the-call-permit-interface`
- Interacting with the Solidity Interface {: #interacting-with-the-solidity-interface } `#interacting-with-the-solidity-interface-interacting-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Contract {: #access-the-contract } `#access-the-contract-access-the-contract`
- Create a Proposal {: #create-a-proposal } `#create-a-proposal-create-a-proposal`
- Propose the Proposal {: #propose-the-proposal } `#propose-the-proposal-propose-the-proposal`
- Vote on a Proposal {: #vote-on-a-proposal } `#vote-on-a-proposal-vote-on-a-proposal`
- Close a Proposal {: #close-a-proposal } `#close-a-proposal-close-a-proposal`

---

## Conviction Voting Precompile Contract
https://docs.moonbeam.network/builders/ethereum/precompiles/features/governance/conviction-voting.md

Learn how to vote on referenda, set up voting delegations, and more, directly through a Solidity interface with the Conviction Voting Precompile on Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Conviction Voting Solidity Interface {: #the-conviction-voting-solidity-interface } `#the-conviction-voting-solidity-interface-the-conviction-voting-solidity-interface`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Contract {: #access-the-contract } `#access-the-contract-access-the-contract`
- Vote on a Referendum {: #vote-on-a-referendum } `#vote-on-a-referendum-vote-on-a-referendum`
- Delegate a Vote {: #delegate-a-vote } `#delegate-a-vote-delegate-a-vote`

---

## Ethereum MainNet Precompiles
https://docs.moonbeam.network/builders/ethereum/precompiles/utility/eth-mainnet.md

Learn how to use the standard precompiled contracts available on Ethereum such as ECRECOVER, SHA256, and more on Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Verify Signatures with ECRECOVER {: #verify-signatures-with-ecrecover } `#verify-signatures-with-ecrecover-verify-signatures-with-ecrecover`
- Hashing with SHA256 {: #hashing-with-sha256 } `#hashing-with-sha256-hashing-with-sha256`
- Hashing with RIPEMD160 {: #hashing-with-ripemd-160 } `#hashing-with-ripemd160-hashing-with-ripemd-160`
- BN128Add {: #bn128add } `#bn128add-bn128add`
- BN128Mul {: #bn128mul } `#bn128mul-bn128mul`
- BN128Pairing {: #bn128pairing } `#bn128pairing-bn128pairing`
- The Identity Function {: #the-identity-function } `#the-identity-function-the-identity-function`
- Modular Exponentiation {: #modular-exponentiation } `#modular-exponentiation-modular-exponentiation`
- P256 Verify {: #p256-verify } `#p256-verify-p256-verify`

---

## GMP Precompile
https://docs.moonbeam.network/builders/ethereum/precompiles/interoperability/gmp.md

Learn about the GMP precompile on Moonbeam and how to use it with the Moonbeam Routed Liquidity program provided by bridges like Wormhole.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The GMP Solidity Interface {: #the-gmp-solidity-interface } `#the-gmp-solidity-interface-the-gmp-solidity-interface`
- Building the Payload for Wormhole {: #building-the-payload-for-wormhole } `#building-the-payload-for-wormhole-building-the-payload-for-wormhole`
- Restrictions {: #restrictions } `#restrictions-restrictions`

---

## Identity Precompile
https://docs.moonbeam.network/builders/ethereum/precompiles/account/identity.md

Learn all you need to know about the Identity Precompile, such as its address, Solidity interface, and how to interact with it using popular Ethereum libraries.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Identity Precompile Solidity Interface {: #the-solidity-interface } `#the-identity-precompile-solidity-interface-the-solidity-interface`
- Interact with the Solidity Interface {: #interact-with-interface } `#interact-with-the-solidity-interface-interact-with-interface`
- Using Ethereum Libraries {: #use-ethereum-libraries } `#using-ethereum-libraries-use-ethereum-libraries`

---

## Interacting with the Proxy Precompile
https://docs.moonbeam.network/builders/ethereum/precompiles/account/proxy.md

How to use the Moonbeam proxy Solidity precompile interface to add and remove proxy accounts from Substrate's Proxy Pallet.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Proxy Solidity Interface {: #the-proxy-solidity-interface } `#the-proxy-solidity-interface-the-proxy-solidity-interface`
- Proxy Types {: #proxy-types } `#proxy-types-proxy-types`
- Proxy Dispatch Limitations {: #proxy-dispatch-limitations } `#proxy-dispatch-limitations-proxy-dispatch-limitations`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Contract {: #access-the-contract } `#access-the-contract-access-the-contract`
- Add a Proxy {: #add-proxy } `#add-a-proxy-add-proxy`
- Check a Proxy's Existence {: #check-proxy } `#check-a-proxys-existence-check-proxy`
- Dispatch a Proxy Call {: #dispatch-proxy-call } `#dispatch-a-proxy-call-dispatch-proxy-call`
- Remove a Proxy {: #remove-proxy } `#remove-a-proxy-remove-proxy`

---

## Native Token ERC-20 Precompile
https://docs.moonbeam.network/builders/ethereum/precompiles/ux/erc20.md

Learn how to access and interact with an ERC-20 representation of the native token on Moonbeam through the precompiled ERC-20 Interface.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The ERC-20 Solidity Interface {: #the-erc20-interface } `#the-erc-20-solidity-interface-the-erc20-interface`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Add Token to MetaMask {: #add-token-to-metamask } `#add-token-to-metamask-add-token-to-metamask`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Contract {: #access-the-contract } `#access-the-contract-access-the-contract`
- Get Basic Token Information {: #get-basic-token-information } `#get-basic-token-information-get-basic-token-information`
- Get Account Balance {: #get-account-balance } `#get-account-balance-get-account-balance`
- Approve a Spend {: #approve-a-spend } `#approve-a-spend-approve-a-spend`
- Get Allowance of Spender {: #get-allowance-of-spender } `#get-allowance-of-spender-get-allowance-of-spender`
- Send Transfer {: #send-transfer } `#send-transfer-send-transfer`
- Send Transfer From Specific Account {: #send-transferfrom } `#send-transfer-from-specific-account-send-transferfrom`

---

## Non-Network Specific Precompiles
https://docs.moonbeam.network/builders/ethereum/precompiles/utility/non-specific.md

Learn how to use precompiled contracts, which are not specific to Ethereum or Moonbeam, yet are supported for use in your application.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Retrieve a Public Key with ECRecoverPublicKey {: verifying-signatures-ecrecoverpublickey } `#retrieve-a-public-key-with-ecrecoverpublickey-verifying-signatures-ecrecoverpublickey`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Retrieve Transaction Signature Values `#retrieve-transaction-signature-values`
- Test ECRecoverPublicKey Contract `#test-ecrecoverpublickey-contract`
- Create a Hash with SHA3FIPS256 {: #create-a-hash-with-sha3fips256 } `#create-a-hash-with-sha3fips256-create-a-hash-with-sha3fips256`

---

## Precompile Registry
https://docs.moonbeam.network/builders/ethereum/precompiles/utility/registry.md

Learn how to access and interact with the Precompile Registry on Moonbeam, which can be used to check if a given address is a precompile and if it is supported.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Precompile Registry Solidity Interface {: #the-solidity-interface } `#the-precompile-registry-solidity-interface-the-solidity-interface`
- Interact with the Precompile Registry Solidity Interface {: #interact-with-precompile-registry-interface } `#interact-with-the-precompile-registry-solidity-interface-interact-with-precompile-registry-interface`
- Use Remix to Interact with the Precompile Registry {: #use-remix } `#use-remix-to-interact-with-the-precompile-registry-use-remix`
- Use Ethereum Libraries to Interact with the Precompile Registry {: #use-ethereum-libraries } `#use-ethereum-libraries-to-interact-with-the-precompile-registry-use-ethereum-libraries`

---

## Preimage Precompile Contract
https://docs.moonbeam.network/builders/ethereum/precompiles/features/governance/preimage.md

Learn how to take the first necessary step to submit a proposal on-chain by submitting a preimage that contains the action to be carried out in the proposal.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Preimage Solidity Interface {: #the-preimage-solidity-interface } `#the-preimage-solidity-interface-the-preimage-solidity-interface`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Contract {: #access-the-contract } `#access-the-contract-access-the-contract`
- Submit a Preimage of a Proposal {: #submit-a-preimage } `#submit-a-preimage-of-a-proposal-submit-a-preimage`

---

## Randomness Precompile
https://docs.moonbeam.network/builders/ethereum/precompiles/features/randomness.md

Learn about the sources of VRF randomness on Moonbeam and how to use the randomness precompile and consumer interface to generate on-chain randomness.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Randomness Solidity Interface {: #the-randomness-interface } `#the-randomness-solidity-interface-the-randomness-interface`
- Functions {: #functions } `#functions-functions`
- Constants {: #constants } `#constants-constants`
- Events {: #events } `#events-events`
- Enums {: #enums } `#enums-enums`
- The Randomness Consumer Solidity Interface {: #randomness-consumer-solidity-interface } `#the-randomness-consumer-solidity-interface-randomness-consumer-solidity-interface`
- Request & Fulfill Process {: #request-and-fulfill-process } `#request-fulfill-process-request-and-fulfill-process`
- Generate a Random Number using the Randomness Precompile {: #interact-with-the-solidity-interfaces } `#generate-a-random-number-using-the-randomness-precompile-interact-with-the-solidity-interfaces`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Create a Random Number Generator Contract {: #create-random-generator-contract } `#create-a-random-number-generator-contract-create-random-generator-contract`
- Remix Set Up {: #remix-set-up} `#remix-set-up-remix-set-up`
- Compile & Deploy the Random Number Generator Contract {: #compile-deploy-random-number } `#compile-deploy-the-random-number-generator-contract-compile-deploy-random-number`
- Submit a Request to Generate a Random Number {: #request-randomness } `#submit-a-request-to-generate-a-random-number-request-randomness`
- Fulfill the Request and Save the Random Number {: #fulfill-request-save-number } `#fulfill-the-request-and-save-the-random-number-fulfill-request-save-number`
- Use Remix to Interact Directly with the Randomness Precompile {: #interact-directly } `#use-remix-to-interact-directly-with-the-randomness-precompile-interact-directly`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up-2`
- Compile & Access the Randomness Precompile {: #compile-randomness } `#compile-access-the-randomness-precompile-compile-randomness`
- Get Request Status & Purge Expired Request {: #get-request-status-and-purge } `#get-request-status-purge-expired-request-get-request-status-and-purge`

---

## Referenda Precompile Contract
https://docs.moonbeam.network/builders/ethereum/precompiles/features/governance/referenda.md

Learn how to view and submit proposals on-chain to be put forth for referenda, directly through a Solidity interface with the Referenda Precompile on Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Referenda Solidity Interface {: #the-referenda-solidity-interface } `#the-referenda-solidity-interface-the-referenda-solidity-interface`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Contract {: #access-the-contract } `#access-the-contract-access-the-contract`
- Submit a Proposal {: #submit-a-proposal } `#submit-a-proposal-submit-a-proposal`
- Submit Decision Deposit {: #submit-decision-deposit } `#submit-decision-deposit-submit-decision-deposit`
- Refund Decision Deposit {: #refund-decision-deposit } `#refund-decision-deposit-refund-decision-deposit`

---

## Relay Data Verifier Precompile Contract
https://docs.moonbeam.network/builders/ethereum/precompiles/utility/relay-data-verifier.md

Learn how to verify data availability and authenticity on the relay chain via a Solidity interface with Moonbeam's Relay Data Verifier Precompile contract.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Relay Data Verifier Solidity Interface {: #the-relay-data-verifier-solidity-interface } `#the-relay-data-verifier-solidity-interface-the-relay-data-verifier-solidity-interface`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Using Ethereum Libraries {: #using-ethereum-libraries } `#using-ethereum-libraries-using-ethereum-libraries`

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

## Staking Precompile Contract
https://docs.moonbeam.network/builders/ethereum/precompiles/features/staking.md

Unlock the potential of staking with a specialized precompiled contract designed to streamline and optimize participation in Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Exit Delays {: #exit-delays } `#exit-delays-exit-delays`
- Parachain Staking Solidity Interface {: #the-parachain-staking-solidity-interface } `#parachain-staking-solidity-interface-the-parachain-staking-solidity-interface`
- Interact with the Solidity Interface {: #interact-with-solidity-interface } `#interact-with-the-solidity-interface-interact-with-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Contract {: #access-the-contract } `#access-the-contract-access-the-contract`
- Delegate a Collator with Auto-Compounding {: #delegate-a-collator } `#delegate-a-collator-with-auto-compounding-delegate-a-collator`
- Verify Delegation {: #verify-delegation } `#verify-delegation-verify-delegation`
- Confirm Auto-Compounding Percentage {: #confirm-auto-compounding } `#confirm-auto-compounding-percentage-confirm-auto-compounding`
- Set or Change the Auto-Compounding Percentage {: #set-or-change-auto-compounding } `#set-or-change-the-auto-compounding-percentage-set-or-change-auto-compounding`
- Revoke a Delegation {: #revoke-a-delegation } `#revoke-a-delegation-revoke-a-delegation`

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
