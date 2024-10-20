#!/bin/sh

xset s off
xset -dpms

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
nohup xrandr --output DP-4 --primary --mode 1920x1080 --left-of DP-2 > /dev/null 2>&1 &
nohup setxkbmap -layout us -variant intl > /dev/null 2>&1 &
nohup ~/.screenlayout/main.sh > /dev/null 2>&1 &
nohup wal -i ~/.wallpapers > /dev/null 2>&1 &
nohup copyq > /dev/null 2>&1 &
nohup flameshot > /dev/null 2>&1 &
# nohup ollama serve > /dev/null 2>&1 &
# nohup redshift -l -23.65747171336024:-46.74419551785399 > /dev/null 2>&1 &
nohup screendimmer > /dev/null 2>&1 &
