#!/bin/bash
# Update the index for all release tags

printf "# zopetoolkit Releases\n\n" > README.md
rm -rf releases
# 2.x releases have no 'zopeapp-versions.cfg' + omit 2.0a1 release

for tag in "master" $(git tag -l "[23]*" | sort -r | grep -v "2.0a1"); do
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

# Add a footer
printf "\n_____\n\n" >> README.md
printf "[How to maintain this page](HOWTO.md)\n" >> README.md
