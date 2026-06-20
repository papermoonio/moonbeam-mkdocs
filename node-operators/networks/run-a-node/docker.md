---
title: Use Docker to Run a Node
description: How to run a full parachain node so you can have your own RPC endpoint or produce blocks for the Moonbeam Network using Docker.
categories:
- Node Operators and Collators
url: https://docs.moonbeam.network/node-operators/networks/run-a-node/docker/
word_count: 3048
token_estimate: 6257
version_hash: sha256:7f6d4f334d5ce1f6265e71ce01cb3b3eb1b3c9d6732fb6a4390d3c0f4e3d7fc9
last_updated: '2026-05-21T21:21:53+00:00'
---

# Run a Node on Moonbeam Using Docker

## Introduction {: #introduction }

Running a full node on a Moonbeam-based network allows you to connect to the network, sync with a bootnode, obtain local access to RPC endpoints, author blocks on the parachain, and more.

In this guide, you'll learn how to quickly spin up a Moonbeam node using [Docker](https://www.docker.com) and how to maintain and purge your node.

## Checking Prerequisites {: #checking-prerequisites }

To get started, you'll need to:

- [Install Docker](https://docs.docker.com/get-started/get-docker/). At the time of writing, the Docker version used was 24.0.6
- Make sure that your system meets the [requirements](/moonbeam-mkdocs/node-operators/networks/run-a-node/overview/#requirements). When connecting to Moonriver on Kusama or Moonbeam on Polkadot, it will take a few days to completely sync the embedded relay chain

## Set up Storage for Chain Data {: #storage-chain-data }

To set up the directory for storing chain data, you'll need to:

1. Create a local directory

    === "Moonbeam"

        ```bash
        mkdir /var/lib/moonbeam-data
        ```

    === "Moonriver"

        ```bash
        mkdir /var/lib/moonriver-data
        ```

    === "Moonbase Alpha"

        ```bash
        mkdir /var/lib/alphanet-data
        ```

2. Set the ownership and permissions for the local directory that stores the chain data. You can set the permissions either for a specific or current user (replace `INSERT_DOCKER_USER` for the actual user that will run the `docker` command)

    === "Moonbeam"

        ```bash
        # chown to a specific user
        chown INSERT_DOCKER_USER /var/lib/moonbeam-data

        # chown to current user
        sudo chown -R $(id -u):$(id -g) /var/lib/moonbeam-data
        ```

    === "Moonriver"

        ```bash
        # chown to a specific user
        chown INSERT_DOCKER_USER /var/lib/moonriver-data

        # chown to current user
        sudo chown -R $(id -u):$(id -g) /var/lib/moonriver-data
        ```

    === "Moonbase Alpha"

        ```bash
        # chown to a specific user
        chown INSERT_DOCKER_USER /var/lib/alphanet-data

        # chown to current user
        sudo chown -R $(id -u):$(id -g) /var/lib/alphanet-data
        ```

## Start-up Commands {: #start-up-commands }

To spin up your node, you'll need to execute the `docker run` command. If you're setting up a collator node, make sure to follow the code snippets for [collators](#collator-node).

Note that in the following start-up command, you have to:

- Replace `INSERT_YOUR_NODE_NAME` with your node name of choice. You'll have to do this in two places: one for the parachain and one for the relay chain
- Replace `INSERT_RAM_IN_MB` for 50% of the actual RAM your server has. For example, for 32GB of RAM, the value must be set to `16000`. The minimum value is `2000`, but it is below the recommended specs

For an overview of the flags used in the following start-up commands, plus additional commonly used flags, please refer to the [Flags](/moonbeam-mkdocs/node-operators/networks/run-a-node/flags/) page of our documentation.

!!! note "For Apple Silicon users"
    If Docker commands fail or behave unexpectedly on Apple Silicon, enable **Use Rosetta for x86_64/amd64 emulation on Apple Silicon** in Docker Desktop settings and use the `amd64` platform for both pull and run commands. For example:

    ```bash
    docker pull --platform=linux/amd64 moonbeamfoundation/moonbeam:v0.51.2
    ```

    ```bash
    docker run --platform=linux/amd64 ...
    ```

### Full Node {: #full-node }

???+ code "Linux snippets"

    === "Moonbeam"

        ```bash
        docker run --network="host" -v "/var/lib/moonbeam-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonbeam \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        --db-cache INSERT_RAM_IN_MB \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "Moonriver"

        ```bash
        docker run --network="host" -v "/var/lib/moonriver-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonriver \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        --db-cache INSERT_RAM_IN_MB \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "Moonbase Alpha"

        ```bash
        docker run --network="host" -v "/var/lib/alphanet-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain alphanet \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        --db-cache INSERT_RAM_IN_MB \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

??? code "MacOS snippets"

    === "Moonbeam"

        ```bash
        docker run -p 9944:9944 -v "/var/lib/moonbeam-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonbeam \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "Moonriver"

        ```bash
        docker run -p 9944:9944 -v "/var/lib/moonriver-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonriver \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "Moonbase Alpha"

        ```bash
        docker run -p 9944:9944 -v "/var/lib/alphanet-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain alphanet \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

#### Allow External Access to Your Node {: #allow-external-access }

If you want to run an RPC endpoint, connect to Polkadot.js Apps, or run your own application, you can use the `--unsafe-rpc-external` flag to run the full node with external access to the RPC ports.
??? code "Example start-up command for Moonbeam"

    === "Linux"

        ```bash hl_lines="11"
        docker run --network="host" -v "/var/lib/moonbeam-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonbeam \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        --db-cache INSERT_RAM_IN_MB \
        --pool-type=fork-aware \
        --unsafe-rpc-external \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "MacOS"

        ```bash hl_lines="10"
        docker run -p 9944:9944 -v "/var/lib/moonbeam-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonbeam \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        --pool-type=fork-aware \
        --unsafe-rpc-external \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

#### Use a SQL Backend for Frontier {: #use-sql }

The default [Frontier](https://polkadot-evm.github.io/frontier/) database, which comes standard with Moonbeam nodes and contains all of the Ethereum-related elements, such as transactions, blocks, and logs, can be modified to use a SQL backend. Since `eth_getLogs` is a very resource-intensive method, the SQL backend aims to provide a more performant alternative for indexing and querying Ethereum logs in comparison to the default RocksDB database.

To spin up a node with a Frontier SQL backend, you'll need to add the `--frontier-backend-type sql` flag to your start-up command.

There are additional flags you can use to configure the pool size, query timeouts, and more for your SQL backend; please refer to the [Flags](/moonbeam-mkdocs/node-operators/networks/run-a-node/flags/#flags-for-sql-backend) page for more information.
??? code "Example start-up command for Moonbeam"

    === "Linux"

        ```bash hl_lines="12"
        docker run --network="host" -v "/var/lib/moonbeam-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonbeam \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        # This is a comment
        --db-cache INSERT_RAM_IN_MB \
        --pool-type=fork-aware \
        --frontier-backend-type sql \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "MacOS"

        ```bash hl_lines="10"
        docker run -p 9944:9944 -v "/var/lib/moonbeam-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonbeam \
        --name "INSERT_YOUR_NODE_NAME" \
        --state-pruning archive \
        --trie-cache-size 1073741824 \
        --pool-type=fork-aware \
        --frontier-backend-type sql \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

### Collator Node

Beginning with v0.39.0, new Moonbeam collator nodes will no longer generate session keys automatically on start-up. Nodes in existence prior to v0.39.0 do not need to make changes to how they handle session keys. 

When setting up a new node, run the following command to generate and store on disk the session keys that will be referenced in the start-up command: 

=== "Moonbeam"

    ```bash

    docker run --network="host" -v "/var/lib/moonbeam-data:/data" \
    -u $(id -u ${USER}):$(id -g ${USER}) \
     moonbeamfoundation/moonbeam:v0.51.2 key generate-node-key --base-path /var/lib/moonbeam-data --chain moonbeam
    
    ```

=== "Moonriver"

    ```bash

    docker run --network="host" -v "/var/lib/moonriver-data:/data" \
    -u $(id -u ${USER}):$(id -g ${USER}) \
     moonbeamfoundation/moonbeam:v0.51.2 key generate-node-key --base-path /var/lib/moonriver-data --chain moonriver

    ```

=== "Moonbase Alpha"

    ```bash

    docker run --network="host" -v "/var/lib/alphanet-data:/data" \
    -u $(id -u ${USER}):$(id -g ${USER}) \
     moonbeamfoundation/moonbeam:v0.51.2 key generate-node-key --base-path /var/lib/alphanet-data --chain alphanet && sudo chown -R moonbase_service  /var/lib/alphanet-data

    ```

!!! note
    You need to [change ownership of the newly created folder](#storage-chain-data) to the specific user or current user for Docker. Node key generation steps can be bypassed using the `--unsafe-force-node-key-generation` parameter in the start-up command, although this is not the recommended practice.

Now you can run your Docker start up commands:

???+ code "Linux snippets"

    === "Moonbeam"

        ```bash
        docker run --network="host" -v "/var/lib/moonbeam-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonbeam \
        --name "INSERT_YOUR_NODE_NAME" \
        --collator \
        --trie-cache-size 1073741824 \
        --db-cache INSERT_RAM_IN_MB \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "Moonriver"

        ```bash
        docker run --network="host" -v "/var/lib/moonriver-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonriver \
        --name "INSERT_YOUR_NODE_NAME" \
        --collator \
        --trie-cache-size 1073741824 \
        --db-cache INSERT_RAM_IN_MB \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "Moonbase Alpha"

        ```bash
        docker run --network="host" -v "/var/lib/alphanet-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain alphanet \
        --name "INSERT_YOUR_NODE_NAME" \
        --collator \
        --trie-cache-size 1073741824 \
        --db-cache INSERT_RAM_IN_MB \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

??? code "MacOS snippets"

    === "Moonbeam"

        ```bash
        docker run -p 9944:9944 -v "/var/lib/moonbeam-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonbeam \
        --name "INSERT_YOUR_NODE_NAME" \
        --collator \
        --trie-cache-size 1073741824 \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "Moonriver"

        ```bash
        docker run -p 9944:9944 -v "/var/lib/moonriver-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain moonriver \
        --name "INSERT_YOUR_NODE_NAME" \
        --collator \
        --trie-cache-size 1073741824 \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

    === "Moonbase Alpha"

        ```bash
        docker run -p 9944:9944 -v "/var/lib/alphanet-data:/data" \
        -u $(id -u ${USER}):$(id -g ${USER}) \
        moonbeamfoundation/moonbeam:v0.51.2 \
        --base-path /data \
        --chain alphanet \
        --name "INSERT_YOUR_NODE_NAME" \
        --collator \
        --trie-cache-size 1073741824 \
        --pool-type=fork-aware \
        -- \
        --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
        --sync fast
        ```

## Syncing Your Node {: #syncing-your-node }

Once Docker pulls the necessary images, your full node will start, displaying lots of information, such as the chain specification, node name, role, genesis state, and more.

<div id="termynal" data-termynal>
     <span data-ty="input"><span class="file-path"></span>docker run --network="host" -v "/var/lib/alphanet-data:/data" -u $(id -u ${USER}):$(id -g ${USER}) moonbeamfoundation/moonbeam:v0.51.2 --base-path=/data --chain alphanet --name="TestNode" --state-pruning archive --trie-cache-size 1073741824 --db-cache 8000 --name="TestNode (Embedded Relay)"</span>
    <span data-ty>2025-07-10 09:04:26 Moonbeam Parachain Collator </span>
    <span data-ty>2025-07-10 09:04:26 ✌️  version 0.51.2 </span>
    <span data-ty>2025-07-10 09:04:26 ❤️  by PureStake, 2019-2025 </span>
    <span data-ty>2025-07-10 09:04:26 📋 Chain specification: Moonbase Development Testnet </span>
    <span data-ty>2025-07-10 09:04:26 🏷  Node name: TestNode </span>
    <span data-ty>2025-07-10 09:04:26 👤 Role: FULL </span>
    <span data-ty>2025-07-10 09:04:26 💾 Database: RocksDb at /data/chains/moonbase_alpha/db/full </span>
    <span data-ty>2025-07-10 09:04:26 Database: RocksDb at </span>
    <span data-ty>2025-07-10 09:04:26 & Native runtime: moonbase-3501 (moonbase-0.tx2.au4)</span>
    <span data-ty>2025-07-10 09:04:26 Parachain id: Id(1000)</span>
    <span data-ty>2025-07-10 09:04:26 Parachain Account: 5Ec4AhPZk8STuex8Wsi9TwDtJQxKqzPJRCH7348Xtcs9vZLJ</span>
    <span data-ty>2025-07-10 09:04:26 Parachain genesis state: 0x0000000000000000000000000000000000000000000000000000000000000000006505bc9a20d69f14620b2417b6d777c398ceb3e32119b9a53507111d1880927c03170a2e7597b7b7e3d84c05391d139a62b157e78786d8c082f29dcf4c11131400</span>
    <span data-ty>2025-07-10 09:04:26 Is collating: no</span>
    <span data-ty>2025-07-10 09:04:26 [ 1 ^ Initializing Genesis block/state (state: 0xb505..927c, header-hash: 0x91bc...9527)</span>
    <span data-ty>2025-07-10 09:04:26 ［Relaychain］ ^ Initializing Genesis block/state (state: 0x96a6..9426, header-hash: 0xelea..9443)</span>
</div>
During the syncing process, you will see logs from both the embedded relay chain ([Relaychain]) and the parachain ([🌗]). These logs display a target block (live network state) and a best block (local node synced state).

<div id="termynal" data-termynal>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ 10 Syncing 137.9 bps, target=#12325010 (8 peers), best: #21001 (0x25d9...57d8), finalized #20992 (0x1ebb..fd23), # 214.4kiB/s 11.7kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 🌗 ⚙️ * Syncing 182.7 bps, target=#5219905 (8 peers), best: #22472 (0x875f..aed7), finalized #9625 (0x601b...e64f), # 371.0kiB/s 113.3kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ I Syncing 186.6 bps, target=#12325011 (8 peers), best: #21935 (0x58f8...d312), finalized #21585 (0x1d73...13c8), #271.9kiB/s T1.3kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 🌗 ⚙️ @ Syncing 193.4 bps, target=#5219905 (8 peers), best: #23440 (0xdce6...8ea6), finalized #9922 (0x07c9...1fdf), # 383.3kiB/s 17.5kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ Ö Syncing 189.5 bps, target=#12325012 (8 peers), best: #22883 (0x6531.2281), finalized #22528 (0x0f21.0855), # 290.8kiB/s 10.6kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 🌗 ⚙️ @ Syncing 206.4 bps, target=#5219905 (8 peers), best: #24474 (0x09dd...6700), finalized #10393 (0x3efc...8a40), #428.7kiB/s 12.4kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ . Syncing 171.6 bps, target=#12325013 (8 peers), best: #23744 (0x4ced...cdae), finalized #23552 (0x1773..09d9), # 252.4kiB/s 10.6kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 🌗 ⚙️ Syncing 212.3 bps, target=#5219905 (8 peers), best: #25536 (0x7bc0...e9b7), finalized #10905 (0x5c70...3063), 1427.1kiB/s 11.4kiB/s</span>
</div>
If you followed the installation instructions for Moonbase Alpha, once synced, you will have a node of the Moonbase Alpha TestNet running locally! For Moonbeam or Moonriver, once synced, you will be connected to peers and see blocks being produced on the network!

!!! note
    It may take a few days to completely sync the embedded relay chain. Make sure that your system meets the [requirements](/moonbeam-mkdocs/node-operators/networks/run-a-node/overview/#requirements).

## Maintain Your Node {: #maintain-your-node }

As Moonbeam development continues, it will sometimes be necessary to upgrade your node software. Node operators will be notified on our [Discord channel](https://discord.com/invite/PfpUATX) when upgrades are available and whether they are necessary (some client upgrades are optional). The upgrade process is straightforward and is the same for a full node or collator.

1. Stop the Docker container:

    ```bash
    sudo docker stop INSERT_CONTAINER_ID
    ```

2. Get the latest version of Moonbeam from the [Moonbeam GitHub Release](https://github.com/moonbeam-foundation/moonbeam/releases) page
3. Use the latest version to spin up your node. To do so, replace the version in the start-up command with the latest and run it

Once your node is running again, you should see logs in your terminal.

## Purge Your Node {: #purge-your-node }

If you need a fresh instance of your Moonbeam node, you can purge your node by removing the associated data directory.

You'll first need to stop the Docker container:

```bash
  sudo docker stop INSERT_CONTAINER_ID
```

If you did not use the `-v` flag to specify a local directory for storing your chain data when you spun up your node, then the data folder is related to the Docker container itself. Therefore, removing the Docker container will remove the chain data.

If you did spin up your node with the `-v` flag, you will need to purge the specified directory. For example, for the suggested data directly, you can run the following command to purge your parachain and relay chain data:

=== "Moonbeam"

    ```bash
    sudo rm -rf /var/lib/moonbeam-data/*
    ```

=== "Moonriver"

    ```bash
    sudo rm -rf /var/lib/moonriver-data/*
    ```

=== "Moonbase Alpha"

    ```bash
    sudo rm -rf /var/lib/alphanet-data/*
    ```

To only remove the parachain data for a specific chain, you can run:

=== "Moonbeam"

    ```bash
    sudo rm -rf /var/lib/moonbeam-data/chains/*
    ```

=== "Moonriver"

    ```bash
    sudo rm -rf /var/lib/moonriver-data/chains/*
    ```

=== "Moonbase Alpha"

    ```bash
    sudo rm -rf /var/lib/alphanet-data/chains/*
    ```

Similarly, to only remove the relay chain data, you can run:

=== "Moonbeam"

    ```bash
    sudo rm -rf /var/lib/moonbeam-data/polkadot/*
    ```

=== "Moonriver"

    ```bash
    sudo rm -rf /var/lib/moonriver-data/polkadot/*
    ```

=== "Moonbase Alpha"

    ```bash
    sudo rm -rf /var/lib/alphanet-data/polkadot/*
    ```

Now that your chain data has been purged, you can start a new node with a fresh data directory. You can install the newest version by repeating the instructions in this guide. Make sure you are using the latest tag available, which you can find on the [Moonbeam GitHub Release](https://github.com/moonbeam-foundation/moonbeam/releases) page.
## Purge Your Frontier Database {: #purge-frontier-database }

To purge only the Frontier database of your Moonbeam node, follow these steps:

1. Stop the Docker container:

    ```bash
    sudo docker stop INSERT_CONTAINER_ID
    ```

2. Remove the Frontier database folder:

    === "Moonbeam"

        ```bash
        sudo rm -rf /var/lib/moonbeam-data/chains/moonbeam/frontier/*
        ```

    === "Moonriver"

        ```bash
        sudo rm -rf /var/lib/moonriver-data/chains/moonriver/frontier/*
        ```

    === "Moonbase Alpha"

        ```bash
        sudo rm -rf /var/lib/alphanet-data/chains/alphanet/frontier/*
        ```

3. Start the Docker container again using the [start-up command](#start-up-commands) for your node type
