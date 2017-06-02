@echo off

set DIR=D:\projects\%1\

if not exist %DIR% (
	echo No project at %DIR%
) else (
	cd /d %DIR%
	git add --all
	git commit -m 'Auto update'
	git push -u origin master
)
