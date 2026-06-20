---
title: Non-Network Specific Precompiles
description: Learn how to use precompiled contracts, which are not specific to Ethereum or Moonbeam, yet are supported for use in your application.
categories:
- Precompiles
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/precompiles/utility/non-specific/
word_count: 1129
token_estimate: 1801
version_hash: sha256:6ee5e446f69f3c344ac7d1539c0aca03eaebf9133e25569ba9ce18d7101690ed
last_updated: '2026-05-21T21:21:53+00:00'
---

# Non-Network Specific Precompiled Smart Contracts

## Introduction {: #introduction }

A precompiled contract, or precompile, is a set of programmed functionalities hard-coded into the blockchain client. Precompiles perform computationally heavy tasks, such as cryptographic processes like hashing. Moving these functionalities to the blockchain client serves the dual purpose of making the computation more efficient than using a traditional smart contract and ensuring everyone has access to the complete and accurate set of processes and algorithms required to operate correctly.

Precompile functionality is bundled and shared under a smart contract address, which allows interactions similar to those of a traditional smart contract. Some precompiled contracts are not specific to Ethereum or Moonbeam, but are supported for use in your Moonbeam application. 

The nonspecific precompiles currently included in this category are the `ECRecoverPublicKey` and `SHA3FIPS256` precompiles. 

In the next section, you will learn more about the functionalities included in these precompiles.  

## Retrieve a Public Key with ECRecoverPublicKey {: verifying-signatures-ecrecoverpublickey }

The primary function of the `ECRecoverPublicKey` precompile is to recover the public key used to create a digital signature from a given message hash and signature. This precompile is similar to [ECRecover](/moonbeam-mkdocs/builders/ethereum/precompiles/utility/eth-mainnet/#verify-signatures-with-ecrecover/), with the exception of returning the public key of the account that signed the message rather than the account address. 

In the following sections, you will learn how to use the `ECRecoverPublicKey` precompile.

### Checking Prerequisites {: #checking-prerequisites }

You need to install Node.js (for this example, you can use v16.x) and the npm package manager. You can download directly from [Node.js](https://nodejs.org/en/download) or in your terminal:

=== "Ubuntu"

    ```bash
    curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -

    sudo apt install -y nodejs
    ```

=== "MacOS"

    ```bash
    # You can use homebrew (https://docs.brew.sh/Installation)
    brew install node

    # Or you can use nvm (https://github.com/nvm-sh/nvm)
    nvm install node
    ```

You can verify that everything is installed correctly by querying the version for each package:

```bash
node -v
```

```bash
npm -v
```
The versions used in this example are v20.15.0 (Node.js) and 10.7.0 (npm). You will also need to install the [Web3](https://web3js.readthedocs.io/en/latest) package by executing:

```bash
npm install --save web3
```

To verify the installed version of Web3, you can use the `ls` command:

```bash
npm ls web3
```

This example uses version 4.11.1. You will also use [Remix](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/), connecting it to the Moonbase Alpha TestNet via [MetaMask](/moonbeam-mkdocs/tokens/connect/metamask/).

To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
### Retrieve Transaction Signature Values

To use the `ECRecoverPublicKey` precompile, you must first sign a message to create and retrieve the message hash and transaction signature values (`v`, `r`, `s`) to pass as arguments in the contract call. Always use security best practices when handling private keys. 

Create a new file called `signMessage.js` in your project directory:

```bash
touch signMessage.js
```

Open `signMessage.js` in your code editor and add the following script to initialize Web3 with Moonbase Alpha TestNet, sign and hash the message, and return the signature values:

```js title="signMessage.js"
const { Web3 } = require('web3');
const web3 = new Web3('https://rpc.api.moonbase.moonbeam.network');

// Address and private key
const address = 'INSERT_RECEIVER_ADDRESS';
const pk1 =
  'INSERT_SENDER_PRIVATE_KEY';
const msg = web3.utils.sha3('supercooltestmessage');

async function signMessage(pk) catch (error)
}

signMessage(pk1);
```

Return to your terminal command line to run the script with this command:

```bash
node signMessage.js
```

This code will return the following object in the terminal:

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>node signMessage.js</span>
    <span data-ty>{</span>
    <span data-ty>  message: '0x5836e21a51f25aad199e2e0feb5ca19673ed56b3811285f5124d7a8171d75851',</span>
    <span data-ty>  messageHash: '0xa69b720d0293b9e8f4e471afb80f9d410b825abe5ce524e7d5755fd2a00bf9de',</span>
    <span data-ty>  v: '0x1b',</span>
    <span data-ty>  r: '0xb7d4783ee3b34d6fbc419d5b7bc67002c511322c5c71b49a7d78a8b7e9c5b30a',</span>
    <span data-ty>  s: '0x4e5939eaef3917b1cb09af9e632cc9a727b64191b7ee40a6ae34f6fdde60a371',</span>
    <span data-ty>  signature: '0xb7d4783ee3b34d6fbc419d5b7bc67002c511322c5c71b49a7d78a8b7e9c5b30a4e5939eaef3917b1cb09af9e632cc9a727b64191b7ee40a6ae34f6fdde60a3711b'</span>
    <span data-ty>}</span>
    <span data-ty="input"><span class="file-path"></span></span>
</div>
Save these values as you will need them in the next section.

### Test ECRecoverPublicKey Contract

You can now visit [Remix](https://remix.ethereum.org/) to test the precompiled contract. Note that you could also use the Web3.js library, but in this case, you can go to Remix to ensure it is using the precompiled contract on the blockchain. The Solidity code you can use to retrieve the public key is the following:

```solidity title="RecoverPublicKey.sol"
// SPDX-License-Identifier: MIT

pragma solidity >=0.8.2 <0.9.0;

contract RecoverPublicKey {
    function recoverPublicKey(
        bytes32 hash,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) public view returns (bytes memory)
}
```

Using the [Remix compiler and deployment](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) and with [MetaMask pointing to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/), you can deploy the contract and call the `recoverPublicKey()` method which returns the public key for the account that signed the message. You can now use this public key value for other cryptographic functions and verifications.

![Returned Public Key on Remix](/moonbeam-mkdocs/images/builders/ethereum/precompiles/utility/nonspecific/nonspecific-1.webp)

## Create a Hash with SHA3FIPS256 {: #create-a-hash-with-sha3fips256 }

SHA3-256 is part of the SHA-3 family of cryptographic hashes codified in [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf) that produces an output 256 bits in length. Although the name is similar to SHA256, the SHA-3 family is built with an entirely different algorithm and accordingly produces a different hash output than SHA256 for the same input. You can verify this yourself using this [SHA3-256 Hash Calculator tool](https://md5calc.com/hash/sha3-256). After calculating the SHA3-256 output, change the algorithm in the drop-down selector to SHA256 and take note of the resulting output.

Currently there is no SHA3-256 support in Solidity, so it needs to be called with inline assembly. The following sample code can be used to call this precompile.

```solidity
pragma solidity ^0.7.0;

contract Precompiles {
    function sha3fips(bytes memory data) public view returns (bytes32)
        }
        return h[0];
    }
}
```

Using [Remix](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) with [MetaMask pointing to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/), you can deploy the contract and call the `sha3fips(bytes memory data)` method to return the encoded string of the data parameter.

<div class="intro-disclaimer">
  The information presented herein is for informational purposes only and has been provided by third parties. Moonbeam does not endorse any project listed and described on the Moonbeam docs website (https://docs.moonbeam.network/).
</div>
