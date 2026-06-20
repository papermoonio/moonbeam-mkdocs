---
title: Ethereum App
description: This guide walks you through how to use your Ledger hardware wallet to sign transactions in Moonbeam-based networks using the Ethereum app on Ledger Live.
categories:
- Tokens and Accounts
- Ethereum Toolkit
url: https://docs.moonbeam.network/tokens/connect/ledger/
word_count: 2818
token_estimate: 3867
version_hash: sha256:ff2973620a6454ce80526c0c53ef04aa6cdd7f1be191b40a8cdb43280c52bc3b
last_updated: '2026-05-21T21:21:53+00:00'
---

# Interacting with Moonbeam Using Ledger and the Ethereum App

## Introduction {: #introduction } 

Hardware wallets provide a safer way to store crypto funds because the private key (used for signing transactions) is stored offline. Ledger offers two hardware wallet solutions at the time of writing: Ledger Nano S and Ledger Nano X.

For Moonbeam, Moonriver, and the Moonbase Alpha TestNet, you can use the Ethereum app on Ledger Live by setting the chain ID. For Moonbeam, the chain ID is 1284, for Moonriver it's 1285, and for Moonbase Alpha it's 1287. The Ethereum app covers all supported Moonbeam-based networks and can be used to connect a Ledger device.

In this tutorial, you will learn how to get started with your Ledger hardware wallet on Moonbeam using the Ethereum app. This guide only illustrates the steps for a Ledger Nano X device, but you can follow along with a Ledger Nano S as well. 

