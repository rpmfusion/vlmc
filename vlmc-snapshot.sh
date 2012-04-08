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
date=$(date +%Y%m%d)
package=vlmc

pushd "$tmp"
git clone git://git.videolan.org/vlmc.git
cd $package
git archive --prefix="${package}-${date}/" --format=tar master | bzip2 > "$pwd"/${package}-${date}.tar.bz2
popd
