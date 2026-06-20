---
title: Staking
description: Moonbeam provides staking features where token holders delegate collator candidates with their tokens and earn rewards.
categories:
- Basics
- Staking
url: https://docs.moonbeam.network/learn/features/staking/
word_count: 1958
token_estimate: 4095
version_hash: sha256:564c98150f80b25ef3f93b09682b56941a68a43de62413fa0812c7bfd0ed3f7a
last_updated: '2026-05-21T21:21:53+00:00'
---

# Staking on Moonbeam

## Introduction {: #introduction }

Moonbeam uses a block production mechanism based on [Polkadot's Proof-of-Stake model](https://docs.polkadot.com/reference/polkadot-hub/consensus-and-security/pos-consensus/), where there are collators and validators. [Collators](https://wiki.polkadot.com/learn/learn-collator/) maintain parachains (in this case, Moonbeam) by collecting transactions from users and producing state transition proofs for the relay chain [validators](https://wiki.polkadot.com/learn/learn-validator/).

The candidates in the active set of collators (nodes that produce blocks) are selected based on their stake in the network. And here is where staking comes in.

Collator candidates (and token holders if they delegate) have a stake in the network. The top N candidates by staked amount are chosen to produce blocks with a valid set of transactions, where N is a configurable parameter. Part of each block reward goes to the collators that produced the block, who then share it with the delegators considering their percental contributions towards the collator's stake. In such a way, network members are incentivized to stake tokens to improve the overall security. Since staking is done at a protocol level through the staking interface, if you choose to delegate, the collators you delegate to do not have access to your tokens.

To easily manage staking related actions, you can visit the [Moonbeam DApp](https://apps.moonbeam.network/moonbeam) and use the network tabs at the top of the page to easily switch between Moonbeam networks. To learn how to use the DApp, you can check out the [How to Stake MOVR Tokens](https://moonbeam.network/news/how-to-stake-movr-tokens-on-moonriver-and-earn-staking-rewards) guide or [video tutorial](https://www.youtube.com/watch?v=8GwetYmzEJM), both of which can be adapted for the Moonbeam and the Moonbase Alpha TestNet.

## General Definitions {: #general-definitions }

Some important parameters to understand in relation to the staking system on Moonbeam include:

 - **Round** — a specific number of blocks around which staking actions are enforced. For example, new delegations are enacted when the next round starts. When bonding less or revoking delegations, funds are returned after a specified number of rounds
 - **Candidates** - node operators that are eligible to become block producers if they can acquire enough stake to be in the active set
 - **Collators** — active set of candidates that are selected to be block producers. They collect transactions from users and produce state transition proofs for the relay chain to validate
 - **Delegators** — token holders who stake tokens, vouching for specific collator candidates. Any user that holds a minimum amount of tokens as [free balance](https://wiki.polkadot.com/learn/learn-account-balances/) can become a delegator
 - **Minimum delegation per candidate** — minimum amount of tokens to delegate candidates once a user is in the set of delegators
 - **Maximum delegators per candidate** — maximum number of delegators, by staked amount, that a candidate can have which are eligible to receive staking rewards
 - **Maximum delegations** — maximum number of candidates a delegator can delegate
 - **Exit delay** - an exit delay is the amount of rounds before a candidate or delegator can execute a scheduled request to decrease or revoke a bond, or leave the set of candidates or delegators
 - **Reward payout delay** - a certain amount of rounds must pass before staking rewards are distributed automatically to the free balance
 - **Reward pool** - a portion of the annual inflation that is set aside for collators and delegators
 - **Collator commission** - default fixed percent a collator takes off the top of the due staking rewards. Not related to the reward pool
 - **Delegator rewards** — the aggregate delegator rewards distributed over all eligible delegators, taking into account the relative size of stakes ([read more](/moonbeam-mkdocs/learn/features/staking/#reward-distribution))
 - **Auto-compounding** - a setting that automatically applies a percentage of a delegator's rewards to their total amount delegated
 - **Slashing** — a mechanism to discourage collator misbehavior, where typically the collator and their delegators get slashed by losing a percentage of their stake. Currently, there is no slashing but this can be changed through governance. Collators who produce blocks that are not finalized by the relay chain won't receive rewards

## Quick Reference {: #quick-reference }

=== "Moonbeam"
    |             Variable             |                                                                         Value                                                                         |
    |:--------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|
    |          Round duration          |                        1800 blocks (6 hours)                        |
    | Minimum delegation per candidate |                                                  50 GLMR                                                   |
    | Maximum delegators per candidate |                                                    300                                                    |
    |       Maximum delegations        |                                                    100                                                    |
    |       Reward payout delay        |    2 rounds (12 hours)    |
    |    Add or increase delegation    |                                           takes effect in the next round (funds are withdrawn immediately)                                            |
    |    Decrease delegation delay     |      28 rounds (168 hours)      |
    |     Revoke delegations delay     | 28 rounds (168 hours) |
    |      Leave delegators delay      |   28 rounds (168 hours)   |

=== "Moonriver"
    |             Variable             |                                                                          Value                                                                          |
    |:--------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------:|
    |          Round duration          |                        600 blocks (2 hours)                        |
    | Minimum delegation per candidate |                                                   5 MOVR                                                   |
    | Maximum delegators per candidate |                                                    300                                                     |
    |       Maximum delegations        |                                                    100                                                     |
    |       Reward payout delay        |    2 rounds (4 hours)    |
    |    Add or increase delegation    |                                            takes effect in the next round (funds are withdrawn immediately)                                             |
    |    Decrease delegation delay     |      24 rounds (48 hours)      |
    |     Revoke delegations delay     | 24 rounds (48 hours) |
    |      Leave delegators delay      |   24 rounds (48 hours)   |

=== "Moonbase Alpha"
    |             Variable             |                                                                         Value                                                                         |
    |:--------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|
    |          Round duration          |                        1200 blocks (2 hours)                        |
    | Minimum delegation per candidate |                                                   1 DEV                                                   |
    | Maximum delegators per candidate |                                                    300                                                    |
    |       Maximum delegations        |                                                    100                                                    |
    |       Reward payout delay        |    2 rounds (4 hours)    |
    |    Add or increase delegation    |                                           takes effect in the next round (funds are withdrawn immediately)                                            |
    |    Decrease delegation delay     |      2 rounds (4 hours)      |
    |     Revoke delegations delay     | 2 rounds (4 hours) |
    |      Leave delegators delay      |   2 rounds (4 hours)   |

!!! note
    As of runtime 3000, [asynchronous backing](https://wiki.polkadot.com/learn/learn-async-backing/#asynchronous-backing) has been enabled on all Moonbeam networks. As a result, the target block time was reduced from 12 seconds to 6 seconds, which may break some timing-based assumptions.
To learn how to get the current value of any of the parameters around staking, check out the [Retrieving Staking Parameters](/moonbeam-mkdocs/tokens/staking/stake/#retrieving-staking-parameters) section of the [How to Stake your Tokens](/moonbeam-mkdocs/tokens/staking/stake/) guide.

If you're looking for candidate or collator-specific requirements and information, you can take a look at the [Collators](/moonbeam-mkdocs/node-operators/networks/collators/requirements/#bonding-requirements) guide.

## Resources for Selecting a Collator {: #resources-for-selecting-a-collator}

There are a few resources you can check out to help you select a collator to delegate:

=== "Moonbeam"
    |           Variable           |                                      Value                                      |
    |:----------------------------:|:-------------------------------------------------------------------------------:|
    |     Stake GLMR Dashboard     |              [Stake GLMR](https://www.stakeglmr.com/)               |
    |    Collators Leaderboard     |       [Moonscan](https://moonbeam.moonscan.io/collators)       |

=== "Moonriver"
    |           Variable           |                                      Value                                       |
    |:----------------------------:|:--------------------------------------------------------------------------------:|
    |     Stake MOVR Dashboard     |               [Stake MOVR](https://www.stakemovr.com/)               |
    |    Collators Leaderboard     |       [Moonscan](https://moonriver.moonscan.io/collators)       |

=== "Moonbase Alpha"
    |      Variable      |                                      Value                                       |
    |:------------------:|:--------------------------------------------------------------------------------:|
    | List of candidates | [Moonbase Alpha Subscan](https://moonbase.subscan.io/validator) |

### General Tips {: #general-tips }

- To optimize your staking rewards, you should generally choose a collator with a lower total amount bonded. In that case, your delegation amount will represent a larger portion of the collator’s total stake and you will earn proportionally higher rewards. However, there is a higher risk of the collator being kicked out of the active set and not earning rewards at all
- The minimum bond for each collator tends to increase over time, so if your delegation is close to the minimum, there is a higher chance you might fall below the minimum and not receive rewards
- Spreading delegations between multiple collators is more efficient in terms of rewards, but only recommended if you have enough to stay above the minimum bond of each collator
- You can consider collator performance by reviewing the number of blocks each collator has produced recently
- You can set up auto-compounding which will automatically restake a specified percentage of your delegation rewards

## Reward Distribution {: #reward-distribution }

Rewards for collators and their delegators are calculated at the start of every round for their work prior to the [reward payout delay](#quick-reference). For example, on Moonriver the rewards are calculated for the collators work from 2 rounds ago.

The calculated rewards are then paid out on a block-by-block basis starting at the second block of the round. For every block, one collator will be chosen to receive their entire reward payout from the prior round, along with their delegators, until all rewards have been paid out for that round. For example, if there are 72 collators who produced blocks in the prior round, all of the collators and their delegators will be paid by block 73 of the new round.

You can choose to auto-compound your delegation rewards so you no longer have to manually delegate rewards. If you choose to set up auto-compounding, you can specify the percentage of rewards to be auto-compounded. These rewards will then be automatically added to your delegation.

### Annual Inflation {: #annual-inflation}

The distribution of the annual inflation goes as follows:

=== "Moonbeam"
    |                 Variable                  |                                         Value                                         |
    |:-----------------------------------------:|:-------------------------------------------------------------------------------------:|
    |             Annual inflation              |               5%               |
    | Rewards pool for collators and delegators | 50% of the annual inflation |
    |            Collator commission            | 20% of the annual inflation  |
    |          Parachain bond reserve           |  30% of the annual inflation  |

=== "Moonriver"
    |                 Variable                  |                                         Value                                          |
    |:-----------------------------------------:|:--------------------------------------------------------------------------------------:|
    |             Annual inflation              |               5%               |
    | Rewards pool for collators and delegators | 50% of the annual inflation |
    |            Collator commission            | 20% of the annual inflation  |
    |          Parachain bond reserve           |  30% of the annual inflation  |

=== "Moonbase Alpha"
    |                 Variable                  |                                         Value                                         |
    |:-----------------------------------------:|:-------------------------------------------------------------------------------------:|
    |             Annual inflation              |               5%               |
    | Rewards pool for collators and delegators | 50% of the annual inflation |
    |            Collator commission            | 20% of the annual inflation  |
    |          Parachain bond reserve           |  30% of the annual inflation  |

From the rewards pool, collators get the rewards corresponding to their stake in the network. The rest are distributed among delegators by stake.

### Calculating Rewards {: #calculating-rewards }

Mathematically speaking, for collators, the reward distribution per block proposed and finalized would look like this:

![Staking Collator Reward](/moonbeam-mkdocs/images/learn/features/staking/staking-overview-1.webp)

Where `amount_due` is the corresponding inflation being distributed in a specific block, the `stake` corresponds to the number of tokens bonded by the collator in respect to the total stake of that collator (accounting delegations).

For each delegator, the reward distribution (per block proposed and finalized by the delegated collator) would look like this:

![Staking Delegator Reward](/moonbeam-mkdocs/images/learn/features/staking/staking-overview-2.webp)

Where `amount_due` is the corresponding inflation being distributed in a specific block, the `stake` corresponds to the amount of tokens bonded by each delegator in respect to the total stake of that collator.

## Risks {: #risks }

*Holders of MOVR/GLMR tokens should perform careful due diligence on collators before delegating. Being listed as a collator is not an endorsement or recommendation from the Moonbeam Network, the Moonriver Network, or Moonbeam Foundation. Neither the Moonbeam Network, Moonriver Network, nor Moonbeam Foundation has vetted the list collators and assumes no responsibility with regard to the selection, performance, security, accuracy, or use of any third-party offerings.  You alone are responsible for doing your own diligence to understand the applicable fees and all risks present, including actively monitoring the activity of your collators.*

*You agree and understand that neither the Moonbeam Network, the Moonriver Network, nor Moonbeam Foundation guarantees that you will receive staking rewards and any applicable percentage provided (i) is an estimate only and not guaranteed, (ii) may change at any time and (iii) may be more or less than the actual staking rewards you receive. The Moonbeam Foundation makes no representations as to the monetary value of any rewards at any time.*

*Staking MOVR/GLMR tokens is not free of risk.*
*Staked MOVR/GLMR tokens are locked up, and retrieving them requires a 2 day/7 day waiting period .*
*Additionally, if a collator fails to perform required functions or acts in bad faith, a portion of their total stake can be slashed (i.e. destroyed). This includes the stake of their delegators. If a collators behaves suspiciously or is too often offline, delegators can choose to unbond from them or switch to another collator. Delegators can also mitigate risk by electing to distribute their stake across multiple collators.*
