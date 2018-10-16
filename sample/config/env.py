CONFIG_DIR = '/laradock/apache2/sites/'
SITES_ENABLED = 0 #'/etc/apache2/sites-enabled/' 
HOSTS_FILE = '/etc/hosts'

COMMAND_RESTART_APACHE = 'sudo /laradock docker-compose down && sudo /laradock docker-compose up -d apache2'
