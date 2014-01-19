#!/usr/bin/env bash
# Script to setup a good Ubuntu 12.04 Restricted Install
# From http://howtoubuntu.org/things-to-do-after-installing-ubuntu-12-04-precise-pangolin modified to remove packages that no longer exist
echo "Downloading GetDeb and PlayDeb" &&
wget http://archive.getdeb.net/install_deb/getdeb-repository_0.1-1~getdeb1_all.deb http://archive.getdeb.net/install_deb/playdeb_0.3-1~getdeb1_all.deb &&
echo "Installing GetDeb" &&
sudo dpkg -i getdeb-repository_0.1-1~getdeb1_all.deb &&
echo "Installing PlayDeb" &&
sudo dpkg -i playdeb_0.3-1~getdeb1_all.deb &&
if [ $(lsb_release -cs) = "luna" ]
then
	echo "elementary OS Luna, Modifying to be Precise" &&
	sudo sed -i 's/luna/precise/g' /etc/apt/sources.list.d/getdeb.list &&
	sudo rm -f /etc/apt/sources.list.d/getdeb.list.bck &&
	sudo sed -i 's/luna/precise/g' /etc/apt/sources.list.d/playdeb.list &&
	sudo rm -f /etc/apt/sources.list.d/playdeb.list.bck
fi &&
echo "Deleting Downloads" &&
rm -f getdeb-repository_0.1-1~getdeb1_all.deb &&
rm -f playdeb_0.3-1~getdeb1_all.deb &&
echo "Enabling Partner Repositories" &&
sudo sed -i "/^# deb .*partner/ s/^# //" /etc/apt/sources.list &&
if [ $(lsb_release -cs) = "luna" ]
then
	echo "elementary OS Luna, Modifying to be Precise" &&
	sudo sed -i 's/luna/precise/g' /etc/apt/sources.list &&
	sudo rm -f /etc/apt/sources.list.bck
fi &&
echo "Adding Personal Package Archives" &&
sudo add-apt-repository -y ppa:videolan/stable-daily && 
sudo add-apt-repository -y ppa:webupd8team/rhythmbox && 
sudo add-apt-repository -y ppa:otto-kesselgulasch/gimp && 
sudo add-apt-repository -y ppa:gnome3-team/gnome3 && 
sudo add-apt-repository -y ppa:webupd8team/java && 
sudo add-apt-repository -y ppa:webupd8team/y-ppa-manager && 
sudo add-apt-repository -y ppa:tualatrix/ppa && 
sudo add-apt-repository -y ppa:transmissionbt/ppa && 
sudo apt-add-repository -y ppa:danielrichter2007/grub-customizer &&
echo "Updating..." &&
sudo apt-get -qq update && 
echo "Upgrading..." &&
sudo apt-get upgrade -y;
echo "Distribution Upgrading..." &&
sudo apt-get dist-upgrade -y;
echo "Installing Essentials..." &&
sudo apt-get install -y synaptic ubuntu-tweak vlc gimp gimp-data gimp-plugin-registry gimp-data-extras y-ppa-manager firestarter bleachbit openjdk-7-jre oracle-java7-installer flashplugin-installer unace unrar zip unzip p7zip-full p7zip-rar sharutils rar uudeview mpack lha arj cabextract file-roller libxine1-ffmpeg mencoder flac faac faad sox ffmpeg2theora libmpeg2-4 uudeview libmpeg3-1 mpeg3-utils mpegdemux liba52-dev mpeg2dec vorbis-tools id3v2 mpg321 mpg123 libflac++6 ffmpeg totem-mozilla icedax lame libmad0 libjpeg-progs libdvdread4 libdvdnav4 libavcodec-extra-53 libavformat-extra-53 libavutil-extra-51 libpostproc-extra-52 libswscale-extra-2 ubuntu-restricted-extras ubuntu-wallpapers* chromium-browser grub-customizer ;
echo "Installing Extras..." &&
sudo apt-get install -y vim gpaint gparted guake git gimp ardesia cheese community-themes gnome-dictionary myunity nautilus-open-terminal screen synapse terminator tree wallch mc virtualbox;
if [ $(getconf LONG_BIT) = "64" ]
then
	echo "64bit Detected" &&
	echo "Installing Google Chrome" &&
	wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&
	sudo dpkg -i google-chrome-stable_current_amd64.deb &&
	rm -f google-chrome-stable_current_amd64.deb
else
	echo "32bit Detected" &&
	echo "Installing Google Chrome" &&
	wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb &&
	sudo dpkg -i google-chrome-stable_current_i386.deb &&
	rm -f google-chrome-stable_current_i386.deb
fi
echo "Cleaning Up" &&
sudo apt-get -f install &&
sudo apt-get autoremove -y &&
sudo apt-get -y autoclean &&
sudo apt-get -y clean
echo "Logging"
echo "These are all of the packages installed after the Essentials.bash script was complete" >> ~/packages.txt
echo "" >>  ~/packages.txt
echo "comm -13 <(gzip -dc /var/log/installer/initial-status.gz | sed -n 's/^Package: //p' | sort) <(comm -23 <(dpkg-query -W -f='${Package}\n' | sed 1d | sort) <(apt-mark showauto | sort) ) >> ~/packages.txt" >> ~/packages.txt
echo "" >>  ~/packages.txt
comm -13 <(gzip -dc /var/log/installer/initial-status.gz | sed -n 's/^Package: //p' | sort) <(comm -23 <(dpkg-query -W -f='${Package}\n' | sed 1d | sort) <(apt-mark showauto | sort) ) >> ~/packages.txt
read -p "Press [Enter] key to finish by restarting (or CTRL-C to stop the script here)..." && sudo reboot
