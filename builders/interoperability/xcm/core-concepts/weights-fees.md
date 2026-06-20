---
title: XCM Execution Fees
description: Learn about the XCM instructions involved in handling XCM execution fee payments and how to calculate fees on Polkadot, Kusama, and Moonbeam-based networks.
categories:
- XCM
url: https://docs.moonbeam.network/builders/interoperability/xcm/core-concepts/weights-fees/
word_count: 3815
token_estimate: 7072
version_hash: sha256:48cdf07f0974ea0c76a273cc9e1caf90baa3de0096386c8a27983e965752f871
last_updated: '2026-05-21T21:21:53+00:00'
---

# XCM Fees on Moonbeam

## Introduction {: #introduction}

XCM aims to be a language that communicates ideas between consensus systems. Sending an XCM message consists of a series of instructions that are executed in both the origin and the destination chains. The combination of XCM instructions results in actions such as token transfers. In order to process and execute each XCM instruction, there are typically associated fees that must be paid.

However, XCM is designed to be general, extensible, and efficient so that it remains valuable and future-proof throughout a growing ecosystem. As such, the generality applies to concepts including payments of fees for XCM execution. In Ethereum, fees are baked into the transaction protocol, whereas in the Polkadot ecosystem, each chain has the flexibility to define how XCM fees are handled.

This guide will cover aspects of fee payment, such as who is responsible for paying XCM execution fees, how it is paid for, and how the fees are calculated on Moonbeam.

!!! note
    **The following information is provided for general information purposes only.** The weight and extrinsic base cost might have changed since the time of writing. Please ensure you check the actual values, and never use the following information for production apps.

## Payment of Fees {: #payment-of-fees }

Generally speaking, the fee payment process can be described as follows:

1. Some assets need to be provided
2. The exchange of assets for computing time (or weight) must be negotiated
3. The XCM operations will be performed as instructed, with the provided weight limit or funds available for execution

Each chain can configure what happens with the XCM fees and in which tokens they can be paid (either the native reserve token or an external one). For example:

- **Polkadot and Kusama** - the fees are paid in DOT or KSM (respectively) and given to the validator of the block
- **Moonbeam and Moonriver** - the XCM execution fees can be paid in the reserve asset (GLMR or MOVR, respectively), but also in assets originated in other chains if they are registered as an [XCM execution asset](/moonbeam-mkdocs/builders/interoperability/xcm/xc-registrationassets/). When XCM execution (token transfers or remote execution) is paid in the native chain reserve asset (GLMR or MOVR), 100% is burned. When XCM execution is paid in a foreign asset, the fee is sent to the Treasury

Consider the following scenario: Alice has some DOT on Polkadot, and she wants to transfer it to Alith on Moonbeam. She sends an XCM message with a set of XCM instructions that will retrieve a given amount of DOT from her account on Polkadot and mint them as xcDOT into Alith's account. Part of the instructions are executed on Polkadot, and the other part is executed on Moonbeam.

How does Alice pay Moonbeam to execute these instructions and fulfill her request? Her request is fulfilled through a series of XCM instructions that are included in the XCM message, which enables her to buy execution time minus any related XCM execution fees. The execution time is used to issue and transfer xcDOT, a representation of DOT on Moonbeam. This means that when Alice sends some DOT to Alith's account on Moonbeam, she'll receive a 1:1 representation of her DOT as xcDOT minus any XCM execution fees. Note that in this scenario, XCM execution fees are paid in xcDOT and sent to the treasury.

The exact process for Alice's transfer is as follows:

1. Assets are sent to an account on Polkadot that is owned by Moonbeam, known as the Sovereign account. After the assets are received, an XCM message is sent to Moonbeam
2. The XCM message in Moonbeam will:
    1. Mint the corresponding asset representation
    2. Buy the corresponding execution time
    3. Use that execution time to deposit the representation (minus fees) to the destination account

### XCM Instructions {: #xcm-instructions }

An XCM message is comprised of a series of XCM instructions. As a result, different combinations of XCM instructions result in different actions. For example, to move DOT to Moonbeam, the following XCM instructions are used:

