---
title: How to Propose a Treasury Spend
description: Learn about the full life cycle of a Treasury proposal from the initial proposal on Moonbeam's Community Forum to Council approval of the on-chain spend.
categories:
- Governance
url: https://docs.moonbeam.network/tokens/governance/treasury-spend/
word_count: 588
token_estimate: 970
version_hash: sha256:817aa8c3037304aa86c68f4b84c64255006748b27dad01b4cf8b489b21e2402b
last_updated: '2026-05-21T21:21:53+00:00'
---

# How to Propose a Treasury Spend

## Introduction {: #introduction }

Treasury spending proposals enable community members to request funding for projects that benefit the Moonbeam network, such as infrastructure improvements, resources, events, and ecosystem tools. The Treasury Council reviews proposals and weighs community feedback received in the Moonbeam Forum. However, the ultimate Aye/Nay decision rests with the Council. For more information about the structure of the Treasury Council, see the [Treasury page](/moonbeam-mkdocs/learn/features/treasury/).

In this guide, you'll learn how to prepare and submit a Treasury spending proposal and understand the full lifecycle of a Treasury proposal. 

## Definitions {: #definitions }

Some of the key parameters for this guide are the following:

 - **Treasury address** — the address where Treasury funds accrue and are disbursed from
 - **Beneficiary** — the address, such as a [Moonbeam Safe multisig](/moonbeam-mkdocs/tokens/manage/multisig-safe/), that will receive the funds of the Treasury proposal if enacted
 - **Value** — the amount that is being asked for and will be allocated to the beneficiary address if the Treasury proposal is passed

## Treasury Addresses {: #treasury-addresses }

The Treasury address for each respective network can be found below:

=== "Moonbeam"

    [0x6d6f646C70792f74727372790000000000000000](https://moonbeam.subscan.io/account/0x6d6f646C70792f74727372790000000000000000)

=== "Moonriver"

    [0x6d6f646C70792f74727372790000000000000000](https://moonriver.subscan.io/account/0x6d6f646C70792f74727372790000000000000000)

=== "Moonbase Alpha"

    [0x6d6F646c70632f74727372790000000000000000](https://moonbase.subscan.io/account/0x6d6F646c70632f74727372790000000000000000)


## Roadmap of a Treasury Proposal {: #roadmap-of-a-treasury-proposal }

The happy path of a Treasury spend request is as follows:

1. **Proposal submission** - the user submits a proposal to the [Moonbeam Forum](https://forum.moonbeam.network/c/governance/treasury-proposals/8)

2. **Forum discussion** - the proposal is discussed by the community on the Forum. The ultimate Aye/Nay decision is determined by the Treasury council

3. **Treasury approval and action** - if the Treasury Council agrees, it authorizes the Treasury spending and moves the process forward
![Moonbeam Forum Home](/moonbeam-mkdocs/images/tokens/governance/treasury-proposals/treasury-proposal-1.webp)

## Submit Your Idea to the Forum {: #submitting-your-idea-to-the-forum }

As mentioned in the happy path above, the first step of a Treasury proposal is to submit the proposal to the [Moonbeam Forum](https://forum.moonbeam.network/c/governance/treasury-proposals/8). You'll need to have an account on the [Moonbeam Forum](https://forum.moonbeam.network/) and be logged in before submitting a Treasury spend proposal. To submit a Treasury spend proposal, follow these steps:

1. From the [**Governance** section](https://forum.moonbeam.network/c/governance/treasury-proposals/8), click **New Topic**. By starting the topic in the **Governance** section, the proposal will come pre-filled with a template to ensure you cover all the necessary points 
2. Provide a **title** for the proposal
3. Enter the contents of the proposal, covering: the **Title** and **Proposal Status**, a brief **Abstract**, the **Motivation**, a **Project Overview** and **Team Experience**, the **Rationale**, any **Key Terms**, the **Overall Cost**, the **Use of Treasury Funds**, the **Technical Specifications**, and the **Steps to Implement**
4. Choose either **Moonbeam** or **Moonriver** as a tag to indicate which network your Treasury proposal applies to
5. Press **Create Topic**

![Submit a Treasury spend proposal](/moonbeam-mkdocs/images/tokens/governance/treasury-proposals/treasury-proposal-2.webp)

## Next Steps {: #next-steps }

No further steps are required after proposing the spend. Members of the Treasury Council will complete all on-chain actions. If approved by the Treasury Council, the delivery of the Treasury payment to the designated beneficiary will happen automatically. For more information about the Treasury Council voting process, see the [Treasury page](/moonbeam-mkdocs/learn/features/treasury/#Treasury-council-voting-process).
