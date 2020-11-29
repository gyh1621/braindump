#!/bin/sh

set -e

BRAINDUMPDIR=$HOME/braindump
ORGSRCDIR=$HOME/org

rm -rf $BRAINDUMPDIR/org
rsync -a --progress $ORGSRCDIR $BRAINDUMPDIR --exclude .git

cd $BRAINDUMPDIR
python3 build.py

hugo
git status

NOWDATE="$(date -u +'%a %d %b %Y %T %p') $(date +'%z')"
while true; do
    read -p "Choose an action? [c(commit&upload), v(view diff), q(quit)]: " cvq
    case $cvq in
        [c]* ) git commit -am "$NOWDATE" && git push; break;;
        [v]* ) git diff;;
        [q]* ) exit;;
        * ) echo "Invalid Choice.";;
    esac
done
