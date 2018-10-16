echo 'To use upgrade do yout have clone it with https.\n'
echo 'Installing updates...'
git pull origin master
sudo cp -r ./ /opt/vhost/ && echo '\n\nRestart your bash to use the vhost alias.'
echo '\nFinished!\n'

