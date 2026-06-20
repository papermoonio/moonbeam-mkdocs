---
title: Run a Moonbeam Development Node
description: Follow this tutorial to learn how to spin up your first Moonbeam development node, how to configure it for development purposes, and connect to it.
categories:
- Basics
url: https://docs.moonbeam.network/builders/get-started/networks/moonbeam-dev/
word_count: 3923
token_estimate: 6697
version_hash: sha256:af73a148bc8059c440776c22e9b699ccf9fb200570486d2224d177fc5b248e18
last_updated: '2026-05-21T21:21:53+00:00'
---

# Getting Started with a Local Moonbeam Development Node

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/-bRooBW2g0o' frameborder='0' allowfullscreen></iframe></div>
<style>.caption { font-family: Open Sans, sans-serif; font-size: 0.9em; color: rgba(170, 170, 170, 1); font-style: italic; letter-spacing: 0px; position: relative;}</style>

## Introduction {: #introduction }

A Moonbeam development node is your own personal development environment for building and testing applications on Moonbeam. For Ethereum developers, it is comparable to the Hardhat Network. It enables you to get started quickly and easily without the overhead of a relay chain. You can spin up your node with the `--sealing` option to author blocks instantly, manually, or at a custom interval after transactions are received. By default, a block will be created when a transaction is received, which is similar to the default behavior of Hardhat Network's instamine feature.

