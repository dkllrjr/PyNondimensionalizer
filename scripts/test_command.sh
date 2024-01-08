#!/bin/bash

source ../pyenv/bin/activate
cd ..
python3 -m pip install -e .
exec bash
