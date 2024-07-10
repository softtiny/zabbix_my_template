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
