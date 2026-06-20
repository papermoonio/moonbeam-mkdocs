---
title: Treasury
description: Moonbeam has an on-chain Treasury controlled by Treasury Council members, enabling stakeholders to submit proposals to further the network.
categories:
- Basics
url: https://docs.moonbeam.network/learn/features/treasury/
word_count: 623
token_estimate: 914
version_hash: sha256:5f6aca805ffdb79cc1897a0cd0588f083a8b5310de6741552e1246414a5c24d3
last_updated: '2026-05-21T21:21:53+00:00'
---

# Treasury on Moonbeam

## Introduction {: #introduction }

The Moonbeam Treasury is an on-chain collection of funds launched at the network's genesis. Initially pre-funded with 0.5% of the token supply, the Treasury continues to accumulate GLMR as 80% of the parachain bond reserve inflation goes to the Treasury. For more information about Moonbeam inflation figures, see [GLMR Tokenomics](https://moonbeam.foundation/glimmer-token-tokenomics/).

The Moonbeam Treasury funds initiatives that support and grow the network. Stakeholders can propose spending requests for Treasury Council review, focusing on efforts like integrations, collaborations, community events, and outreach. Treasury spend proposers must submit their proposals to the [Moonbeam Forum](https://forum.moonbeam.network/c/governance/treasury-proposals/8). For submission details, see [How to Propose a Treasury Spend](/moonbeam-mkdocs/tokens/governance/treasury-spend/).

The [Treasury Council](https://forum.moonbeam.network/g/TreasuryCouncil) oversees the spending of the Moonbeam Treasury and votes on funding proposals. It comprises two members from the Moonbeam Foundation and three external community members. The three external members are elected to terms of 6 months. The same Treasury Council oversees Treasury requests for both Moonbeam and Moonriver. The Council meets monthly to review proposals submitted on the [Moonbeam Forum](https://forum.moonbeam.network/c/governance/treasury-proposals/8). Once a proposal is agreed upon, the Council members must complete the on-chain approval process.

## General Definitions {: #general-definitions }

Some important terminology to understand regarding treasuries:

- **Treasury Council** — a group of Moonbeam Foundation representatives and external community members. The Council reviews funding proposals, ensures alignment with the community, and ultimately authorizes Treasury spending
- **Proposal** — a plan or suggestion submitted by stakeholders to further the network to be approved by the Treasury Council

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
## Treasury Council Voting Process {: #treasury-council-voting-process }

A member of the Treasury Council will submit a `treasury.spend` call. This call requires specifying the amount, the asset type, and the beneficiary account to receive the funds. The Treasury supports spending various token types beyond GLMR, including native USDT/USDC. Once this extrinsic is submitted, a new Treasury Council collective proposal will be created and made available for council members to vote on. Once approved through the Treasury Council's internal voting process, the funds will be released automatically to the beneficiary account through the `treasury.payout` extrinsic.
 
!!! note
    There is no on-chain action for the proposer or beneficiary of the Treasury spend request.
    All Treasury spend actions will be completed by members of the Treasury Council.

Note that this process has changed significantly from prior Treasury processes, where tokenholders could submit Treasury proposals with bonds attached. Now, no on-chain action is necessary to submit a Treasury proposal. Rather, all that is needed is to raise a Treasury Council request on the [Moonbeam Forum](https://forum.moonbeam.network/c/governance/treasury-proposals/8) and the Treasury Council will take care of the on-chain components. 

For more information, see [How to Propose a Treasury Spend](/moonbeam-mkdocs/tokens/governance/treasury-spend/#next-steps)
