---
title: How to Vote on a Proposal in OpenGov
description: Follow this guide to learn how to vote and lock your tokens to support or reject a proposal put forth for a referendum in Governance v2 (OpenGov) on Moonbeam.
categories:
- Governance
url: https://docs.moonbeam.network/tokens/governance/voting/
word_count: 3753
token_estimate: 5083
version_hash: sha256:67b0c66770b2db0edb09e4883edc553ee87f3aa82abea63c64867631bebe65cc
last_updated: '2026-05-21T21:21:53+00:00'
---

# How to Vote on a Proposal in Governance v2: OpenGov

## Introduction {: #introduction }

Referenda are simple, inclusive, and stake-based voting schemes. Each referendum has a proposal associated with it that suggests an action to take place. In OpenGov, each referendum will have a specified Origin class that the proposal will be executed with, and each Origin has its own Track that proposals will process through. Although referenda are completed by a common process, the requirements for approval are Track-specific.

Token holders can vote on referenda using their own tokens, including those that are locked in staking. The weight of a vote is defined by two factors: the number of tokens locked and the lock duration (called Conviction). This is to ensure that there is an economic buy-in to prevent vote-selling. Consequently, the longer you are willing to lock your tokens, the stronger your vote will be weighted. You also have the option of not locking tokens at all, but the vote weight is drastically reduced.

In Moonbeam, users are able to create and vote on proposals using their H160 address and private key, that is, their regular Ethereum account!

This guide will outline the process, with step-by-step instructions, of how to vote on referenda in Governance v2: OpenGov. This guide will show you how to vote on Moonbase Alpha, but it can be easily adapted for Moonbeam and Moonriver.

