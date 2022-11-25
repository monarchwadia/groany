#!/bin/bash

rm -rf dist/;
./test.sh && python -m build