When DOT is transferred from Polkadot to Moonbeam, the following XCM instructions are executed in sequence:

1. [`TransferReserveAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#transfer-reserve-asset) - executes on Polkadot, moving the DOT from the sender and depositing it into Moonbeam’s Sovereign account on Polkadot

2. [`ReserveAssetDeposited`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#reserve-asset-deposited) - executes on Moonbeam, minting the corresponding ERC-20 representation of DOT (xcDOT) on Moonbeam

3. [`ClearOrigin`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#clear-origin) - executes on Moonbeam, clearing any origin data—previously set to Polkadot’s Sovereign account

4. [`BuyExecution`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#buy-execution) - executes on Moonbeam, determining the execution fees. Here, a portion of the newly minted xcDOT is used to pay the cost of XCM

5. [`DepositAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#deposit-asset) - executes on Moonbeam, delivering the xcDOT to the intended recipient’s account on Moonbeam
To check how the instructions for an XCM message are built to transfer self-reserve assets to a target chain, such as DOT to Moonbeam, you can refer to the [X-Tokens Open Runtime Module Library](https://github.com/moonbeam-foundation/open-runtime-module-library/blob/master/xtokens/src/lib.rs) repository (as an example). You'll want to take a look at the [`transfer_self_reserve_asset`](https://github.com/moonbeam-foundation/open-runtime-module-library/blob/master/xtokens/src/lib.rs#L699) function. You'll notice it calls `TransferReserveAsset` and passes in `assets`, `dest`, and `xcm` as parameters. In particular, the `xcm` parameter includes the `BuyExecution` and `DepositAsset` instructions. If you then head over to the Polkadot GitHub repository, you can find the [`TransferReserveAsset` instruction](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.17.1/polkadot/xcm/xcm-executor/src/lib.rs#L671). The XCM message is constructed by combining the `ReserveAssetDeposited` and `ClearOrigin` instructions with the `xcm` parameter, which as mentioned includes the `BuyExecution` and `DepositAsset` instructions.

In scenarios where you want to move an asset back to its reserve chain, such as sending xcDOT from Moonbeam to Polkadot, Moonbeam uses the following set of XCM instructions:

1. [`WithdrawAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#withdraw-asset) – executes on Moonbeam, taking the specified token (xcDOT) from the sender

2. [`InitiateReserveWithdraw`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#initiate-reserve-withdraw) – executes on Moonbeam, which, burns the token on Moonbeam (removing the wrapped representation), and sends an XCM message to Polkadot, indicating the tokens should be released there 

3. [`WithdrawAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#withdraw-asset) – executes on Polkadot, removing the tokens from Moonbeam’s Sovereign account on Polkadot

4. [`ClearOrigin`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#clear-origin) – gets executed on Polkadot. Clears any origin data (e.g., the Sovereign account on Moonbeam)

5. [`BuyExecution`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#buy-execution) – Polkadot determines the execution fees and uses part of the DOT being transferred to pay for them

6. [`DepositAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#deposit-asset) – finally, the native DOT tokens are deposited into the specified Polkadot account
To check how the instructions for an XCM message are built to transfer reserve assets to a target chain, such as xcDOT to Polkadot, you can refer to the [X-Tokens Open Runtime Module Library](https://github.com/moonbeam-foundation/open-runtime-module-library/tree/master/xtokens) repository. You'll want to take a look at the [`transfer_to_reserve`](https://github.com/moonbeam-foundation/open-runtime-module-library/blob/master/xtokens/src/lib.rs#L719) function. You'll notice that it calls `WithdrawAsset`, then `InitiateReserveWithdraw` and passes in `assets`, `dest`, and `xcm` as parameters. In particular, the `xcm` parameter includes the `BuyExecution` and `DepositAsset` instructions. If you then head over to the Polkadot GitHub repository, you can find the [`InitiateReserveWithdraw` instruction](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.17.1/polkadot/xcm/xcm-executor/src/lib.rs#L903). The XCM message is constructed by combining the `WithdrawAsset` and `ClearOrigin` instructions with the `xcm` parameter, which as mentioned includes the `BuyExecution` and `DepositAsset` instructions.

## Relay Chain XCM Fee Calculation  {: #rel-chain-xcm-fee-calc }

Substrate has introduced a weight system that determines how heavy or, in other words, how expensive from a computational cost perspective an extrinsic is. One unit of weight is defined as one picosecond of execution time. When it comes to paying fees, users will pay a transaction fee based on the weight of the call that is being made, in addition to factors such as network congestion.

The following sections will break down how to calculate XCM fees for Polkadot and Kusama. It's important to note that Kusama, in particular, uses benchmarked data to determine the total weight costs for XCM instructions and that some XCM instructions might include database reads and writes, which add weight to the call.

There are two databases available in Polkadot and Kusama: RocksDB (which is the default) and ParityDB, both of which have their own associated weight costs for each network.

### Polkadot {: #polkadot }

The total weight costs on Polkadot take into consideration database reads and writes in addition to the weight required for a given instruction. Polkadot uses benchmarked weights for instructions, and database read-and-write operations. The breakdown of weight costs for the database operations can be found on the respective repository files for [RocksDB (default)](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/polkadot/constants/src/weights/rocksdb_weights.rs) and [ParityDB](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/polkadot/constants/src/weights/paritydb_weights.rs).  

Now that you are aware of the weight costs for database reads and writes on Polkadot, you can calculate the weight cost for a given instruction using the base weight for instructions.

On Polkadot, the benchmarked base weights are broken up into two categories: fungible and generic. Fungible weights are for XCM instructions that involve moving assets, and generic weights are for everything else. You can view the current weights for [fungible assets](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/polkadot/src/weights/xcm/pallet_xcm_benchmarks_fungible.rs#L46) and [generic assets](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/polkadot/src/weights/xcm/pallet_xcm_benchmarks_generic.rs#L46) directly in the Polkadot Runtime code.

With the instruction weight cost established, you can calculate the cost of each instruction in DOT.

In Polkadot, the [`ExtrinsicBaseWeight`](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/polkadot/constants/src/weights/extrinsic_weights.rs#L56) is set to `126,045,000` which is [mapped to 1/10th](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/polkadot/constants/src/lib.rs#L92) of a cent. Where 1 cent is `10^10 / 100`.

Therefore, to calculate the cost of executing an XCM instruction, you can use the following formula:

```text
XCM-DOT-Cost = XCMInstrWeight * DOTWeightToFeeCoefficient
```

Where `DOTWeightToFeeCoefficient` is a constant (map to 1 cent), and can be calculated as:

```text
DOTWeightToFeeCoefficient = 10^10 / ( 10 * 100 * DOTExtrinsicBaseWeight )
```

Now, you can begin to calculate the final fee in DOT, using `DOTWeightToFeeCoefficient` as a constant and `TotalWeight` as the variable:

```text
XCM-Planck-DOT-Cost = TotalWeight * DOTWeightToFeeCoefficient
XCM-DOT-Cost = XCM-Planck-DOT-Cost / DOTDecimalConversion
```

### Kusama {: #kusama }

The total weight costs on Kusama take into consideration database reads and writes in addition to the weight required for a given instruction. The breakdown of weight costs for the database operations can be found on the respective repository files for [RocksDB (default)](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/kusama/constants/src/weights/rocksdb_weights.rs) and [ParityDB](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/kusama/constants/src/weights/paritydb_weights.rs). 

On Kusama, the benchmarked base weights are broken up into two categories: fungible and generic. Fungible weights are for XCM instructions that involve moving assets, and generic weights are for everything else. You can view the current weights for [fungible assets](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/kusama/src/weights/xcm/pallet_xcm_benchmarks_fungible.rs#L46) and [generic assets](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/kusama/src/weights/xcm/pallet_xcm_benchmarks_generic.rs#L46) directly in the Kusama Runtime code.

With the instruction weight cost established, you can calculate the cost of the instruction in KSM with the [`ExtrinsicBaseWeight`](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/kusama/constants/src/weights/extrinsic_weights.rs#L56) and the [weight fee mapping](https://github.com/polkadot-fellows/runtimes/blob/v1.6.1/relay/kusama/constants/src/lib.rs#L90).

To calculate the cost of executing an XCM instruction, you can use the following formula:

```text
XCM-KSM-Cost = XCMInstrWeight * KSMWeightToFeeCoefficient
```

Where `KSMWeightToFeeCoefficient` is a constant (map to 1 cent), and can be calculated as:

```text
KSMWeightToFeeCoefficient = 10^12 / ( 10 * 3000 * KSMExtrinsicBaseWeight )
```

Now, you can begin to calculate the final fee in KSM, using `KSMWeightToFeeCoefficient` as a constant and `TotalWeight` as the variable:

```text
XCM-Planck-KSM-Cost = TotalWeight * KSMWeightToFeeCoefficient
XCM-KSM-Cost = XCM-Planck-KSM-Cost / KSMDecimalConversion
```

## Moonbeam-based Networks XCM Fee Calculation  {: #moonbeam-xcm-fee-calc }

Substrate has introduced a weight system that determines how heavy or, in other words, how expensive an extrinsic is from a computational cost perspective. One unit of weight is defined as one picosecond of execution time. When it comes to paying fees, users will pay a transaction fee based on the weight of the call being made, and each parachain can decide how to convert weight to fee. For example, this may account for additional costs related to transaction size and storage.

For all Moonbeam-based networks, both the generic and fungible XCM instructions are benchmarked. The total weight cost of each XCM instruction considers the number of database reads and writes in addition to the base execution time determined by the benchmark. The Polkadot SDK has a breakdown of the relevant [RocksDB database weights](https://github.com/paritytech/polkadot-sdk/blob/polkadot-v1.17.1/substrate/frame/support/src/weights/rocksdb_weights.rs#L27-L28).

Now you can calculate the weight cost for both fungible and generic XCM instructions using the base weight for instruction and the extra database reads and writes if applicable.

For example, the `WithdrawAsset` instruction is part of the fungible XCM instructions. Its benchmarked weight can be found in the [Moonbeam runtime source code](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4303/runtime/moonbeam/src/weights/xcm/pallet_xcm_benchmarks_fungible.rs) and includes a base execution time plus the cost of database reads and writes. The exception is when transferring local XC-20s, where the total weight cost for the `WithdrawAsset` instruction is based on converting Ethereum gas to Substrate weight.

The `BuyExecution` instruction is generic and therefore has a predefined benchmarked weight. You can view its current base weight in the [Moonbeam runtime source code](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4303/runtime/moonbeam/src/weights/xcm/pallet_xcm_benchmarks_generic.rs#L101-L103). In addition to the base weight, the instruction performs 14 database reads and 4 writes, which are added to calculate the total weight.


You can find all the weight values for all the XCM instructions in the following table, which apply to all Moonbeam-based networks:

|                                                                                     Benchmarked Generic Instructions                                                                                     |                                                                                    Benchmarked Fungible Instructions                                                                                    |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| [Generic XCM Instructions](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4303/runtime/moonbeam/src/weights/xcm/pallet_xcm_benchmarks_generic.rs) | [Fungible XCM Instructions](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4303/runtime/moonbeam/src/weights/xcm/pallet_xcm_benchmarks_fungible.rs) |

The following sections will break down how to calculate XCM fees for Moonbeam-based networks. There are two main scenarios:

 - Fees paid in the reserve token (native tokens like GLMR, MOVR, or DEV)
 - Fees paid in external assets (XC-20s)

### Fee Calculation for Reserve Assets {: #moonbeam-reserve-assets }

For each XCM instruction, the weight units are converted to balance units as part of the fee calculation. The amount of Wei per weight unit for each of the Moonbeam-based networks is as follows:

|                                                                                                  Moonbeam                                                                                                   |                                                                                                   Moonriver                                                                                                    |                                                                                               Moonbase Alpha                                                                                                |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| [1,250,000](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4303/runtime/moonbeam/src/lib.rs#L169) | [12,500](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4303/runtime/moonriver/src/lib.rs#L172) | [12,500](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4302/runtime/moonbase/src/lib.rs#L164) |

This means that on Moonbeam, for example, the formula to calculate the cost of one XCM instruction in the reserve asset is as follows:

```text
XCM-Wei-Cost = XCMInstrWeight * WeiPerWeight
XCM-GLMR-Cost = XCM-Wei-Cost / 10^18
```

Therefore, taking a single fungible instruction as an example, the calculation is:

```text
XCM-Wei-Cost = 200000000 * 1250000
XCM-GLMR-Cost = 250000000000000 / 10^18
```

The total cost is `0.00025 GLMR` for an XCM instruction on Moonbeam.

### Fee Calculation for External Assets {: #fee-calc-external-assets }

Moonbeam charges fees for external assets based on the weight of the call. Weight is a struct that contains two fields, `refTime` and `proofSize`. `refTime` refers to the amount of computational time that can be used for execution. `proofSize` refers to the size of the PoV (Proof of Validity) of the Moonbeam block that gets submitted to the Polkadot Relay Chain for validation. Since both `refTime` and `proofSize` are integral components of determining a weight, it is impossible to obtain an accurate weight value with just one of these values.

You can query the `refTime` and `proofSize` of an XCM instruction with the [`queryXcmWeight` method of the `xcmPaymentApi`](#query-xcm-weight). You can do this [programmatically](#query-xcm-weight) or by visiting the [Runtime Calls tab of Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fmoonbeam.api.onfinality.io%2Fpublic-ws#/runtime). The `queryXcmWeight` method takes an XCM version and instruction has a parameter and returns the corresponding `refTime` and `proofSize` values.

#### Weight to Gas Mapping {: #weight-to-gas-mapping }

For calls that are derived from EVM operations, such as the `DepositAsset` instruction which relies on the EVM operation `MintInto`, you can calculate their respective weight values by multiplying the gas limit by weight multipliers. For `refTime`, you'll need to multiply the gas limit by `25000` and for `proofSize` you'll need to multiply the gas limit by `8`.  A chart is included below for convenience. 

| Weight Type |                  Multiplier Value                   |
|:-----------:|:---------------------------------------------------:|
|  Ref Time   |  25,000   |
| Proof Size  | 8 |

To determine the total weight for Alice's transfer of DOT to Moonbeam, you'll need the weight for each of the four XCM instructions required for the transfer. Note that while the first three instructions have specific `refTime` and `proofSize` values corresponding to these instructions that can be retrieved via [`queryXcmWeight` method of the `xcmPaymentApi`](#query-xcm-weight), `DepositAsset` relies on the EVM operation [`MintInto`](https://github.com/moonbeam-foundation/moonbeam/blob/runtime-4303/pallets/moonbeam-foreign-assets/src/evm.rs#L40) and a `WeightPerGas` conversion of `25,000` per gas. The `refTime` of `DepositAsset` can thus be calculated as: 

```text
155000 gas * 25000 weight per gas = 3875000000
```

And the `proofSize` of `DepositAsset` can be calculated as:

```text
155000 gas * 8 weight per gas = 1240000
```

### Weight to Asset Fee Conversion {: #weight-to-asset-fee-conversion} 

Once you have the sum of the `refTime` and `proofSize` values, you can easily retrieve the required commensurate fee amount. The [`queryWeightToAssetFee` method of the `xcmPaymentApi`](#weight-to-asset-fee-conversion) takes a `refTime`, `proofSize`, and asset multilocation as parameters and returns the commensurate fee. By providing the amounts obtained above of `4,428,242,000` `refTime` and `1,259,056` `proofSize`, and the asset multilocation for DOT, we get a fee amount of `88,920,522` Plank, which is the smallest unit in Polkadot. We can convert this to DOT by dividing by `10^10` which gets us a DOT fee amount of `0.008892` DOT. 

## XCM Payment API Expanded Examples {: #xcm-payment-api-exanded-examples }

The XCM Payment API methods provide various helpful ways to calculate fees, evaluate acceptable fee payment currencies, and more. Remember that in addition to accessing this via API, you can also interact with the XCM Payment API via the [Runtime Calls tab of Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fmoonbeam.api.onfinality.io%2Fpublic-ws#/runtime).

### Query Acceptable Fee Payment Assets {: #query-acceptable-fee-payment-assets }

This function takes the XCM Version as a parameter and returns a list of acceptable fee assets in multilocation form. 

```javascript
const allowedAssets =
  await api.call.xcmPaymentApi.queryAcceptablePaymentAssets(3);
console.log(allowedAssets);
```

??? code "View the complete script"

    ```js
    import { ApiPromise, WsProvider } from '@polkadot/api';

    const main = async () => {
      // Construct API provider
      const wsProvider = new WsProvider('INSERT_WSS_ENDPOINT');
      const api = await ApiPromise.create({ provider: wsProvider });

      const allowedAssets =
        await api.call.xcmPaymentApi.queryAcceptablePaymentAssets(4);
      console.log(allowedAssets);

      // Disconnect the API
      await api.disconnect();
    };

    main();
    ```

### Weight to Asset Fee Conversion {: #weight-to-asset-fee-conversion }

This method converts a weight into a fee for the specified asset. It takes as parameters a weight and an asset multilocation and returns the respective fee amount.

```javascript
const fee = await api.call.xcmPaymentApi.queryWeightToAssetFee(
  {
    refTime: 10_000_000_000n,
    proofSize: 0n,
  },
  {
    V3: {
      Concrete: { parents: 1, interior: 'Here' },
    },
  }
);

console.log(fee);
```

??? code "View the complete script"

    ```js
    import { ApiPromise, WsProvider } from '@polkadot/api';

    const main = async () => {
      // Construct API provider
      const wsProvider = new WsProvider('INSERT_WSS_ENDPOINT');
      const api = await ApiPromise.create({ provider: wsProvider });

      const fee = await api.call.xcmPaymentApi.queryWeightToAssetFee(
        {
          refTime: 10_000_000_000n,
          proofSize: 0n,
        },
        {
          V3: {
            Concrete: { parents: 1, interior: 'Here' },
          },
        }
      );

      console.log(fee);

      // Disconnect the API
      await api.disconnect();
    };

    main();
    ```

### Query XCM Weight {: #query-xcm-weight}

This method takes an XCM message as a parameter and returns the weight of the message. 

```javascript
const message = { V3: [instr1, instr2] };

const theWeight = await api.call.xcmPaymentApi.queryXcmWeight(message);
console.log(theWeight);
```

??? code "View the complete script"

    ```js
    import { ApiPromise, WsProvider } from '@polkadot/api';

    const main = async () => {
      // Construct API provider
      const wsProvider = new WsProvider('INSERT_WSS_ENDPOINT');
      const api = await ApiPromise.create({ provider: wsProvider });

      const amountToSend = BigInt(1 * 10 ** 12); // Sending 1 token (assuming 12 decimal places)
      const assetMultiLocation = {
        parents: 0,
        interior: { X1: { PalletInstance: 3 } },
      }; // The asset's location (adjust PalletInstance as needed)
      const recipientAccount = '0x1234567890abcdef1234567890abcdef12345678'; // The recipient's account on the destination chain

      // 2. XCM Destination (e.g., Parachain ID 2000)
      const dest = { V3: { parents: 1, interior: { X1: { Parachain: 2000 } } } };

      // 3. XCM Instruction 1: Withdraw the asset from the sender
      const instr1 = {
        WithdrawAsset: [
          {
            id: { Concrete: assetMultiLocation },
            fun: { Fungible: amountToSend },
          },
        ],
      };

      // 4. XCM Instruction 2: Deposit the asset into the recipient's account on the destination chain
      const instr2 = {
        DepositAsset: {
          assets: { Wild: 'All' }, // Sending all withdrawn assets (in this case, 1 token)
          beneficiary: {
            parents: 0,
            interior: { X1: { AccountKey20: { key: recipientAccount } } },
          },
        },
      };

      // 5. Build the XCM Message
      const message = { V3: [instr1, instr2] };

      const theWeight = await api.call.xcmPaymentApi.queryXcmWeight(message);
      console.log(theWeight);

      // Disconnect the API
      await api.disconnect();
    };

    main();
    ```
