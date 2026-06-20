---
title: Preimage Precompile Contract
description: Learn how to take the first necessary step to submit a proposal on-chain by submitting a preimage that contains the action to be carried out in the proposal.
categories:
- Precompiles
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/precompiles/features/governance/preimage/
word_count: 1293
token_estimate: 2022
version_hash: sha256:168d07e3f198bcdae9c6fa40c45d90bbfac7376806ba6ef7990d487ff0b0430e
last_updated: '2026-05-21T21:21:53+00:00'
---

# Interacting with the Preimage Precompile

## Introduction {: #introduction }

As a Polkadot parachain and decentralized network, Moonbeam features native on-chain governance that enables stakeholders to participate in the direction of the network. With the introduction of OpenGov, also referred to as Governance v2, the Preimage Pallet allows token holders to take the first step towards creating a proposal by submitting the preimage, which is the action to be carried out in the proposal, on-chain. The hash of the preimage is required to submit the proposal. To learn more about Moonbeam's governance system, such as an overview of related terminology, the roadmap of a proposal, and more, please refer to the [Governance on Moonbeam](/moonbeam-mkdocs/learn/features/governance/) page.

The Preimage Precompile interacts directly with Substrate's Preimage Pallet. This pallet is coded in Rust and is normally not accessible from the Ethereum side of Moonbeam. However, the Preimage Precompile allows you to access functions needed to create and manage preimages, all of which are part of the Substrate Preimage Pallet, directly from a Solidity interface.

The Preimage Precompile is located at the following address:

=== "Moonbeam"

     ```text
     0x0000000000000000000000000000000000000813
     ```

=== "Moonriver"

     ```text
     0x0000000000000000000000000000000000000813
     ```

=== "Moonbase Alpha"

     ```text
     0x0000000000000000000000000000000000000813
     ```

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## The Preimage Solidity Interface {: #the-preimage-solidity-interface }

