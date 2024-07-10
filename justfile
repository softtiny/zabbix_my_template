#!/usr/bin/env just --justfile
#https://github.com/casey/just

set dotenv-load

@default:
    just --list

@ipython:
    ipython

@tools:
    python tools.py -v

@valuemap:
    python valuemap_create.py

@network_itemprototype:
    python network/itemprototype_create.py
