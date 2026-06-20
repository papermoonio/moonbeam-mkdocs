---
title: How to use viem Ethereum Library
description: Check out this tutorial to learn how to use the viem TypeScript interface for Ethereum to send transactions and deploy Solidity smart contracts to Moonbeam.
categories:
- Libraries and SDKs
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/libraries/viem/
word_count: 4865
token_estimate: 8135
version_hash: sha256:ac33bcbfbba18ab05952e47ddc2e73425bded159f97389d99e10329de73e8949
last_updated: '2026-05-21T21:21:53+00:00'
---

# viem TypeScript Ethereum Library

## Introduction {: #introduction }

[viem](https://viem.sh) is a modular TypeScript library that allows developers to interact with abstractions over the JSON-RPC API, making it easy to interact with Ethereum nodes. Since Moonbeam has an Ethereum-like API available that is fully compatible with Ethereum-style JSON RPC invocations, developers can leverage this compatibility to interact with Moonbeam nodes. For more information on viem, check out their [documentation site](https://viem.sh/docs/getting-started).

In this guide, you'll learn how to use viem to send a transaction and deploy a contract on the Moonbase Alpha TestNet. This guide can be adapted for [Moonbeam](/moonbeam-mkdocs/builders/get-started/networks/moonbeam/), [Moonriver](/moonbeam-mkdocs/builders/get-started/networks/moonriver/), or a [Moonbeam development node](/moonbeam-mkdocs/builders/get-started/networks/moonbeam-dev/).

## Checking Prerequisites {: #checking-prerequisites }

For the examples in this guide, you will need to have the following:

- An account with funds.
  You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
- 
  To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/)
!!! note
    The examples in this guide assume you have a MacOS or Ubuntu 22.04-based environment and will need to be adapted accordingly for Windows.
## Installing viem {: #installing-viem }

To get started, you'll need to create a basic TypeScript project. First, create a directory to store all of the files you'll be creating throughout this guide, and initialize the project with the following command:

```bash
mkdir viem-examples && cd viem-examples && npm init --y
```

For this guide, you'll need to install the viem library and the Solidity compiler. To install both packages, you can run the following command:

=== "npm"

    ```bash
    npm install typescript ts-node viem solc@0.8.30
    ```

=== "yarn"

    ```bash
    yarn add typescript ts-node viem solc@0.8.30
    ```

You can create a TypeScript configuration file by running:

```bash
npx tsc --init
```

!!! note
    This tutorial was created using Node.js v18.18.0.

## Set Up a viem Client (Provider)

