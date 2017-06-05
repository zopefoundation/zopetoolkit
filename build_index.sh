#!/bin/bash
# Update the index for all release tags

printf "# zopetoolkit Releases\n\n" > README.md
rm -rf releases
# 2.x releases have no 'zopeapp-versions.cfg'

for tag in "master" $(git tag -l "2*" | sort -r); do
    echo $tag
    mkdir -p releases/$tag
    git show $tag:ztk-versions.cfg > releases/$tag/ztk-versions.cfg
    printf "## $tag\n\n- [ztk-versions.cfg](releases/$tag/ztk-versions.cfg)\n\n" >> README.md;
done

for tag in $(git tag -l "1*" | grep -v dev- | sort -r); do
    echo $tag
    mkdir -p releases/$tag
    git show $tag:ztk-versions.cfg > releases/$tag/ztk-versions.cfg
    git show $tag:zopeapp-versions.cfg > releases/$tag/zopeapp-versions.cfg
    printf "## $tag\n\n- [ztk-versions.cfg](releases/$tag/ztk-versions.cfg)\n- [zopeapp-versions.cfg](releases/$tag/zopeapp-versions.cfg)\n\n" >> README.md;
done
