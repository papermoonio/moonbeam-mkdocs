---
title: Deploy Contracts with Hardhat
description: Learn how to use Hardhat, an Ethereum development environment, to compile, deploy, and debug Solidity smart contracts on Moonbeam.
categories:
- Dev Environments
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/dev-env/hardhat/
word_count: 4376
token_estimate: 7639
version_hash: sha256:7c77f674ed5169f93ba6f0d15b97c0931ec5ece9bda23bed69e110de61cb4ce2
last_updated: '2026-05-21T21:21:53+00:00'
---

# Using Hardhat to Deploy To Moonbeam

## Introduction {: #introduction }

[Hardhat](https://hardhat.org) is a flexible and extensible Ethereum development environment that streamlines the smart contract development process. Since Moonbeam is Ethereum-compatible, you can use Hardhat to develop and deploy smart contracts on Moonbeam.

Hardhat takes a task-based approach to development, where you can define and execute [tasks](https://hardhat.org/hardhat-runner/docs/advanced/create-task) that perform specific actions. These actions include compiling and deploying contracts, running tests, and more. Tasks are highly configurable, so you can create, customize, and execute tasks that are tailored to meet your needs.

You can also extend Hardhat's functionality through the use of [plugins](https://hardhat.org/hardhat-runner/plugins). Plugins are external extensions that integrate with Hardhat to provide additional features and tools for your workflow. For example, there are plugins for common Ethereum libraries, like [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/) and [viem](/moonbeam-mkdocs/builders/ethereum/libraries/viem/), a plugin that extends the Chai assertion library to include Ethereum-specific functionality, and more. All of these plugins can be used to extend your Hardhat project on Moonbeam.

This guide will provide a brief introduction to Hardhat and show you how to use Hardhat to compile, deploy, and debug Ethereum smart contracts on the Moonbase Alpha TestNet. This guide can also be adapted for Moonbeam, Moonriver, or a Moonbeam development node. The content below targets Hardhat 3 (current release: 3.0.17).

Please note that although Hardhat comes with a [Hardhat Network](https://hardhat.org/docs#hardhat-network) component, which provides a local development environment, you should use a [local Moonbeam development node](/moonbeam-mkdocs/builders/get-started/networks/moonbeam-dev/) instead. You can connect a Moonbeam development node to Hardhat just like you would with any other network.

## Checking Prerequisites {: #checking-prerequisites }

To get started, you will need the following:

- Have Node.js 22.10.0 or later (Hardhat 3 only supports even-numbered LTS versions) and npm
- Have [MetaMask installed](/moonbeam-mkdocs/tokens/connect/metamask/#install-the-metamask-extension) and [connected to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/#connect-metamask-to-moonbeam).
- Have an account with funds.
  You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
- 
  To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/)
## Create a Hardhat Project {: #creating-a-hardhat-project }

You will need to create a Hardhat project if you don't already have one. You can create one by completing the following steps:

1. Create a directory for your project.

    ```sh
    mkdir hardhat && cd hardhat
    ```

2. Initialize the project, which will create a `package.json` file.

    ```sh
    npm init -y
    ```

3. Install Hardhat.

    ```sh
    npm install --save-dev hardhat
    ```

4. Create a Hardhat project.

    ```sh
    npx hardhat --init
    ```

    !!! note
        `npx` is used to run executables installed locally in your project. Although Hardhat can be installed globally, installing it locally in each project is recommended so you can control the version on a project-by-project basis.


5. You'll be prompted with a series of questions to set up your project:

    - Choose **Hardhat 3 Beta (recommended for new projects)** rather than Hardhat 2.
    - Choose where to initialize the project (default is current directory).
    - Confirm converting to ESM (required for Hardhat v3).
    - Select the type of project to initialize:
        - A TypeScript Hardhat project using Node Test Runner and viem
        - A TypeScript Hardhat project using Mocha and Ethers.js

    For this example, you can choose either option based on your preference. If you choose the Mocha and Ethers.js option, you'll get a project structure with:
    
    - A sample contract in `contracts/Counter.sol`
    - A test file in `test/Counter.ts`
    - TypeScript configuration
    - Mocha and Ethers.js dependencies

    The project will be set up with all necessary dependencies and configurations for you to start developing.

<div id="termynal" data-termynal>
  <span data-ty="input"><span class="file-path"></span>npx hardhat init</span>
  <span data-ty>888&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;888</span>
  <span data-ty>888&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;888</span>
  <span data-ty>888&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;888</span>
  <span data-ty>8888888888&nbsp;&nbsp;8888b.&nbsp;&nbsp;888d888&nbsp;.d88888&nbsp;88888b.&nbsp;&nbsp;&nbsp;8888b.&nbsp;&nbsp;888888</span>
  <span data-ty>888&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"88b&nbsp;888P"&nbsp;&nbsp;d88"&nbsp;888&nbsp;888&nbsp;"88b&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"88b&nbsp;888</span>
  <span data-ty>888&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;.d888888&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;&nbsp;888&nbsp;888&nbsp;&nbsp;888&nbsp;.d888888&nbsp;888</span>
  <span data-ty>888&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;888&nbsp;&nbsp;888&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;Y88b&nbsp;888&nbsp;888&nbsp;&nbsp;888&nbsp;888&nbsp;&nbsp;888&nbsp;Y88b.</span>
  <span data-ty>888&nbsp;&nbsp;&nbsp;&nbsp;888&nbsp;"Y888888&nbsp;888&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Y88888&nbsp;888&nbsp;&nbsp;888&nbsp;"Y888888&nbsp;&nbsp;"Y888</span>
    <br>
  <span data-ty>👷 Welcome to Hardhat v3.0.17 👷‍</span>
    <br>
  <span data-ty="input" data-ty-prompt="?">&nbsp;Which version of Hardhat would you like to use? …</span>
  <span data-ty="input" data-ty-prompt="❯">&nbsp;Hardhat 3 Beta (recommended for new projects)</span>
  <span data-ty>&nbsp;&nbsp;Hardhat 2 (older version)</span>
    <br>
  <span data-ty="input" data-ty-prompt="✔">&nbsp;Where would you like to initialize the project?</span>
  <span data-ty="input" data-ty-prompt="Please provide either a relative or an absolute path:">&nbsp;.</span>
  <span data-ty="input" data-ty-prompt="✔">&nbsp;Hardhat only supports ESM projects. Would you like to change "package.json" to turn your project into ESM? (Y/n) · true</span>
  <span data-ty="input" data-ty-prompt="?">&nbsp;What type of project would you like to initialize? …</span>
  <span data-ty>&nbsp;&nbsp;A TypeScript Hardhat project using Node Test Runner and Viem</span>
  <span data-ty="input" data-ty-prompt="❯">&nbsp;A TypeScript Hardhat project using Mocha and Ethers.js</span>
</div>
## Hardhat Configuration File {: #hardhat-configuration-file }

The Hardhat configuration file is the entry point into your Hardhat project. It defines various settings and options for your Hardhat project, such as the Solidity compiler version to use and the networks you can deploy your contracts to.

If you are using JavaScript, keep `"type": "module"` in your `package.json`. A minimal `hardhat.config.js` looks like:

```js
import { defineConfig } from 'hardhat/config';

export default defineConfig({
  solidity: '0.8.28',
});
```

If you chose a TypeScript template, the file will be `hardhat.config.ts`, and the config content will be the same. For this example, you can keep the Solidity compiler version at `0.8.28`; however, if you are using a contract that requires a newer version, don't forget to update it here.

Install the plugins and libraries used in this guide if your project template did not add them:

```bash
npm install --save-dev @nomicfoundation/hardhat-ethers @nomicfoundation/hardhat-ignition-ethers @nomicfoundation/hardhat-keystore ethers
```

Next, you'll need to modify your configuration file to add the network configurations for the network you want to deploy your contract to. For Moonbeam networks, you'll need to specify the following:

- **`url`**: The [RPC endpoint](/moonbeam-mkdocs/builders/get-started/endpoints/) of the node.
- **`chainId`**: The chain ID, which is used to validate the network.
- **`accounts`**: The accounts that can be used to deploy and interact with contracts. You can either enter an array of the private keys for your accounts or use an [HD Wallet](https://github.com/ethereumbook/ethereumbook/blob/develop/src/chapter_5.md#hierarchical-deterministic-wallets-bip-32bip-44).
- **`type`**: For external RPC networks on Moonbeam, set `type: 'http'`.
- **`chainType`**: For Moonbeam networks, set `chainType: 'l1'`.

Hardhat includes an encrypted secrets manager via the `@nomicfoundation/hardhat-keystore` plugin, which keeps sensitive data out of source control. After installing and importing the plugin, set your secrets with the keystore:

=== "Moonbeam"

    ```bash
    npx hardhat keystore set MOONBEAM_RPC_URL
    npx hardhat keystore set MOONBEAM_PRIVATE_KEY
    ```

=== "Moonriver"

    ```bash
    npx hardhat keystore set MOONRIVER_RPC_URL
    npx hardhat keystore set MOONRIVER_PRIVATE_KEY
    ```

=== "Moonbase Alpha"

    ```bash
    npx hardhat keystore set MOONBASE_RPC_URL
    npx hardhat keystore set MOONBASE_PRIVATE_KEY
    ```

=== "Moonbeam Dev Node"

    ```bash
    npx hardhat keystore set DEV_RPC_URL
    npx hardhat keystore set DEV_PRIVATE_KEY
    ```

!!! warning
    The Hardhat console task does not currently prompt for keystore secrets. Use environment variables for your config variables before running `npx hardhat console`, or interact through scripts/tasks instead of the console when using the keystore.

Then, update your configuration file to use the encrypted secrets and ESM syntax:

=== "Moonbeam"

    ```js
    import hardhatEthers from '@nomicfoundation/hardhat-ethers';
    import hardhatIgnitionEthers from '@nomicfoundation/hardhat-ignition-ethers';
    import hardhatKeystore from '@nomicfoundation/hardhat-keystore';
    import { configVariable, defineConfig } from 'hardhat/config';

    export default defineConfig({
      plugins: [hardhatEthers, hardhatIgnitionEthers, hardhatKeystore],
      solidity: '0.8.28',
      networks: {
        moonbeam: {
          type: 'http',
          chainType: 'l1',
          url: configVariable('MOONBEAM_RPC_URL'),
          chainId: 1284, // (hex: 0x504),
          accounts: [configVariable('MOONBEAM_PRIVATE_KEY')],
        },
      },
    });
    ```

=== "Moonriver"

    ```js
    import hardhatEthers from '@nomicfoundation/hardhat-ethers';
    import hardhatIgnitionEthers from '@nomicfoundation/hardhat-ignition-ethers';
    import hardhatKeystore from '@nomicfoundation/hardhat-keystore';
    import { configVariable, defineConfig } from 'hardhat/config';

    export default defineConfig({
      plugins: [hardhatEthers, hardhatIgnitionEthers, hardhatKeystore],
      solidity: '0.8.28',
      networks: {
        moonriver: {
          type: 'http',
          chainType: 'l1',
          url: configVariable('MOONRIVER_RPC_URL'),
          chainId: 1285, // (hex: 0x505),
          accounts: [configVariable('MOONRIVER_PRIVATE_KEY')],
        },
      },
    });
    ```

=== "Moonbase Alpha"

    ```js
    import hardhatEthers from '@nomicfoundation/hardhat-ethers';
    import hardhatIgnitionEthers from '@nomicfoundation/hardhat-ignition-ethers';
    import hardhatKeystore from '@nomicfoundation/hardhat-keystore';
    import { configVariable, defineConfig } from 'hardhat/config';

    export default defineConfig({
      plugins: [hardhatEthers, hardhatIgnitionEthers, hardhatKeystore],
      solidity: '0.8.28',
      networks: {
        moonbase: {
          type: 'http',
          chainType: 'l1',
          url: configVariable('MOONBASE_RPC_URL'),
          chainId: 1287, // (hex: 0x507),
          accounts: [configVariable('MOONBASE_PRIVATE_KEY')],
        },
      },
    });
    ```

=== "Moonbeam Dev Node"

    ```js
    import hardhatEthers from '@nomicfoundation/hardhat-ethers';
    import hardhatIgnitionEthers from '@nomicfoundation/hardhat-ignition-ethers';
    import hardhatKeystore from '@nomicfoundation/hardhat-keystore';
    import { configVariable, defineConfig } from 'hardhat/config';

    export default defineConfig({
      plugins: [hardhatEthers, hardhatIgnitionEthers, hardhatKeystore],
      solidity: '0.8.28',
      networks: {
        dev: {
          type: 'http',
          chainType: 'l1',
          url: configVariable('DEV_RPC_URL'),
          chainId: 1281, // (hex: 0x501),
          accounts: [configVariable('DEV_PRIVATE_KEY')],
        },
      },
    });
    ```

When you run tasks that require these secrets, Hardhat will prompt you for the password to decrypt them. The secrets are only decrypted when needed, meaning you only need to enter the password if a Hardhat task uses a secret.

If you are planning on using any plugins with your project, you'll need to install the plugin and import it into your Hardhat config file (`hardhat.config.ts` or `hardhat.config.js`). Once a plugin has been imported, it becomes part of the [Hardhat Runtime Environment](https://hardhat.org/hardhat-runner/docs/advanced/hardhat-runtime-environment), and you can leverage the plugin's functionality within tasks, scripts, and more.

For more information on the available configuration options, please refer to Hardhat's documentation on [Configuration](https://hardhat.org/hardhat-runner/docs/config#networks-configuration).

## The Contract File {: #the-contract-file }

Now that you've configured your project, you can begin the development process by creating your smart contract. The contract will be a simple one that will let you store a value that can be retrieved later, called `Box`.

To add the contract, you'll take the following steps:

1. Change into the `contracts` directory.

    ```sh
    cd contracts
    ```

2. Create a `Box.sol` file.

    ```sh
    touch Box.sol
    ```

3. Open the file and add the following contract to it:

    ```solidity
    // contracts/Box.sol
    // SPDX-License-Identifier: MIT
    pragma solidity ^0.8.1;

    contract Box {
        uint256 private value;

        // Emitted when the stored value changes
        event ValueChanged(uint256 newValue);

        // Stores a new value in the contract
        function store(uint256 newValue) public {
            value = newValue;
            emit ValueChanged(newValue);
        }

        // Reads the last stored value
        function retrieve() public view returns (uint256)
    }
    ```

## Compile the Contract {: #compiling-solidity }

The next step is to compile the `Box.sol` smart contract. For this, you can use the built-in `compile` task, which will look for Solidity files in the `contracts` directory and compile them using the version and compiler settings defined in your Hardhat config file.

To use the `compile` task, all you have to do is run:

```sh
npx hardhat compile
```

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>npx hardhat compile</span>
    <br>
    <span data-ty>Compiled 2 Solidity files with solc 0.8.28 (evm target: cancun)</span>
    <br>
    <span data-ty>Compiled 1 Solidity test file with solc 0.8.28 (evm target: cancun)</span>
    <span data-ty><span class="file-path"></span></span>
</div>
After compilation, an `artifacts` directory is created that holds the bytecode and metadata of the contract, which are `.json` files. It's a good idea to add this directory to a `.gitignore` file.

If you make changes to the contract after you've compiled it, you can compile it again using the same command. Hardhat will look for any changes and recompile the contract. If no changes are found, nothing will be compiled. If needed, you can force a compilation using the `clean` task, which will clear the cache and delete the old artifacts.

## Deploy the Contract {: #deploying-the-contract }

To deploy the contract, you'll use Hardhat Ignition, a declarative framework for deploying smart contracts. Hardhat Ignition is designed to make it easy to manage recurring tasks surrounding smart contract deployment and testing. For more information, be sure to check out the [Hardhat Ignition docs](https://hardhat.org/ignition/docs/getting-started#overview). 

To set up the proper file structure for your Ignition module, create a folder named `ignition` and a subdirectory called `modules`. Then add a new file to it called `Box.js`. You can take all three of these steps with the following command:

```sh
cd ignition/modules && touch Box.js
```

Next, you can write your Hardhat Ignition module. To get started, take the following steps:

1. Import the `buildModule` function from the Hardhat Ignition module.
2. Export a module using `buildModule`.
3. Use the `getAccount` method to select the deployer account.
4. Deploy the `Box` contract.
5. Return an object from the module. This makes the `Box` contract accessible for interaction in Hardhat tests and scripts.

```js
// 1. Import the `buildModule` function from the Hardhat Ignition module
import { buildModule } from '@nomicfoundation/hardhat-ignition/modules';

// 2. Export a module using `buildModule`
// Use `export default` instead of `module.exports`
export default buildModule('BoxModule', (m) => {
  // 3. Use the `getAccount` method to select the deployer account
  const deployer = m.getAccount(0);
  
  // 4. Deploy the `Box` contract
  const box = m.contract('Box', [], {
    from: deployer, 
  });
  
  // 5. Return an object from the module
  return { box };
});
```

To run the script and deploy the `Box.sol` contract, use the following command, which requires you to specify the network name as defined in your Hardhat config file. If you don't specify a network, hardhat will deploy the contract to a local Hardhat network by default. 

```sh
npx hardhat ignition deploy ./ignition/modules/Box.js --network moonbase
```

!!! note
    If you're using another Moonbeam network, make sure that you specify the correct network. The network name needs to match the one defined in your Hardhat config file.

You'll be prompted to enter your password for the Hardhat secrets manager. Next, you'll be prompted to confirm the network you wish to deploy to. A few seconds after you confirm, the contract is deployed, and you'll see the contract address in the terminal.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span> npx hardhat ignition deploy ./ignition/modules/Box.js --network moonbase</span>
    <br>
    <span data-ty>✅ Confirm deploy to network moonbase (1287)? … yes</span>
    <span data-ty>Hardhat Ignition 🚀</span>
    <br>
    <span data-ty>Deploying [ BoxModule ]</span>
    <br>
    <span data-ty>Batch #1</span>
    <span data-ty>Executed BoxModule#Box</span>
    <br>
    <span data-ty>[ BoxModule ] successfully deployed 🚀</span>
    <br>
    <span data-ty>Deployed Addresses</span>
    <br>
    <span data-ty>BoxModule#Box - 0xfBD78CE8C9E1169851119754C4Ea2f70AB159289</span>
    <span data-ty="input"><span class="file-path"></span></span>
</div>
Congratulations, your contract is live! Save the address, as you will use it to interact with this contract instance in the next step.

## Interact with the Contract {: #interacting-with-the-contract }

You can interact with your newly deployed contract using Hardhat in two ways: run console-style commands from a helper script (recommended for Hardhat 3), or reuse that script to automate interactions via the `run` task.

### Console-Style Interaction {: #hardhat-console }

Similarly to the deployment script, you can create a lightweight helper that mirrors the console workflow, save it under `scripts`, and run it with the built-in `run` task. This approach works even when your credentials are stored in the Hardhat keystore because `network.connect()` is executed inside a normal Hardhat task (which can unlock the keystore) instead of the console, which does not have access to the Hardhat keystore.

To get started, create a `box-console.ts` file in the `scripts` directory:

```sh
cd scripts && touch box-console.ts
```

Update the script with your deployed contract address before running it. The full helper looks like this:

??? code "View the complete script"

    ```ts
    // scripts/box-console.ts
    import { network } from 'hardhat';

    const CONTRACT_ADDRESS = 'INSERT_CONTRACT_ADDRESS';
    const VALUE_TO_STORE = 5n;

    async function main()

      if (!CONTRACT_ADDRESS.startsWith('0x'))

      const { ethers } = await network.connect('moonbase');
      const [signer] = await ethers.getSigners();

      console.log(`Using signer ${signer.address}`);
      console.log(`Attaching to Box at ${CONTRACT_ADDRESS}`);

      const Box = await ethers.getContractFactory('Box');
      const box = await Box.attach(CONTRACT_ADDRESS);

      const current = (await box.retrieve()).toString();
      console.log(`Current stored value: ${current}`);

      console.log(`Calling store(${VALUE_TO_STORE})...`);
      const tx = await box.store(VALUE_TO_STORE);
      console.log(`Submitted tx ${tx.hash}, waiting for confirmation...`);
      await tx.wait();

      const updated = (await box.retrieve()).toString();
      console.log(`Updated stored value: ${updated}`);
    }

    main().catch((err) => {
      console.error(err);
      process.exitCode = 1;
    });
    ```

Replace `INSERT_CONTRACT_ADDRESS` with the address printed by Hardhat Ignition and adjust `VALUE_TO_STORE` if you want to store a different value.

### Run the Script {: #run-the-script }

Use the `run` task to execute the helper script against your deployed `Box` contract so you can verify the keystore unlock flow works and confirm the contract stores the new value on Moonbase Alpha.

```sh
npx hardhat run --network moonbase scripts/box-console.ts
```

You'll be prompted for the Hardhat keystore password (if you're using encrypted secrets), after which the script connects to Moonbase Alpha, attaches to your deployed `Box` contract, and logs the values stored before and after calling `store(5n)`. Upon running it, you should see output similar to:

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>npx hardhat run --network moonbase scripts/box-console.ts</span>
    <br>
    <span data-ty></span>
    <span data-ty>[hardhat-keystore] Enter the password: **********</span>
    <span data-ty>Using signer 0x3B939FeaD1557C741Ff06492FD0127bd287A421e</span>
    <span data-ty>Attaching to Box at INSERT_CONTRACT_ADDRESS</span>
    <span data-ty>Current stored value: 4</span>
    <span data-ty>Calling store(5)...</span>
    <span data-ty>Submitted tx 0xdb0a7bfe9caeae5fb590cde27ad156f9b2788434aa4a94b95d1c3a8ce3d58b30, waiting for confirmation...</span>
    <span data-ty>Updated stored value: 5</span>
    <span data-ty="input"><span class="file-path"></span>%</span>
</div>
The script prints the signer being used, the value stored before the transaction, the submitted transaction hash, and the updated value after calling `store(5n)`.

## Hardhat Forking {: #hardhat-forking }

You can [fork](https://hardhat.org/hardhat-network/docs/guides/forking-other-networks) any EVM-compatible chain using Hardhat, including Moonbeam. Forking simulates the live Moonbeam network locally, enabling you to interact with deployed contracts on Moonbeam in a local test environment. Since Hardhat forking is based on an EVM implementation, you can interact with the fork using standard [Ethereum JSON-RPC methods supported by Moonbeam](/moonbeam-mkdocs/builders/ethereum/json-rpc/eth-rpc/) and [Hardhat](https://hardhat.org/hardhat-network/docs/reference#json-rpc-methods-support).

There are some limitations to be aware of when using Hardhat forking. You cannot interact with any of the Moonbeam precompiled contracts or their functions. Precompiles are a part of the Substrate implementation and therefore cannot be replicated in the simulated EVM environment. This prohibits you from interacting with cross-chain assets on Moonbeam and Substrate-based functionality such as staking and governance.


### Forking Moonbeam {: #forking-moonbeam }

You can fork Moonbeam from the command line or configure your Hardhat project to always run the fork from your Hardhat config file. To fork Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).

To fork Moonbeam from the command line, you can run the following command from within your Hardhat project directory:

=== "Moonbeam"

    ```sh
    npx hardhat node --fork INSERT_RPC_API_ENDPOINT
    ```

=== "Moonriver"

    ```sh
    npx hardhat node --fork INSERT_RPC_API_ENDPOINT
    ```

=== "Moonbase Alpha"

    ```sh
    npx hardhat node --fork https://rpc.api.moonbase.moonbeam.network
    ```

If you prefer to configure your Hardhat project, you can update your Hardhat config file with the following configurations:

=== "Moonbeam"

    ```js
    ...
    networks: {
      hardhat: {
        forking: {
          url: 'INSERT_RPC_API_ENDPOINT',
        },
      },
    },
    ...
    ```

=== "Moonriver"

    ```js
    ...
    networks: {
      hardhat: {
        forking: {
          url: 'INSERT_RPC_API_ENDPOINT',
        },
      },
    },
    ...
    ```

=== "Moonbase Alpha"

    ```js
    ...
    networks: {
      hardhat: {
        forking: {
          url: 'https://rpc.api.moonbase.moonbeam.network',
        },
      },
    },
    ...
    ```

When you spin up the Hardhat fork, you'll have 20 development accounts that are pre-funded with 10,000 test tokens. The forked instance is available at `http://127.0.0.1:8545/`. The output in your terminal should resemble the following:

<div id="termynal" data-termynal>
    <span data-ty>Private Key: Oxdbda1821b80551c9d65939329250298aa3472ba22feea921c0cf5d620ea67b97</span>
    <span data-ty>Account #9: Oxa0Ee7A142d267C1f36714E4a8F75612F20a79720 (10000 ETH)</span>
    <span data-ty>Private Key: 0x2a871d0798f97d79848a013d4936a73bf4cc922c825d33c1cf7073dff6d409c6</span>
    <span data-ty>Account #10: OxBcd4042DE499D14e55001CcbB24a551F3b954096 (10000 ETH)</span>
    <span data-ty>Private Key: Oxf214f2b2cd398c806f84e317254e0f0b801d0643303237d97a22a48e01628897</span>
    <span data-ty>Account #11: 0x71bE63f3384f5fb98995898A86B02Fb2426c5788 (10000 ETH)</span>
    <span data-ty>Private Key: 0x701b615bbdfb9de65240bc28bd21bbc0d996645a3dd57e7b12bc2bdf6f192c82</span>
    <span data-ty>Account #12: OxFABBOac9d68B0B445fB7357272F202C5651694a (10000 ETH)</span>
    <span data-ty>Private Key: Oxa267530f49f8280200edf313ee7af6b827f2a8bce2897751d06a843f644967b1</span>
    <span data-ty>Account #13: 0x1CBd3b2770909D4e10f157cABC84C7264073C9Ec (10000 ETH)</span>
    <span data-ty>Private Key: 0x47c99abed3324a2707c28affff1267e45918ec8c3f20b8aa892e8b065d2942dd</span>
    <span data-ty>Account #14: OxdF3e18d64BC6A983f673Ab319CCaE4f1a5707097 (10000 ETH)</span>
    <span data-ty>Private Key: Oxc526ee95bf44d8fc405a158bb884d9d1238d990612e9f33d006bb0789009aaa</span>
    <span data-ty>Account #15: Oxcd3B766CCDd6AE721141F452C550Ca635964ce71 (10000 ETH)</span>
    <span data-ty>Private Key: 0x8166f546bab6da521a8369cab06c5d2b9e46670292d85c875ee9ec20e84ffb61</span>
    <span data-ty>Account #16: 0×2546BcD3c84621e976D8185a91A922aE77ECEc30 (10000 ETH)</span>
    <span data-ty>Private Key: Oxea6c44ac03bff858b476bba40716402b03e41b8e97e276d1baec7c37d42484a0</span>
    <span data-ty>Account #17: OxbDA5747bFD65F08deb54cb465eB87D40e51B197E (10000 ETH)</span>
    <span data-ty>Private Key: 0x689af8efa8c651a91ad287602527f3af2fe9f6501a7ac4b06166765a93e037fd</span>
    <span data-ty>Account #18: OxdD2FD4581271e230360230F9337D5c0430Bf44C0 (10000 ETH)</span>
    <span data-ty>Private Key: Oxde9be858da4a475276426320d5e9262ecfc3ba460bfac56360bfa6c4c28b4ee0</span>
    <span data-ty>Account #19: 0×8626f6940E2eb28930eFb4CeF49B2d1F2C9C1199 (10000 ETH)</span>
    <span data-ty>Private Key: Oxdf57089febbacf7ba0bc227dafbffa9fc08a93fdc68e1e42411a14efcf23656e</span>
    <span data-ty>WARNING: These accounts, and their private keys, are publicly known.<br>Any funds sent to them on Mainnet or any other live network WILL BE LOST.</span>
</div>
To verify you have forked the network, you can query the latest block number:

```sh
curl --data '{"method":"eth_blockNumber","params":[],"id":1,"jsonrpc":"2.0"}' -H "Content-Type: application/json" -X POST localhost:8545 
```

If you convert the `result` from [hex to decimal](https://www.rapidtables.com/convert/number/hex-to-decimal.html), you should get the latest block number from the time you forked the network. You can cross-reference the block number using a [block explorer](/moonbeam-mkdocs/builders/get-started/explorers/).

From here, you can deploy new contracts to your forked instance of Moonbeam or interact with contracts already deployed by creating a local instance of the deployed contract.

To interact with an already deployed contract, you can create a new script in the `scripts` directory using `ethers`. Because you'll be running it with Hardhat, you can import `ethers` directly from the Hardhat runtime without extra setup. Inside the script, you can access a live contract on the network using the following snippet:

```js
import { ethers } from 'hardhat';

async function main()

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
