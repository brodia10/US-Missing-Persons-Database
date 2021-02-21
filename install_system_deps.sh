#!/bin/bash

OS=$1

if [ "$OS" = "Linux" ]; then
    echo "Installing GeoDjango dependencies for $OS"
    sudo apt-get install binutils libproj-dev gdal-bin
elif [ "$OS" = "Darwin" ]; then
    echo "Installing GeoDjango dependencies for $OS"
    brew install postgresql
    brew install postgis
    brew install gdal
    brew install libgeoip
else
    echo "ERROR: No GeoDjango installation process for $OS !!"
    exit 1
fi

wget https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip
unzip TM_WORLD_BORDERS-0.3.zip -d usmp/core/data
rm TM_WORLD_BORDERS-0.3.zip