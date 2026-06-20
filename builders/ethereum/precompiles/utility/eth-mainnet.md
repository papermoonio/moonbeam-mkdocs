---
title: Ethereum MainNet Precompiles
description: Learn how to use the standard precompiled contracts available on Ethereum such as ECRECOVER, SHA256, and more on Moonbeam.
categories:
- Precompiles
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/precompiles/utility/eth-mainnet/
word_count: 1931
token_estimate: 3544
version_hash: sha256:c454c97497dc545f21c93ac4c38904a8d5adc7f245f385c56083d391ce0df240
last_updated: '2026-05-21T21:21:53+00:00'
---

# Ethereum MainNet Precompiled Contracts

## Introduction {: #introduction }

Precompiled contracts in Ethereum are contracts that include complex cryptographic computations, but do not require the overhead of the EVM. These precompiles can be used within the EVM to handle specific common operations such as hashing and signature schemes.

The following precompiles are currently included: ecrecover, sha256, ripemd-160, Bn128Add, Bn128Mul, Bn128Pairing, the identity function, and modular exponentiation.

These precompiles are natively available on Ethereum and, to maintain Ethereum compatibility, they are also available on Moonbeam.

In this guide, you will learn how to use and/or verify these precompiles.

## Checking Prerequisites {: #checking-prerequisites }

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
As of writing this guide, the versions used were 15.2.1 and 7.0.8, respectively. You will also need to install the [Web3](https://web3js.readthedocs.io/en/latest) package by executing:

```bash
npm install --save web3
```

To verify the installed version of Web3, you can use the `ls` command:

```bash
npm ls web3
```

As of writing this guide, the version used was 1.3.0. You will be also using [Remix](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/), connecting it to the Moonbase Alpha TestNet via [MetaMask](/moonbeam-mkdocs/tokens/connect/metamask/).

To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
## Verify Signatures with ECRECOVER {: #verify-signatures-with-ecrecover }

The main function of this precompile is to verify the signature of a message. In general terms, you feed `ecrecover` the transaction's signature values and it returns an address. The signature is verified if the address returned is the same as the public address that sent the transaction.

The following will be a small example to showcase how to leverage this precompiled function. You'll need to retrieve the transaction's signature values (`v`, `r`, `s`). Therefore, you'll sign and retrieve the signed message where these values are:

```js
const { Web3 } = require('web3');

// Provider
const web3 = new Web3('https://rpc.api.moonbase.moonbeam.network');

// Address and Private Key
const address = '0x6Be02d1d3665660d22FF9624b7BE0551ee1Ac91b';
const pk1 = '99B3C12287537E38C90A9219D4CB074A89A16E9CDB20BF85728EBD97C343E342';
const msg = web3.utils.sha3('supercalifragilisticexpialidocious');

async function signMessage(pk) catch (error)
}

signMessage(pk1);
```

This code will return the following object in the terminal:

```text
{
  message: '0xc2ae6711c7a897c75140343cde1cbdba96ebbd756f5914fde5c12fadf002ec97',
  messageHash: '0xc51dac836bc7841a01c4b631fa620904fc8724d7f9f1d3c420f0e02adf229d50',
  v: '0x1b',
  r: '0x44287513919034a471a7dc2b2ed121f95984ae23b20f9637ba8dff471b6719ef',
  s: '0x7d7dc30309a3baffbfd9342b97d0e804092c0aeb5821319aa732bc09146eafb4',
  signature: '0x44287513919034a471a7dc2b2ed121f95984ae23b20f9637ba8dff471b6719ef7d7dc30309a3baffbfd9342b97d0e804092c0aeb5821319aa732bc09146eafb41b'
}
```

With the necessary values, you can go to [Remix](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) to test the precompiled contract. Note that this can also be verified with the Web3.js library, but in this case, you can go to Remix to be sure that it is using the precompiled contract on the blockchain. The Solidity code you can use to verify the signature is the following:

```solidity
pragma solidity ^0.7.0;

contract ECRECOVER {
    address addressTest = 0x12Cb274aAD8251C875c0bf6872b67d9983E53fDd;
    bytes32 msgHash =
        0xc51dac836bc7841a01c4b631fa620904fc8724d7f9f1d3c420f0e02adf229d50;
    uint8 v = 0x1b;
    bytes32 r =
        0x44287513919034a471a7dc2b2ed121f95984ae23b20f9637ba8dff471b6719ef;
    bytes32 s =
        0x7d7dc30309a3baffbfd9342b97d0e804092c0aeb5821319aa732bc09146eafb4;

    function verify() public view returns (bool)
}
```

Using the [Remix compiler and deployment](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) and with [MetaMask pointing to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/), you can deploy the contract and call the `verify()` method that returns **true** if the address returned by `ecrecover` is equal to the address used to sign the message (related to the private key and needs to be manually set in the contract).

## Hashing with SHA256 {: #hashing-with-sha256 }

This hashing function returns the SHA256 hash from the given data. To test this precompile, you can use this [SHA256 Hash Calculator tool](https://md5calc.com/hash/sha256) to calculate the SHA256 hash of any string you want. In this case, you'll do so with `Hello World!`. You can head directly to Remix and deploy the following code, where the calculated hash is set for the `expectedHash` variable:

```solidity
pragma solidity ^0.7.0;

contract Hash256 {
    bytes32 public expectedHash =
        0x7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069;

    function calculateHash() internal pure returns (bytes32)

    function checkHash() public view returns (bool)
}
```

Once the contract is deployed, you can call the `checkHash()` method that returns **true** if the hash returned by `calculateHash()` is equal to the hash provided.

## Hashing with RIPEMD160 {: #hashing-with-ripemd-160 }

This hashing function returns a RIPEMD160 hash from the given data. To test this precompile, you can use this [RIPEMD160 Hash Calculator tool](https://md5calc.com/hash/ripemd160) to calculate the RIPEMD160 hash of any string. In this case, you'll do so again with `Hello World!`. You'll reuse the same code as before, but use the `ripemd160` function. Note that it returns a `bytes20` type variable:

```solidity
pragma solidity ^0.7.0;

contract HashRipmd160 {
    bytes20 public expectedHash = hex"8476ee4631b9b30ac2754b0ee0c47e161d3f724c";

    function calculateHash() internal pure returns (bytes20)

    function checkHash() public view returns (bool)
}
```

With the contract deployed, you can call the `checkHash()` method that returns **true** if the hash returned by `calculateHash()` is equal to the hash provided.

## BN128Add {: #bn128add }

The BN128Add precompile implements a native elliptic curve point addition. It returns an elliptic curve point representing `(ax, ay) + (bx, by)` such that `(ax, ay)` and `(bx, by)` are valid points on the curve BN256.

Currently there is no BN128Add support in Solidity, so it needs to be called with inline assembly. The following sample code can be used to call this precompile.

```solidity
pragma solidity >=0.4.21;

contract Precompiles {
    function callBn256Add(
        bytes32 ax,
        bytes32 ay,
        bytes32 bx,
        bytes32 by
    ) public returns (bytes32[2] memory result)
        }
    }
}
```

Using the [Remix compiler and deployment](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) and with [MetaMask pointing to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/), you can deploy the contract and call the `callBn256Add(bytes32 ax, bytes32 ay, bytes32 bx, bytes32 by)` method to return the result of the operation.

## BN128Mul {: #bn128mul }

The BN128Mul precompile implements a native elliptic curve multiplication with a scalar value. It returns an elliptic curve point representing `scalar * (x, y)` such that `(x, y)` is a valid curve point on the curve BN256.

Currently there is no BN128Mul support in Solidity, so it needs to be called with inline assembly. The following sample code can be used to call this precompile.

```solidity
pragma solidity >=0.4.21;

contract Precompiles {
    function callBn256ScalarMul(
        bytes32 x,
        bytes32 y,
        bytes32 scalar
    ) public returns (bytes32[2] memory result)
        }
    }
}
```

Using the [Remix compiler and deployment](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) and with [MetaMask pointing to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/), you can deploy the contract and call the `callBn256ScalarMul(bytes32 x, bytes32 y, bytes32 scalar)` method to return the result of the operation.

## BN128Pairing {: #bn128pairing }

The BN128Pairing precompile implements elliptic curve pairing operation to perform zkSNARK verification. For more information, check out the [EIP-197 standard](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-197.md).

Currently there is no BN128Pairing support in Solidity, so it needs to be called with inline assembly. The following sample code can be used to call this precompile.

```solidity
pragma solidity >=0.4.21;

contract Precompiles {
    function callBn256Pairing(
        bytes memory input
    ) public returns (bytes32 result)
            default {
                result := mload(memPtr)
            }
        }
    }
}
```

Using the [Remix compiler and deployment](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) and with [MetaMask pointing to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/), you can deploy the contract and call the `function callBn256Pairing(bytes memory input)` method to return the result of the operation.

## The Identity Function {: #the-identity-function }

Also known as datacopy, this function serves as a cheaper way to copy data in memory.

Currently there is no Identity Function support in Solidity, so it needs to be called with inline assembly. The following sample code (adapted to Solidity), can be used to call this precompiled contract:

```solidity
pragma solidity ^0.7.0;

contract Identity {
    bytes public memoryStored;

    function callDatacopy(bytes memory data) public returns (bytes memory)
        }

        memoryStored = result;

        return result;
    }
}
```

With the contract deployed, you can call the `callDataCopy()` method and verify if `memoryStored` matches the bytes that you pass in as an input of the function.

## Modular Exponentiation {: #modular-exponentiation }

This precompile calculates the remainder when an integer `b` (base) is raised to the `e`-th power (the exponent), and is divided by a positive integer `m` (the modulus).

The Solidity compiler does not support it, so it needs to be called with inline assembly. The following code was simplified to show the functionality of this precompile:

```solidity
pragma solidity ^0.7.0;

contract ModularCheck {
    uint public checkResult;

    // Function to Verify ModExp Result
    function verify(uint _base, uint _exp, uint _modulus) public {
        checkResult = modExp(_base, _exp, _modulus);
    }

    function modExp(
        uint256 _b,
        uint256 _e,
        uint256 _m
    ) public returns (uint256 result)
            result := mload(value)
        }
    }
}
```

You can try this in [Remix](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/). Use the function `verify()`, passing the base, exponent, and modulus. The function will store the value in the `checkResult` variable.

## P256 Verify {: #p256-verify }

The P256Verify Precompile adds support for [RIP-7212](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7212.md), signature verification for Secp256r1 elliptic curve. This precompile adds a WASM implementation of the signature verification and is intended to be replaced by a native runtime function call once available.

```solidity
// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >=0.8.3;

contract P256Verify {
    function verify(
        bytes32 msg_hash,
        bytes32[2] memory signature,
        bytes32[2] memory public_key
    ) public view returns (bool)
        require(success, "p256verify precompile call failed");

        return output;
    }
}
```

The file below contains two different test cases: one with a valid signature test and a second with an invalid signature test.

??? code "p256verifywithtests.sol"
    ```solidity
    // SPDX-License-Identifier: GPL-3.0-only
    pragma solidity >=0.8.3;

    contract P256Verify {
        function verify(
            bytes32 msg_hash,
            bytes32[2] memory signature,
            bytes32[2] memory public_key
        ) public view returns (bool)
            require(success, "p256verify precompile call failed");

            return output;
        }

        function test() public {
            bytes32[2] memory msg_hashes;
            bytes32[2][2] memory signatures;
            bytes32[2][2] memory public_keys;
            bool[2] memory expected_result;

            // Case 1 (valid)
            msg_hashes[0] = hex"b5a77e7a90aa14e0bf5f337f06f597148676424fae26e175c6e5621c34351955";
            signatures[0][0] = hex"289f319789da424845c9eac935245fcddd805950e2f02506d09be7e411199556";
            signatures[0][1] = hex"d262144475b1fa46ad85250728c600c53dfd10f8b3f4adf140e27241aec3c2da";
            public_keys[0][0] = hex"3a81046703fccf468b48b145f939efdbb96c3786db712b3113bb2488ef286cdc";
            public_keys[0][1] = hex"ef8afe82d200a5bb36b5462166e8ce77f2d831a52ef2135b2af188110beaefb1";
            expected_result[0] = true;

            // Case 2 (invalid)
            msg_hashes[1] = hex"d182e6ad7f520e511f6c3e2b8c68059b6bbd41fbabd9831f79217e1319cde05b";
            signatures[1][0] = hex"6162630000000000000000000000000000000000000000000000000000000000";
            signatures[1][1] = hex"6162630000000000000000000000000000000000000000000000000000000000";
            public_keys[1][0] = hex"6162630000000000000000000000000000000000000000000000000000000000";
            public_keys[1][1] = hex"6162630000000000000000000000000000000000000000000000000000000000";
            expected_result[0] = false;

            for (uint256 i = 0; i < expected_result.length; i++) else {
                    require(!result, "Expected failure");
                }
            }
        }
    }
    ```

Using the [Remix compiler and deployment](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) and with [MetaMask pointing to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/), you can deploy the contract and call the `verify` method with the following parameters: 

=== "Valid Signature"

	| Parameter    | Value                                                                                                                                          |
	|--------------|------------------------------------------------------------------------------------------------------------------------------------------------|
	| `msg_hash`   | `0xb5a77e7a90aa14e0bf5f337f06f597148676424fae26e175c6e5621c34351955`                                                                           |
	| `signature`  | `["0x289f319789da424845c9eac935245fcddd805950e2f02506d09be7e411199556", "0xd262144475b1fa46ad85250728c600c53dfd10f8b3f4adf140e27241aec3c2da"]` |
	| `public_key` | `["0x3a81046703fccf468b48b145f939efdbb96c3786db712b3113bb2488ef286cdc", "0xef8afe82d200a5bb36b5462166e8ce77f2d831a52ef2135b2af188110beaefb1"]` | 
	| Expected Result | `true`                                                                                                                                        |

=== "Invalid Signature"

	| Parameter       | Value                                                                                                                                          |
	|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
	| `msg_hash`      | `0xd182e6ad7f520e511f6c3e2b8c68059b6bbd41fbabd9831f79217e1319cde05b`                                                                           |
	| `signature`     | `["0x6162630000000000000000000000000000000000000000000000000000000000", "0x6162630000000000000000000000000000000000000000000000000000000000"]` |
	| `public_key`    | `["0x6162630000000000000000000000000000000000000000000000000000000000", "0x6162630000000000000000000000000000000000000000000000000000000000"]` |
	| Expected Result | `false`                                                                                                                                        |

You'll receive two booleans in response; the first one indicates whether the signature was valid, and the second indicates whether the call to the P256Verify precompile was successful. The second boolean should always return true; the first is the one to check to see if the signature is valid.
