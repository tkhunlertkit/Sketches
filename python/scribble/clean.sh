#!/bin/bash

find . ! -name 'scribble.py' ! -name 'clean.sh' -type f -exec rm -rf {} +
