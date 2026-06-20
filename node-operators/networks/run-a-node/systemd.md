---
title: Run a Node on Moonbeam Using Systemd
description: How to run a full parachain node so you can have your own RPC endpoint or produce blocks for the Moonbeam Network using Systemd.
categories:
- Node Operators and Collators
url: https://docs.moonbeam.network/node-operators/networks/run-a-node/systemd/
word_count: 2843
token_estimate: 5461
version_hash: sha256:b629e28386a283843dcc91850a65735b2a73caea68e65f8adf204e57fb96407d
last_updated: '2026-05-21T21:21:53+00:00'
---

# Run a Node on Moonbeam Using Systemd

## Introduction {: #introduction }

Running a full node on a Moonbeam-based network allows you to connect to the network, sync with a bootnode, obtain local access to RPC endpoints, author blocks on the parachain, and more.

In this guide, you'll learn how to spin up a Moonbeam node using [Systemd](https://systemd.io) and how to maintain and purge your node.

If you're interested in compiling the binary yourself, which may take over 30 min and require 32GB of memory, you can check out the [Manually Compile the Moonbeam Binary](/moonbeam-mkdocs/node-operators/networks/run-a-node/compile-binary/) guide.

## Checking Prerequisites {: #checking-prerequisites }

The following sections go through the process of using the binary and running a Moonbeam full node as a systemd service. To get started, you'll need to:

