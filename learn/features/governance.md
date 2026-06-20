---
title: Governance
description: As a Polkadot parachain, Moonbeam uses an on-chain governance system, allowing for a stake-weighted vote on public referenda.
categories:
- Governance
- Basics
url: https://docs.moonbeam.network/learn/features/governance/
word_count: 4140
token_estimate: 13238
version_hash: sha256:8fd064f22cca3717929adae08e047165fef231f337fe7c0c1f64306efcdf3983
last_updated: '2026-05-21T21:21:53+00:00'
---

# Governance on Moonbeam

## Introduction {: #introduction }

The goal of Moonbeam’s governance mechanism is to advance the protocol according to the desires of the community. In that shared mission, the governance process seeks to include all token holders. Any and all changes to the protocol must go through a referendum so that all token holders, weighted by stake, can have input on the decision.

Governance forums like the [Moonbeam Community Forum](https://forum.moonbeam.network) and [Polkassembly](https://moonbeam.polkassembly.io/opengov) enable open discussion and allow proposals to be refined based on community input. Autonomous enactments and [forkless upgrades](https://wiki.polkadot.com/learn/learn-runtime-upgrades/#forkless-upgrades) unite the community towards a shared mission to advance the protocol.

With the rollout of OpenGov (originally referred to as Gov2), the second phase of governance in Polkadot, several modifications have been introduced to the governance process. You can read the [OpenGov: What is Polkadot Gov2](https://moonbeam.network/news/opengov-what-is-polkadot-gov2) blog post, which provides an overview of all of the changes made in OpenGov.

As of runtime 2400, all Moonbeam networks use OpenGov as their governance system.

## Principles {: #principles }

Guiding "soft" principles for engagement with Moonbeam's governance process include:

 - Being inclusive to token holders that want to engage with Moonbeam and that are affected by governance decisions
 - Favoring token holder engagement, even with views contrary to our own, versus a lack of engagement
 - A commitment to openness and transparency in the decision-making process
 - Working to keep the greater good of the network above personal gain
 - Acting at all times as a moral agent that considers the consequences of action (or inaction) from a moral standpoint
 - Being patient and generous in our interactions with other token holders, but not tolerating abusive or destructive language, actions, and behavior, and abiding by [Moonbeam’s Code of Conduct](https://github.com/moonbeam-foundation/code-of-conduct)

These points were heavily inspired by Vlad Zamfir’s writings on governance. Refer to his articles, especially the [How to Participate in Blockchain Governance in Good Faith (and with Good Manners)](https://medium.com/@Vlad_Zamfir/how-to-participate-in-blockchain-governance-in-good-faith-and-with-good-manners-bd4e16846434) Medium article.

## On-Chain Governance Mechanics {: #on-chain-governance-mechanics }

The "hard" governance process for Moonbeam will be driven by an on-chain process that allows the majority of tokens on the network to determine the outcomes of key decisions around the network. These decision points come in the form of stake-weighted voting on proposed referenda.

Some of the main components of this governance model include:

 - **Referenda** — a stake-based voting scheme where each referendum is tied to a specific proposal for a change to the Moonbeam system including values for key parameters, code upgrades, or changes to the governance system itself
 - **Voting** — referenda will be voted on by token holders on a stake-weighted basis. Referenda which pass are subject to delayed enactment so that people who disagree with the direction of the decision have time to exit the network
 - **Council & Technical Committee Governance V1** — a group of community members who have special voting rights within the system. With the deprecation and removal of Governance v1, both of these committees were dissolved as of the [runtime 2800 release](https://forum.moonbeam.network/t/runtime-rt2801-schedule/1616/4)
 - **OpenGov Technical Committee** — a group of community members who can add certain proposals to the Whitelisted Track

For more details on how these Substrate frame pallets implement on-chain governance, you can check out the [Polkadot Governance Wiki](https://wiki.polkadot.com/learn/learn-polkadot-opengov/).

## Governance v2: OpenGov {: #opengov }

This section will cover everything you need to know about OpenGov on Moonbeam.

### General Definitions {: #general-definitions-gov2 }

 - **Proposal** — an action or item, defined by the preimage hash, being proposed by a token holder and open for consideration and discussion by token holders
 - **Referendum** — a proposal that is up for token-holder voting. Each referendum is tied to a specific proposal for a change to the Moonbeam system including values for key parameters, code upgrades, or changes to the governance system itself
 - **Preimage hash** — hash of the proposal to be enacted. The first step to make a proposal is to submit a preimage. The hash is just its identifier. The proposer of the preimage can be different than the user that proposes that preimage as a formal proposal
 - **Preimage deposit** — amount of tokens that the proposer needs to bond when submitting a preimage. It is calculated as the sum of a base deposit per network plus a fee per byte of the preimage being proposed
 - **Origin** - an authorization-based dispatch source for an operation, which is used to determine the Track that a referendum is posted under
 - **Track** - an Origin-specific pipeline that outlines the life cycle of proposals. Currently, there are five Tracks:

    |    Origin Track     |                                   Description                                    |                         Referendum Examples                          |
    |:-------------------:|:--------------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
    |        Root         |                                Highest privilege                                 |           Runtime upgrades, Technical Committee management           |
    |     Whitelisted     | Proposals to be whitelisted by the Technical Committee before being dispatched |                       Fast-tracked operations                        |
    |    General Admin    |                          For general on-chain decisions                          | Changes to XCM fees, Orbiter program, Staking parameters, Registrars |
    | Emergency Canceller |          For cancellation of a referendum. Decision Deposit is refunded          |                    Wrongly constructed referendum                    |
    |  Emergency Killer   |       For killing of bad/malicious referendum. Decision Deposit is slashed       |                         Malicious referendum                         |
    | Fast General Admin  |                      For faster general on-chain decisions                       |                       HRMP channel management                        |

Tracks have different criteria parameters that are proportional to their level of Origin class. For example, more dangerous and privileged referenda will have more safeguards, higher thresholds, and longer consideration periods for approval. Please refer to the [Governance Parameters](#governance-parameters-v2) section for more information.

 - **Voting** — a mechanism for token holders to support (Aye), oppose (Nay), or remain neutral (Abstain) on a proposal. For Aye and Nay, the voting weight is determined by both the number of tokens locked and the lock duration (Conviction). Abstain votes do not receive additional weighting
    - **Conviction** — the time that token holders voluntarily lock their tokens when voting; the longer they are locked, the more weight their vote has
    - **Lock balance** — the number of tokens that a user commits to a vote (note, this is not the same as a user's total account balance)
    Moonbeam uses the concept of voluntary locking, which allows token holders to increase their voting power by locking tokens for a longer period of time. Specifying no Lock Period means a user's vote is valued at 10% of their lock balance. Specifying a greater Conviction increases voting power. For each increase in Conviction (vote multiplier), the Lock Periods double
 - **Approval** — minimum "Aye" votes as a percentage of overall Conviction-weighted votes needed for approval
 - **Support** — the minimum portion of Aye and Abstain votes (ignoring conviction) needed as a percentage of the total active supply for a proposal to pass. Nay votes do not count toward Support
 - **Lead-in Period** — the initial proposal voting and discussion period. At this stage, proposals are in an undecided state until they pass some criteria for the given Track. The criteria include:
    - **Prepare Period** — the minimum time the referendum needs to wait before it can progress to the next phase after submission
    - **Capacity** — limit for the number of referenda on a given Track that can be decided at once
    - **Decision Deposit** — the minimum deposit amount required for a referendum to progress to the decision phase after the end of the Lead-in Period. Since each Track has a defined Capacity, this deposit is larger than the submission deposit, and its goal is to mitigate spam 
    
 - **Decide Period** - token holders continue to vote on the referendum. If a referendum does not pass by the end of the period, it will be rejected, and the Decision Deposit will be refunded
 - **Confirm Period** - a period of time within the Decide Period where the referendum needs to have maintained enough Approval and Support to be approved and move to the Enactment Period
 - **Enactment Period** - a specified time, which is defined at the time the proposal was created, that an approved referendum waits before it can be dispatched. There is a minimum amount of time for each Track

 - **Vote Delegation** — a voter can give their voting power, including Conviction voting, to another token holder (delegate), who may be more knowledgeable and able to make specific decisions
 - **Multirole Delegation** — the ability to delegate voting power on a Track-by-Track basis, where a token holder can specify different delegates for each Track
### Governance Parameters {: #governance-parameters-v2 }

=== "Moonbeam"  
    |          Variable           |                           Value                            |
    |:---------------------------:|:----------------------------------------------------------:|
    |    Preimage base deposit    |     500 GLMR     |
    |  Preimage deposit per byte  |     0.01 GLMR     |
    | Proposal Submission Deposit | 1000 GLMR |

=== "Moonriver"
    |          Variable           |                            Value                            |
    |:---------------------------:|:-----------------------------------------------------------:|
    |    Preimage base deposit    |     5 MOVR     |
    |  Preimage deposit per byte  |     0.0001 MOVR     |
    | Proposal Submission Deposit | 10 MOVR |

=== "Moonbase Alpha"
    |          Variable           |                           Value                           |
    |:---------------------------:|:---------------------------------------------------------:|
    |    Preimage base deposit    |     5 DEV     |
    |  Preimage deposit per byte  |     0.0001 DEV     |
    | Proposal Submission Deposit | 10 DEV |

#### General Parameters by Track {: #general-parameters-by-track }

=== "Moonbeam"
    |         Track          | Track ID |                                      Capacity                                       |                                Decision<br>Deposit                                 |
    |:----------------------:|:--------:|:-----------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
    |          Root          |    0     |        5 proposals        |        2000000 GLMR        |
    |      Whitelisted       |    1     |    100 proposals     |    200000 GLMR     |
    |     General Admin      |    2     |   10 proposals    |   10000 GLMR    |
    | Emergency<br>Canceller |    3     |     20 proposals      |     200000 GLMR      |
    |  Emergency<br>Killer   |    4     |       100 proposals       |       400000 GLMR       |
    |   Fast General Admin   |    5     | 10 proposals | 10000 GLMR |

=== "Moonriver"
    |         Track          | Track ID |                                       Capacity                                       |                                 Decision<br>Deposit                                 |
    |:----------------------:|:--------:|:------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
    |          Root          |    0     |        5 proposals        |        100000 MOVR        |
    |      Whitelisted       |    1     |    100 proposals     |    10000 MOVR     |
    |     General Admin      |    2     |   10 proposals    |   500 MOVR    |
    | Emergency<br>Canceller |    3     |     20 proposals      |     10000 MOVR      |
    |  Emergency<br>Killer   |    4     |       100 proposals       |       20000 MOVR       |
    |   Fast General Admin   |    5     | 10 proposals | 500 MOVR |

=== "Moonbase Alpha"
    |         Track          | Track ID |                                      Capacity                                       |                                Decision<br>Deposit                                |
    |:----------------------:|:--------:|:-----------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
    |          Root          |    0     |        5 proposals        |        100000 DEV        |
    |      Whitelisted       |    1     |    100 proposals     |    10000 DEV     |
    |     General Admin      |    2     |   10 proposals    |   500 DEV    |
    | Emergency<br>Canceller |    3     |     20 proposals      |     10000 DEV      |
    |  Emergency<br>Killer   |    4     |       100 proposals       |       20000 DEV       |
    |   Fast General Admin   |    5     | 10 proposals | 500 DEV |

#### Period Parameters by Track {: #period-parameters-by-track }

=== "Moonbeam"
    |         Track          |                                                                                Prepare<br>Period                                                                                 |                                                                                  Decide<br>Period                                                                                  |                                                                                Confirm<br>Period                                                                                 |                                                                                 Minimum<br>Enactment Period                                                                                  |
    |:----------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
    |          Root          |               14400 blocks <br>(1 day)               |               201600 blocks<br> (14 days)               |               14400 blocks<br> (1 day)               |               14400 blocks<br> (1 day)               |
    |      Whitelisted       |        100 blocks<br> (10 minutes)        |        201600 blocks<br> (14 days)        |        100 blocks<br> (10 minutes)        |        300 blocks<br> (30 minutes)        |
    |     General Admin      |      600 blocks<br> (1 hour)      |      201600 blocks<br> (14 days)      |      14400 blocks<br> (1 day)      |      14400 blocks<br> (1 day)      |
    | Emergency<br>Canceller |          600 blocks<br> (1 hour)          |          201600 blocks<br> (14 days)          |          1800 blocks<br> (3 hours)          |          100 blocks<br> (10 minutes)          |
    |  Emergency<br>Killer   |             600 blocks<br> (1 hour)             |             201600 blocks<br> (14 days)             |             1800 blocks<br> (3 hours)             |             100 blocks<br> (10 minutes)             |
    |   Fast General Admin   | 600 blocks<br> (1 hour) | 201600 blocks<br> (14 days) | 1800 blocks<br> (3 hours) | 100 blocks<br> (10 minutes) |

=== "Moonriver"
    |         Track          |                                                                                 Prepare<br>Period                                                                                  |                                                                                   Decide<br>Period                                                                                   |                                                                                 Confirm<br>Period                                                                                  |                                                                                  Minimum<br>Enactment Period                                                                                   |
    |:----------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
    |          Root          |               14400 blocks <br>(1 day)               |               201600 blocks<br> (14 days)               |               14400 blocks<br> (1 day)               |               14400 blocks<br> (1 day)               |
    |      Whitelisted       |        100 blocks<br> (10 minutes)        |        201600 blocks<br> (14 days)        |        100 blocks<br> (10 minutes)        |        300 blocks<br> (30 minutes)        |
    |     General Admin      |      600 blocks<br> (1 hour)      |      201600 blocks<br> (14 days)      |      14400 blocks<br> (1 day)      |      14400 blocks<br> (1 day)      |
    | Emergency<br>Canceller |          600 blocks<br> (1 hour)          |          201600 blocks<br> (14 days)          |          1800 blocks<br> (3 hours)          |          100 blocks<br> (10 minutes)          |
    |  Emergency<br>Killer   |             600 blocks<br> (1 hour)             |             201600 blocks<br> (14 days)             |             1800 blocks<br> (3 hours)             |             100 blocks<br> (10 minutes)             |
    |   Fast General Admin   | 600 blocks<br> (1 hour) | 201600 blocks<br> (14 days) | 1800 blocks<br> (3 hours) | 100 blocks<br> (10 minutes) |

=== "Moonbase Alpha"
    |         Track          |                                                                                Prepare<br>Period                                                                                 |                                                                                  Decide<br>Period                                                                                  |                                                                                Confirm<br>Period                                                                                 |                                                                                 Minimum<br>Enactment Period                                                                                  |
    |:----------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
    |          Root          |               14400 blocks <br>(1 day)               |               201600 blocks<br> (14 days)               |               14400 blocks<br> (1 day)               |               14400 blocks<br> (1 day)               |
    |      Whitelisted       |        100 blocks<br> (10 minutes)        |        201600 blocks<br> (14 days)        |        100 blocks<br> (10 minutes)        |        300 blocks<br> (30 minutes)        |
    |     General Admin      |      600 blocks<br> (1 hour)      |      201600 blocks<br> (14 days)      |      14400 blocks<br> (1 day)      |      14400 blocks<br> (1 day)      |
    | Emergency<br>Canceller |          600 blocks<br> (1 hour)          |          201600 blocks<br> (14 days)          |          1800 blocks<br> (3 hours)          |          100 blocks<br> (10 minutes)          |
    |  Emergency<br>Killer   |             600 blocks<br> (1 hour)             |             201600 blocks<br> (14 days)             |             1800 blocks<br> (3 hours)             |             100 blocks<br> (10 minutes)             |
    |   Fast General Admin   | 600 blocks<br> (1 hour) | 201600 blocks<br> (14 days) | 1800 blocks<br> (3 hours) | 100 blocks<br> (10 minutes) |

!!! note
    As of runtime 3000, [asynchronous backing](https://wiki.polkadot.com/learn/learn-async-backing/#asynchronous-backing) has been enabled on all Moonbeam networks. As a result, the target block time was reduced from 12 seconds to 6 seconds, which may break some timing-based assumptions.
#### Support and Approval Parameters by Track {: #support-and-approval-parameters-by-track }

=== "Moonbeam"
    |         Track          | Approval Curve |                                                                                                                                                                                                                                                 Approval Parameters                                                                                                                                                                                                                                                  | Support Curve |                                                                                                                                                                                                                                               Support Parameters                                                                                                                                                                                                                                               |
    |:----------------------:|:--------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
    |          Root          |   Reciprocal   |                                           Day 0: 100%<br>Day 4: 80%<br>Day 14: 50%                                           |    Linear     |                                                                                                                Day 0: 25%<br>Day 14: 0.5%                                                                                                                |
    |      Whitelisted       |   Reciprocal   |                      Day 0: 100%<br>Day 1: 96%<br>Day 14: 50%                      |  Reciprocal   |                      Day 0: 2%<br>Hour 1: 1%<br>Day 14: 0%                      |
    |     General Admin      |   Reciprocal   |                Day 0: 100%<br>Day 4: 80%<br>Day 14: 50%                |  Reciprocal   |                Day 0: 50%<br>Day 7: 10%<br>Day 14: 0%                |
    | Emergency<br>Canceller |   Reciprocal   |                            Day 0: 100%<br>Day 1: 96%<br>Day 14: 50%                            |  Reciprocal   |                            Day 0: 10%<br>Day 1: 1%<br>Day 14: 0%                            |
    |  Emergency<br>Killer   |   Reciprocal   |                                     Day 0: 100%<br>Day 1: 96%<br>Day 14: 50%                                     |  Reciprocal   |                                     Day 0: 10%<br>Day 1: 1%<br>Day 14: 0%                                     |
    |   Fast General Admin   |   Reciprocal   | Day 0: 100%<br>Day 4: 80%<br>Day 14: 50% |  Reciprocal   | Day 0: 50%<br>Day 5: 1%<br>Day 14: 0% |

=== "Moonriver"
    |         Track          | Approval Curve |                                                                                                                                                                                                                                                    Approval Parameters                                                                                                                                                                                                                                                     | Support Curve |                                                                                                                                                                                                                                                  Support Parameters                                                                                                                                                                                                                                                  |
    |:----------------------:|:--------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
    |          Root          |   Reciprocal   |                                           Day 0: 100%<br>Day 4: 80%<br>Day 14: 50%                                           |    Linear     |                                                                                                                 Day 0: 25%<br>Day 14: 0.5%                                                                                                                 |
    |      Whitelisted       |   Reciprocal   |                      Day 0: 100%<br>Day 1: 96%<br>Day 14: 50%                      |  Reciprocal   |                      Day 0: 2%<br>Hour 1: 1%<br>Day 14: 0%                      |
    |     General Admin      |   Reciprocal   |                Day 0: 100%<br>Day 4: 80%<br>Day 14: 50%                |  Reciprocal   |                Day 0: 50%<br>Day 7: 10%<br>Day 14: 0%                |
    | Emergency<br>Canceller |   Reciprocal   |                            Day 0: 100%<br>Day 1: 96%<br>Day 14: 50%                            |  Reciprocal   |                            Day 0: 10%<br>Day 1: 1%<br>Day 14: 0%                            |
    |  Emergency<br>Killer   |   Reciprocal   |                                     Day 0: 100%<br>Day 1: 96%<br>Day 14: 50%                                     |  Reciprocal   |                                     Day 0: 10%<br>Day 1: 1%<br>Day 14: 0%                                     |
    |   Fast General Admin   |   Reciprocal   | Day 0: 100%<br>Day 4: 80%<br>Day 14: 50% |  Reciprocal   | Day 0: 50%<br>Day 5: 1%<br>Day 14: 0% |

=== "Moonbase Alpha"
    |         Track          | Approval Curve |                                                                                                                                                                                                                                                 Approval Parameters                                                                                                                                                                                                                                                  | Support Curve |                                                                                                                                                                                                                                               Support Parameters                                                                                                                                                                                                                                               |
    |:----------------------:|:--------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
    |          Root          |   Reciprocal   |                                           Day 0: 100%<br>Day 4: 80%<br>Day 14: 50%                                           |    Linear     |                                                                                                                Day 0: 25%<br>Day 14: 0.5%                                                                                                                |
    |      Whitelisted       |   Reciprocal   |                      Day 0: 100%<br>Day 1: 96%<br>Day 14: 50%                      |  Reciprocal   |                      Day 0: 2%<br>Hour 1: 1%<br>Day 14: 0%                      |
    |     General Admin      |   Reciprocal   |                Day 0: 100%<br>Day 4: 80%<br>Day 14: 50%                |  Reciprocal   |                Day 0: 50%<br>Day 7: 10%<br>Day 14: 0%                |
    | Emergency<br>Canceller |   Reciprocal   |                            Day 0: 100%<br>Day 1: 96%<br>Day 14: 50%                            |  Reciprocal   |                            Day 0: 50%<br>Day 1: 1%<br>Day 14: 0%                            |
    |  Emergency<br>Killer   |   Reciprocal   |                                     Day 0: 100%<br>Day 1: 96%<br>Day 14: 50%                                     |  Reciprocal   |                                     Day 0: 10%<br>Day 1: 1%<br>Day 14: 0%                                     |
    |   Fast General Admin   |   Reciprocal   | Day 0: 100%<br>Day 4: 80%<br>Day 14: 50% |  Reciprocal   | Day 0: 50%<br>Day 5: 1%<br>Day 14: 0% |

#### Conviction Multiplier {: #conviction-multiplier-v2 }

The Conviction multiplier is related to the number of Enactment Periods the tokens will be locked for after the referenda is enacted (if approved). Consequently, the longer you are willing to lock your tokens, the stronger your vote will be weighted. You also have the option of not locking tokens at all, but vote weight is drastically reduced (tokens are still locked during the duration of the referendum).

If you were to vote 1000 tokens with a 6x Conviction, your weighted vote would be 6000 units. That is, 1000 locked tokens multiplied by the Conviction, which in this scenario would be 6. On the other hand, if you decided you didn't want to have your tokens locked after enactment, you could vote your 1000 tokens with a 0.1x Conviction. In this case, your weighted vote would only be 100 units.

The Conviction multiplier values for each network are:

=== "Moonbeam"
    | Lock Periods After Enactment | Conviction Multiplier |                       Approx. Lock Time                        |
    |:----------------------------:|:---------------------:|:--------------------------------------------------------------:|
    |              0               |          0.1          |                              None                              |
    |              1               |           1           | 1 day  |
    |              2               |           2           | 2 days |
    |              4               |           3           | 4 days |
    |              8               |           4           | 8 days |
    |              16              |           5           | 16 days |
    |              32              |           6           | 32 days |

=== "Moonriver"
    | Lock Periods After Enactment | Conviction Multiplier |                        Approx. Lock Time                        |
    |:----------------------------:|:---------------------:|:---------------------------------------------------------------:|
    |              0               |          0.1          |                              None                               |
    |              1               |           1           | 1 day  |
    |              2               |           2           | 2 days |
    |              4               |           3           | 4 days |
    |              8               |           4           | 8 days |
    |              16              |           5           | 16 days |
    |              32              |           6           | 32 days |

=== "Moonbase Alpha"
    | Lock Periods After Enactment | Conviction Multiplier |                       Approx. Lock Time                        |
    |:----------------------------:|:---------------------:|:--------------------------------------------------------------:|
    |              0               |          0.1          |                              None                              |
    |              1               |           1           | 1 day  |
    |              2               |           2           | 2 days |
    |              4               |           3           | 4 days |
    |              8               |           4           | 8 days |
    |              16              |           5           | 16 days |
    |              32              |           6           | 32 days |

!!! note
    The lock time approximations are based upon regular 6-second block times. Block production may vary and thus the displayed lock times should not be deemed exact.

### Roadmap of a Proposal {: #roadmap-of-a-proposal-v2 }

Before a proposal is submitted, the author of the proposal can submit their proposal idea to the designated Democracy Proposals section of the [Moonbeam Governance discussion forum](https://forum.moonbeam.network/c/governance/2) for feedback from the community for at least five days. From there, the author can make adjustments to the proposal based on the feedback they've collected.

Once the author is ready, they can submit their proposal on-chain. To do so, first, they need to submit the preimage of the proposal. The submitter needs to bond a fee to store the preimage on-chain. The bond is returned once the submitter unnotes the preimage. Next, they can submit the actual proposal and pay the Submission Deposit, which is enough to cover the on-chain storage cost of the proposal. Then the Lead-in Period begins and the community can begin voting "Aye" or "Nay" on the proposal by locking tokens. In order for the referendum to advance and move out of the Lead-in Period to the Decide period, the following criteria must be met:

- The referendum must wait the duration of the Prepare Period, which allows for adequate time to discuss the proposal before it progresses to the next phase
- There is enough Capacity in the chosen Track
- A Decision Deposit has been made that meets the minimum requirements for the Track

If a referendum meets the above criteria, it moves to the Decide Period and takes up one of the spots in its designated Track. In the Decide Period, voting continues and the referendum has a set amount of days to reach the Approval and Support requirements needed for it to progress to the Confirm Period.

Once in the Confirm Period, a referendum must continuously meet the Approval and Support requirements for the duration of the period. If a referendum fails to meet the requirements at any point, it is returned to the Decide Period. If the referendum meets the Approval and Support requirements again, it can progress to the Confirm Period again and the Decide Period will be delayed until the end of the Confirm Period. If the Decide Period ends and not enough Approval and Support was received, the referendum will be rejected and the Decision Deposit will be returned. The proposal can be proposed again at any time.

If a referendum continuously receives enough Approval and Support during the Confirm Period, it will be approved and move to the Enactment Period. It will wait the duration of the Enactment Period before it gets dispatched.

The happy path for a proposal is shown in the following diagram:

![A happy path diagram of the proposal roadmap in OpenGov.](/moonbeam-mkdocs/images/learn/features/governance/proposal-roadmap.webp)

### Proposal Example Walkthrough

A proposal (with its preimage) is submitted for the General Admin Track on Moonriver would have the following characteristics:

 - The Approval curve starts at 100% on Day 0, goes to 80% on Day 4
 - The Support curve starts at 50% on Day 0, goes to 10% on Day 7
 - A referendum starts the Decide Period with 0% "Aye" votes (nobody voted in the Lead-in Period)
 - Token holders begin to vote and the Approval increases to a value above 80% by Day 4
 - If the Approval and Support thresholds are met for the duration of the Confirm Period (14400 blocks, approximately 1 day), the referendum is approved
 - If the Approval and Support thresholds are not met during the Decision Period, the proposal is rejected. Note that the thresholds need to be met for the duration of the Confirm Period. Consequently, if they are met but the Decision Period expires before the completion of the Confirm Period, the proposal is rejected

The Approval and Support percentages can be calculated using the following:

=== "Approval"

    ```text
    Approval = 100 * ( Total Conviction-weighted "Aye" votes / Total Conviction-weighted votes ) 
    ```

=== "Support"

    ```text
    Support = 100 * ( Total Aye + Abstain votes, ignoring conviction / Total supply )
    ```

### Proposal Cancellations {: #proposal-cancellations }

In the event that a proposal already in the voting stage is found to have an issue, it may be necessary to prevent its approval. These instances may involve malicious activity or technical issues that make the changes impossible to implement due to recent upgrades to the network.

Cancellations must be voted on by the network to be executed. Cancellation proposals are faster than a typical proposal because they must be decided before the enactment of the proposal they seek to cancel, but they follow the same process as other referenda.

There is a cancellation Origin for use against referenda that contain an unforeseen problem, called the Emergency Canceller. The Emergency Canceller Origin and the Root Origin are allowed to cancel referenda. Regardless of the Origin, if a proposal is cancelled, it gets rejected and the Decision Deposit gets refunded.

In addition, there is a Kill Origin, which is for bad referenda intending to harm the network, called Emergency Killer. The Emergency Killer Origin and the Root Origin have the ability to kill referenda. In this case, a proposal is cancelled and the Decision Deposit is slashed, meaning the deposit amount is burned regardless of the Origin.

### Rights of the OpenGov Technical Committee {: #rights-of-the-opengov-technical-committee }


On Polkadot, the Technical Committee from Governance v1 was replaced by the [Fellowship](https://wiki.polkadot.com/learn/learn-polkadot-technical-fellowship/), a self-governing expert body composed of members with deep technical knowledge of the Kusama and Polkadot networks protocols.

For Moonbeam's implementation of OpenGov, instead of the Fellowship, there is a community OpenGov Technical Committee that has very similar power to that of the Fellowship. Their power in governance resides in their ability to whitelist a proposal. OpenGov Technical Committee members may only vote to whitelist a proposal if whitelisting that proposal would protect against a security vulnerability to the network. The passing threshold of the OpenGov Technical Committee members on whether to whitelist a proposal is determined by governance. As such, the OpenGov Technical Committee has very limited power over the network. Its purpose is to provide technical review of urgent security issues that are proposed by token holders.

While still subject to governance, the idea behind the Whitelist track is that it will have different parameters to make it faster for proposals to pass. The Whitelist Track parameters, including approval, support, and voting, are determined by the Moonriver or Moonbeam token holders through governance and cannot be changed by the OpenGov Technical Committee.

The OpenGov Technical Committee is made up of members of the community who have technical knowledge and expertise in Moonbeam-based networks.

### Related Guides on OpenGov {: #try-it-out }

For related guides on submitting and voting on referenda on Moonbeam with OpenGov, please check the following guides:

 - [How to Submit a Proposal](/moonbeam-mkdocs/tokens/governance/proposals/)
 - [How to Vote on a Proposal](/moonbeam-mkdocs/tokens/governance/voting/)
 - [Interact with the Preimages Precompiled Contract (Solidity Interface)](/moonbeam-mkdocs/builders/ethereum/precompiles/features/governance/preimage/)
 - [Interact with the Referenda Precompiled Contract (Solidity Interface)](/moonbeam-mkdocs/builders/ethereum/precompiles/features/governance/referenda/)
 - [Interact with the Conviction Voting Precompiled Contract (Solidity Interface)](/moonbeam-mkdocs/builders/ethereum/precompiles/features/governance/conviction-voting/)
