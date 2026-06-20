---
category: Node Operators and Collators
description: How to run a full node or a block-producing collator.
page_count: 13
token_estimate: 3644
updated: '2026-06-20T05:24:27.156643+00:00'
---

## Author Mapping Precompile
https://docs.moonbeam.network/node-operators/networks/collators/author-mapping.md

A guide for collators to learn how to use the Author Mapping Solidity interface to map session keys to a Moonbeam address where block rewards are paid out. 

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- The Author Mapping Solidity Interface {: #the-solidity-interface } `#the-author-mapping-solidity-interface-the-solidity-interface`
- Required Bonds {: #bonds } `#required-bonds-bonds`
- Interact with the Solidity Interface {: #interact-with-the-solidity-interface } `#interact-with-the-solidity-interface-interact-with-the-solidity-interface`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Generate Session Keys {: #generate-session-keys } `#generate-session-keys-generate-session-keys`
- Remix Set Up {: #remix-set-up } `#remix-set-up-remix-set-up`
- Compile the Contract {: #compile-the-contract } `#compile-the-contract-compile-the-contract`
- Access the Contract {: #access-the-contract } `#access-the-contract-access-the-contract`
- Map Session Keys {: #map-session-keys } `#map-session-keys-map-session-keys`

---

## Collator Account Management
https://docs.moonbeam.network/node-operators/networks/collators/account-management.md

Learn how to manage your collator account, including generating session keys, mapping Nimbus IDs, setting an identity, and creating proxy accounts.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Process to Add and Update Session Keys {: #process } `#process-to-add-and-update-session-keys-process`
- Generate Session Keys {: #session-keys } `#generate-session-keys-session-keys`
- Manage Session Keys {: #manage-session-keys } `#manage-session-keys-manage-session-keys`
- Author Mapping Pallet Interface {: #author-mapping-interface } `#author-mapping-pallet-interface-author-mapping-interface`
- Map Session Keys {: #mapping-extrinsic } `#map-session-keys-mapping-extrinsic`
- Check Mappings {: #checking-the-mappings } `#check-mappings-checking-the-mappings`
- Remove Session Keys {: #removing-session-keys } `#remove-session-keys-removing-session-keys`
- Setting an Identity {: #setting-an-identity } `#setting-an-identity-setting-an-identity`
- Proxy Accounts {: #proxy-accounts } `#proxy-accounts-proxy-accounts`

---

## Collators FAQ
https://docs.moonbeam.network/node-operators/networks/collators/faq.md

Some FAQs around becoming a collator, collator activities, and things to be aware of when running and operating a collator node on Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Q & A `#q-a`

---

## Compile the Binary to Run a Node
https://docs.moonbeam.network/node-operators/networks/run-a-node/compile-binary.md

Learn how to manually compile the binary to run a full Moonbeam node. Compiling the binary can take around 30 minutes and requires at least 32GB of memory.

### Sections
- Introduction `#introduction`
- Compile the Binary {: #compile-the-binary } `#compile-the-binary-compile-the-binary`

---

## Moonbeam Collator Activities
https://docs.moonbeam.network/node-operators/networks/collators/activities.md

Instructions on how to dive in and learn about the related activities for becoming and maintaining a collator node in the Moonbeam Network.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Collator Timings {: #collator-timings } `#collator-timings-collator-timings`
- Become a Candidate {: #become-a-candidate } `#become-a-candidate-become-a-candidate`
- Get the Size of the Candidate Pool {: #get-the-size-of-the-candidate-pool } `#get-the-size-of-the-candidate-pool-get-the-size-of-the-candidate-pool`
- Join the Candidate Pool {: #join-the-candidate-pool } `#join-the-candidate-pool-join-the-candidate-pool`
- Stop Collating {: #stop-collating } `#stop-collating-stop-collating`
- Schedule Request to Leave Candidates {: #schedule-request-to-leave-candidates } `#schedule-request-to-leave-candidates-schedule-request-to-leave-candidates`
- Execute Request to Leave Candidates {: #execute-request-to-leave-candidates } `#execute-request-to-leave-candidates-execute-request-to-leave-candidates`
- Cancel Request to Leave Candidates {: #cancel-request-to-leave-candidates } `#cancel-request-to-leave-candidates-cancel-request-to-leave-candidates`
- Temporarily Leave the Candidate Pool {: #temporarily-leave-the-candidate-pool } `#temporarily-leave-the-candidate-pool-temporarily-leave-the-candidate-pool`
- Change Self-Bond Amount {: #change-self-bond-amount } `#change-self-bond-amount-change-self-bond-amount`
- Bond More {: #bond-more } `#bond-more-bond-more`
- Bond Less {: #bond-less} `#bond-less-bond-less`
- Mark a Collator as Inactive {: #mark-collator-as-inactive } `#mark-a-collator-as-inactive-mark-collator-as-inactive`

---

## Moonbeam Collator Requirements
https://docs.moonbeam.network/node-operators/networks/collators/requirements.md

Learn about the requirements for becoming and maintaining a collator node on Moonbeam networks, including requirements for hardware, bonds, and more.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Community Guidelines {: #community-guidelines } `#community-guidelines-community-guidelines`
- Hardware Requirements {: #hardware-requirements } `#hardware-requirements-hardware-requirements`
- Account Requirements {: #account-requirements } `#account-requirements-account-requirements`
- Getting Started with Moonkey {: #getting-started-with-moonkey } `#getting-started-with-moonkey-getting-started-with-moonkey`
- Generating an Account with Moonkey {: #generating-an-account-with-moonkey } `#generating-an-account-with-moonkey-generating-an-account-with-moonkey`
- Other Moonkey Features {: #other-moonkey-features } `#other-moonkey-features-other-moonkey-features`
- Bonding Requirements {: #bonding-requirements } `#bonding-requirements-bonding-requirements`
- Minimum Collator Bond {: #minimum-collator-bond } `#minimum-collator-bond-minimum-collator-bond`
- Key Association Bond {: #key-association-bond } `#key-association-bond-key-association-bond`
- Collator Questionnaire {: #collator-questionnaire } `#collator-questionnaire-collator-questionnaire`

---

## Orbiter Program for Collators
https://docs.moonbeam.network/node-operators/networks/collators/orbiter.md

Learn about the Moonbeam Orbiter Program for collators, including the eligibility criteria, bond requirements, rewards, performance metrics, and more.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Duration {: #duration } `#duration-duration`
- Eligibility {: #eligibility } `#eligibility-eligibility`
- Communication {: #communication } `#communication-communication`
- Orbiters and Orbiter Pool Configurations {: #configuration } `#orbiters-and-orbiter-pool-configurations-configuration`
- Application and Onboarding Process {: #application-and-onboarding-process } `#application-and-onboarding-process-application-and-onboarding-process`
- Bonds {: #bond } `#bonds-bond`
- Mapping Bond {: #mapping-bond} `#mapping-bond-mapping-bond`
- Orbiter Bond {: #orbiter-bond } `#orbiter-bond-orbiter-bond`
- Rewards {: #rewards } `#rewards-rewards`
- Performance Metrics {: #performance-metrics } `#performance-metrics-performance-metrics`
- Leaving the Program {: #leaving-the-program } `#leaving-the-program-leaving-the-program`

---

## Run a Collator Node
https://docs.moonbeam.network/node-operators/networks/collators/overview.md

Instructions on how to dive in and become a collator in the Moonbeam Network once you are running a node.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Join the Discord {: #join-discord } `#join-the-discord-join-discord`

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

## Run a Node Flags & Options
https://docs.moonbeam.network/node-operators/networks/run-a-node/flags.md

A list of helpful flags for spinning up a full parachain node on Moonbeam. Also learn how to access all of the flags available for node operators.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Common Flags {: #common-flags } `#common-flags-common-flags`
- Execution Strategy Flags {: #execution-strategy } `#execution-strategy-flags-execution-strategy`
- Flags for Configuring a SQL Backend {: #flags-for-sql-backend } `#flags-for-configuring-a-sql-backend-flags-for-sql-backend`
- How to Access All of the Available Flags {: #how-to-access-all-of-the-available-flags } `#how-to-access-all-of-the-available-flags-how-to-access-all-of-the-available-flags`
- Docker {: #docker } `#docker-docker`
- Systemd {: #systemd } `#systemd-systemd`

---

## Run a Node on Moonbeam Using Systemd
https://docs.moonbeam.network/node-operators/networks/run-a-node/systemd.md

How to run a full parachain node so you can have your own RPC endpoint or produce blocks for the Moonbeam Network using Systemd.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Download the Latest Release Binary {: #the-release-binary } `#download-the-latest-release-binary-the-release-binary`
- Set Up the Service {: #set-up-the-service } `#set-up-the-service-set-up-the-service`
- Create the Configuration File {: #create-the-configuration-file } `#create-the-configuration-file-create-the-configuration-file`
- Full Node {: #full-node } `#full-node-full-node`
- Collator {: #collator } `#collator-collator`
- Run the Service {: #run-the-service } `#run-the-service-run-the-service`
- Maintain Your Node {: #maintain-your-node } `#maintain-your-node-maintain-your-node`
- Purge Your Node {: #purge-your-node } `#purge-your-node-purge-your-node`
- Purge Your Frontier Database {: #purge-frontier-database } `#purge-your-frontier-database-purge-frontier-database`

---

## Run a Tracing Node
https://docs.moonbeam.network/node-operators/networks/tracing-node.md

Learn how to leverage Geth's Debug and Txpool APIs, and OpenEthereum's Trace module to run a tracing node on Moonbeam.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Tracing Node Flags {: #tracing-node-flags } `#tracing-node-flags-tracing-node-flags`
- Run a Tracing Node with Docker {: #run-a-tracing-node-with-docker } `#run-a-tracing-node-with-docker-run-a-tracing-node-with-docker`
- Run a Tracing Node with Systemd {: #run-a-tracing-node-with-systemd } `#run-a-tracing-node-with-systemd-run-a-tracing-node-with-systemd`
- Setup the Wasm Overrides {: #setup-the-wasm-overrides } `#setup-the-wasm-overrides-setup-the-wasm-overrides`
- Create the Configuration File {: #create-the-configuration-file } `#create-the-configuration-file-create-the-configuration-file`
- Run the Service {: #run-the-service } `#run-the-service-run-the-service`
- Using a Tracing Node {: #using-a-tracing-node } `#using-a-tracing-node-using-a-tracing-node`

---

## Use Docker to Run a Node
https://docs.moonbeam.network/node-operators/networks/run-a-node/docker.md

How to run a full parachain node so you can have your own RPC endpoint or produce blocks for the Moonbeam Network using Docker.

### Sections
- Introduction {: #introduction } `#introduction-introduction`
- Checking Prerequisites {: #checking-prerequisites } `#checking-prerequisites-checking-prerequisites`
- Set up Storage for Chain Data {: #storage-chain-data } `#set-up-storage-for-chain-data-storage-chain-data`
- Start-up Commands {: #start-up-commands } `#start-up-commands-start-up-commands`
- Full Node {: #full-node } `#full-node-full-node`
- Collator Node `#collator-node`
- Syncing Your Node {: #syncing-your-node } `#syncing-your-node-syncing-your-node`
- Maintain Your Node {: #maintain-your-node } `#maintain-your-node-maintain-your-node`
- Purge Your Node {: #purge-your-node } `#purge-your-node-purge-your-node`
- Purge Your Frontier Database {: #purge-frontier-database } `#purge-your-frontier-database-purge-frontier-database`
