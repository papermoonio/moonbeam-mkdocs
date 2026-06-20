---
title: List your Dapp on the Moonbeam DApp Directory
description: Follow this tutorial to learn how to list your Moonbeam or Moonriver project or update a current listing on the Moonbeam Foundation DApp Directory.
categories:
- Reference
url: https://docs.moonbeam.network/learn/dapp-directory/
word_count: 11900
token_estimate: 28377
version_hash: sha256:4e64ab357176ea7ddefc85cf4a7c269ca20bd5eb892be5b7d8812d9e4aabb29a
last_updated: '2026-05-21T21:21:53+00:00'
---

# How to List your Project on the Moonbeam DApp Directory

## Introduction to the Moonbeam DApp Directory {: #introduction-to-state-of-the-dapps }

The Moonbeam ecosystem comprises two distinct production networks: Moonbeam and Moonriver. Each network has its own dedicated DApp Directory, maintained by the Moonbeam Foundation: [Moonbeam](https://apps.moonbeam.network/moonbeam/app-dir) and [Moonriver](https://apps.moonbeam.network/moonriver/app-dir). These directories categorize projects spanning from DeFi to NFTs to gaming, providing users with comprehensive access to diverse applications.

You'll supply core project details like name, description, and relevant links when adding your project. Depending on your project type, you may include additional data such as on-chain stats and token information.

Despite the distinction between the Moonbeam and Moonriver DApp directories, the submission process remains the same. To list your project on the DApp Directory, you must submit a pull request to the [Moonbeam Foundation's App Directory Data repository on GitHub](https://github.com/moonbeam-foundation/app-directory-data). This guide outlines the necessary data and formatting specifics for your submission.

![The Moonbeam DApp Directory home page](/moonbeam-mkdocs/images/learn/dapps-list/directory-1.webp)

## Overview of the Project Data {: #overview-project-data }

There are four main sources of data that are used for a project's listing in the Moonbeam DApp Directory:

- **Core project data**: Core project data such as descriptions, logos, and screenshots. This data also includes IDs used to query data from external platforms.
- **Active users and transaction volume**: On-chain data based on smart contract activity for all of the contracts associated with the project. Data is discovered via the use of contract labeling in Moonscan and is indexed and consumed by the DApp Directory.
- **TVL data**: TVL data for the protocol, sourced from the project's listing on DefiLlama.
- **Project token information**: Token information, which is sourced from the project's listing on CoinGecko.

## Prerequisites for Using External Data Sources {: #configuring-external-data-sources }

Before pulling data from the mentioned sources, certain prerequisites must be fulfilled. However, it's worth noting that these steps may not apply to all project types. For instance, in the case of wallets, where there are no smart contracts, the DApp Directory is currently unable to display user and transaction activity data.

### Configure the Data Source for Active Users and Transaction Volume {: #configure-active-users }

For projects that have smart contracts deployed on Moonbeam or Moonriver, it is important that those contracts can be linked to the DApp Directory project data.

The end-to-end flow for linking smart contract activity to the DApp Directory is as follows:

1. The smart contract owner fills in the [form to label contracts on Moonscan](https://moonscan.io/contactus?id=5).
2. The contracts become labeled in Moonscan.
3. Labeled contracts can then be ingested by ecosystem analytics providers to index activity for your project.
4. (Recommended) Register your project with FiDi so your activity can be indexed and publicly viewable. See the FiDi registration section below.

To get your project's smart contracts properly labeled on [Moonscan](https://moonscan.io), submit the [Moonscan contract labeling form](https://moonscan.io/contactus?id=5) with your project and contract details.

### Register with FiDi for Analytics (Recommended)

New and existing projects are encouraged to register with FiDi so your project's activity can be indexed and surfaced in public analytics. Submit your project using the [FiDi Project Listing Form](https://docs.google.com/forms/d/e/1FAIpQLSc8c5iOzwIHhLJKRTnC48j7CAj9JY8i_lHxryNBdJdzIyDx3Q/viewform).

After submission, Moonbeam FiDi analytics can be viewed on the [Moonbeam FiDi Dashboard](https://moonbeam.fidi.tech/dashboard/moonbeam).

Required Project Information:

Where possible, include a short purpose description for each contract to improve completeness.

- **Core smart contracts**: Addresses of main contracts that define core functionality and interact significantly with the network. Optionally, include a brief description of each contract's purpose.
- **Factory contracts**: If applicable, addresses of any contracts that deploy other contracts as part of your dApp. Please also provide the creation topic (hash of the creation event) for each factory contract.
- **Deployer wallets**: If applicable, addresses of wallets used to deploy your project's contracts.

Additional Project-Specific Information (Optional):

- **Treasury/Admin wallets**: Addresses of wallets with administrative control or funds. Optionally, include a brief description of each wallet's function.
- **Oracle contracts**: Addresses of any oracle contracts. Optionally, include a brief description of what data these oracles provide.
- **Bridge contracts**: Addresses of any bridge contracts and the list of connected chains.
- **Governance contracts**: Addresses of any contracts related to on-chain governance. Optionally, include a brief explanation of your governance model.

Additional considerations:

- If your project batches transactions, consider using the Batch Precompile.
- Factory contracts should derive from or mimic the standard Uniswap factory.
- Diamond (multi-facet proxy) contracts are supported and will be indexed correctly.
- Typical listing time is 1–2 weeks; FiDi may reach out for clarifications.

Once you've labeled your smart contracts and are ready to submit your project to the DApp Directory, configuring the Directory to utilize your smart contract data becomes straightforward. You'll only need the **Project** component of your labeled contracts.

Consider the following example project with two smart contracts: a Comptroller and a Router recently updated to a new version.

|  Project   | Contract Name | Contract Version |      Resulting Label       |
|:----------:|:-------------:|:----------------:|:--------------------------:|
| My Project |  Comptroller  |        V1        | My Project: Comptroller V1 |
| My Project |    Router     |        V2        |   My Project: Router V2    |

To submit your project to the Moonbeam DApp Directory, ensure you have your **Project** name ready, identified here as `My Project`.

If you're ready to add your project to the DApp Directory, skip to the [How to Submit Your Project Listing](#how-to-submit-your-project-listing) section.

### Configure the Data Source for TVL {: #configure-tvl }

If the project represents a DeFi protocol with TVL (whereby value is locked in the protocol's smart contract), it is possible to display TVL in the Moonbeam DApp Directory.

TVL data is pulled from [DefiLlama](https://defillama.com), so you must list your project there. To get your project listed, please refer to DefiLlama's documentation on [How to list a DeFi project](https://docs.llama.fi/list-your-project/submit-a-project).

After listing your project, you can easily configure the DApp Directory to pull data from DefiLlama. To do so, you'll need the DefiLlama identifier, which you can find in the URL for your protocol's page. For example, the URL for Moonwell's page is `https://defillama.com/protocol/moonwell`, so the identifier is `moonwell`.

If you have the identifier and are ready to submit your project to the Moonbeam DApp Directory, skip to the [How to Submit Your Project Listing](#how-to-submit-your-project-listing) section.

### Configure the Data Source for Project Token Information {: #project-token-information }

If a project has a token, it is possible to display the name of the token, current price, and contract in the DApp Directory.

However, the data is pulled from [CoinGecko](https://www.coingecko.com), so the project's token must be listed there. If your token is not listed there, you can complete [CoinGecko's Request Form](https://support.coingecko.com/hc/en-us/requests/new) to initiate the listing process.

Assuming your project's token is listed there, you must obtain the CoinGecko **API ID** value. You can find the **API ID** value in the **Information** section of the token's page on CoinGecko. For example, the **API ID** on [Moonwell's token page](https://www.coingecko.com/en/coins/moonwell) is `moonwell-artemis`.

If you have the CoinGecko ID and are ready to submit your project to the Moonbeam DApp Directory, you can continue to the next section.

## How to Submit Your Project Listing {: #how-to-submit-your-project-listing }

As mentioned, you must submit a pull request to the Moonbeam Foundation's GitHub repository that holds the DApp Directory's data. Before getting started, it's worth noting that to expedite the review process, the GitHub user who submits the pull request is recommended to be a major contributor to the project's GitHub so that the Moonbeam Foundation can quickly verify that they represent the project. You can check out the [Review Process](#review-process) section for more information.

To begin, you have two options for adding your project information to the [`app-directory-data` repository on GitHub](https://github.com/moonbeam-foundation/app-directory-data). You can utilize [GitHub's browser-based editor](https://github.dev/moonbeam-foundation/app-directory-data), which offers a user-friendly interface.

![The app-directory-data repository loaded on GitHub's browser-based editor](/moonbeam-mkdocs/images/learn/dapps-list/directory-2.webp)

Or you can clone the repository locally and make modifications using your preferred code editor, in which you can use the following command to clone the repository:

```bash
git clone https://github.com/moonbeam-foundation/app-directory-data.git
```

Once you've cloned the project, you can create a new branch to which you will add all of your changes. To do this on the browser-based editor, take the following steps:

1. Click on the current branch name in the bottom left corner.
2. A menu will appear at the top of the page. Enter the name of your branch.
3. Click **Create new branch...**.

![Create a new branch on GitHub's browser-based editor](/moonbeam-mkdocs/images/learn/dapps-list/directory-3.webp)

The page will reload, and your branch name will now be displayed in the bottom left corner.

### Projects with Deployments on Moonbeam and Moonriver {: #projects-with-deployments }

If a project is deployed to both Moonbeam and Moonriver, there are two different options available:

- Create a separate project structure for each deployment.
- Use a single project structure and modify the project data file for both projects.

Separate project structures should be used if:

- The two deployments have distinct representations in DefiLlama (i.e., two distinct identifiers).
- The project has two different tokens, one native to Moonbeam and one native to Moonriver.

Otherwise, either option may be used.

### Set Up the Folder Structure for Your Project {: #set-up-the-file-structure }

All configurations for each project listed in the DApp Directory are stored in the `projects` folder.

To get started, you must have a name that uniquely and properly identifies your project. Using your project name, you can take the following steps:

1. Create a new directory for your project using your unique project name.
2. In your project directory, you'll need to create:
    1. A project data file is a JSON file that defines all your project data and contains references to the images stored in the `logos` and `screenshots` folders. The list of fields you can use to define your data, with descriptions, is outlined in the next section. The file must be named using your unique project name.
    2. A `logos` folder where your project logo images are stored.
    3. (Optional) A `screenshots` folder where screenshots for the project are stored.

??? code "Example folder structure"

    ```text
    my-project
    ├── my-project.json
    ├── logos
    │   ├── my-project-logo-small.jpeg
    │   └── my-project-logo-full.jpeg
    └── screenshots
        ├── my-project-screenshot1-small.jpeg
        ├── my-project-screenshot1-full.jpeg
        ├── my-project-screenshot2-small.jpeg
        └── my-project-screenshot2-full.jpeg
    ```

![The file structure displayed on GitHub's browser-based editor](/moonbeam-mkdocs/images/learn/dapps-list/directory-4.webp)

With the foundational file structure in place, you're ready to populate the necessary information for your project submission.

### Add Information to the Project Data File {: #add-information }

Your project's data file is where you'll add all the information for your project. The file permits the following top-level properties:

| <div style="width:10vw">Property</div> |                         Type                          |                                                                                                                                                                      Description                                                                                                                                                                       |
|:--------------------------------------:|:-----------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                  `id`                  |                        String                         |                                                                                               Unique identifier for the dApp in the Moonbeam DApp Directory. It should be a unique, human-readable string representing this project. E.g., `my-project`                                                                                                |
|                 `slug`                 |                        String                         |                                                  Identifier used in certain third-party sources. In particular, if the project is listed in DefiLlama, this value should be set to the DefiLlama identifier. See the [Configure the Data Source for TVL](#configure-tvl) section for more information                                                  |
|                 `name`                 |                        String                         |                                                                                                                                      The project name as it will appear in the DApp Directory. E.g., `My Project`                                                                                                                                      |
|               `category`               |                        String                         |                                         The category the project should be associated with. A project can only have one category, and it corresponds to the category list in the left-hand nav of the DApp Directory. See the [Category and Tags](#category-and-tags) section for the accepted list of values                                          |
|             `coinGeckoId`              |                        String                         |                                              If the project has a token listed on CoinGecko, this property should have the **API ID** value corresponding to the given token. See the [Configure the Data Source for Project Token Information](#project-token-information) section for more information                                               |
|                `chains`                |                   Array of Strings                    |                                                                                                               List of Moonbeam ecosystem chains on which the project is deployed. Valid values are currently `moonbeam` and `moonriver`                                                                                                                |
|                 `logo`                 |            Map of Strings to JSON objects             |                                                                                                     Map of logo image files associated with this project and stored in the `logos` directory. See the [Logos](#logos) section for more information                                                                                                     |
|           `shortDescription`           |                        String                         |                                                                                                      A short description of the project used in the display card when browsing dapps in the directory. This should be kept to under 80 characters                                                                                                      |
|             `description`              |                        String                         |                                                                               A longer description used in the project detail page. Markdown or similar formatting cannot be used. Line breaks can be used using `\r\n`. The text should be limited to a few paragraphs                                                                                |
|                 `tags`                 |                   Array of Strings                    |                                                                       A list of applicable [tags](#category-and-tags) for this project. Tag values will show up in the project details. See the [Category and Tags](#category-and-tags) section for the accepted list of values                                                                        |
|              `contracts`               |            Array of contract JSON objects             |                                                     List of contracts for the project. Currently, this is used only for token contracts. The list of smart contracts which make up the protocol is externally sourced from Moonscan. See the [Contracts](#contracts) section for more information                                                      |
|                 `urls`                 |       Map of Strings (names) to Strings (URLs)        |                                                                                                        Mapping of URLs for websites and socials associated with the project. See the [URLs](#urls) section for the accepted list of properties                                                                                                         |
|             `screenshots`              | Array of Maps of Strings (size) to image JSON objects |                                                                                        List of screenshot image files associated with this project and stored in the `screenshots` directory. See the [Screenshots](#screenshots) section for more information                                                                                         |
|         `projectCreationDate`          |                          int                          |                                                                                                                                   The date the project was created. Used for sorting purposes in the DApp Directory                                                                                                                                    |

??? code "Example project data file"

    ```json
    {
        "id": "moonwell",
        "slug": "moonwell",
        "name": "Moonwell",
        "category": "lending",
        "coinGeckoId": "moonwell-artemis",
        "chains": [
            "moonbeam"
        ],
        "logo": {
            "small": {
                "fileName": "moonwell-logo-small.jpeg",
                "width": 40,
                "height": 40,
                "mimeType": "image/jpeg"
            },
            "large": {
                "fileName": "moonwell-logo-large.jpeg",
                "width": 400,
                "height": 400,
                "mimeType": "image/jpeg"
            },
            "full": {
                "fileName": "moonwell-logo-full.jpeg",
                "width": 3000,
                "height": 3000,
                "mimeType": "image/jpeg"
            }
        },
        "shortDescription": "Lending, borrowing, and DeFi protocol built on Moonbeam and Moonriver",
        "description": "Moonwell is an open lending, borrowing, and decentralized finance protocol built on Moonbeam and Moonriver. Moonwell’s composable design can accommodate a full range of DeFi applications in the greater Polkadot and Kusama (DotSama) ecosystem.\r\n\r\nOur first deployment will be on Kusama’s Moonriver, the sister network of Polkadot’s Moonbeam. Moonriver is where new products are expected to be incubated and developed prior to being deployed on Moonbeam.",
        "tags": [
            "Lending",
            "DeFi"
        ],
        "contracts": [
            {
                "contract": "0x511ab53f793683763e5a8829738301368a2411e3",
                "chain": "moonbeam",
                "name": "WELL Token"
            }
        ],
        "urls": {
            "website": "https://moonwell.fi/",
            "try": "https://moonwell.fi/",
            "twitter": "https://twitter.com/MoonwellDeFi",
            "medium": "https://moonwell.medium.com/",
            "telegram": "https://t.me/moonwellfichat",
            "github": "https://github.com/moonwell-open-source",
            "discord": "https://discord.gg/moonwellfi"
        },
        "screenshots": [
            {
                "small": {
                    "fileName": "moonwell-screenshot-small1.png",
                    "width": 429,
                    "height": 200,
                    "mimeType": "image/png"
                },
                "full": {
                    "fileName": "moonwell-screenshot-full1.png",
                    "width": 514,
                    "height": 300,
                    "mimeType": "image/png"
                }
            },
            {
                "small": {
                    "fileName": "moonwell-screenshot-small2.png",
                    "width": 429,
                    "height": 200,
                    "mimeType": "image/png"
                },
                "full": {
                    "fileName": "moonwell-screenshot-full2.png",
                    "width": 1716,
                    "height": 800,
                    "mimeType": "image/png"
                }
            },
            {
                "small": {
                    "fileName": "moonwell-screenshot-small3.png",
                    "width": 429,
                    "height": 200,
                    "mimeType": "image/png"
                },
                "full": {
                    "fileName": "moonwell-screenshot-full3.png",
                    "width": 1054,
                    "height": 637,
                    "mimeType": "image/png"
                }
            },
            {
                "small": {
                    "fileName": "moonwell-screenshot-small4.png",
                    "width": 429,
                    "height": 200,
                    "mimeType": "image/png"
                },
                "full": {
                    "fileName": "moonwell-screenshot-full4.png",
                    "width": 1365,
                    "height": 436,
                    "mimeType": "image/png"
                }
            }
        ],
        "projectCreationDate": 1644828523000
    }
    ```

#### Category and Tags {: #category-and-tags }

A category is the primary classification for a project. A project can be categorized under only one category, but it can have multiple tags. Ensure you carefully select the most applicable category for your project to ensure it is easily found. Any secondary classifications can be included as a tag. 

The currently supported values for `category` are:

```text
- Bridges
- DAO
- DEX
- DeFi
- Gaming
- Lending
- NFTs
- Other
- Social
- Wallets
```

The currently supported values for `tag` are:

```text
- Bridges
- DAO
- DEX
- DeFi
- DePIN
- Developer Tools
- Explorers
- Files
- GLMR Grants
- Gaming
- Infrastructure
- IoT
- Lending
- MOVR Grants
- Messaging
- NFT
- NFT Marketplaces
- On-ramp
- Other
- Social
- Tool
- VPN
- Wallets
- ZeroTrust
```

#### URLs {: #urls }

The `urls` property name/value pairs are used so a project can provide links to their website, socials, etc.

The following table lists the supported `urls` properties:

| Property Name |                                                    Description                                                     |                     Example                     |
|:-------------:|:------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------:|
|   `website`   |                                          The main website for the project                                          |            https://moonbeam.network/            |
|     `try`     | URL a user should visit if they want to try out the dApp. Typically, this page will have a link to launch the dApp |            https://moonbeam.network/            |
|   `twitter`   |                                     The project's X (Twitter) profile                                      |       https://x.com/MoonbeamNetwork       |
|   `medium`    |                                             The project's Medium site                                              |       https://medium.com/moonbeam-network       |
|  `telegram`   |                                               The project's Telegram                                               |         https://t.me/Moonbeam_Official          |
|   `github`    |                                          The project's GitHub repository                                           | https://github.com/moonbeam-foundation/moonbeam |
|   `discord`   |                                               The project's Discord                                                |       https://discord.com/invite/PfpUATX        |

The format of the property name/value pairs should follow the JSON standard, for example:

```json
"urls": {
    "website": "https://moonbeam.network/",
    "try": "https://docs.moonbeam.network/",
    "twitter": "https://x.com/MoonbeamNetwork"
}
```

#### Logos {: #logos }

The `logos` property of the main project data file is a map of image sizes (i.e., `small`, `large`, `full`) to corresponding image JSON objects. The image JSON object contains the display properties for the given image.

The following table lists the properties of the image JSON object:

|  Property  |  Type  |                                                                       Description                                                                        |
|:----------:|:------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------:|
| `fileName` | String |                                         The name of the image file (unqualified) stored in the `logos` directory                                         |
|  `width`   |  int   |                                                          The width of the logo image in pixels                                                           |
|  `height`  |  int   |                                                          The height of the logo image in pixels                                                          |
| `mimeType` | String | The standard [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types) of the file. E.g., `"image/jpeg"` |

Currently, only the `small` size is utilized, and the dimensions for small logos should be 40x40 pixels.

Here is an example showing the structure of the `logo` property that supplies `small` and `full` logos:

```json
"logo": {
    "small": {
        "fileName": "my-project-logo-small.jpeg",
        "width": 40,
        "height": 40,
        "mimeType": "image/jpeg"
    },
    "full": {
        "fileName": "my-project-logo-full.jpeg",
        "width": 3000,
        "height": 3000,
        "mimeType": "image/jpeg"
    }
}
```

#### Screenshots {: #screenshots }

The `screenshots` property of the main project data file is an array of maps. Each map in the array is for a specific screenshot.

However, different-sized images for each screenshot should be supplied so that different sizes can be used in different contexts (e.g., thumbnails vs full-sized images). Thus, for each screenshot, there is a map of image sizes (i.e., `small`, `large`, `full`) to corresponding image JSON objects. The image JSON object contains the display properties for the given image.

The following table lists the properties of the image JSON object:

|  Property  |  Type  |                                                                       Description                                                                        |
|:----------:|:------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------:|
| `fileName` | String |                                      The name of the image file (unqualified) stored in the `screenshots` directory                                      |
|  `width`   |  int   |                                                          The width of the logo image in pixels                                                           |
|  `height`  |  int   |                                                          The height of the logo image in pixels                                                          |
| `mimeType` | String | The standard [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types) of the file. E.g., `"image/jpeg"` |

Here is an example showing the structure of the `screenshot` property for two screenshots (`screenshot1` and `screenshot2`):

```json
"screenshots": [
    {
        "small": {
            "fileName": "my-project-screenshot1-small.png",
            "width": 429,
            "height": 200,
            "mimeType": "image/png"
        },
        "full": {
            "fileName": "my-project-screenshot1-full.png",
            "width": 514,
            "height": 300,
            "mimeType": "image/png"
        }
    },
    {
        "small": {
            "fileName": "my-project-screenshot2-small.png",
            "width": 429,
            "height": 200,
            "mimeType": "image/png"
        },
        "full": {
            "fileName": "my-project-screenshot2-full.png",
            "width": 1716,
            "height": 800,
            "mimeType": "image/png"
        }
    }
]
```

#### Contracts {: #contracts }

A list of contracts for the project. Currently, this is used only for token contracts.

The smart contracts that make up the protocol are sourced from [Moonscan](https://moonscan.io) based on tagging, so they do not need to be listed here. If you have not properly labeled your contracts or are unsure if they are labeled according to the Moonbeam community standard, please refer to the [Configure the Data Source for Active Users and Transaction Volume](#configure-active-users) section.

The following table lists the properties found in the contract JSON object:

|  Property  |  Type  |                                  Description                                  |
|:----------:|:------:|:-----------------------------------------------------------------------------:|
| `contract` | String |                      The address for the smart contract                       |
|  `chain`   | String | The chain on which the contract is deployed (i.e., `moonbeam` or `moonriver`) |
|   `name`   | String |                           The name of the contract                            |

Here is a `contracts` array with a single smart contract for the WGLMR token:

```json
"contracts": [
    {
        "contract": "0xAcc15dC74880C9944775448304B263D191c6077F",
        "chain": "moonbeam",
        "name": "Wrapped GLMR Token"
    }
]
```

### Submit a Pull Request {: #submit-a-pull-request }

After you've populated the project data file and added your logos and screenshots, you should be ready to submit your pull request.

![All of the project files added on GitHub's browser-based editor](/moonbeam-mkdocs/images/learn/dapps-list/directory-5.webp)

From the web-based editor, take the following steps to commit your changes to the `app-directory-data` repository:

1. Click on the **Source Control** tab, which should show you how many pages have been added or changed.
2. Review the files under the **Changes** section. Click the **+** button next to **Changes**, or as you review each file, click the **+** button next to the file name to add them to the list of **Staged Changes**.

![Staging the changed files on GitHub's browser-based editor](/moonbeam-mkdocs/images/learn/dapps-list/directory-6.webp)

All of your files should now be under the **Staged Changes** section. All you have to commit and push the changes are:

1. Enter a descriptive commit message, such as "Add My Project", making sure to use your actual project name.
2. Click **Commit & Push**.

![Committing the staged files on GitHub's browser-based editor](/moonbeam-mkdocs/images/learn/dapps-list/directory-7.webp)

Now that you've committed the changes, you'll need to head over to the [`app-directory-data` repository](https://github.com/moonbeam-foundation/app-directory-data) and open a pull request against the `develop` branch:

1. At the top of the repository page, click **Compare and Pull** button displayed on the banner, or
2. If the banner is not there anymore, you'll need to select your branch from the branches dropdown.
3. Click the **Contribute** dropdown.
4. Click the **Open pull request** button.

![The main page of the app-directory-data repository on GitHub](/moonbeam-mkdocs/images/learn/dapps-list/directory-8.webp)

You'll be taken to the **Comparing changes** page, where you'll need to:

1. Make sure that you are merging your branch into the `develop` branch, which is the **base** branch.
2. Add a title.
3. Add a description of the changes.
4. Click **Create pull request**.

![Submit a pull request on the Comparing changes page of the app-directory-data repository on GitHub](/moonbeam-mkdocs/images/learn/dapps-list/directory-9.webp)

### The Review Process {: #review-process }

Submitted pull requests will be reviewed bi-weekly by the Moonbeam Foundation. During the review, and especially for new projects, the Foundation may have to verify that the GitHub user who created the pull request is a contributor and/or represents the specific project. One way projects can expedite this process is if the submitter's GitHub account is also a major contributor to the project itself on GitHub. Alternatively, teams should leave a note in the pull request comments indicating how we can get in touch with project team members to verify.

A comment will be added to the pull request if any changes are requested. After your pull request has been approved, it will be merged, and your project will be added to the Moonbeam DApp Directory!

## How to Update Your Project Listing {: #how-to-update-your-project-listing }

As your project evolves, you may need to update your project's listing or images related to your listing. You can create a new branch for your changes, find and modify your existing project's data from the root `projects` directory, and make the desired changes.

If you are no longer using a logo or screenshot, please remember to remove it from the `logos` or `screenshots` directory.

Once your changes have been made, you must follow the same instructions in the [Submit a Pull Request](#submit-a-pull-request) section so the changes can be [reviewed](#review-process) by the Moonbeam Foundation. Please note that pull requests are reviewed on a bi-weekly basis, so if the update is urgent, you can create a [forum post](https://forum.moonbeam.network) asking for assistance.

## DApp Directory API {: #dapp-directory-api }

The DApp Directory also features a queryable API that you can use to integrate data from Moonbeam's DApp Directory into your application. The API is public and currently does not require authentication. The base URL for the API is as follows:

```bash
https://apps.moonbeam.network/api/ds/v1/app-dir/
```

### Query a Project {: #query-a-project}

You can retrieve all the information for a particular project by appending `/projects/INSERT_PROJECT_NAME` to the base URL. If you need clarification on the project name, you can omit the project name as shown below to retrieve data for every listed project and find the project in the response. 

```bash
https://apps.moonbeam.network/api/ds/v1/app-dir/projects
```

Here's an example of querying the API for StellaSwap, which returns the project description, social media information, user counts, relevant smart contract addresses, market data, images, and more. 

```bash
https://apps.moonbeam.network/api/ds/v1/app-dir/projects/stellaswap
```

You can visit the query URL directory in the browser, using a tool like Postman, or directly from the command line with Curl as follows: 

```bash
curl -H "Content-Type: application/json" -X GET 'https://apps.moonbeam.network/api/ds/v1/app-dir/projects/stellaswap'
```

??? code "API Response to Querying StellaSwap"

    ```json
    {
        "project":{
            "currentTx":{
                "moonbeam":2883079
            },
            "web3goIDs":[
                "StellaSwap"
            ],
            "name":"StellaSwap",
            "currentTVL":{
                "moonbeam":5046832.23328
            },
            "currentUsers":{
                "moonbeam":52455
            },
            "coinGeckoId":"stellaswap",
            "shortDescription":"The leading DEX and DeFi gateway on Moonbeam",
            "id":"stellaswap",
            "featured":true,
            "tags":[
                "DEX",
                "DeFi"
            ],
            "tvlChange7d":{
                "moonbeam":-1.61482567543498
            },
            "urls":{
                "telegram":"https://t.me/stellaswap",
                "website":"https://stellaswap.com/",
                "try":"https://stellaswap.com/",
                "twitter":"https://twitter.com/StellaSwap",
                "github":"https://github.com/stellaswap",
                "medium":"https://stellaswap.medium.com/"
            },
            "web3goContracts":[
                {
                    "name":"StellaSwap: stDOT Oracle Master",
                    "chain":"moonbeam",
                    "contract":"0x3b23f0675ffc45153eca239664ccaefc5e816b9c"
                },
                {
                    "name":"StellaSwap: stDOT Token",
                    "chain":"moonbeam",
                    "contract":"0xbc7e02c4178a7df7d3e564323a5c359dc96c4db4"
                },
                {
                    "name":"StellaSwap: stDOT Controller",
                    "chain":"moonbeam",
                    "contract":"0x002d34d6a1b4a8e665fec43fd5d923f4d7cd254f"
                },
                {
                    "name":"StellaSwap: stDOT Proxy Admin",
                    "chain":"moonbeam",
                    "contract":"0xe8a5c0039226269313c89c093a6c3524c4d39fa4"
                },
                {
                    "name":"StellaSwap: madUSDC GLMR V2",
                    "chain":"moonbeam",
                    "contract":"0x2ad0e92461df950e2b1c72e2f7a865c81eaa3ce6"
                },
                {
                    "name":"StellaSwap: Dual ETH - GLMR Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0x2ba130297d1966e077c2fb5e4b434e8802925277"
                },
                {
                    "name":"StellaSwap: BCMC Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0x18e75887aa81e113636e18d5a78e3ff93787ec88"
                },
                {
                    "name":"StellaSwap: Pulsar Position Manager V1",
                    "chain":"moonbeam",
                    "contract":"0x1ff2adaa387dd27c22b31086e658108588eda03a"
                },
                {
                    "name":"StellaSwap: DualETH Pool LP Token V1",
                    "chain":"moonbeam",
                    "contract":"0xa3ee3a0a36dc915fdc93062e4b386df37d00217e"
                },
                {
                    "name":"StellaSwap: Interlay Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0x3a7572220afaddc31a72a520642111776d92b2d2"
                },
                {
                    "name":"StellaSwap: Router V1",
                    "chain":"moonbeam",
                    "contract":"0xd0a01ec574d1fc6652edf79cb2f880fd47d34ab1"
                },
                {
                    "name":"StellaSwap: xStella - GLMR Rewarder 2nd V1",
                    "chain":"moonbeam",
                    "contract":"0xb4dba7fe6fcc613963d64204fcf789e9e376679a"
                },
                {
                    "name":"StellaSwap: GLMR Rewarder First V1",
                    "chain":"moonbeam",
                    "contract":"0x69f9d134991e141c4244f397514ba05d67861cc0"
                },
                {
                    "name":"StellaSwap: CELER Rewarder 0 V1",
                    "chain":"moonbeam",
                    "contract":"0xbebd88782a1145b71df3f4986ef7686154ce01d9"
                },
                {
                    "name":"StellaSwap: MATICILO V1",
                    "chain":"moonbeam",
                    "contract":"0xfffa340944ff32f50c7935e2b5d22a7c3393b313"
                },
                {
                    "name":"StellaSwap: ETHmad - GLMR V1",
                    "chain":"moonbeam",
                    "contract":"0x9fe074a56ffa7f4079c6190be6e8452911b7e349"
                },
                {
                    "name":"StellaSwap: STELLA Token",
                    "chain":"moonbeam",
                    "contract":"0x0e358838ce72d5e61e0018a2ffac4bec5f4c88d2"
                },
                {
                    "name":"StellaSwap: SFL - 4pool Wormhole V1",
                    "chain":"moonbeam",
                    "contract":"0xb1bc9f56103175193519ae1540a0a4572b1566f6"
                },
                {
                    "name":"StellaSwap: BICO Trusted Forwarder V1",
                    "chain":"moonbeam",
                    "contract":"0x3d08ce1f9609bb02f47192ff620634d9eb0e7b56"
                },
                {
                    "name":"StellaSwap: Gass Refund V1",
                    "chain":"moonbeam",
                    "contract":"0xee42d4861b56b32776e6fe9a2fe122af0e3f4a33"
                },
                {
                    "name":"StellaSwap: xcDOT - GLMR V1",
                    "chain":"moonbeam",
                    "contract":"0xe76215efea540ea87a2e1a4bf63b1af6942481f3"
                },
                {
                    "name":"StellaSwap: 4pool LP V1",
                    "chain":"moonbeam",
                    "contract":"0xda782836b65edc4e6811c7702c5e21786203ba9d"
                },
                {
                    "name":"StellaSwap: SFL LP V1",
                    "chain":"moonbeam",
                    "contract":"0xa0aa99f71033378864ed6e499eb03612264e319a"
                },
                {
                    "name":"StellaSwap: SFL - 4pool V1",
                    "chain":"moonbeam",
                    "contract":"0x422b5b7a15fb12c518aa29f9def640b4773427f8"
                },
                {
                    "name":"StellaSwap: Acala - GLMR Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0x9de8171bebfa577d6663b594c60841fe096eff97"
                },
                {
                    "name":"StellaSwap: Zap V1",
                    "chain":"moonbeam",
                    "contract":"0x01834cf26717f0351d9762cc9cca7dc059d140df"
                },
                {
                    "name":"StellaSwap: GLMR Rewarder for UST - GLMR V1",
                    "chain":"moonbeam",
                    "contract":"0xc85ddcff71200f9673137e2f93ce504bdbf7db4e"
                },
                {
                    "name":"StellaSwap: xStella Token",
                    "chain":"moonbeam",
                    "contract":"0x06a3b410b681c82417a906993acefb91bab6a080"
                },
                {
                    "name":"StellaSwap: ETHmad - GLMR V2",
                    "chain":"moonbeam",
                    "contract":"0xa6ec79c97e533e7bddb00898e22c6908742e039b"
                },
                {
                    "name":"StellaSwap: WBTC - USDT Contract V1",
                    "chain":"moonbeam",
                    "contract":"0xcae51da6dceacd84f79df4b88d9f92035d1479e9"
                },
                {
                    "name":"StellaSwap: AVAXILO V1",
                    "chain":"moonbeam",
                    "contract":"0x96bef4719ae7c053113292e6aa7fc36e62b243e8"
                },
                {
                    "name":"StellaSwap: Swap For Gas V1",
                    "chain":"moonbeam",
                    "contract":"0xb64dee2d182fed3dd6c273303fb08f11808c9c23"
                },
                {
                    "name":"StellaSwap: Farming Centre V1",
                    "chain":"moonbeam",
                    "contract":"0x0d4f8a55a5b2583189468ca3b0a32d972f90e6e5"
                },
                {
                    "name":"StellaSwap: FTMILO V1",
                    "chain":"moonbeam",
                    "contract":"0x096352f7ea415a336b41fc48b33142eff19a8ad8"
                },
                {
                    "name":"StellaSwap: Acala Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0xb7b5d3659ad213478bc8bfb94d064d0efdda8f7c"
                },
                {
                    "name":"StellaSwap: USDC Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0xa52123adc0bc5c4c030d1ff4f5dad966366a646c"
                },
                {
                    "name":"StellaSwap: Vault V1",
                    "chain":"moonbeam",
                    "contract":"0x54e2d14df9348b3fba7e372328595b9f3ae243fe"
                },
                {
                    "name":"StellaSwap: CELER Rewarder 1 V1",
                    "chain":"moonbeam",
                    "contract":"0x70cbd76ed57393e0cd81e796de850080c775d24f"
                },
                {
                    "name":"StellaSwap: Stella Timelock V1",
                    "chain":"moonbeam",
                    "contract":"0xc6f73b028cd3154a5bb87f49aa43aa259a6522fb"
                },
                {
                    "name":"StellaSwap: GLMR - MAI Vault V1",
                    "chain":"moonbeam",
                    "contract":"0x3a82f4da24f93a32dc3c2a28cfa9d6e63ec28531"
                },
                {
                    "name":"StellaSwap: UST - GLMR V1",
                    "chain":"moonbeam",
                    "contract":"0x556d9c067e7a0534564d55f394be0064993d2d3c"
                },
                {
                    "name":"StellaSwap: SFL - axlUSDC - 4pool V1",
                    "chain":"moonbeam",
                    "contract":"0xa1ffdc79f998e7fa91ba3a6f098b84c9275b0483"
                },
                {
                    "name":"StellaSwap: Stable Router V1",
                    "chain":"moonbeam",
                    "contract":"0xb0dfd6f3fddb219e60fcdc1ea3d04b22f2ffa9cc"
                },
                {
                    "name":"StellaSwap: ATOM - GLMR Rewarder New V1",
                    "chain":"moonbeam",
                    "contract":"0x5aa224966e302424ec13a4f51b80bcfc205984b6"
                },
                {
                    "name":"StellaSwap: CELR Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0x05ad30253f0b20be35d84253d6aca8bd7ec0c66c"
                },
                {
                    "name":"StellaSwap: Router V3",
                    "chain":"moonbeam",
                    "contract":"0xe6d0ed3759709b743707dcfecae39bc180c981fe"
                },
                {
                    "name":"StellaSwap: xStella - GLMR Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0x896135ff51debe8083a2e03f9d44b1d3c77a0324"
                },
                {
                    "name":"StellaSwap: XStella - MAI Vault V1",
                    "chain":"moonbeam",
                    "contract":"0x3756465c5b1c1c4cee473880c9726e20875284f1"
                },
                {
                    "name":"StellaSwap: ATOM - USDC Rewarder New V1",
                    "chain":"moonbeam",
                    "contract":"0x5546e272c67fac10719f1223b1c0212fa3e41a8f"
                },
                {
                    "name":"StellaSwap: SFL - athUSDC - 4pool V1",
                    "chain":"moonbeam",
                    "contract":"0x715d7721fa7e8616ae9d274704af77857779f6f0"
                },
                {
                    "name":"StellaSwap: IDO Locker V1",
                    "chain":"moonbeam",
                    "contract":"0x4b1381b5b959a8ba7f44414c7d758e53d500a8a9"
                },
                {
                    "name":"StellaSwap: Locker V1",
                    "chain":"moonbeam",
                    "contract":"0x8995066b7f1fb3abe3c88040b677d03d607a0b58"
                },
                {
                    "name":"StellaSwap: ATOM - USDC - GLMR Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0xe06e720aaed5f5b817cb3743108ae0a12fe69e9b"
                },
                {
                    "name":"StellaSwap: Mistake in Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0x168ceb7e49c21e3f37820a34590171214a765f5f"
                },
                {
                    "name":"StellaSwap: LP 4pool - Wormhole V1",
                    "chain":"moonbeam",
                    "contract":"0xb326b5189aa42acaa3c649b120f084ed8f4dcaa6"
                },
                {
                    "name":"StellaSwap: Farms V1",
                    "chain":"moonbeam",
                    "contract":"0xedfb330f5fa216c9d2039b99c8ce9da85ea91c1e"
                },
                {
                    "name":"StellaSwap: Factory V1",
                    "chain":"moonbeam",
                    "contract":"0x68a384d826d3678f78bb9fb1533c7e9577dacc0e"
                },
                {
                    "name":"StellaSwap: anyETH-madETH Pool",
                    "chain":"moonbeam",
                    "contract":"0xb86271571c90ad4e0c9776228437340b42623402"
                },
                {
                    "name":"StellaSwap: Dual Farms V2",
                    "chain":"moonbeam",
                    "contract":"0xf3a5454496e26ac57da879bf3285fa85debf0388"
                },
                {
                    "name":"StellaSwap: CELER Rewarder 01 - 02 V1",
                    "chain":"moonbeam",
                    "contract":"0x713f76076283fcd81babe06c76ff51485edf9d5e"
                },
                {
                    "name":"StellaSwap: SCNFT Token",
                    "chain":"moonbeam",
                    "contract":"0x5f23a6a0b6b90fdeeb4816afbfb2ec0408fda59e"
                },
                {
                    "name":"StellaSwap: ATOM - GLMR - GLMR Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0xe60c41de5537418fde05b804df077397dfa84d75"
                },
                {
                    "name":"StellaSwap: Timelock Main V1",
                    "chain":"moonbeam",
                    "contract":"0x9a8693c6f7bf0f44e885118f3f83e2cdb4e611b8"
                },
                {
                    "name":"StellaSwap: MAI - B4P - Wormhole V1",
                    "chain":"moonbeam",
                    "contract":"0xf0a2ae65342f143fc09c83e5f19b706abb37414d"
                },
                {
                    "name":"StellaSwap: LP Token V1",
                    "chain":"moonbeam",
                    "contract":"0x7b17122b941d2173192c7d8d68faabdc88421326"
                },
                {
                    "name":"StellaSwap: Multisig V1",
                    "chain":"moonbeam",
                    "contract":"0x4300e09284e3bb4d9044ddab31efaf5f3301daba"
                },
                {
                    "name":"StellaSwap: Router V2",
                    "chain":"moonbeam",
                    "contract":"0x70085a09d30d6f8c4ecf6ee10120d1847383bb57"
                },
                {
                    "name":"StellaSwap: DOTxc - GLMR V1",
                    "chain":"moonbeam",
                    "contract":"0x505b0a5458dd12605b84bb2928dd2bc5b44993b9"
                },
                {
                    "name":"StellaSwap: SFL - MAI - 4pool V1",
                    "chain":"moonbeam",
                    "contract":"0x7fbe3126c03444d43fc403626ec81e3e809e6b46"
                },
                {
                    "name":"StellaSwap: xStella - USDC Rewarder V1",
                    "chain":"moonbeam",
                    "contract":"0xfa16d5b8bf03677945f0a750c8d2a30001b2fa93"
                },
                {
                    "name":"StellaSwap: madUSDC - GLMR V1",
                    "chain":"moonbeam",
                    "contract":"0x9200cb047a9c4b34a17ccf86334e3f434f948301"
                }
            ],
            "slug":"stellaswap",
            "createdAt":1699292612617,
            "tvlChange1d":{
                "moonbeam":-0.748278690902012
            },
            "logo":{
                "small":{
                    "width":36,
                    "fileName":"stellaswap-logo-small.jpeg",
                    "mimeType":"image/jpeg",
                    "height":36
                },
                "large":{
                    "width":510,
                    "fileName":"stellaswap-logo-large.jpeg",
                    "mimeType":"image/jpeg",
                    "height":510
                },
                "full":{
                    "width":3000,
                    "fileName":"stellaswap-logo-full.jpeg",
                    "mimeType":"image/jpeg",
                    "height":3000
                }
            },
            "chains":[
                "moonbeam"
            ],
            "usersChange7d":{
                "moonbeam":-17.2727272727273
            },
            "marketData":{
                "symbol":"stella",
                "marketCap":808908,
                "marketCapRank":2865,
                "priceChangePercentage1y":-43.01356,
                "currentPrice":0.01729378,
                "priceChangePercentage14d":-17.23772,
                "contracts":{
                    "moonbeam":"0x0e358838ce72d5e61e0018a2ffac4bec5f4c88d2"
                },
                "priceChangePercentage60d":-39.75633,
                "priceChangePercentage30d":-26.13934,
                "priceChangePercentage24h":-4.63782,
                "priceChangePercentage200d":-74.57003,
                "marketCapChangePercentage24h":-4.62971,
                "priceChange24h":-0.0008410608839097,
                "marketCapChange24h":-39268.122562502,
                "priceChangePercentage7d":-7.91278
            },
            "projectCreationDate":1644828523000,
            "contracts":[
                {
                    "chain":"moonbeam",
                    "contract":"0x0e358838ce72d5e61e0018a2ffac4bec5f4c88d2"
                }
            ],
            "updatedAt":1722544694830,
            "category":"dex",
            "description":"StellaSwap is one of the first automated market-making (AMM), decentralized exchange (DEX) for the Moonbeam parachain network. The unique value proposition of StellaSwap is that we're committed in establishing a strong foundation with our native token, STELLA, as a governance token, diverse farms, a built in bridge and user-centered service. \r\n\r\nStellaSwap's main objective is to create a broader range of network effects to address the issues of liquidity in the DeFi space, instead of limiting ourselves to a single solution like many DEXs are doing now. This manifests itself in the diverse product suite of StellaSwap that will be explained in more details. Our products are structured in such a way that facilitates decentralized governance of STELLA holders, while continuing to innovate on the collective foundations by design.",
            "usersChange1d":{
                "moonbeam":-6.18556701030928
            }
        }
    }
    ```

### Query a Category {: #query-a-category}

You can also query the API by [category](#category-and-tags). For example, you can retrieve information about all NFT projects with the following query:

```bash
https://apps.moonbeam.network/api/ds/v1/app-dir/projects?category=nfts
```

??? code "API Response to Querying NFT projects"

    ```json
    {
        "projects":[
            {
                "urls":{
                    "telegram":"https://t.me/nfts2me",
                    "website":"https://nfts2me.com/",
                    "try":"https://nfts2me.com/",
                    "twitter":"https://twitter.com/nfts2me",
                    "medium":"https://nfts2me.medium.com/",
                    "discord":"https://nfts2me.com/discord/"
                },
                "slug":"nfts2me",
                "createdAt":1699292617117,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"nfts2me-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"nfts2me-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"nfts2me-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"NFTs2Me",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1673608509000,
                "shortDescription":"NFTs2Me is a toolkit for creating and managing NFT projects.",
                "contracts":[
                    {
                        "chain":"moonbeam",
                        "contract":"0x2269bCeB3f4e0AA53D2FC43B1B7C5C5D13B119a5"
                    }
                ],
                "updatedAt":1722498896566,
                "category":"nfts",
                "description":"NFTs2Me is a tool for creating and managing NFT projects. It includes features such as an art generator, delayed reveal, minting widget, token gating, and support for multiple blockchain platforms. It also offers customization options, an affiliate system, automatic logo and banner generation, and support for redeemable NFTs. It is user-friendly and suitable for those new to the world of NFTs.\n\nIn addition to these features, NFTs2Me also offers a minting widget and free IPFS hosting to make it simple to mint and store your NFTs securely and efficiently. The minting widget allows you to easily create and mint new NFTs, while the free IPFS hosting provides a secure and decentralized way to store your NFTs.",
                "id":"nfts2me",
                "tags":[
                    "NFT",
                    "Tool"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/rmrkapp",
                    "website":"https://singular.app/",
                    "try":"https://singular.app/",
                    "twitter":"https://twitter.com/RmrkSingular",
                    "discord":"https://discord.gg/TjB6v5AGZz"
                },
                "slug":"singular-app",
                "createdAt":1699292616171,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"singular-app-logo-small.png",
                        "mimeType":"image/png",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"singular-app-logo-large.png",
                        "mimeType":"image/png",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"singular-app-logo-full.png",
                        "mimeType":"image/png",
                        "height":3000
                    }
                },
                "name":"Singular App",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1686240710000,
                "shortDescription":"The home of NFTs by @RmrkApp. Create and trade your nestable, equippable, soulbound, and multi-asset NFTs with us - no coding required.",
                "contracts":[
                    
                ],
                "updatedAt":1722498914806,
                "category":"nfts",
                "description":"Singular is an NFT 2.0 marketplace that allows users to buy, sell, and trade both regular and advanced NFTs. Users can create and/or connect a wallet, browse digital items, and securely conduct transactions using blockchain technology.",
                "id":"singular-app",
                "tags":[
                    "NFT Marketplaces"
                ]
            },
            {
                "urls":{
                    "telegram":"https:/t.me/metacourtgg",
                    "website":"https://www.metacourt.gg/",
                    "try":"https://www.metacourt.gg/",
                    "twitter":"https://twitter.com/metacourtgg",
                    "medium":"https://metacourtgg.medium.com/",
                    "discord":"https://discord.gg/9AnnfKCb39"
                },
                "slug":"metacourt",
                "createdAt":1699292616238,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"metacourt-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"metacourt-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"metacourt-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Metacourt",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1663756794000,
                "shortDescription":"Metacourt created NFTdeals for anyone who wants to become an influencer and trade their social media",
                "contracts":[
                    
                ],
                "updatedAt":1722498888422,
                "category":"nfts",
                "description":"Influencer accelerator for anyone who wants to become an influencer in the space. We allow selling your social media through NFTs and joining influencer marketing campaigns.",
                "id":"metacourt",
                "tags":[
                    "NFT Marketplaces"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/tofuNFT",
                    "website":"https://tofunft.com/",
                    "try":"https://tofunft.com/",
                    "twitter":"https://twitter.com/tofuNFT",
                    "medium":"https://medium.com/tofunftofficial",
                    "discord":"https://discord.com/invite/3wFUTZmTm7"
                },
                "slug":"tofunft",
                "createdAt":1699292615874,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"tofunft-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"tofunft-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"tofunft-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"tofuNFT",
                "chains":[
                    "moonbeam",
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1644828523000,
                "shortDescription":"The largest multichain NFT marketplace",
                "contracts":[
                    
                ],
                "updatedAt":1722498924881,
                "category":"nfts",
                "description":"tofuNFT.com is an NFT marketplace focused on GameFi and collectibles, rebranded from SCV’s NFT market. Enjoy exploring & trading with your buddies!",
                "id":"tofunft",
                "tags":[
                    "NFT Marketplaces",
                    "NFT"
                ]
            },
            {
                "urls":{
                    "website":"https://d-book.io",
                    "try":"https://d-book.io",
                    "twitter":"https://twitter.com/dbook_io"
                },
                "slug":"d-book.io",
                "createdAt":1699292617021,
                "logo":{
                    "small":{
                        "width":129,
                        "fileName":"d-book.io-logo-small.png",
                        "mimeType":"image/png",
                        "height":36
                    },
                    "large":{
                        "width":129,
                        "fileName":"d-book.io-logo-large.png",
                        "mimeType":"image/png",
                        "height":36
                    },
                    "full":{
                        "width":3000,
                        "fileName":"d-book.io-logo-full.png",
                        "mimeType":"image/png",
                        "height":3000
                    }
                },
                "name":"D-book.io",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1682016612000,
                "shortDescription":"Buğra Ayan is a speaker,and university lecturer in Turkey who founded the Web3 Association Turkey.",
                "contracts":[
                    {
                        "chain":"moonbeam",
                        "contract":"0x8d4BA02D0973749ad7c646DcaAa60BDC66F6F6D2"
                    }
                ],
                "updatedAt":1722498866417,
                "category":"nfts",
                "description":"We are an NFT Book Platform that connects authors and the decentralized world, aiming for a transformation ecosystem.",
                "id":"d-book.io",
                "tags":[
                    "NFT Marketplaces",
                    "NFT"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/BcmHuntGroup",
                    "website":"https://bcmhunt.com/",
                    "try":"https://bcmhunt.com/",
                    "twitter":"https://twitter.com/bcmhunt",
                    "medium":"https://medium.com/bcmhunt",
                    "discord":"https://discord.com/invite/Ee9aJ287J2"
                },
                "slug":"blockchain-monster-hunt",
                "createdAt":1699292616780,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"blockchain-monster-hunt-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":510,
                        "fileName":"blockchain-monster-hunt-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":510
                    },
                    "full":{
                        "width":3000,
                        "fileName":"blockchain-monster-hunt-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Blockchain Monster Hunt",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1644828523000,
                "shortDescription":"The First Multichain NFT Monster Hunt",
                "contracts":[
                    
                ],
                "updatedAt":1722498855937,
                "category":"nfts",
                "description":"Blockchain Monster Hunt (BCMH) is the world’s first multi-chain game that runs entirely on the blockchain itself. Inspired by Pokémon-GO,BCMH allows players  to continuously explore brand new places on the blockchain to hunt and battle monsters. Each block on the blockchain is a unique digital space where a limited number of monsters (of the same DNA gene and rarity) may exist.  Players and collectors can hunt or battle for a chance to capture these unique monsters and to earn coins.",
                "id":"blockchain-monster-hunt",
                "tags":[
                    "NFT",
                    "Gaming",
                    "GLMR Grants"
                ]
            },
            {
                "urls":{
                    "website":"https://speedboat.studio/",
                    "try":"https://speedboat.studio/",
                    "twitter":"https://twitter.com/Speedboat_STDO",
                    "medium":"https://medium.com/@speedboat_studio",
                    "discord":"https://discord.gg/y7TQbtEWSV"
                },
                "slug":"speedboat.studio",
                "createdAt":1699292616328,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"speedboat.studio-logo-small.png",
                        "mimeType":"image/png",
                        "height":36
                    },
                    "large":{
                        "width":190,
                        "fileName":"speedboat.studio-logo-large.png",
                        "mimeType":"image/png",
                        "height":190
                    },
                    "full":{
                        "width":3000,
                        "fileName":"speedboat.studio-logo-full.png",
                        "mimeType":"image/png",
                        "height":3000
                    }
                },
                "name":"Speedboat",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1657584952000,
                "shortDescription":"Your no-code Web3 toolkit",
                "contracts":[
                    
                ],
                "updatedAt":1722498916466,
                "category":"nfts",
                "description":"Speedboat is a Web3 toolkit for everyone. Built on the idea that NFTs are not just expensive JPEGs, but programmable experiences.",
                "id":"speedboat.studio",
                "tags":[
                    "NFT",
                    "Tool"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/+qGh0InPSPc1iMTNk",
                    "website":"https://www.glmrapes.com/",
                    "try":"https://www.glmrapes.com/",
                    "twitter":"https://twitter.com/GLMRApes",
                    "discord":"https://discord.com/invite/glmrapes"
                },
                "web3goContracts":[
                    {
                        "name":"GLMR Apes: GLMR Ape",
                        "chain":"moonbeam",
                        "contract":"0x8fbe243d898e7c88a6724bb9eb13d746614d23d6"
                    },
                    {
                        "name":"GLMR Apes: GLMR Jungle",
                        "chain":"moonbeam",
                        "contract":"0xcb13945ca8104f813992e4315f8ffefe64ac49ca"
                    }
                ],
                "currentTx":{
                    "moonbeam":7830
                },
                "slug":"glmr-apes",
                "web3goIDs":[
                    "GLMR Apes"
                ],
                "createdAt":1699292616827,
                "logo":{
                    "small":{
                        "width":47,
                        "fileName":"glmr-apes-logo-small.png",
                        "mimeType":"image/png",
                        "height":36
                    },
                    "large":{
                        "width":528,
                        "fileName":"glmr-apes-logo-large.png",
                        "mimeType":"image/png",
                        "height":408
                    },
                    "full":{
                        "width":3000,
                        "fileName":"glmr-apes-logo-full.png",
                        "mimeType":"image/png",
                        "height":3000
                    }
                },
                "name":"GLMR APES",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "usersChange7d":{
                    "moonbeam":-66.6666666666667
                },
                "currentUsers":{
                    "moonbeam":1531
                },
                "projectCreationDate":1644828523000,
                "shortDescription":"The first NFT collection on GLMR by & for the community",
                "contracts":[
                    
                ],
                "updatedAt":1722547408370,
                "category":"nfts",
                "description":"GLIMMER APES is the first NFT collection on GLMR by & for the community. The longer you’re bonding with GLMR Apes and the friendlier their behavior. Join the troops as soon as possible to become an EARLY APE, take part in our giveaways and games and land in the GLMR APE VIP CLUB.",
                "id":"glmr-apes",
                "tags":[
                    "NFT",
                    "Gaming"
                ],
                "usersChange1d":{
                    "moonbeam":0
                }
            },
            {
                "urls":{
                    "website":"https://snakesoldiers.com",
                    "try":"https://snakesoldiers.com",
                    "twitter":"https://twitter.com/snakesoldiers",
                    "github":"https://github.com/steven2308/snake-soldiers-contracts",
                    "medium":"https://medium.com/@snakesoldiers/emoting-to-influence-the-hatch-df3eab7e45b8",
                    "discord":"http://discord.gg/A6zQSz4YU4"
                },
                "slug":"snake-soldiers",
                "createdAt":1699292616971,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"snake-soldiers-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"snake-soldiers-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"snake-soldiers-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Snake Soldiers",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1691439275000,
                "shortDescription":"NFT game collection divided in 3 categories: Generals, Commanders and Soldiers🐍. Built on Moonbeam",
                "contracts":[
                    {
                        "chain":"moonbeam",
                        "contract":"0x3ab955216BdD76f51fbe02A3fe237D6612BBD09F"
                    }
                ],
                "updatedAt":1722498915320,
                "category":"nfts",
                "description":"Snake Soldiers is an NFT collection with a supply of at most 5k units, all unique and distributed among 3 ranks. Each snake will be usable inside a play to own game, where snakes will be the main characters, necessary to interact with the SerpenTerra ecosystem. This metaverse will be based on the RMRK 2.0 standard, making forward compatible and giving super powers to the NFTs.",
                "id":"snake-soldiers",
                "tags":[
                    "NFT"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/+LqmDOeGUQdRmYjVh%60%60",
                    "website":"https://omni-x.io",
                    "try":"https://omni-x.io",
                    "twitter":"https://twitter.com/omnix_nft",
                    "github":"https://github.com/Omni-X-NFT",
                    "discord":"https://discord.gg/omni-x"
                },
                "slug":"omni-x",
                "createdAt":1699292617077,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"omni-x-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":107,
                        "fileName":"omni-x-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":108
                    },
                    "full":{
                        "width":3000,
                        "fileName":"omni-x-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Omni-X",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1673811786000,
                "shortDescription":"The first natively omnichain NFT platform",
                "contracts":[
                    
                ],
                "updatedAt":1722498898538,
                "category":"nfts",
                "description":"Omni X is an omnichain NFT protocol and marketplace that connects communities, creators, and enthusiasts across multiple blockchains. \n\nWe provide tooling for creating ONFT collections, bridging regular NFTs to ONFTs and grant access to unparalleled liquidity that allows users to buy and sell NFTs from any blockchain to any other blockchain.",
                "id":"omni-x",
                "tags":[
                    "NFT Marketplaces",
                    "Infrastructure"
                ]
            },
            {
                "urls":{
                    "website":"https://www.publicpressure.io/",
                    "try":"https://www.publicpressure.io/",
                    "twitter":"https://twitter.com/jointhepressure",
                    "discord":"https://discord.gg/publicpressure"
                },
                "slug":"publicpressure",
                "createdAt":1702283744356,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"publicpressure-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"publicpressure-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"publicpressure-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Public Pressure",
                "chains":[
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1651597275000,
                "shortDescription":"Support your favorite artists, own their music, get rewarded.",
                "contracts":[
                    
                ],
                "updatedAt":1722498907699,
                "category":"nfts",
                "description":"We are the web3 music platform powered by artists, labels and fans",
                "id":"publicpressure",
                "tags":[
                    "NFT Marketplaces"
                ]
            },
            {
                "currentTx":{
                    "moonbeam":8409
                },
                "web3goIDs":[
                    "Moonbeans"
                ],
                "name":"Moonbeans",
                "currentUsers":{
                    "moonbeam":1134
                },
                "coinGeckoId":"moonbeans",
                "shortDescription":"Galactic Co-Op & Profit sharing NFT platform and soon to be Metaverse",
                "id":"moonbeans",
                "tags":[
                    "NFT Marketplaces"
                ],
                "urls":{
                    "website":"https://moonbeans.io/",
                    "twitter":"https://twitter.com/moonbeansio",
                    "github":"https://github.com/m00nbeans",
                    "discord":"https://discord.com/invite/qqE9aBPzQ9",
                    "telegram":"https://t.me/moonbeansio",
                    "try":"https://moonbeans.io/",
                    "medium":"https://medium.com/@MoonBeans"
                },
                "web3goContracts":[
                    {
                        "name":"Moonbeans: Beanie Distributor V2",
                        "chain":"moonbeam",
                        "contract":"0xda6367c6510d8f2d20a345888f9dff3eb3226b02"
                    },
                    {
                        "name":"Moonbeans: Marketplace V9",
                        "chain":"moonbeam",
                        "contract":"0x683724817a7d526d6256aec0d6f8ddf541b924de"
                    },
                    {
                        "name":"Moonbeans: Storefront Ownership V1",
                        "chain":"moonbeam",
                        "contract":"0x971dfedd548f2269e515957404cbbee1f507cd01"
                    }
                ],
                "slug":"moonbeans",
                "createdAt":1699292615978,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"moonbeans-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"moonbeans-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"moonbeans-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "chains":[
                    "moonbeam",
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "usersChange7d":{
                    "moonbeam":0
                },
                "marketData":{
                    "symbol":"beans",
                    "marketCap":0,
                    "priceChangePercentage1y":-62.22489,
                    "currentPrice":0.062264,
                    "priceChangePercentage14d":-13.93552,
                    "contracts":{
                        
                    },
                    "priceChangePercentage60d":-44.93764,
                    "priceChangePercentage30d":-33.587,
                    "priceChangePercentage24h":-0.05451,
                    "priceChangePercentage200d":-83.0363,
                    "marketCapChangePercentage24h":0,
                    "priceChange24h":-0.0000339560550113,
                    "marketCapChange24h":0,
                    "priceChangePercentage7d":-5.36696
                },
                "projectCreationDate":1644828523000,
                "contracts":[
                    {
                        "chain":"moonbeam",
                        "contract":"0x65b09ef8c5a096c5fd3a80f1f7369e56eb932412"
                    },
                    {
                        "chain":"moonriver",
                        "contract":"0xC2392DD3e3fED2c8Ed9f7f0bDf6026fcd1348453"
                    }
                ],
                "updatedAt":1722548296818,
                "category":"nfts",
                "description":"Moonbeans is an NFT marketplace launched on October 8, 2021, featuring 465 Beanies on the Moonriver network. The platform offers NFT trading with fees for artists, traders, and project developers. Multiple collections are available, including Beanies and RivrMaids.",
                "usersChange1d":{
                    "moonbeam":0
                }
            },
            {
                "urls":{
                    "telegram":"https://t.me/blocsport",
                    "website":"https://blocsport.one/",
                    "try":"https://blocsport.one/",
                    "twitter":"https://twitter.com/blocsport1",
                    "medium":"https://blocsport1.medium.com/"
                },
                "slug":"blocsport-one",
                "createdAt":1699292616637,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"blocsport-one-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"blocsport-one-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"blocsport-one-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Blocsport.one",
                "chains":[
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1644828523000,
                "shortDescription":"Web 3.0 metaverse, smart sports money, athlete NFT launchpad & assets tokenization",
                "contracts":[
                    
                ],
                "updatedAt":1722498857332,
                "category":"nfts",
                "description":"Blocsport.one is a Swiss sports tech company founded in 2019 that is transforming the sports business by building a transparent and reliable sports ecosystem uniting athletes, clubs, and fans based on blockchain. Company owns NFTdeals.io exclusive marketplace and has the biometric-enabled football scouting DApp live. Blocsport.one helps the young promising athletes get the money and exposure for their career development, which is nobody else doing in the world.",
                "id":"blocsport-one",
                "tags":[
                    "NFT"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/mintverse",
                    "website":"https://www.mintverse.com/",
                    "try":"https://www.mintverse.com/",
                    "twitter":"https://twitter.com/mintverse_",
                    "medium":"https://medium.com/mintverse",
                    "discord":"https://discord.com/invite/mhhnbvAaq9"
                },
                "slug":"mintverse",
                "createdAt":1702283733666,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"mintverse-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"mintverse-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"mintverse-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Mintverse",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1651597514000,
                "shortDescription":"Mint, Explore & Trade Liquid NFT Assets Across Multiple Chains",
                "contracts":[
                    
                ],
                "updatedAt":1722498889300,
                "category":"nfts",
                "description":"Comprehensive NFT Aggregation Marketplace with a 0% trading fee",
                "id":"mintverse",
                "tags":[
                    "NFT Marketplaces"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/rmrkapp",
                    "website":"https://upgradooor.app",
                    "try":"https://upgradooor.app",
                    "twitter":"https://x.com/rmrkapp",
                    "github":"https://github.com/rmrk-team",
                    "medium":"https://medium.com/rmrkapp"
                },
                "slug":"upgradooor",
                "createdAt":1699292616895,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"upgradooor-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"upgradooor-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"upgradooor-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Upgradooor",
                "chains":[
                    "moonbeam",
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1692259742000,
                "shortDescription":"Upgrade your NFT 1.0 collections to NFT 2.0 by wrapping them into advanced functionality",
                "contracts":[
                    
                ],
                "updatedAt":1722498927244,
                "category":"nfts",
                "description":"As a collection issuer, use Upgradooor to initialize the process of upgrading your collection to NFT 2.0 if you are currently using ERC721.\n\nAs a holder, once the collection owner initiates the process, you can wrap any NFT you hold in that collection and instantly turn it into an equippable, multi-asset, composable NFT with no added risk.\n\nYou can always unwrap at will, and all the changes will still wait for you when you decide to re-claim the 2.0 wrapper again.\n\nUpgrading allows you to:\n\n- add more assets (outputs) to a legacy NFT, preventing needless airdrop spam\n- airdrop NFTs into the NFT itself, preventing detachment of context, and saving tremendous amounts of gas by letting people transfer just the parent NFT\n- define equippable settings and even achieve compatibility with other collections, for cross collection equippables and thus cross collection royalties and commissions\n- see your NFTs on Singular, and use GBM auctions as a unique and novel listing mechanic",
                "id":"upgradooor",
                "tags":[
                    "NFT",
                    "Tool"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/moonfit_official_community",
                    "website":"https://moonfit.xyz/",
                    "try":"https://moonfit.xyz/",
                    "twitter":"https://twitter.com/MoonFitOfficial",
                    "discord":"https://discord.gg/hStdUVtHXp"
                },
                "slug":"moonfit",
                "createdAt":1702283734897,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"moonfit-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"moonfit-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"moonfit-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"MoonFit",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1654692249000,
                "shortDescription":"Web3 & NFT Lifestyle App That Pays You Anytime You Burn Calories",
                "contracts":[
                    
                ],
                "updatedAt":1722498891201,
                "category":"nfts",
                "description":"MoonFit is a Web3 Lifestyle App that promotes active living by rewarding users with tokens and NFTs anytime they burn calories through physical activities.",
                "id":"moonfit",
                "tags":[
                    "NFT",
                    "Gaming"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/rmrkapp",
                    "website":"https://rmrk.app/",
                    "try":"https://rmrk.app/",
                    "twitter":"https://twitter.com/rmrkapp",
                    "discord":"https://discord.com/invite/bV9kQbVC99"
                },
                "slug":"rmrk",
                "createdAt":1699292615938,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"rmrk-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"rmrk-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"rmrk-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"RMRK",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "marketData":{
                    "symbol":"rmrk",
                    "marketCap":5985029,
                    "marketCapRank":1602,
                    "priceChangePercentage1y":-64.99216,
                    "currentPrice":0.62974,
                    "priceChangePercentage14d":-24.26661,
                    "contracts":{
                        "moonbeam":"0x524d524b4c9366be706d3a90dcf70076ca037ae3"
                    },
                    "priceChangePercentage60d":-51.72181,
                    "priceChangePercentage30d":-30.11256,
                    "priceChangePercentage24h":-2.58554,
                    "priceChangePercentage200d":-75.55551,
                    "marketCapChangePercentage24h":-2.50147,
                    "priceChange24h":-0.01671434617594,
                    "marketCapChange24h":-153554.8536219,
                    "priceChangePercentage7d":-1.5052
                },
                "coinGeckoId":"rmrk",
                "projectCreationDate":1644828523000,
                "shortDescription":"Creators of NFTs 2.0 via ERC6059, ERC6220, ERC5773, EIP6381, and EIP6454.\nNFT equippables, future compatibility, reputation, and token balances.",
                "contracts":[
                    
                ],
                "updatedAt":1722548302467,
                "category":"nfts",
                "description":"With the RMRK NFT Building Block System\nOur ERC NFT standards allow you to unlock the true potential of NFTs.\nTailored to work with each other, these EVM smart contracts will help you create your NFT projects of varying complexity.",
                "id":"rmrk",
                "tags":[
                    "NFT",
                    "Infrastructure"
                ]
            },
            {
                "urls":{
                    "website":"https://www.mynft.com/",
                    "try":"https://bridge.mynft.com/home",
                    "twitter":"https://twitter.com/mynft"
                },
                "slug":"mynft",
                "createdAt":1699292616578,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"mynft-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"mynft-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"mynft-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"myNFT",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1644828523000,
                "shortDescription":"The marketplace that puts the power back in your hands",
                "contracts":[
                    
                ],
                "updatedAt":1722498895020,
                "category":"nfts",
                "description":"myNFT is the marketplace that puts the power back in your hands. It is a creative workshop, a trading platform and a discovery engine, helping you tell your story and share your passions, on your own terms. myNFT is built on decentralized technologies empowering you to create, trade, and discover. myNFT is built by Perpetual Altruism, a leader in the NFT space and the creator of charitable NFT publisher Cryptograph and the GBM auction system. Perpetual Altruism is backed by prominent investors and creators and is also the recipient of grants from the Web3 Foundation and the Moonbeam network for their work on the decentralized internet, which powers myNFT.",
                "id":"mynft",
                "tags":[
                    "NFT Marketplaces",
                    "GLMR Grants",
                    "MOVR Grants"
                ]
            },
            {
                "urls":{
                    "website":"https://readl.co/",
                    "try":"https://readl.co/",
                    "twitter":"https://twitter.com/readl_co",
                    "medium":"https://medium.com/@readlnetwork",
                    "discord":"https://discord.gg/XPTENepHqY"
                },
                "slug":"readl",
                "createdAt":1702283745749,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"readl-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"readl-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"readl-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Readl",
                "chains":[
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1655885161000,
                "shortDescription":"Bringing the publishing industry to web3",
                "contracts":[
                    
                ],
                "updatedAt":1722498910044,
                "category":"nfts",
                "description":"Readl is the protocol that provides publishers and storytellers with the infrastructure to publish their content on the blockchain, while providing a user-friendly platform to enjoy any story, in any format.",
                "id":"readl",
                "tags":[
                    "NFT Marketplaces",
                    "MOVR Grants"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/rmrkapp",
                    "website":"https://emotes.app",
                    "try":"https://emotes.app",
                    "twitter":"https://x.com/rmrkapp",
                    "github":"https://github.com/rmrk-team",
                    "medium":"https://medium.com/rmrkapp"
                },
                "slug":"emotes.app",
                "createdAt":1699292616951,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"emotes.app-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"emotes.app-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"emotes.app-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Emotes.app",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1692254489000,
                "shortDescription":"React on anyone's NFT - throw 💩 at those apes, give a 🤗 to those Pudgies!",
                "contracts":[
                    
                ],
                "updatedAt":1722498871347,
                "category":"nfts",
                "description":"Emotes.app is a RMRK mini-app which allows you to send emotes / reactions to anyone's NFT. It utilizes RMRK's ERC7009 and is trivial to integrate into any project wanting to take advantage of the community's reactions to their NFTs.\n\nUse it to direct storylines, affect NFT egg hatching, or just do relative price comparison when influencers like one NFTs and dislike another!",
                "id":"emotes.app",
                "tags":[
                    "NFT",
                    "Social"
                ]
            },
            {
                "urls":{
                    "telegram":"https://twitter.com/PolkaPets",
                    "website":"https://www.polkapet.world/",
                    "try":"https://www.polkapet.world/",
                    "twitter":"https://twitter.com/PolkaPets",
                    "medium":"https://polkapetworld.medium.com/"
                },
                "slug":"polkapet-world",
                "createdAt":1702283743596,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"polkapet-world-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"polkapet-world-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"polkapet-world-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"PolkaPets",
                "chains":[
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "marketData":{
                    "priceChangePercentage60d":1206.42918,
                    "symbol":"pets",
                    "marketCap":0,
                    "priceChangePercentage30d":619.39533,
                    "priceChangePercentage200d":135.91624,
                    "priceChangePercentage1y":355.00061,
                    "currentPrice":0.00515699,
                    "priceChangePercentage14d":-15.30948,
                    "contracts":{
                        "moonriver":"0x1e0f2a75be02c025bd84177765f89200c04337da"
                    },
                    "priceChangePercentage7d":749.62625
                },
                "coinGeckoId":"polkapet-world",
                "projectCreationDate":1651157216000,
                "shortDescription":"Welcome to PolkaPet World",
                "contracts":[
                    
                ],
                "updatedAt":1722548303208,
                "category":"nfts",
                "description":"An immersive NFT collection created in partnership with the biggest and best PolkaDot projects ",
                "id":"polkapet-world",
                "tags":[
                    "NFT"
                ]
            },
            {
                "urls":{
                    "website":"https://www.moonarines.com/",
                    "try":"https://www.moonarines.com/",
                    "discord":"https://discord.gg/bXhSyW8htW"
                },
                "slug":"moonarines",
                "createdAt":1702283733870,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"moonarines-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"moonarines-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"moonarines-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Moonarines",
                "chains":[
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1654792422000,
                "shortDescription":"Be part of the conquest of the digital space",
                "contracts":[
                    
                ],
                "updatedAt":1722498889804,
                "category":"nfts",
                "description":"The Moonarines are unique NFT characters starting soon on the Moonriver Network!\nWith the Moonarines, the NFT owners will be taken to an unforgettable adventure to explore the Cryptoverse!",
                "id":"moonarines",
                "tags":[
                    "NFT"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/NFTrade",
                    "website":"https://nftrade.com/",
                    "try":"https://nftrade.com/",
                    "twitter":"https://twitter.com/NFTradeOfficial",
                    "medium":"https://medium.com/@NFTrade",
                    "discord":"https://discord.com/invite/SESqfsyw8k"
                },
                "slug":"nftrade",
                "createdAt":1699292616005,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"nftrade-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"nftrade-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"nftrade-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"NFTrade",
                "chains":[
                    "moonbeam",
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "marketData":{
                    "symbol":"nftd",
                    "marketCap":234018,
                    "marketCapRank":3653,
                    "priceChangePercentage1y":-65.38449,
                    "currentPrice":0.00502075,
                    "priceChangePercentage14d":-7.09922,
                    "contracts":{
                        
                    },
                    "priceChangePercentage60d":-27.37596,
                    "priceChangePercentage30d":-14.12267,
                    "priceChangePercentage24h":-2.22137,
                    "priceChangePercentage200d":-56.66993,
                    "marketCapChangePercentage24h":-2.16658,
                    "priceChange24h":-0.00011406326237191,
                    "marketCapChange24h":-5182.473845666,
                    "priceChangePercentage7d":-6.88049
                },
                "coinGeckoId":"nftrade",
                "projectCreationDate":1644828523000,
                "shortDescription":"Create, Buy, Sell, Swap and Farm NFTs",
                "contracts":[
                    
                ],
                "updatedAt":1722548304198,
                "category":"nfts",
                "description":"NFTrade is a multi-chain platform for NFT creation and trading. Seamlessly launch, mint, and swap non-fungible tokens. Earn digital collectibles. NFTrade places you at the heart of the NFT economy. Create, Buy, Sell, Swap and Farm NFTs. All chains, All NFTs, One Platform.",
                "id":"nftrade",
                "tags":[
                    "NFT Marketplaces",
                    "MOVR Grants"
                ]
            },
            {
                "urls":{
                    "website":"https://www.pipcards.com/",
                    "try":"https://www.pipcards.com/",
                    "twitter":"https://twitter.com/pipcards",
                    "discord":"https://discord.com/invite/hnSC7QjTHj"
                },
                "slug":"pipcards",
                "createdAt":1699292616371,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"pipcards-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"pipcards-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"pipcards-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"PIP Cards",
                "chains":[
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1651149583000,
                "shortDescription":"Post-generated NFT playing card decks",
                "contracts":[
                    
                ],
                "updatedAt":1722498904704,
                "category":"nfts",
                "description":"PIPS is a first-of-its-kind NFT generative playing card project that will enable NFT holders to generate an entire deck of custom cards to be used cross-chain.",
                "id":"pipcards",
                "tags":[
                    "NFT",
                    "Gaming"
                ]
            },
            {
                "urls":{
                    "website":"https://bithotel.io/",
                    "twitter":"https://twitter.com/playbithotel",
                    "github":"https://github.com/BitHotelOrg/bithotel-token-contracts",
                    "discord":"https://discord.gg/RFFZNwxY9n",
                    "telegram":"https://t.me/bithotelcommunity",
                    "try":"https://bithotel.io/",
                    "medium":"https://medium.com/@bithotelnftgame"
                },
                "slug":"bit-hotel",
                "createdAt":1702283710425,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"bit-hotel-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":500,
                        "fileName":"bit-hotel-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":500
                    },
                    "full":{
                        "width":3000,
                        "fileName":"bit-hotel-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Bit Hotel",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1658743551000,
                "shortDescription":"Bit Hotel is a Social-first Play 2 Earn NFT Gaming Metaverse set in a Pixel-art Hotel.",
                "contracts":[
                    {
                        "chain":"moonbeam",
                        "contract":"Not deployed yet"
                    },
                    {
                        "chain":"moonriver",
                        "contract":"Not deployed yet"
                    }
                ],
                "updatedAt":1722498854706,
                "category":"nfts",
                "description":"In Bit Hotel users can compete to earn Bit Hotel tokens and acquire native NFTs. These NFTs have in-game utilities and consist of characters, hotel rooms, furniture and other assets that have their own unique perks. With over 250k Hotel Guests cross-channel, this nostalgic Hotel metaverse is taking people back to their 8bit upbringing.",
                "id":"bit-hotel",
                "tags":[
                    "NFT",
                    "Gaming"
                ]
            },
            {
                "tvlChange7d":{
                    "moonriver":0.00190215150271202
                },
                "urls":{
                    "website":"https://www.moonbeamdao.com/",
                    "try":"https://www.moonbeamdao.com/",
                    "twitter":"https://twitter.com/moonbeam_dao",
                    "medium":"https://medium.com/@moonbeamdao",
                    "discord":"https://discord.gg/AevrFzwZjk"
                },
                "web3goContracts":[
                    {
                        "name":"MoonDAO: MDAO Token",
                        "chain":"moonbeam",
                        "contract":"0xc6342eab8b7cc405fc35eba7f7401fc400ac0709"
                    }
                ],
                "currentTx":{
                    "moonbeam":972
                },
                "slug":"moondao",
                "web3goIDs":[
                    "MoonDAO"
                ],
                "createdAt":1699292616416,
                "tvlChange1d":{
                    "moonriver":-0.0349944884006391
                },
                "logo":{
                    "small":{
                        "width":25,
                        "fileName":"moondao-logo-small.png",
                        "mimeType":"image/png",
                        "height":36
                    },
                    "large":{
                        "width":330,
                        "fileName":"moondao-logo-large.png",
                        "mimeType":"image/png",
                        "height":475
                    },
                    "full":{
                        "width":3000,
                        "fileName":"moondao-logo-full.png",
                        "mimeType":"image/png",
                        "height":3000
                    }
                },
                "name":"MoonDAO",
                "chains":[
                    "moonbeam"
                ],
                "currentTVL":{
                    "moonriver":76.75665
                },
                "currentUsers":{
                    "moonbeam":229
                },
                "projectCreationDate":1648347145000,
                "shortDescription":"The first & only community art dao on moonbeam",
                "contracts":[
                    
                ],
                "updatedAt":1722547637377,
                "category":"nfts",
                "description":"MoonDao is the first community Art Collection DAO on the Moonbeam network!\n\nWe aim to utilize input from our community to select high-end NFT’s. These NFT’s will be acquired with the MoonDao treasury and stored in the MoonDao Vault.\n\nMoon ownership grants access to DAO voting rights, future events, and additional holder perks outlined below. Welcome to the moon, we hope you stay.\n\n",
                "id":"moondao",
                "tags":[
                    "NFT",
                    "DAO"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/raresama",
                    "website":"https://raresama.com/",
                    "try":"https://raresama.com/",
                    "twitter":"https://twitter.com/RaresamaNFT",
                    "discord":"https://discord.com/channels/938592318380982303/1010237900685840405"
                },
                "slug":"raresama",
                "createdAt":1699292615958,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"raresama-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"raresama-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"raresama-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Raresama",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1662528828000,
                "shortDescription":"Discover amazing Rare digital artwork",
                "contracts":[
                    
                ],
                "updatedAt":1722498909462,
                "category":"nfts",
                "description":"Raresama brings the magic of owning a piece of artwork to your fingertips. Create or browse NFT art collections and enjoy a diverse mix of artists, genres, styles and movements.",
                "id":"raresama",
                "tags":[
                    "NFT Marketplaces"
                ]
            },
            {
                "urls":{
                    "telegram":"https://gal.xyz/telegram",
                    "website":"https://galxe.com/",
                    "try":"https://galxe.com/",
                    "twitter":"https://twitter.com/Galxe",
                    "medium":"https://blog.galxe.com/",
                    "discord":"https://gal.xyz/discord"
                },
                "slug":"galxe",
                "createdAt":1699292616277,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"galxe-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"galxe-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"galxe-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Galxe",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1659868871000,
                "shortDescription":"Create Impactful Experiences With #Web3 Credentials. (Formerly Project Galaxy) ",
                "contracts":[
                    
                ],
                "updatedAt":1722498876438,
                "category":"nfts",
                "description":"Galxe is the leading Web3 credential data network in the world. A collaborative credential infrastructure enabling brands and developers to engage communities and build robust products in Web3.",
                "id":"galxe",
                "tags":[
                    "NFT",
                    "Social",
                    "Tool"
                ]
            },
            {
                "urls":{
                    "telegram":"http://t.me/MoonsamaNFT",
                    "website":"https://moonsama.com/",
                    "try":"https://moonsama.com/",
                    "twitter":"https://twitter.com/MoonsamaNFT",
                    "discord":"discord.gg/moonsama"
                },
                "slug":"moonsama",
                "createdAt":1702283735408,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"moonsama-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"moonsama-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"moonsama-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Moonsama",
                "chains":[
                    "moonriver",
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1651156798000,
                "shortDescription":"Let's build the multiverse",
                "contracts":[
                    
                ],
                "updatedAt":1722498892389,
                "category":"nfts",
                "description":"Moonsama’s protocol for bi-directional bridging of on-chain digital assets and off-chain applications. This is how we connect web2.0 games, metaverses and blockchains. It enables new games, development and community fun from across the Kusamaverse and beyond!",
                "id":"moonsama",
                "tags":[
                    "NFT",
                    "Gaming"
                ]
            },
            {
                "urls":{
                    "website":"https://smartstamp.com/",
                    "try":"https://smartstamp.com/",
                    "discord":"https://discord.gg/kajPqvZY"
                },
                "slug":"smartstamp",
                "createdAt":1699292617058,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"smartstamp-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":436,
                        "fileName":"smartstamp-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":436
                    },
                    "full":{
                        "width":3000,
                        "fileName":"smartstamp-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"SmartStamp",
                "chains":[
                    "moonbeam",
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1675081766000,
                "shortDescription":"SmartStamp is the pioneering new standard in identification and authentication for the art world.",
                "contracts":[
                    
                ],
                "updatedAt":1722498915044,
                "category":"nfts",
                "description":"Developed over more than a decade, SmartStamp’s app uses patented AI technology that is designed to read and record artworks’ surface characteristics– offering artists, collectors, institutions, and all arts and culture stakeholders a way to securely and immutably link physical objects to their digital fingerprints on the blockchain. Using the SmartStamp app is as simple as taking a picture, making the groundbreaking security and timestamping power of blockchain technology accessible to anyone who can use a smartphone.",
                "id":"smartstamp",
                "tags":[
                    "NFT"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/yusernetwork",
                    "website":"https://yuser.network/",
                    "try":"https://yuser.network/",
                    "twitter":"https://twitter.com/yuser",
                    "medium":"https://medium.com/yuser",
                    "discord":"https://discord.com/invite/uRRxnfAjhY"
                },
                "slug":"yuser",
                "createdAt":1699292616605,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"yuser-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"yuser-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"yuser-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Yuser",
                "chains":[
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1644828523000,
                "shortDescription":"The first NFT social networking app- by creators, for creators",
                "contracts":[
                    
                ],
                "updatedAt":1722498932483,
                "category":"nfts",
                "description":"Yuser’s mission is to build an ecosystem of interconnected applications that put power back into the hands of users by giving them full control over their content, data, and personal networks. Developers can connect via an API to instantly gain access to millions of users and incentivize them to try their product by paying them with a token.",
                "id":"yuser",
                "tags":[
                    "NFT Marketplaces",
                    "GLMR Grants",
                    "MOVR Grants"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/cryptosoots",
                    "website":"https://raregems.io/my#",
                    "try":"https://raregems.io/my#",
                    "twitter":"https://twitter.com/RareGems_io"
                },
                "slug":"rare-gems",
                "createdAt":1702283745336,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"rare-gems-logo-small.png",
                        "mimeType":"image/png",
                        "height":36
                    },
                    "large":{
                        "width":360,
                        "fileName":"rare-gems-logo-large.png",
                        "mimeType":"image/png",
                        "height":360
                    },
                    "full":{
                        "width":3000,
                        "fileName":"rare-gems-logo-full.png",
                        "mimeType":"image/png",
                        "height":3000
                    }
                },
                "name":"Rare Gems",
                "chains":[
                    "moonriver",
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1652705611000,
                "shortDescription":"Multichain NFT marketplace.",
                "contracts":[
                    
                ],
                "updatedAt":1722498909205,
                "category":"nfts",
                "description":"Multichain NFT marketplace\nCreated by \n@cryptosoots",
                "id":"rare-gems",
                "tags":[
                    "NFT Marketplaces"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/rmrkapp",
                    "website":"https://wizard.rmrk.dev",
                    "try":"https://wizard.rmrk.dev",
                    "twitter":"https://x.com/rmrkapp",
                    "github":"https://github.com/rmrk-team",
                    "medium":"https://medium.com/rmrkapp"
                },
                "slug":"rmrk-wizard",
                "createdAt":1699292616919,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"rmrk-wizard-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"rmrk-wizard-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"rmrk-wizard-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"RMRK Wizard",
                "chains":[
                    "moonbeam",
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1692255253000,
                "shortDescription":"A no-code-but-code wizard UI for building NFTs 2.0",
                "contracts":[
                    
                ],
                "updatedAt":1722498911520,
                "category":"nfts",
                "description":"A simple UI to put together NFT 2.0 legos created by the RMRK.app team. Use this tool to get started developing advanced NFT collections by picking from a set of functions you need, and the tool will compose code for you which only needs final tweaks before being deployed!",
                "id":"rmrk-wizard",
                "tags":[
                    "NFT",
                    "Tool",
                    "Developer Tools"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/evelonapp",
                    "website":"https://platform.evelon.app/",
                    "try":"https://www.evelon.app/",
                    "twitter":"https://twitter.com/EvelonApp"
                },
                "slug":"evelon-app",
                "createdAt":1699292616145,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"evelon-app-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"evelon-app-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"evelon-app-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Evelon.App",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1690486894000,
                "shortDescription":"Transform the way you create and bring to life your own unique DNFTs, with the revolutionary platform that combines cutting-edge AI technology.",
                "contracts":[
                    
                ],
                "updatedAt":1722498873048,
                "category":"nfts",
                "description":"Evelon is a no code platform that allows you to create and deploy dynamic NFTs with ease. This project is a game changer in the world of NFTs and image generation. Evelon uses AI to generate high-quality images, making it possible to create NFTs with unique visuals that are both dynamic and engaging.",
                "id":"evelon-app",
                "tags":[
                    "NFT",
                    "Tool"
                ]
            },
            {
                "urls":{
                    "website":"https://mintlabz.io/",
                    "try":"https://app.mintlabz.io/",
                    "twitter":"https://twitter.com/mintlabz",
                    "medium":"https://blog.mintlabz.io/",
                    "discord":"https://discord.com/invite/BRF2PEetea"
                },
                "slug":"mintlabz",
                "createdAt":1712311518649,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"mintlabz-logo-small.png",
                        "mimeType":"image/png",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"mintlabz-logo-large.png",
                        "mimeType":"image/png",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"mintlabz-logo-full.png",
                        "mimeType":"image/png",
                        "height":3000
                    }
                },
                "name":"Mintlabz",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1712189524,
                "shortDescription":"MintLabz is a complete crosschain NFT solution at zero cost.",
                "contracts":[
                    
                ],
                "updatedAt":1722498889042,
                "category":"nfts",
                "description":"MintLabz aims to establish a digital NFT minting platform for third party projects to create NFT collections with utilities to reward the NFT holder. Our mission is to become the number one choice for providing complete cross-chain NFT solutions to B2B customers.",
                "id":"mintlabz",
                "tags":[
                    "nfts"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/golempark",
                    "website":"https://golempark.com",
                    "try":"https://golempark.com",
                    "twitter":"https://twitter.com/golempark",
                    "discord":"https://discord.gg/rNvtdHN8q7"
                },
                "slug":"golem-park",
                "createdAt":1699292617039,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"golem-park-logo-small.png",
                        "mimeType":"image/png",
                        "height":36
                    },
                    "large":{
                        "width":512,
                        "fileName":"golem-park-logo-large.png",
                        "mimeType":"image/png",
                        "height":512
                    },
                    "full":{
                        "width":3000,
                        "fileName":"golem-park-logo-full.png",
                        "mimeType":"image/png",
                        "height":3000
                    }
                },
                "name":"Golem Park",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1676839105000,
                "shortDescription":"Golem Park is holders friendly NFT collection. P2E blockchain game, $GP Token, Staking Pools & more",
                "contracts":[
                    {
                        "chain":"moonbeam",
                        "contract":"0x74746524f5A31F08e0528FaA704C2c5d8d116506"
                    }
                ],
                "updatedAt":1722498878088,
                "category":"nfts",
                "description":"First Time In Crypto History Token Burning Campaign!\n30% Of Total Token Supply Will Be Burned In 30 Days.\n\nAfter Minting We Are Going To Release Deflationary $GP Token & 50% Of Total Supply Will Be Distributed To All $GP NFT Holders, 1 NFT = 5 000 000 Tokens. Then 30 Days Each Day We'll Burn 1% Of Total Token Supply To Ensure Token Price Will Go UP!\n\nWorld Of Golems is a decentralized Play-To-Earn blockchain game.\nOnce You Become Golem Park NFT Holder You Will Be Able To Participate in the WoG Game, Own Countries And Display Your Message On Them.\n\nThe Leaderboard Shows Of TOP 5 Wealthiest Countries & Every Month Owners Of These Countries Will Be Rewarded With $GLMR.",
                "id":"golem-park",
                "tags":[
                    "NFT"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/rarible",
                    "website":"https://rarible.com/",
                    "try":"https://rarible.com/",
                    "twitter":"https://x.com/rarible",
                    "discord":"https://discord.com/invite/rarible"
                },
                "slug":"rarible",
                "createdAt":1722498909701,
                "logo":{
                    "small":{
                        "width":429,
                        "fileName":"rarible-small.png",
                        "mimeType":"image/png",
                        "height":121
                    },
                    "large":{
                        "width":858,
                        "fileName":"rarible-medium.png",
                        "mimeType":"image/png",
                        "height":242
                    },
                    "full":{
                        "width":1716,
                        "fileName":"rarible-large.png",
                        "mimeType":"image/png",
                        "height":485
                    }
                },
                "name":"Rarible",
                "chains":[
                    "moonbeam"
                ],
                "shortDescription":"Rarible - NFT Marketplace for Brands, Communities and Traders",
                "projectCreationDate":1721872843,
                "contracts":[
                    
                ],
                "updatedAt":1722498909701,
                "category":"nfts",
                "description":"Discover, sell and buy NFTs on Rarible! Our aggregated NFT marketplace for Ethereum NFTs and Polygon NFTs powers brands, collections and creator marketplaces.",
                "id":"rarible",
                "featured":false,
                "tags":[
                    "NFT"
                ]
            },
            {
                "urls":{
                    "website":"https://neoncrisis.io/",
                    "try":"https://neoncrisis.io/",
                    "twitter":"https://twitter.com/NeonCrisisNFT",
                    "discord":"https://discord.gg/MVVjT9k9eD"
                },
                "slug":"neoncrisis-io",
                "createdAt":1702283737907,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"neoncrisis-io-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":319,
                        "fileName":"neoncrisis-io-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":319
                    },
                    "full":{
                        "width":3000,
                        "fileName":"neoncrisis-io-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"Neon Crisis",
                "chains":[
                    "moonriver"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1654792548000,
                "shortDescription":"6,008 heroes on the $MOVR network. A $RMRK powered metaverse featuring battle simulations, equipables, and more!",
                "contracts":[
                    
                ],
                "updatedAt":1722498896060,
                "category":"nfts",
                "description":"",
                "id":"neoncrisis-io",
                "tags":[
                    "NFT",
                    "Gaming"
                ]
            },
            {
                "urls":{
                    "telegram":"https://t.me/xp_network",
                    "website":"https://xp.network/",
                    "try":"https://xp.network/",
                    "twitter":"https://twitter.com/xpnetwork_",
                    "discord":"https://discord.com/invite/g3vkcsmd38"
                },
                "slug":"xp-network",
                "createdAt":1699292615205,
                "logo":{
                    "small":{
                        "width":36,
                        "fileName":"xp-network-logo-small.jpeg",
                        "mimeType":"image/jpeg",
                        "height":36
                    },
                    "large":{
                        "width":400,
                        "fileName":"xp-network-logo-large.jpeg",
                        "mimeType":"image/jpeg",
                        "height":400
                    },
                    "full":{
                        "width":3000,
                        "fileName":"xp-network-logo-full.jpeg",
                        "mimeType":"image/jpeg",
                        "height":3000
                    }
                },
                "name":"XP Network",
                "chains":[
                    "moonbeam"
                ],
                "defiLLamaTvlExist":false,
                "projectCreationDate":1673327644000,
                "shortDescription":"A powerful NFT bridge trusted by all major blockchains ",
                "contracts":[
                    
                ],
                "updatedAt":1722498932103,
                "category":"nfts",
                "description":"We build software tools that enable experienced developers and non-coding blockchain community members to move their assets seamlessly and intuitively between versatile distributed ledgers. By doing so, we encourage unlimited growth of exchange and trade between otherwise isolated ecosystems. We enable them to enrich each other technologically with insights and discoveries. To gain access to new, previously inaccessible markets with users hungry for fresh ideas and technologies to invest in.",
                "id":"xp-network",
                "tags":[
                    "NFT",
                    "Bridges"
                ]
            }
        ],
        "count":39
    }
    ```

Below are all possible categories and their respective parameters for querying the API. Ensure you query the API with the parameter formatted exactly as shown in lowercase.

| Category | API Parameter |
|:--------:|:-------------:|
| Bridges  |   `bridges`   |
|   DAO    |     `dao`     |
|   DEX    |     `dex`     |
|   DeFi   |    `defi`     |
|  Gaming  |   `gaming`    |
| Lending  |   `lending`   |
|   NFTs   |    `nfts`     |
|  Other   |    `other`    |
|  Social  |   `social`    |
| Wallets  |   `wallets`   |


### Query a Chain {: #query-a-chain}

The following queries can be used to query all of the listed projects on Moonbeam or Moonriver. Note that Moonbase Alpha is not a supported network in the DApp Directory.

=== "Moonbeam"

    ```bash
    https://apps.moonbeam.network/api/ds/v1/app-dir/projects?chain=moonbeam
    ```

=== "Moonriver"

    ```bash
    https://apps.moonbeam.network/api/ds/v1/app-dir/projects?chain=moonriver
    ```

<div class="page-disclaimer">
    You are responsible for checking and validating the accuracy and truthfulness of all content. You are also responsible for doing your own diligence to understand the applicable risks present, including selection, performance, security, accuracy, or use of any third-party information.  All information contained herein is subject to modification without notice.
</div>
