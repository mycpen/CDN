#!/usr/bin/bash

# 远端同步至本地
git pull

# 推送变更
git add .
git commit -m "$(date +'%Y/%m/%d')"
git push
