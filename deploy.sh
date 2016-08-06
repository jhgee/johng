#!/bin/bash

# Pull last revision
git pull

# Hugo
hugo

# Load server configuration
source config.sh

# Deploy to production
lftp sftp://$USER:$PASS@$HOST  -e "set ftp:ssl-allow no; mirror  --reverse -e -R $SOURCEFOLDER $TARGETFOLDER --verbose; bye"
