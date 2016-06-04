#!/bin/bash
printf '\e[8;40;80t'
printf '\e[3;0;0t'
mydir="$(dirname "$BASH_SOURCE")"
cd "$mydir/Michael" /tmp
python timer.py;
exit;