<div class="intro-disclaimer">
  The information presented herein is for informational purposes only and has been provided by third parties. Moonbeam does not endorse any project listed and described on the Moonbeam docs website (https://docs.moonbeam.network/).
</div>
## Checking Prerequisites {: #checking-prerequisites } 

Before you get started, update [Ledger Live](https://www.ledger.com/ledger-live) to the latest version available. Also, make sure you've your Ledger hardware wallet device running the latest firmware. The Ledger support website offers tutorials on [how to update](https://support.ledger.com/article/360013349800-zde) the firmware.

At the time of writing, the following versions were used:

 - [Ledger Live 2.35.1](https://support.ledger.com/article/What-s-new-in-Ledger-Live)
 - [Ledger Nano S firmware v2.0.0](https://support.ledger.com/article/360010446000-zd)
 - [Ledger Nano X firmware v2.0.1](https://support.ledger.com/article/360014980580-zd)
As of November 29, 2022, the Moonbeam and Ledger Live integration was released, allowing you to send and receive GLMR tokens with your Ledger device directly in Ledger Live. With this integration, you'll no longer need to connect your Ledger to MetaMask. If you prefer this method, please skip ahead to the [Use Ledger Live to Send & Receive GLMR](#use-ledger-live) section of this guide.

If you prefer to use MetaMask as an intermediary between your Ledger device and Moonbeam, make sure that your MetaMask is [connected to Moonbeam](/moonbeam-mkdocs/tokens/connect/metamask/).

As of [MetaMask version 10.5.0](https://consensys.io/blog/metamask-and-ledger-integration-fixed), connecting your Ledger device with MetaMask on Chrome is easy again. You just need to have the latest version of MetaMask installed.
## Install the Ledger Live App {: install-the-ledger-live-app }

If you want to connect to Moonbeam, Moonriver, or the Moonbase Alpha TestNet you can do so by installing the Ethereum app, and later on you'll need to specify a chain ID.

To get started, open up Ledger Live and:

1. Select **Manager** from the menu
2. Connect and unlock your device (this must be done before installation)
3. In the **App catalog** search for Ethereum (ETH) and click **Install**. Your Ledger device will show **Processing** and once the installation is complete, the app will appear on your Ledger device
In the Ledger Live app, depending on which app(s) you installed you should see them listed under the **Apps installed** tab on the **Manager** page. After the app(s) have been successfully installed, you can close out of Ledger Live. 

<img src="/images/tokens/connect/ledger/ethereum/ledger-1.webp" alt="Moonriver Ledger App Installed" style="width: 50%; display: block; margin-left: auto; margin-right: auto;" />

## Import your Ledger Account to MetaMask {: #import-your-ledger-account-to-metamask } 

Now that you've installed the app(s) on Ledger Live, you can connect your Ledger to the computer and unlock it, and open the Ethereum app. 

 Then import your Ledger account to MetaMask using the following steps:

 1. Click on the top-right logo to expand the menu
 2. Select **Connect Hardware Wallet**
![MetaMask Connect Hardware Wallet](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-2.webp)

In the next screen, you are prompted to select which hardware wallet you'll like to use in MetaMask. At the moment of writing, only Ledger and Trezor hardware wallets are supported. Here, take the following steps:

 1. Select the Ledger logo
 2. Click on **Continue**
![MetaMask Select Ledger Hardware Wallet](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-3.webp)

If you're using Chrome or a Chrome-based browser like Brave, you'll be prompted to select your Ledger device to connect via WebHID:

1. Select your Ledger device from the pop-up
2. Click **Connect**
![Ledger on Chrome](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-4.webp)

If a pop-up doesn't appear, you may need to change your MetaMask settings to enable a WebHID connection. You can check and update your MetaMask settings by following these steps:

1. Expand the top-right menu and go to **Settings** 
2. Navigate to **Advanced**
3. Scroll down to **Preferred Ledger Connection Type** and select **WebHID** from the dropdown

!!! note
    The **Preferred Ledger Connection Type** setting is only available on Chrome and Chrome-based browsers. This setting doesn't exist on other browsers such as Firefox.
If MetaMask was able to connect successfully to your Ledger device, you should see a list of five Moonbeam/Ethereum-styled accounts. If not, double-check that Ledger Live is closed, you've connected your Ledger device to the computer, and unlocked it, and make sure the Ethereum app is open.

### Import Accounts and View Balances {: #import-accounts-and-view-balances } 

From the list of accounts, take the following steps:

 1. Select the accounts you would like to import from your Ledger device
 2. Click on **Unlock**
![MetaMask Select Ethereum Accounts to Import](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-5.webp)

If you've imported your Ledger account successfully, you should see your account and balance displayed in the main MetaMask screen like shown in the following image:

![MetaMask Successfully Imported Ledger Account](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-6.webp)

You can switch accounts in MetaMask at any time to view the balance of your other imported Ledger accounts.

You've now successfully imported a Moonbeam compatible account from your Ledger device and are now ready to start interacting with your Ledger device.

## Receive Tokens {: #receive-tokens } 

To get started interacting with your Ledger device, you will need to send some funds to it. Copy your address from MetaMask by clicking on your account name and address in MetaMask.
![MetaMask Copy Account](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-7.webp)

Next, you will need to obtain some GLMR, MOVR, or DEV tokens and using the address you just copied, send the tokens to your account. After the transaction has successfully gone through, you will see your balance update.

You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network).
## Send Tokens {: #send-tokens } 

Next up is sending and signing transactions on Moonbeam using your Ledger device. To get started sending a transaction, click on the **Send** button:

![MetaMask Ledger Account Funded](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-8.webp)

As you would in a standard transaction, set the recipient address, enter the number of tokens to send, review transaction details and confirm it. This will initiate the transaction signature wizard in your Ledger device. Here, take the following steps:

 1. Click the button to proceed to the next screen. Your Ledger device is only warning you to review the transaction
 2. Check the number of tokens being sent then proceed to the next screen
 3. Check the recipient's address and proceed to the next screen
4. Check the chain ID of the network. This information confirms which network MetaMask is connected to. For Moonbeam the chain ID is 1284 (hex: 0x504), Moonriver is 1285 (hex: 0x505), and Moonbase Alpha is 1287 (hex: 0x507). When ready, proceed to the next screen
5. Check the max fees applicable to this transaction. This is the gas price multiplied by the gas limit you've set on MetaMask. When ready, proceed to the next screen
6. If you agree with all the transaction details, approve it. This will sign the transaction and will trigger MetaMask to send it. If you don't agree with all the transaction details, reject it. This will cancel the transaction, and MetaMask will mark it as failed

![MetaMask Ledger Transaction Wizard](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-9.webp)

Right after you've approved the transaction, MetaMask sends it to the network. Once the transaction is confirmed, it will be displayed as **Send** on the **Activity** tab in MetaMask.

![MetaMask Ledger Transaction Wizard](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-10.webp)

And that is it! You've signed a transaction and sent some tokens on Moonbeam using your Ledger hardware wallet!

## Interact with Contracts Using your Ledger {: #interact-with-contracts-using-your-ledger } 

By default, Ledger devices don't admit a `data` field in the transaction object. Consequently, users can't deploy or interact with smart contracts.

However, if you want to use your Ledger hardware wallet for transactions related to smart contracts, you need to change a configuration parameter inside the app on your device. To do so, take the following steps:

 1. On your Ledger, open the Moonriver or Ethereum app
 2. Navigate to **Settings**
 3. Find the **Blind signing** page. It should state **NOT Enabled** at the bottom
 4. Select/validate the option to change its value to **Enabled**

!!! note
    This option is necessary to use your Ledger device to interact with ERC-20 token contracts that might live inside the Moonbeam ecosystem.
![MetaMask Ledger Allow Contracts Tx](/moonbeam-mkdocs/images/tokens/connect/ledger/ethereum/ledger-11.webp)

## Use Ledger Live to Send & Receive GLMR {: #use-ledger-live }

You can also use your Ledger device to send and receive GLMR tokens securely from within Ledger Live. This enables you to manage your GLMR tokens without connecting your device to MetaMask.

When you open up the Ledger Live app, make sure that you've installed the latest updates. If there are any pending updates that need to be installed, there will be a banner at the top of the screen that prompts you to install the updates.

To get started, you'll need to login to your Ledger device to unlock it. From Ledger Live, click on **My Ledger**. On your device, you'll be prompted to allow Ledger manager; you can click both buttons on your device to allow it.

Once on the Ledger manager, you'll need to make sure that your firmware is up to date, and if the Moonbeam and/or Ethereum apps need to be updated, go ahead and install the latest versions.

Next, you'll need to add an account to your Ledger Live app. To do so, you can take the following steps:

1. Click on **Accounts** from the left-side menu
2. Select **Add account**
3. A dropdown will appear. Search for GLMR and **Moonbeam (GLMR)** should appear for you to select
4. Click **Continue**

![Add account to Ledger Live](/moonbeam-mkdocs/images/tokens/connect/ledger/ledger-live-1.webp)

Next, you'll be able to enter an account name and click **Add account**. If your account was successfully added, you can click **Done** and your account will appear in your list of accounts.

### Receive Tokens

To receive GLMR to your Ledger device, you can take the following steps from Ledger Live:

1. Click on **Receive** from the left-side menu
2. A pop-up will appear. You can select your Moonbeam account where you want to receive tokens from the **Account to credit** dropdown
3. Click **Continue**

![Verify receiving address in Ledger Live](/moonbeam-mkdocs/images/tokens/connect/ledger/ledger-live-2.webp)

Next, your address should appear on Ledger Live, and you'll be prompted to verify your address on your Ledger device. On your device, you can take the following steps:

1. You should see **Verify Address** on your device's screen. Click the right button to start verifying your address
2. On the next screen, you should see your address. Compare the address on your device to the one displayed on Ledger Live and verify it matches. At this time, you'll want to copy the address from Ledger Live so you can send a transaction to it. Click the right button to continue
3. Now, you should see the **Approve** screen. If the addresses match, you can click both buttons on your device to approve the verification. Otherwise, click the right button again to get to the **Reject** screen where you can click both buttons to reject the verification

![Verify receiving address on Ledger device](/moonbeam-mkdocs/images/tokens/connect/ledger/ledger-live-3.webp)

Over on Ledger Live, you'll see that your address has been shared securely, and you can click **Done**. Now, you can send some GLMR to your Ledger account.

### Send Tokens

To send GLMR from your Ledger device, you can take the following steps from Ledger Live:

1. Click on **Send** from the left-side menu
2. A pop-up will appear. From the **Account to debit** dropdown, you can select your Moonbeam account that you want to send tokens from
3. Enter an address in the **Receipient address** field
4. Click **Continue**

![Send transaction in Ledger Live](/moonbeam-mkdocs/images/tokens/connect/ledger/ledger-live-4.webp)

On the next screen, you can enter the amount of GLMR that you would like to send and click **Continue**.

![Enter amount to send in Ledger Live](/moonbeam-mkdocs/images/tokens/connect/ledger/ledger-live-5.webp)

The last step on Ledger Live is to verify that the transaction details are correct. If everything looks good, you can click **Continue**. Then you'll be prompted to confirm the transaction on your Ledger device:

1. The first screen will be the **Review transaction** screen. Click the right button to proceed to the next screen
2. Verify the amount of GLMR you're sending and click the right button to proceed
3. Verify the address you're sending the GLMR to and click the right button to proceed
4. The **Network** screen should show **Moonbeam**. Click the right button to proceed
5. Review the **Max Fees** and click the right button to proceed
6. If everything looks good, you can click both buttons to **Accept and send** the transaction. Otherwise, you can click the right button to get to the **Reject** screen where you can click both buttons to reject the transaction

![Send transaction from Ledger device](/moonbeam-mkdocs/images/tokens/connect/ledger/ledger-live-6.webp)

On Ledger Live, you should see that your transaction was sent, and you can view the details of the transaction. Once the transaction has been confirmed, your GLMR balance will update.

You've successfully used the Moonbeam Ledger Live integration to receive and send tokens with your Ledger device directly from Ledger Live.
<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
