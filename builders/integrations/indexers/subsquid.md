---
title: Index Data with SQD (formerly Subsquid)
description: Learn how to use SQD (Subsquid), a query node framework for Substrate-based chains, to index and process Substrate and EVM data for Moonbeam and Moonriver.
categories:
- Indexers and Queries
url: https://docs.moonbeam.network/builders/integrations/indexers/subsquid/
word_count: 1706
token_estimate: 2760
version_hash: sha256:afbab7dffb22f0009df1fc090022026feb73573c609d8c4c5a86f10664dc3a53
last_updated: '2026-05-21T21:21:53+00:00'
---

# Indexing Moonbeam with SQD (formerly Subsquid)

## Introduction {: #introduction }

[SQD (formerly Subsquid)](https://sqd.dev/) is a data network that allows rapid and cost-efficient retrieval of blockchain data from 100+ chains using SQD’s decentralized data lake and open-source SDK. In very simple terms, SQD can be thought of as an ETL (extract, transform, and load) tool with a GraphQL server included. It enables comprehensive filtering, pagination, and even full-text search capabilities.

SQD has native and full support for both Ethereum Virtual Machine (EVM) and Substrate data. Since Moonbeam is a Substrate-based smart contact platform that is EVM-compatible, SQD can be used to index both EVM and Substrate-based data. SQD offers a Substrate Archive and Processor and an EVM Archive and Processor. The Substrate Archive and Processor can be used to index both Substrate and EVM data. This allows developers to extract on-chain data from any of the Moonbeam networks and process EVM logs as well as Substrate entities (events, extrinsics, and storage items) in one single project and serve the resulting data with one single GraphQL endpoint. If you exclusively want to index EVM data, it is recommended to use the EVM Archive and Processor.

This quick-start guide will show you how to create Substrate and EVM projects with SQD and configure it to index data on Moonbeam.

<div class="intro-disclaimer">
  The information presented herein is for informational purposes only and has been provided by third parties. Moonbeam does not endorse any project listed and described on the Moonbeam docs website (https://docs.moonbeam.network/).
</div>
## Checking Prerequisites {: #checking-prerequisites }

To get started with SQD, you'll need to have the following:

- [Node.js](https://nodejs.org/en/download) version 16 or newer
- [Docker](https://docs.docker.com/get-started/get-docker/)
- [Squid CLI](https://docs.sqd.ai/squid-cli/installation/)

!!! note
    The Squid template is not compatible with `yarn`, so you'll need to use `npm` instead.

## Index Substrate Data on Moonbeam {: #index-substrate-calls-events }

To get started indexing Substrate data on Moonbeam, you'll need to create a SQD project and configure it for Moonbeam by taking the following steps:

1. Create a SQD project based on the Substrate template by running:

    ```bash
    sqd init INSERT_SQUID_NAME --template substrate
    ```

    For more information on getting started with this template, please check out the [Quickstart: Substrate chains](http://docs.sqd.ai/quickstart/quickstart-substrate/) guide on SQD's documentation site.

2. Navigate into the root directory of your Squid project and install dependencies by running:  

    ```bash
    npm ci
    ```

3. To configure your SQD project to run on Moonbeam, you'll need to update the `typegen.json` file. The `typegen.json` file is responsible for generating TypeScript interface classes for your data. Depending on the network you're indexing data on, the `specVersions` value in the `typegen.json` file should be configured as follows:

    === "Moonbeam"

        ```json
        "specVersions": "https://v2.archive.subsquid.io/metadata/moonbeam",
        ```

    === "Moonriver"

        ```json
        "specVersions": "https://v2.archive.subsquid.io/metadata/moonriver",
        ```

    === "Moonbase Alpha"

        ```json
        "specVersions": "https://v2.archive.subsquid.io/metadata/moonbase",
        ```

4. Modify the `src/processor.ts` file, which is where Squids instantiate the processor, configure it, and attach handler functions. The processor fetches historical on-chain data from an [Archive](https://docs.sqd.ai/glossary/#archives), which is a specialized data lake. You'll need to configure your processor to pull data from the Archive that corresponds to the [network](http://docs.sqd.ai/substrate-indexing/supported-networks/) you are indexing data on:

    === "Moonbeam"

        ```ts
        const processor = new SubstrateBatchProcessor();
        processor.setDataSource({
          chain: 'INSERT_RPC_API_ENDPOINT',
          // Resolves to 'https://v2.archive.subsquid.io/network/moonbeam-mainnet'
          archive: lookupArchive('moonbeam', {type: 'Substrate', release: 'ArrowSquid'}),
        })
        ```

    === "Moonriver"

        ```ts
        const processor = new SubstrateBatchProcessor();
        processor.setDataSource({
          chain: 'INSERT_RPC_API_ENDPOINT',
          // Resolves to 'https://v2.archive.subsquid.io/network/moonriver-mainnet'
          archive: lookupArchive('moonriver', {type: 'Substrate', release: 'ArrowSquid'}),
        })
        ```

    === "Moonbase Alpha"

        ```ts
        const processor = new SubstrateBatchProcessor();
        processor.setDataSource({
          chain: 'https://rpc.api.moonbase.moonbeam.network',
          // Resolves to 'https://v2.archive.subsquid.io/network/moonbase-testnet'
          archive: lookupArchive('moonbase', {type: 'Substrate', release: 'ArrowSquid'}),
        })
        ```

    !!! note
        To configure your project for Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
5. There's one more quick change to make to the template. The SQD Substrate template is configured to process Substrate account types, but Moonbeam uses Ethereum-style accounts. The `getTransferEvents` function in the `src/main.ts` file will iterate through the events ingested by `processor.ts` and store the relevant `transfer` events in the database. In the `getTransferEvents` function, remove the ss58 encoding of the `from` and `to` fields. In an unmodified Substrate template, the `from` and `to` fields are ss58 encoded as shown:

    ```ts
    from: ss58.codec('kusama').encode(rec.from),
    to: ss58.codec('kusama').encode(rec.to),
    ```

    After removing the ss58 encoding, the respective lines are:

    ```ts
    from: rec.from, 
    to: rec.to, 
    ```

And that's all you have to do to configure your SQD project to index Substrate data on Moonbeam! Now you can update the `schema.graphql`, `typegen.json`, `src/main.ts`, and `src/processor.ts` files to index the data you need for your project! Next, take the steps in the [Run your Indexer](#run-your-indexer) section to run your indexer and query your Squid.

## Index Ethereum Data on Moonbeam {: #index-ethereum-contracts }

To get started indexing EVM data on Moonbeam, you'll need to create a SQD project and configure it for Moonbeam by taking the following steps:

1. You can create a SQD project for EVM data by using the generic [EVM template](https://github.com/subsquid-labs/squid-evm-template) or you can use the [ABI template](https://github.com/subsquid-labs/squid-abi-template) for indexing data related to a specific contract:

    === "EVM"

        ```bash
        sqd init INSERT_SQUID_NAME --template evm
        ```

    === "ABI"

        ```bash
        sqd init INSERT_SQUID_NAME --template abi
        ```

    For more information on getting started with both of these templates, please check out the following SQD docs:
      
      - [Quickstart: EVM chains](http://docs.sqd.ai/quickstart/quickstart-ethereum/)
      - [Quickstart: generate from ABI](http://docs.sqd.ai/quickstart/quickstart-abi/)

2. Navigate into the root directory of your Squid project and install dependencies by running:

    ```bash
    npm ci
    ```

3. Modify the `src/processor.ts` file, which is where Squids instantiate the processor, configure it, and attach handler functions. The processor fetches historical on-chain data from an [Archive](https://docs.sqd.ai/glossary/#archives), which is a specialized data lake. You'll need to configure your processor to pull data from the Archive that corresponds to the [network](http://docs.sqd.ai/evm-indexing/supported-networks/) you are indexing data on:

    === "Moonbeam"

        ```ts
        const processor = new EvmBatchProcessor();
        processor.setDataSource({
          chain: 'INSERT_RPC_API_ENDPOINT',
          // Resolves to 'https://v2.archive.subsquid.io/network/moonbeam-mainnet'
          archive: lookupArchive('moonbeam', { type: 'EVM' })
        })
        ```

    === "Moonriver"

        ```ts
        const processor = new EvmBatchProcessor();
        processor.setDataSource({
          chain: 'INSERT_RPC_API_ENDPOINT',
          // Resolves to 'https://v2.archive.subsquid.io/network/moonriver-mainnet'
          archive: lookupArchive('moonriver', { type: 'EVM' }),
        })
        ```

    === "Moonbase Alpha"

        ```ts
        const processor = new EvmBatchProcessor();
        processor.setDataSource({
          chain: 'https://rpc.api.moonbase.moonbeam.network',
          // Resolves to 'https://v2.archive.subsquid.io/network/moonbase-testnet'
          archive: lookupArchive('moonbase', { type: 'EVM' }),
        })
        ```

    !!! note
        To configure your project for Moonbeam or Moonriver, you will need to have your own endpoint and API key, which you can get from one of the supported [Endpoint Providers](/moonbeam-mkdocs/builders/get-started/endpoints/).
And that's all you have to do to configure your SQD project to index EVM data on Moonbeam! Now you can update the `schema.graphql`, `src/main.ts`, and `src/processor.ts` files to index the data you need for your project! Continue with the steps in the following section to run your indexer and query your Squid.

## Run Your Indexer {: #run-your-indexer }

These steps apply to both Substrate and EVM indexers. Running your SQD indexer after you've properly configured it takes only a few steps:  

1. Launch Postgres by running:

    ```bash
    sqd up
    ```

2. Inspect and run the processor:

    ```bash
    sqd process
    ```

3. Open a separate terminal window in the same directory, then start the GraphQL server:

    ```bash
    sqd serve
    ```

4. You can query your template Substrate or EVM Squid with the below sample queries. If you've modified the template Squid to index different data, you'll need to modify this query accordingly

    === "Substrate Indexer"

        ```graphql
        query MyQuery {
          accountsConnection(orderBy: id_ASC)
        }
        ```

    === "EVM Indexer"

        ```graphql
        query MyQuery {
          burns(orderBy: value_DESC)
        }
        ```

For additional examples and workflows, refer to the [SQD documentation](https://docs.sqd.ai/).

<div class="page-disclaimer">
  The information presented herein has been provided by third parties and is made available solely for general information purposes. Moonbeam does not endorse any project listed and described on the Moonbeam Doc Website (https://docs.moonbeam.network/). Moonbeam Foundation does not warrant the accuracy, completeness or usefulness of this information. Any reliance you place on such information is strictly at your own risk. Moonbeam Foundation disclaims all liability and responsibility arising from any reliance placed on this information by you or by anyone who may be informed of any of its contents. All statements and/or opinions expressed in these materials are solely the responsibility of the person or entity providing those materials and do not necessarily represent the opinion of Moonbeam Foundation. The information should not be construed as professional or financial advice of any kind. Advice from a suitably qualified professional should always be sought in relation to any particular matter or circumstance. The information herein may link to or integrate with other websites operated or content provided by third parties, and such other websites may link to this website. Moonbeam Foundation has no control over any such other websites or their content and will have no liability arising out of or related to such websites or their content. The existence of any such link does not constitute an endorsement of such websites, the content of the websites, or the operators of the websites. These links are being provided to you only as a convenience and you release and hold Moonbeam Foundation harmless from any and all liability arising from your use of this information or the information provided by any third-party website or service.
</div>
