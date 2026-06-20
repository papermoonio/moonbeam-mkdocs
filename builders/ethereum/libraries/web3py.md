---
title: How to use Web3.py Ethereum Library
description: Follow this tutorial to learn how to use the Ethereum Web3 Python Library to to send transactions and deploy Solidity smart contracts to Moonbeam.
categories:
- Libraries and SDKs
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/libraries/web3py/
word_count: 3878
token_estimate: 6331
version_hash: sha256:c407013f7c7ce200f75fa8ebaf4b7b7993e4701eca7e8f070cf6a71703f8be3b
last_updated: '2026-05-21T21:21:53+00:00'
---

# Web3.py Python Library

## Introduction {: #introduction }

[Web3.py](https://web3py.readthedocs.io) is a set of libraries that allow developers to interact with Ethereum nodes using HTTP, IPC, or WebSocket protocols with Python. Moonbeam has an Ethereum-like API available that is fully compatible with Ethereum-style JSON-RPC invocations. Therefore, developers can leverage this compatibility and use the Web3.py library to interact with a Moonbeam node as if they were doing so on Ethereum.

In this guide, you'll learn how to use the Web3.py library to send a transaction and deploy a contract on Moonbase Alpha. This guide can be adapted for [Moonbeam](/moonbeam-mkdocs/builders/get-started/networks/moonbeam/), [Moonriver](/moonbeam-mkdocs/builders/get-started/networks/moonriver/), or a [Moonbeam development node](/moonbeam-mkdocs/builders/get-started/networks/moonbeam-dev/).

## Checking Prerequisites {: #checking-prerequisites }

For the examples in this guide, you will need to have the following:

 - An account with funds.
  You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
 - 
To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/)
!!! note
    The examples in this guide assume you have a MacOS or Ubuntu 22.04-based environment and will need to be adapted accordingly for Windows.
## Create a Python Project {: #create-a-python-project }

To get started, you can create a directory to store all of the files you'll be creating throughout this guide:

```bash
mkdir web3-examples && cd web3-examples
```

For this guide, you'll need to install the Web3.py library and the Solidity compiler. To install both packages, you can run the following command:

```bash
pip3 install web3 py-solc-x solc-select
```

## Setup Web3.py with Moonbeam {: #setup-web3-with-moonbeam }

