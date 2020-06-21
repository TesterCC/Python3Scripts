#!/usr/bin/env bash
# use when-changed
when-changed -r -v -1 -s ./ "pytest -s $1"