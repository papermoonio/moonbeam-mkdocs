---
title: How to use the Python Substrate Interface
description: Learn the basics of how to use the Python Substrate Interface library to query chain data, send transactions, and more on Moonbeam networks.
categories:
- Substrate Toolkit
- Libraries and SDKs
url: https://docs.moonbeam.network/builders/substrate/libraries/py-substrate-interface/
word_count: 2115
token_estimate: 3455
version_hash: sha256:6434c7974d4a7b7d86c38cac6af95858e30de0d94ba23bbffa88d15c7cf6ad53
last_updated: '2026-05-21T21:21:53+00:00'
---

# Python Substrate Interface

## Introduction {: #introduction }

[Python Substrate Interface](https://github.com/polkascan/py-substrate-interface) library allows application developers to query a Moonbeam node and interact with the node's Polkadot or Substrate features using a native Python interface. Here you will find an overview of the available functionalities and some commonly used code examples to get you started on interacting with Moonbeam networks using Python Substrate Interface.

## Checking Prerequisites {: #checking-prerequisites }

For the examples in this guide, you will need to have the following:

 - An account with funds.
  You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
 - 
  To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/)
 - Have [`pip`](https://pypi.org/project/pip) installed

!!! note
    The examples in this guide assume you have a MacOS or Ubuntu 22.04-based environment and will need to be adapted accordingly for Windows.
### Installing Python Substrate Interface {: #installing-python-substrate-interface }

You can install Python Substrate Interface library for your project through `pip`. Run the following command in your project directory:

```bash
pip install substrate-interface
```

## Creating an API Provider Instance {: #creating-an-API-provider-instance }

Similar to ETH API libraries, you must first instantiate an API instance of Python Substrate Interface API. Create the `WsProvider` using the websocket endpoint of the Moonbeam network you wish to interact with.

To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
=== "Moonbeam"

    ```python
    # Imports
    from substrateinterface import SubstrateInterface

    # Construct the API provider
    ws_provider = SubstrateInterface(
        url="INSERT_WSS_API_ENDPOINT",
    ) 
    ```

=== "Moonriver"

    ```python
    # Imports
    from substrateinterface import SubstrateInterface

    # Construct the API provider
    ws_provider = SubstrateInterface(
        url="INSERT_WSS_API_ENDPOINT",
    )   
    ```

=== "Moonbase Alpha"

    ```python
    # Imports
    from substrateinterface import SubstrateInterface

    # Construct the API provider
    ws_provider = SubstrateInterface(
        url="wss://wss.api.moonbase.moonbeam.network",
    )   
    ```

=== "Moonbeam Dev Node"

    ```python
    # Import
    from substrateinterface import SubstrateInterface

    # Construct the API provider
    ws_provider = SubstrateInterface(
        url="ws://127.0.0.1:9944",
    )   
    ```

## Querying for Information {: #querying-for-information }

In this section, you will learn how to query for on-chain information of Moonbeam networks using Python Substrate Interface library.

### Accessing Runtime Constants {: #accessing-runtime-constants }

All runtime constants, such as `BlockWeights`, `DefaultBlocksPerRound` and `ExistentialDeposit`, are provided in the metadata. You can use the [`get_metadata_constants`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.get_metadata_constants) method to see a list of available runtime constants within Moonbeam network's metadata.

Runtime constants available in the metadata can be queried through the [`get_constant`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.get_constant) method.

```python
# Imports
from substrateinterface import SubstrateInterface

# Construct the API provider
ws_provider = SubstrateInterface(
    url="wss://wss.api.moonbase.moonbeam.network",
)   

# List of available runtime constants in the metadata
constant_list = ws_provider.get_metadata_constants()
print(constant_list)

# Retrieve the Existential Deposit constant on Moonbeam, which is 0
constant = ws_provider.get_constant("Balances", "ExistentialDeposit")
print(constant.value)
```

### Retrieving Blocks and Extrinsics {: #retrieving-blocks-and-extrinsics }

You can retrieve basic information about Moonbeam networks, such as blocks and extrinsics, using the Python Substrate Interface API.

To retrieve a block, you can use the [`get_block`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.get_block) method. You can also access extrinsics and their data fields inside a block object, which is simply a Python dictionary.

To retrieve a block header, you can use the [`get_block_header`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.get_block_header) method.  

```python
# Imports
from substrateinterface import SubstrateInterface

# Construct the API provider
ws_provider = SubstrateInterface(
    url="wss://wss.api.moonbase.moonbeam.network",
)

# Retrieve the latest block
block = ws_provider.get_block()

# Retrieve the latest finalized block
block = ws_provider.get_block_header(finalized_only=True)

# Retrieve a block given its Substrate block hash
block_hash = "0xa499d4ebccdabe31218d232460c0f8b91bd08f72aca25f9b25b04b6dfb7a2acb"
block = ws_provider.get_block(block_hash=block_hash)

# Iterate through the extrinsics inside the block
for extrinsic in block["extrinsics"]:
    if "address" in extrinsic:
        signed_by_address = extrinsic["address"].value
    else:
        signed_by_address = None
    print(
        "\nPallet: {}\nCall: {}\nSigned by: {}".format(
            extrinsic["call"]["call_module"].name,
            extrinsic["call"]["call_function"].name,
            signed_by_address,
        )
    )
```

!!! note
    The block hash used in the above code sample is the Substrate block hash. The standard methods in Python Substrate Interface assume you are using the Substrate version of primitives, such as block or tx hashes.

### Subscribing to New Block Headers {: #subscribing-to-new-block-headers }

You can also adapt the previous example to use a subscription based model to listen to new block headers.

```python
# Imports
from substrateinterface import SubstrateInterface

# Construct the API provider
ws_provider = SubstrateInterface(
    url="wss://wss.api.moonbase.moonbeam.network",
)


def subscription_handler(obj, update_nr, subscription_id):
    print(f"New block #{obj['header']['number']}")

    if update_nr > 10:
        return {
            "message": "Subscription will cancel when a value is returned",
            "updates_processed": update_nr,
        }


result = ws_provider.subscribe_block_headers(subscription_handler)
```

### Querying for Storage Information {: #querying-for-storage-information }

You can use the [`get_metadata_storage_functions`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.get_metadata_storage_functions) to see a list of available storage functions within Moonbeam network's metadata.

Chain states that are provided in the metadata through storage functions can be queried through the [`query`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.query) method.

The Substrate system modules, such as `System`, `Timestamp`, and `Balances`, can be queried to provide basic information such as account nonce and balance. The available storage functions are read from the metadata dynamically, so you can also query for storage information on Moonbeam custom modules, such as `ParachainStaking` and `Democracy`, for state information that's specific to Moonbeam.

```python
# Imports
from substrateinterface import SubstrateInterface

# Construct the API provider
ws_provider = SubstrateInterface(
    url="wss://wss.api.moonbase.moonbeam.network",
)

# List of available storage functions in the metadata
method_list = ws_provider.get_metadata_storage_functions()
print(method_list)

# Query basic account information
account_info = ws_provider.query(
    module="System",
    storage_function="Account",
    params=["0x578002f699722394afc52169069a1FfC98DA36f1"],
)
# Log the account nonce
print(account_info.value["nonce"])
# Log the account free balance
print(account_info.value["data"]["free"])

# Query candidate pool information from Moonbeam's Parachain Staking module
candidate_pool_info = ws_provider.query(
    module="ParachainStaking", storage_function="CandidatePool", params=[]
)
print(candidate_pool_info)
```

## Signing and Transactions {: #signing-and-transactions }

### Creating a Keypair {: #creating-a-keypair }

The keypair object in Python Substrate Interface is used in the signing of any data, whether it's a transfer, a message, or a contract interaction.  

You can create a keypair instance from the shortform private key or from the mnemonic. For Moonbeam networks, you also need to specify the `KeypairType` to be `KeypairType.ECDSA`.

```python
# Imports
from substrateinterface import Keypair, KeypairType

# Define the shortform private key
privatekey = bytes.fromhex("INSERT_PRIVATE_KEY_WITHOUT_0X_PREFIX")

# Define the account mnemonic
mnemonic = "INSERT_MNEMONIC"

# Generate the keypair from shortform private key
keypair = Keypair.create_from_private_key(privatekey, crypto_type=KeypairType.ECDSA)

# Generate the keypair from mnemonic
keypair = Keypair.create_from_mnemonic(mnemonic, crypto_type=KeypairType.ECDSA)
```

### Forming and Sending a Transaction {: #forming-and-sending-a-transaction }

The [`compose_call`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.compose_call) method can be used to compose a call payload which can be used as an unsigned extrinsic or a proposal.

Then the payload can be signed using a keypair through the [`create_signed_extrinsic`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.create_signed_extrinsic) method.

The signed extrinsic can then be submitted using the [`submit_extrinsic`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.submit_extrinsic) method.

This method will also return an `ExtrinsicReceipt` object which contains information about the on-chain execution of the extrinsic. If you need to examine the receipt object, you can set the `wait_for_inclusion` to `True` when submitting the extrinsic to wait until the extrinsic is successfully included into the block.

The following sample code will show a complete example for sending a transaction.

```python
# Imports
from substrateinterface import SubstrateInterface, Keypair, KeypairType
from substrateinterface.exceptions import SubstrateRequestException

# Construct the API provider
ws_provider = SubstrateInterface(
    url="wss://wss.api.moonbase.moonbeam.network",
)

# Define the shortform private key of the sending account
privatekey = bytes.fromhex("INSERT_PRIVATE_KEY_WITHOUT_0X_PREFIX")

# Generate the keypair
keypair = Keypair.create_from_private_key(privatekey, crypto_type=KeypairType.ECDSA)

# Form a transaction call
call = ws_provider.compose_call(
    call_module="Balances",
    call_function="transfer_allow_death",
    call_params={
        "dest": "0x44236223aB4291b93EEd10E4B511B37a398DEE55",
        "value": 1 * 10**18,
    },
)

# Form a signed extrinsic
extrinsic = ws_provider.create_signed_extrinsic(call=call, keypair=keypair)

# Submit the extrinsic
try:
    receipt = ws_provider.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    print(
        "Extrinsic '{}' sent and included in block '{}'".format(
            receipt.extrinsic_hash, receipt.block_hash
        )
    )
except SubstrateRequestException as e:
    print("Failed to send: {}".format(e))
```

### Offline Signing {: #offline-signing }

You can sign transaction payloads or any arbitrary data using a keypair object through the [`sign`](https://jamdottech.github.io/py-polkadot-sdk/reference/keypair/#substrateinterface.keypair.Keypair.sign) method. This can be used for offline signing of transactions.

1. First, generate the signature payload on an online machine:

    ```python
    # Imports
    from substrateinterface import SubstrateInterface

    # Construct the API provider
    ws_provider = SubstrateInterface(
        url="wss://wss.api.moonbase.moonbeam.network",
    )

    # Construct a transaction call
    call = ws_provider.compose_call(
        call_module="Balances",
        call_function="transfer_allow_death",
        call_params={
            "dest": "0x44236223aB4291b93EEd10E4B511B37a398DEE55",
            "value": 1 * 10**18,
        },
    )

    # Generate the signature payload
    signature_payload = ws_provider.generate_signature_payload(call=call)
    ```

2. On an offline machine, create a keypair with the private key of the sending account, and sign the signature payload:

    ```python
    # Imports
    from substrateinterface import Keypair, KeypairType

    # Define the signature payload from the offline machine
    signature_payload = "INSERT_SIGNATURE_PAYLOAD"

    # Define the shortform private key of the sender account
    privatekey = bytes.fromhex("INSERT_PRIVATE_KEY_WITHOUT_0X_PREFIX")

    # Generate the keypair from shortform private key
    keypair = Keypair.create_from_private_key(privatekey, crypto_type=KeypairType.ECDSA)

    # Sign the signature_payload 
    signature = keypair.sign(signature_payload)
    ```

3. On an online machine, create a keypair with the public key of the sending account, and submit the extrinsic with the generated signature from the offline machine:

    ```python
    # Imports
    from substrateinterface import SubstrateInterface, Keypair, KeypairType

    # Construct the API provider
    ws_provider = SubstrateInterface(
        url="wss://wss.api.moonbase.moonbeam.network",
    )

    # Define the signature from the offline machine
    signature_payload = "INSERT_SIGNATURE_PAYLOAD"

    # Construct a keypair with the Ethereum style wallet address of the sending account
    keypair = Keypair(public_key="INSERT_ADDRESS_WITHOUT_0X", crypto_type=KeypairType.ECDSA)

    # Construct the same transaction call that was signed
    call = ws_provider.compose_call(
        call_module="Balances",
        call_function="transfer_allow_death",
        call_params={
            "dest": "0x44236223aB4291b93EEd10E4B511B37a398DEE55",
            "value": 1 * 10**18,
        },
    )

    # Construct the signed extrinsic with the generated signature
    extrinsic = ws_provider.create_signed_extrinsic(
        call=call, keypair=keypair, signature=signature
    )

    # Submit the signed extrinsic
    result = ws_provider.submit_extrinsic(extrinsic=extrinsic)

    # Print the execution result
    print(result.extrinsic_hash)
    ```

## Custom RPC Requests {: #custom-rpc-requests }

You can also make custom RPC requests with the [`rpc_request`](https://jamdottech.github.io/py-polkadot-sdk/reference/base/#substrateinterface.base.SubstrateInterface.rpc_request) method.

This is particularly useful for interacting with Moonbeam's [Ethereum JSON-RPC](/moonbeam-mkdocs/builders/ethereum/json-rpc/eth-rpc/) endpoints or Moonbeam's [custom RPC](/moonbeam-mkdocs/builders/ethereum/json-rpc/moonbeam-custom-api/) endpoints.

The [Consensus and Finality page](/moonbeam-mkdocs/learn/core-concepts/consensus-finality/#checking-tx-finality-with-substrate-libraries) has examples for using the custom RPC calls through Python Substrate Interface to check the finality of a transaction given its transaction hash.

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
