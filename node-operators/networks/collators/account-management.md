---
title: Collator Account Management
description: Learn how to manage your collator account, including generating session keys, mapping Nimbus IDs, setting an identity, and creating proxy accounts.
categories:
- Node Operators and Collators
url: https://docs.moonbeam.network/node-operators/networks/collators/account-management/
word_count: 2606
token_estimate: 4257
version_hash: sha256:668cc2f55128e4151f00f1874098d908f8a99a6d75e9cc17a9fbdb7b0db15ebe
last_updated: '2026-05-21T21:21:53+00:00'
---

# Collator Account Management

## Introduction {: #introduction }

When running a collator node on Moonbeam-based networks, there are some account management activities that you will need to be aware of. First and foremost you will need to create [session keys](https://wiki.polkadot.com/learn/learn-cryptography/#session-keys) for your primary and backup servers which will be used to determine block production and sign blocks.

In addition, there are some optional account management activities that you can consider such as setting an on-chain identity or setting up proxy accounts.

This guide will cover how to manage your collator account including generating and rotating your session keys, registering and updating your session keys, setting an identity, and creating proxy accounts.

## Process to Add and Update Session Keys {: #process }

The process for adding your session keys for the first time is the same as it would be for rotating your session keys. The process to create/rotate session keys is as follows:

1. [Generate session keys](#session-keys) using the `author_rotateKeys` RPC method. The response to calling this method will be a 128 hexadecimal character string containing a Nimbus ID and the public key of a VRF session key
2. [Join the candidate pool](/moonbeam-mkdocs/node-operators/networks/collators/activities/#become-a-candidate) if you haven't already
3. [Map the session keys](#mapping-extrinsic) to your candidate account using the [Author Mapping Pallet](#author-mapping-interface)'s `setKeys(keys)` extrinsic, which accepts the entire 128 hexadecimal character string as the input. When you call `setKeys` for the first time, you'll be required to submit a [mapping bond](#mapping-bonds). If you're rotating your keys and you've previously submitted a mapping bond, no new bond is required

Each step of the process is outlined in the following sections.

## Generate Session Keys {: #session-keys }

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
## Manage Session Keys {: #manage-session-keys }

Once you've created or rotated your session keys, you'll be able to manage your session keys using the extrinsics in the Author Mapping Pallet. You can map your session keys, verify the on-chain mappings, and remove session keys.

### Author Mapping Pallet Interface {: #author-mapping-interface }

The `authorMapping` module has the following extrinsics:

 - **setKeys**(keys) — accepts the result of calling `author_rotateKeys`, which is the concatenated public keys of your Nimbus and VRF keys, and sets the session keys at once. Useful after a key rotation or migration. Calling `setKeys` requires a [bond](#mapping-bonds). Replaces the deprecated `addAssociation` and `updateAssociation` extrinsics
- **removeKeys**() - removes the session keys. This is only required if you intend to stop collating and leave the candidate pool. Replaces the deprecated `clearAssociation` extrinsic

The module also adds the following RPC calls (chain state):

- **mappingWithDeposit**(NimbusPrimitivesNimbusCryptoPublic | string | Uint8Array) — displays all mappings stored on-chain, or only that related to the Nimbus ID if provided
- **nimbusLookup**(AccountId20) - displays a reverse mapping of account IDs to Nimbus IDs for all collators or for a given collator address

### Map Session Keys {: #mapping-extrinsic }

With your newly generated session keys in hand, the next step is to map your session keys to your H160 account (an Ethereum-style address). Make sure you hold the private keys to this account, as this is where the block rewards are paid out to.

To map your session keys to your account, you need to be inside the [candidate pool](/moonbeam-mkdocs/node-operators/networks/collators/activities/#become-a-candidate). Once you are a candidate, you need to send a mapping extrinsic, which requires a mapping bond.

#### Mapping Bonds {: #mapping-bonds }

The mapping bond is per session keys registered. The bond for mapping your session keys to your account is as follows:

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

#### Use Polkadot.js Apps to Map Session Keys {: #use-polkadotjs-apps }

In this section, you'll learn how to map session keys from Polkadot.js Apps. To learn how to create the mapping through the author mapping precompiled contract, you can refer to the page on [Interacting with the Author Mapping Precompile](/moonbeam-mkdocs/node-operators/networks/collators/author-mapping/).

To create the mapping from [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#assets) (make sure you're connected to the correct network), click on **Developer** at the top of the page, choose the **Extrinsics** option from the dropdown, and take the following steps:

 1. Choose the account that you want to map your author ID to be associated with, from which you'll sign this transaction
 2. Select the **authorMapping** extrinsic
 3. Set the method to **setKeys()**
 4. Enter the **keys**. It is the response obtained via the RPC call `author_rotateKeys` in the previous section, which is the concatenated public keys of your Nimbus ID and VRF key
 5. Click on **Submit Transaction**

![Author ID Mapping to Account Extrinsic](/moonbeam-mkdocs/images/node-operators/networks/collators/account-management/account-1.webp)

!!! note
    If you receive the following error, you may need to try rotating and mapping your keys again: `VRF PreDigest was not included in the digests (check rand key is in keystore)`.

If the transaction is successful, you will see a confirmation notification on your screen. If not, make sure you've [joined the candidate pool](/moonbeam-mkdocs/node-operators/networks/collators/activities/#become-a-candidate).

### Check Mappings {: #checking-the-mappings }

You can check the current on-chain mappings by verifying the chain state. You can do this one of two ways: via the `mappingWithDeposit` method or the `nimbusLookup` method. Both methods can be used to query the on-chain data for all of the collators or for a specific collator.

You can check the current on-chain mappings for a specific collator or you can also check all of the mappings stored on-chain.

#### Using the Mapping with Deposit Method {: #using-mapping-with-deposit }

To use the `mappingWithDeposit` method to check the mapping for a specific collator, you'll need to get the Nimbus ID. To do so, you can take the first 64 hexadecimal characters of the concatenated public keys to get the Nimbus ID. To verify that the Nimbus ID is correct, you can run the following command with the first 64 characters passed into the `params` array:

```bash
curl http://127.0.0.1:9944 -H "Content-Type:application/json;charset=utf-8" -d   '{
  "jsonrpc":"2.0",
  "id":1,
  "method":"author_hasKey",
  "params": ["72c7ca7ef07941a3caeb520806576b52cb085f7577cc12cd36c2d64dbf73757a", "nmbs"]
}'
```

If it's correct the response should return `"result": true`.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>curl http://127.0.0.1:9933 -H "Content-Type:application/json;char set=utf-8" -d '{</span>
    <span data-ty>"jsonrpc":"2.0"</span>
    <span data-ty>"id" :1,</span>
    <span data-ty>"method": "author_hasKey",</span>
    <span data-ty>"params": ["72c7ca7ef07941a3caeb520806576b52cb085f7577c12c36c2d64dbf73757a", "nmbs"]</span>
    <span data-ty>}'</span>
    <span data-ty>{"jsonrpc":"2.0", "result" :true, "id" :1}</span>
    <span data-ty="input"><span class="file-path"></span></span>
</div>
From [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#assets), click on **Developer** at the top of the page, then choose **Chain State** from the dropdown, and take the following steps:

 1. Choose **authorMapping** as the state to query
 2. Select the **mappingWithDeposit** method
 3. Provide a Nimbus ID to query. Optionally, you can disable the slider to retrieve all mappings 
 4. Click on the **+** button to send the RPC call

![Nimbus ID Mapping Chain State](/moonbeam-mkdocs/images/node-operators/networks/collators/account-management/account-2.webp)

You should be able to see the H160 account associated with the Nimbus ID provided and the deposit paid. If no Nimbus ID was included, this would return all the mappings stored on-chain.

#### Using the Nimbus Lookup Method {: #using-nimbus-lookup }

To use the `nimbusLookup` method to check the mapping for a specific collator, you'll need the collator's address. If you do not pass an argument to the method, you can retrieve all of the on-chain mappings.

From [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#assets), click on **Developer** at the top of the page, then choose **Chain State** from the dropdown, and take the following steps:

 1. Choose **authorMapping** as the state to query
 2. Select the **nimbusLookup** method
 3. Provide a collator's address to query. Optionally, you can disable the slider to retrieve all mappings
 4. Click on the **+** button to send the RPC call

![Nimbus ID Mapping Chain State](/moonbeam-mkdocs/images/node-operators/networks/collators/account-management/account-3.webp)

You should be able to see the nimbus ID associated with the H160 account provided. If no account was provided, this would return all the mappings stored on-chain.

### Remove Session Keys {: #removing-session-keys }

Before removing your session keys, you'll want to make sure that you've stopped collating and left the candidate pool. To stop collating, you'll need to schedule a request to leave the candidate pool, wait a delay period, and then execute the request. For step-by-step instructions, please refer to the [Stop Collating](/moonbeam-mkdocs/node-operators/networks/collators/activities/#stop-collating) section of the Moonbeam Collator Activities page.

Once you have left the candidate pool, you can remove your session keys. After which, the mapping bond you deposited will be returned to your account.

From [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network#assets), click on **Developer** at the top of the page, then choose **Extrinsics** from the dropdown, and take the following steps:

1. Select your account
2. Choose the **authorMapping** pallet and the **removeKeys** extrinsic
3. Click **Submit Transaction**

![Remove session keys on Polkadot.js Apps](/moonbeam-mkdocs/images/node-operators/networks/collators/account-management/account-4.webp)

Once the transaction goes through, the mapping bond will be returned to you. To make sure that the keys were removed, you can follow the steps in the [Check Mappings](#checking-the-mappings) section.

## Setting an Identity {: #setting-an-identity }

Setting an on-chain identity enables your collator node to be easily identifiable. As opposed to showing your account address, your chosen display name will be displayed instead.

There are a couple of ways you can set your identity, to learn how to set an identity for your collator node please check out the [Managing your Account Identity](/moonbeam-mkdocs/tokens/manage/identity/) page of our documentation.

## Proxy Accounts {: #proxy-accounts }

Proxy accounts are accounts that can be enabled to perform a limited number of actions on your behalf. Proxies allow users to keep a primary account securely in cold storage while using the proxy to actively participate in the network on behalf of the primary account. You can remove authorization of the proxy account at any time. As an additional layer of security, you can setup your proxy with a delay period. This delay period would provide you time to review the transaction, and cancel if needed, before it automatically gets executed.

To learn how to setup a proxy account, please refer to the [Setting up a Proxy Account](/moonbeam-mkdocs/tokens/manage/proxy-accounts/) page of our documentation.
