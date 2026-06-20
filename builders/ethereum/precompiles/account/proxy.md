---
title: Interacting with the Proxy Precompile
description: How to use the Moonbeam proxy Solidity precompile interface to add and remove proxy accounts from Substrate's Proxy Pallet.
categories:
- Precompiles
- Ethereum Toolkit
url: https://docs.moonbeam.network/builders/ethereum/precompiles/account/proxy/
word_count: 2074
token_estimate: 3274
version_hash: sha256:8fcab0b4e127a1b3a06c3bd1a80c5b5390a5b42ef8c9065244ec278b3e6ad2ab
last_updated: '2026-05-21T21:21:53+00:00'
---

# Interacting with the Proxy Precompile

## Introduction {: #introduction }

The Proxy Precompile on Moonbeam allows accounts to set proxy accounts that can perform specific limited actions on their behalf, such as governance, staking, or balance transfers.

If a user wants to provide a second user access to a limited number of actions on their behalf, traditionally the only method to do so would be by providing the first account's private key to the second. However, Moonbeam includes native proxy functionality in the runtime, which enables proxy accounts. Proxy accounts should be used due to the additional layer of security that they provide, where many accounts can perform actions for a main account. This is best if, for example, a user wants to keep their wallet safe in cold storage but still wants to access parts of the wallet's functionality like governance or staking.

**The Proxy Precompile can only be called from an Externally Owned Account (EOA) or by the [Batch Precompile](/moonbeam-mkdocs/builders/ethereum/precompiles/ux/batch/).**

To learn more about proxy accounts and how to set them up for your own purposes without use of the Proxy Precompile, view the [Setting up a Proxy Account](/moonbeam-mkdocs/tokens/manage/proxy-accounts/) page.

The Proxy Precompile is located at the following address:

=== "Moonbeam"

     ```text
     0x000000000000000000000000000000000000080b
     ```
=== "Moonriver"

     ```text
     0x000000000000000000000000000000000000080b
     ```
=== "Moonbase Alpha"

     ```text
     0x000000000000000000000000000000000000080b
     ```

!!! note
    There can be some unintended consequences when using the precompiled contracts on Moonbeam. Please refer to the [Security Considerations](/moonbeam-mkdocs/learn/core-concepts/security/) page for more information.
## The Proxy Solidity Interface {: #the-proxy-solidity-interface }

