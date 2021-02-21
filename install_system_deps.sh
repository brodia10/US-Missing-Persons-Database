#!/bin/bash

OS=$1

if [ "$OS" = "Linux" ]; then
    echo "Installing GeoDjango dependencies for $OS"
    sudo apt-get install $(cat Aptfile)
elif [ "$OS" = "Darwin" ]; then
    echo "Installing GeoDjango dependencies for $OS"
    brew install $(cat Aptfile.darwin)
else
    echo "ERROR: No GeoDjango installation process for $OS !!"
    exit 1
fi

wget https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip
unzip TM_WORLD_BORDERS-0.3.zip -d usmp/core/data
rm TM_WORLD_BORDERS-0.3.zip