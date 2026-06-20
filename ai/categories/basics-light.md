---
category: Basics
description: Moonbeam's framework, architecture, and core components.
page_count: 25
token_estimate: 6449
updated: '2026-06-20T05:24:27.156643+00:00'
---

## Account Balances
https://docs.moonbeam.network/learn/core-concepts/balances.md

A description of the main differences that Ethereum developers need to understand in terms of account balances on Moonbeam and how they differ from Ethereum.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Ethereum Account Balances {: #ethereum-account-balances } `#ethereum-account-balances-ethereum-account-balances`
- Moonbeam Account Balances {: #moonbeam-account-balances } `#moonbeam-account-balances-moonbeam-account-balances`
- Calculating Your Transferable Balance {: #calculating-your-transferable-balance } `#calculating-your-transferable-balance-calculating-your-transferable-balance`
- Retrieve Your Balance {: #retrieve-your-balance } `#retrieve-your-balance-retrieve-your-balance`
- Main Differences {: #main-differences } `#main-differences-main-differences`

---

## Block Explorers
https://docs.moonbeam.network/builders/get-started/explorers.md

An overview of the currently available block explorers that may be used to navigate the Substrate and Ethereum layers of Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Quick Links {: #quick-links } `#quick-links-quick-links`
- Ethereum API {: #ethereum-api } `#ethereum-api-ethereum-api`
- Moonscan {: #Moonscan } `#moonscan-moonscan`
- Expedition {: #expedition } `#expedition-expedition`
- Substrate API {: #substrate-api } `#substrate-api-substrate-api`
- Subscan {: #subscan } `#subscan-subscan`
- Polkadot.js {: #polkadotjs } `#polkadotjs-polkadotjs`

---

## Calculating Transaction Fees
https://docs.moonbeam.network/learn/core-concepts/tx-fees.md

Learn about the transaction fee model used in Moonbeam and the differences compared to Ethereum that developers should be aware of.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Key Differences with Ethereum {: #key-differences-with-ethereum} `#key-differences-with-ethereum-key-differences-with-ethereum`
- Overview of MBIP-5 {: #overview-of-mbip-5 } `#overview-of-mbip-5-overview-of-mbip-5`
- Ethereum API Transaction Fees {: #ethereum-api-transaction-fees } `#ethereum-api-transaction-fees-ethereum-api-transaction-fees`
- Base Fee {: #base-fee} `#base-fee-base-fee`
- GasPrice, MaxFeePerGas, and MaxPriorityFeePerGas {: #gasprice-maxfeepergas-maxpriorityfeepergas } `#gasprice-maxfeepergas-and-maxpriorityfeepergas-gasprice-maxfeepergas-maxpriorityfeepergas`
- Transaction Weight {: #transaction-weight} `#transaction-weight-transaction-weight`
- Fee History Endpoint {: #eth-feehistory-endpoint } `#fee-history-endpoint-eth-feehistory-endpoint`
- Sample Code for Calculating Transaction Fees {: #sample-code } `#sample-code-for-calculating-transaction-fees-sample-code`
- Substrate API Transaction Fees {: #substrate-api-transaction-fees } `#substrate-api-transaction-fees-substrate-api-transaction-fees`

---

## Consensus & Finality
https://docs.moonbeam.network/learn/core-concepts/consensus-finality.md

The main differences that Ethereum developers should understand in terms of consensus and finality on Moonbeam and how it differs from Ethereum.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Ethereum Consensus and Finality {: #ethereum-consensus-and-finality } `#ethereum-consensus-and-finality-ethereum-consensus-and-finality`
- Moonbeam Consensus and Finality {: #moonbeam-consensus-and-finality } `#moonbeam-consensus-and-finality-moonbeam-consensus-and-finality`
- Main Differences Between PoS and DPoS {: #main-differences } `#main-differences-between-pos-and-dpos-main-differences`
- Check Transaction Finality with Ethereum RPC Endpoints {: #check-tx-finality-with-ethereum-rpc-endpoints } `#check-transaction-finality-with-ethereum-rpc-endpoints-check-tx-finality-with-ethereum-rpc-endpoints`
- Check Transaction Finality with Moonbeam RPC Endpoints {: #check-tx-finality-with-moonbeam-rpc-endpoints } `#check-transaction-finality-with-moonbeam-rpc-endpoints-check-tx-finality-with-moonbeam-rpc-endpoints`
- Check Transaction Finality with Substrate RPC Endpoints {: #check-tx-finality-with-substrate-rpc-endpoints } `#check-transaction-finality-with-substrate-rpc-endpoints-check-tx-finality-with-substrate-rpc-endpoints`

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

## Ethereum Compatibility
https://docs.moonbeam.network/learn/features/eth-compatibility.md

Transitioning from Ethereum to Moonbeam? Here's a brief overview of the key components and key differences of Moonbeam's Ethereum compatibility.

### Sections
- Key Components {: #key-components } `#key-components-key-components`
- EVM Compatibility {: #evm } `#evm-compatibility-evm`
- Ethereum-style Accounts {: #ethereum-style-accounts } `#ethereum-style-accounts-ethereum-style-accounts`
- JSON-RPC Support {: #json-rpc-support } `#json-rpc-support-json-rpc-support`
- Ethereum Developer Tools and Libraries {: #ethereum-dev-tools } `#ethereum-developer-tools-and-libraries-ethereum-dev-tools`
- Precompiled Contracts {: #precompiled-contracts } `#precompiled-contracts-precompiled-contracts`
- Ethereum Token Standards {: #ethereum-token-standards } `#ethereum-token-standards-ethereum-token-standards`
- Key Differences {: #key-differences } `#key-differences-key-differences`
- Consensus Mechanisms {: #consensus-mechanisms } `#consensus-mechanisms-consensus-mechanisms`
- Finality {: #finality } `#finality-finality`
- Proxy Accounts {: #proxy-accounts } `#proxy-accounts-proxy-accounts`
- Account Balances {: #account-balances } `#account-balances-account-balances`
- Balance Transfers {: #balance-transfers } `#balance-transfers-balance-transfers`
- Transaction Fees {: #transaction-fees } `#transaction-fees-transaction-fees`

---

## Get Started with Moonbeam
https://docs.moonbeam.network/builders/get-started/networks/moonbeam.md

Learn how to connect to Moonbeam via RPC and WSS endpoints, how to connect MetaMask to Moonbeam, and about the available Moonbeam block explorers.

### Sections
- Network Endpoints {: #network-endpoints } `#network-endpoints-network-endpoints`
- Quick Start {: #quick-start } `#quick-start-quick-start`
- Chain ID {: #chain-id } `#chain-id-chain-id`
- Block Explorers {: #block-explorers } `#block-explorers-block-explorers`
- Connect MetaMask {: #connect-metamask } `#connect-metamask-connect-metamask`
- Configuration {: #configuration } `#configuration-configuration`

---

## Governance
https://docs.moonbeam.network/learn/features/governance.md

As a Polkadot parachain, Moonbeam uses an on-chain governance system, allowing for a stake-weighted vote on public referenda.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Principles {: #principles } `#principles-principles`
- On-Chain Governance Mechanics {: #on-chain-governance-mechanics } `#on-chain-governance-mechanics-on-chain-governance-mechanics`
- Governance v2: OpenGov {: #opengov } `#governance-v2-opengov-opengov`
- General Definitions {: #general-definitions-gov2 } `#general-definitions-general-definitions-gov2`
- Governance Parameters {: #governance-parameters-v2 } `#governance-parameters-governance-parameters-v2`
- Roadmap of a Proposal {: #roadmap-of-a-proposal-v2 } `#roadmap-of-a-proposal-roadmap-of-a-proposal-v2`
- Proposal Example Walkthrough `#proposal-example-walkthrough`
- Proposal Cancellations {: #proposal-cancellations } `#proposal-cancellations-proposal-cancellations`
- Rights of the OpenGov Technical Committee {: #rights-of-the-opengov-technical-committee } `#rights-of-the-opengov-technical-committee-rights-of-the-opengov-technical-committee`
- Related Guides on OpenGov {: #try-it-out } `#related-guides-on-opengov-try-it-out`

---

## Moonbase Alpha Get Started Guide
https://docs.moonbeam.network/builders/get-started/networks/moonbase.md

The Moonbeam TestNet, named Moonbase Alpha, is the easiest way to get started with a Polkadot environment. Follow this tutorial to connect to the TestNet.

### Sections
- Network Endpoints {: #network-endpoints } `#network-endpoints-network-endpoints`
- Quick Start {: #quick-start } `#quick-start-quick-start`
- Chain ID {: #chain-id } `#chain-id-chain-id`
- Block Explorers `#block-explorers`
- Connect MetaMask `#connect-metamask`
- Configuration {: #configuration } `#configuration-configuration`
- Get Tokens {: #get-tokens } `#get-tokens-get-tokens`
- Demo DApps {: #Demo-DApps } `#demo-dapps-demo-dapps`
- Quick Links {: #quick-links } `#quick-links-quick-links`
- Moonbase ERC20 Minter {: #moonbase-erc20-minter } `#moonbase-erc20-minter-moonbase-erc20-minter`
- Moonbeam WalletConnect {: #moonbeam-walletconnect } `#moonbeam-walletconnect-moonbeam-walletconnect`
- MoonGas {: #moongas } `#moongas-moongas`

---

## Moonriver Get Started Guide
https://docs.moonbeam.network/builders/get-started/networks/moonriver.md

Learn how to connect to Moonriver via RPC and WSS endpoints, how to connect MetaMask to Moonriver, and about the available Moonriver block explorers.

### Sections
- Network Endpoints {: #network-endpoints } `#network-endpoints-network-endpoints`
- Quick Start {: #quick-start } `#quick-start-quick-start`
- Chain ID {: #chain-id } `#chain-id-chain-id`
- Block Explorers {: #block-explorers } `#block-explorers-block-explorers`
- Connect MetaMask {: #connect-metamask } `#connect-metamask-connect-metamask`
- Configuration {: #configuration } `#configuration-configuration`

---

## Quickly Get Started
https://docs.moonbeam.network/builders/get-started/quick-start.md

Everything you need to know to get started developing, deploying, and interacting with smart contracts on Moonbeam.

### Sections
- Quick Overview {: #overview } `#quick-overview-overview`
- Moonbeam Networks {: #moonbeam-networks } `#moonbeam-networks-moonbeam-networks`
- Network Configurations {: #network-configurations } `#network-configurations-network-configurations`
- Block Explorers {: #explorers } `#block-explorers-explorers`
- Funding TestNet Accounts {: #testnet-tokens } `#funding-testnet-accounts-testnet-tokens`
- Development Tools {: #development-tools } `#development-tools-development-tools`
- JavaScript Tools {: #javascript } `#javascript-tools-javascript`
- Python Tools {: #python } `#python-tools-python`

---

## Randomness
https://docs.moonbeam.network/learn/features/randomness.md

Learn about the sources of VRF randomness on Moonbeam, the request and fulfillment process, and some security considerations when using on-chain randomness.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- General Definitions {: #general-definitions } `#general-definitions-general-definitions`
- Quick Reference {: #quick-reference } `#quick-reference-quick-reference`
- Local VRF {: #local-vrf } `#local-vrf-local-vrf`
- BABE Epoch Randomness {: #babe-epoch-randomness } `#babe-epoch-randomness-babe-epoch-randomness`
- Request & Fulfill Process {: #request-and-fulfill-process } `#request-fulfill-process-request-and-fulfill-process`
- Security Considerations {: #security-considerations } `#security-considerations-security-considerations`

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

## Run a Collator Node
https://docs.moonbeam.network/node-operators/networks/collators/overview.md

Instructions on how to dive in and become a collator in the Moonbeam Network once you are running a node.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Join the Discord {: #join-discord } `#join-the-discord-join-discord`

---

## Run a Moonbeam Development Node
https://docs.moonbeam.network/builders/get-started/networks/moonbeam-dev.md

Follow this tutorial to learn how to spin up your first Moonbeam development node, how to configure it for development purposes, and connect to it.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Spin Up a Moonbeam Development Node {: #spin-up-a-node } `#spin-up-a-moonbeam-development-node-spin-up-a-node`
- Spin Up a Node with Docker {: #getting-started-with-docker } `#spin-up-a-node-with-docker-getting-started-with-docker`
- Spin Up a Node with a Binary File {: #getting-started-with-the-binary-file } `#spin-up-a-node-with-a-binary-file-getting-started-with-the-binary-file`
- Configure Your Moonbeam Development Node {: #configure-moonbeam-dev-node } `#configure-your-moonbeam-development-node-configure-moonbeam-dev-node`
- Common Flags to Configure Your Node {: #node-flags } `#common-flags-to-configure-your-node-node-flags`
- Common Options to Configure Your Node {: #node-options } `#common-options-to-configure-your-node-node-options`
- Configure Block Production {: #configure-block-production } `#configure-block-production-configure-block-production`
- Prefunded Development Accounts {: #pre-funded-development-accounts } `#prefunded-development-accounts-pre-funded-development-accounts`
- Development Node Endpoints {: #access-your-development-node } `#development-node-endpoints-access-your-development-node`
- Block Explorers {: #block-explorers } `#block-explorers-block-explorers`
- Debug, Trace, and TxPool APIs {: #debug-trace-txpool-apis } `#debug-trace-and-txpool-apis-debug-trace-txpool-apis`
- Purge a Development Node {: #purging-your-node } `#purge-a-development-node-purging-your-node`
- Purge a Node Spun Up with Docker {: #purge-docker-node } `#purge-a-node-spun-up-with-docker-purge-docker-node`
- Purge a Node Spun up with a Binary File {: #purge-binary-node } `#purge-a-node-spun-up-with-a-binary-file-purge-binary-node`

---

## Run a Node
https://docs.moonbeam.network/node-operators/networks/run-a-node/overview.md

Learn about all of the necessary details to run a full parachain node for the Moonbeam Network to have your RPC endpoint or produce blocks.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Requirements {: #requirements } `#requirements-requirements`
- Running Ports {: #running-ports } `#running-ports-running-ports`
- Default Ports for a Parachain Full-Node {: #default-ports-for-a-parachain-full-node } `#default-ports-for-a-parachain-full-node-default-ports-for-a-parachain-full-node`
- Default Ports of Embedded Relay Chain {: #default-ports-of-embedded-relay-chain } `#default-ports-of-embedded-relay-chain-default-ports-of-embedded-relay-chain`
- Installation {: #installation } `#installation-installation`
- Debug, Trace and TxPool APIs {: #debug-trace-txpool-apis } `#debug-trace-and-txpool-apis-debug-trace-txpool-apis`
- Lazy Loading {: #lazy-loading } `#lazy-loading-lazy-loading`
- Logs and Troubleshooting {: #logs-and-troubleshooting } `#logs-and-troubleshooting-logs-and-troubleshooting`
- P2P Ports Not Open {: #p2p-ports-not-open } `#p2p-ports-not-open-p2p-ports-not-open`
- In Sync {: #in-sync } `#in-sync-in-sync`
- Genesis Mismatching {: #genesis-mismatching } `#genesis-mismatching-genesis-mismatching`

---

## Security Considerations
https://docs.moonbeam.network/learn/core-concepts/security.md

A description of the main differences that Ethereum developers need to understand in terms of security considerations when developing on Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Arbitrary Code Execution {: #arbitrary-code-execution } `#arbitrary-code-execution-arbitrary-code-execution`
- Precompiles Can Override a Set Value {: #setting-a-value } `#precompiles-can-override-a-set-value-setting-a-value`
- Whitelisting Safe Function Selectors {: #whitelisting-function-selectors } `#whitelisting-safe-function-selectors-whitelisting-function-selectors`
- Whitelisting Safe Contracts {: #whitelisting-safe-contracts} `#whitelisting-safe-contracts-whitelisting-safe-contracts`
- Precompiles Can Bypass Sender vs Origin Checks {: #bypass-sender-origin-checks } `#precompiles-can-bypass-sender-vs-origin-checks-bypass-sender-origin-checks`

---

## Solidity Precompiles
https://docs.moonbeam.network/builders/ethereum/precompiles/overview.md

An overview of the available Solidity precompiles on Moonbeam. Precompiles enable you to interact with Substrate features using the Ethereum API.

### Sections
- Overview {: #introduction } `#overview-introduction`
- Precompiled Contract Addresses {: #precompiled-contract-addresses } `#precompiled-contract-addresses-precompiled-contract-addresses`
- Ethereum MainNet Precompiles {: #ethereum-mainnet-precompiles } `#ethereum-mainnet-precompiles-ethereum-mainnet-precompiles`
- Non-Moonbeam Specific nor Ethereum Precompiles {: #non-moonbeam-specific-nor-ethereum-precompiles } `#non-moonbeam-specific-nor-ethereum-precompiles-non-moonbeam-specific-nor-ethereum-precompiles`
- Moonbeam Specific Precompiles {: #moonbeam-specific-precompiles } `#moonbeam-specific-precompiles-moonbeam-specific-precompiles`

---

## Staking
https://docs.moonbeam.network/learn/features/staking.md

Moonbeam provides staking features where token holders delegate collator candidates with their tokens and earn rewards.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- General Definitions {: #general-definitions } `#general-definitions-general-definitions`
- Quick Reference {: #quick-reference } `#quick-reference-quick-reference`
- Resources for Selecting a Collator {: #resources-for-selecting-a-collator} `#resources-for-selecting-a-collator-resources-for-selecting-a-collator`
- General Tips {: #general-tips } `#general-tips-general-tips`
- Reward Distribution {: #reward-distribution } `#reward-distribution-reward-distribution`
- Annual Inflation {: #annual-inflation} `#annual-inflation-annual-inflation`
- Calculating Rewards {: #calculating-rewards } `#calculating-rewards-calculating-rewards`
- Risks {: #risks } `#risks-risks`

---

## Transfer & Monitor Balances on Moonbeam
https://docs.moonbeam.network/learn/core-concepts/transfers-api.md

A description of the main differences that developers need to understand in terms of the different balance transfers available on Moonbeam compared to Ethereum.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Ethereum Transfers {: #ethereum-transfers } `#ethereum-transfers-ethereum-transfers`
- Moonbeam Transfers {: #moonbeam-transfers } `#moonbeam-transfers-moonbeam-transfers`
- Monitor Native Token Balance Transfers {: #monitor-transfers } `#monitor-native-token-balance-transfers-monitor-transfers`
- Using Polkadot.js API {: #using-polkadotjs-api } `#using-polkadotjs-api-using-polkadotjs-api`
- Using Substrate API Sidecar {: #using-substrate-api-sidecar } `#using-substrate-api-sidecar-using-substrate-api-sidecar`

---

## Treasury
https://docs.moonbeam.network/learn/features/treasury.md

Moonbeam has an on-chain Treasury controlled by Treasury Council members, enabling stakeholders to submit proposals to further the network.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- General Definitions {: #general-definitions } `#general-definitions-general-definitions`
- Treasury Addresses {: #treasury-addresses } `#treasury-addresses-treasury-addresses`
- Roadmap of a Treasury Proposal {: #roadmap-of-a-treasury-proposal } `#roadmap-of-a-treasury-proposal-roadmap-of-a-treasury-proposal`
- Treasury Council Voting Process {: #treasury-council-voting-process } `#treasury-council-voting-process-treasury-council-voting-process`

---

## Unified Accounts
https://docs.moonbeam.network/learn/core-concepts/unified-accounts.md

Moonbeam replaced the default Substrate account system with native support for the Ethereum-based H160 accounts and ECDSA keys. Find out more information!

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Substrate EVM Compatible Blockchain {: #substrate-evm-compatible-blockchain } `#substrate-evm-compatible-blockchain-substrate-evm-compatible-blockchain`
- Moonbeam Unified Accounts {: #moonbeam-unified-accounts } `#moonbeam-unified-accounts-moonbeam-unified-accounts`

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
