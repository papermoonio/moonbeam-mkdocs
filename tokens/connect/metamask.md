---
title: How to Connect MetaMask
description: This guide walks you through how to connect MetaMask, a browser-based Ethereum wallet, to Moonbeam-based networks and how to transfer funds.
categories:
- Tokens and Accounts
- Ethereum Toolkit
url: https://docs.moonbeam.network/tokens/connect/metamask/
word_count: 2048
token_estimate: 3727
version_hash: sha256:cf17c90cf3ee8ba49da8bd5afe13c02f458a8808c12d48a50adb0bbbc1277318
last_updated: '2026-05-21T21:21:53+00:00'
---

# Interacting with Moonbeam Using MetaMask

## Introduction {: #introduction }

Developers can leverage Moonbeam's Ethereum compatibility features to integrate tools, such as [MetaMask](https://metamask.io), into their dApps. By doing so, they can use the injected library MetaMask provides to interact with the blockchain.

Currently, MetaMask can be configured to connect to a few networks: Moonbeam, Moonriver, the Moonbase Alpha TestNet, and a Moonbeam development node.

If you already have MetaMask installed, you can easily connect MetaMask to the network of your choice:

<div class="button-wrapper">
    <a href="#" class="md-button connectMetaMask" value="moonbeam">Connect to Moonbeam</a>
</div>

<div class="button-wrapper">
    <a href="#" class="md-button connectMetaMask" value="moonriver">Connect to Moonriver</a>
</div>

<div class="button-wrapper">
    <a href="#" class="md-button connectMetaMask" value="moonbase">Connect to Moonbase Alpha</a>
</div>

!!! note
    MetaMask will pop up asking for permission to add a custom network. Once you approve permissions, MetaMask will switch your current network.

