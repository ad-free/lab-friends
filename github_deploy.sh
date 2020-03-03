#!/bin/bash -e

printf '1>>>>>>>>>>>>>.\n'
git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* || exit
git fetch --all || exit

printf '\nb2>>>>>>>>>>>>>>'
git checkout master || exit
git merge --no-ff origin/dev || exit

printf '3>>>>>>>>>\n'
git push https://"${GITHUB_TOKEN}"@github.com/ad-free/lab-friends.git

printf 'Deployed'