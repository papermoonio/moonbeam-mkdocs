---
title: Canonical Contract Addresses on Moonbeam
description: Overview of the canonical contracts available on Moonbeam, Moonriver, & Moonbase Alpha, including common-good contracts and precompiles.
categories:
- Reference
- Precompiles
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/canonical-contracts/
word_count: 1971
token_estimate: 6986
version_hash: sha256:4e5359d541e93f2cc3d2497bc88e6e5fa2bee8dcf3a310412f5beb0281535a07
last_updated: '2026-05-21T21:21:53+00:00'
---

# Canonical Contracts

## Common-good Contracts {: #common-goods-contracts }

The following contracts addresses have been established:

=== "Moonbeam"
    |                                                         Contract                                                         |                  Address                   |
    |:------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------:|
    |      [WGLMR](https://moonbeam.moonscan.io/address/0xAcc15dC74880C9944775448304B263D191c6077F#code)       | 0xAcc15dC74880C9944775448304B263D191c6077F |
    |    [Multicall](https://moonbeam.moonscan.io/address/0x83e3b61886770de2F64AAcaD2724ED4f08F7f36B#code)     | 0x83e3b61886770de2F64AAcaD2724ED4f08F7f36B |
    |    [Multicall2](https://moonbeam.moonscan.io/address/0x6477204E12A7236b9619385ea453F370aD897bb2#code)    | 0x6477204E12A7236b9619385ea453F370aD897bb2 |
    |    [Multicall3](https://moonbeam.moonscan.io/address/0xca11bde05977b3631167028862be2a173976ca11#code)    | 0xcA11bde05977b3631167028862bE2a173976CA11 |
    | [Multisig Factory](https://moonbeam.moonscan.io/address/0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2#code) | 0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2 |
    |                           [EIP-1820](https://eips.ethereum.org/EIPS/eip-1820)                            | 0x1820a4B7618BdE71Dce8cdc73aAB6C95905faD24 |

=== "Moonriver"
    |                                                         Contract                                                          |                  Address                   |
    |:-------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------:|
    |       [WMOVR](https://moonriver.moonscan.io/token/0x98878b06940ae243284ca214f92bb71a2b032b8a#code)        | 0x98878B06940aE243284CA214f92Bb71a2b032B8A |
    |    [Multicall](https://moonriver.moonscan.io/address/0x30f283Cc0284482e9c29dFB143bd483B5C19954b#code)*    | 0x30f283Cc0284482e9c29dFB143bd483B5C19954b |
    |    [Multicall2](https://moonriver.moonscan.io/address/0xaef00a0cf402d9dedd54092d9ca179be6f9e5ce3#code)    | 0xaef00a0cf402d9dedd54092d9ca179be6f9e5ce3 |
    |    [Multicall3](https://moonriver.moonscan.io/address/0xca11bde05977b3631167028862be2a173976ca11#code)    | 0xcA11bde05977b3631167028862bE2a173976CA11 |
    | [Multisig Factory](https://moonriver.moonscan.io/address/0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2#code) | 0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2 |
    |                            [EIP-1820](https://eips.ethereum.org/EIPS/eip-1820)                            | 0x1820a4B7618BdE71Dce8cdc73aAB6C95905faD24 |

    _*Deployed by SushiSwap_

=== "Moonbase Alpha"
    |                                                         Contract                                                         |                  Address                   |
    |:------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------:|
    |       [WDEV](https://moonbase.moonscan.io/address/0xD909178CC99d318e4D46e7E66a972955859670E1#code)       | 0xD909178CC99d318e4D46e7E66a972955859670E1 |
    |    [Multicall](https://moonbase.moonscan.io/address/0x4E2cfca20580747AdBA58cd677A998f8B261Fc21#code)*    | 0x4E2cfca20580747AdBA58cd677A998f8B261Fc21 |
    |    [Multicall2](https://moonbase.moonscan.io/address/0x37084d0158C68128d6Bc3E5db537Be996f7B6979#code)    | 0x37084d0158C68128d6Bc3E5db537Be996f7B6979 |
    |    [Multicall3](https://moonbase.moonscan.io/address/0xca11bde05977b3631167028862be2a173976ca11#code)    | 0xcA11bde05977b3631167028862bE2a173976CA11 |
    | [Multisig Factory](https://moonbase.moonscan.io/address/0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2#code) | 0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2 |
    |                           [EIP-1820](https://eips.ethereum.org/EIPS/eip-1820)                            | 0x1820a4B7618BdE71Dce8cdc73aAB6C95905faD24 |

    _*Deployed in the [UniswapV2 Demo Repo](https://github.com/papermoonio/moonbeam-uniswap/tree/main/uniswap-contracts-moonbeam)_

## Precompiled Contracts {: #precompiled-contracts }

There are a set of precompiled contracts included on Moonbeam, Moonriver, and Moonbase Alpha that are categorized by address and based on the origin network. If you were to convert the precompiled addresses to decimal format, and break them into categories by numeric value, the categories are as follows:

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
### Moonbeam-Specific Precompiles {: #moonbeam-specific-precompiles }

=== "Moonbeam"
    |                                                                           Contract                                                                            |                               Address                               |
    |:-------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
    |      [Parachain Staking](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/parachain-staking/StakingInterface.sol)      |              0x0000000000000000000000000000000000000800              |
    |             [ERC-20 Interface](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/balances-erc20/ERC20.sol)              |               0x0000000000000000000000000000000000000802               |
    |                                                                      Democracy [Removed]                                                                      |             0x0000000000000000000000000000000000000803             |
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
    |                   [Identity](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/identity/Identity.sol)                   |             0x0000000000000000000000000000000000000818              |
    |                  [XCM Interface](https://github.com/Moonsong-Labs/moonkit/blob/main/precompiles/pallet-xcm/XcmInterface.sol)                  |           0x000000000000000000000000000000000000081A           |

=== "Moonriver"
    |                                                                           Contract                                                                            |                               Address                                |
    |:-------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
    |      [Parachain Staking](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/parachain-staking/StakingInterface.sol)      |              0x0000000000000000000000000000000000000800              |
    |             [ERC-20 Interface](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/balances-erc20/ERC20.sol)              |               0x0000000000000000000000000000000000000802               |
    |                                                                      Democracy [Removed]                                                                      |             0x0000000000000000000000000000000000000803             |
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
    |                   [Identity](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/identity/Identity.sol)                   |             0x0000000000000000000000000000000000000818              |
    |                  [XCM Interface](https://github.com/Moonsong-Labs/moonkit/blob/main/precompiles/pallet-xcm/XcmInterface.sol)                  |           0x000000000000000000000000000000000000081A           |

=== "Moonbase Alpha"
    |                                                                           Contract                                                                            |                               Address                               |
    |:-------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
    |      [Parachain Staking](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/parachain-staking/StakingInterface.sol)      |              0x0000000000000000000000000000000000000800              |
    |             [ERC-20 Interface](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/balances-erc20/ERC20.sol)              |               0x0000000000000000000000000000000000000802               |
    |                                                                      Democracy [Removed]                                                                      |             0x0000000000000000000000000000000000000803             |
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
    |                   [Identity](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/identity/Identity.sol)                   |             0x0000000000000000000000000000000000000818              |
    |                  [XCM Interface](https://github.com/Moonsong-Labs/moonkit/blob/main/precompiles/pallet-xcm/XcmInterface.sol)                  |           0x000000000000000000000000000000000000081A           |