Throughout this guide, you'll be creating a bunch of scripts that provide different functionalities, such as sending a transaction, deploying a contract, and interacting with a deployed contract. In most of these scripts, you'll need to create a [Web3.py provider](https://web3py.readthedocs.io/en/stable/providers.html) to interact with the network.

To configure your project for Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
To create a provider, you can take the following steps:

1. Import the `web3` library
2. Create the `web3` provider using the `Web3(Web3.HTTPProvider())` method and providing the endpoint URL

=== "Moonbeam"

    ```python
    # 1. Import web3.py
    from web3 import Web3

    # 2. Create web3.py provider
    web3 = Web3(Web3.HTTPProvider("INSERT_RPC_API_ENDPOINT")) # Insert your RPC URL here
    ```

=== "Moonriver"

    ```python
    # 1. Import web3.py
    from web3 import Web3

    # 2. Create web3.py provider
    web3 = Web3(Web3.HTTPProvider("INSERT_RPC_API_ENDPOINT")) # Insert your RPC URL here
    ```

=== "Moonbase Alpha"

    ```python
    # 1. Import web3.py
    from web3 import Web3

    # 2. Create web3.py provider
    web3 = Web3(Web3.HTTPProvider("https://rpc.api.moonbase.moonbeam.network"))
    ```

=== "Moonbeam Dev Node"

    ```python
    # 1. Import web3.py
    from web3 import Web3

    # 2. Create web3.py provider
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:9944"))
    ```

Save this code snippet, as you'll need it for the scripts that are used in the following sections.

## Send a Transaction {: #send-a-transaction }

During this section, you'll be creating a couple of scripts. The first one will be to check the balances of your accounts before trying to send a transaction. The second script will actually send the transaction.

You can also use the balance script to check the account balances after the transaction has been sent.

### Check Balances Script {: #check-balances-script }

You'll only need one file to check the balances of both addresses before and after the transaction is sent.  To get started, you can create a `balances.py` file by running:

```bash
touch balances.py
```

Next, you will create the script for this file and complete the following steps:

1. [Set up the Web3 provider](#setup-web3-with-moonbeam)
2. Define the `address_from` and `address_to` variables
3. Get the balance for the accounts using the `web3.eth.get_balance` function and format the results using the `web3.from_wei`

```python
from web3 import Web3

# 1. Add the Web3 provider logic here:
provider_rpc = {
    "development": "http://localhost:9944",
    "moonbase": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["moonbase"]))  # Change to correct network

# 2. Create address variables
address_from = 'INSERT_FROM_ADDRESS'
address_to = 'INSERT_TO_ADDRESS'

# 3. Fetch balance data
balance_from = web3.from_wei(
    web3.eth.get_balance(Web3.to_checksum_address(address_from)), "ether"
)
balance_to = web3.from_wei(
    web3.eth.get_balance(Web3.to_checksum_address(address_to)), "ether"
)

print(f"The balance of { address_from } is: { balance_from } DEV")
print(f"The balance of { address_to } is: { balance_to } DEV")
```

To run the script and fetch the account balances, you can run the following command:

```bash
python3 balances.py
```

If successful, the balances for the origin and receiving address will be displayed in your terminal in ETH.

### Send Transaction Script {: #send-transaction-script }

You'll only need one file for executing a transaction between accounts. For this example, you'll be transferring 1 DEV token from an origin address (from which you hold the private key) to another address. To get started, you can create a `transaction.py` file by running:

```bash
touch transaction.py
```

Next, you will create the script for this file and complete the following steps:

1. Add imports, including Web3.py and the `rpc_gas_price_strategy`, which will be used in the following steps to get the gas price used for the transaction
2. [Set up the Web3 provider](#setup-web3-with-moonbeam)
3. Define the `account_from`, including the `private_key`, and the `address_to` variables. The private key is required to sign the transaction. **Note: This is for example purposes only. Never store your private keys in a Python file**
4. Use the [Web3.py Gas Price API](https://web3py.readthedocs.io/en/stable/gas_price.html) to set a gas price strategy. For this example, you'll use the imported `rpc_gas_price_strategy`
5. Create and sign the transaction using the `web3.eth.account.sign_transaction` function. Pass in the `nonce` `gas`, `gasPrice`, `to`, and `value` for the transaction along with the sender's `private_key`. To get the `nonce` you can use the `web3.eth.get_transaction_count` function and pass in the sender's address. To predetermine the `gasPrice` you'll use the `web3.eth.generate_gas_price` function. For the `value`, you can format the amount to send from an easily readable format to Wei using the `web3.to_wei` function
6. Using the signed transaction, you can then send it using the `web3.eth.send_raw_transaction` function and wait for the transaction receipt by using the `web3.eth.wait_for_transaction_receipt` function

```python
# 1. Add imports
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from web3 import Web3

# 2. Add the Web3 provider logic here:
provider_rpc = {
    "development": "http://localhost:9944",
    "moonbase": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["moonbase"]))  # Change to correct network

# 3. Create address variables
account_from = {
    'private_key': 'INSERT_YOUR_PRIVATE_KEY',
    'address': 'INSERT_PUBLIC_ADDRESS_OF_PK',
}
address_to = 'INSERT_TO_ADDRESS'

print(
    f'Attempting to send transaction from { account_from["address"] } to { address_to }'
)

# 4. Set the gas price strategy
web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

# 5. Sign tx with PK
tx_create = web3.eth.account.sign_transaction(
    {
        "nonce": web3.eth.get_transaction_count(
            Web3.to_checksum_address(account_from["address"])
        ),
        "gasPrice": web3.eth.generate_gas_price(),
        "gas": 21000,
        "to": Web3.to_checksum_address(address_to),
        "value": web3.to_wei("1", "ether"),
    },
    account_from["private_key"],
)

# 6. Send tx and wait for receipt
tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction successful with hash: { tx_receipt.transactionHash.hex() }")
```

To run the script, you can run the following command in your terminal:

```bash
python3 transaction.py
```

If the transaction was successful, in your terminal you'll see the transaction hash has been printed out.

You can also use the `balances.py` script to check that the balances for the origin and receiving accounts have changed. The entire workflow would look like this:

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>python3 balances.py</span>
    <span data-ty>The balance of 0x3B939FeaD1557C741Ff06492FD0127bd287A421e is: 3563.79 DEV</span>
    <span data-ty>The balance of 0x9Bf5Ae10540a1ab9B363bEA02A9406E6b2efA9af is: 0 DEV</span>
    <span data-ty="input"><span class="file-path"></span>python3 transaction.py</span>
    <span data-ty>Attempting to send transaction from 0x3B939FeaD1557C741Ff06492FD0127bd287A421e to 0x9Bf5Ae10540a1ab9B363bEA02A9406E6b2efA9af</span>
    <span data-ty>Transaction successful with hash: 0xac70452510657ed43c27510578d3ce4b3b880d4cca1a24ade1497c6e0ee7f5d6</span>
    <span data-ty="input"><span class="file-path"></span>python3 balances.py</span>
    <span data-ty>The balance of 0x3B939FeaD1557C741Ff06492FD0127bd287A421e is: 3562.79 DEV</span>
    <span data-ty>The balance of 0x9Bf5Ae10540a1ab9B363bEA02A9406E6b2efA9af is: 1 DEV</span>
    <span data-ty="input"><span class="file-path">
</div>
## Deploy a Contract {: #deploy-a-contract }

The contract you'll be compiling and deploying in the next couple of sections is a simple incrementer contract, arbitrarily named `Incrementer.sol`. You can get started by creating a file for the contract:

```bash
touch Incrementer.sol
```

Next, you can add the Solidity code to the file:

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.30;

contract Incrementer {
    uint256 public number;

    constructor(uint256 _initialNumber)

    function increment(uint256 _value) public {
        number = number + _value;
    }

    function reset() public {
        number = 0;
    }
}
```

The `constructor` function, which runs when the contract is deployed, sets the initial value of the number variable stored on-chain (the default is `0`). The `increment` function adds the `_value` provided to the current number, but a transaction needs to be sent, which modifies the stored data. Lastly, the `reset` function resets the stored value to zero.

!!! note
    This contract is a simple example for illustration purposes only and does not handle values wrapping around.
### Compile Contract Script {: #compile-contract-script }

In this section, you'll create a script that uses the Solidity compiler to output the bytecode and interface (ABI) for the `Incrementer.sol` contract. To get started, you can create a `compile.py` file by running:

```bash
touch compile.py
```

Next, you will create the script for this file and complete the following steps:

1. Import the `solcx` package
2. **Optional** - If you haven't already installed the Solidity compiler, you can do so with by using the `solcx.install_solc` function
3. Compile the `Incrementer.sol` function using the `solcx.compile_files` function
4. Export the contract's ABI and bytecode

```python
# 1. Import solcx
import solcx

# 2. If you haven't already installed the Solidity compiler, uncomment the following line
# solcx.install_solc()

# 3. Compile contract
temp_file = solcx.compile_files(
    'Incrementer.sol',
    output_values=['abi', 'bin'],
    # solc_version='0.8.19'
)

# 4. Export contract data
abi = temp_file['Incrementer.sol:Incrementer']['abi']
bytecode = temp_file['Incrementer.sol:Incrementer']['bin']
```

!!! note
    If you see an error stating that `Solc is not installed`, uncomment step 2 described in the code snippet.

### Deploy Contract Script {: #deploy-contract-script }

With the script for compiling the `Incrementer.sol` contract in place, you can then use the results to send a signed transaction that deploys it. To do so, you can create a file for the deployment script called `deploy.py`:

```bash
touch deploy.py
```

Next, you will create the script for this file and complete the following steps:

1. Add imports, including Web3.py and the ABI and bytecode of the `Incrementer.sol` contract
2. [Set up the Web3 provider](#setup-web3-with-moonbeam)
3. Define the `account_from`, including the `private_key`. The private key is required to sign the transaction. **Note: This is for example purposes only. Never store your private keys in a Python file**
4. Create a contract instance using the `web3.eth.contract` function and passing in the ABI and bytecode of the contract
5. Build a constructor transaction using the contract instance and passing in the value to increment by. For this example, you can use `5`. You'll then use the `build_transaction` function to pass in the transaction information including the `from` address and the `nonce` for the sender. To get the `nonce` you can use the `web3.eth.get_transaction_count` function 
6. Sign the transaction using the `web3.eth.account.sign_transaction` function and pass in the constructor transaction and the `private_key` of the sender
7. Using the signed transaction, you can then send it using the `web3.eth.send_raw_transaction` function and wait for the transaction receipt by using the `web3.eth.wait_for_transaction_receipt` function

```python
# 1. Add imports
from compile import abi, bytecode
from web3 import Web3

# 2. Add the Web3 provider logic here:
provider_rpc = {
    "development": "http://localhost:9944",
    "moonbase": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["moonbase"]))  # Change to correct network

# 3. Create address variable
account_from = {
    'private_key': 'INSERT_YOUR_PRIVATE_KEY',
    'address': 'INSERT_PUBLIC_ADDRESS_OF_PK',
}

print(f'Attempting to deploy from account: { account_from["address"] }')

# 4. Create contract instance
Incrementer = web3.eth.contract(abi=abi, bytecode=bytecode)

# 5. Build constructor tx
construct_txn = Incrementer.constructor(5).build_transaction(
    {
        "from": Web3.to_checksum_address(account_from["address"]),
        "nonce": web3.eth.get_transaction_count(
            Web3.to_checksum_address(account_from["address"])
        ),
    }
)

# 6. Sign tx with PK
tx_create = web3.eth.account.sign_transaction(
    construct_txn, account_from["private_key"]
)

# 7. Send tx and wait for receipt
tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Contract deployed at address: { tx_receipt.contractAddress }")
```

To run the script, you can enter the following command into your terminal:

```bash
python3 deploy.py
```

If successful, the contract's address will be displayed in the terminal.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>python3 deploy.py</span>
    <span data-ty>Attempting to deploy from account: 0x3B939FeaD1557C741Ff06492FD0127bd287A421e</span>
    <span data-ty>Contract deployed at address: 0xFef3cFb8eE1FE727b3848E551ae5DC8903237B08</span>
    <span data-ty="input"><span class="file-path">
</div>
### Read Contract Data (Call Methods)

Call methods are the type of interaction that don't modify the contract's storage (change variables), meaning no transaction needs to be sent. They simply read various storage variables of the deployed contract.

To get started, you can create a file and name it `get.py`:

```bash
touch get.py
```

Then you can take the following steps to create the script:

1. Add imports, including Web3.py and the ABI of the `Incrementer.sol` contract
2. [Set up the Web3 provider](#setup-web3-with-moonbeam)
3. Define the `contract_address` of the deployed contract
4. Create a contract instance using the `web3.eth.contract` function and passing in the ABI and address of the deployed contract
5. Using the contract instance, you can then call the `number` function

```python
# 1. Import the ABI
from compile import abi
from web3 import Web3

# 2. Add the Web3 provider logic here:
provider_rpc = {
    "development": "http://localhost:9944",
    "moonbase": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["moonbase"]))  # Change to correct network

# 3. Create address variable
contract_address = 'INSERT_CONTRACT_ADDRESS'

print(f"Making a call to contract at address: { contract_address }")

# 4. Create contract instance
Incrementer = web3.eth.contract(address=contract_address, abi=abi)

# 5. Call Contract
number = Incrementer.functions.number().call()
print(f"The current number stored is: { number } ")
```

To run the script, you can enter the following command in your terminal:

```bash
python3 get.py
```

If successful, the value will be displayed in the terminal.

### Interact with Contract (Send Methods)

Send methods are the type of interaction that modify the contract's storage (change variables), meaning a transaction needs to be signed and sent. In this section, you'll create two scripts: one to increment and one to reset the incrementer. To get started, you can create a file for each script and name them `increment.py` and `reset.py`:

```bash
touch increment.py reset.py
```

Open the `increment.py` file and take the following steps to create the script:

1. Add imports, including Web3.py and the ABI of the `Incrementer.sol` contract
2. [Set up the Web3 provider](#setup-web3-with-moonbeam)
3. Define the `account_from`, including the `private_key`, the `contract_address` of the deployed contract, and the `value` to increment by. The private key is required to sign the transaction. **Note: This is for example purposes only. Never store your private keys in a Python file**
4. Create a contract instance using the `web3.eth.contract` function and passing in the ABI and address of the deployed contract
5. Build the increment transaction using the contract instance and passing in the value to increment by. You'll then use the `build_transaction` function to pass in the transaction information including the `from` address and the `nonce` for the sender. To get the `nonce` you can use the `web3.eth.get_transaction_count` function
6. Sign the transaction using the `web3.eth.account.sign_transaction` function and pass in the increment transaction and the `private_key` of the sender
7. Using the signed transaction, you can then send it using the `web3.eth.send_raw_transaction` function and wait for the transaction receipt by using the `web3.eth.wait_for_transaction_receipt` function

```python
# 1. Add imports
from compile import abi
from web3 import Web3

# 2. Add the Web3 provider logic here:
provider_rpc = {
    "development": "http://localhost:9944",
    "moonbase": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["moonbase"]))  # Change to correct network

# 3. Create variables
account_from = {
    'private_key': 'INSERT_YOUR_PRIVATE_KEY',
    'address': 'INSERT_PUBLIC_ADDRESS_OF_PK',
}
contract_address = 'INSERT_CONTRACT_ADDRESS'
value = 3

print(
    f"Calling the increment by { value } function in contract at address: { contract_address }"
)

# 4. Create contract instance
Incrementer = web3.eth.contract(address=contract_address, abi=abi)

# 5. Build increment tx
increment_tx = Incrementer.functions.increment(value).build_transaction(
    {
        "from": Web3.to_checksum_address(account_from["address"]),
        "nonce": web3.eth.get_transaction_count(
            Web3.to_checksum_address(account_from["address"])
        ),
    }
)

# 6. Sign tx with PK
tx_create = web3.eth.account.sign_transaction(increment_tx, account_from["private_key"])

# 7. Send tx and wait for receipt
tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Tx successful with hash: { tx_receipt.transactionHash.hex() }")
```

To run the script, you can enter the following command in your terminal:

```bash
python3 increment.py
```

If successful, the transaction hash will be displayed in the terminal. You can use the `get.py` script alongside the `increment.py` script to make sure that value is changing as expected:

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>python get.py</span>
    <span data-ty>Making a call to contract at address: 0xFef3cFb8eE1FE727b3848E551ae5DC8903237B08</span>
    <span data-ty>The current number stored is: 5</span>
    <span data-ty="input"><span class="file-path"></span>python increment.py</span>
    <span data-ty>Calling the increment by 3 function in contract at address: 0xFef3cFb8eE1FE727b3848E551ae5DC8903237B08</span>
    <span data-ty>Tx successful with hash: 0x47757fd97e3ef8db973e335d1f2d19c46b37d0dbd53fea1636ec559ccf119a13</span>
    <span data-ty="input"><span class="file-path"></span>python get.py</span>
    <span data-ty>Making a call to contract at address: 0xFef3cFb8eE1FE727b3848E551ae5DC8903237B08</span>
    <span data-ty>The current number stored is: 8</span>
    <span data-ty="input"><span class="file-path">
</div>
Next you can open the `reset.py` file and take the following steps to create the script:

1. Add imports, including Web3.py and the ABI of the `Incrementer.sol` contract
2. [Set up the Web3 provider](#setup-web3-with-moonbeam)
3. Define the `account_from`, including the `private_key`, and the `contract_address` of the deployed contract. The private key is required to sign the transaction. **Note: This is for example purposes only. Never store your private keys in a Python file**
4. Create a contract instance using the `web3.eth.contract` function and passing in the ABI and address of the deployed contract
5. Build the reset transaction using the contract instance. You'll then use the `build_transaction` function to pass in the transaction information including the `from` address and the `nonce` for the sender. To get the `nonce` you can use the `web3.eth.get_transaction_count` function
6. Sign the transaction using the `web3.eth.account.sign_transaction` function and pass in the reset transaction and the `private_key` of the sender
7. Using the signed transaction, you can then send it using the `web3.eth.send_raw_transaction` function and wait for the transaction receipt by using the `web3.eth.wait_for_transaction_receipt` function

```python
# 1. Add imports
from compile import abi
from web3 import Web3

# 2. Add the Web3 provider logic here:
provider_rpc = {
    "development": "http://localhost:9944",
    "moonbase": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["moonbase"]))  # Change to correct network

