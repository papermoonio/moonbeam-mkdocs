---
title: Deploy Contracts with Foundry
description: Learn how to use Foundry, an Ethereum development environment, to compile, deploy, and debug Solidity smart contracts on Moonbeam.
categories:
- Dev Environments
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/dev-env/foundry/
word_count: 5191
token_estimate: 9594
version_hash: sha256:e9b8c453d0e66b0a9eaa75d30ca20aca4402ea0298dccab5999748f4542d6e90
last_updated: '2026-05-21T21:21:53+00:00'
---

# Using Foundry to Deploy To Moonbeam

## Introduction {: #introduction }

[Foundry](https://github.com/foundry-rs/foundry) is an Ethereum development environment written in Rust that helps developers manage dependencies, compile projects, run tests, deploy contracts, and interact with blockchains from the command line. Foundry can directly interact with Moonbeam's Ethereum API so it can be used to deploy smart contracts into Moonbeam.

Four tools make up Foundry:  

- **[Forge](https://www.getfoundry.sh/forge)**: Compiles, tests, and deploys contracts.
- **[Cast](https://www.getfoundry.sh/cast)**: A command line interface for interacting with contracts.
- **[Anvil](https://www.getfoundry.sh/anvil)**: A local TestNet node for development purposes that can fork preexisting networks.
- **[Chisel](https://www.getfoundry.sh/chisel)**: A Solidity REPL for quickly testing Solidity snippets.

This guide will cover how to use Foundry to compile, deploy, and debug Ethereum smart contracts on the Moonbase Alpha TestNet. This guide can also be adapted for Moonbeam, Moonriver, or a Moonbeam development node.

## Checking Prerequisites {: #checking-prerequisites }

To get started, you will need the following:

 - Have an account with funds.
  You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network).
 - 
To test out the examples in this guide on Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
 - Have [Foundry installed](https://www.getfoundry.sh/introduction/installation)

## Creating a Foundry Project {: #creating-a-foundry-project }

You will need to create a Foundry project if you don't already have one. You can create one by completing the following steps:

1. Install Foundry if you haven't already. If on Linux or MacOS, you can run these commands:
  
    ```bash
    curl -L https://foundry.paradigm.xyz | bash
    foundryup
    ```

    If on Windows, you'll have to install Rust and then build Foundry from source:

    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs/ | sh
    cargo install --git https://github.com/foundry-rs/foundry foundry-cli anvil --bins --locked
    ```

2. Create the project, which will create a folder with three folders within it, and open it:

    ```bash
    forge init foundry && cd foundry
    ```

With the default project created, you should see three folders.  

- `lib`: All of the project's dependencies in the form of git submodules.
- `src`: Where to put your smart contracts (with functionality).
- `test`: Where to put the forge tests for your project, which are written in Solidity.

In addition to these three folders, a git project will also be created along with a prewritten `.gitignore` file with relevant file types and folders ignored.

## The Source Folder {: #the-src-folder }

The `src` folder may already contain `Counter.sol`, a minimal Solidity contract. Feel free to delete it. To avoid errors, you should also delete the `Counter.s.sol` file in the `scripts` folder and the `Counter.t.sol` file in the `test` folder. In the following steps, you will be deploying an ERC-20 contract. In the contracts directory, you can create the `MyToken.sol` file:

```bash
cd src
touch MyToken.sol
```

Open the file and add the following contract to it:

```solidity
pragma solidity ^0.8.30;

// Import OpenZeppelin Contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

// This ERC-20 contract mints the specified amount of tokens to the contract creator
contract MyToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("MyToken", "MYTOK")
}
```

Before you attempt to compile, install OpenZeppelin contracts as a dependency. You may have to commit previous changes to git beforehand. By default, Foundry uses git submodules instead of npm packages, so the traditional npm import path and command are not used. Instead, use the name of OpenZeppelin's GitHub repository:

```bash
forge install OpenZeppelin/openzeppelin-contracts
```

## Compiling Solidity {: #compiling-solidity }

Once all dependencies have been installed, you can compile the contract:

```bash
forge build
```

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>forge build</span>
    <span data-ty>[⠒] Compiling...</span>
    <span data-ty>[⠰] Compiling 30 files with 0.8.23</span>
    <span data-ty>[⠔] Solc 0.8.23 finished in 2.29s</span>
    <span data-ty>Compiler run successful!</span>
</div>
After compilation, two folders will be created: `out` and `cache`. The ABI and bytecode for your contracts will be contained within the `out` folder. These two folders are already ignored by the `.gitignore` included in the default Foundry project initialization.

## Deploying the Contract {: #deploying-the-contract }

There are two primary ways to deploy contracts using Foundry. The first is the straightforward command `forge create`. There's also the more flexible and powerful option of foundry scripting, which runs simulations before any deployments. In the following sections, `forge create` and foundry scripting will both be covered.

### Using Forge Create {: #using-forge-create }

Before deploying, you'll need to set up your keystore by importing your private key. You can do this using the `cast wallet import` command as follows:

```bash
cast wallet import deployer --interactive
```

This will prompt you to:

1. Enter your private key.
2. Enter a password to encrypt the keystore.

The account will be saved as "deployer" in your keystore. You can then use this account name in the deployment commands. You'll be prompted for your keystore password when deploying contracts or sending transactions. 

Deploying the contract with `forge create` takes a single command, but you must include an RPC endpoint and constructor arguments. `MyToken.sol` asks for an initial supply of tokens in its constructor, so each of the following commands includes 100 as a constructor argument. You can deploy the `MyToken.sol` contract using the following command for the correct network:

=== "Moonbeam"

    ```bash
    forge create src/MyToken.sol:MyToken \
    --rpc-url INSERT_RPC_API_ENDPOINT \
    --broadcast \
    --account deployer \
    --constructor-args 100
    ```

=== "Moonriver"

    ```bash
    forge create src/MyToken.sol:MyToken \
    --rpc-url INSERT_RPC_API_ENDPOINT \
    --broadcast \
    --account deployer \
    --constructor-args 100
    ```

=== "Moonbase Alpha"

    ```bash
    forge create src/MyToken.sol:MyToken \
    --rpc-url https://rpc.api.moonbase.moonbeam.network \
    --broadcast \
    --account deployer \
    --constructor-args 100
    ```

=== "Moonbeam Dev Node"

    ```bash
    forge create src/MyToken.sol:MyToken \
    --rpc-url http://127.0.0.1:9944 \
    --broadcast \
    --account deployer \
    --constructor-args 100
    ```

After you've deployed the contract and a few seconds have passed, you should see the address in the terminal.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>forge create src/MyToken.sol:MyToken \
--rpc-url https://rpc.api.moonbase.moonbeam.network \
--account deployer \
--constructor-args 100</span>
    <br>
    <span data-ty>[⠒] Compiling...</span>
    <span data-ty>No files changed, compilation skipped</span>
    <span data-ty>Deployer: 0x3B939FeaD1557C741Ff06492FD0127bd287A421e</span>
    <span data-ty>Deployed to: 0xc111402Aa1136ff6224106709ae51864512eC68f</span>
    <span data-ty>Transaction hash: 0xd77fc26aa296e81f35718b5878cda98e8371f6bf33b0f57e7d92997a36cf6465</span>
</div>
Congratulations! Your contract is live! Save the address, as you will use it to interact with this contract instance in the next step.

### Deploying via Solidity Scripting {: #deploying-via-solidity-scripting }  

Solidity scripting is a more powerful and flexible way to deploy contracts than [`forge create`](#deploying-the-contract). Writing a Solidity script is identical to writing a typical Solidity smart contract, though you won't ever deploy this contract.

You can tailor the behavior of `forge script` with various parameters. All components are optional except for local simulation, which is a required part of every run. The `forge script` command will attempt to execute all applicable steps in the following order:

1. **Local simulation**: Simulate the transaction(s) in a local EVM.
2. **Onchain simulation**: Simulate the transaction(s) via the provided RPC URL.
3. **Broadcasting**: When the `--broadcast` flag is provided, and simulations succeed, the transaction(s) are dispatched.
4. **Verification**: API-based smart contract verification when the `--verify` flag and a valid API key are provided.

Now, go ahead and write the script. In the script folder, create a file named `MyToken.s.sol`. Copy and paste the contents of the below file. 

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.30;

import "forge-std/Script.sol";
import "../src/MyToken.sol";

contract MyScript is Script {
    function run() external {
        vm.startBroadcast();

        MyToken mytoken = new MyToken(1000000000);

        vm.stopBroadcast();
    }
}
```

Notice that even though the above script is not being deployed, it still requires all the typical formatting for a Solidity contract, such as the pragma statement.

For this example, Foundry will first attempt a local simulation and a simulation against the provided RPC before deploying the contract. Remember that it will execute all relevant steps in order. Foundry won't proceed with the deployment if any of the simulations fail. You can deploy the `MyToken.sol` contract with this command.

```bash
forge script script/MyToken.s.sol --rpc-url https://rpc.api.moonbase.moonbeam.network --broadcast --account deployer
```

If your script's execution succeeds, your terminal should resemble the output below.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>forge script script/MyToken.s.sol --rpc-url https://rpc.api.moonbase.moonbeam.network --broadcast --account deployer --sender 0x3b939fead1557c741ff06492fd0127bd287a421e</span>
    <span data-ty>[⠒] Compiling...</span>
    <span data-ty>No files changed, compilation skipped</span>
    <span data-ty>EIP-3855 is not supported in one or more of the RPCs used.
Unsupported Chain IDs: 1287.</span>
    <span data-ty>Contracts deployed with a Solidity version equal or higher than 0.8.20 might not work properly.</span>
    <span data-ty>For more information, please see https://eips.ethereum.org/EIPS/eip-3855</span>
    <span data-ty>Script ran successfully.</span>
    <span data-ty>## Setting up 1 EVM.</span>
    <span data-ty>==========================</span>
    <br>
    <span data-ty>Chain 1287</span>
    <span data-ty>Estimated gas price: 0.0625 gwei</span>
    <span data-ty>Estimated total gas used for script: 1196500</span>
    <span data-ty>Estimated amount required: 0.00007478125 ETH</span>
    <span data-ty>==========================</span>
    <br>
    <span data-ty>Enter keystore password:</span>
    <span data-ty>##</span>
    <span data-ty>Sending transactions [0 - 0].</span>
    <span data-ty>⠁ [00:00:00] [########################################################################################################] 1/1 txes (0.0s)##</span>
    <span data-ty>Waiting for receipts.
⠉ [00:00:07] [#########################################################################################################################] 1/1 receipts (0.0s)</span>
    <span data-ty>##### moonbase</span>
    <br>
    <span data-ty>✅  [Success]Hash: 0xb70942942d731486872e7faba8a800e86809f44c2c3bd3f6306373562712e9d3 Contract Address: 0x98c3fC51d3487c1689e39ee63Ba110cfD8e1F552</span>
      <span data-ty>Block: 11847291</span>
      <span data-ty>Paid: 0.000027472875 ETH (879132 gas * 0.03125 gwei)</span>
      <span data-ty>==========================</span>
      <span data-ty>ONCHAIN EXECUTION COMPLETE & SUCCESSFUL.</span>
      <span data-ty>Total Paid: 0.000027472875 ETH (879132 gas * avg 0.03125 gwei)</span>
      <span data-ty>Transactions saved to: /Users/ubuntu-jammy/foundry/foundry/broadcast/MyToken.s.sol/1287/run-latest.json</span>
      <span data-ty>Sensitive values saved to: /Users/ubuntu-jammy/foundry/foundry/cache/MyToken.s.sol/1287/run-latest.json</span>
      <span data-ty="input"><span class="file-path"></span> </span>
 </span>
</div>
And that's it! For more information about Solidity scripting with Foundry, be sure to check out [Foundry's documentation site](https://www.getfoundry.sh/forge/scripting).

## Interacting with the Contract {: #interacting-with-the-contract }

Foundry includes cast, a CLI for performing Ethereum RPC calls.

Try to retrieve your token's name using Cast, where `INSERT_YOUR_CONTRACT_ADDRESS` is the address of the contract that you deployed in the previous section:

=== "Moonbeam"

    ```bash
    cast call INSERT_YOUR_CONTRACT_ADDRESS "name()" --rpc-url INSERT_RPC_API_ENDPOINT
    ```

=== "Moonriver"

    ```bash
    cast call INSERT_YOUR_CONTRACT_ADDRESS "name()" --rpc-url INSERT_RPC_API_ENDPOINT
    ```

=== "Moonbase Alpha"

    ```bash
    cast call INSERT_YOUR_CONTRACT_ADDRESS "name()" --rpc-url https://rpc.api.moonbase.moonbeam.network
    ```

=== "Moonbeam Dev Node"

    ```bash
    cast call INSERT_YOUR_CONTRACT_ADDRESS "name()" --rpc-url http://127.0.0.1:9944
    ```

You should get this data in hexadecimal format:

```text
0x000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000074d79546f6b656e00000000000000000000000000000000000000000000000000
```

This is far from readable, but you can use Cast to convert it into your desired format. In this case, the data is text, so you can convert it into ASCII characters to see "My Token":

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>cast --to-ascii 0x000000000000000000000000000000000000000000000000000000000000002000
    000000000000000000000000000000000000000000000000000000000000074d7954
    6f6b656e00000000000000000000000000000000000000000000000000</span>
    <br>
    <span data-ty> MyToken</span>
</div>
```bash
cast --to-ascii 0x000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000074d79546f6b656e00000000000000000000000000000000000000000000000000
```

You can also mutate data with cast as well. Try burning tokens by sending them to the zero address.

=== "Moonbeam"

    ```bash
    cast send --private-key INSERT_YOUR_PRIVATE_KEY \
    --rpc-url INSERT_RPC_API_ENDPOINT \
    --chain 1284 \
    INSERT_YOUR_CONTRACT_ADDRESS \
    "transfer(address,uint256)" 0x0000000000000000000000000000000000000001 1
    ```

=== "Moonriver"

    ```bash
    cast send --private-key INSERT_YOUR_PRIVATE_KEY \
    --rpc-url INSERT_RPC_API_ENDPOINT \
    --chain 1285 \
    INSERT_YOUR_CONTRACT_ADDRESS \
    "transfer(address,uint256)" 0x0000000000000000000000000000000000000001 1
    ```

=== "Moonbase Alpha"

    ```bash
    cast send --private-key INSERT_YOUR_PRIVATE_KEY \
    --rpc-url https://rpc.api.moonbase.moonbeam.network \
    --chain 1287 \
    INSERT_YOUR_CONTRACT_ADDRESS \
    "transfer(address,uint256)" 0x0000000000000000000000000000000000000001 1
    ```

=== "Moonbeam Dev Node"

    ```bash
    cast send --private-key INSERT_YOUR_PRIVATE_KEY \
    --rpc-url http://127.0.0.1:9944 \
    --chain 1281 \
    INSERT_YOUR_CONTRACT_ADDRESS \
    "transfer(address,uint256)" 0x0000000000000000000000000000000000000001 1
    ```

The transaction will be signed by your Moonbase account and be broadcast to the network. The output should look similar to:

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>cast send --private-key INSERT_PRIVATE_KEY \
--rpc-url https://rpc.api.moonbase.moonbeam.network \
--chain 1287 \
INSERT_CONTRACT_ADDRESS \
"transfer(address,uint256)" 0x0000000000000000000000000000000000000001 1</span>
    <br>
    <br>
    <span data-ty>blockHash               0x6f99fac1bb49feccb7b0476e0ffcd3cef4c456aa9111e193ce11c7a1ab62314e</span>
    <span data-ty>blockNumber             5892860</span>
    <span data-ty>contractAddress</span>
    <span data-ty>cumulativeGasUsed       51332</span>
    <span data-ty>effectiveGasPrice       3125000000</span>
    <span data-ty>gasUsed                 51332</span>
    <span data-ty>logs                    [{"address":"0xc111402aa1136ff6224106709ae51864512ec68f","topics":["0xddf252ad1be2c89b69
    c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
    "0x0000000000000000000000003b939fead155
    7c741ff06492fd0127bd287a421e",
    "0x0000000000000000000000000000000000000000000000000000000000000001"],
    "data":"0x0000000000000000000000000000000000000
    000000000000000000000000001",
    "blockHash":"0x6f99fac1bb49feccb7b0476e0ffcd3cef4c4
    56aa9111e193ce11c7a1ab62314e",
    "blockNumber":"0x59eafc",
    "transactionHash":"0xdd5f11be68d5
    2967356ccf34b9a4b2632d0d5ac8932ff27e72c544320dec33e3",
    "transactionIndex":"0x0","logIndex":"0x0","transactionLogIndex":"0x0","removed":false}]</span>
    <span data-ty>logsBloom               0x000000000000000000000000000000000000000000000000000000000000000000000000000000004
    00000000000000000000000000000000000000000040000000000000000000000000008000000000000
    00000004000000000000000000000000000000000000000100000000000000000000000000000000001
    00000010000000000000000000000000000000000000000000000000000000002000000040000000000
    00000000000000000000000000000000000000000000000000000000002000000000000000000000000
    00000000000000000000000000004000000000000000000000000000000000000000000000000000000
    0001000000</span>
    <span data-ty>root</span>
    <span data-ty>status                  1</span>
    <span data-ty>transactionHash         0xdd5f11be68d52967356ccf34b9a4b2632d0d5ac8932ff27e72c544320dec33e3</span>
    <span data-ty>transactionIndex        0</span>
    <span data-ty>type                    2</span>
</div>
Congratulations, you have successfully deployed and interacted with a contract using Foundry!

## Forking with Anvil {: #forking-with-cast-anvil }

As previously mentioned, [Anvil](https://www.getfoundry.sh/anvil#anvil) is a local TestNet node for development purposes that can fork preexisting networks. Forking Moonbeam allows you to interact with live contracts deployed on the network.

There are some limitations to be aware of when forking with Anvil. Since Anvil is based on an EVM implementation, you cannot interact with any of the Moonbeam precompiled contracts and their functions. Precompiles are a part of the Substrate implementation and therefore cannot be replicated in the simulated EVM environment. This prohibits you from interacting with cross-chain assets on Moonbeam and Substrate-based functionality such as staking and governance.

To fork Moonbeam or Moonriver, you will need to have your own endpoint and API key which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).

To fork Moonbeam from the command line, you can run the following command from within your Foundry project directory:

=== "Moonbeam"

    ```bash
    anvil --fork-url INSERT_RPC_API_ENDPOINT
    ```

=== "Moonriver"

    ```bash
    anvil --fork-url INSERT_RPC_API_ENDPOINT
    ```

=== "Moonbase Alpha"

    ```bash
    anvil --fork-url https://rpc.api.moonbase.moonbeam.network
    ```

Your forked instance will have 10 development accounts that are pre-funded with 10,000 test tokens. The forked instance is available at `http://127.0.0.1:8545/`. The output in your terminal should resemble the following:

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>anvil --fork-url https://rpc.api.moonbase.moonbeam.network</span>
    <br>
    <br>
    <span data-ty>Available Accounts</span>
    <span data-ty>==================</span>
    <span data-ty>(0) "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266" (10000.000000000000000000 ETH)</span>
    <span data-ty>(1) "0x70997970C51812dc3A010C7d01b50e0d17dc79C8" (10000.000000000000000000 ETH)</span>
    <span data-ty>(2) "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC" (10000.000000000000000000 ETH)</span>
    <span data-ty>(3) "0x90F79bf6EB2c4f870365E785982E1f101E93b906" (10000.000000000000000000 ETH)</span>
    <span data-ty>(4) "0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65" (10000.000000000000000000 ETH)</span>
    <span data-ty>(5) "0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc" (10000.000000000000000000 ETH)</span>
    <span data-ty>(6) "0x976EA74026E726554dB657fA54763abd0C3a0aa9" (10000.000000000000000000 ETH)</span>
    <span data-ty>(7) "0x14dC79964da2C08b23698B3D3cc7Ca32193d9955" (10000.000000000000000000 ETH)</span>
    <span data-ty>(8) "0x23618e81E3f5cdF7f54C3d65f7FBc0aBf5B21E8f" (10000.000000000000000000 ETH)</span>
    <span data-ty>(9) "0xa0Ee7A142d267C1f36714E4a8F75612F20a79720" (10000.000000000000000000 ETH)</span>
    <br>
    <span data-ty>Private Keys</span>
    <span data-ty>==================</span>
    <span data-ty>(0) 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80</span>
    <span data-ty>(1) 0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d</span>
    <span data-ty>(2) 0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a</span>
    <span data-ty>(3) 0x7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6</span>
    <span data-ty>(4) 0x47e179ec197488593b187f80a00eb0da91f1b9d0b13f8733639f19c30a34926a</span>
    <span data-ty>(5) 0x8b3a350cf5c34c9194ca85829a2df0ec3153be0318b5e2d3348e872092edffba</span>
    <span data-ty>(6) 0x92db14e403b83dfe3df233f83dfa3a0d7096f21ca9b0d6d6b8d88b2b4ec1564e</span>
    <span data-ty>(7) 0x4bbbf85ce3377467afe5d46f804f221813b2bb87f24d81f60f1fcdbf7cbf4356</span>
    <span data-ty>(8) 0xdbda1821b80551c9d65939329250298aa3472ba22feea921c0cf5d620ea67b97</span>
    <span data-ty>(9) 0x2a871d0798f97d79848a013d4936a73bf4cc922c825d33c1cf7073dff6d409c6</span>
    <br>
    <span data-ty>Wallet</span>
    <span data-ty>==================</span>
    <span data-ty>Mnemonic: test test test test test test test test test test test junk</span>
    <span data-ty>Derivation path: m/44'/60'/0'/0/</span>
    <br>
    <span data-ty>Fork</span>
    <span data-ty>==================</span>
    <span data-ty>Endpoint: https://rpc.api.moonbase.moonbeam.network</span>
    <span data-ty>Block number: 5892944</span>
    <span data-ty>Block hash: 0xc9579299f55d507c305d5357d4c1b9d9c550788ddb471b0231d8d0146e7144b7</span>
    <span data-ty>Chain ID: 1287</span>
    <br>
    <span data-ty>Base Fee</span>
    <span data-ty>==================</span>
    <span data-ty>125000000</span>
    <br>
    <span data-ty>Gas Limit</span>
    <span data-ty>==================</span>
    <span data-ty>30000000</span>
    <br>
    <span data-ty>Genesis Timestamp</span>
    <span data-ty>==================</span>
    <span data-ty>1705278817</span>
    <br>
    <span data-ty>Listening on 127.0.0.1:8545</span>
</div>
To verify you have forked the network, you can query the latest block number:

```bash
curl --data '{"method":"eth_blockNumber","params":[],"id":1,"jsonrpc":"2.0"}' -H "Content-Type: application/json" -X POST localhost:8545 
```

If you convert the `result` from [hex to decimal](https://www.rapidtables.com/convert/number/hex-to-decimal.html), you should get the latest block number from the time you forked the network. You can cross reference the block number using a [block explorer](/moonbeam-mkdocs/builders/get-started/explorers/).

From here you can deploy new contracts to your forked instance of Moonbeam or interact with contracts already deployed. Building off of the previous example in this guide, you can make a call using Cast to check the balance of the minted MYTOK tokens in the account you deployed the contract with:

```bash
cast call INSERT_CONTRACT_ADDRESS  "balanceOf(address)(uint256)" INSERT_YOUR_ADDRESS --rpc-url http://localhost:8545
```

## Using Chisel {: #using-chisel }

Chisel is a Solidity REPL or shell. It allows a developer to write Solidity directly in the console for testing small snippets of code, letting developers skip the project setup and contract deployment steps for what should be a quick process.  

Since Chisel is mainly useful for quick testing, it can be used outside of a Foundry project. But, if executed within a Foundry project, it will keep the configurations within `foundry.toml` when running.  

For this example, you will be testing out some of the features of `abi` within Solidity because it is complex enough to demonstrate how Chisel could be useful. To get started using Chisel, run the following in the command line to start the shell:

```bash
chisel
```

In the shell, you can write Solidity code as if it were running within a function:

```solidity
bytes memory myData = abi.encode(100, true, "Develop on Moonbeam");
```

Let's say you were interested in how `abi` encoded data because you're looking into how to most efficiently store data on the blockchain and thus save gas. To view how the `myData` is stored in memory, you can use the following command while in the Chisel shell:

```bash
!memdump
```

`memdump` will dump all of the data in your current session. You'll likely see something like this below. If you aren't good at reading hexadecimal or if you don't know how ABI encoding works, then you might not be able to find where the `myData` variable has been stored.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>chisel</span>
    <br>
    <span data-ty>Welcome to Chisel! Type `!help` to show available commands.</span>
    <span data-ty="input" data-ty-prompt="➜"> bytes memory myData = abi.encode(100, true, "Develop on Moonbeam");</span>
    <br>
    <span data-ty="input" data-ty-prompt="➜"> !memdump</span>
    <span data-ty>[0x00:0x20]: 0x0000000000000000000000000000000000000000000000000000000000000000</span>
    <span data-ty>[0x20:0x40]: 0x0000000000000000000000000000000000000000000000000000000000000000</span>
    <span data-ty>[0x40:0x60]: 0x0000000000000000000000000000000000000000000000000000000000000140</span>
    <span data-ty>[0x60:0x80]: 0x0000000000000000000000000000000000000000000000000000000000000000</span>
    <span data-ty>[0x80:0xa0]: 0x00000000000000000000000000000000000000000000000000000000000000a0</span>
    <span data-ty>[0xa0:0xc0]: 0x0000000000000000000000000000000000000000000000000000000000000064</span>
    <span data-ty>[0xc0:0xe0]: 0x0000000000000000000000000000000000000000000000000000000000000001</span>
    <span data-ty>[0xe0:0x100]: 0x0000000000000000000000000000000000000000000000000000000000000060</span>
    <span data-ty>[0x100:0x120]: 0x0000000000000000000000000000000000000000000000000000000000000013</span>
    <span data-ty>[0x120:0x140]: 0x446576656c6f70206f6e204d6f6f6e6265616d00000000000000000000000000</span>
    <span data-ty="input" data-ty-prompt="➜"> </span>
</div>
Fortunately, Chisel lets you easily figure out where this information is stored. Using the `!rawstack` command, you can find the location in the stack where the value of a variable:  

```bash
!rawstack myData
```

In this situation, since bytes is over 32 bytes in length, the memory pointer is displayed instead. But that's exactly what's needed since you already know the entirety of the stack from the `!memdump` command.

<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span>chisel</span>
    <br>
    <span data-ty>Welcome to Chisel! Type `!help` to show available commands.</span>
    <span data-ty="input" data-ty-prompt="➜"> bytes memory myData = abi.encode(100, true, "Develop on Moonbeam");</span>
    <br>
    <span data-ty="input" data-ty-prompt="➜"> !memdump</span>
    <span data-ty>[0x00:0x20]: 0x0000000000000000000000000000000000000000000000000000000000000000</span>
    <span data-ty>[0x20:0x40]: 0x0000000000000000000000000000000000000000000000000000000000000000</span>
    <span data-ty>[0x40:0x60]: 0x0000000000000000000000000000000000000000000000000000000000000140</span>
    <span data-ty>[0x60:0x80]: 0x0000000000000000000000000000000000000000000000000000000000000000</span>
    <span data-ty>[0x80:0xa0]: 0x00000000000000000000000000000000000000000000000000000000000000a0</span>
    <span data-ty>[0xa0:0xc0]: 0x0000000000000000000000000000000000000000000000000000000000000064</span>
    <span data-ty>[0xc0:0xe0]: 0x0000000000000000000000000000000000000000000000000000000000000001</span>
    <span data-ty>[0xe0:0x100]: 0x0000000000000000000000000000000000000000000000000000000000000060</span>
    <span data-ty>[0x100:0x120]: 0x0000000000000000000000000000000000000000000000000000000000000013</span>
    <span data-ty>[0x120:0x140]: 0x446576656c6f70206f6e204d6f6f6e6265616d00000000000000000000000000</span>
    <span data-ty="input" data-ty-prompt="➜"> !rawstack myData </span>
    <br>
    <span data-ty>Type: bytes32 </span>
    <span data-ty>└ Data: 0x0000000000000000000000000000000000000000000000000000000000000080</span>
    <span data-ty="input" data-ty-prompt="➜"> </span>
</div>
The `!rawstack` command shows that the `myData` variable is stored at `0x80`, so when comparing this with the memory dump retrieved from the `!memdump` command, it looks like `myData` is stored like this:  

```text
[0x80:0xa0]: 0x00000000000000000000000000000000000000000000000000000000000000a0
[0xa0:0xc0]: 0x0000000000000000000000000000000000000000000000000000000000000064
[0xc0:0xe0]: 0x0000000000000000000000000000000000000000000000000000000000000001
[0xe0:0x100]: 0x0000000000000000000000000000000000000000000000000000000000000060
[0x100:0x120]: 0x0000000000000000000000000000000000000000000000000000000000000013
[0x120:0x140]: 0x446576656c6f70206f6e204d6f6f6e6265616d00000000000000000000000000
```

At first glance, this makes sense, since `0xa0` has a value of `0x64` which is equal to 100, and `0xc0` has a value of `0x01` which is equal to true. If you want to learn more about how ABI-encoding works, the [Solidity documentation for ABI is helpful](https://docs.soliditylang.org/en/v0.8.18/abi-spec.html). In this case, there are a lot of zeros in this method of data packing, so as a smart contract developer you might instead try to use structs or pack the data together more efficiently with bitwise code.  

Since you're done with this code, you can clear the state of Chisel so that it doesn't mess with any future logic that you want to try out (while running the same instance of Chisel):  

```bash
!clear
```

There's an even easier way to test with Chisel. When writing code that ends with a semicolon (`;`), Chisel will run it as a statement, storing its value in Chisel's runtime state. But if you only needed to see how the ABI-encoded data was represented, then you could get away with running the code as an expression. To try this out with the same `abi` example, write the following in the Chisel shell:

```bash
abi.encode(100, true, "Develop on Moonbeam")
```

You should see something like the following:  

<div id="termynal" data-termynal>
	<span data-ty="input" data-ty-prompt="➜"> !clear</span>
	<span data-ty>Cleared session!</span>
	<span data-ty="input" data-ty-prompt="➜"> abi.encode(100, true, "Develop on Moonbeam")</span>
	<span data-ty>Type: dynamic bytes</span>
	<span data-ty>├ Hex (Memory):</span>
	<span data-ty>├─ Length ([0x00:0x20]): 0x00000000000000000000000000000000000000000000000000000000000000a0</span>
	<span data-ty>├─ Contents ([0x20:..]): 0x0000000000000000000000000000000000000000000000000000000000000064</span>
	<span data-ty>0000000000000000000000000000000000000000000000000000000000000001</span>
	<span data-ty>0000000000000000000000000000000000000000000000000000000000000060</span>
	<span data-ty>0000000000000000000000000000000000000000000000000000000000000001</span>
	<span data-ty>34446576656c6f70206f6e204d6f6f6e6265616d00000000000000000000000000</span>
	<span data-ty>├ Hex (Tuple Encoded):</span>
	<span data-ty>├─ Pointer ([0x00:0x20]): 0x0000000000000000000000000000000000000000000000000000000000000020</span>
	<span data-ty>├─ Length ([0x20:0x40]): 0x00000000000000000000000000000000000000000000000000000000000000a0</span>
	<span data-ty>└─ Contents ([0x40:..]): 0x0000000000000000000000000000000000000000000000000000000000000064</span>
	<span data-ty>0000000000000000000000000000000000000000000000000000000000000001</span>
	<span data-ty>0000000000000000000000000000000000000000000000000000000000000060</span>
	<span data-ty>0000000000000000000000000000000000000000000000000000000000000001</span>
	<span data-ty>34446576656c6f70206f6e204d6f6f6e6265616d00000000000000000000000000</span>
	<span data-ty="input" data-ty-prompt="➜"></span>
</div>
While it doesn't display the data in the same way, you still get the contents of the data, and it also further breaks down how the information is coded, such as letting you know that the `0xa0` value defines the length of the data.  

By default, when you leave the Chisel shell, none of the data is persisted. But you can instruct chisel to do so. For example, you can take the following steps to store a variable:

1. Store a `uint256` in Chisel.
    ```bash
    uint256 myNumber = 101;
    ```

2. Store the session with `!save`. For this example, you can use the number `1` as a save ID.
    ```bash
    !save 1
    ```

3. Quit the session.
    ```bash
    !quit
    ```

Then to view and interact with your stored Chisel states, you can take the following steps:

1. View a list of saved Chisel states.
     ```bash
     chisel list
     ```

2. Load your stored states.
    ```bash
    chisel load 1
    ```

3. View the `uint256` saved in Chisel from the previous set of steps.
    ```bash
    !rawstack myNumber
    ```  

<div id="termynal" data-termynal>
	<span data-ty="input" data-ty-prompt="➜"> uint256 myNumber = 101;</span>
	<span data-ty="input" data-ty-prompt="➜"> !save 1</span>
	<span data-ty="input" data-ty-prompt="➜"> Saved session to cache with ID = 1</span>
	<span data-ty="input" data-ty-prompt="(ID: 1) ➜"> !quit</span>
	<span data-ty="input"><span class="file-path"></span>chisel list</span>
	<span data-ty>⚒️ Chisel Sessions</span>
	<span data-ty>├─ "2024-01-15 01:17:34" - chisel-1.json</span>
	<span data-ty="input"><span class="file-path"></span>chisel load 1</span>
	<span data-ty>Welcome to Chisel! Type `!help` to show available commands.</span>
	<span data-ty="input" data-ty-prompt="(ID: 1) ➜"> !rawstack myNumber</span>
	<span data-ty>Type: bytes32</span>
	<span data-ty>└ Data: 0x0000000000000000000000000000000000000000000000000000000000000065</span>
	<span data-ty="input" data-ty-prompt="(ID: 1) ➜"></span>
</div>
You can even fork networks while using Chisel:

```bash
!fork https://rpc.api.moonbase.moonbeam.network
```

Then, for example, you can query the balance of one of Moonbase Alpha's collators:  

```text
0x12E7BCCA9b1B15f33585b5fc898B967149BDb9a5.balance
```

<div id="termynal" data-termynal>
	<span data-ty="input" data-ty-prompt="➜"> !fork https://rpc.api.moonbase.moonbeam.network</span>
	<span data-ty>Set fork URL to https://rpc.api.moonbase.moonbeam.network</span>
	<span data-ty="input" data-ty-prompt="➜"> 0x12E7BCCA9b1B15f33585b5fc898B967149BDb9a5.balance</span>
	<span data-ty>Type: uint</span>
	<span data-ty>├ Hex: 0x000000000000000000000000000000000000000000000358affd3d76ebb78555</span>
	<span data-ty>└ Decimal: 15803094286802091476309</span>
	<span data-ty="input" data-ty-prompt="➜"></span>
</div>
If you want to learn more about Chisel, download Foundry and refer to its [official reference page](https://www.getfoundry.sh/reference/chisel/chisel).

## Foundry With Hardhat {: #foundry-with-hardhat }  

Often, there will be the case where a project that you wish to integrate with has all of its setup within [Hardhat](/moonbeam-mkdocs/builders/ethereum/dev-env/hardhat/), making it an arduous task to convert the entirety of the project into Foundry. This additional work is avoidable by creating a hybrid project that uses both Hardhat and Foundry features together. This is possible with Hardhat's [hardhat-foundry plugin](https://hardhat.org/hardhat-runner/plugins/nomicfoundation-hardhat-foundry).  

To convert your preexisting Foundry project to a hybrid project, you will essentially have to install a Hardhat project into the same folder:  

```bash
npm init
npm install --save-dev hardhat @nomicfoundation/hardhat-foundry
npx hardhat init
```

For more information, please refer to our documentation on [Creating a Hardhat Project](/moonbeam-mkdocs/builders/ethereum/dev-env/hardhat/#creating-a-hardhat-project).

After initializing the new Hardhat project, a few new folders and files should appear: `contracts`, `hardhat.config.js`, `scripts`, and `test/Lock.js`. You'll need to make a few modifications to create a hybrid project:

1. Edit the `hardhat.config.js` file within your repository. Open it up, and at the top, add the following:  

    ```javascript
    require("@nomicfoundation/hardhat-foundry");
    ```

    After adding the `hardhat-foundry` plugin, the typical `contracts` folders for Hardhat will not work because now Hardhat expects all smart contracts to be stored within Foundry's `src` folder

2. Move all smart contracts within the `contracts` folder into the `src` folder, and then delete the `contracts` folder.
3. Edit the `foundry.toml` file to ensure that dependencies installed via Git submodules and npm can be compiled by the Forge tool. Edit the `profile.default` to ensure that the `libs` entry has both `lib` and `node_modules`:  

    ```toml
    [profile.default]
    src = 'src'
    out = 'out'
    libs = ['lib', 'node_modules']
    solc = '0.8.20'
    evm_version = 'london'
    ```

Now both `forge build` and `npx hardhat compile` should work regardless of the dependencies.  

Both `forge test` and `npx hardhat test` should now be able to access all smart contracts and dependencies. `forge test` will only test the Solidity tests, whereas `npx hardhat test` will only test the JavaScript tests. If you would like to use them in conjunction, then you can create a new script within your `package.json` file:  

```json
"scripts": {
    "test": "npx hardhat test && forge test"
}
```

You can run this command with:  

```bash
npm run test
```

Finally, while not necessary, it could be worthwhile to move all JavaScript scripts from the `scripts` folder into Foundry's `script` folder and delete the `scripts` folder so that you don't have two folders that serve the same purpose.

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
