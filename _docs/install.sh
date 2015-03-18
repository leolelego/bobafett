#!/bin/bash
# Download
git clone https://github.com/leoderbois/Boba-Fett-Theme-For-Jekyll.git

# Create ressources
cd Boba-Fett-Theme-For-Jekyll

mv _configDemo.yml _config.yml

mkdir assets
mkdir css
cp _docs/main.scss css/
cp -r _docs/_demoposts _posts
rm -rf assets
cp -r _docs/assetsdemo assets

mv CNAMEDEMO CNAME

