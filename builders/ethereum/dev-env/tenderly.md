---
title: Tenderly Development Platform
description: Learn how to use Tenderly, an Ethereum development platform, to build, debug, and monitor Solidity smart contracts on Moonbeam.
categories:
- Dev Environments
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/dev-env/tenderly/
word_count: 1717
token_estimate: 2473
version_hash: sha256:af6b2627d4535876991109d53731e4c47244d4ed4c36f3e2ca335cd852f6c074
last_updated: '2026-05-21T21:21:53+00:00'
---

# Using Tenderly on Moonbeam

## Introduction {: #introduction }

[Tenderly](https://tenderly.co) is a Web3 development platform that contains a suite of tools designed to help developers throughout the DApp development life cycle. With Tenderly, you can build, debug, test, optimize, monitor, set up alerts, and view analytics for your smart contracts on Moonbeam and Moonriver.

The Tenderly platform provides the following features:

- **[Contract Verification](https://docs.tenderly.co/contract-verification)** - as it is essential to verify your smart contracts to take full advantage of all of Tenderly's features, Tenderly provides several methods of verification. You can verify smart contracts through [the Tenderly dashboard](https://docs.tenderly.co/contract-verification/dashboard), [the Tenderly CLI and Foundry](https://docs.tenderly.co/contract-verification/foundry), or [the Tenderly Hardhat plugin](https://docs.tenderly.co/contract-verification/hardhat)

- **[Debugger](https://docs.tenderly.co/debugger)** - use the visual debugger to inspect transactions and get better insight into the behavior of your code. With the debugger, you can review a transaction's stack trace, view the calls made in a transaction, step through a contract, and review decoded inputs, outputs, and state variables. You can use the debugger on the Tenderly dashboard or the [Tenderly Debugger Chrome Extension](https://docs.tenderly.co/debugger/dev-toolkit-browser-extension)

- **[Gas Profiler](https://docs.tenderly.co/debugger/gas-profiler)** - view how much gas you're spending on a granular level, so you can optimize your smart contracts and reduce transaction gas costs

- **[Simulator](https://docs.tenderly.co/simulator-ui)** - simulate transactions in a TestNet development environment to learn how your transactions will behave without having to send them on-chain. This way, you can know the transaction's outcome and ensure it works as expected before sending it to the network. You can experiment with different parameters, simulate historical and current transactions, and edit the contract source code. You can access the simulator from the Tenderly dashboard, or you can use the [Tenderly Simulation API](https://docs.tenderly.co/reference/api#tag/Simulations) to take advantage of the simulator programmatically

- **[Virtual TestNets](https://docs.tenderly.co/virtual-testnets)** - simulate the live Moonbeam network in an isolated environment to interact with deployed contracts and real-time on-chain data. These test environments enable controlled development, testing, and debugging across smart contracts, UI, backend, and data indexing. They support sequential transaction simulations for complex scenarios. There are some limitations to be aware of when using this feature. [Moonbeam precompiled contracts](/moonbeam-mkdocs/builders/ethereum/precompiles/overview/) are not supported, as they are part of the Substrate implementation and cannot be replicated in the simulated EVM environment, prohibiting you from interacting with cross-chain assets, staking, and governance.

- **[Alerting](https://docs.tenderly.co/alerts/intro-to-alerts)** - configure real-time alerts to notify you whenever a specific event occurs, allowing you to stay informed about what's going on with your smart contracts

- **[Web3 Actions](https://docs.tenderly.co/web3-actions/intro-to-web3-actions)** - create programmable functions in JavaScript or TypeScript that are executed automatically by Tenderly when a specific smart contract or chain event occurs

!!! note
    Tenderly supports Moonbeam, Moonriver, and Moonbase Alpha, except for the Web3 Gateway. For more information, check out Tenderly's documentation on [Supported Networks](https://docs.tenderly.co/supported-networks#supported-networks).

## Getting Started

The Tenderly dashboard provides access to an all-in-one Web3 development platform. To get started with the dashboard, you'll need to [sign up](https://dashboard.tenderly.co/register) for an account. Once you've signed up, you'll be able to start exploring your Tenderly dashboard.

![Tenderly dashboard](/moonbeam-mkdocs/images/builders/ethereum/dev-env/tenderly/tenderly-1.webp)

If you prefer not to set up an account, you can also access limited features using [Tenderly's explorer](https://dashboard.tenderly.co/explorer). Without an account, you can still gain insights into contracts and transactions. However, you won't be able to simulate transactions or create Virtual TestNets.

To interact with Tenderly's features programmatically, you can check out the [Tenderly CLI](https://github.com/Tenderly/tenderly-cli) GitHub repository for more information.

The following sections will show you how to get started with Tenderly on Moonbeam. For more detailed documentation, please refer to [Tenderly's documentation site](https://docs.tenderly.co).

### Add a Contract {: #add-a-contract }

A good place to start with the Tenderly dashboard is to add a deployed smart contract. Once you've added a contract, you'll be able to create transaction simulations and Virtual TestNets, use the debugger, set up monitoring and alerts, and more.

To add a new contract, you can click on **Contracts** on the left-side panel and click **Add Contract**. A pop-up will appear, and you can take the following steps:

1. Enter the contract address
2. (Optional) You can give your contract a name
3. Choose **Moonbeam**, **Moonriver**, or **Moonbase Alpha** as the network, depending on which network you've deployed your smart contract to
4. (Optional) Toggle the **Add more** slider to add additional contracts after the initial one
5. Finally, to add the contract to the dashboard, click **Save**

![Add a contract](/moonbeam-mkdocs/images/builders/ethereum/dev-env/tenderly/tenderly-2.webp)

After a contract has been added, it will appear in the list of contracts on the **Contracts** dashboard. If the contract hasn't been verified yet, the dashboard will display an **Unverified** status along with a **Verify** button.

![Contract in list of contracts](/moonbeam-mkdocs/images/builders/ethereum/dev-env/tenderly/tenderly-3.webp)

To take full advantage of the Tenderly tool set, it is recommended that you verify your smart contracts, which you can do by clicking on **Verify**. You can choose to verify your contract by uploading the contract's JSON, ABI, or source code. For more information, please refer to Tenderly's documentation on [Smart Contract Verification](https://docs.tenderly.co/contract-verification#verifying-a-smart-contract).

### Create a Virtual TestNet {: #virtual-testnets-moonbeam }

Tenderly's Virtual TestNets feature simulates the live Moonbeam network in an isolated environment, which enables you to interact with deployed contracts and live on-chain data.

There are some limitations to be aware of when using this feature. You cannot interact with any of the [Moonbeam precompiled contracts](/moonbeam-mkdocs/builders/ethereum/precompiles/) and their functions. Precompiles are a part of the Substrate implementation and, therefore, cannot be replicated in the simulated EVM environment. This prohibits you from interacting with cross-chain assets on Moonbeam and Substrate-based functionality such as staking and governance.

Tenderly makes creating a TestNet through the dashboard quite simple. To get started, click on **Virtual TestNets** on the left-side menu and then click **Create Virtual TestNet**. From there, you can take the following steps:

1. Select **Moonbeam**, **Moonriver**, or **Moonbase Alpha** from the **Parent network** dropdown
2. (Optional) Give your TestNet a name
3. Select your **Chain ID**; you can use a custom one or the original network ID. It is recommended to set a custom Chain ID to prevent replay attacks and avoid issues when adding the Virtual TestNet to wallets
4. Choose whether to turn on or off the **Public Explorer**
5. Enable **State Sync** if you want to keep your Virtual TestNet updated in real-time with the parent network
6. To limit data, disable **Use latest block** and enter a block number, or keep it enabled to include all blocks
7. Click **Create**

![Virtual TestNet Moonbeam](/moonbeam-mkdocs/images/builders/ethereum/dev-env/tenderly/tenderly-4.webp)

Once you've created your Virtual TestNet, you can start using it by deploying a contract or creating a transaction simulation.

To deploy a contract, go to Contracts in the left menu. Use one from **Watched Contracts** or add a new one via **Watch Contract**. Once added, it will appear in **Contracts**, where you can view its details.

To create a simulation, click the **Simulation** button and enter the configurations for the simulation. For more information on simulations, please refer to Tenderly's [Simulator UI Overview](https://docs.tenderly.co/simulator-ui/using-simulation-ui) documentation.

![TestNet simulations](/moonbeam-mkdocs/images/builders/ethereum/dev-env/tenderly/tenderly-5.webp)

Now that you've learned how to get started with a few of Tenderly's features on Moonbeam, please feel free to dive in and check out the other tools available in their development platform. You can visit [Tenderly's documentation site](https://docs.tenderly.co) for more information. You can also check out Moonbeam's tutorial on [Using Tenderly to Simulate and Debug Transactions](/moonbeam-mkdocs/tutorials/eth-api/using-tenderly/).

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
