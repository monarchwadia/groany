# python-assignment-monarch

## Dev workflow

```
pip install build
python -m build
```

To do `pip install` for development purposes, do the following:

```
pip install -e .[dev]
```

Your dev workflow can then be started using...

```
pip install --editable .
```

This will install Groany as a CLI tool. Changes should automatically propagate.

## Production workflow

We don't want to install dev dependencies in production...

```
python setup.py install
```

## Publishing

```
rm -rf dist/
python -m build
pip install --upgrade twine
twine upload --repository testpypi dist/*
```
Username: `__token__`
Password: `<the api token>`

## Installing from remote

```
pip install --index-url https://test.pypi.org/simple/ groany
```