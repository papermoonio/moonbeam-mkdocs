# Moonbeam Documentation Site (Mkdocs framework and material theme)

### Website URLS:

- **Production site:** https://docs.moonbeam.network
- **Staging site:** http://docs-stage.moonbeam.network/
- **Dev site:** http://docs-dev.moonbeam.network/

_Note: to access staging and dev sites you need to be on the internal PureStake VPN and add the following entries to your host file:_

```text
3.18.120.148 docs-stage.moonbeam.network
3.18.120.148 docs-dev.moonbeam.network
```

## Pre-requisites

To get started you need to have [mkdocs](https://www.mkdocs.org/) installed. All dependencies can be installed with a single command, you can run:

```bash
pip install -r requirements.txt
```

## Getting started

With the dependencies install, let's proceed to clone the necessary repos. In order to everything work correctly the file structure needs to be the following:

```text
moonbeam-mkdocs
|--- /material-overrides/ (folder)
|--- /moonbeam-docs/ (repository)
|--- mkdocs.yml
```

So first, lets clone this repository:

```bash
git clone https://github.com/papermoonio/moonbeam-mkdocs
cd moonbeam-mkdocs
```

Next, inside the folder just created, clone the [moonbeam-docs repository](https://github.com/moonbeam-foundation/moonbeam-docs):

```bash
git clone https://github.com/moonbeam-foundation/moonbeam-docs
```

Now in the `moonbeam-mkdocs` folder (which should be the current one) you can build the site by running:

```bash
cd ..
mkdocs serve
```

After a successful build, the site should be available at `http://127.0.0.1:8000`

## Editing Theme Files

If you're editing any of the files in the `material-overrides` directory, you can run the following command to watch for these changes and render them automatically:

```bash
mkdocs serve --watch-theme
```

Otherwise, you'll need to stop the server (`control + C`) and restart it (`mkdocs serve`) to see the changes.

## Ignoring Excluded Docs Output

Running `mkdocs serve` displays the excluded documents in your terminal. To prevent this effect, you can run:

```bash
mkdocs serve --clean
```

## Other Notes

https://www.mkdocs.org/
https://squidfunk.github.io/mkdocs-material/

This repo contains the mkdocs config files, theme overrides and css changes.
The actual content is stored in the moonbeam-docs repo and pulled into the moonbeam-docs sub-directory during build.
The static site is published to S3 using s3_website https://github.com/laurilehmijoki/s3_website
