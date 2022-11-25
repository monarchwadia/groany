#!/bin/bash

./build.sh && pip install --upgrade twine && twine upload --repository testpypi dist/*