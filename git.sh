#!/usr/bin/bash

# 设置用户
git config --local user.email 'github-actions[bot]@users.noreply.github.com'
git config --local user.name 'github-actions[bot]'

# 远端同步至本地
git pull

# 推送变更
git add .
git commit -m "$(date +'%Y/%m/%d')"
git push

# 删除用户
git config --local --unset user.email
git config --local --unset user.name