!!! note
    This page goes through the mechanics of how to vote at a more technical level. Token holders can leverage platforms such as [Polkassembly](https://moonbeam.network/news/participate-in-opengov-with-polkassembly-on-moonbeam) to vote using a more friendly user interface.

## Definitions {: #definitions }

Some of the key parameters for this guide are the following:

 - **Voting** — a mechanism for token holders to support (Aye), oppose (Nay), or remain neutral (Abstain) on a proposal. For Aye and Nay, the voting weight is determined by both the number of tokens locked and the lock duration (Conviction). Abstain votes do not receive additional weighting
    - **Conviction** — the time that token holders voluntarily lock their tokens when voting; the longer they are locked, the more weight their vote has
    - **Lock balance** — the number of tokens that a user commits to a vote (note, this is not the same as a user's total account balance)
    Moonbeam uses the concept of voluntary locking, which allows token holders to increase their voting power by locking tokens for a longer period of time. Specifying no Lock Period means a user's vote is valued at 10% of their lock balance. Specifying a greater Conviction increases voting power. For each increase in Conviction (vote multiplier), the Lock Periods double
 - **Maximum number of votes** — the maximum number of concurrent votes per account

    === "Moonbeam"

        ```text
        512 votes
        ```

    === "Moonriver"

        ```text
        512 votes
        ```

    === "Moonbase Alpha"

        ```text
        512 votes
        ```

 - **Approval** — minimum "Aye" votes as a percentage of overall Conviction-weighted votes needed for approval
 - **Support** — the minimum portion of Aye and Abstain votes (ignoring conviction) needed as a percentage of the total active supply for a proposal to pass. Nay votes do not count toward Support
 - **Lead-in Period** — the initial proposal voting and discussion period. At this stage, proposals are in an undecided state until they pass some criteria for the given Track. The criteria include:
    - **Prepare Period** — the minimum time the referendum needs to wait before it can progress to the next phase after submission
    - **Capacity** — limit for the number of referenda on a given Track that can be decided at once
    - **Decision Deposit** — the minimum deposit amount required for a referendum to progress to the decision phase after the end of the Lead-in Period. Since each Track has a defined Capacity, this deposit is larger than the submission deposit, and its goal is to mitigate spam 
    
 - **Decide Period** - token holders continue to vote on the referendum. If a referendum does not pass by the end of the period, it will be rejected, and the Decision Deposit will be refunded
 - **Confirm Period** - a period of time within the Decide Period where the referendum needs to have maintained enough Approval and Support to be approved and move to the Enactment Period
 - **Enactment Period** - a specified time, which is defined at the time the proposal was created, that meets at least the minimum amount of time that an approved referendum waits before it can be dispatched

 - **Vote Delegation** — a voter can give their voting power, including Conviction voting, to another token holder (delegate), who may be more knowledgeable and able to make specific decisions
 - **Multirole Delegation** — the ability to delegate voting power on a Track-by-Track basis, where a token holder can specify different delegates for each Track
For an overview of the Track-specific parameters such as the length of the Decide, Confirm, and Enactment Period, the Approval and Support requirements, and more, please refer to the [Governance Parameters for OpenGov (Governance v2) section of the governance overview page](/moonbeam-mkdocs/learn/features/governance/#governance-parameters-v2).

## Roadmap of a Proposal {: #roadmap-of-a-proposal }

This guide will cover how to vote on public referenda, as seen in the steps highlighted in the proposal roadmap diagram below. In addition to learning how to vote on referenda, you'll also learn how the proposal progresses through the Lead-in Period, the Decide and Confirm Period, and the Enactment Period.

You can find a full explanation of the [happy path for an OpenGov proposal on the Governance overview page](/moonbeam-mkdocs/learn/features/governance/#roadmap-of-a-proposal-v2).

![Proposal Roadmap](/moonbeam-mkdocs/images/tokens/governance/voting/proposal-roadmap.webp)

## Forum Discussion {: #forum-discussion}

A vote on a democracy referendum is a binary outcome. However, a token holder's opinion is often more nuanced than yes or no, which is why it's strongly recommended that you preface any proposal with a post on [Moonbeam's Community Forum](https://forum.moonbeam.network).

The forum serves the critical role of providing a platform for discussion and allowing proposers to receive feedback from the community prior to an on-chain action. Creating a post on the forum is quick and easy, as shown in the [Using the Moonbeam Community Forum](https://moonbeam.network/news/using-the-moonbeam-community-forum-to-submit-a-treasury-proposal) guide. There are categories corresponding to each type of proposal, including democracy, treasury, and grant proposals. While this step is optional, explaining the details of the proposal and following up with any questions raised may increase the chances of the initiative being accepted and subsequently passed by the community.

![Moonbeam's Community Forum home](/moonbeam-mkdocs/images/tokens/governance/voting/vote-1.webp)

## Voting on a Referendum {: #voting-on-a-referendum }

This section goes over the process of voting on a public referendum in OpenGov (Governance v2) on Moonbase Alpha. These steps can be adapted for Moonbeam and Moonriver. The guide assumes that there is one already taking place. If there is an open referendum that you want to vote on, you can adapt these instructions to learn how to vote on it.

To vote on a proposal on the network, you need to use the Polkadot.js Apps interface. To do so, you need to import an Ethereum-style account first (H160 address), which you can do by following the [Creating or Importing an H160 Account](/moonbeam-mkdocs/tokens/connect/polkadotjs/#creating-or-importing-an-h160-account) guide. For this example, three accounts were imported and named with super original names: Alice, Bob, and Charlie.

![Accounts in Polkadot.js](/moonbeam-mkdocs/images/tokens/governance/proposals/proposals-3.webp)

To get started, you'll need to navigate to [Moonbase Alpha's Polkadot.js Apps interface](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network). Everything related to governance lives under the **Governance** tab. To view all of the referenda, you can choose **Referenda** from the **Governance** dropdown. On the **Referenda** page, you'll see a list of referenda organized by Track. To view the details of a specific referendum, you can click on the arrow next to the description. The number next to the action and description is called the referendum index.

### How to Support a Proposal by Contributing to the Decision Deposit {: #submit-decision-deposit }

In order for a referendum to move out of the Lead-in Period into the Decide Period, the Decision Deposit must be submitted. This deposit can be submitted by the author of the proposal or any other token holder. The deposit varies depending on the Track of the proposal.

For example, a referendum that is in the General Admin Track has a Decision Deposit of 500 on Moonbase Alpha.

From the [list of referenda on Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#/referenda), you may notice that some proposals are in the **Preparing** state. If a referendum requires the Decision Deposit to be submitted, you'll see a **Decision deposit** button. To submit the deposit, you can go ahead and click on this button.

![To start to submit a Decision Deposit for a referendum, click on the "Decision deposit" button on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-2.webp)

Then take the following steps to submit the deposit from a specific account:

1. Select the **deposit from account**. This account does not need to be the author of the proposal; it can be from any token holder. However, if the proposal is deemed malicious, the Decision Deposit will be burned. So, before placing the deposit, it is advised to do your due diligence to ensure the proposal is not malicious
2. The **referendum id** and **decision deposit** fields will automatically be populated for you based on the referendum and Track it belongs to
3. Click **Place deposit** and sign the transaction

![To submit the Decision Deposit, choose the account to place the deposit and click on the "Place deposit" button on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-3.webp)

Once the deposit has been placed, Polkadot.js Apps will update and display the account that paid the Decision Deposit along with the amount of the deposit. Now this referendum is one step closer to meeting the criteria of the Lead-in Period.

If the Prepare Period has passed and there is enough space for a referendum in the General Admin Track, this proposal will move on to the Decide Period.

### How to Vote {: #how-to-vote }

As you may have noticed, voting is not required in the Lead-in Period. However, it is essential in the Decide Period. The steps in this section will apply to referenda in both the Lead-in Period and the Decide Period.

To vote and lock tokens either in favor of or against a referendum, you can get started by clicking on the **Vote** button next to the referendum you want to vote on.

![To vote on a referendum, click on the "Vote" button on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-4.webp)

Then you can take the following steps to fill in the details of the vote:

1. Select the **vote with account**
2. Choose how you would like to vote on the referendum. You can choose **Aye** in favor of the referendum, **Nay** in opposition to it, or **Split** if you want to specify an "Aye" vote value and a "Nay" vote value
3. Enter the vote value
4. Set the vote conviction, which determines the weight of your vote (`vote_weight = tokens * conviction_multiplier`). Please refer to the [Conviction multiplier](/moonbeam-mkdocs/learn/features/governance/#conviction-multiplier) docs for more information
5. Click **Vote** and sign the transaction

![To submit a vote on a referendum, fill out the details of the vote and click on the "Vote" button on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-5.webp)

!!! note
    The lockup periods shown in the previous image are not to be taken as references as they are subject to change.

To see how your vote and all of the other votes for a referendum impacted the Approval and Support curves, you can click on the arrow next to the **Vote** button. You'll notice there are two charts, one for each curve. If you hover over the charts, you can see the minimum Approval or Support required for a specific block along with the current Approval or Support.

![View the Approval and Support curves for a referendum on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-6.webp)

A proposal in the General Admin Track on Moonbase Alpha would have the following characteristics:

 - The Approval curve starts at 100% on Day 0 and goes to 80% on Day 4
 - The Support curve starts at 50% on Day 0 and goes to 10% on Day 7
 - A referendum starts the Decide Period with 0% "Aye" votes (nobody voted in the Lead-in Period)
 - Token holders begin to vote, and the Approval increases to a value above 80% by Day 4
 - If the Approval and Support thresholds are met for the duration of the Confirm Period (14400 blocks, approximately 1 day), the referendum is approved
 - If the Approval and Support thresholds are not met during the Decision Period, the proposal is rejected. Note that the thresholds need to be met for the duration of the Confirm Period. Consequently, if they are met but the Decision Period expires before the completion of the Confirm Period, the proposal is rejected

In the following image, you'll notice enough Approval and Support have been received, so the Confirm Period is underway. If the referendum maintains the Approval and Support levels, at block 124,962, the Confirm Period will end, and then the Enactment Period will begin. You can hover over the charts to find out more information on each of these periods. Assuming this referendum maintains the levels of Approval and Support it has received, the Enactment Period will end at block 132,262, and the proposal action will be dispatched.

![View the Approval and Support curves for a referendum on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-7.webp)

If the referendum doesn't continuously receive enough Approval and Support during the Confirm Period, it still has a chance to pass as long as the Approval and Support requirements are met again and continuously for the duration of the Confirm Period. If a referendum enters the Confirm Period but the Decide Period is set to end before the Confirm Period is over, the Decide Period will actually be extended until the end of the Confirm Period. If the Decide Period ends and the referendum still hasn't received enough Approval and Support, the referendum will be rejected, and the Decision Deposit can be refunded.

The Enactment Period is defined by the author of the proposal at the time it was initially submitted, but it needs to be at least the minimum Enactment Period.

### Delegate Voting {: #delegate-voting }

Token holders have the option to delegate their vote to another account whose opinion they trust. The account being delegated does not need to take any particular action. When they vote, the vote weight (that is, tokens times the Conviction multiplier chosen by the delegator) is added to their vote.

With the introduction of OpenGov (Governance v2), token holders can even delegate their vote on a Track-by-Track basis and specify different delegates for each Track, which is referred to as Multirole Delegation.

From the [referenda page on Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#/referenda), you can click **Delegate** to get started.

![To submit a delegate vote on a referendum, click on the "Delegate" button on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-8.webp)

Then you can take the following steps to fill in the details of the delegation:

1. Enter the **delegate from account**, which should be the account that you wish to delegate your vote from
2. Select the **submission track** or switch the **apply delegation to all tracks** slider to on if you want the other account to vote on your behalf on any of the Tracks
3. Enter the **delegated vote value**
4. Set the vote conviction, which determines the weight of your vote (`vote_weight = tokens * conviction_multiplier`). Please refer to the [Conviction Multiplier](/moonbeam-mkdocs/learn/features/governance/#conviction-multiplier) docs for more information
5. Click **Next**
6. On the next screen, select the **delegate to address**, which should be the account that you wish to delegate your vote to
7. Click **Delegate** and sign the transaction

![Submit a delegate vote on a referendum by filling in all of the delegation details and clicking on the "Delegate" button on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-9.webp)

Now the account you selected to delegate your vote to will be able to vote on your behalf. Once this account votes, the total vote weight delegated will be allocated to the option that the account selected. For this example, Baltahar can vote in favor of a referendum with a total weight of 20000 (10000 tokens with an x2 Conviction factor) using the vote weight that Charleth delegated to him.

You can continue the above process for each Track and delegate a different account with varying vote weights.

To undelegate a delegation, you'll need to head to the **Developer** tab and click on **Extrinsics**. From there, you can take the following steps:

1. Select the account you have delegated from
2. Choose the **convictionVoting** pallet and the **undelegate** extrinsic
3. Enter the **class** of the Origin. For the General Admin Track, it is `2`. For a complete list of Track IDs, refer to the [OpenGov section of the governance overview page](/moonbeam-mkdocs/learn/features/governance/#general-parameters-by-track)
4. Click **Submit transaction** and sign the transaction

![Undelegate a vote on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-10.webp)

### Refunding the Decision Deposit {: #refund-the-decision-deposit }

If a referendum has been approved or rejected, the Decision Deposit will be eligible to be refunded, as long as it was not rejected due to it being a malicious proposal. Malicious proposals will result in the Decision Deposit being slashed. Any token holder can trigger the refund of the deposit back to the original account that placed the deposit. To refund the deposit, you can take the following steps on the [referenda page on Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#/referenda). If the referendum is eligible and the deposit hasn't already been refunded, you'll see a **Refund deposit** button. So, you can go ahead and click that button to get started.

![Get started refunding a Decision Deposit from a passed referendum on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-11.webp)

Then, to submit the refund transaction, you can:

1. Choose the account for which you want to trigger the refund. This does not need to be the account that initially placed the deposit
2. Click **Refund deposit** and sign the transaction

![Refund the Decision Deposit on Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-12.webp)

### Unlocking Locked Tokens {: #unlocking-locked-tokens }

When token holders vote, the tokens used are locked and cannot be transferred. You can verify if you have any locked tokens in the **Accounts** tab by expanding the address's account details. There, you will see different types of balances. If you have any tokens locked in referenda, you'll see **referenda** listed in your balance details, and you can hover over it to find out details about which referendum your tokens are locked for. Different lock statuses include:

 - Locked because of an ongoing referendum, meaning that you've used your tokens and have to wait until the referendum finishes, even if you've voted with a no-lock Conviction factor
 - Locked because of the Conviction multiplier selected, displaying the number of blocks and time left
 - Lock expired, meaning that you can now get your tokens back

![View locked balances on the account page of Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-13.webp)

Once the lock has expired, you can request your tokens back. To do so, navigate to the **Extrinsics** menu under the **Developers** tab. Here, two different extrinsics need to be sent. First, you need to provide the following information:

 1. Select the account from which you want to recover your tokens
 2. Choose the pallet you want to interact with. In this case, it is the `convictionVoting` pallet and the extrinsic to use for the transaction. This will determine the fields that you need to fill in the following steps. In this case, it is `removeVote` extrinsic. This step is necessary to unlock the tokens. This extrinsic can also be used to remove your vote from a referendum
 4. Optionally, you can specify the Track ID to remove votes for. To do so, simply toggle the **include option** slider and enter the Track ID in the **class u16** field
 5. Enter the referendum index. This is the number that appeared on the left-hand side of the **Referenda** tab
 6. Click the **Submit Transaction** button and sign the transaction

![Submit an extrinsic to remove your vote on a referendum in Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-14.webp)

For the next extrinsic, you need to provide the following information:

 1. Select the account from which you want to recover your tokens
 2. Choose the pallet you want to interact with. In this case, it is the `convictionVoting` pallet
 3. Choose the extrinsic method to use for the transaction. This will determine the fields that need to be filled out in the following steps. In this case, it is the `unlock` extrinsic
 4. Enter the Track ID to remove the voting lock for
 5. Enter the target account that will receive the unlocked tokens. In this case, the tokens will be returned to Alice
 6. Click the **Submit Transaction** button and sign the transaction

![Submit an extrinsic to unlock your tokens that were locked in referenda in Polkadot.js Apps.](/moonbeam-mkdocs/images/tokens/governance/voting/vote-15.webp)

Once the transaction goes through, the locked tokens should be unlocked. To double-check, you can go back to the **Accounts** tab and see that your full balance is now **transferable**.
