echo 'Installing updates...'
sudo cp -r ./ /opt/vhost/
echo  'alias vhost="sudo python3 /opt/vhost/sample/main.py"' >> /etc/bash.bashrc
echo 'Install completed!'
echo 'restart your bash to use the vhost alias.'
