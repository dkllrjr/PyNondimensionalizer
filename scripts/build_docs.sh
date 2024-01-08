#!/bin/bash

source ../pyenv/bin/activate
cd ..
python3 -m pip install -e .
pdoc --math -t ./templates -o ./docs ./pynondimensionalizer
rm -r *.egg-info
