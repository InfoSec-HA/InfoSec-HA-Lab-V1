#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi
sudo apt-get install php7.2-curl php7.2-mbstring php7.2-xml -y
sudo apt-get install php7.3-curl php7.3-mbstring php7.3-xml -y
sudo apt-get install php php-mysqli php-gd libapache2-mod-php -y
sudo apt install hhvm -y

export PHP_haitham=$(php --version | grep -i 'PHP'|cut -d ')' -f 1 | head -1 | cut -c 5-10|cut -d '.' -f 1,2)


source ~/.bashrc
echo $PHP_haitham

sudo python3 InfoSec-lab.py $PHP_haitham