- Make sure you're running Ubuntu 18.04, 20.04, or 22.04. Moonbeam may work with other Linux flavors, but Ubuntu is currently the only tested version
- Make sure that your system meets the [requirements](/moonbeam-mkdocs/node-operators/networks/run-a-node/overview/#requirements). When connecting to Moonriver on Kusama or Moonbeam on Polkadot, it will take a few days to completely sync the embedded relay chain

## Download the Latest Release Binary {: #the-release-binary }

To download the latest [release binary](https://github.com/moonbeam-foundation/moonbeam/releases), take the following steps:

1. Create a directory to store the binary and chain data (you might need `sudo`)

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

2. Use `wget` to grab the latest [release binary](https://github.com/moonbeam-foundation/moonbeam/releases) and output it to the directory created in the previous step

    === "Moonbeam"

        ```bash
        wget https://github.com/moonbeam-foundation/moonbeam/releases/download/v0.51.2/moonbeam \
        -O /var/lib/moonbeam-data/moonbeam
        ```

    === "Moonriver"

        ```bash
        wget https://github.com/moonbeam-foundation/moonbeam/releases/download/v0.51.2/moonbeam \
        -O /var/lib/moonriver-data/moonbeam
        ``` 

    === "Moonbase Alpha"

        ```bash
        wget https://github.com/moonbeam-foundation/moonbeam/releases/download/v0.51.2/moonbeam \
        -O /var/lib/alphanet-data/moonbeam
        ```

3. To verify that you have downloaded the correct version, you can run the following command in your terminal

    === "Moonbeam"

        ```bash
        sha256sum /var/lib/moonbeam-data/moonbeam
        ```

    === "Moonriver"

        ```bash
        sha256sum /var/lib/moonriver-data/moonbeam
        ```

    === "Moonbase Alpha"

        ```bash
        sha256sum /var/lib/alphanet-data/moonbeam
        ```

    You should receive the following output:

    === "Moonbeam"

        ```text
        58b5f7c87b338202dcecbb558fc6f0fdd861f64ba68acfc025acb1b2d4e7d2b3
        ```

    === "Moonriver"

        ```text
        58b5f7c87b338202dcecbb558fc6f0fdd861f64ba68acfc025acb1b2d4e7d2b3
        ```

    === "Moonbase Alpha"

        ```text
        58b5f7c87b338202dcecbb558fc6f0fdd861f64ba68acfc025acb1b2d4e7d2b3
        ```

## Set Up the Service {: #set-up-the-service }

The following commands will set up everything regarding running the service:

1. Create a service account to run the service

    === "Moonbeam"

        ```bash
        adduser moonbeam_service --system --no-create-home
        ```

    === "Moonriver"

        ```bash
        adduser moonriver_service --system --no-create-home
        ```

    === "Moonbase Alpha"

        ```bash
        adduser moonbase_service --system --no-create-home
        ```

2. Ensure that you properly configure the ownership and permissions for the local directory housing the chain data, and also remember to grant execute permission to the binary file

    === "Moonbeam"

        ```bash
        sudo chown -R moonbeam_service /var/lib/moonbeam-data
        sudo chmod +x /var/lib/moonbeam-data/moonbeam
        ```

    === "Moonriver"

        ```bash
        sudo chown -R moonriver_service /var/lib/moonriver-data
        sudo chmod +x /var/lib/moonriver-data/moonbeam
        ```

    === "Moonbase Alpha"

        ```bash
        sudo chown -R moonbase_service /var/lib/alphanet-data
        sudo chmod +x /var/lib/alphanet-data/moonbeam
        ```

## Create the Configuration File {: #create-the-configuration-file }

Next, create the systemd service file. If you're configuring a collator node, use the [collator-specific](#collator) configuration snippets below.

First, you'll need to create a file named `/etc/systemd/system/moonbeam.service` to store the configurations.

Note that in the following start-up configurations, you have to:

- Replace `INSERT_YOUR_NODE_NAME` with your node name of choice. You'll have to do this in two places: one for the parachain and one for the relay chain
- Replace `INSERT_RAM_IN_MB` for 50% of the actual RAM your server has. For example, for 32GB of RAM, the value must be set to `16000`. The minimum value is `2000`, but it is below the recommended specs
- Double-check that the binary is in the proper path as described below (_ExecStart_)
- Double-check the base path if you've used a different directory

For an overview of the flags used in the following start-up commands, plus additional commonly used flags, please refer to the [Flags](/moonbeam-mkdocs/node-operators/networks/run-a-node/flags/) page of our documentation.

### Full Node {: #full-node }

=== "Moonbeam"

    ```bash
    [Unit]
    Description="Moonbeam systemd service"
    After=network.target
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=on-failure
    RestartSec=10
    User=moonbeam_service
    SyslogIdentifier=moonbeam
    SyslogFacility=local7
    KillSignal=SIGHUP
    ExecStart=/var/lib/moonbeam-data/moonbeam \
         --state-pruning archive \
         --trie-cache-size 1073741824 \
         --db-cache INSERT_RAM_IN_MB \
         --base-path /var/lib/moonbeam-data \
         --chain moonbeam \
         --name "INSERT_YOUR_NODE_NAME" \
         -- \
         --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
         --sync fast
    
    [Install]
    WantedBy=multi-user.target
    ```

=== "Moonriver"

    ```bash
    [Unit]
    Description="Moonriver systemd service"
    After=network.target
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=on-failure
    RestartSec=10
    User=moonriver_service
    SyslogIdentifier=moonriver
    SyslogFacility=local7
    KillSignal=SIGHUP
    ExecStart=/var/lib/moonriver-data/moonbeam \
         --state-pruning archive \
         --trie-cache-size 1073741824 \
         --db-cache INSERT_RAM_IN_MB \
         --base-path /var/lib/moonriver-data \
         --chain moonriver \
         --name "INSERT_YOUR_NODE_NAME" \
         -- \
         --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
         --sync fast
    
    [Install]
    WantedBy=multi-user.target
    ```

=== "Moonbase Alpha"

    ```bash
    [Unit]
    Description="Moonbase Alpha systemd service"
    After=network.target
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=on-failure
    RestartSec=10
    User=moonbase_service
    SyslogIdentifier=moonbase
    SyslogFacility=local7
    KillSignal=SIGHUP
    ExecStart=/var/lib/alphanet-data/moonbeam \
         --state-pruning archive \
         --trie-cache-size 1073741824 \
         --db-cache INSERT_RAM_IN_MB \
         --base-path /var/lib/alphanet-data \
         --chain alphanet \
         --name "INSERT_YOUR_NODE_NAME" \
         -- \
         --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
         --sync fast

    [Install]
    WantedBy=multi-user.target
    ```

#### Allow External Access to Your Node {: #allow-external-access }

If you want to run an RPC endpoint, connect to Polkadot.js Apps, or run your own application, you can use the `--unsafe-rpc-external` flag to run the full node with external access to the RPC ports.
??? code "Example start-up command for Moonbeam"

    ```bash
    [Unit]
    Description="Moonbeam systemd service"
    After=network.target
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=on-failure
    RestartSec=10
    User=moonbeam_service
    SyslogIdentifier=moonbeam
    SyslogFacility=local7
    KillSignal=SIGHUP
    ExecStart=/var/lib/moonbeam-data/moonbeam \
         --state-pruning archive \
         --trie-cache-size 1073741824 \
         --db-cache INSERT_RAM_IN_MB \
         --base-path /var/lib/moonbeam-data \
         --chain moonbeam \
         --name "INSERT_YOUR_NODE_NAME" \
         --unsafe-rpc-external \
         -- \
         --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
         --sync fast
    
    [Install]
    WantedBy=multi-user.target
    ```

#### Use a SQL Backend for Frontier {: #use-sql }

The default [Frontier](https://polkadot-evm.github.io/frontier/) database, which comes standard with Moonbeam nodes and contains all of the Ethereum-related elements, such as transactions, blocks, and logs, can be modified to use a SQL backend. Since `eth_getLogs` is a very resource-intensive method, the SQL backend aims to provide a more performant alternative for indexing and querying Ethereum logs in comparison to the default RocksDB database.

To spin up a node with a Frontier SQL backend, you'll need to add the `--frontier-backend-type sql` flag to your start-up command.

There are additional flags you can use to configure the pool size, query timeouts, and more for your SQL backend; please refer to the [Flags](/moonbeam-mkdocs/node-operators/networks/run-a-node/flags/#flags-for-sql-backend) page for more information.
??? code "Example start-up command for Moonbeam"

    ```bash
    [Unit]
    Description="Moonbeam systemd service"
    After=network.target
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=on-failure
    RestartSec=10
    User=moonbeam_service
    SyslogIdentifier=moonbeam
    SyslogFacility=local7
    KillSignal=SIGHUP
    ExecStart=/var/lib/moonbeam-data/moonbeam \
         --state-pruning archive \
         --trie-cache-size 1073741824 \
         --db-cache INSERT_RAM_IN_MB \
         --base-path /var/lib/moonbeam-data \
         --chain moonbeam \
         --name "INSERT_YOUR_NODE_NAME" \
         --frontier-backend-type sql \
         -- \
         --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
         --sync fast
    
    [Install]
    WantedBy=multi-user.target
    ```

### Collator {: #collator }

Beginning with v0.39.0, new Moonbeam collator nodes will no longer generate session keys automatically on start-up. Nodes in existence prior to v0.39.0 do not need to make changes to how they handle session keys.

When setting up a new node, run the following command to generate and store on disk the session keys that will be referenced in the start-up command:

=== "Moonbeam"

    ```bash

    /var/lib/moonbeam-data/moonbeam key generate-node-key --base-path /var/lib/moonbeam-data --chain moonbeam && sudo chown -R moonbeam_service /var/lib/moonbeam-data
    
    ```

=== "Moonriver"

    ```bash

    /var/lib/moonriver-data/moonbeam key generate-node-key --base-path /var/lib/moonriver-data --chain moonriver && sudo chown -R moonriver_service /var/lib/moonriver-data

    ```

=== "Moonbase Alpha"

    ```bash

    /var/lib/alphanet-data/moonbeam key generate-node-key --base-path /var/lib/alphanet-data --chain alphanet  && sudo chown -R moonbase_service  /var/lib/alphanet-data

    ```

!!! note
    This step can be bypassed using the `--unsafe-force-node-key-generation` parameter in the start-up command, although this is not the recommended practice.

Now you can create the systemd configuration file:

=== "Moonbeam"

    ```bash
    [Unit]
    Description="Moonbeam systemd service"
    After=network.target
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=on-failure
    RestartSec=10
    User=moonbeam_service
    SyslogIdentifier=moonbeam
    SyslogFacility=local7
    KillSignal=SIGHUP
    ExecStart=/var/lib/moonbeam-data/moonbeam \
         --collator \
         --trie-cache-size 1073741824 \
         --db-cache INSERT_RAM_IN_MB \
         --base-path /var/lib/moonbeam-data \
         --chain moonbeam \
         --name "INSERT_YOUR_NODE_NAME" \
         -- \
         --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
         --sync fast
    
    [Install]
    WantedBy=multi-user.target
    ```

=== "Moonriver"

    ```bash
    [Unit]
    Description="Moonriver systemd service"
    After=network.target
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=on-failure
    RestartSec=10
    User=moonriver_service
    SyslogIdentifier=moonriver
    SyslogFacility=local7
    KillSignal=SIGHUP
    ExecStart=/var/lib/moonriver-data/moonbeam \
         --collator \
         --trie-cache-size 1073741824 \
         --db-cache INSERT_RAM_IN_MB \
         --base-path /var/lib/moonriver-data \
         --chain moonriver \
         --name "INSERT_YOUR_NODE_NAME" \
         -- \
         --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
         --sync fast
    
    [Install]
    WantedBy=multi-user.target
    ```

=== "Moonbase Alpha"

    ```bash
    [Unit]
    Description="Moonbase Alpha systemd service"
    After=network.target
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=on-failure
    RestartSec=10
    User=moonbase_service
    SyslogIdentifier=moonbase
    SyslogFacility=local7
    KillSignal=SIGHUP
    ExecStart=/var/lib/alphanet-data/moonbeam \
         --collator \
         --trie-cache-size 1073741824 \
         --db-cache INSERT_RAM_IN_MB \
         --base-path /var/lib/alphanet-data \
         --chain alphanet \
         --name "INSERT_YOUR_NODE_NAME" \
         -- \
         --name "INSERT_YOUR_NODE_NAME (Embedded Relay)" \
         --sync fast

    [Install]
    WantedBy=multi-user.target
    ```

## Run the Service {: #run-the-service }

Register and start the service by running:

```bash
systemctl enable moonbeam.service
systemctl start moonbeam.service
```

And lastly, verify that the service is running:

```bash
systemctl status moonbeam.service
```
<div id="termynal" data-termynal>
    <span data-ty="input"><span class="file-path"></span> systemctl status moonbeam.service</span>
    <span data-ty>• moonbeam.service - "Moonbase Alpha systemd service"</span>
    <span data-ty>   Loaded: loaded (/etc/systemd/system/moonbeam.service; enabled; vendor preset:></span>
    <span data-ty>   Active: active (running) since Tue 2025-07-10 09:04:26 UTC; 45 ago</span>
    <span data-ty>   Main PID: 52847 (moonbeam)</span>
    <span data-ty>   Tasks: 13 (limit: 4662)</span>
    <span data-ty>   Memory: 113.7M</span>
    <span data-ty>   CPU: 6.9995</span>
    <span data-ty>   CGroup: /system.slice/moonbeam.service</span>
    <span data-ty>       └─52847 /var/lib/alphanet-data/moonbeam --state-pruning=archive --tri></span>
    <span data-ty>lines 1-9/9 (END)</span>
</div>
You can also check the logs by executing:

```bash
journalctl -f -u moonbeam.service
```

<div id="termynal" data-termynal>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ @ Syncing 158.7 bps, target=#12361301 (9 peers), best: #35487 (0x527e...c72b), finalized #35328 (0xfcd2...828), # 239.9kiB/s 15.6kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 Syncing 150.7 bps, target=#5236155 (9 peers), best: #40870 (0x3659...c530), finalized #16793 (0x815...578), # 299.7kiB/s 10.6kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ Syncing 162.5 bps, target=#12361302 (9 peers), best: #36300 (0x9edb..b2c2), finalized #35985 (0x7345..e874), +256.6kiB/s 19.6kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26  Syncing 168.8 bps, target=#5236155 (9 peers), best: #41714 (0x2feb...3f10), finalized #17122 (0x4954...8161), +353.2kiB/s 11.4kB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ @ Syncing 181.3 bps, target=#12361303 (9 peers), best: #37208 (0xbad2...6c2d), finalized #36864 (0x3015..bd42), # 288.4kiB/s 14.8kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 Syncing 161.9 bps, target=#5236155 (9 peers), best: #42525 (0x9711...0de7), finalized #17561 (0x56f4...ad20), # 310.0kiB/s 11.0kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 [Relaychain] 🌗 ⚙️ @ Syncing 166.0 bps, target=#12361303 (9 peers), best: #38039 (0xb19f445c), finalized #37888 (0x68bb...6900), +176.9kiB/s 13.1kiB/s</span>
<span data-ty>moonbase[52847]: 2025-07-10 09:04:26 Syncing 183.7 bps, target=#5236155 (9 peers), best: #43444 (0xccd0...a18f), finalized #18073 (0xe474...2032), #357.3kiB/s 10.3kiB/s</span>
</div>
During the syncing process, you will see logs from both the embedded relay chain ([Relaychain]) and the parachain ([🌗]). These logs display a target block (live network state) and a best block (local node synced state).

!!! note
    It may take a few days to completely sync the embedded relay chain. Make sure that your system meets the [requirements](/moonbeam-mkdocs/node-operators/networks/run-a-node/overview/#requirements).

If you need to stop the service for any reason, you can run:

```bash
systemctl stop moonbeam.service
```

## Maintain Your Node {: #maintain-your-node }

As Moonbeam development continues, it will sometimes be necessary to upgrade your node software. Node operators will be notified on our [Discord channel](https://discord.com/invite/PfpUATX) when upgrades are available and whether they are necessary (some client upgrades are optional). The upgrade process is straightforward and is the same for a full node or collator.

If you want to update your client, you can keep your existing chain data in tact, and only update the binary by following these steps:

1. Stop the systemd service

    ```bash
    sudo systemctl stop moonbeam.service
    ```

2. Remove the old binary file

    === "Moonbeam"

        ```bash
        rm /var/lib/moonbeam-data/moonbeam
        ```

    === "Moonriver"

        ```bash
        rm /var/lib/moonriver-data/moonbeam
        ```

    === "Moonbase Alpha"

        ```bash
        rm /var/lib/alphanet-data/moonbeam
        ```

3. Get the latest version of the [Moonbeam release binary on GitHub](https://github.com/moonbeam-foundation/moonbeam/releases) and run the following command to update to that version

    === "Moonbeam"

        ```bash
        wget https://github.com/moonbeam-foundation/moonbeam/releases/download/INSERT_NEW_VERSION_TAG/moonbeam \
        -O /var/lib/moonbeam-data/moonbeam
        ```

    === "Moonriver"

        ```bash
        wget https://github.com/moonbeam-foundation/moonbeam/releases/download/INSERT_NEW_VERSION_TAG/moonbeam \
        -O /var/lib/moonriver-data/moonbeam
        ```

    === "Moonbase Alpha"

        ```bash
        wget https://github.com/moonbeam-foundation/moonbeam/releases/download/INSERT_NEW_VERSION_TAG/moonbeam \
        -O /var/lib/alphanet-data/moonbeam
        ```

    !!! note
        If you [compiled the binary manually](/moonbeam-mkdocs/node-operators/networks/run-a-node/compile-binary/), you'll need to move the binary from `./target/release/moonbeam` to the data directory.

4. Update permissions

    === "Moonbeam"

        ```bash
        chmod +x /var/lib/moonbeam-data/moonbeam
        chown moonbeam_service /var/lib/moonbeam-data/moonbeam
        ```

    === "Moonriver"

        ```bash
        chmod +x /var/lib/moonriver-data/moonbeam
        chown moonriver_service /var/lib/moonriver-data/moonbeam
        ```

    === "Moonbase Alpha"

        ```bash
        chmod +x /var/lib/alphanet-data/moonbeam
        chown moonbase_service /var/lib/alphanet-data/moonbeam
        ```

5. Start your service

    ```bash
    systemctl start moonbeam.service
    ```

To check the status of the service and/or logs, you can refer to the [commands from before](#run-the-service).

## Purge Your Node {: #purge-your-node }

If you need a fresh instance of your Moonbeam node, you can purge your node by removing the associated data directory.

You'll first need to stop the systemd service:

```bash
sudo systemctl stop moonbeam
```

To purge your parachain and relay chain data, you can run the following command:

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

1. Stop the systemd service:

    ```bash
    sudo systemctl stop moonbeam.service
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

3. Start the systemd service:

    ```bash
    sudo systemctl start moonbeam.service
    ```
