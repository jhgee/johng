#!/bin/bash

# Pull last revision
git pull

# Hugo
hugo

# Load server configuration
source config.sh

# Deploy to production
lftp sftp://$USER:$PASS@$HOST  -e "ssl:verify-certificate false; set sftp:auto-confirm yes; mirror  --reverse -e -R $SOURCEFOLDER $TARGETFOLDER --verbose; bye"
