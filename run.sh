#!/bin/sh

docker run --rm -it -v "$(pwd)":/work opencv-stitcher-example python main.py
