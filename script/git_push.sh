#!/bin/sh

DIR=/media/ethan/Docs/projects/$1

if [ -d "$DIR" ]; then
	cd $DIR
	git add --all
	git commit -m 'Auto update'
	git push -u origin master
else
	echo "No project at $DIR"
fi
