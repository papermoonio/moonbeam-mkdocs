---
title: How to use Polkadot.js Apps
description: Follow this quick tutorial to learn how to use Moonbeam’s Ethereum-style H160 addresses and send transactions with Polkadot.js Apps.
categories:
- Tokens and Accounts
- Ethereum Toolkit
url: https://docs.moonbeam.network/tokens/connect/polkadotjs/
word_count: 1387
token_estimate: 2002
version_hash: sha256:1fca6f81d5d6b372cbd6cdb9711c94ef21741d751219584b75a9c481e1b27fec
last_updated: '2026-05-21T21:21:53+00:00'
---

# How to use Polkadot.js Apps to Interact with Moonbeam

## Introduction {: #introduction }

As a Polkadot parachain, Moonbeam uses a [unified account structure](/moonbeam-mkdocs/learn/core-concepts/unified-accounts/) that allows you to interact with Substrate (Polkadot) functionality and Moonbeam's EVM, all from a single Ethereum-style address. This unified account structure means that you don't need to maintain both a Substrate and an Ethereum account to interact with Moonbeam - instead, you can do it all with a single Ethereum private key.

The Polkadot.js Apps interface natively supports H160 addresses and ECDSA keys. So, in this tutorial, you can check out this integration of Ethereum-based accounts on [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network%2Fpublic-ws#/accounts).

<div class="intro-disclaimer">
  The information presented herein is for informational purposes only and has been provided by third parties. Moonbeam does not endorse any project listed and described on the Moonbeam docs website (https://docs.moonbeam.network/).
</div>
!!! note
    Polkadot.js Apps is phasing out support for accounts stored locally in the browser's cache. Instead, it is recommended that you use a browser extension like [Talisman to inject your accounts into Polkadot.js Apps](/moonbeam-mkdocs/tokens/connect/talisman/).

## Connect Polkadot.js Apps to Moonbeam {: #connect-polkadotjs-apps }

When launching [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network%2Fpublic-ws#/accounts) for the first time, you may or may not be connected to the desired network.

You can change the selected network by clicking the logo in the top left corner, where you'll find a list of networks organized by MainNets, TestNets, and local networks. Each network can be found under the following sections:

|          Network          |        Section        |
|:-------------------------:|:---------------------:|
|          Moonbeam         | Polkadot & Parachains |
|         Moonriver         |  Kusama & Parachains  |
|       Moonbase Alpha      |     Test Networks     |
| Moonbeam Development Node |      Development      |

Once you've selected the correct network, you can scroll back to the top and click **Switch**.

![Connect to Moonbase Alpha](/moonbeam-mkdocs/images/tokens/connect/polkadotjs/polkadotjs-1.webp)

After switching, the Polkadot.js site will not only connect to the chosen network, but the logo and styling will change for each network.

![Connect to Moonbase Alpha](/moonbeam-mkdocs/images/tokens/connect/polkadotjs/polkadotjs-2.webp)

## Create or Import an H160 Account into Polkadot.js Apps {: #creating-or-importing-an-h160-account }

!!! note
    For security purposes, it is recommended that you do not store accounts locally in the browser. A more secure method is using a browser extension like [Talisman to inject your accounts into Polkadot.js Apps](/moonbeam-mkdocs/tokens/connect/talisman/).

In this section, you'll learn how you can create a new account or import a preexisting MetaMask account to Polkadot.js Apps. First, there is one prerequisite step. As part of the process of phasing out support for accounts stored locally in the browser's cache, you'll need to enable support for local storage of accounts in the **Settings** tab. To do so, take the following steps:

1. Navigate to the **Settings** tab
2. Select **Allow local in-browser account storage** under the **in-browser account creation** heading
3. Press **Save**

![Allow local in-browser account storage](/moonbeam-mkdocs/images/tokens/connect/polkadotjs/polkadotjs-3.webp)

You can now head back to the [Accounts page of Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=wss://wss.api.moonbase.moonbeam.network%2Fpublic-ws#/accounts) and proceed with the next steps:

1. Navigate to the **Accounts** section
2. Click on the **Add account** button

![Connect to Moonbase Alpha](/moonbeam-mkdocs/images/tokens/connect/polkadotjs/polkadotjs-4.webp)

This will open a wizard pop-up that will guide you through the process of adding an account to the Polkadot.js Apps interface:

1. Click on the drop-down menu
2. Change the selection from **Mnemonic** to **Private Key**, this allows you to add an account through a private key

!!! note
    Currently, you can only create or import accounts in Polkadot.js via a private key. Doing so with the mnemonic will result in a different public address if you later try to import this account to an Ethereum wallet such as MetaMask. This is because Polkadot.js uses BIP39, whereas Ethereum uses BIP32 or BIP44.

![Connect to Moonbase Alpha](/moonbeam-mkdocs/images/tokens/connect/polkadotjs/polkadotjs-5.webp)

Next, if you want to create a new account, make sure you store the private key displayed by the wizard. If you want to import an existing account, enter your private key that you can export from MetaMask.

!!! note
    Never reveal your private keys as they give direct access to your funds. The steps in this guide are for demonstration purposes only.

Make sure to include the prefix in the private key, i.e., `0x`. If you entered the information correctly, the corresponding public address should appear in the upper left corner of the window, and then click **Next**.

![Connect to Moonbase Alpha](/moonbeam-mkdocs/images/tokens/connect/polkadotjs/polkadotjs-6.webp)

To finish the wizard, you can set an account name and password. After a confirmation message, you should see in the main **Accounts** tab the address with the corresponding balance: in this case, Bob's address. Moreover, you can overlay the MetaMask extension to see that both balances are the same.

![Connect to Moonbase Alpha](/moonbeam-mkdocs/images/tokens/connect/polkadotjs/polkadotjs-7.webp)

## Send a Transaction Through Substrate's API {: #sending-a-transaction-through-substrates-api }

Now, to demonstrate the potential of Moonbeam's [unified accounts](/moonbeam-mkdocs/learn/core-concepts/unified-accounts/) scheme, you can make a transfer through the Substrate API using Polkadot.js Apps. Remember that you are interacting with Substrate using an Ethereum-style H160 address. To do so, you can import another account.

Next, click on Bob's **send** button, which opens another wizard that guides you through the process of sending a transaction.

1. Set the **send to address**
2. Enter the **amount** to send, which for this example is 1 DEV token
3. When ready, click on the **Make Transfer** button

![Connect to Moonbase Alpha](/moonbeam-mkdocs/images/tokens/connect/polkadotjs/polkadotjs-8.webp)

Then you'll be prompted to enter your password and sign and submit the transaction. Once the transaction is confirmed, you should see the balances updated for each account.

![Connect to Moonbase Alpha](/moonbeam-mkdocs/images/tokens/connect/polkadotjs/polkadotjs-9.webp)

And that is it! We are excited about being able to support H160 accounts in Polkadot.js Apps, as we believe this will greatly enhance the user experience on the Moonbeam Network and its Ethereum compatibility features.

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
