#!/bin/sh

#VerifyMinecraftEdu

MCPATH="/Library/Application Support/minecraftedu"
HOMEPATH="$HOME/Library/Application Support/"
VERSION="%REPLACE%"

if [[ $USER == "admin" ]]; then
	logger "VerifyMinecraftEdu.sh: Skipping sync for $USER"
	exit 0
fi

logger "VerifyMinecraftEdu.sh: Starting for $USER"
if [[ -e "$MCPATH" ]]; then
	if [[ ! -e "$HOME/.mcedu-${VERSION}" ]]; then
		/usr/bin/rsync -rlptDv --delete --exclude 'minecraft/saves' "$MCPATH" "$HOMEPATH" | logger
		touch ~/.mcedu-"${VERSION}"
	fi
else
	logger "Didn't find MinecraftEDU in /Library/Application Support/."
fi
logger "VerifyMinecraftEdu.sh: complete."
