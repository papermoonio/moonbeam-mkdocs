---
title: Author Mapping Precompile
description: A guide for collators to learn how to use the Author Mapping Solidity interface to map session keys to a Moonbeam address where block rewards are paid out. 
categories:
- Node Operators and Collators
url: https://docs.moonbeam.network/node-operators/networks/collators/author-mapping/
word_count: 1931
token_estimate: 3317
version_hash: sha256:f8d062373badb8fcd15ab6cc6f1a56673cf017025f556c11d6f4bb9b488b0c71
last_updated: '2026-05-21T21:21:53+00:00'
---

# Interacting with the Author Mapping Precompile

## Introduction {: #introduction }

The author mapping precompiled contract on Moonbeam allows collator candidates to map session keys to a Moonbeam address where block rewards are paid out, through a familiar and easy-to-use Solidity interface. This enables candidates to complete author mapping with a Ledger or any other Ethereum wallet compatible with Moonbeam. However, it is recommended to generate your keys on an air-gapped machine. You can find out more information by referring to the [account requirements section of the Collator Requirements page](/moonbeam-mkdocs/node-operators/networks/collators/requirements/#account-requirements).

To become a collator candidate, you must be [running a collator node](/moonbeam-mkdocs/node-operators/networks/run-a-node/overview/). You'll also need to [join the candidate pool](/moonbeam-mkdocs/node-operators/networks/collators/activities/#become-a-candidate) fully sync your node and submit the required [bonds](#bonds) before generating your session keys and mapping them to your account. There is an [additional bond](#bonds) that must be paid when mapping your session keys.

The precompile is located at the following address:

=== "Moonbeam"

     ```text
     0x0000000000000000000000000000000000000807
     ```

=== "Moonriver"

     ```text
     0x0000000000000000000000000000000000000807
     ```

=== "Moonbase Alpha"

     ```text
     0x0000000000000000000000000000000000000807
     ```

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## The Author Mapping Solidity Interface {: #the-solidity-interface }

[`AuthorMappingInterface.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/author-mapping/AuthorMappingInterface.sol) is a Solidity interface that allows developers to interact with the precompile's methods.

- **removeKeys**() - removes the author ID and session keys. Replaces the deprecated `clearAssociation` extrinsic
- **setKeys**(*bytes memory* keys) — accepts the result of calling `author_rotateKeys`, which is the concatenated public keys of your Nimbus and VRF keys, and sets the author ID and the session keys at once. Useful after a key rotation or migration. Calling `setKeys` requires a [bond](#bonds). Replaces the deprecated `addAssociation` and `updateAssociation` extrinsics
- **nimbusIdOf**(*address* who) - retrieves the Nimbus ID of the given address. If no Nimbus ID exists for the given address, it returns `0`
- **addressOf**(*bytes32* nimbusId) - retrieves the address associated to a given Nimbus ID. If the Nimbus ID is unknown, it returns `0`
- **keysOf**(*bytes32* nimbusId) - retrieves the keys associated to the given Nimbus ID. If the Nimbus ID is unknown, it returns empty bytes

## Required Bonds {: #bonds }

To follow along with this tutorial, you'll need to join the candidate pool and map your session keys to your H160 Ethereum-style account. Two bonds are required to perform both of these actions.

The minimum bond to join the candidate pool is set as follows:

=== "Moonbeam"

    ```text
    100000 GLMR
    ```

=== "Moonriver"

    ```text
    500 MOVR
    ```

=== "Moonbase Alpha"

    ```text
    500 DEV
    ```

There is a bond that is sent when mapping your session keys with your account. This bond is per session keys registered. The bond set is as follows:

=== "Moonbeam"

    ```text
    10000 GLMR
    ```
  
=== "Moonriver"

    ```text
    100 MOVR
    ```

=== "Moonbase Alpha"

    ```text
    100 DEV
    ```

## Interact with the Solidity Interface {: #interact-with-the-solidity-interface }

### Checking Prerequisites {: #checking-prerequisites }

The below example is demonstrated on Moonbase Alpha, however, similar steps can be taken for Moonbeam and Moonriver. You should:  

 - Have MetaMask installed and [connected to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/)
 - Have an account with DEV tokens. You should have enough to cover the [candidate and mapping bonds](#bonds) plus gas fees to send the transaction and map your session keys to your account. To get enough DEV tokens to follow along with this guide, you can contact a moderator directly via the [Moonbeam Discord server](https://discord.com/invite/PfpUATX)
 - Make sure you're [running a collator node](/moonbeam-mkdocs/node-operators/networks/run-a-node/overview/) and it's fully synced
 - Make sure you've [joined the candidate pool](/moonbeam-mkdocs/node-operators/networks/collators/activities/#become-a-candidate)

As previously mentioned, you can use a Ledger by connecting it to MetaMask. Please refer to the [Ledger](/moonbeam-mkdocs/tokens/connect/ledger/) guide to import your Ledger to MetaMask. Note that Ledger is not recommended for production use. For more information, see the [account requirements in the Collator Requirements](/moonbeam-mkdocs/node-operators/networks/collators/requirements/#account-requirements).

### Generate Session Keys {: #generate-session-keys }

To match the Substrate standard, Moonbeam collator's session keys are [SR25519](https://wiki.polkadot.com/learn/learn-cryptography/#what-is-sr25519-and-where-did-it-come-from). This guide will show you how you can create/rotate your session keys associated with your collator node.

First, make sure you're [running a collator node](/moonbeam-mkdocs/node-operators/networks/run-a-node/overview/). Once you have your collator node running, your terminal should print similar logs:

<div id="termynal" data-termynal>
    <span data-ty>2025-02-25 20:00:52 [Relaychain] 💤 Idle (6 peers), best: #12706 (0x1d51.3042), finalized #12704 (0xf74b.aa44), 1 0.4kiB/s 1 0.6kiB/s</span>
    <span data-ty>2025-02-25 20:00:52 💤 Idle (6 peers), best: #5751 (Oxc5alesb5), finalized #5750 (0x9dc..e bad), 1 9.6kiB/s 1 3.5kiB/s</span>
    <span data-ty>2025-02-25 20:00:53 [Relaychain] ✨ Imported #12707 (0x77ea.4299)</span>
    <span data-ty>2025-02-25 20:00:57 [Relaychain] 💤 Idle (6 peers), best: #12707 (0x77ea..4299), finalized #12704 (0xf74b..aa44), | 16.4kiB/s 1 12.2kiB/s</span>
    <span data-ty>2025-02-25 20:00:57 💤 Idle (6 peers), best: #5751 (0xc5a1e8b5), finalized #5750 (0x9fdc...e bad), 1 1.6kiB/s 1 0.4kiB/s</span>
    <span data-ty>2025-02-25 20:00:59 [Relaychain] ✨ Imported #12708 (0x009f...3bbf)</span>
    <span data-ty>2025-02-25 20:01:00 ✨ Imported #5753 (0x8981.6c81)</span>
    <span data-ty>2025-02-25 20:01:00 ✨ Imported #5753 (0x33a...b5e3)</span>
    <span data-ty>2025-02-25 20:01:02 [Relaychain] 💤 Idle (6 peers), best: #12708 (0x009f...3bbf), finalized #12706 (0x1d51.3042), 1 1.5kiB/s 1 1.3kiB/s</span>
    <span data-ty>2025-02-25 20:01:02 💤 Idle (6 peers), best: #5752 (0x7036.569e), finalized #5751 (0xc5a1..e8b5), 1 3.3kiB/s 1 5.8kiB/s</span>
    <span data-ty>2025-02-25 20:01:05 [Relaychain] ✨ Imported #12709 (0x76b9...bf65)</span>
    <span data-ty>2025-02-25 20:01:07 [Relaychain] 💤 Idle (6 peers), best: #12709 (0x76b9..bf65), finalized #12706 (0x1d51.3042), | 2.0kiB/s | 0.9kiB/s</span>
    <span data-ty>2025-02-25 20:01:07 💤 Idle (6 peers), best: #5752 (0x7036.569e), finalized #5751 (0xc5a1..e8b5), 1 0 1 0</span>
</div>

Next, session keys can be created/rotated by sending an RPC call to the HTTP endpoint with the `author_rotateKeys` method. When you call `author_rotateKeys`, the result is the size of two keys. The response will contain a concatenated Nimbus ID and VRF key. The Nimbus ID will be used to sign blocks and the [VRF](https://wiki.polkadot.com/general/web3-and-polkadot/#vrf) key is required for block production. The concatenated keys will be used to create an association to your H160 account for block rewards to be paid out.

For reference, if your collator's HTTP endpoint is at port `9944`, the JSON-RPC call might look like this:

```bash
curl http://127.0.0.1:9944 -H \
"Content-Type:application/json;charset=utf-8" -d \
  '{
    "jsonrpc":"2.0",
    "id":1,
    "method":"author_rotateKeys",
    "params": []
  }'
```

The collator node should respond with the concatenated public keys of your new session keys. The first 64 hexadecimal characters after the `0x` prefix represent your Nimbus ID and the last 64 hexadecimal characters are the public key of your VRF session key. You'll use the concatenated public keys when mapping your Nimbus ID and setting the session keys in the next section.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>curl http://127.0.0.1:9933-H\ "Content-Type: application/json;charset=utf-8" -d \</span>
    <span data-ty>'{</span>
    <span data-ty>"jsonrpc": "2.0",</span>
    <span data-ty>"id" :1,</span>
    <span data-ty>"method": "author_rotatekeys",</span>
    <span data-ty>"params": []</span>
    <span data-ty>}'</span>
    <span data-ty>{"jsonrpc": "2.0", "result":"0x72c7ca7ef0794103caeb520806576b52cb085f7577cc12cd36c2d64dbf73757a789407ec0f401a8792ac57c4fb7dabd4da6cc74d9ac9b8dd8c4faf770255403f", "id" :1}</span>
    <span data-ty="input"><span class="file-path"></span></span>
</div>

Make sure you write down the concatenated public keys. Each of your servers, your primary and backup, should have their own unique keys. Since the keys never leave your servers, you can consider them a unique ID for that server.

Next, you'll need to register your session keys and map them to an H160 Ethereum-styled address to which the block rewards are paid.
### Remix Set Up {: #remix-set-up }

To get started, get a copy of [`AuthorMappingInterface.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/author-mapping/AuthorMappingInterface.sol) and take the following steps:

