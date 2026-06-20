---
title: Verify Smart Contracts with Plugins
description: Learn how to verify smart contracts on Moonbeam networks using built-in tools from Hardhat and Foundry that support Moonscan’s API.
categories:
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/verify-contracts/etherscan-plugins/
word_count: 1407
token_estimate: 2593
version_hash: sha256:42ba9a6bda588d1d5f0cfd70c4ff5d47420b79a7c57b8a227ed686c8010eb59c
last_updated: '2026-05-21T21:21:53+00:00'
---

# Verify Smart Contracts with Etherscan Plugins

## Introduction {: #introduction }

Verifying smart contracts is a great way of improving the transparency and security of contracts deployed on Moonbeam. Hardhat and Foundry integrate with Etherscan's contract verification service to automate the process of verifying contracts by locally detecting which contracts to verify and which Solidity libraries are required, if any.

The Hardhat plugin integrates seamlessly into your [Hardhat](https://hardhat.org) project. [Foundry](https://github.com/foundry-rs/foundry) also has Etherscan capabilities, but they are built into its Forge tool instead of being included in a separate plugin.

This guide will show you how to use both plugins to verify smart contracts deployed on Moonbase Alpha. This guide can also be adapted for Moonbeam and Moonriver.

## Checking Prerequisites {: #checking-prerequisites }

To follow along with this tutorial, you will need to have:

- [MetaMask installed and connected to the Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/) TestNet
- An account funded with `DEV` tokens.
 You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
- An Etherscan API key
- Git installed and configured

## Generating an Etherscan API Key {: generating-an-etherscan-api-key }

To verify contracts on Moonscan for any Moonbeam network, you’ll need an [Etherscan API key](https://docs.etherscan.io/getting-started). Because Moonscan is part of Etherscan’s ecosystem, a single key works across all supported networks.

To create an [Etherscan account](https://etherscan.io/) and generate your key, follow these steps:

1. Click **Sign In**
2. Select **Click to sign up** and then register your new account

![Sign up for Moonscan](/moonbeam-mkdocs/images/builders/ethereum/verify-contracts/etherscan-plugins/plugins-1.webp)

Once you have an account and are signed in, you will then be able to create an API key.

1. Select **API Dashboard** from the left side menu
2. To add a new key, click the **+ Add** button

![Add an API key](/moonbeam-mkdocs/images/builders/ethereum/verify-contracts/etherscan-plugins/plugins-2.webp)

You will then be prompted to enter in an **AppName** for your API key and once you enter a name and click **Continue** it will appear in your list of API keys.

## Using the Hardhat Etherscan Plugin {: #using-the-hardhat-verify-plugin }

The example in this section of the guide will be based off of the `Box.sol` contract that was created in the [Using Hardhat to Deploy To Moonbeam](/moonbeam-mkdocs/builders/ethereum/dev-env/hardhat/) guide.

To get started with the Hardhat Etherscan plugin, you will need to first install the plugin library:

```bash
npm install --save-dev @nomicfoundation/hardhat-verify
```

You can add your Etherscan API key to the `hardhat.config.js` file.

From within your Hardhat project, open your `hardhat.config.js` file. You'll need to import the `hardhat-verify` plugin, your Etherscan API key, and add the config for Etherscan:

```js
require('@nomicfoundation/hardhat-verify');

module.exports = {
  networks: {
    moonbeam: { ... },
    moonriver: { ... },
    moonbaseAlpha: { ... }
  },
  etherscan: {
    apiKey: {
      moonbeam: 'INSERT_ETHERSCAN_API_KEY',
      moonriver: 'INSERT_ETHERSCAN_API_KEY',
      moonbaseAlpha: 'INSERT_ETHERSCAN_API_KEY', 
    },
  },
};
```

To verify the contract, you will run the `verify` command and pass in the address of the deployed contract and the network where it's deployed:

```bash
npx hardhat verify --network moonbase INSERT_CONTRACT_ADDRESS
```

In your terminal you should see the source code for your contract was successfully submitted for verification. If the verification was successful, you should see **Successfully verified contract** and there will be a link to the contract code on [Moonscan for Moonbase Alpha](https://moonbase.moonscan.io).

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>npx hardhat verify --network moonbase 0x5d73ecDB4652173b881893235B64F1a0BdE22dD6</span>
    <br>
    <span data-ty>Successfully submitted source code for contract</span>
    <span data-ty>contracts/Box.sol:Box at 0x5d73ecDB4652173b881893235B64F1a0BdE22dD6</span>
    <span data-ty>for verification on the block explorer. Waiting for verification result...</span>
    <br>
    <span data-ty>Successfully verified contract Box on Etherscan.</span>
    <span data-ty>https://moonbase.moonscan.io/address/0x5d73ecDB4652173b881893235B64F1a0BdE22dD6#code</span>
     <span data-ty="input"><span class="file-path"></span></span>
</div>
If you're verifying a contract that has constructor arguments, you'll need to run the above command and add the constructor arguments used to deploy the contract at the end of the command. For example:

```bash
npx hardhat verify --network moonbase INSERT_CONTRACT_ADDRESS INSERT_CONSTRUCTOR_ARGS
```

Please refer to the [Hardhat Verify documentation](https://hardhat.org/hardhat-runner/plugins/nomicfoundation-hardhat-verify) for help with additional use cases such as:

- [complex arguments](https://hardhat.org/hardhat-runner/plugins/nomicfoundation-hardhat-verify#complex-arguments)
- [libraries with undetectable addresses](https://hardhat.org/hardhat-runner/plugins/nomicfoundation-hardhat-verify#libraries-with-undetectable-addresses)
- using [multiple API keys](https://hardhat.org/hardhat-runner/plugins/nomicfoundation-hardhat-verify#multiple-api-keys-and-alternative-block-explorers)
- using the [`verify` command programmatically](https://hardhat.org/hardhat-runner/plugins/nomicfoundation-hardhat-verify#using-programmatically)
- [determining the correct constructor arguments](https://info.etherscan.com/determine-correct-constructor-argument-during-source-code-verification-on-etherscan/)

## Using Foundry to Verify {: #using-foundry-to-verify }

The example in this section of the guide will use the `MyToken.sol` contract that was created in the [Using Foundry to Deploy to Moonbeam](/moonbeam-mkdocs/builders/ethereum/dev-env/foundry/) guide. 

In addition to the Foundry project, you will need an [Etherscan API key](https://etherscan.io/) to verify your contract. 

If you have already deployed the example contract, you can verify it with the `verify-contract` command. Before you can verify the contract, you will need to ABI-encode the constructor arguments. To do so for the example contract, you can run the following command:

```bash
cast abi-encode "constructor(uint256)" 100
```

The result should be `0x0000000000000000000000000000000000000000000000000000000000000064`. You can then verify the contract using the following command:

=== "Moonbeam"

    ```bash
    forge verify-contract --chain-id 1284 \
    YOUR_CONTRACT_ADDRESS \
    --constructor-args 0x0000000000000000000000000000000000000000000000000000000000000064 \
    src/MyToken.sol:MyToken \
    --etherscan-api-key INSERT_YOUR_ETHERSCAN_API_KEY
    ```

=== "Moonriver"

    ```bash
    forge verify-contract --chain-id 1285 \
    YOUR_CONTRACT_ADDRESS \
    --constructor-args 0x0000000000000000000000000000000000000000000000000000000000000064 \
    src/MyToken.sol:MyToken \
    --etherscan-api-key INSERT_YOUR_ETHERSCAN_API_KEY
    ```

=== "Moonbase Alpha"

    ```bash
    forge verify-contract --chain-id 1287 \
    YOUR_CONTRACT_ADDRESS \
    --constructor-args 0x0000000000000000000000000000000000000000000000000000000000000064 \
    src/MyToken.sol:MyToken \
    --etherscan-api-key INSERT_YOUR_ETHERSCAN_API_KEY
    ```

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>forge verify-contract --chain-id 1284 \</span>
    <span data-ty>YOUR_CONTRACT_ADDRESS \</span>
    <span data-ty>--constructor-args 0x0000000000000000000000000000000000000000000000000000000000000064 \</span>
    <span data-ty>src/MyToken.sol:MyToken \</span>
    <span data-ty>--etherscan-api-key INSERT_YOUR_ETHERSCAN_API_KEY</span>
    <br>
    <span data-ty>Submitting verification for [src/MyToken. sol:MyToken] Ok("0×5A05EBOA18ee616bb5dac2C4D0a48991a83533d2" ) .</span>
    <span data-ty>Submitted contract for verification:</span>
    <span data-ty>        Response:'OK'</span>
    <span data-ty>        GUID:'f7iwagu9vspdrdfirbie1wp16cmuvfk3zvcsix9ey21t3a8ttt'</span>
    <span data-ty>        URL: https: //moonbase.moonscan.io/address/0×5a05eb0a18ee616bb5dac2c4d0a48991a83533d2</span>
    <span data-ty>Waiting for verification result...</span>
    <span data-ty>Contract successfully verified.</span>
    <span data-ty="input"><span class="file-path"></span></span>
</div>
If you wanted to deploy the example contract and verify at the same time, then you would use the following command:

=== "Moonbeam"

    ```bash
    forge create --rpc-url INSERT_RPC_API_ENDPOINT \
    --constructor-args 100 \
    --etherscan-api-key INSERT_YOUR_ETHERSCAN_API_KEY \
    --verify --private-key YOUR_PRIVATE_KEY \
    src/MyToken.sol:MyToken
    ```

=== "Moonriver"

    ```bash
    forge create --rpc-url INSERT_RPC_API_ENDPOINT \
    --constructor-args 100 \
    --etherscan-api-key INSERT_YOUR_ETHERSCAN_API_KEY \
    --verify --private-key YOUR_PRIVATE_KEY \
    src/MyToken.sol:MyToken
    ```

=== "Moonbase Alpha"

    ```bash
    forge create --rpc-url https://rpc.api.moonbase.moonbeam.network \
    --constructor-args 100 \
    --etherscan-api-key INSERT_YOUR_ETHERSCAN_API_KEY \
    --verify --private-key YOUR_PRIVATE_KEY \
    src/MyToken.sol:MyToken
    ```

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>forge create --rpc-url INSERT_RPC_API_ENDPOINT \</span>
    <span data-ty>--constructor-args 100 \</span>
    <span data-ty>--etherscan-api-key INSERT_YOUR_ETHERSCAN_API_KEY \</span>
    <span data-ty>--verify --private-key YOUR_PRIVATE_KEY \</span>
    <span data-ty>src/MyToken.sol:MyToken</span>
    <br>
    <span data-ty>Compiling...</span>
    <span data-ty>No files changed, compilation skipped</span>
    <span data-ty>Deployer: 0x0394c0EdFcCA370B20622721985B577850B0eb 75</span>
    <span data-ty>Deployed to: 0d21b2653f61b5B5399A677D377D52D07C7668f67</span>
    <span data-ty>Transaction hash: 0x80fff772b930f425ed3568f0b3d8844e5297691c78807c7b393c85910b7717</span>
    <span data-ty>Starting contract verification...</span>
    <span data-ty>Waiting for etherscan to detect contract deployment...</span>
    <br>
    <span data-ty>Submitting verification for [src/MyToken.sol:MyToken]Ok("0x21b265361b5B5399A677D377D52D07C7668f67").</span>
    <span data-ty>Submitted contract for verification:</span>
    <span data-ty>        Response:'OK'</span>
    <span data-ty>        GUID:'ebbliyrquc5itkavvhvmilanzu5rdqusikImgraanepjm8gpq'</span>
    <span data-ty>        URL: https: //moonbase.moonscan.io/address/0x21b2653f61b55399a677d377d52d07c7668f67</span>
    <span data-ty>Waiting for verification result...</span>
    <span data-ty>Contract successfully verified.</span>
    <span data-ty="input"><span class="file-path"></span></span>
</div>
