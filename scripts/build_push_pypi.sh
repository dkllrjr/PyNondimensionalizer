#!/bin/bash

source ../pyenv/bin/activate
python3 -m pip install --upgrade build twine
cd ..
echo `pwd`
python3 -m build
#python3 -m twine upload --repository testpypi --verbose dist/*
python3 -m twine upload --verbose dist/*
rm -r *.egg-info
rm -r dist
