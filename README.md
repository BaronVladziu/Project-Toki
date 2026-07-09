# Project-Toki

## Introduction

I'm a fan of a silly little language called Toki Pona, so I created some useful (or not) tools to analyse and process this language.

To learn more about the language check:

- https://tokipona.org/ - official language website
- https://linku.la/ - great interactive English - Toki Pona dictionary

Current tools:

- [Generating text structure tree](#generating-text-structure-tree)

## Setup

```shell
git clone https://github.com/BaronVladziu/Project-Toki.git
cd Project-Toki
./setup.sh
```

## Usage

### Generating text structure tree

```shell
source .venv/bin/activate
./project_toki/tools/analyse_text.py -i "mi sona e toki pona a!"
```

## Running tests

```shell
./test.sh
```
