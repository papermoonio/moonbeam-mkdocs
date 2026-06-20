---
title: Sovereign Accounts and Reserve-Backed Transfers
description: Discover how sovereign accounts work on Moonbeam, how to calculate them, and their role in cross-chain asset transfers.
categories:
- XCM
url: https://docs.moonbeam.network/builders/interoperability/xcm/core-concepts/sovereign-accounts/
word_count: 539
token_estimate: 824
version_hash: sha256:3b5043d7164ec7bbcd41c77d5e01c4758b6289fc87dd213e476464d10e44cb2e
last_updated: '2026-05-21T21:21:53+00:00'
---

# Overview of Sovereign Accounts

## Introduction {: #introduction }

In Polkadot-based ecosystems, a sovereign account is a unique, keyless account controlled by a blockchain’s runtime through XCM rather than an individual or organization. These accounts are used to store assets when transferring tokens cross-chain. For example, if you send a reserve tokens transfer from a parachain to Moonbeam, the originating parachain locks those tokens in Moonbeam’s sovereign account on the source chain, while a wrapped representation of those tokens is minted on Moonbeam.

Sovereign accounts play a central role in [reserve-backed transfers](https://wiki.polkadot.com/learn/learn-xcm-usecases/#reserve-asset-transfer), where one chain (the “reserve”) holds the real assets and other chains hold derivative tokens. When tokens move across chains, the reserve (or origin) chain locks or unlocks the underlying asset, and derivative tokens are minted or burned on the destination chain.

## Calculating a Parachain Sovereign Account {: #calculating-sovereign }

You can calculate a parachain’s sovereign account on a given relay chain using the [xcm-tools](https://github.com/Moonsong-Labs/xcm-tools) repository. This is especially useful when you need to verify where underlying tokens are locked or to fund a parachain’s sovereign account directly.

1. Clone or navigate to the [xcm-tools repository](https://github.com/Moonsong-Labs/xcm-tools)
2. Use the `calculate-sovereign-account` script, specifying the **Parachain ID** with the `--p` flag and the relay chain with the `--r` flag (default is `polkadot`; other accepted values are `kusama` or `moonbase`)

The parachain ID you need can be found on the respective relay chain’s [Polkadot.js Apps **Parachains** page](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Frelay.api.moonbase.moonbeam.network#/parachains). The **Parachains** page can be accessed under the **Network** dropdown.

For example, to calculate the sovereign account address for parachain `1000` on the Moonbase Alpha testnet:

```bash
yarn calculate-sovereign-account --p 1000 --r moonbase
```

Running the script will generate output like the following:

<div id="termynal" data-termynal>
<span data-ty="input"><span class="file-path">yarn calculate-sovereign-account --p 1000 --r moonbase</span>
<span data-ty>yarn run v1.22.22</span>
<span data-ty>$ ts-node 'scripts/calculate-sovereign-account.ts' --p 1000 --r moonbase</span>
<span data-ty>Sovereign Account Address on Relay: 0x70617261e8030000000000000000000000000000000000000000000000000000</span>
<span data-ty>Sovereign Account Address on other Parachains (Generic): 0x7369626ce8030000000000000000000000000000000000000000000000000000</span>
<span data-ty>Sovereign Account Address on Moonbase Alpha: 0x7369626ce8030000000000000000000000000000</span>
</div>
The relay address is how the Polkadot or Kusama relay chain references the sovereign account. Generic parachain address is typically used for referencing this parachain’s sovereign account from other parachains. The Moonbase Alpha address is the corresponding sovereign account in the H160 EVM address format used by Moonbase Alpha.

## Learn More {: #learn-more }

Sovereign accounts form the backbone of reserve-backed transfers, enabling safe custody of assets for minting wrapped tokens across Polkadot’s ecosystem. By combining sovereign accounts with the XCM framework, parachains can interoperate seamlessly—locking and unlocking assets in a transparent, trust-minimized way. For more information about how sovereign accounts facilitate cross-chain transfers with XCM, be sure to check out the [Send XC-20s section](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/overview/).
