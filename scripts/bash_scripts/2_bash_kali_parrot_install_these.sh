#!/bin/bash

#Making a list of stuff to install when i make a fresh Kali box.

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