Throughout this guide, you'll be creating a bunch of scripts that provide different functionality, such as sending a transaction, deploying a contract, and interacting with a deployed contract. In most of these scripts, you'll need to create a [viem client](https://docs.ethers.org/v6/api/providers/) to interact with the network.

To configure your project for Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
You can create a viem client for reading chain data, like balances or contract data, using the `createPublicClient` function, or you can create a viem client for writing chain data, like sending transactions, using the `createWalletClient` function.

### For Reading Chain Data {: #for-reading-chain-data }

To create a client for reading chain data, you can take the following steps:

1. Import the `createPublicClient` and `http` functions from `viem` and the network you want to interact with from `viem/chains`. The chain can be any of the following: `moonbeam`, `moonriver`, or `moonbaseAlpha`
2. Create the `client` using the `createPublicClient` function and pass in the network and the HTTP RPC endpoint

=== "Moonbeam"

    ```ts
    import { createPublicClient, http } from 'viem';
    import { moonbeam } from 'viem/chains';

    const rpcUrl = 'INSERT_RPC_API_ENDPOINT'
    const publicClient = createPublicClient({
      chain: moonbeam,
      transport: http(rpcUrl),
    });
    ```

=== "Moonriver"

    ```ts
    import { createPublicClient, http } from 'viem';
    import { moonriver } from 'viem/chains';

    const rpcUrl = 'INSERT_RPC_API_ENDPOINT'
    const publicClient = createPublicClient({
      chain: moonriver,
      transport: http(rpcUrl),
    });
    ```

=== "Moonbase Alpha"

    ```ts
    import { createPublicClient, http } from 'viem';
    import { moonbaseAlpha } from 'viem/chains';

    const rpcUrl = 'https://rpc.api.moonbase.moonbeam.network'
    const publicClient = createPublicClient({
      chain: moonbaseAlpha,
      transport: http(rpcUrl),
    });
    ```

=== "Moonbeam Dev Node"

    ```ts
    import { createPublicClient, http } from 'viem';
    import { moonbeamDev } from 'viem/chains';

    const rpcUrl = 'http://127.0.0.1:9944'
    const publicClient = createPublicClient({
      chain: moonbeamDev,
      transport: http(rpcUrl),
    })
    ```

### For Writing Chain Data {: #for-writing-chain-data }

To create a client for writing chain data, you can take the following steps:

1. Import the `createWalletClient` and `http` functions from `viem`, the `privateKeyToAccount` function for loading your accounts via their private keys, and the network you want to interact with from `viem/chains`. The chain can be any of the following: `moonbeam`, `moonriver`, or `moonbaseAlpha`
2. Create your account using the `privateKeyToAccount` function
3. Create the `client` using the `createWalletClient` function and pass in the account, network, and the HTTP RPC endpoint

!!! remember
    This is for demo purposes only. Never store your private key in a TypeScript file.

=== "Moonbeam"

    ```ts
    import { createWalletClient, http } from 'viem';
    import { privateKeyToAccount } from 'viem/accounts';
    import { moonbeam } from 'viem/chains';

    const account = privateKeyToAccount('INSERT_PRIVATE_KEY');
    const rpcUrl = 'INSERT_RPC_API_ENDPOINT'
    const walletClient = createWalletClient({
      account,
      chain: moonbeam,
      transport: http(rpcUrl),
    });
    ```

=== "Moonriver"

    ```ts
    import { createWalletClient, http } from 'viem';
    import { privateKeyToAccount } from 'viem/accounts';
    import { moonriver } from 'viem/chains';

    const account = privateKeyToAccount('INSERT_PRIVATE_KEY');
    const rpcUrl = 'INSERT_RPC_API_ENDPOINT'
    const walletClient = createWalletClient({
      account,
      chain: moonriver,
      transport: http(rpcUrl),
    });
    ```

=== "Moonbase Alpha"

    ```ts
    import { createWalletClient, http } from 'viem';
    import { privateKeyToAccount } from 'viem/accounts';
    import { moonbaseAlpha } from 'viem/chains';

    const account = privateKeyToAccount('INSERT_PRIVATE_KEY');
    const rpcUrl = 'https://rpc.api.moonbase.moonbeam.network'
    const walletClient = createWalletClient({
      account,
      chain: moonbaseAlpha,
      transport: http(rpcUrl),
    });
    ```

=== "Moonbeam Dev Node"

    ```ts
    import { createWalletClient, http } from 'viem';
    import { privateKeyToAccount } from 'viem/accounts';
    import { moonbeamDev } from 'viem/chains';

    const account = privateKeyToAccount('INSERT_PRIVATE_KEY');
    const rpcUrl = 'http://127.0.0.1:9944'
    const walletClient = createWalletClient({
      account,
      chain: moonbeamDev,
      transport: http(rpcUrl),
    });
    ```

!!! note
    To interact with browser-based wallets, you can use the following code to create an account:

    ```ts
    const [account] = await window.ethereum.request({
      method: 'eth_requestAccounts',
    });
    const walletClient = createWalletClient({
      account,
      chain: moonbeam,
      transport: custom(window.ethereum),
    });
    ```

## Send a Transaction {: #send-transaction }

During this section, you'll be creating a couple of scripts. The first one will be to check the balances of your accounts before trying to send a transaction. The second script will actually send the transaction.

You can also use the balance script to check the account balances after the transaction has been sent.

### Check Balances Script {: #check-balances-script }

You'll only need one file to check the balances of both addresses before and after the transaction is sent. To get started, you can create a `balances.ts` file by running:

```bash
touch balances.ts
```

Next, you will create the script for this file and complete the following steps:

1. Update your imports to include the `createPublicClient`, `http`, and `formatEther` functions from `viem` and the network you want to interact with from `viem/chains`
2. [Set up a public viem client](#for-reading-chain-data), which can be used for reading chain data, such as account balances
3. Define the `addressFrom` and `addressTo` variables
4. Create the asynchronous `balances` function that wraps the `publicClient.getBalance` method
5. Use the `publicClient.getBalance` function to fetch the balances for the `addressFrom` and `addressTo` addresses. You can also leverage the `formatEther` function to transform the balance into a more readable number (in GLMR, MOVR, or DEV)
6. Lastly, run the `balances` function

```ts
// 1. Imports
import { createPublicClient, http, formatEther } from 'viem';
import { moonbaseAlpha } from 'viem/chains';

// 2. Create a public client for reading chain data
const rpcUrl = 'https://rpc.api.moonbase.moonbeam.network';
const publicClient = createPublicClient({
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});

// 3. Create address variables
const addressFrom = 'INSERT_FROM_ADDRESS';
const addressTo = 'INSERT_TO_ADDRESS';

// 4. Create balances function
const balances = async () => {
  // 5. Fetch balances
  const balanceFrom = formatEther(
    await publicClient.getBalance({ address: addressFrom })
  );
  const balanceTo = formatEther(
    await publicClient.getBalance({ address: addressTo })
  );

  console.log(`The balance of ${addressFrom} is: ${balanceFrom} DEV`);
  console.log(`The balance of ${addressTo} is: ${balanceTo} DEV`);
};

// 6. Call the balances function
balances();
```

To run the script and fetch the account balances, you can run the following command:

```bash
npx ts-node balances.ts
```

If successful, the balances for the origin and receiving address will be displayed in your terminal in DEV.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>npx ts-node balances.ts</span>
    <span data-ty>The balance of 0x3B939FeaD1557C741Ff06492FD0127bd287A421e is: 3601.72 DEV</span>
    <span data-ty>The balance of 0x78F34038c82638E0563b974246D421154C26b004 is: 0 DEV</span>
    <span data-ty="input"><span class="file-path"></span>
</div>
### Send Transaction Script {: #send-transaction-script }

You'll only need one file to execute a transaction between accounts. For this example, you'll be transferring 1 DEV token from an origin address (from which you hold the private key) to another address. To get started, you can create a `transaction.ts` file by running:

```bash
touch transaction.ts
```

Next, you will create the script for this file and complete the following steps:

1. Update your imports to include the `createWalletClient`, `http`, and `parseEther` functions from `viem`, the `privateKeyToAccount` function from `viem/accounts`, and the network you want to interact with from `viem/chains`
2. [Set up a viem wallet client](#for-writing-chain-data) for writing chain data, which can be used along with your private key to send transactions. **Note: This is for example purposes only. Never store your private keys in a TypeScript file**
3. [Set up a public viem client](#for-reading-chain-data) for reading chain data, which will be used to wait for the transaction receipt
4. Define the `addressTo` variable
5. Create the asynchronous `send` function, which wraps the transaction object and the `walletClient.sendTransaction` method
6. Use the `walletClient.sendTransaction` function to sign and send the transaction. You'll need to pass in the transaction object, which only requires the recipient's address and the amount to send. Note that `parseEther` can be used, which handles the necessary unit conversions from Ether to Wei, similar to using `parseUnits(value, decimals)`. Use `await` to wait until the transaction is processed and the transaction hash is returned
7. Use the `publicClient.waitForTransactionReceipt` function to wait for the transaction receipt, signaling that the transaction has been completed. This is particularly helpful if you need the transaction receipt or if you're running the `balances.ts` script directly after this one to check if the balances have been updated as expected
8. Lastly, run the `send` function

```ts
// 1. Imports
import { createPublicClient, createWalletClient, http, parseEther } from 'viem';
import { privateKeyToAccount } from 'viem/accounts';
import { moonbaseAlpha } from 'viem/chains';

// 2. Create a wallet client for writing chain data
const account = privateKeyToAccount('INSERT_PRIVATE_KEY');
const rpcUrl = 'https://rpc.api.moonbase.moonbeam.network';
const walletClient = createWalletClient({
  account,
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});

// 3. Create a public client for reading chain data
const publicClient = createPublicClient({
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});

// 4. Create to address variable
const addressTo = 'INSERT_ADDRESS';

// 5. Create send function
const send = async () => {
  console.log(
    `Attempting to send transaction from ${account.address} to ${addressTo}`
  );

  // 6. Sign and send tx
  const hash = await walletClient.sendTransaction({
    to: addressTo,
    value: parseEther('1'),
  });

  // 7. Wait for the transaction receipt
  await publicClient.waitForTransactionReceipt({
    hash,
  });

  console.log(`Transaction successful with hash: ${hash}`);
};

// 8. Call the send function
send();
```

To run the script, you can run the following command in your terminal:

```bash
npx ts-node transaction.ts
```

If the transaction was successful, in your terminal you'll see the transaction hash has been printed out.

!!! note
    Viem requires that you prepend your private key with `0x`. Many wallets omit this `0x`, so verify you've included it as you replace `INSERT_PRIVATE_KEY`.

You can also use the `balances.ts` script to check that the balances for the origin and receiving accounts have changed. The entire workflow would look like this:

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>npx ts-node balances.ts</span>
    <span data-ty>The balance of 0x3B939FeaD1557C741Ff06492FD0127bd287A421e is: 3601.72 DEV</span>
    <span data-ty>The balance of 0x78F34038c82638E0563b974246D421154C26b004 is: 0 DEV</span>
    <br>
    <span data-ty="input"><span class="file-path">npx ts-node transaction.ts</span>
    <span data-ty>Attempting to send transaction from 0x3B939FeaD1557C741Ff06492FD0127bd287A421e to 0x78F34038c82638E0563b974246D421154C26b004</span>
    <span data-ty>Transaction successful with hash: 0xc482d907b2ae4ca1202c6cc5b486694b8439a9853caad9c2cdafec39defa1968</span>
    <span data-ty="input"><span class="file-path">npx ts-node balances.ts</span>
    <span data-ty>The balance of 0x3B939FeaD1557C741Ff06492FD0127bd287A421e is: 3600.72 DEV</span>
    <span data-ty>The balance of 0x78F34038c82638E0563b974246D421154C26b004 is: 1 DEV</span>
    <span data-ty="input"><span class="file-path"></span>
</div>
## Deploy a Contract {: #deploy-contract }

The contract you'll be compiling and deploying in the next couple of sections is a simple incrementer contract, arbitrarily named `Incrementer.sol`. You can get started by creating a file for the contract:

```bash
touch Incrementer.sol
```

Next, you can add the Solidity code to the file:

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.30;

contract Incrementer {
    uint256 public number;

    constructor(uint256 _initialNumber)

    function increment(uint256 _value) public {
        number = number + _value;
    }

    function reset() public {
        number = 0;
    }
}
```

The `constructor` function, which runs when the contract is deployed, sets the initial value of the number variable stored on-chain (the default is `0`). The `increment` function adds the `_value` provided to the current number, but a transaction needs to be sent, which modifies the stored data. Lastly, the `reset` function resets the stored value to zero.

!!! note
    This contract is a simple example for illustration purposes only and does not handle values wrapping around.
### Compile Contract Script {: #compile-contract-script }

In this section, you'll create a script that uses the Solidity compiler to output the bytecode and interface (ABI) for the `Incrementer.sol` contract. To get started, you can create a `compile.ts` file by running:

```bash
touch compile.ts
```
Next, you will create the script for this file and complete the following steps:

1. Import the `fs` and `solc` packages
2. Using the `fs.readFileSync` function, you'll read and save the file contents of `Incrementer.sol` to `source`
3. Build the `input` object for the Solidity compiler by specifying the `language`, `sources`, and `settings` to be used
4. Using the `input` object, you can compile the contract using `solc.compile`
5. Extract the compiled contract file and export it to be used in the deployment script
```js
// 1. Import packages
const fs = require('fs');
const solc = require('solc');

// 2. Get path and load contract
const source = fs.readFileSync('Incrementer.sol', 'utf8');

// 3. Create input object
const input = {
   language: 'Solidity',
   sources: {
      'Incrementer.sol': {
         content: source,
      },
   },
   settings: {
      outputSelection: {
         '*': {
            '*': ['*'],
         },
      },
   },
};
// 4. Compile the contract
const tempFile = JSON.parse(solc.compile(JSON.stringify(input)));
const contractFile = tempFile.contracts['Incrementer.sol']['Incrementer'];

// 5. Export contract data
export default contractFile;
```

### Deploy Contract Script {: #deploy-contract-script }

With the script for compiling the `Incrementer.sol` contract in place, you can then use the results to send a signed transaction that deploys it. To do so, you can create a file for the deployment script called `deploy.ts`:

```bash
touch deploy.ts
```

Next, you will create the script for this file and complete the following steps:

1. Update your imports to include the `createPublicClient`, `createWalletClient`, and `http` functions from `viem`, the `privateKeyToAccount` function from `viem/accounts`, the network you want to interact with from `viem/chains`, and the `contractFile` from the `compile.ts` file you created in the [Compile Contract Script](#compile-contract-script) section
2. [Set up a viem wallet client](#for-writing-chain-data) for writing chain data, which will be used along with your private key to deploy the `Incrementer` contract. **Note: This is for example purposes only. Never store your private keys in a TypeScript file**
3. [Set up a public viem client](#for-reading-chain-data) for reading chain data, which will be used to read the transaction receipt for the deployment
4. Load the contract `bytecode` and `abi` for the compiled contract
5. Create the asynchronous `deploy` function that will be used to deploy the contract via the `walletClient.deployContract` method
6. Use the `walletClient.deployContract` function to sign and send the transaction. You'll need to pass in the contract's ABI and bytecode, the account to deploy the transaction from, and the initial value for the incrementer. Use `await` to wait until the transaction is processed and the transaction hash is returned
7. Use the `publicClient.readContract` function to get the transaction receipt for the deployment. Use `await` to wait until the transaction is processed and the contract address is returned
8. Lastly, run the `deploy` function

```ts
// 1. Update imports
import { createPublicClient, createWalletClient, http } from 'viem';
import { privateKeyToAccount } from 'viem/accounts';
import { moonbaseAlpha } from 'viem/chains';
import contractFile from './compile';

// 2. Create a wallet client for writing chain data
// The private key must be prepended with `0x` to avoid errors
const account = privateKeyToAccount('INSERT_PRIVATE_KEY');
const rpcUrl = 'https://rpc.api.moonbase.moonbeam.network';
const walletClient = createWalletClient({
  account,
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});
// 3. Create a public client for reading chain data
const publicClient = createPublicClient({
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});

// 4. Load contract information
const bytecode = contractFile.evm.bytecode.object;
const abi = contractFile.abi;
const _initialNumber = 5;

// 5. Create deploy function
const deploy = async () => {
  console.log(`Attempting to deploy from account: ${account.address}`);

  // 6. Send tx (initial value set to 5)
  const contract = await walletClient.deployContract({
    abi,
    account,
    bytecode,
    args: [_initialNumber],
  });

  // 7. Get the transaction receipt for the deployment
  const transaction = await publicClient.waitForTransactionReceipt({
    hash: contract,
  });

  console.log(`Contract deployed at address: ${transaction.contractAddress}`);
};

// 8. Call the deploy function
deploy();
```

To run the script, you can enter the following command into your terminal:

```bash
npx ts-node deploy.ts
```

If successful, the contract's address will be displayed in the terminal.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>npx ts-node deploy.ts</span>
    <span data-ty>Attempting to deploy from account: 0x3B939FeaD1557C741Ff06492FD0127bd287A421e</span>
    <span data-ty>Contract deployed at address: 0x4503b1086c6780e888194fd9caebca5f65b210c9</span>
    <span data-ty="input"><span class="file-path"></span>
</div>
### Read Contract Data (Call Methods)

Call methods are the type of interaction that doesn't modify the contract's storage (change variables), meaning no transaction needs to be sent. They simply read various storage variables of the deployed contract.

To get started, you can create a file and name it `get.ts`:

```bash
touch get.ts
```

Then you can take the following steps to create the script:

1. Update your imports to include the `createPublicClient` and `http` functions from `viem`, the network you want to interact with from `viem/chains`, and the `contractFile` from the `compile.ts` file you created in the [Compile Contract Script](#compile-contract-script) section
2. [Set up a public viem client](#for-reading-chain-data) for reading chain data, which will be used to read the current number of the `Incrementer` contract
3. Create the `contractAddress` variable using the address of the deployed contract and the `abi` variable using the `contractFile` from the `compile.ts` file
4. Create the asynchronous `get` function
5. Call the contract using the `publicClient.readContract` function, passing in the `abi`, the name of the function, the `contractAddress`, and any arguments (if needed). You can use `await`, which will return the value requested once the request promise resolves
6. Lastly, call the `get` function

```ts
// 1. Update imports
import { createPublicClient, http } from 'viem';
import { moonbaseAlpha } from 'viem/chains';
import contractFile from './compile';

// 2. Create a public client for reading chain data
const rpcUrl = 'https://rpc.api.moonbase.moonbeam.network';
const client = createPublicClient({
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});

// 3. Create contract variables
const contractAddress = 'INSERT_CONTRACT_ADDRESS';
const abi = contractFile.abi;

// 4. Create get function
const get = async () => {
  console.log(`Making a call to contract at address: ${contractAddress}`);

  // 5. Call contract
  const data = await client.readContract({
    abi,
    functionName: 'number',
    address: contractAddress,
    args: [],
  });

  console.log(`The current number stored is: ${data}`);
};

// 6. Call get function
get();
```

To run the script, you can enter the following command in your terminal:

```bash
npx ts-node get.ts
```

If successful, the value will be displayed in the terminal.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>npx ts-node get.ts</span>
    <span data-ty>Making a call to contract at address: 0x4503b1086c6780e888194fd9caebca5f65b210c9</span>
    <span data-ty>The current number stored is: 5</span>
    <span data-ty="input"><span class="file-path"></span>
</div>
### Interact with Contract (Send Methods)

Send methods are the type of interactions that modify the contract's storage (change variables), meaning a transaction needs to be signed and sent. In this section, you'll create two scripts: one to increment and one to reset the incrementer. To get started, you can create a file for each script and name them `increment.ts` and `reset.ts`:

```bash
touch increment.ts reset.ts
```

Open the `increment.ts` file and take the following steps to create the script:

1. Update your imports to include the `createWalletClient` and `http` functions from `viem`, the network you want to interact with from `viem/chains`, and the `contractFile` from the `compile.ts` file you created in the [Compile Contract Script](#compile-contract-script) section
2. [Set up a viem wallet client](#for-writing-chain-data) for writing chain data, which will be used along with your private key to send a transaction. **Note: This is for example purposes only. Never store your private keys in a TypeScript file**
3. [Set up a public viem client](#for-reading-chain-data) for reading chain data, which will be used to wait for the transaction receipt
4. Create the `contractAddress` variable using the address of the deployed contract, the `abi` variable using the `contractFile` from the `compile.ts` file, and the `_value` to increment the contract by
5. Create the asynchronous `increment` function
6. Call the contract using the `walletClient.writeContract` function, passing in the `abi`, the name of the function, the `contractAddress`, and the `_value`. You can use `await`, which will return the transaction hash once the request promise resolves
7. Use the `publicClient.waitForTransactionReceipt` function to wait for the transaction receipt, signaling that the transaction has been completed. This is particularly helpful if you need the transaction receipt or if you're running the `get.ts` script directly after this one to check that the current number has been updated as expected
8. Lastly, call the `increment` function

```js
// 1. Update imports
import { createPublicClient, createWalletClient, http } from 'viem';
import { privateKeyToAccount } from 'viem/accounts';
import { moonbaseAlpha } from 'viem/chains';
import contractFile from './compile';

// 2. Create a wallet client for writing chain data
const account = privateKeyToAccount('INSERT_PRIVATE_KEY');
const rpcUrl = 'https://rpc.api.moonbase.moonbeam.network';
const walletClient = createWalletClient({
  account,
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});

// 3. Create a public client for reading chain data
const publicClient = createPublicClient({
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});

// 4. Create contract variables
const contractAddress = 'INSERT_CONTRACT_ADDRESS';
const abi = contractFile.abi;
const _value = 3;

// 5. Create increment function
const increment = async () => {
  console.log(
    `Calling the increment by ${_value} function in contract at address: ${contractAddress}`
  );
  // 6. Call contract
  const hash = await walletClient.writeContract({
    abi,
    functionName: 'increment',
    address: contractAddress,
    args: [_value],
  });

  // 7. Wait for the transaction receipt
  await publicClient.waitForTransactionReceipt({
    hash,
  });

  console.log(`Tx successful with hash: ${hash}`);
};

// 8. Call increment function
increment();
```

To run the script, you can enter the following command in your terminal:

```bash
npx ts-node increment.ts
```

If successful, the transaction hash will be displayed in the terminal. You can use the `get.ts` script alongside the `increment.ts` script to make sure that value is changing as expected.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>npx ts-node get.ts</span>
    <span data-ty>Making a call to contract at address: 0x4503b1086c6780e888194fd9caebca5f65b210c9</span>
    <span data-ty>The current number stored is: 5</span>
    <span data-ty="input"><span class="file-path"></span>npx ts-node increment.ts</span>
    <span data-ty>Calling the increment by 3 function in contract at address: 0x4503b1086c6780e888194fd9caebca5f65b210c9</span>
    <span data-ty>Tx successful with hash: 0x041c9767e7a96f60f372341647430560569fd6ff64a27b4b9c6241e55dde57e1</span>
    <span data-ty="input"><span class="file-path"></span>npx ts-node get.ts</span>
    <span data-ty>Making a call to contract at address: 0x4503b1086c6780e888194fd9caebca5f65b210c9</span>
    <span data-ty>The current number stored is: 8</span>
    <span data-ty="input"><span class="file-path"></span>
</div>
Next, you can open the `reset.ts` file and take the following steps to create the script:

1. Update your imports to include the `createWalletClient` and `http` functions from `viem`, the network you want to interact with from `viem/chains`, and the `contractFile` from the `compile.ts` file you created in the [Compile Contract Script](#compile-contract-script) section
2. [Set up a viem wallet client](#for-writing-chain-data) for writing chain data, which will be used along with your private key to send a transaction. **Note: This is for example purposes only. Never store your private keys in a TypeScript file**
3. [Set up a public viem client](#for-reading-chain-data) for reading chain data, which will be used to wait for the transaction receipt
4. Create the `contractAddress` variable using the address of the deployed contract and the `abi` variable using the `contractFile` from the `compile.ts` file to increment the contract by
5. Create the asynchronous `reset` function
6. Call the contract using the `walletClient.writeContract` function, passing in the `abi`, the name of the function, the `contractAddress`, and an empty array for the arguments. You can use `await`, which will return the transaction hash once the request promise resolves
7. Use the `publicClient.waitForTransactionReceipt` function to wait for the transaction receipt, signaling that the transaction has been completed. This is particularly helpful if you need the transaction receipt or if you're running the `get.ts` script directly after this one to check that the current number has been reset to `0`
8. Lastly, call the `reset` function

```ts
// 1. Update imports
import { createPublicClient, createWalletClient, http } from 'viem';
import { privateKeyToAccount } from 'viem/accounts';
import { moonbaseAlpha } from 'viem/chains';
import contractFile from './compile';

// 2. Create a wallet client for writing chain data
const account = privateKeyToAccount('INSERT_PRIVATE_KEY');
const rpcUrl = 'https://rpc.api.moonbase.moonbeam.network';
const walletClient = createWalletClient({
  account,
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});

// 3. Create a public client for reading chain data
const publicClient = createPublicClient({
  chain: moonbaseAlpha,
  transport: http(rpcUrl),
});

// 4. Create contract variables
const contractAddress = 'INSERT_CONTRACT_ADDRESS';
const abi = contractFile.abi;

// 5. Create reset function
const reset = async () => {
  console.log(
    `Calling the reset function in contract at address: ${contractAddress}`
  );

  // 6. Call contract
  const hash = await walletClient.writeContract({
    abi,
    functionName: 'reset',
    address: contractAddress,
    args: [],
  });

  // 7. Wait for the transaction receipt
  await publicClient.waitForTransactionReceipt({
    hash,
  });

  console.log(`Tx successful with hash: ${hash}`);
};

// 8. Call reset function
reset();
```

To run the script, you can enter the following command in your terminal:

```bash
npx ts-node reset.ts
```

If successful, the transaction hash will be displayed in the terminal. You can use the `get.ts` script alongside the `reset.ts` script to make sure that value is changing as expected.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>npx ts-node get.ts</span>
    <span data-ty>Making a call to contract at address: 0x4503b1086c6780e888194fd9caebca5f65b210c9</span>
    <span data-ty>The current number stored is: 8</span>
    <span data-ty="input"><span class="file-path"></span>npx ts-node reset.ts</span>
    <span data-ty>Calling the reset function in contract at address: 0x4503b1086c6780e888194fd9caebca5f65b210c9</span>
    <span data-ty>Tx successful with hash: 0xc1a772131ccf6a03675ff3e88798a6e70a99e145eeb0e98170ff2e3345ee14a7</span>
    <span data-ty="input"><span class="file-path"></span>npx ts-node get.ts</span>
    <span data-ty>Making a call to contract at address: 0x4503b1086c6780e888194fd9caebca5f65b210c9</span>
    <span data-ty>The current number stored is: 0</span>
    <span data-ty="input"><span class="file-path"></span>
</div>
<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
