#!/bin/bash
set -e
# Forenoid extras -----------------------------------------
export DISPLAY=:1
export USER=root
vncserver :1 -geometry 1920x1080 -depth 24 &
sleep 2
xhost +
sleep 2
websockify 5902 localhost:5901 &
sleep 2
(cd /driver_proxy && python3 main.py &)
sleep 2
(DISPLAY=:1 cd /browser_launcher && python3 main.py &)
sleep 2
# ---------------------------------------------------------
echo "***** SeleniumBase Docker Machine *****"
exec "$@"