[`Proxy.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/proxy/Proxy.sol) is an interface through which Solidity contracts can interact with the Proxy Pallet. You do not have to be familiar with the Substrate API since you can interact with it using the Ethereum interface you're familiar with.

The interface includes the following functions:

??? function "**addProxy**(*address* delegate, *ProxyType* proxyType, *uint32* delay) - registers a proxy account for the sender after a specified number of `delay` blocks (generally zero). Will fail if a proxy for the caller already exists"

    === "Parameters"

        - `delegate` - address of the account to be registered as a proxy
        - `proxyType` - ProxyType enumeration specifying the type of proxy to be registered
        - `delay` - uint32 number of blocks before the proxy registration becomes active

??? function "**removeProxy**(*address* delegate, *ProxyType* proxyType, *uint32* delay) - removes a registered proxy for the sender"

    === "Parameters"

        - `delegate` - address of the proxy account to be removed
        - `proxyType` - ProxyType enumeration of the proxy type to be removed
        - `delay` - uint32 delay value of the proxy to be removed

??? function "**removeProxies**() - removes all of the proxy accounts delegated to the sender"

    === "Parameters"

        None.

??? function "**proxy**(*address* real, *address* callTo, *bytes* callData) - dispatches `callData` to `callTo` on behalf of `real` using the caller's registered proxy rights"

    === "Parameters"

        - `real` - address of the account the call will be executed for
        - `callTo` - address receiving the proxied call (subject to [dispatch limitations](#proxy-dispatch-limitations))
        - `callData` - call data to forward to the destination

??? function "**proxyForceType**(*address* real, *ProxyType* forceProxyType, *address* callTo, *bytes* callData) - dispatches `callData` on behalf of `real` while enforcing the provided proxy type instead of inferring it"

    === "Parameters"

        - `real` - address of the account the call will be executed for
        - `forceProxyType` - ProxyType value that must match the caller's registered proxy type
        - `callTo` - address receiving the proxied call (subject to [dispatch limitations](#proxy-dispatch-limitations))
        - `callData` - call data to forward to the destination

??? function "**isProxy**(*address* real, *address* delegate, *ProxyType* proxyType, *uint32* delay) - returns a boolean, `true` if the delegate address is a proxy of type `proxyType`, for address `real`, with the specified `delay`"

    === "Parameters"

        - `real` - address of the account that might be represented by the proxy
        - `delegate` - address of the potential proxy account
        - `proxyType` - ProxyType enumeration of the proxy type to check
        - `delay` - uint32 delay value to check

The `proxyType` parameter is defined by the following `ProxyType` enum, where the values start at `0` with the most permissive proxy type and are represented as `uint8` values:

```solidity
enum ProxyType {
    Any,
    NonTransfer,
    Governance,
    Staking,
    CancelProxy,
    Balances,
    AuthorMapping,
    IdentityJudgement
}
```

## Proxy Types {: #proxy-types }

There are multiple types of proxy roles that can be delegated to accounts, which are represented in `Proxy.sol` through the `ProxyType` enum. The following list includes all of the possible proxies and the type of transactions they can make on behalf of the primary account:

 - **Any** — allows the proxy account to dispatch the `Governance`, `Staking`, `Balances`, and `AuthorMapping` actions permitted by the runtime filter; arbitrary smart contract targets are not allowed, and balance transfers are limited to EOAs without contract code
 - **NonTransfer** — allows transactions through the `Governance`, `Staking` and `AuthorMapping` precompiles, where the `msg.value` is checked to be zero; no contract calls outside those precompiles are permitted
 - **Governance** - the governance proxy will allow the proxy account to make any type of governance related transaction (includes both democracy or council pallets)
 - **Staking** - the staking proxy will allow the proxy account to make staking related transactions through the `Staking` Precompile, including calls to the `AuthorMapping` Precompile
 - **CancelProxy** - the cancel proxy will allow the proxy account to reject and remove delayed proxy announcements (of the primary account). Currently, this is not an action supported by the Proxy Precompile
 - **Balances** - allows only plain balance transfers to EOAs with no contract code and does not support calling contracts or precompiles
 - **AuthorMapping** - this type of proxy account is used by collators to migrate services from one server to another
 - **IdentityJudgement** - the identity judgement proxy will allow the proxy account to judge and certify the personal information associated with accounts on Polkadot. Currently, this is not an action supported by the Proxy Precompile

## Proxy Dispatch Limitations {: #proxy-dispatch-limitations }

Moonbeam applies an EVM call filter to proxy dispatches. The key rules are as follows:

- Only EOAs (or the [Batch Precompile](/moonbeam-mkdocs/builders/ethereum/precompiles/ux/batch/)) can call the Proxy Precompile; contracts cannot
- Not a general “call any contract as the real account” path—non-precompile contract calls are rejected
- Governance, Staking, and AuthorMapping calls must target their respective precompiles with `msg.value = 0`
- Balances proxy calls only allow plain value transfers to EOAs with no contract code (not to contracts or precompiles)
- `CancelProxy` is not dispatched through the Proxy Precompile

## Interact with the Solidity Interface {: #interact-with-the-solidity-interface }

The following section will cover how to interact with the Proxy Precompile from Remix. Please note that **the Proxy Precompile can only be called from an EOA or by the [Batch Precompile](/moonbeam-mkdocs/builders/ethereum/precompiles/ux/batch/)**.

### Checking Prerequisites {: #checking-prerequisites }

The below example is demonstrated on Moonbase Alpha, however, similar steps can be taken for Moonbeam and Moonriver. You should:  

 - Have MetaMask installed and [connected to Moonbase Alpha](/moonbeam-mkdocs/tokens/connect/metamask/)
 - Have an account with some DEV tokens.
  You can get DEV tokens for testing on Moonbase Alpha once every 24 hours from the [Moonbase Alpha Faucet](https://faucet.moonbeam.network)
 - Have a second account that you control to use as a proxy account (funding optional)

### Remix Set Up {: #remix-set-up }

To get started, get a copy of [`Proxy.sol`](https://github.com/moonbeam-foundation/moonbeam/blob/master/precompiles/proxy/Proxy.sol) and take the following steps:

1. Click on the **File explorer** tab
2. Copy and paste the file contents into a [Remix file](https://remix.ethereum.org) named `Proxy.sol`

![Copying and Pasting the Proxy Interface into Remix](/moonbeam-mkdocs/images/builders/ethereum/precompiles/account/proxy/proxy-1.webp)

### Compile the Contract {: #compile-the-contract }

1. Click on the **Compile** tab, second from top
2. Then to compile the interface, click on **Compile Proxy.sol**

![Compiling Proxy.sol](/moonbeam-mkdocs/images/builders/ethereum/precompiles/account/proxy/proxy-2.webp)

### Access the Contract {: #access-the-contract }

1. Click on the **Deploy and Run** tab, directly below the **Compile** tab in Remix. Note: you are not deploying a contract here, instead you are accessing a precompiled contract that is already deployed
2. Make sure **Injected Provider - Metamask** is selected in the **ENVIRONMENT** drop down
3. Ensure **Proxy.sol** is selected in the **CONTRACT** dropdown. Since this is a precompiled contract there is no need to deploy, instead you are going to provide the address of the Precompile in the **At Address** field
4. Provide the address of the Proxy Precompile for Moonbase Alpha: `0x000000000000000000000000000000000000080b` and click **At Address**
5. The Proxy Precompile will appear in the list of **Deployed Contracts**

![Provide the address](/moonbeam-mkdocs/images/builders/ethereum/precompiles/account/proxy/proxy-3.webp)

### Add a Proxy {: #add-proxy }

You can add a proxy for your account via the Proxy Precompile if your account doesn't already have a proxy. In this example, you will add a [balances](#:~:text=Balances) proxy to an account by taking the following steps:

1. Expand the Proxy Precompile contract to see the available functions
2. Find the **addProxy** function and press the button to expand the section
3. Insert your second account's address as the **delegate**, `5` as **proxyType**, and `0` as **delay**
4. Press **transact** and confirm the transaction in MetaMask

!!! note
     When constructing the transaction in Remix, the **proxyType** is represented as a `uint8`, instead of the expected enum `ProxyType`. In Solidity, enums are compiled as `uint8`, so when you pass in `5` for **proxyType**, you indicate the sixth element in the `ProxyType` enum, which is the balances proxy.

![Call the addProxy function](/moonbeam-mkdocs/images/builders/ethereum/precompiles/account/proxy/proxy-4.webp)

### Check a Proxy's Existence {: #check-proxy }

You can determine whether or not an account is a proxy account for a primary account. In this example, you will insert the parameters of the [previously added proxy](#add-proxy) to determine if the proxy account was successfully added:

1. Find the **isProxy** function and press the button to expand the section
2. Insert your primary account's address as **real**, your second account's address as **delegate**, `5` as **proxyType**, and `0` as **delay**
3. Press **call**

If everything went correctly, the output should be `true`.

![Call the isProxy function](/moonbeam-mkdocs/images/builders/ethereum/precompiles/account/proxy/proxy-5.webp)

### Dispatch a Proxy Call {: #dispatch-proxy-call }

Once you've registered a proxy, you can forward a call on behalf of the real account. In Remix, expand the Proxy Precompile contract and open **proxy** (or **proxyForceType** if you want to force the proxy type). The following example will use a Balances proxy (or `Any` with Balances allowed) to send value to an EOA with no contract code, keeping `callData` as `0x` for a plain transfer. Remember that the runtime limits described in [Proxy Dispatch Limitations](#proxy-dispatch-limitations) apply.

Ensure MetaMask is connected to the delegate/proxy account (the one authorized via `addProxy`), not the primary account, before dispatching. Then, take the following steps:

1. In Remix, set the amount to send in the **VALUE** field. Double-check the VALUE units (wei vs ether) before sending. 
2. Enter the address of the account being proxied.
3. Enter the callTo address (this is the receiving account).
4. Enter `0x` for call data.
5. Press **Transact** to dispatch the call.

![Dispatching a proxied call](/moonbeam-mkdocs/images/builders/ethereum/precompiles/account/proxy/proxy-6.webp)

### Remove a Proxy {: #remove-proxy }

You can remove a proxy from your account via the Proxy Precompile. In this example, you will remove the balances proxy [previously added](#add-proxy) to your delegate account by taking the following steps:

1. Expand the Proxy Precompile contract to see the available functions
2. Find the **removeProxy** function and press the button to expand the section
3. Insert your second account's address as the **delegate**, `5` as **proxyType**, `0` and as **delay**
4. Press **transact** and confirm the transaction in MetaMask

After the transaction is confirmed, if you repeat the steps to [check for a proxy's existence](#check-proxy), the result should be `false`.

![Call the removeProxy function](/moonbeam-mkdocs/images/builders/ethereum/precompiles/account/proxy/proxy-7.webp)

And that's it! You've completed your introduction to the Proxy Precompile. Additional information on setting up proxies is available on the [Setting up a Proxy Account](/moonbeam-mkdocs/tokens/manage/proxy-accounts/) page and the [Proxy Accounts](https://wiki.polkadot.com/learn/learn-proxies/) page on Polkadot's documentation. Feel free to reach out on [Discord](https://discord.com/invite/PfpUATX) if you have any questions about any aspect of the Proxy Precompile.
