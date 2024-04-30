#!/bin/bash

#start up script for kali/parrotOS boxes/ things to install on new install

cd /opt
sudo su
apt get
apt upgrade
apt install vsftpd
apt install ftp
pip install sshuttle
git clone https://github.com/Dewalt-arch/pimpmykali.git
git clone https://github.com/Tib3rius/AutoRecon.git
apt install -y docker.io
systemctl enable docker --now
go install github.com/tomnomnom/assetfinder@latest
pip3 install salt
