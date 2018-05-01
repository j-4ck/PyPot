echo "$(tput setaf 2)[+] Installing the colorama module for python... $(tput setaf 7)"
pip install colorama
echo "$(tput setaf 2)[+] Installing the pygeoip module for python... $(tput setaf 7)"
pip install pygeoip
echo "$(tput setaf 3)[-] Installing the last required files for pygeoip... $(tput setaf 7)"
cd /root/
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
echo "$(tput setaf 2)[-] Unzipping GeoIP.dat... $(tput setaf 7)"
cd /root/
gunzip GeoIP.dat.gz
echo "$(tput setaf 2)[!] Done! Message j4ck for help with any problems!"