<div class="intro-disclaimer">
  The information presented herein is for informational purposes only and has been provided by third parties. Moonbeam does not endorse any project listed and described on the Moonbeam docs website (https://docs.moonbeam.network/).
</div>
## Install the MetaMask Extension {: #install-the-metamask-extension }

First, you'll start with a fresh and default [MetaMask](https://metamask.io) installation from the Chrome store. After downloading, installing, and initializing the extension, follow the **Get Started** guide. In there, you need to create a wallet, set a password, and store your secret backup phrase (this gives direct access to your funds, so make sure to store these in a secure place).

## Setup a Wallet {: #setup-a-wallet }

After installing [MetaMask](https://metamask.io), the setup will automatically open a new task with a welcome screen. Here, you are offered two options:

- **Create a new wallet** - you'll go through some steps to get a new seed phrase. Ensure you store this phrase securely and you don't share it publicly
- **Import an existing wallet** - you already have a seed phrase stored, and you want to restore an account from that recovery phrase

![Metamask Setup Interface](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-1.webp)

Once you've selected the option that fits your needs, follow the steps, and you should be all set.

!!! note
    Multiple accounts can be derived from a seed phrase by changing what is known as the address index. By default, when creating or importing an account from the seed phrase, you get the account with the address index 0. You can get the other indexes by just adding new accounts in the main Metamask screen.

## Import Accounts {: #import-accounts }

Once you've created a wallet or imported an existing one, you can also import any account into MetaMask if you hold the private keys.

For this example, you'll use private keys from the development account. Click the account switcher button to import an account using its private keys. That is where it says **Account 1**.

![Importing account from private key metamask menu](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-2.webp)

Next, click on **Import Account**.

![Importing account from private key account switcher menu](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-3.webp)

Finally, enter the private keys of the account you are trying to import. For example, you can use one of the accounts prefunded in the Moonbeam development node. This guide uses Gerald's key. Once you've entered the private key, click on **Import**.

??? note "Development account addresses and private keys"
    - Alith:
        - Public Address: `0xf24FF3a9CF04c71Dbc94D0b566f7A27B94566cac`
        - Private Key: `0x5fb92d6e98884f76de468fa3f6278f8807c48bebc13595d45af5bdc4da702133`

    - Baltathar:
        - Public Address: `0x3Cd0A705a2DC65e5b1E1205896BaA2be8A07c6e0`
        - Private Key: `0x8075991ce870b93a8870eca0c0f91913d12f47948ca0fd25b49c6fa7cdbeee8b`

    - Charleth:
        - Public Address: `0x798d4Ba9baf0064Ec19eB4F0a1a45785ae9D6DFc`
        - Private Key: `0x0b6e18cafb6ed99687ec547bd28139cafdd2bffe70e6b688025de6b445aa5c5b`

    - Dorothy:
        - Public Address: `0x773539d4Ac0e786233D90A233654ccEE26a613D9`
        - Private Key: `0x39539ab1876910bbf3a223d84a29e28f1cb4e2e456503e7e91ed39b2e7223d68`

    - Ethan:
        - Public Address: `0xFf64d3F6efE2317EE2807d223a0Bdc4c0c49dfDB`
        - Private Key: `0x7dce9bc8babb68fec1409be38c8e1a52650206a7ed90ff956ae8a6d15eeaaef4`

    - Faith:
        - Public Address: `0xC0F0f4ab324C46e55D02D0033343B4Be8A55532d`
        - Private Key: `0xb9d2ea9a615f3165812e8d44de0d24da9bbd164b65c4f0573e1ce2c8dbd9c8df`

    - Goliath:
        - Public Address: `0x7BF369283338E12C90514468aa3868A551AB2929`
        - Private Key: `0x96b8a38e12e1a31dee1eab2fffdf9d9990045f5b37e44d8cc27766ef294acf18`

    - Heath: 
        - Public Address: `0x931f3600a299fd9B24cEfB3BfF79388D19804BeA`
        - Private Key: `0x0d6dcaaef49272a5411896be8ad16c01c35d6f8c18873387b71fbc734759b0ab`

    - Ida: 
        - Public Address: `0xC41C5F1123ECCd5ce233578B2e7ebd5693869d73`
        - Private Key: `0x4c42532034540267bf568198ccec4cb822a025da542861fcb146a5fab6433ff8`

    - Judith: 
        - Public Address: `0x2898FE7a42Be376C8BC7AF536A940F7Fd5aDd423`
        - Private Key: `0x94c49300a58d576011096bcb006aa06f5a91b34b4383891e8029c21dc39fbb8b`
    - Gerald:
        - Public Address: `0x6Be02d1d3665660d22FF9624b7BE0551ee1Ac91b`
        - Private Key: `0x99b3c12287537e38c90a9219d4cb074a89a16e9cdb20bf85728ebd97c343e342`
![Paste your account key into MetaMask](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-4.webp)

You should end up with an imported **Account 2** that looks like this:

![MetaMask displaying your new Account 2](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-5.webp)

## Connect MetaMask to Moonbeam {: #connect-metamask-to-moonbeam }

Once you have [MetaMask](https://metamask.io) installed and have created or imported an account, you can connect it to any Moonbeam-based network. To do so, take the following steps:

1. Click in the upper left network selector menu
2. Select **Add Network**

![Add new network in Metamask menu](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-6.webp)

Next, go to the bottom of the page and click on **Add a network manually**:

![Add network manually in Metamask](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-7.webp)

Here, you can configure MetaMask for the following networks:

=== "Moonbeam"
    |         Variable          |                                      Value                                       |
    |:-------------------------:|:--------------------------------------------------------------------------------:|
    |       Network Name        |                                    `Moonbeam`                                    |
    |          RPC URL          |                     `https://rpc.api.moonbeam.network`                     |
    |         Chain ID          | `1284` (hex: `0x504`) |
    |     Symbol (Optional)     |                                      `GLMR`                                      |
    | Block Explorer (Optional) |                     `https://moonscan.io`                     |

=== "Moonriver"
    |         Variable          |                                       Value                                        |
    |:-------------------------:|:----------------------------------------------------------------------------------:|
    |       Network Name        |                                    `Moonriver`                                     |
    |          RPC URL          |                     `https://rpc.api.moonriver.moonbeam.network`                      |
    |         Chain ID          | `1285` (hex: `0x505`) |
    |     Symbol (Optional)     |                                       `MOVR`                                       |
    | Block Explorer (Optional) |                     `https://moonriver.moonscan.io/`                      |

=== "Moonbase Alpha"
    |         Variable          |                                      Value                                       |
    |:-------------------------:|:--------------------------------------------------------------------------------:|
    |       Network Name        |                                 `Moonbase Alpha`                                 |
    |          RPC URL          |                        `https://rpc.api.moonbase.moonbeam.network`                         |
    |         Chain ID          | `1287` (hex: `0x507`) |
    |     Symbol (Optional)     |                                      `DEV`                                       |
    | Block Explorer (Optional) |                     `https://moonbase.moonscan.io/`                     |

=== "Moonbeam Dev Node"
    |         Variable          |                                         Value                                          |
    |:-------------------------:|:--------------------------------------------------------------------------------------:|
    |       Network Name        |                                     `Moonbeam Dev`                                     |
    |          RPC URL          |                          `http://127.0.0.1:9944`                          |
    |         Chain ID          | `1281` (hex: `0x501`) |
    |     Symbol (Optional)     |                                         `DEV`                                          |
    | Block Explorer (Optional) |                      `https://moonbeam-explorer.netlify.app/`                       |

To do so, fill in the following information:

1. **Network name** - name that represents the network you are connecting to
2. **RPC URL** - [RPC endpoint](/moonbeam-mkdocs/builders/get-started/endpoints/) of the network
3. **Chain ID** - chain ID of the Ethereum compatible network
4. **Symbol** - (optional) symbol of the native token of the network. For example, for Moonbeam, the value would be **GLMR**
5. **Block Explorer** - (optional) URL of the [block explorer](/moonbeam-mkdocs/builders/get-started/explorers/)
6. Once you've verified all the information, click on **Save**

![Add network in Metamask](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-8.webp)

Once you've added the network, you'll be redirected to a screen stating that you've successfully added a network. Furthermore, you'll be prompted to **Switch to Moonbase Alpha**, the network added in this example.

![Successfully added a network in Metamask](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-9.webp)

## Interact with the Network {: #interact-with-the-network }

Once you've [connected Metamask](#connect-metamask-to-moonbeam) to any Moonbeam-based network, you can start using your wallet by:

- Sending a token transfer to another address
- Adding ERC-20s to Metamask and interacting with them
- Adding ERC-721s to Metamask and interacting with them

### Initiate a Transfer { #initiate-a-transfer }

This section showcases how to do a simple token transfer to another address as an example of using Metamask with Moonbeam.

To do so, take the following steps:

1. Ensure you are connected to the correct network
2. Ensure you have selected the account you want to use for the transfer
3. On the main screen of your Metamask wallet, click on **Send**

![Initiate balance transfer in Metamask](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-10.webp)

Next, you can enter the address to which you want to send the tokens. For this example, a wallet that has already been imported to Metamask is selected, known as **Bob**.

![Select account to send tokens to in Metamask](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-11.webp)

On the next screen, take the following steps:

1. Enter the number of tokens you want to send
2. Verify that all the information is correct, and click on **Next**

![Set the amount of tokens to send in Metamask](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-12.webp)

Lastly, confirm that all the gas-related parameters and fees are correct. After you've verified that everything is OK, click **Confirm**. At this point, your transaction has been sent to the network!

![Confirming a transaction in Metamask](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-13.webp)

Once you've confirmed your transaction, you are taken back to the main screen of your wallet, where you'll see the transaction as **Pending**. After less than a minute, the transaction should be **Confirmed**. If you click on your transaction, you can check more details and view it in a block explorer.

![Transaction confirmed in Metamask](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-14.webp)

### Add an ERC-20 Token {: #add-an-erc20-token }

To add an ERC-20 to your MetaMask wallet, you'll need to import the token using its address:

1. Make sure you've switched to the **Tokens** tab in MetaMask
2. Click **Import tokens**
3. Enter the contract address of the token you want to import. The **Token symbol** and **Token decimal** fields will automatically be populated, but you can edit the **Token symbol** if needed
4. Click **Next**

![The tokens tab and the import tokens process in MetaMask, where the token address, symbol, and decimal are defined.](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-15.webp)

Next, you'll be able to review the token import details. To finalize the import, you can click **Import**.

![Review the token details and finalize the import in MetaMask.](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-16.webp)

Under the **Tokens** tab, you'll be able to see the token and the account balance for the token.

![View the imported token in the list of assets on the tokens tab in MetaMask.](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-17.webp)

### Add an ERC-721 Token {: #add-an-erc721-token }

To add an ERC-721 to your MetaMask wallet, you'll need the token's address:

1. Make sure you've switched to the **NFTs** tab in MetaMask
2. Click **Import NFT**
3. Enter the **Address** of the NFT you want to import and the **Token ID**
4. Click **Import**

![The NFTs tab and the import NFT process in MetaMask, where the address and the token ID of the NFT are defined.](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-18.webp)

Once you've imported your NFT, you'll be able to see a preview of your NFT in the **NFTs** tab. You can click on the NFT to see more details.

![View the imported NFT in the list of NFTs on the NFTs tab in MetaMask.](/moonbeam-mkdocs/images/tokens/connect/metamask/metamask-19.webp)

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
