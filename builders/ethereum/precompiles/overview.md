---
title: Solidity Precompiles
description: An overview of the available Solidity precompiles on Moonbeam. Precompiles enable you to interact with Substrate features using the Ethereum API.
categories:
- Reference
- Basics
url: https://docs.moonbeam.network/builders/ethereum/precompiles/overview/
word_count: 2054
token_estimate: 6385
version_hash: sha256:5ebc25753131f81fbe09df091f8a5bde5d317c0a9ce732ba0e7f1c00973d3303
last_updated: '2026-05-21T21:21:53+00:00'
---

# Overview of the Precompiled Contracts on Moonbeam

## Overview {: #introduction }

On Moonbeam, a precompiled contract is native Substrate code that has an Ethereum-style address and can be called using the Ethereum API, like any other smart contract. The precompiles allow you to call the Substrate runtime directly which is not normally accessible from the Ethereum side of Moonbeam.

The Substrate code responsible for implementing precompiles can be found in the [EVM pallet](https://polkadot-evm.github.io/frontier/rustdocs/pallet_evm/). The EVM pallet includes the [standard precompiles found on Ethereum and some additional precompiles that are not specific to Ethereum](https://github.com/polkadot-evm/frontier/tree/master/frame/evm/precompile). It also provides the ability to create and execute custom precompiles through the generic [`Precompiles` trait](https://polkadot-evm.github.io/frontier/rustdocs/pallet_evm/trait.Precompile.html). There are several custom Moonbeam-specific precompiles that have been created, all of which can be found in the [Moonbeam codebase](https://github.com/moonbeam-foundation/moonbeam/tree/master/precompiles). It is important to highlight that the precompiles from this list with the `CallableByContract` check are not callable inside the contract constructor.

The Ethereum precompiled contracts contain complex functionality that is computationally intensive, such as hashing and encryption. The custom precompiled contracts on Moonbeam provide access to Substrate-based functionality such as staking, governance, XCM-related functions, and more.

The Moonbeam-specific precompiles can be interacted with through familiar and easy-to-use Solidity interfaces using the Ethereum API, which are ultimately used to interact with the underlying Substrate interface. This flow is depicted in the following diagram:

![Precompiled Contracts Diagram](/moonbeam-mkdocs/images/builders/ethereum/precompiles/overview/overview-1.webp)

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## Precompiled Contract Addresses {: #precompiled-contract-addresses }

The precompiled contracts are categorized by address and based on the origin network. If you were to convert the precompiled addresses to decimal format, and break them into categories by numeric value, the categories are as follows:

- **0-1023** - [Ethereum MainNet precompiles](#ethereum-mainnet-precompiles)
- **1024-2047** - precompiles that are [not in Ethereum and not Moonbeam specific](#non-moonbeam-specific-nor-ethereum-precompiles)
- **2048-4095** - [Moonbeam specific precompiles](#moonbeam-specific-precompiles)

### Ethereum MainNet Precompiles {: #ethereum-mainnet-precompiles }

=== "Moonbeam"
    |                                                          Contract                                                           |                  Address                   |
    |:---------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------:|
    |      [ECRECOVER](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#verify-signatures-with-ecrecover)      | 0x0000000000000000000000000000000000000001 |
    |              [SHA256](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#hashing-with-sha256)              | 0x0000000000000000000000000000000000000002 |
    |          [RIPEMD160](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#hashing-with-ripemd-160)           | 0x0000000000000000000000000000000000000003 |
    |            [Identity](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#the-identity-function)            | 0x0000000000000000000000000000000000000004 |
    |    [Modular Exponentiation](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#modular-exponentiation)     | 0x0000000000000000000000000000000000000005 |
    |                  [BN128Add](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#bn128add)                   | 0x0000000000000000000000000000000000000006 |
    |                  [BN128Mul](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#bn128mul)                   | 0x0000000000000000000000000000000000000007 |
    |              [BN128Pairing](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#bn128pairing)               | 0x0000000000000000000000000000000000000008 |
    | [Blake2](https://polkadot-evm.github.io/frontier/rustdocs/pallet_evm_precompile_blake2/struct.Blake2F.html) | 0x0000000000000000000000000000000000000009 |
    |                 [P256Verify](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7212.md)                 | 0x0000000000000000000000000000000000000100 |

=== "Moonriver"
    |                                                          Contract                                                           |                  Address                   |
    |:---------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------:|
    |      [ECRECOVER](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#verify-signatures-with-ecrecover)      | 0x0000000000000000000000000000000000000001 |
    |              [SHA256](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#hashing-with-sha256)              | 0x0000000000000000000000000000000000000002 |
    |          [RIPEMD160](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#hashing-with-ripemd-160)           | 0x0000000000000000000000000000000000000003 |
    |            [Identity](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#the-identity-function)            | 0x0000000000000000000000000000000000000004 |
    |    [Modular Exponentiation](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#modular-exponentiation)     | 0x0000000000000000000000000000000000000005 |
    |                  [BN128Add](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#bn128add)                   | 0x0000000000000000000000000000000000000006 |
    |                  [BN128Mul](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#bn128mul)                   | 0x0000000000000000000000000000000000000007 |
    |              [BN128Pairing](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#bn128pairing)               | 0x0000000000000000000000000000000000000008 |
    | [Blake2](https://polkadot-evm.github.io/frontier/rustdocs/pallet_evm_precompile_blake2/struct.Blake2F.html) | 0x0000000000000000000000000000000000000009 |
    |                 [P256Verify](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7212.md)                 | 0x0000000000000000000000000000000000000100 |

=== "Moonbase Alpha"
    |                                                          Contract                                                           |                  Address                   |
    |:---------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------:|
    |      [ECRECOVER](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#verify-signatures-with-ecrecover)      | 0x0000000000000000000000000000000000000001 |
    |              [SHA256](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#hashing-with-sha256)              | 0x0000000000000000000000000000000000000002 |
    |          [RIPEMD160](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#hashing-with-ripemd-160)           | 0x0000000000000000000000000000000000000003 |
    |            [Identity](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#the-identity-function)            | 0x0000000000000000000000000000000000000004 |
    |    [Modular Exponentiation](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#modular-exponentiation)     | 0x0000000000000000000000000000000000000005 |
    |                  [BN128Add](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#bn128add)                   | 0x0000000000000000000000000000000000000006 |
    |                  [BN128Mul](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#bn128mul)                   | 0x0000000000000000000000000000000000000007 |
    |              [BN128Pairing](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#bn128pairing)               | 0x0000000000000000000000000000000000000008 |
    | [Blake2](https://polkadot-evm.github.io/frontier/rustdocs/pallet_evm_precompile_blake2/struct.Blake2F.html) | 0x0000000000000000000000000000000000000009 |
    |                 [P256Verify](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7212.md)                 | 0x0000000000000000000000000000000000000100 |
### Non-Moonbeam Specific nor Ethereum Precompiles {: #non-moonbeam-specific-nor-ethereum-precompiles }

=== "Moonbeam"
    |                                                                      Contract                                                                      |                  Address                   |
    |:--------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------:|
    |                    [SHA3FIPS256](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#hashing-with-sha3fips256)                     | 0x0000000000000000000000000000000000000400 |
    |                                                                 Dispatch [Removed]                                                                 | 0x0000000000000000000000000000000000000401 |
    | [ECRecoverPublicKey](https://polkadot-evm.github.io/frontier/rustdocs/pallet_evm_precompile_simple/struct.ECRecoverPublicKey.html) | 0x0000000000000000000000000000000000000402 |

=== "Moonriver"
    |                                                                      Contract                                                                      |                  Address                   |
    |:--------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------:|
    |                    [SHA3FIPS256](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#hashing-with-sha3fips256)                     | 0x0000000000000000000000000000000000000400 |
    |                                                                 Dispatch [Removed]                                                                 | 0x0000000000000000000000000000000000000401 |
    | [ECRecoverPublicKey](https://polkadot-evm.github.io/frontier/rustdocs/pallet_evm_precompile_simple/struct.ECRecoverPublicKey.html) | 0x0000000000000000000000000000000000000402 |

=== "Moonbase Alpha"
    |                                                                           Contract                                                                            |                  Address                   |
    |:-------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------:|
    |                          [SHA3FIPS256](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#hashing-with-sha3fips256)                          | 0x0000000000000000000000000000000000000400 |
    |                                                                      Dispatch [Removed]                                                                       | 0x0000000000000000000000000000000000000401 |
    |      [ECRecoverPublicKey](https://polkadot-evm.github.io/frontier/rustdocs/pallet_evm_precompile_simple/struct.ECRecoverPublicKey.html)       | 0x0000000000000000000000000000000000000402 |
### Moonbeam Specific Precompiles {: #moonbeam-specific-precompiles }

=== "Moonbeam"
    |                                                                                        Contract                                                                                        |                               Address                               |
    |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
    |                  [Parachain Staking](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/parachain-staking/StakingInterface.sol)                  |              0x0000000000000000000000000000000000000800              |
    |                         [ERC-20 Interface](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/balances-erc20/ERC20.sol)                          |               0x0000000000000000000000000000000000000802               |
    |                                                                      Democracy [Removed]                                                                      |             0x0000000000000000000000000000000000000803             |
    |                                [X-Tokens](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xtokens/Xtokens.sol)                                |              0x0000000000000000000000000000000000000804              |
    |                        [Relay Encoder](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/relay-encoder/RelayEncoder.sol)                        |           0x0000000000000000000000000000000000000805           |
    |                [XCM Transactor V1](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v1/XcmTransactorV1.sol)                 |         0x0000000000000000000000000000000000000806         |
    |                  [Author Mapping](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/author-mapping/AuthorMappingInterface.sol)                  |          0x0000000000000000000000000000000000000807           |
    |                                   [Batch](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/batch/Batch.sol)                                    |               0x0000000000000000000000000000000000000808               |
    |                            [Randomness](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/randomness/Randomness.sol)                            |            0x0000000000000000000000000000000000000809             |
    |                           [Call Permit](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/call-permit/CallPermit.sol)                           |            0x000000000000000000000000000000000000080a            |
    |                                   [Proxy](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/proxy/Proxy.sol)                                    |               0x000000000000000000000000000000000000080b               |
    |                            [XCM Utilities](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-utils/XcmUtils.sol)                            |             0x000000000000000000000000000000000000080C             |
    |                [XCM Transactor V2](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v2/XcmTransactorV2.sol)                 |         0x000000000000000000000000000000000000080d         |
    |                   [Council Collective [Removed]](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)                   |        0x000000000000000000000000000000000000080e         |
    |             [Technical Committee Collective [Removed]](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)             |     0x000000000000000000000000000000000000080f     |
    |                   [Treasury Council Collective](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)                    |        0x0000000000000000000000000000000000000810        |
    |                             [Referenda](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/referenda/Referenda.sol)                              |             0x0000000000000000000000000000000000000811             |
    |                  [Conviction Voting](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/conviction-voting/ConvictionVoting.sol)                  |         0x0000000000000000000000000000000000000812         |
    |                               [Preimage](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/preimage/Preimage.sol)                               |             0x0000000000000000000000000000000000000813              |
    |                      [OpenGov Tech Committee](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)                      | 0x0000000000000000000000000000000000000814 |
    |               [Precompile Registry](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/precompile-registry/PrecompileRegistry.sol)               |             0x0000000000000000000000000000000000000815              |
    |                                      [GMP](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/gmp/Gmp.sol)                                       |                0x0000000000000000000000000000000000000816                |
    |                [XCM Transactor V3](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v3/XcmTransactorV3.sol)                 |         0x0000000000000000000000000000000000000817         |
    |                               [XCM interface](https://github.com/Moonsong-Labs/moonkit/blob/main/precompiles/pallet-xcm/XcmInterface.sol)                               |             0x000000000000000000000000000000000000081A              |
    |                               [Identity](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/identity/Identity.sol)                               |             0x0000000000000000000000000000000000000818              |
    

=== "Moonriver"
    |                                                                           Contract                                                                            |                               Address                                |
    |:-------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
    |      [Parachain Staking](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/parachain-staking/StakingInterface.sol)      |              0x0000000000000000000000000000000000000800              |
    |             [ERC-20 Interface](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/balances-erc20/ERC20.sol)              |               0x0000000000000000000000000000000000000802               |
    |                                                                     Democracy [Disabled]                                                                      |             0x0000000000000000000000000000000000000803             |
    |                    [X-Tokens](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xtokens/Xtokens.sol)                    |              0x0000000000000000000000000000000000000804              |
    |            [Relay Encoder](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/relay-encoder/RelayEncoder.sol)            |           0x0000000000000000000000000000000000000805           |
    |    [XCM Transactor V1](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v1/XcmTransactorV1.sol)     |         0x0000000000000000000000000000000000000806         |
    |      [Author Mapping](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/author-mapping/AuthorMappingInterface.sol)      |          0x0000000000000000000000000000000000000807           |
    |                       [Batch](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/batch/Batch.sol)                        |               0x0000000000000000000000000000000000000808               |
    |                [Randomness](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/randomness/Randomness.sol)                |            0x0000000000000000000000000000000000000809             |
    |               [Call Permit](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/call-permit/CallPermit.sol)               |            0x000000000000000000000000000000000000080a            |
    |                       [Proxy](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/proxy/Proxy.sol)                        |               0x000000000000000000000000000000000000080b               |
    |                [XCM Utilities](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-utils/XcmUtils.sol)                |             0x000000000000000000000000000000000000080C             |
    |    [XCM Transactor V2](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v2/XcmTransactorV2.sol)     |         0x000000000000000000000000000000000000080d         |
    |       [Council Collective [Removed]](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)       |        0x000000000000000000000000000000000000080e         |
    | [Technical Committee Collective [Removed]](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol) |     0x000000000000000000000000000000000000080f     |
    |       [Treasury Council Collective](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)        |        0x0000000000000000000000000000000000000810        |
    |                 [Referenda](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/referenda/Referenda.sol)                  |             0x0000000000000000000000000000000000000811             |
    |      [Conviction Voting](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/conviction-voting/ConvictionVoting.sol)      |         0x0000000000000000000000000000000000000812         |
    |                   [Preimage](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/preimage/Preimage.sol)                   |             0x0000000000000000000000000000000000000813              |
    |          [OpenGov Tech Committee](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)          | 0x0000000000000000000000000000000000000814 |
    |   [Precompile Registry](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/precompile-registry/PrecompileRegistry.sol)   |             0x0000000000000000000000000000000000000815              |
    |                          [GMP](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/gmp/Gmp.sol)                           |                0x0000000000000000000000000000000000000816                |
    |    [XCM Transactor V3](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v3/XcmTransactorV3.sol)     |         0x0000000000000000000000000000000000000817         |
    |                               [XCM interface](https://github.com/Moonsong-Labs/moonkit/blob/main/precompiles/pallet-xcm/XcmInterface.sol)                               |             0x000000000000000000000000000000000000081A              |
    |                   [Identity](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/identity/Identity.sol)                   |             0x0000000000000000000000000000000000000818              |

=== "Moonbase Alpha"
    |                                                                            Contract                                                                            |                               Address                               |
    |:--------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
    |      [Parachain Staking](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/parachain-staking/StakingInterface.sol)      |              0x0000000000000000000000000000000000000800              |
    |             [ERC-20 Interface](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/balances-erc20/ERC20.sol)              |               0x0000000000000000000000000000000000000802               |
    |                                                                      Democracy [Removed]                                                                       |             0x0000000000000000000000000000000000000803             |
    |                    [X-Tokens](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xtokens/Xtokens.sol)                    |              0x0000000000000000000000000000000000000804              |
    |            [Relay Encoder](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/relay-encoder/RelayEncoder.sol)            |           0x0000000000000000000000000000000000000805           |
    |    [XCM Transactor V1](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v1/XcmTransactorV1.sol)     |         0x0000000000000000000000000000000000000806         |
    |      [Author Mapping](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/author-mapping/AuthorMappingInterface.sol)      |          0x0000000000000000000000000000000000000807           |
    |                       [Batch](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/batch/Batch.sol)                        |               0x0000000000000000000000000000000000000808               |
    |                [Randomness](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/randomness/Randomness.sol)                |            0x0000000000000000000000000000000000000809             |
    |               [Call Permit](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/call-permit/CallPermit.sol)               |            0x000000000000000000000000000000000000080a            |
    |                       [Proxy](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/proxy/Proxy.sol)                        |               0x000000000000000000000000000000000000080b               |
    |                [XCM Utilities](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-utils/XcmUtils.sol)                |             0x000000000000000000000000000000000000080C             |
    |    [XCM Transactor V2](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v2/XcmTransactorV2.sol)     |         0x000000000000000000000000000000000000080d         |
    |       [Council Collective [Removed]](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)       |        0x000000000000000000000000000000000000080e         |
    | [Technical Committee Collective [Removed]](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol) |     0x000000000000000000000000000000000000080f     |
    |       [Treasury Council Collective](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)        |        0x0000000000000000000000000000000000000810        |
    |                 [Referenda](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/referenda/Referenda.sol)                  |             0x0000000000000000000000000000000000000811             |
    |      [Conviction Voting](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/conviction-voting/ConvictionVoting.sol)      |         0x0000000000000000000000000000000000000812         |
    |                   [Preimage](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/preimage/Preimage.sol)                   |             0x0000000000000000000000000000000000000813              |
    |          [OpenGov Tech Committee](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/collective/Collective.sol)          | 0x0000000000000000000000000000000000000814 |
    |   [Precompile Registry](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/precompile-registry/PrecompileRegistry.sol)   |             0x0000000000000000000000000000000000000815              |
    |                          [GMP](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/gmp/Gmp.sol)                           |                0x0000000000000000000000000000000000000816                |
    |    [XCM Transactor V3](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/xcm-transactor/src/v3/XcmTransactorV3.sol)     |         0x0000000000000000000000000000000000000817         |
    |                               [XCM Interface](https://github.com/Moonsong-Labs/moonkit/blob/main/precompiles/pallet-xcm/XcmInterface.sol)                               |             0x000000000000000000000000000000000000081A              |
    |                   [Identity](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/identity/Identity.sol)                   |             0x0000000000000000000000000000000000000818              |
