#!/bin/bash


# This script installs the necessary libs for GeoDjango and should be ran from the repository root.
# It detects which OS you're using and proceeds with the correct installation method.
# This works for any version of Linux or OSx.
# Make sure you run "chmod +x ./install_system_deps.sh" to make it executable.

# Colors for colored output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
RESET='\033[0m'


# Start script
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo -e "${GREEN}Installing GeoDjango dependencies for ${YELLOW}$OSTYPE..."
    sudo apt-get install binutils libproj-dev gdal-bin
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "${GREEN}Installing GeoDjango dependencies for ${YELLOW}$OSTYPE..."
    brew install postgresql
    brew install postgis
    brew install gdal
    brew install libgeoip
else
    echo - e"${RED}ERROR: No GeoDjango installation process for $OSTYPE !!"
    exit 1
fi


file_url="https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip"
zip_file=TM_WORLD_BORDERS-0.3.zip
unzip_to_directory="usmp/core/data"

echo
echo -e "${CYAN}Downloading...${RESET} ${YELLOW}$file_url${RESET}"
curl -O $file_url
echo
echo -e "${CYAN}Unzipping...${RESET} ${YELLOW}$zip_file${RESET} -> ${YELLOW}$unzip_to_directory${RESET}"
unzip $zip_file -d $unzip_to_directory
echo
echo -e "${CYAN}Removing zip file...${RESET} ${YELLOW}$zip_file${RESET}"
rm $zip_file
echo 
echo -e "${GREEN}Finished."
echo