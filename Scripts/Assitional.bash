#!/usr/bin/env bash
echo "Adding Repositories..." &&
sudo add-apt-repository -y ppa:skype-wrapper/ppa && #Skype-Wraper
sudo add-apt-repository ppa:otto-kesselgulasch/gimp && #Latest Version of Gimp
echo "Installing Packages..." &&
sudo apt-get update &&
sudo apt-get upgrade -y &&
sudo apt-get install skype-wrapper skype;
echo "Cleaning Up" &&
sudo apt-get -f install &&
sudo apt-get autoremove -y &&
sudo apt-get -y autoclean &&
sudo apt-get -y clean
