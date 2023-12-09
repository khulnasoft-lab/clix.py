#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place docs_src clix tests --exclude=__init__.py
black clix tests docs_src
isort clix tests docs_src
