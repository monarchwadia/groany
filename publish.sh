#!/bin/bash

./build.sh && pip install --upgrade twine && twine upload --repository testpypi -u__token__ dist/*