# 3. Create variables
account_from = {
    'private_key': 'INSERT_YOUR_PRIVATE_KEY',
    'address': 'INSERT_PUBLIC_ADDRESS_OF_PK',
}
contract_address = 'INSERT_CONTRACT_ADDRESS'

print(f"Calling the reset function in contract at address: { contract_address }")

# 4. Create contract instance
Incrementer = web3.eth.contract(address=contract_address, abi=abi)

# 5. Build reset tx
reset_tx = Incrementer.functions.reset().build_transaction(
    {
        "from": Web3.to_checksum_address(account_from["address"]),
        "nonce": web3.eth.get_transaction_count(
            Web3.to_checksum_address(account_from["address"])
        ),
    }
)

# 6. Sign tx with PK
tx_create = web3.eth.account.sign_transaction(reset_tx, account_from["private_key"])

# 7. Send tx and wait for receipt
tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Tx successful with hash: { tx_receipt.transactionHash.hex() }")
```

To run the script, you can enter the following command in your terminal:

```bash
python3 reset.py
```

If successful, the transaction hash will be displayed in the terminal. You can use the `get.py` script alongside the `reset.py` script to make sure that value is changing as expected:

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>python get.py</span>
    <span data-ty>Making a call to contract at address: 0xFef3cFb8eE1FE727b3848E551ae5DC8903237B08</span>
    <span data-ty>The current number stored is: 8</span>
    <span data-ty="input"><span class="file-path"></span>python reset.py</span>
    <span data-ty>Calling the reset function in contract at address: 0xFef3cFb8eE1FE727b3848E551ae5DC8903237B08</span>
    <span data-ty>Tx successful with hash: 0x152f07430b524838da848b44d58577db252681fba6fbeaf117b2f9d432e301b2</span>
    <span data-ty="input"><span class="file-path"></span>python get.py</span>
    <span data-ty>Making a call to contract at address: 0xFef3cFb8eE1FE727b3848E551ae5DC8903237B08</span>
    <span data-ty>The current number stored is: 0</span>
    <span data-ty="input"><span class="file-path">
</div>
<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