[`Preimage.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/preimage/Preimage.sol) is a Solidity interface that allows developers to interact with the precompile's two methods:

??? function "**notePreimage**(*bytes memory* encodedProposal) - registers a preimage on-chain for an upcoming proposal. This doesn't require the proposal to be in the dispatch queue but does require a deposit which is returned once enacted."

    === "Parameters"

        - `encodedProposal` - bytes memory containing the encoded proposal to be registered. Returns the preimage hash

??? function "**unnotePreimage**(*bytes32* hash) - clears an unrequested preimage from storage."

    === "Parameters"

        - `hash` - bytes32 hash of the preimage to be removed from storage

The interface also includes the following events:

- **PreimageNoted**(*bytes32* hash) - emitted when a preimage was registered on-chain
- **PreimageUnnoted**(*bytes32* hash) - emitted when a preimage was un-registered on-chain

## Interact with the Solidity Interface {: #interact-with-the-solidity-interface }

### Checking Prerequisites {: #checking-prerequisites }

The below example is demonstrated on Moonbase Alpha, however, similar steps can be taken for Moonriver. To follow the steps in this guide, you'll need to have the following:

 - MetaMask installed and [connected to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/)
 - An account with some DEV tokens.
 You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
### Remix Set Up {: #remix-set-up }

1. Click on the **File explorer** tab
2. Paste a copy of [`Preimage.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/preimage/Preimage.sol) into a [Remix file](https://remix.ethereum.org) named `Preimage.sol`

![Copy and paste the referenda Solidity interface into Remix.](/moonbeam-mkdocs/images/builders/ethereum/precompiles/features/governance/preimage/preimage-1.webp)

### Compile the Contract {: #compile-the-contract }

1. Click on the **Compile** tab, second from top
2. Then to compile the interface, click on **Compile Preimage.sol**

![Compile the Preimage.sol interface using Remix.](/moonbeam-mkdocs/images/builders/ethereum/precompiles/features/governance/preimage/preimage-2.webp)

### Access the Contract {: #access-the-contract }

1. Click on the **Deploy and Run** tab, directly below the **Compile** tab in Remix. Note: you are not deploying a contract here, instead you are accessing a precompiled contract that is already deployed
2. Make sure **Injected Provider - Metamask** is selected in the **ENVIRONMENT** drop down
3. Ensure **Preimage.sol** is selected in the **CONTRACT** dropdown. Since this is a precompiled contract there is no need to deploy, instead you are going to provide the address of the precompile in the **At Address** field
4. Provide the address of the Preimage Precompile for Moonbase Alpha: `0x0000000000000000000000000000000000000813` and click **At Address**
5. The Preimage Precompile will appear in the list of **Deployed Contracts**

![Access the Preimage.sol interface by providing the precompile's address.](/moonbeam-mkdocs/images/builders/ethereum/precompiles/features/governance/preimage/preimage-3.webp)

### Submit a Preimage of a Proposal {: #submit-a-preimage }

In order to submit a proposal, you'll first need to submit a preimage of that proposal, which essentially defines the proposed action on-chain. You can submit the preimage using the `notePreimage` function of the Preimage Precompile. The `notePreimage` function accepts the encoded proposal, so the first step you'll need to take is to get the encoded proposal, which can easily be done using Polkadot.js Apps.

In this section, you'll get the preimage hash and the encoded proposal data for a proposal. To get the preimage hash, you'll first need to navigate to the **Preimage** page of [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network%2Fpublic-ws#):

 1. Navigate to the [**Governance** tab](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network%2Fpublic-ws#/democracy)
 2. Select **Preimages** from the dropdown
 3. From the **Preimages** page, click on **+ Add preimage**

![Add a new preimage](/moonbeam-mkdocs/images/builders/ethereum/precompiles/features/governance/preimage/preimage-4.webp)

Then take the following steps:

 1. Select an account (any account is fine because you're not submitting any transaction here)
 2. Choose the pallet you want to interact with and the dispatchable function (or action) to propose. The action you choose will determine the fields that need to fill in the following steps. In this example, it is the **system** pallet and the **remark** function
 3. Enter the text of the remark, ensuring it is unique. Duplicate proposals such as "Hello World!" will not be accepted
 4. Click the **Submit preimage** button but don't sign or confirm the transaction on the next page 

![Get the proposal hash](/moonbeam-mkdocs/images/builders/ethereum/precompiles/features/governance/preimage/preimage-5.webp)

On the next screen, take the following steps:

 1. Press the triangle icon to reveal the encoded proposal in bytes
 2. Copy the **bytes** (encoded proposal) — you'll need them when calling the `notePreimage` function

![Get the encoded proposal](/moonbeam-mkdocs/images/builders/ethereum/precompiles/features/governance/preimage/preimage-6.webp)

!!! note
     You should NOT sign and submit the transaction here. You will submit this information via the `notePreimage` function in the next step.

Now you can take the **bytes** of the encoded proposal that you got from [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network%2Fpublic-ws#/democracy) and submit it via the `notePreimage` function of the Preimage Precompile. To submit the preimage via the `notePreimage` function, take the following steps:

1. Expand the Preimage Precompile contract to see the available functions
2. Find the **notePreimage** function and press the button to expand the section
3. Provide the **bytes** of the encoded proposal that you noted in the prior section. Note, the encoded proposal is not the same as the preimage hash. Ensure you are entering the correct value into this field
4. Press **transact** and confirm the transaction in MetaMask

![Submit the preimage using the notePreimage function of the Preimage Precompile.](/moonbeam-mkdocs/images/builders/ethereum/precompiles/features/governance/preimage/preimage-7.webp)

Now that you've submitted the preimage for your proposal your proposal can be submitted! Head over to the [Referenda Precompile documentation](/moonbeam-mkdocs/builders/ethereum/precompiles/features/governance/referenda/) to learn how to submit your proposal.

If you wish to remove a preimage, you can follow the same steps noted above except use the `unnotePreimage` function and pass in the preimage hash instead of the encoded proposal.
