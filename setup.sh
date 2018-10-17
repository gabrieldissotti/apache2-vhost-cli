echo 'Checking dependencies'
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install termcolor

echo 'Installing updates...'
sudo cp -r ./ /opt/vhost/
echo  'alias vhost="sudo python3 /opt/vhost/sample/main.py"' >> /etc/bash.bashrc
echo 'Install completed!'
echo 'restart your bash to use the vhost alias.'
