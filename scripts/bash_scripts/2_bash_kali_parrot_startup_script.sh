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
apt install -y docker.io
systemctl enable docker --now
go install github.com/tomnomnom/assetfinder@latest
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
pip3 install salt