If you follow this guide to the end, you will have a Moonbeam development node running in your local environment with 10 prefunded [accounts](#pre-funded-development-accounts).

!!! note
    This tutorial was created using the v0.51.2 tag of [Moonbase Alpha](https://github.com/moonbeam-foundation/moonbeam/releases/tag/v0.51.2). The Moonbeam platform and the [Frontier](https://github.com/polkadot-evm/frontier) components it relies on for Substrate-based Ethereum compatibility are still under very active development.
    The examples in this guide assume you have a MacOS or Ubuntu 22.04-based environment and will need to be adapted accordingly for Windows.
## Spin Up a Moonbeam Development Node {: #spin-up-a-node }

There are two ways to get started running a Moonbeam node. You can use [Docker to run a pre-built binary](#getting-started-with-docker) or you can [compile the binary locally](#getting-started-with-the-binary-file) and set up a development node yourself. Using Docker is a quick and convenient way to get started, as you won't have to install Substrate and all the dependencies, and you can skip the node-building process as well. It does require you to [install Docker](https://docs.docker.com/get-started/get-docker/). On the other hand, if you decide you want to go through the process of building your development node, it could take roughly 30 minutes or longer to complete, depending on your hardware.

### Spin Up a Node with Docker {: #getting-started-with-docker }

Using Docker enables you to spin up a node in a matter of seconds. Once you have Docker installed, you can take the following steps to spin up your node:

1. Execute the following command to download the latest Moonbeam image:

    ```bash
    docker pull moonbeamfoundation/moonbeam:v0.51.2
    ```

    The tail end of the console log should look like this:

    <div id="termynal" data-termynal>
      <span data-ty="input"><span class="file-path"></span>docker pull moonbeamfoundation/moonbeam:v0.51.2</span>
      <br>
      <span data-ty>v0.51.2: Pulling from moonbeamfoundation/moonbeam
        <br> b0a0cf830b12: Pull complete
        <br> fbff687640dd: Pull complete
        <br> 58ea427410e2: Pull complete
        <br> 811ba55e6e61: Pull complete
        <br> 4316d5f1b914: Pull complete
        <br> 128693ce218e: Pull complete
        <br> a3ac90b88463: Pull complete
        <br> Digest: sha256:d2448058e383377052666b250dc32f2676062a11aea07c90578c2483c918a786
        <br> Status: Downloaded newer image for moonbeamfoundation/moonbeam:v0.51.2
        <br> docker.io/moonbeamfoundation/moonbeam:v0.51.2
      </span>
    </div>
2. Spin up a Moonbeam development node by running the following Docker command, which will launch the node in instant seal mode for local testing so that blocks are authored instantly as transactions are received:

    === "Ubuntu"

        ```bash
        docker run --rm --name moonbeam_development --network host \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --dev --rpc-external
        ```

    === "MacOS"

        ```bash
        docker run --rm --name moonbeam_development -p 9944:9944 \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --dev --rpc-external
        ```

    === "Windows"

        ```bash
        docker run --rm --name moonbeam_development -p 9944:9944 ^
        moonbeamfoundation/moonbeam:v0.51.2 ^
        --dev --rpc-external
        ```

    !!! note "For Apple Silicon users"
        If the Docker commands fail or behave unexpectedly on Apple Silicon, enable **Use Rosetta for x86_64/amd64 emulation on Apple Silicon** in Docker Desktop settings and use the `amd64` platform for both pull and run commands:

        ```bash
        docker pull --platform=linux/amd64 moonbeamfoundation/moonbeam:v0.51.2
        ```

        ```bash
        docker run --rm --platform=linux/amd64 --name moonbeam_development -p 9944:9944 \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --dev --rpc-external
        ```

        If performance is still insufficient, consider [spinning up a node with a binary file](#getting-started-with-the-binary-file).

If successful, you should see an output showing an idle state waiting for blocks to be authored:

<div id="termynal" data-termynal>
  <span data-ty="input"><span class="file-path"></span>docker run --rm --name moonbeam_development --network host \
    <br> moonbeamfoundation/moonbeam:v0.51.2 \
    <br> --dev --rpc-external
  </span>
  <br>
  <span data-ty>CLI parameter `--execution` has no effect anymore and will be removed in the future!
    <br> 2025-07-10 09:04:26 Moonbeam Parachain Collator
    <br> 2025-07-10 09:04:26 ✌️  version 0.51.2
    <br> 2025-07-10 09:04:26 ❤️  by PureStake, 2019-2025
    <br> 2025-07-10 09:04:26 📋 Chain specification: Moonbase Development Testnet
    <br> 2025-07-10 09:04:26 🏷  Node name: black-and-white-sticks-9174
    <br> 2025-07-10 09:04:26 👤 Role: AUTHORITY
    <br> 2025-07-10 09:04:26 💾 Database: RocksDb at /tmp/substrateO3YeRz/chains/moonbase_dev/db/full
    <br> 2025-07-10 09:04:26 🔨 Initializing Genesis block/state (state: 0xf7c4…5c0f, header-hash: 0x42bd…3b5b)
    <br> 2025-07-10 09:04:26 Using default protocol ID "sup" because none is configured in the chain specs
    <br> 2025-07-10 09:04:26 🏷  Local node identity is: 12D3KooWLcpczme2JeBEfLqmjqkzYVKTGKhhGmwSzHjRXGBVhDX7
    <br> 2025-07-10 09:04:26 💻 Operating system: linux
    <br> 2025-07-10 09:04:26 💻 CPU architecture: x86_64
    <br> 2025-07-10 09:04:26 💻 Target environment: gnu
    <br> 2025-07-10 09:04:26 💻 CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
    <br> 2025-07-10 09:04:26 💻 CPU cores: 12
    <br> 2025-07-10 09:04:26 💻 Memory: 7946MB
    <br> 2025-07-10 09:04:26 💻 Kernel: 6.4.16-linuxkit
    <br> 2025-07-10 09:04:26 💻 Linux distribution: Debian GNU/Linux 12 (bookworm)
    <br> 2025-07-10 09:04:26 💻 Virtual machine: yes
    <br> 2025-07-10 09:04:26 📦 Highest known block at #0
    <br> 2025-07-10 09:04:26 Running JSON-RPC server: addr=0.0.0.0:9944, allowed origins=["*"]
    <br> 2025-07-10 09:04:26 🏁 CPU score: 1.14 GiBs
    <br> 2025-07-10 09:04:26 〽️ Prometheus exporter started at 127.0.0.1:9615
    <br> 2025-07-10 09:04:26 🏁 Memory score: 10.41 GiBs
    <br> 2025-07-10 09:04:26 🏁 Disk score (seq. writes): 987.96 MiBs
    <br> 2025-07-10 09:04:26 🏁 Disk score (rand. writes): 363.65 MiBs
    <br> 2025-07-10 09:04:26 Development Service Ready
    <br> 2025-07-10 09:04:26 💤 Idle (0 peers), best: #0 (0xa083…f354), finalized #0 (0xa083…f354), ⬇ 0 ⬆ 0
    <br> 2025-07-10 09:04:26 💤 Idle (0 peers), best: #0 (0xa083…f354), finalized #0 (0xa083…f354), ⬇ 0 ⬆ 0
  </span>
</div>
For more information on some of the flags and options used in the example, check out [Flags](#node-flags) and [Options](#node-options). If you want to see a complete list of all of the flags, options, and subcommands, open the help menu by running:

```bash
docker run --rm --name moonbeam_development \
moonbeamfoundation/moonbeam \
--help
```

To continue with the tutorial, the next section is not necessary, as you've already spun up a node with Docker. You can skip ahead to the [Configure your Moonbeam Development Node](#configure-moonbeam-dev-node) section.

### Spin Up a Node with a Binary File {: #getting-started-with-the-binary-file }

As an alternative to using Docker, you can spin up a node using the Moonbeam binary. This method is more time-consuming. Depending on your hardware, the process could take around 30 minutes to complete.

!!! note
    If you know what you are doing, you can directly download the precompiled binaries attached to each release on the [Moonbeam release page](https://github.com/moonbeam-foundation/moonbeam/releases). These will not work in all systems. For example, the binaries only work with x86-64 Linux with specific versions of dependencies. The safest way to ensure compatibility is to compile the binary on the system where it will be run.

To build the binary file, you can take the following steps:

1. Clone a specific tag of the Moonbeam repo, which you can find on the [Moonbeam GitHub repository](https://github.com/moonbeam-foundation/moonbeam):

    ```bash
    git clone -b v0.51.2 https://github.com/moonbeam-foundation/moonbeam
    cd moonbeam
    ```

    !!! note
        Spaces in the installation file path will cause a compilation error.

2. Check if Rust is installed. If Rust is installed, skip the next two steps. Otherwise, install Rust and its prerequisites [via Rust's recommended method](https://rust-lang.org/tools/install/) by executing:

    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

3. Update your PATH environment variable by running:

    ```bash
    source $HOME/.cargo/env
    ```

4. Build the development node by running:

    !!! note
        If you are using Ubuntu 20.04 or 22.04, then you will need to make sure these additional dependencies have been installed before building the binary:

        ```bash
        apt install clang protobuf-compiler libprotobuf-dev pkg-config libssl-dev -y 
        ```

        For MacOS users, these dependencies can be installed via Homebrew:

        ```bash
        brew install llvm
        brew install protobuf
        ```

    ```bash
    cargo build --release
    ```

    Here is what the tail end of the build output should look like:

    <div id="termynal" data-termynal>
      <span data-ty>Compiling try-runtime-cli v0.9.0 (https://github.com/paritytech/substrate?branch=rococo-v1#401c24e8)
        <br> Compiling frame-benchmarking-cli v3.0.0 (https://github.com/paritytech/substrate?branch=rococo-v1#401c24e8)
        <br> Compiling cumulus-client-cli v0.1.0 (https://github.com/paritytech/cumulus?branch=rococo-v1#9d89ed65)
        <br> Compiling moonbeam-rpc-txpool v0.6.0 (/home/purestake/moonbeam/client/rpc/txpool)
        <br> Compiling moonbeam-rpc-debug v0.1.0 (/home/purestake/moonbeam/client/rpc/debug)
        <br> Compiling moonbeam-rpc-trace v0.6.0 (/home/purestake/moonbeam/client/rpc/trace)
        <br> Compiling cumulus-client-network v0.1.0 (https://github.com/paritytech/cumulus?branch=rococo-v1#9d89ed65)
        <br> Compiling cumulus-client-consensus-relay-chain v0.1.0 (https://github.com/paritytech/cumulus?branch=rococo-v1#9d89ed65)
        <br> Compiling polkadot-test-service v0.8.29 (https://github.com/paritytech/polkadot?branch=rococo-v1#b64741e6)
        <br> Compiling cumulus-client-collator v0.1.0 (https://github.com/paritytech/cumulus?branch=rococo-v1#9d89ed65)
        <br> Compiling cumulus-client-service v0.1.0 (https://github.com/paritytech/cumulus?branch=rococo-v1#9d89ed65)
        <br> Finished release [optimized] target(s) in 31m 17s
      </span>
    </div>
!!! note
    The initial build will take a while. Depending on your hardware, you should expect approximately 30 minutes for the build process to finish.

Then, you will want to run the node in development mode using the following command:

```bash
./target/release/moonbeam --dev
```

!!! note
    For people not familiar with Substrate, the `--dev` flag is a way to run a Substrate-based node in a single-node developer configuration for testing purposes. When you run your node with the `--dev` flag, your node is started in a fresh state, and its state does not persist.

You should see an output that looks like the following, showing an idle state waiting for blocks to be produced:

<div id="termynal" data-termynal>
  <span data-ty="input"><span class="file-path"></span>./target/release/moonbeam --dev</span>
  <br>
  <span data-ty> 2025-07-10 09:04:26 Moonbeam Parachain Collator
    <br> 2025-07-10 09:04:26 ✌️  version 0.51.2
    <br> 2025-07-10 09:04:26 ❤️  by PureStake, 2019-2025
    <br> 2025-07-10 09:04:26 📋 Chain specification: Moonbase Development Testnet
    <br> 2025-07-10 09:04:26 🏷  Node name: black-and-white-sticks-9174
    <br> 2025-07-10 09:04:26 👤 Role: AUTHORITY
    <br> 2025-07-10 09:04:26 💾 Database: RocksDb at /tmp/substrateO3YeRz/chains/moonbase_dev/db/full
    <br> 2025-07-10 09:04:26 🔨 Initializing Genesis block/state (state: 0x7c34…99c5, header-hash: 0xa083…f354)
    <br> 2025-07-10 09:04:26 Using default protocol ID "sup" because none is configured in the chain specs
    <br> 2025-07-10 09:04:26 🏷  Local node identity is: 12D3KooWLcpczme2JeBEfLqmjqkzYVKTGKhhGmwSzHjRXGBVhDX7
    <br> 2025-07-10 09:04:26 💻 Operating system: linux
    <br> 2025-07-10 09:04:26 💻 CPU architecture: x86_64
    <br> 2025-07-10 09:04:26 💻 Target environment: gnu
    <br> 2025-07-10 09:04:26 💻 CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
    <br> 2025-07-10 09:04:26 💻 CPU cores: 12
    <br> 2025-07-10 09:04:26 💻 Memory: 7946MB
    <br> 2025-07-10 09:04:26 💻 Kernel: 6.4.16-linuxkit
    <br> 2025-07-10 09:04:26 💻 Linux distribution: Debian GNU/Linux 12 (bookworm)
    <br> 2025-07-10 09:04:26 💻 Virtual machine: yes
    <br> 2025-07-10 09:04:26 📦 Highest known block at #0
    <br> 2025-07-10 09:04:26 Running JSON-RPC server: addr=0.0.0.0:9944, allowed origins=["*"]
    <br> 2025-07-10 09:04:26 🏁 CPU score: 1.14 GiBs
    <br> 2025-07-10 09:04:26 〽️ Prometheus exporter started at 127.0.0.1:9615
    <br> 2025-07-10 09:04:26 🏁 Memory score: 10.41 GiBs
    <br> 2025-07-10 09:04:26 🏁 Disk score (seq. writes): 987.96 MiBs
    <br> 2025-07-10 09:04:26 🏁 Disk score (rand. writes): 363.65 MiBs
    <br> 2025-07-10 09:04:26 Development Service Ready
    <br> 2025-07-10 09:04:26 💤 Idle (0 peers), best: #0 (0xa083…f354), finalized #0 (0xa083…f354), ⬇ 0 ⬆ 0
    <br> 2025-07-10 09:04:26 💤 Idle (0 peers), best: #0 (0xa083…f354), finalized #0 (0xa083…f354), ⬇ 0 ⬆ 0
  </span>
</div>
For more information on some of the flags and options used in the example, check out the [Flags](#node-flags) and [Options](#node-options). If you want to see a complete list of all of the flags, options, and subcommands, open the help menu by running:

```bash
./target/release/moonbeam --help
```

## Configure Your Moonbeam Development Node {: #configure-moonbeam-dev-node }

Now that you know how to get a standard Moonbeam development node up and running, you may be wondering how you can configure it. The following sections will cover some common configurations you can use when you spin up your node.

### Common Flags to Configure Your Node {: #node-flags }

Flags do not take an argument. To use a flag, add it to the end of a command. For example:

```bash
./target/release/moonbeam --dev
```

- **`--dev`** - specifies the development chain
- **`--tmp`** - runs a temporary node in which all of the configuration will be deleted at the end of the process
- **`--rpc-external`** - listen to all RPC and WebSocket interfaces

### Common Options to Configure Your Node {: #node-options }

Options accept an argument to the right of the option. For example:

```bash
./target/release/moonbeam --dev --sealing 6000
```

- **`-l <log pattern>` or `--log <log pattern>`** - sets a custom logging filter. The syntax for the log pattern is `<target>=<level>`. For example, to print all of the JSON-RPC logs, the command would look like this: `-l json=trace`
- **`--sealing <interval>`** - when blocks should be sealed in the dev service. Accepted arguments for interval: `instant`, `manual`, or a number representing the timer interval in milliseconds (for example, `6000` will have the node produce blocks every 6 seconds). The default is `instant``. Please refer to the [Configure Block Production](#configure-block-production) section below for more information
- **`--rpc-port <port>`** - sets the unified port for HTTP and WS connections. Accepts a port as the argument. Default is 9944
- **`--ws-port <port>`** - *deprecated as of [client v0.33.0](https://github.com/moonbeam-foundation/moonbeam/releases/tag/v0.33.0), use `--rpc-port` for HTTP and WS connections instead* - sets the WebSockets RPC server TCP port. As of [client v0.30.0](https://github.com/moonbeam-foundation/moonbeam/releases/tag/v0.30.0), it sets the unified port for both HTTP and WS connections. Accepts a port as the argument
- **`--rpc-max-connections <connections>`** - specifies the combined HTTP and WS connection limit. The default is 100 connections
- **`--ws-max-connections <connections>`** - *deprecated as of [client v0.33.0](https://github.com/moonbeam-foundation/moonbeam/releases/tag/v0.33.0), use `--rpc-max-connections` to limit the HTTP and WS connections instead* - this flag adjusts the combined HTTP and WS connection limit. The default is 100 connections
- **`--rpc-cors <origins>`** - specifies the browser origins allowed to access the HTTP and WS RPC servers. The origins can be a comma-separated list of the origins to allow access, or you can also specify `null`. When running a development node, the default is to allow all origins

For a complete list of flags and options, spin up your Moonbeam development node with `--help` added to the end of the command.

### Configure Block Production {: #configure-block-production }

By default, your Moonbeam development node is spun up in instant seal mode, which instantly authors blocks as transactions are received. However, you can specify when blocks should be authored or sealed by using the `--sealing` option.

The `--sealing` flag accepts any of the following arguments:

- `instant` - as we already covered, this is the default option in which blocks are authored as soon as a transaction is received
- `manual` - allows you to produce blocks manually. If a transaction is received, a block will not be produced until you manually create one
- an interval in milliseconds - authors a block on a specific time interval. For example, if you set it to `6000`, you will have the node produce blocks every 6 seconds

The flag should be appended to the start-up command in the following format:

```text
--sealing <interval>
```

If you choose `manual`, you'll need to manually create the blocks yourself, which can be done with the `engine_createBlock` JSON-RPC method:

```text
engine_createBlock(createEmpty: *bool*, finalize: *bool*, parentHash?: *BlockHash*)
```

For example, you can use the following snippet to manually create a block using [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/), an Ethereum library that makes it easy to interact with JSON-RPC methods:

```js
import { ethers } from 'ethers';

const produceBlock = async () => {
  // Connect to the Ethereum node (if applicable, replace the URL with your node's address)
  const provider = new ethers.JsonRpcProvider(
    'http://127.0.0.1:9944'
  );

  // Set the custom JSON-RPC method and parameters
  const method = 'engine_createBlock';
  const params = [true, true, null];

  try {
    // Send the custom JSON-RPC call
    const result = await provider.send(method, params);
  } catch (error)
};

produceBlock();
```

!!! note
    If you're unfamiliar with Ethers, please refer to the [Ethers.js](/moonbeam-mkdocs/builders/ethereum/libraries/ethersjs/) documentation page to learn more.

## Prefunded Development Accounts {: #pre-funded-development-accounts }

Moonbeam has a [unified accounts](/moonbeam-mkdocs/learn/core-concepts/unified-accounts/) system, which enables users to have an Ethereum-styled H160 account that can interact with the Substrate API and the Ethereum API. As a result, you can interact with your account through [Polkadot.js Apps](/moonbeam-mkdocs/tokens/connect/polkadotjs/#connect-polkadotjs-apps) or [MetaMask](/moonbeam-mkdocs/tokens/connect/metamask/) (or any other [EVM wallet](/moonbeam-mkdocs/tokens/connect/)). In addition, you can also use other [development tools](/moonbeam-mkdocs/builders/ethereum/dev-env/), such as [Remix](/moonbeam-mkdocs/builders/ethereum/dev-env/remix/) and [Hardhat](/moonbeam-mkdocs/builders/ethereum/dev-env/hardhat/).

Your Moonbeam development node comes with ten prefunded Ethereum-styled accounts for development. The addresses are derived from Substrate's canonical development mnemonic:

```text
bottom drive obey lake curtain smoke basket hold race lonely fit walk
```

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
Also included with the development node is an additional prefunded account used for testing purposes:

- Gerald:
    - Public Address: `0x6Be02d1d3665660d22FF9624b7BE0551ee1Ac91b`
    - Private Key: `0x99b3c12287537e38c90a9219d4cb074a89a16e9cdb20bf85728ebd97c343e342`
You can connect any of these accounts to [MetaMask](/moonbeam-mkdocs/tokens/connect/metamask/), [Talisman](/moonbeam-mkdocs/tokens/connect/talisman/), [Polkadot.js Apps](/moonbeam-mkdocs/tokens/connect/polkadotjs/), etc., using their private keys.

## Development Node Endpoints {: #access-your-development-node }

You can access your Moonbeam development node using the following RPC and WSS endpoints:

=== "HTTP"

    ```text
    http://127.0.0.1:9944
    ```

=== "WSS"

    ```text
    ws://127.0.0.1:9944
    ```

## Block Explorers {: #block-explorers }

For a Moonbeam development node, you can use any of the following block explorers:

 - **Substrate API** — [Polkadot.js Apps](https://polkadot.js.org/apps/?rpc=ws://127.0.0.1:9944#/explorer) on WS port `9944`
 - **Ethereum API JSON-RPC-based** — [Moonbeam Basic Explorer](https://moonbeam-explorer.netlify.app/?network=MoonbeamDevNode) on HTTP port `9944`

## Debug, Trace, and TxPool APIs {: #debug-trace-txpool-apis }

You can also gain access to some non-standard RPC methods by running a tracing node, which allows developers to inspect and debug transactions during runtime. Tracing nodes use a different Docker image than a standard Moonbeam development node.

To learn how to run a Moonbeam development tracing node, check out the [Run a Tracing Node](/moonbeam-mkdocs/node-operators/networks/tracing-node/) guide, and be sure to switch to the **Moonbeam Development Node** tab throughout the instructions. Then, to access the non-standard RPC methods with your tracing node, check out the [Debug & Trace](/moonbeam-mkdocs/builders/ethereum/json-rpc/debug-trace/) guide.

## Purge a Development Node {: #purging-your-node }

If you want to remove data associated with your node, you can purge it. The instructions for purging a node are different depending on how you initially spun up your node.

### Purge a Node Spun Up with Docker {: #purge-docker-node }

If you spun up your node using Docker along with the `-v` flag to specify a mounted directory for your container, you will need to purge that directory. To do so, you can run the following command:

```bash
sudo rm -rf /var/lib/alphanet-data/*
```

If you followed the instructions in this guide and did not use the `-v` flag, you can stop and remove the Docker container. The associated data will be removed along with it. To do so, you can run the following command:

```bash
sudo docker stop `CONTAINER_ID` && docker rm `CONTAINER_ID`
```

### Purge a Node Spun up with a Binary File {: #purge-binary-node }

When running a node via the binary file, data is stored in a local directory, typically located in `~/.local/shared/moonbeam/chains/development/db`. If you want to start a fresh instance of the node, you can either delete the content of the folder or run the following command inside the `moonbeam` folder:

```bash
./target/release/moonbeam purge-chain --dev -y
```

This will remove the data folder. Note that all chain data is now lost. To learn more about all of the available `purge-chain` commands, you can check out the [Purging Binary Data](/moonbeam-mkdocs/node-operators/networks/run-a-node/systemd/#purging-compiled-binary) section of our documentation.
