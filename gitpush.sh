#!/bin/bash
time=`date +"%F %T"`

git add .
git commit -m "${time}"
git push
