#!/bin/sh

set -e

BRAINDUMPDIR=$HOME/braindump
NOWDATE="$(date -u +'%a %d %b %Y %T %p') $(date +'%z')"

cd $BRAINDUMPDIR

build() {
    python3 build.py

    hugo
    git status
}

liveBuild() {
    hugo server &
    while true; do
        build > /dev/null &
        wait $!
        sleep 60
    done
}

cleanup() {
    pkill -P $$
}

trap cleanup SIGINT SIGTERM

while true; do
    read -p "Choose an action? [b(build), c(commit&upload), v(view diff), h(hugo server), r(live build with hugo server), q(quit)]: " bcvhrq
    case $bcvhrq in
        [b]* ) build;;
        [c]* ) git commit -am "$NOWDATE" && git push;;
        [v]* ) git diff;;
        [h]* ) hugo server;;
        [r]* ) liveBuild;;
        [q]* ) exit;;
        * ) echo "Invalid Choice.";;
    esac
done
