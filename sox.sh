#!/bin/sh
filename=$1
duration=$2
arecord -q -f cd -d $duration -t raw | lame -r - $filename
sox $filename -n stat 2>&1 | sed -n 's#^Maximum amplitude:[^0-9]*\([0-9.]*\)$#\1#p'
