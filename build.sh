#!/bin/bash

rm -rf dist/;
pip install -e .[dev] && ./test.sh && python -m build
