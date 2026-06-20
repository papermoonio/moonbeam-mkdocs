---
title: Gasless Transactions with 0xGasless
description: Learn how to implement gasless transactions on Moonbeam using 0xGasless, enabling users to interact with smart contracts without holding native tokens.
categories:
- Tutorials
url: https://docs.moonbeam.network/tutorials/integrations/0xgasless/
word_count: 1529
token_estimate: 2467
version_hash: sha256:96741f0b8981ad196db317d97dbc5d808af8ff79d9dd71fe759d03dd527abb97
last_updated: '2026-05-21T21:21:53+00:00'
---

# Enabling Gasless Transactions with 0xGasless

## Why Gasless Transactions?

One of the primary challenges in blockchain development has been the requirement for users to hold native tokens (like ETH or GLMR) to pay transaction fees. This traditional EOA-based model creates unnecessary friction, particularly when onboarding users who expect Web2-like experiences.

Gasless transactions can help solve this through Account Abstraction ([ERC-4337](https://eips.ethereum.org/EIPS/eip-4337)), implementing meta-transactions that separate user actions from fee payment. This architecture allows dApps or third-party paymasters to cover gas costs on behalf of users while smart contract wallets handle the transaction execution. [0xGasless](https://0xgasless.com/index.html) leverages these principles in its SDK, enabling Moonbeam developers to implement sophisticated features like social logins, transaction batching, and custom wallet controls – all while abstracting away the complexity of gas management from end users.

In the following tutorial, we'll go through the end-to-end steps of setting up a paymaster on 0xGasless and dispatching a gasless transaction to modify the state of a smart contract on Moonbeam.

## Create and Fund a Paymaster

First, you'll need to [register for an account on 0xGasless](https://dashboard.0xgasless.com/auth/sign-in). Then, [create a Paymaster](https://dashboard.0xgasless.com/paymaster) for the Moonbeam Network by pressing **Create Paymaster** and then taking the following steps:

1. Enter a name for your paymaster
2. Select **Moonbeam** as the chain
3. Press **Create**

![Create Paymaster](/moonbeam-mkdocs/images/tutorials/integrations/0xgasless/0xgasless-1.webp)

Your paymaster needs funds to cover gas fees for sponsored transactions. To deposit GLMR into your paymaster, take the following steps:

1. Enter the amount you would like to deposit
2. Press **Deposit** and confirm the transaction in your wallet

![Fund Paymaster](/moonbeam-mkdocs/images/tutorials/integrations/0xgasless/0xgasless-2.webp)

Your deposited funds remain flexible - use them to sponsor gasless transactions or withdraw them whenever needed.

## Dispatching a Gasless Transaction

In the following section, we'll create a script demonstrating how to dispatch a gasless transaction. 

### Prerequisites

Create a `.env` file in your project's root directory with the following:

```bash
PRIVATE_KEY=INSERT_PRIVATE_KEY
RPC_URL=https://rpc.api.moonbeam.network
```

Why are we specifying a private key in the `.env`? While this transaction will be gasless, you still need a private key to sign the transaction. The account associated with this private key:

- Does not need any GLMR tokens
- Will not pay for gas fees
- Is only used for transaction signing

!!! note 

	Never commit your .env file or share your private key. Add .env to your .gitignore file.

Also, make sure you have installed the 0xGasless SDK and supporting `ethers` and `dotenv` packages:

```bash
npm install ethers dotenv @0xgasless/smart-account
```

First, we'll import the required packages as follows:

```js
require('dotenv').config();
const ethers = require('ethers');
const {
  PaymasterMode,
  createSmartAccountClient,
} = require('@0xgasless/smart-account');
```

Next, we'll set the critical constants. We must define the `CHAIN_ID`, `BUNDLER_URL`, and `PAYMASTER_URL`. You can get your unique paymaster URL from the paymaster on your [0xGasless Dashboard](https://dashboard.0xgasless.com/paymaster).

The contract address we've defined here is the address of an [Incrementer contract](https://moonscan.io/address/0x3ae26f2c909eb4f1edf97bf60b36529744b09213) on Moonbeam, on which we'll call the increment function specified by the function selector. This simple contract will allow us to easily see if the gasless transaction has been dispatched successfully. 

```js
const CHAIN_ID = 1284; // Moonbeam mainnet
const BUNDLER_URL = `https://bundler.0xgasless.com/${CHAIN_ID}`;
const PAYMASTER_URL =
  'https://paymaster.0xgasless.com/v1/1284/rpc/INSERT_API_KEY';
const CONTRACT_ADDRESS = '0x3aE26f2c909EB4F1EdF97bf60B36529744b09213';
const FUNCTION_SELECTOR = '0xd09de08a';
```

!!! warning

    The Paymaster URL format has recently changed. Use:

    ```
    https://paymaster.0xgasless.com/v1/1284/rpc/INSERT_API_KEY
    ```

    Do not use the deprecated format:

    ```
    https://paymaster.0xgasless.com/api/v1/1284/rpc/INSERT_API_KEY
    ```

    The difference is that `/api` has been removed from the path. Make sure your code uses the current format.

### Sending the Transaction

To send a gasless transaction using the 0xGasless smart account, you can call `smartWallet.sendTransaction()` with two parameters:

   - The `transaction` object containing the contract interaction details
   - A configuration object specifying `paymasterServiceData` with `SPONSORED` mode. This indicates that the 0xGasless paymaster will use the gas tank to pay for the gas. 

The function returns a UserOperation response containing a hash. Wait for the transaction receipt using the `waitForUserOpReceipt()` helper function, which polls for completion with a configurable timeout (default 60 seconds).

```javascript
const userOpResponse = await smartWallet.sendTransaction(transaction, {
  paymasterServiceData: { mode: PaymasterMode.SPONSORED },
});

const receipt = await waitForUserOpReceipt(userOpResponse, 60000);
```

Putting it all together and adding plenty of logging and error handling for easy debugging, the full script is as follows:

??? code "Dispatch a gasless transaction"
    ```javascript
    require('dotenv').config();
    const ethers = require('ethers');
    const {
      PaymasterMode,
      createSmartAccountClient,
    } = require('@0xgasless/smart-account');

    const CHAIN_ID = 1284; // Moonbeam mainnet
    const BUNDLER_URL = `https://bundler.0xgasless.com/${CHAIN_ID}`;
    const PAYMASTER_URL =
      'https://paymaster.0xgasless.com/v1/1284/rpc/INSERT_API_KEY';
    const CONTRACT_ADDRESS = '0x3aE26f2c909EB4F1EdF97bf60B36529744b09213';
    const FUNCTION_SELECTOR = '0xd09de08a';

    async function main() (Chain ID: ${network.chainId})`
        );
        const balance = await provider.getBalance(wallet.address);
        console.log(`Wallet balance: ${ethers.utils.formatEther(balance)} GLMR`);

        // Initialize smart account
        console.log('Initializing smart account...');
        const smartWallet = await createSmartAccountClient({
          signer: wallet,
          paymasterUrl: PAYMASTER_URL,
          bundlerUrl: BUNDLER_URL,
          chainId: CHAIN_ID,
        });
        const smartWalletAddress = await smartWallet.getAddress();
        console.log('Smart Account Address:', smartWalletAddress);

        // Create a transaction for contract interaction
        console.log('Creating contract transaction...');
        const transaction = {
          to: CONTRACT_ADDRESS,
          value: '0', // No native token transfer
          data: FUNCTION_SELECTOR, // The function selector for the method we want to call
        };

        // Send the transaction
        console.log('Sending transaction...');
        const userOpResponse = await smartWallet.sendTransaction(transaction, {
          paymasterServiceData: { mode: PaymasterMode.SPONSORED },
        });
        console.log('UserOp Hash:', userOpResponse.hash);

        console.log('Waiting for transaction receipt...');
        const userOpReceipt = await waitForUserOpReceipt(userOpResponse, 60000); // Wait for up to 60 seconds

        if (userOpReceipt.success) else {
          console.log('Transaction failed');
          console.log('Receipt:', userOpReceipt);
        }
      } catch (error)
    }

    async function waitForUserOpReceipt(userOpResponse, timeoutMs = 60000) catch (error)ms`));
            } else {
              setTimeout(checkReceipt, 5000); // Retry every 5 seconds
            }
          }
        };
        checkReceipt();
      });
    }

    main().catch((error) => {
      console.error('Unhandled error in main function:');
      console.error(error);
    });
    ```

### Verifying Completion

Upon running the script, you'll see output that looks like the following: 

<div id="termynal" data-termynal>
    <span data-ty="input">0xgasless % node dispatch.js</span>
    <span data-ty>Starting the script...</span>
    <span data-ty>Setting up provider and wallet...</span>
    <span data-ty>Checking network connection...</span>
    <span data-ty>Connected to network: unknown (Chain ID: 1284)</span>
    <span data-ty>Wallet balance: 8.781249287153010128 GLMR</span>
    <span data-ty>Initializing smart account...</span>
    <span data-ty>Smart Account Address: 0xbBf77D3B43d81D426c4c3D200a76F4D3a914ccE3</span>
    <span data-ty>Creating contract transaction...</span>
    <span data-ty>Sending transaction...</span>
    <span data-ty>UserOp Hash: undefined</span>
    <span data-ty>Waiting for transaction receipt...</span>
    <span data-ty>Transaction successful!</span>
    <span data-ty>Transaction hash: 0x9cb49cc0acc21abc364c13dd52b3f65c206ec61c57a13c23b635f59e1919cf7c</span>
</div>
Since the gasless transaction we initiated interacts with an [Incrementer](https://moonscan.io/address/0x3ae26f2c909eb4f1edf97bf60b36529744b09213#readContract) smart contract on Moonbeam, it's easy to check to see if the transaction was initiated successfully. You can return to [Read Contract section of the Incrementer contract on Moonscan](https://moonscan.io/address/0x3ae26f2c909eb4f1edf97bf60b36529744b09213#readContract) and check the number stored in the contract. Alternatively, you can head to the **Internal Transactions** tab and toggle advanced mode **ON** to see the contract call incrementing the contract. 

For more information about integrating support for gasless transactions into your dApp, be sure to check out the [0xGasless docs](https://docs.0xgasless.com/).

<div class="page-disclaimer">
    This tutorial is for educational purposes only. As such, any contracts or code created in this tutorial should not be used in production.
</div>
<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
