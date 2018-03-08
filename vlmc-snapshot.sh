#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
package=vlmc

pushd "$tmp"
git clone https://code.videolan.org/videolan/vlmc.git
cd $package
date=$(git log -1 --format=%cd --date=short | tr -d \-)
git archive --prefix="${package}-${date}/" --format=tar master | bzip2 > "$pwd"/${package}-${date}.tar.bz2
popd
sed -i "s|^%global date .*|%global date $date|" vlmc.spec
