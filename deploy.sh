#!/bin/bash

# Pull last revision
git pull

# Hugo
hugo

# Load server configuration
source config.sh

# Deploy to production
lftp sftp://$USER:$PASS@$HOST  -e "mirror  --reverse -e -r $SOURCEFOLDER $TARGETFOLDER --verbose; bye"
