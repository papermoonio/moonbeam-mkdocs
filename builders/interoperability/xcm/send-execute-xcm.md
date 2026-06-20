---
title: Send, Execute and Test XCM Messages
description: Build a custom XCM message, verify its construction and integrity using the XCM Dry Run API, and then execute it locally on Moonbeam to observe the results.
categories:
- XCM
url: https://docs.moonbeam.network/builders/interoperability/xcm/send-execute-xcm/
word_count: 5636
token_estimate: 10230
version_hash: sha256:a5e375c067be69c3e0cb20bd62d032d9fabc1d46a93c238a00a235f42192297e
last_updated: '2026-05-21T21:21:53+00:00'
---

# Send, Execute, and Test XCM Messages

## Introduction {: #introduction }

XCM messages are comprised of a [series of instructions](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/) that are executed by the Cross-Consensus Virtual Machine (XCVM). Combinations of these instructions result in predetermined actions, such as cross-chain token transfers. You can create your own custom XCM messages by combining various XCM instructions.

Pallets such as [Polkadot XCM](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/send-xc20s/xcm-pallet/) and [XCM Transactor](/moonbeam-mkdocs/builders/interoperability/xcm/remote-execution/substrate-calls/xcm-transactor-pallet/) provide functions with a predefined set of XCM instructions to either send [XC-20s](/moonbeam-mkdocs/builders/interoperability/xcm/xc20/overview/) or remotely execute on other chains via XCM. However, to get a better understanding of the results from combining different XCM instructions, you can build and execute custom XCM messages locally on Moonbeam (only available on Moonbase Alpha). You can also send custom XCM messages to another chain (which will start with the [`DescendOrigin`](https://github.com/paritytech/xcm-format#descendorigin) instruction). Nevertheless, for the XCM message to be successfully executed, the target chain needs to be able to understand the instructions.

To execute or send a custom XCM message, you can either use the [Polkadot XCM Pallet](#polkadot-xcm-pallet-interface) directly or through the Ethereum API with the [XCM Utilities Precompile](/moonbeam-mkdocs/builders/interoperability/xcm/xcm-utils/). In this guide, you'll learn how to use both methods to execute and send custom-built XCM messages locally on Moonbase Alpha.

This guide assumes that you are familiar with general XCM concepts, such as [general XCM terminology](/moonbeam-mkdocs/builders/interoperability/xcm/overview/#general-xcm-definitions) and [XCM instructions](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/). For more information, you can check out the [XCM Overview](/moonbeam-mkdocs/builders/interoperability/xcm/overview/) documentation.

## Polkadot XCM Pallet Interface {: #polkadot-xcm-pallet-interface }

### Extrinsics {: #extrinsics }

The Polkadot XCM Pallet includes the following relevant extrinsics (functions):

???+ function "**execute**(message, maxWeight) — **supported on Moonbase Alpha only** - executes a custom XCM message on the source chain"

    === "Parameters"

        - `message` - the SCALE-encoded versioned XCM message to be executed
        - `maxWeight` - the maximum weight allowed to be consumed, which is defined by specifying the:
            - `refTime` - the amount of computational time that can be used for execution
            - `proofSize` - the amount of storage in bytes that can be used

    === "Polkadot.js API Example"
        
        ```js
        import { ApiPromise, WsProvider } from '@polkadot/api';

        const message = { V4: [INSERT_XCM_INSTRUCTIONS] };
        const maxWeight = { refTime: INSERT_REF_TIME, proofSize: INSERT_PROOF_SIZE };

        const main = async () => {
          const api = await ApiPromise.create({
            provider: new WsProvider('INSERT_WSS_ENDPOINT'),
          });
          const tx = api.tx.polkadotXcm.execute(message, maxWeight);
          const txHash = await tx.signAndSend('INSERT_ACCOUNT_OR_KEYRING');
        };

        main();
        ```

???+ function "**send**(dest, message) — **supported on Moonbase Alpha only** - sends a custom XCM message to a destination chain. For the XCM message to be successfully executed, the target chain needs to be able to understand the instructions in the message"

    === "Parameters"

        - `dest` - the XCM versioned multilocation representing a chain in the ecosystem where the XCM message is being sent to (the target chain)
        - `message` - the SCALE-encoded versioned XCM message to be executed

    === "Polkadot.js API Example"
        
        ```js
        import { ApiPromise, WsProvider } from '@polkadot/api';

        const dest = { V4: { parents: INSERT_PARENTS, interior: INSERT_INTERIOR } };
        const message = { V4: [INSERT_XCM_INSTRUCTIONS] };

        const main = async () => {
          const api = await ApiPromise.create({
            provider: new WsProvider('INSERT_WSS_ENDPOINT'),
          });
          const tx = api.tx.polkadotXcm.send(dest, message);
          const txHash = await tx.signAndSend('INSERT_ACCOUNT_OR_KEYRING');
        };

        main();
        ```

### Storage Methods {: #storage-methods }

The Polkadot XCM Pallet includes the following relevant read-only storage methods:

???+ function "**assetTraps**(hash) — returns the existing number of times an asset has been trapped given a hash of the asset"

    === "Parameters"

        `hash` - (optional) the Blake2-256 hash of the [`Asset`](https://github.com/paritytech/xcm-format#6-universal-asset-identifiers)

    === "Returns"

        The number of times an asset has been trapped. If the hash was omitted, it returns an array of all of the hashes and the number of times each asset has been trapped.

        ```js
        // If using Polkadot.js API and calling toJSON() on the value
        // If hash was provided:
        10

        // If hash was omitted:
        [
          [
            0xf7d4341888be30c6a842a77c52617423e8109aa249e88779019cf731ed772fb7
          ],
          10
        ],
        ...
        ```

    === "Polkadot.js API Example"

        ```js
        
        ```

??? function "**palletVersion**() — returns current pallet version from storage"

    === "Parameters"

        None

    === "Returns"

        A number representing the current version of the pallet.

        ```js
        // If using Polkadot.js API and calling toJSON() on the unwrapped value
        0
        ```

    === "Polkadot.js API Example"

        ```js
        import { ApiPromise, WsProvider } from '@polkadot/api';

        const main = async () => {
          const api = await ApiPromise.create({
            provider: new WsProvider('INSERT_WSS_ENDPOINT'),
          });
          const palletVersion = await api.query.polkadotXcm.palletVersion();
        };

        main();
        ```

## Checking Prerequisites {: #checking-prerequisites }

To follow along with this guide, you will need the following:

- Your account must be funded with DEV tokens.
  You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
## Execute an XCM Message Locally {: #execute-an-xcm-message-locally }

This section of the guide covers the process of building a custom XCM message to be executed locally (i.e., in Moonbeam) via two different methods: the `execute` function of the Polkadot XCM Pallet and the `xcmExecute` function of the [XCM Utilities Precompile](/moonbeam-mkdocs/builders/interoperability/xcm/xcm-utils/). This functionality provides a playground for you to experiment with different XCM instructions and see firsthand the results of these experiments. This also comes in handy to determine the [fees](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/weights-fees/) associated with a given XCM message on Moonbeam.

In the following example, you'll transfer DEV tokens from one account to another on Moonbase Alpha. To do so, you'll be building an XCM message that contains the following XCM instructions, which are executed locally (in this case, on Moonbase Alpha):

 - [`WithdrawAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#withdraw-asset) - removes assets and places them into the holding register
 - [`DepositAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#deposit-asset) - removes the assets from the holding register and deposits the equivalent assets to a beneficiary account

!!! note
    Typically, when you send an XCM message cross-chain to a target chain, the [`BuyExecution` instruction](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#buy-execution) is needed to pay for remote execution. However, for local execution, this instruction is not necessary as you are already getting charged via the extrinsic call.

### Execute an XCM Message with the Polkadot.js API {: #execute-an-xcm-message-with-polkadotjs-api }

In this example, you'll execute a custom XCM message locally on Moonbase Alpha using the Polkadot.js API to interact directly with the Polkadot XCM Pallet.

The `execute` function of the Polkadot XCM Pallet accepts two parameters: `message` and `maxWeight`. You can start assembling these parameters by taking the following steps:

1. Build the `WithdrawAsset` instruction, which will require you to define:
    - The multilocation of the DEV token on Moonbase Alpha
    - The amount of DEV tokens to transfer

    ```js
    const instr1 = {
      WithdrawAsset: [
        {
          id: { parents: 0, interior: { X1: [{ PalletInstance: 3 }] } },
          fun: { Fungible: 100000000000000000n }, // 0.1 DEV
        },
      ],
    };
    ```

2. Build the `DepositAsset` instruction, which will require you to define:
    - The asset identifier for DEV tokens. You can use the [`WildAsset` format](https://github.com/paritytech/xcm-format/blob/master/README.md#6-universal-asset-identifiers), which allows for wildcard matching, to identify the asset
    - The multilocation of the beneficiary account on Moonbase Alpha

    ```js
    const instr2 = {
      DepositAsset: {
        assets: {
          Wild: {
            AllCounted: 1,
          },
        },
        beneficiary: {
          parents: 0,
          interior: {
            X1: [
              {
                AccountKey20: {
                  key: '0x3Cd0A705a2DC65e5b1E1205896BaA2be8A07c6e0',
                },
              },
            ],
          },
        },
      },
    };
    ```

3. Combine the XCM instructions into a versioned XCM message:

    ```js
    const message = { V4: [instr1, instr2] };
    ```

4. Specify the `maxWeight`, which includes a value for `refTime` and `proofSize` that you will need to define. You can get both of these values by providing the XCM message as a parameter to the `queryXcmWeight` method of the [`xcmPaymentApi` runtime call](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fmoonbeam-alpha.api.onfinality.io%2Fpublic-ws#/runtime). 

    ```js
    const maxWeight = { refTime: 7250000000n, proofSize: 19374n };
    ```

Now that you have the values for each of the parameters, you can write the script for the execution. You'll take the following steps:

 1. Provide the input data for the call. This includes:
     - The Moonbase Alpha endpoint URL to create the provider
     - The values for each of the parameters of the `execute` function
 2. Create a Keyring instance that will be used to send the transaction
 3. Create the [Polkadot.js API](/moonbeam-mkdocs/builders/substrate/libraries/polkadot-js-api/) provider
 4. Craft the `polkadotXcm.execute` extrinsic with the `message` and `maxWeight`
 5. Send the transaction using the `signAndSend` extrinsic and the Keyring instance you created in the second step

!!! remember
    This is for demo purposes only. Never store your private key in a JavaScript file.

```js
import { ApiPromise, WsProvider, Keyring } from '@polkadot/api'; // Version 10.13.1
import { cryptoWaitReady } from '@polkadot/util-crypto';

// 1. Provide input data
const providerWsURL = 'wss://wss.api.moonbase.moonbeam.network';
const privateKey = 'INSERT_PRIVATE_KEY';
const instr1 = {
  WithdrawAsset: [
    {
      id: { parents: 0, interior: { X1: [{ PalletInstance: 3 }] } },
      fun: { Fungible: 100000000000000000n }, // 0.1 DEV
    },
  ],
};
const instr2 = {
  DepositAsset: {
    assets: {
      Wild: {
        AllCounted: 1,
      },
    },
    beneficiary: {
      parents: 0,
      interior: {
        X1: [
          {
            AccountKey20: {
              key: '0x3Cd0A705a2DC65e5b1E1205896BaA2be8A07c6e0',
            },
          },
        ],
      },
    },
  },
};
const message = { V4: [instr1, instr2] };
const maxWeight = { refTime: 7250000000n, proofSize: 19374n };

const executeXcmMessage = async () => {
  // 2. Create Keyring instance
  await cryptoWaitReady();
  const keyring = new Keyring({ type: 'ethereum' });
  const alice = keyring.addFromUri(privateKey);

  // 3. Create Substrate API provider
  const substrateProvider = new WsProvider(providerWsURL);
  const api = await ApiPromise.create({ provider: substrateProvider });

  // 4. Craft the extrinsic
  const tx = api.tx.polkadotXcm.execute(message, maxWeight);

  // 5. Send the transaction
  const txHash = await tx.signAndSend(alice);
  console.log(`Submitted with hash ${txHash}`);

  api.disconnect();
};

executeXcmMessage();
```

!!! note
    You can view an example of the above script, which sends 1 DEV to Bob's account on Moonbase Alpha, on [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#/extrinsics/decode/0x1c030408000400010403001300008a5d784563010d010204000103003cd0a705a2dc65e5b1e1205896baa2be8a07c6e007803822b001ba2e0100) using the following encoded calldata: `0x1c030408000400010403001300008a5d784563010d010204000103003cd0a705a2dc65e5b1e1205896baa2be8a07c6e007803822b001ba2e0100`.

Once the transaction is processed, the 0.1 DEV tokens should be withdrawn from Alice's account along with the associated XCM fees, and the destination account should have received 0.1 DEV tokens in their account. A `polkadotXcm.Attempted` event will be emitted with the outcome.


## Test an XCM Message with the Dry Run API {: #test-an-xcm-message-with-the-dry-run-api }

The XCM Dry Run API is an easy and convenient way to test the integrity of your XCM message without incurring any transaction fees. The XCM Dry Run API can be accessed from the [Runtime Calls](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbeam.network#/runtime) tab of the **Developer** section of Polkadot.js Apps.

### Dry Run Call API Method {: #dry-run-call-api-method }

This method takes as a parameter the origin and the call data and returns an execution result, actual weight, and event data.  

```javascript
const testAccount = api.createType(
  'AccountId20',
  '0x88bcE0b038eFFa09e58fE6d24fDe4b5Af21aa798'
);
const callData =
  '0x1c030408000400010403001300008a5d784563010d010204000103003cd0a705a2dc65e5b1e1205896baa2be8a07c6e007803822b001ba2e0100';
const callDataU8a = hexToU8a(callData);

const result = await api.call.dryRunApi.dryRunCall(
  { system: { Signed: testAccount } },
  callDataU8a
);
```

??? code "View the complete script"

    ```js
    import { ApiPromise, WsProvider } from '@polkadot/api';
    import { hexToU8a } from '@polkadot/util';

    const main = async () => {
      try {
        // Construct API provider
        const wsProvider = new WsProvider('INSERT_WSS_ENDPOINT');
        const api = await ApiPromise.create({ provider: wsProvider });

        console.log('Connected to the API. Preparing dry run call...');

        // Create a test account (you should replace this with an actual account)
        const testAccount = api.createType(
          'AccountId20',
          '0x88bcE0b038eFFa09e58fE6d24fDe4b5Af21aa798'
        );

        // The call data (replace with your actual call data)
        const callData =
          '0x1c030408000400010403001300008a5d784563010d010204000103003cd0a705a2dc65e5b1e1205896baa2be8a07c6e007803822b001ba2e0100'; // Your hex-encoded call data

        // Convert hex to Uint8Array
        const callDataU8a = hexToU8a(callData);

        // Perform the dry run call
        const result = await api.call.dryRunApi.dryRunCall(
          { system: { Signed: testAccount } }, // origin
          callDataU8a // call
        );

        console.log(
          'Dry run XCM result:',
          JSON.stringify(result.toJSON(), null, 2)
        );

        // Disconnect the API
        await api.disconnect();
        console.log('Disconnected from the API.');
      } catch (error)
    };

    main().catch(console.error);
    ```

Upon calling the XCM Dry Run API, the method will tell you whether the call would be successful and returns the event data that would be emitted if the call were actually submitted on chain. You can view the initial output of the `dryRunCall` below.

??? code "View the complete output"

    ```json
    Dry run XCM result: {
      "ok": {
        "executionResult": {
          "ok": {
            "actualWeight": {
              "refTime": 7301615000,
              "proofSize": 20928
            },
            "paysFee": "Yes"
          }
        },
        "emittedEvents": [
          {
            "index": "0x030b",
            "data": [
              "0x88bcE0b038eFFa09e58fE6d24fDe4b5Af21aa798",
              "0x0000000000000000016345785d8a0000"
            ]
          },
          {
            "index": "0x0300",
            "data": [
              "0x3Cd0A705a2DC65e5b1E1205896BaA2be8A07c6e0",
              "0x0000000000000000016345785d8a0000"
            ]
          },
          {
            "index": "0x030a",
            "data": [
              "0x3Cd0A705a2DC65e5b1E1205896BaA2be8A07c6e0",
              "0x0000000000000000016345785d8a0000"
            ]
          },
          {
            "index": "0x1c00",
            "data": [
              {
                "complete": {
                  "used": {
                    "refTime": 7250000000,
                    "proofSize": 19374
                  }
                }
              }
            ]
          }
        ],
        "localXcm": {
          "v4": [
            {
              "withdrawAsset": [
                {
                  "id": {
                    "parents": 0,
                    "interior": {
                      "x1": [
                        {
                          "palletInstance": 3
                        }
                      ]
                    }
                  },
                  "fun": {
                    "fungible": "0x0000000000000000016345785d8a0000"
                  }
                }
              ]
            },
            {
              "depositAsset": {
                "assets": {
                  "wild": {
                    "allCounted": 1
                  }
                },
                "beneficiary": {
                  "parents": 0,
                  "interior": {
                    "x1": [
                      {
                        "accountKey20": {
                          "network": null,
                          "key": "0x3cd0a705a2dc65e5b1e1205896baa2be8a07c6e0"
                        }
                      }
                    ]
                  }
                }
              }
            }
          ]
        } // Additional events returned here
          // Omitted for clarity 
    ```

### Dry Run XCM API Method {: #dry-run-xcm-api-method }

The `dryRunXCM` method of the XCM Dry Run API takes a full XCM message as a parameter instead of an encoded call, as well as the origin of the message.

`dryRunXCM` takes as a parameter the origin and the XCM message and returns an execution result, actual weight, and event data.  

```javascript
// Define the origin
const origin = { V4: { parents: 1, interior: 'Here' } };

const message = []; // Insert XCM Message Here

// Perform the dry run XCM call
const result = await api.call.dryRunApi.dryRunXcm(origin, message);
```

??? code "View the complete script"

    ```js
    import { ApiPromise, WsProvider } from '@polkadot/api';
    import { hexToU8a } from '@polkadot/util';

    const main = async () => {
      try {
        // Construct API provider
        const wsProvider = new WsProvider('INSERT_WSS_ENDPOINT');
        const api = await ApiPromise.create({ provider: wsProvider });
        console.log('Connected to the API. Preparing dry run XCM call...');

        // Define the origin
        const origin = { V4: { parents: 1, interior: 'Here' } };
        const amountToSend = 1000000000000;

        const message = {
          V4: [
            {
              WithdrawAsset: [
                {
                  id: { parents: 1, interior: 'Here' },
                  fun: { Fungible: amountToSend },
                },
              ],
            },
            {
              BuyExecution: {
                fees: {
                  id: { parents: 1, interior: 'Here' },
                  fun: { Fungible: amountToSend },
                },
                weightLimit: { Unlimited: null },
              },
            },
            {
              DepositAsset: {
                assets: { Wild: { AllOf: { id: { parents: 1, interior: 'Here' } } } },
                maxAssets: 1,
                beneficiary: {
                  parents: 0,
                  interior: {
                    X1: [
                      {
                        AccountKey20: {
                          network: null,
                          key: hexToU8a('0x3B939FeaD1557C741Ff06492FD0127bd287A421e')
                        }
                      }
                    ]
                  }
                }
              }
            }
          ],
        };

        // Perform the dry run XCM call
        const result = await api.call.dryRunApi.dryRunXcm(origin, message);
        
        console.log(
          'Dry run XCM result:',
          JSON.stringify(result.toJSON(), null, 2)
        );

        await api.disconnect();
        console.log('Disconnected from the API.');
      } catch (error)
    };

    main().catch(console.error);
    ```

Upon calling the XCM Dry Run API, the method will tell you whether the call would be successful and returns the event data that would be emitted if the XCM were to be actually submitted on chain. You can view the initial output of the `dryRunXCM` below.

??? code "View the complete output"

    ```json
    Dry run XCM result: {
      "ok": {
        "executionResult": {
          "complete": {
            "used": {
              "refTime": 76473048000,
              "proofSize": 222483
            }
          }
        },
        "emittedEvents": [
          {
            "index": "0x1d03",
            "data": [
              "0x1fcacbd218edc0eba20fc2308c778080",
              "0x506172656E740000000000000000000000000000",
              1000000000000
            ]
          },
          {
            "index": "0x1d01",
            "data": [
              "0x1fcacbd218edc0eba20fc2308c778080",
              "0x3B939FeaD1557C741Ff06492FD0127bd287A421e",
              959944978002
            ]
          },
          {
            "index": "0x1d01",
            "data": [
              "0x1fcacbd218edc0eba20fc2308c778080",
              "0x6d6F646c70632f74727372790000000000000000",
              40055021998
            ]
          }
        ], // Additional events returned here
          // Omitted for clarity 
    ```

## Execute an XCM Message with the XCM Utilities Precompile {: #execute-xcm-utils-precompile }

In this section, you'll use the `xcmExecute` function of the [XCM Utilities Precompile](/moonbeam-mkdocs/builders/interoperability/xcm/xcm-utils/), which is only supported on Moonbase Alpha, to execute an XCM message locally. The XCM Utilities Precompile is located at the following address:

```text
0x000000000000000000000000000000000000080C
```

Under the hood, the `xcmExecute` function of the XCM Utilities Precompile calls the `execute` function of the Polkadot XCM Pallet, which is a Substrate pallet that is coded in Rust. The benefit of using the XCM Utilities Precompile to call `xcmExecute` is that you can do so via the Ethereum API and use [Ethereum libraries](/moonbeam-mkdocs/builders/ethereum/libraries/) like [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/).

The `xcmExecute` function accepts two parameters: the SCALE encoded versioned XCM message to be executed and the maximum weight to be consumed.

First, you'll learn how to generate the encoded calldata, and then you'll learn how to use the encoded calldata to interact with the XCM Utilities Precompile.

### Generate the Encoded Calldata of an XCM Message {: #generate-encoded-calldata }

To get the encoded calldata of the XCM message, you can create a script similar to the one you created in the [Execute an XCM Message with the Polkadot.js API](#execute-an-xcm-message-with-polkadotjs-api) section. Instead of building the message and sending the transaction, you'll build the message to get the encoded calldata. You'll take the following steps:

 1. Provide the input data for the call. This includes:
     - The Moonbase Alpha endpoint URL to create the provider
     - The values for each of the parameters of the `execute` function as defined in the [Execute an XCM Message with the Polkadot.js API](#execute-an-xcm-message-with-polkadotjs-api) section
 2. Create the [Polkadot.js API](/moonbeam-mkdocs/builders/substrate/libraries/polkadot-js-api/) provider
 3. Craft the `polkadotXcm.execute` extrinsic with the `message` and `maxWeight`
 4. Use the transaction to get the encoded calldata

The entire script is as follows:

```js
import { ApiPromise, WsProvider } from '@polkadot/api'; // Version 10.13.1

// 1. Provide input data
const moonbeamAccount = 'INSERT_ADDRESS';
const providerWsURL = 'wss://wss.api.moonbase.moonbeam.network';
const instr1 = {
  WithdrawAsset: [
    {
      id: { parents: 0, interior: { X1: [{ PalletInstance: 3 }] } },
      fun: { Fungible: 100000000000000000n },
    },
  ],
};
const instr2 = {
  DepositAsset: {
    assets: { Wild: { AllCounted: 1 } },
    beneficiary: {
      parents: 0,
      interior: {
        X1: [
          {
            AccountKey20: {
              key: moonbeamAccount,
            },
          },
        ],
      },
    },
  },
};
const message = { V4: [instr1, instr2] };
const maxWeight = { refTime: 7250000000n, proofSize: 19374n };

const getEncodedXcmMessage = async () => {
  // 2. Create Substrate API provider
  const substrateProvider = new WsProvider(providerWsURL);
  const api = await ApiPromise.create({ provider: substrateProvider });

  // 3. Craft the extrinsic
  const tx = api.tx.polkadotXcm.execute(message, maxWeight);

  // 4. Get the encoded XCM message
  // By using index 0, you'll get just the encoded XCM message.
  // If you wanted to get the maxWeight, you could use index 1
  const encodedXcmMessage = tx.args[0].toHex();
  console.log(`Encoded Calldata for XCM Message: ${encodedXcmMessage}`);

  api.disconnect();
};

getEncodedXcmMessage();
```

### Execute the XCM Message {: #execute-xcm-message }

Now that you have the SCALE encoded XCM message, you can use the following code snippets to programmatically call the `xcmExecute` function of the XCM Utilities Precompile using your [Ethereum library](/moonbeam-mkdocs/builders/ethereum/libraries/) of choice. Generally speaking, you'll take the following steps:

1. Create a provider and signer
2. Create an instance of the XCM Utilities Precompile to interact with
3. Define parameters required for the `xcmExecute` function, which will be the encoded calldata for the XCM message and the maximum weight to use to execute the message. You can set the `maxWeight` to be `400000000n`, which corresponds to the `refTime`. The `proofSize` will automatically be set to the default, which is 64KB
4. Execute the XCM message

!!! remember
    The following snippets are for demo purposes only. Never store your private keys in a JavaScript or Python file.

=== "Ethers.js"

    ```js
    import { ethers } from 'ethers'; // Import Ethers library
    import abi from './xcmUtilsABI.js'; // Import the XCM Utilities Precompile ABI

    const privateKey = 'INSERT_YOUR_PRIVATE_KEY';
    const xcmUtilsAddress = '0x000000000000000000000000000000000000080C';

    /* Create Ethers provider and signer */
    const provider = new ethers.JsonRpcProvider(
      'https://rpc.api.moonbase.moonbeam.network'
    );
    const signer = new ethers.Wallet(privateKey, provider);

    /* Create contract instance of the XCM Utilities Precompile */
    const xcmUtils = new ethers.Contract(
      xcmUtilsAddress,
      abi,
      signer
    );

    const executeXcmMessageLocally = async () => {
      /* Define parameters required for the xcmExecute function */
      const encodedCalldata = 'INSERT_ENCODED_CALLDATA';
      const maxWeight = '400000000';

      /* Execute the custom XCM message */
      const tx = await xcmUtils.xcmExecute(encodedCalldata, maxWeight);
      await tx.wait();
      console.log(`Transaction receipt: ${tx.hash}`);
    };

    executeXcmMessageLocally();
    ```

=== "Web3.js"

    ```js
    import { Web3 } from 'web3'; // Import Web3 library
    import abi from './xcmUtilsABI.js'; // Import the XCM Utilities Precompile ABI

    const privateKey = 'INSERT_PRIVATE_KEY';
    const accountFrom = web3.eth.accounts.privateKeyToAccount(privateKey).address;
    const xcmUtilsAddress = '0x000000000000000000000000000000000000080C';

    /* Create Web3 provider */
    const web3 = new Web3('https://rpc.api.moonbase.moonbeam.network'); // Change to network of choice

    /* Create contract instance of the XCM Utilities Precompile */
    const xcmUtils = new web3.eth.Contract(
      abi,
      xcmUtilsAddress,
      { from: accountFrom } // 'from' is necessary for gas estimation
    );

    const executeXcmMessageLocally = async () => {
      /* Define parameters required for the xcmExecute function */
      const encodedCalldata = 'INSERT_ENCODED_CALLDATA';
      const maxWeight = '400000000';

      /* Send the custom XCM message */
      // Craft the extrinsic
      const tx = await xcmUtils.methods.xcmExecute(encodedCalldata, maxWeight);
      // Sign transaction
      const signedTx = await web3.eth.accounts.signTransaction(
        {
          to: xcmUtilsAddress,
          data: tx.encodeABI(),
          gas: await tx.estimateGas(),
          gasPrice: await web3.eth.getGasPrice(),
          nonce: await web3.eth.getTransactionCount(accountFrom),
        },
        privateKey
      );
      // Send the signed transaction
      const sendTx = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
      console.log(`Transaction receipt: ${sendTx.transactionHash}`);
    };

    executeXcmMessageLocally();
    ```

=== "Web3.py"

    ```py
    from web3 import Web3

    abi = "INSERT_XCM_UTILS_ABI"  # Paste or import the XCM Utils ABI
    # This is for demo purposes, never store your private key in plain text
    private_key = "INSERT_PRIVATE_KEY"
    # The wallet address that corresponds to your private key
    address = "INSERT_ADDRESS"
    xcm_utils_address = "0x000000000000000000000000000000000000080C"

    ## Create Web3 provider ##
    web3 = Web3(Web3.HTTPProvider("https://rpc.api.moonbase.moonbeam.network"))

    ## Create contract instance of the XCM Utilities Precompile ##
    xcm_utils = web3.eth.contract(
        # XCM Utilities Precompile address
        address=xcm_utils_address,
        abi=abi,
    )


    def execute_xcm_message_locally():
        ## Define parameters required for the xcmExecute function ##
        encoded_calldata = "INSERT_ENCODED_CALLDATA"
        max_weight = 400000000

        ## Execute the custom XCM message ##
        # Craft the extrinsic
        tx = xcm_utils.functions.xcmExecute(encoded_calldata, max_weight).build_transaction(
            {
                "from": address,
                "nonce": web3.eth.get_transaction_count(address),
            }
        )
        # Sign transaction
        signedTx = web3.eth.account.sign_transaction(tx, private_key)
        # Send tx
        hash = web3.eth.send_raw_transaction(signedTx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(hash)
        print(f"Transaction receipt: { receipt.transactionHash.hex() }")


    execute_xcm_message_locally()
    ```

And that's it! You've successfully used the Polkadot XCM Pallet and the XCM Utilities Precompile to execute a custom XCM message locally on Moonbase Alpha!

## Send an XCM Message Cross-Chain {: #send-xcm-message }

This section of the guide covers the process of sending a custom XCM message cross-chain (i.e., from Moonbeam to a target chain, such as the relay chain) via two different methods: the `send` function of the Polkadot XCM Pallet and the `xcmSend` function of the [XCM Utilities Precompile](/moonbeam-mkdocs/builders/interoperability/xcm/xcm-utils/).

For the XCM message to be successfully executed, the target chain needs to be able to understand the instructions in the message. If it doesn't, you'll see a `Barrier` filter on the destination chain. For security reasons, the XCM message is prepended with the [`DescendOrigin`](https://github.com/paritytech/xcm-format#descendorigin) instruction to prevent XCM execution on behalf of the origin chain Sovereign account. **The example in this section will not work for the reasons mentioned above, it is purely for demonstration purposes**.

In the following example, you'll be building an XCM message that contains the following XCM instructions, which will be executed in the Alphanet relay chain:

 - [`WithdrawAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#withdraw-asset) - removes assets and places them into the holding register
 - [`BuyExecution`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#buy-execution) - takes the assets from holding to pay for execution fees. The fees to pay are determined by the target chain
 - [`DepositAsset`](/moonbeam-mkdocs/builders/interoperability/xcm/core-concepts/instructions/#deposit-asset)- removes the assets from the holding register and deposits the equivalent assets to a beneficiary account

Together, the intention of these instructions is to transfer the native asset of the relay chain, which is UNIT for the Alphanet relay chain, from Moonbase Alpha to an account on the relay chain. This example is for demonstration purposes only to show you how a custom XCM message could be sent cross-chain. Please keep in mind that the target chain needs to be able to understand the instructions in the message to execute them.

### Send an XCM Message with the Polkadot.js API {: #send-xcm-message-with-polkadotjs-api }

In this example, you'll send a custom XCM message from your account on Moonbase Alpha to the relay chain using the [Polkadot.js API](/moonbeam-mkdocs/builders/substrate/libraries/polkadot-js-api/) to interact directly with the Polkadot XCM Pallet.

The `send` function of the Polkadot XCM Pallet accepts two parameters: `dest` and `message`. You can start assembling these parameters by taking the following steps:

1. Build the multilocation of the relay chain token, UNIT, for the `dest`:

    ```js
    const dest = { V4: { parents: 1, interior: null } };
    ```

2. Build the `WithdrawAsset` instruction, which will require you to define:
    - The multilocation of the UNIT token on the relay chain
    - The amount of UNIT tokens to withdraw

    ```js
    const instr1 = {
      WithdrawAsset: [
        {
          id: { parents: 1, interior: null },
          fun: { Fungible: 1000000000000n }, // 1 UNIT
        },
      ],
    };
    ```

3. Build the `BuyExecution` instruction, which will require you to define:
    - The multilocation of the UNIT token on the relay chain
    - The amount of UNIT tokens to buy for execution
    - The weight limit

    ```js
    const instr2 = {
      BuyExecution: [
        {
          id: { parents: 1, interior: null },
          fun: { Fungible: 1000000000000n }, // 1 UNIT
        },
        { Unlimited: null },
      ],
    };
    ```

4. Build the `DepositAsset` instruction, which will require you to define:
    - The asset identifier for UNIT tokens. You can use the [`WildAsset` format](https://github.com/paritytech/xcm-format/blob/master/README.md#6-universal-asset-identifiers), which allows for wildcard matching, to identify the asset
    - The multilocation of the beneficiary account on the relay chain

    ```js
    const instr3 = {
      DepositAsset: {
        assets: { Wild: 'All' },
        beneficiary: {
          parents: 1,
          interior: {
            X1: [
              {
                AccountId32: {
                  id: relayAccount,
                },
              },
            ],
          },
        },
      },
    };
    ```

5. Combine the XCM instructions into a versioned XCM message:

    ```js
    const message = { V4: [instr1, instr2, instr3] };
    ```

Now that you have the values for each of the parameters, you can write the script to send the XCM message. You'll take the following steps:

 1. Provide the input data for the call. This includes:
     - The Moonbase Alpha endpoint URL to create the provider
     - The values for each of the parameters of the `send` function
 2. Create a Keyring instance that will be used to send the transaction
 3. Create the [Polkadot.js API](/moonbeam-mkdocs/builders/substrate/libraries/polkadot-js-api/) provider
 4. Craft the `polkadotXcm.send` extrinsic with the `dest` and `message`
 5. Send the transaction using the `signAndSend` extrinsic and the Keyring instance you created in the second step

!!! remember
    This is for demo purposes only. Never store your private key in a JavaScript file.

```js
import { ApiPromise, WsProvider, Keyring } from '@polkadot/api'; // Version 10.13.1
import { cryptoWaitReady, decodeAddress } from '@polkadot/util-crypto';

// 1. Input data
const providerWsURL = 'wss://wss.api.moonbase.moonbeam.network';
// You can use the decodeAddress function to ensure that your address is properly
// decoded. If it isn't decoded, it will decode it and if it is, it will ignore it
const privateKey = 'INSERT_PRIVATE_KEY';
const relayAccount = decodeAddress('INSERT_ADDRESS');
const dest = { V4: { parents: 1, interior: null } };
const instr1 = {
  WithdrawAsset: [
    {
      id: { parents: 1, interior: null },
      fun: { Fungible: 1000000000000n }, // 1 UNIT
    },
  ],
};
const instr2 = {
  BuyExecution: [
    {
      id: { parents: 1, interior: null },
      fun: { Fungible: 1000000000000n }, // 1 UNIT
    },
    { Unlimited: null },
  ],
};
const instr3 = {
  DepositAsset: {
    assets: { Wild: 'All' },
    beneficiary: {
      parents: 1,
      interior: {
        X1: [
          {
            AccountId32: {
              id: relayAccount,
            },
          },
        ],
      },
    },
  },
};
const message = { V4: [instr1, instr2, instr3] };

const sendXcmMessage = async () => {
  // 2. Create Keyring instance
  await cryptoWaitReady();
  const keyring = new Keyring({ type: 'ethereum' });
  const alice = keyring.addFromUri(privateKey);

  // 3. Create Substrate API Provider
  const substrateProvider = new WsProvider(providerWsURL);
  const api = await ApiPromise.create({ provider: substrateProvider });

  // 4. Create the extrinsic
  const tx = api.tx.polkadotXcm.send(dest, message);

  // 5. Send the transaction
  const txHash = await tx.signAndSend(alice);
  console.log(`Submitted with hash ${txHash}`);

  api.disconnect();
};

sendXcmMessage();
```

!!! note
    You can view an example of the above script, which sends 1 UNIT to Bob's relay chain account, on [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#/extrinsics/decode/0x1c00040100040c0004010000070010a5d4e813010000070010a5d4e8000d0100010101000c36e9ba26fa63c60ec728fe75fe57b86a450d94e7fee7f9f9eddd0d3f400d67) using the following encoded calldata: `0x1c00040100040c0004010000070010a5d4e813010000070010a5d4e8000d0100010101000c36e9ba26fa63c60ec728fe75fe57b86a450d94e7fee7f9f9eddd0d3f400d67`.

Once the transaction is processed, a `polkadotXcm.sent` event is emitted with the details of the sent XCM message.

### Send an XCM Message with the XCM Utilities Precompile {: #send-xcm-utils-precompile }

In this section, you'll use the `xcmSend` function of the [XCM Utilities Precompile](/moonbeam-mkdocs/builders/interoperability/xcm/xcm-utils/), which is only supported on Moonbase Alpha, to send an XCM message cross-chain. The XCM Utilities Precompile is located at the following address:

=== "Moonbase Alpha"

     ```text
     0x000000000000000000000000000000000000080C
     ```

Under the hood, the `xcmSend` function of the XCM Utilities Precompile calls the `send` function of the Polkadot XCM Pallet, which is a Substrate pallet that is coded in Rust. The benefit of using the XCM Utilities Precompile to call `xcmSend` is that you can do so via the Ethereum API and use Ethereum libraries like [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/). For the XCM message to be successfully executed, the target chain needs to be able to understand the instructions in the message.

The `xcmSend` function accepts two parameters: the multilocation of the destination and the SCALE encoded versioned XCM message to be sent.

First, you'll learn how to generate the encoded calldata for the XCM message, and then you'll learn how to use the encoded calldata to interact with the XCM Utilities Precompile.

#### Generate the Encoded Calldata of an XCM Message {: #generate-encoded-calldata }

To get the encoded calldata of the XCM message, you can create a script similar to the one you created in the [Send an XCM Message with the Polkadot.js API](#send-xcm-message-with-polkadotjs-api) section. Instead of building the message and sending the transaction, you'll build the message to get the encoded calldata. You'll take the following steps:

 1. Provide the input data for the call. This includes:
     - The Moonbase Alpha endpoint URL to create the provider
     - The values for each of the parameters of the `send` function as defined in the [Send an XCM Message with the Polkadot.js API](#send-xcm-message-with-polkadotjs-api) section
 2. Create the [Polkadot.js API](/moonbeam-mkdocs/builders/substrate/libraries/polkadot-js-api/) provider
 3. Craft the `polkadotXcm.execute` extrinsic with the `message` and `maxWeight`
 4. Use the transaction to get the encoded calldata

The entire script is as follows:

```js
import { ApiPromise, WsProvider } from '@polkadot/api'; // Version 10.13.1
import { decodeAddress } from '@polkadot/util-crypto';

// 1. Input data
const providerWsURL = 'wss://wss.api.moonbase.moonbeam.network';
// You can use the decodeAddress function to ensure that your address is properly
// decoded. If it isn't decoded, it will decode it and if it is, it will ignore it
const relayAccount = decodeAddress('INSERT_ADDRESS');
const dest = { V4: { parents: 1, interior: null } };
const instr1 = {
  WithdrawAsset: [
    {
      id: { parents: 1, interior: null },
      fun: { Fungible: 1000000000000n }, // 1 UNIT
    },
  ],
};
const instr2 = {
  BuyExecution: [
    {
      id: { parents: 1, interior: null },
      fun: { Fungible: 1000000000000n }, // 1 UNIT
    },
    { Unlimited: null },
  ],
};
const instr3 = {
  DepositAsset: {
    assets: { Wild: 'All' },
    beneficiary: {
      parents: 1,
      interior: {
        X1: [
          {
            AccountId32: {
              id: relayAccount,
            },
          },
        ],
      },
    },
  },
};
const message = { V4: [instr1, instr2, instr3] };

const generateEncodedXcmMessage = async () => {
  // 2. Create Substrate API Provider
  const substrateProvider = new WsProvider(providerWsURL);
  const api = await ApiPromise.create({ provider: substrateProvider });

  // 3. Create the extrinsic
  const tx = api.tx.polkadotXcm.send(dest, message);

  // 4. Get the encoded XCM message
  // By using index 1, you'll get just the encoded XCM message.
  // If you wanted to get the dest, you could use index 0
  const encodedXcmMessage = tx.args[1].toHex();
  console.log(`Encoded Calldata for XCM Message: ${encodedXcmMessage}`);

  api.disconnect();
};

generateEncodedXcmMessage();
```

#### Send the XCM Message {: #send-xcm-message }

Before you can send the XCM message, you'll also need to build the multilocation of the destination. For this example, you'll target the relay chain with Moonbase Alpha as the origin chain:

```js
const dest = [
  1, // Parents: 1 
  [] // Interior: Here
];
```

Now that you have the SCALE encoded XCM message and the destination multilocation, you can use the following code snippets to programmatically call the `xcmSend` function of the XCM Utilities Precompile using your [Ethereum library](/moonbeam-mkdocs/builders/ethereum/libraries/) of choice. Generally speaking, you'll take the following steps:

1. Create a provider and signer
2. Create an instance of the XCM Utilities Precompile to interact with
3. Define parameters required for the `xcmSend` function, which will be the destination and the encoded calldata for the XCM message
4. Send the XCM message

!!! remember
    The following snippets are for demo purposes only. Never store your private keys in a JavaScript or Python file.

=== "Ethers.js"

    ```js
    import { ethers } from 'ethers'; // Import Ethers library
    import abi from './xcmUtilsABI.js'; // Import the XCM Utilities Precompile ABI

    const privateKey = 'INSERT_PRIVATE_KEY';
    const xcmUtilsAddress = '0x000000000000000000000000000000000000080C';

    /* Create Ethers provider and signer */
    const provider = new ethers.JsonRpcProvider(
      'https://rpc.api.moonbase.moonbeam.network'
    );
    const signer = new ethers.Wallet(privateKey, provider);

    /* Create contract instance of the XCM Utilities Precompile */
    const xcmUtils = new ethers.Contract(
      xcmUtilsAddress,
      abi,
      signer
    );

    const sendXcm = async () => {
      /* Define parameters required for the xcmSend function */
      const encodedCalldata = 'INSERT_ENCODED_CALLDATA';
      const dest = [
        1, // Parents: 1 
        [] // Interior: Here
      ];

      /* Send the custom XCM message */
      const tx = await xcmUtils.xcmSend(dest, encodedCalldata);
      await tx.wait();
      console.log(`Transaction receipt: ${tx.hash}`);
    };

    sendXcm();
    ```

=== "Web3.js"

    ```js
    import { Web3 } from 'web3'; // Import Web3 library
    import abi from './xcmUtilsABI.js'; // Import the XCM Utilities Precompile ABI

    const privateKey = 'INSERT_PRIVATE_KEY';
    const accountFrom = web3.eth.accounts.privateKeyToAccount(privateKey).address;
    const xcmUtilsAddress = '0x000000000000000000000000000000000000080C';

    /* Create Web3 provider */
    const web3 = new Web3('https://rpc.api.moonbase.moonbeam.network'); // Change to network of choice

    /* Create contract instance of the XCM Utilities Precompile */
    const xcmUtils = new web3.eth.Contract(
      abi,
      xcmUtilsAddress,
      { from: accountFrom } // 'from' is necessary for gas estimation
    );

    const sendXcm = async () => {
      /* Define parameters required for the xcmSend function */
      const encodedCalldata = 'INSERT_ENCODED_CALLDATA';
      const dest = [
        1, // Parents: 1
        [], // Interior: Here
      ];

      /* Send the custom XCM message */
      // Craft the extrinsic
      const tx = await xcmUtils.methods.xcmSend(dest, encodedCalldata);
      // Sign transaction
      const signedTx = await web3.eth.accounts.signTransaction(
        {
          to: xcmUtilsAddress,
          data: tx.encodeABI(),
          gas: await tx.estimateGas(),
          gasPrice: await web3.eth.getGasPrice(),
          nonce: await web3.eth.getTransactionCount(accountFrom),
        },
        privateKey
      );
      // Send the signed transaction
      const sendTx = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
      console.log(`Transaction receipt: ${sendTx.transactionHash}`);
    };

    sendXcm();
    ```

=== "Web3.py"

    ```py
    from web3 import Web3

    abi = "INSERT_XCM_UTILS_ABI"  # Paste or import the XCM Utils ABI
    # This is for demo purposes, never store your private key in plain text
    private_key = "INSERT_PRIVATE_KEY"
    # The wallet address that corresponds to your private key
    address = "INSERT_ADDRESS"
    xcm_utils_address = "0x000000000000000000000000000000000000080C"

    ## Create Web3 provider ##
    web3 = Web3(Web3.HTTPProvider("https://rpc.api.moonbase.moonbeam.network"))

    ## Create contract instance of the XCM Utilities Precompile ##
    xcm_utils = web3.eth.contract(
        # XCM Utilities Precompile address
        address=xcm_utils_address,
        abi=abi,
    )


    def send_xcm():
        ## Define parameters required for the xcmSend function ##
        encoded_calldata = "INSERT_ENCODED_CALLDATA"
        xcm_dest = [1, []]  # Parents: 1  # Interior: Here

        ## Send the custom XCM message ##
        # Craft the extrinsic
        tx = xcm_utils.functions.xcmSend(xcm_dest, encoded_calldata).build_transaction(
            {
                "from": address,
                "nonce": web3.eth.get_transaction_count(address),
            }
        )
        # Sign transaction
        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        # Send tx
        hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(hash)
        print(f"Transaction receipt: { receipt.transactionHash.hex() }")


    send_xcm()
    ```

And that's it! You've successfully used the Polkadot XCM Pallet and the XCM Utilities Precompile to send a message from Moonbase Alpha to another chain!
