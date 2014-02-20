#! /bin/bash -x
# usage: `. screencast.sh <filename>`

# Helpers function to color terminal.
textreset=$(tput sgr0)
colored=$(tput setaf 6) 

# Checking requirements.
INSTALLED_PACKAGES=$(sudo enter-chroot -b dpkg -l | awk '{print $2}')
REQUIRED_PACKAGES="libav-tools libavcodec-extra-53 libavdevice-extra-53 \
    libavfilter-extra-2 libavformat-extra-53 libavutil-extra-51 \
    libpostproc-extra-52 libswscale-extra-2 x264 libx264-dev pulseaudio"
for package in $REQUIRED_PACKAGES; do
  if ! echo $INSTALLED_PACKAGES | \grep -q -E "^ii $package"; then
    echo "${colored}Installing avconv and its friends...${textreset}"
    sudo enter-chroot -x sudo apt-get install -qq -y $REQUIRED_PACKAGES
    break
  fi
done

# Start screen capture.
echo "${colored}Starting screen capture...${textreset}"
if [ "$1" ]; then 
  FILENAME="$1" 
else 
  FILENAME="screencast"
fi
RESOLUTION=`xrandr |sed -n 's/.*current \([0-9]\+\) x \([0-9]\+\).*/\1x\2/p'`
sudo enter-chroot host-x11 avconv -f alsa -ac 2 -ab 128k -i pulse \
    -f x11grab -r 30 -s $RESOLUTION -i :0.0 \
    -vcodec libx264 -preset ultrafast -crf 0 Downloads/"$FILENAME".mkv