1. Click on the **File explorer** tab
2. Copy and paste the file contents into a [Remix file](https://remix.ethereum.org) named `AuthorMappingInterface.sol`

![Copying and Pasting the Author Mapping Interface into Remix](/moonbeam-mkdocs/images/node-operators/networks/collators/author-mapping/author-mapping-1.webp)

### Compile the Contract {: #compile-the-contract }

1. Click on the **Compile** tab, second from top
2. Then to compile the interface, click on **Compile AuthorMappingInterface.sol**

![Compiling AuthorMappingInterface.sol](/moonbeam-mkdocs/images/node-operators/networks/collators/author-mapping/author-mapping-2.webp)

### Access the Contract {: #access-the-contract }

1. Click on the **Deploy and Run** tab, directly below the **Compile** tab in Remix. Note: you are not deploying a contract here, instead you are accessing a precompiled contract that is already deployed
2. Make sure **Injected Provider - Metamask** is selected in the **ENVIRONMENT** drop down
3. Ensure **AuthorMappingInterface.sol** is selected in the **CONTRACT** dropdown. Since this is a precompiled contract there is no need to deploy, instead you are going to provide the address of the precompile in the **At Address** field
4. Provide the address of the author mapping precompile for Moonbase Alpha: `0x0000000000000000000000000000000000000807` and click **At Address**

![Provide the address](/moonbeam-mkdocs/images/node-operators/networks/collators/author-mapping/author-mapping-3.webp)

The author mapping precompile will appear in the list of **Deployed Contracts**.

### Map Session Keys {: #map-session-keys }

The next step is to map your session keys to your H160 account (an Ethereum-style address). Make sure you hold the private keys to this account, as this is where the block rewards are paid out to.

To map your session keys to your account, you need to be inside the [candidate pool](/moonbeam-mkdocs/node-operators/networks/collators/activities/#become-a-candidate). Once you are a candidate, you need to send a mapping extrinsic. Note that this will bond tokens per author ID registered.

Before getting started, ensure you're connected to the account that you want to map your session keys to. This will be the account where you will receive block rewards.

1. Expand the **AUTHORMAPPING** contract
2. Expand the **setKeys** method
3. Enter your session keys
4. Click **transact**
5. Confirm the MetaMask transaction that appears by clicking **Confirm**

![Map your session keys](/moonbeam-mkdocs/images/node-operators/networks/collators/author-mapping/author-mapping-4.webp)

To verify you have mapped your session keys successfully, you can use either the `mappingWithDeposit` method or the `nimbusLookup` method of the [author mapping pallet](/moonbeam-mkdocs/node-operators/networks/collators/account-management/#author-mapping-interface). To do so, please refer to the [Check Mappings section of the Collator Account Management guide](/moonbeam-mkdocs/node-operators/networks/collators/account-management/#check-the-mappings).
