---
title: Collators FAQ
description: Some FAQs around becoming a collator, collator activities, and things to be aware of when running and operating a collator node on Moonbeam.
categories:
- Node Operators and Collators
url: https://docs.moonbeam.network/node-operators/networks/collators/faq/
word_count: 1520
token_estimate: 2557
version_hash: sha256:7c85a4fd270c77349d4600a12fdecfdff630dac658c82677cdd8e59f36189190
last_updated: '2026-05-21T21:21:53+00:00'
---

# Frequently Asked Questions

## Introduction {: #introduction }

Collators are an integral part of the parachains they take part in. They receive transactions and create state transition proofs for the relay chain validators.

Running a Moonbeam collator requires Linux systems administration skills, careful monitoring, and an attention to detail. Below are some tips and tricks that have been accumulated which should help you get up and running quickly.

## Q & A

**Q: Where can I get help?**

**A:** There is an active and friendly [Discord](https://discord.com/invite/PfpUATX) community for collators. Join the server and introduce yourself even before you need help. Send **gilmouta** or **artkaseman** a DM and let them know who you are, and they can reach out to you if they see any issues with your node.

***

**Q: How do I stay up to date?**

**A:** All upgrades and important technical information are announced on [Discord](https://discord.com/invite/PhfEbKYqak), in the **#tech-upgrades-announcements** channel. Join and follow this channel. You can set up integrations to Slack or Telegram if those are your preferred communication channels.

***

**Q: How do I register my node?**

**A:** There is a [questionnaire](https://docs.google.com/forms/d/e/1FAIpQLSfjmcXdiOXWtquYlBhdgXBunCKWHadaQCgPuBtzih1fd0W3aA/viewform), in which you will be able to provide your contact information as well as some basic hardware specs. You must be running a collator node on Moonbase Alpha to fill out the questionnaire.

***

**Q: What are the hardware requirements?**

**A:** Running a collator requires top of the line hardware to be able to process transactions and maximize your rewards. This is a very important factor in block production and rewards.

Run a systemd service on a top of the line bare-metal machine (i.e. run a physical server, not a cloud VM, or a docker container). You can run your own, or select a provider to manage the server for you.

Run only one service at a time per bare-metal machine. Do not run multiple instances.

***

**Q: What is the recommended hardware to run a collator?**

**A:**

Hardware recommendations:

- Top of the line CPU:
    - Ryzen 9 5950x or 5900x
    - Intel Xeon E-2386 or E-2388
- Primary and backup bare metal servers in different data centers and countries (Hetzner is OK for one of them)
- Dedicated server for Moonbeam that isn't shared with any other apps
- 1 TB NVMe SSD
- 32 GB RAM

***

**Q: What about backup nodes?**

**A:** Run two bare-metal machines of the same specifications, in different countries and service providers. If your primary fails you can quickly resume services on your backup and continue to produce blocks and earn rewards. Please refer to the Q&A on [failovers](#:~:text=What is the failover process if my Primary node is down) below.

***

**Q: What are the different networks?**

**A:** There are three networks, and each requires dedicated hardware. The Moonbase Alpha TestNet is free and should be used to familiarize yourself with the setup.

- **Moonbeam** - production network on Polkadot
- **Moonriver** - production network on Kusama
- **Moonbase Alpha TestNet** - development network

***

**Q: What ports do I allow on my firewall?**

**A:**

- Allow all incoming requests on TCP ports 30333 and 30334
- Allow requests from your management IPs on TCP port 22
- Drop all other ports

***

**Q: Is there a CPU optimized binary?**

**A:** On each [release page](https://github.com/moonbeam-foundation/moonbeam/releases) are CPU optimized binaries. Select the binary for your CPU architecture.

- **Moonbeam-znver3** - Ryzen 9
- **Moonbeam-skylake** - Intel
- **Moonbeam** - generic can be used for all others

***

**Q: What are the recommendations on monitoring my node?**

**A:** Monitoring is very important for the health of the network and to maximize your rewards. We recommend using [Grafana Labs](https://grafana.com). They have a free tier which should handle 6+ moonbeam servers.

***

**Q: What are the KPIs I should be monitoring?**

**A:** The main key performance indicator is blocks produced. The prometheus metric for this is called `substrate_proposer_block_constructed_count`.  

***

**Q: How should I setup alerting?**

**A:** Alerting is critical to keeping your moonbeam node producing blocks and earning rewards. We recommend [pagerduty.com](https://www.pagerduty.com), which is supported by [Grafana Labs](https://grafana.com). Use the [KPI query](#:~:text=substrate_proposer_block_constructed_count) above and set an alert when this drops below 1. The alert should page the person on-call 24/7.  

***

**Q: What are Nimbus keys?**

**A:** Nimbus keys are just like [session keys in Polkadot](https://wiki.polkadot.com/learn/learn-cryptography/#session-keys). You should have unique keys on your primary and backup servers. Save the key output somewhere safe where you can access it in the middle of the night if you receive an alert. To create your keys, please refer to the [Session Keys](/moonbeam-mkdocs/node-operators/networks/collators/account-management/#session-keys) section of the documentation.

***

**Q: What is the failover process if my primary node is down?**

**A:** When the primary server is down, the best way to perform a failover to the backup server is to perform a key association update. Each server should have a unique set of [keys](#:~:text=What are Nimbus keys) already. Run the `setKeys` author mapping extrinsic. You can follow the [Mapping Extrinsic](/moonbeam-mkdocs/node-operators/networks/collators/account-management/#mapping-extrinsic) instructions and modify the instructions to use the `setKeys` extrinsic.

***

**Q: Should I set up centralized logging?**

**A:** [Grafana Labs](https://grafana.com) can also be configured for centralized logging and is recommended. You can see all your nodes in one place. [Kibana](https://www.elastic.co/kibana) has a more robust centralized logging offering, but Grafana is simple and good enough to start.

***

**Q: What should I look for in the logs?**

**A:** Logs are very useful to determine if you are in sync and ready to join the collators pool. Look at the tail end of the logs to determine if: 

1. Your Relay chain is in sync
2. Your parachain is in sync

You should see **Idle** in your logs when your node is in sync.

![In sync Relay chain and parachain](/moonbeam-mkdocs/images/node-operators/networks/collators/account-management/account-1.webp)

A common issue is joining the pool before your node is in sync. You will be unable to produce any blocks or receive any rewards. Wait until you are in sync and idle before joining the candidate pool.

<div id="termynal" data-termynal>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ 10 Syncing 137.9 bps, target=#12325010 (8 peers), best: #21001 (0x25d9...57d8), finalized #20992 (0x1ebb..fd23), # 214.4kiB/s 11.7kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 🌗 ⚙️ * Syncing 182.7 bps, target=#5219905 (8 peers), best: #22472 (0x875f..aed7), finalized #9625 (0x601b...e64f), # 371.0kiB/s 113.3kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ I Syncing 186.6 bps, target=#12325011 (8 peers), best: #21935 (0x58f8...d312), finalized #21585 (0x1d73...13c8), #271.9kiB/s T1.3kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 🌗 ⚙️ @ Syncing 193.4 bps, target=#5219905 (8 peers), best: #23440 (0xdce6...8ea6), finalized #9922 (0x07c9...1fdf), # 383.3kiB/s 17.5kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ Ö Syncing 189.5 bps, target=#12325012 (8 peers), best: #22883 (0x6531.2281), finalized #22528 (0x0f21.0855), # 290.8kiB/s 10.6kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 🌗 ⚙️ @ Syncing 206.4 bps, target=#5219905 (8 peers), best: #24474 (0x09dd...6700), finalized #10393 (0x3efc...8a40), #428.7kiB/s 12.4kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ . Syncing 171.6 bps, target=#12325013 (8 peers), best: #23744 (0x4ced...cdae), finalized #23552 (0x1773..09d9), # 252.4kiB/s 10.6kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 🌗 ⚙️ Syncing 212.3 bps, target=#5219905 (8 peers), best: #25536 (0x7bc0...e9b7), finalized #10905 (0x5c70...3063), 1427.1kiB/s 11.4kiB/s</span>
</div>
The relay chain takes much longer to sync than the parachain. You will not see any finalized blocks until the relay chain has synced.

***

**Q: How much is the bond to become a collator?**

**A:** There are two bonds you need to be aware of. Make sure your node is configured and in sync before proceeding with these steps.

The first is the [bond to join the collators](/moonbeam-mkdocs/node-operators/networks/collators/activities/#become-a-candidate) pool:

- **Moonbeam** - minimum of 100000 GLMR
- **Moonriver** - minimum of 500 MOVR
- **Moonbase Alpha** - minimum of 500 DEV

The second is the [bond for key association](/moonbeam-mkdocs/node-operators/networks/collators/account-management/#mapping-bonds):

- **Moonbeam** - minimum of 10000 GLMR
- **Moonriver** - minimum of 100 MOVR
- **Moonbase Alpha** - minimum of 100 DEV

***

**Q: How do I set an identity on my collator account?**  

**A:** Setting an identity on chain will help to identify your node and attract delegations. You can set an identity by following the instructions on the [Managing an Identity](/moonbeam-mkdocs/tokens/manage/identity/) page of our documentation.
