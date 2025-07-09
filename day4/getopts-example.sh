#!/bin/bash


show_help() {
echo "usage: $0 -f <filename>"
echo " -f specify the file name"
echo " -h show this help message"
}



while getopts "f:h" opt; do

case "$opt" in
f) FILENAME=$OPTARG ;;
h) show_help; exit 0 ;;
*) show_help; exit 1 ;;
esac
done

if [ -n "$FILENAME" ]; then
echo "you entered file : $FILENAME"
fi
