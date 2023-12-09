#!/usr/bin/env bash

set -e
set -x

mypy clix
black clix tests docs_src --check
isort clix tests docs_src --check-only
