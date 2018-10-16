# encoding:utf-8
#!/usr/bin/env python3
# for: Linux(Debian distros)
# Developed by: Gabriel Dissotti
import os
from config import env
from termcolor import colored
from helpers import prefill, messages
import subprocess

# Variables
example_new_vhost = "\t\t\t    (Example: dev.test.com)\n"
text_new_vhost = "Enter the new Virtual Host: "
text_dir_name = "Enter the absolute path of the site: "
text_hostname = "Enter the IP server:"

# Colors
text_dir_name = colored(text_dir_name , 'cyan', attrs=['blink'])
text_hostname = colored(text_hostname , 'cyan', attrs=['blink'])
text_new_vhost = colored(text_new_vhost,'cyan', attrs=['blink'])

def getListVhosts():
    arq = open(env.HOSTS_FILE, 'r', encoding="utf8")
    hosts = arq.readlines()
    print(colored("\nNº   IP\t\tNames", 'white', attrs=['blink','bold']))
    for i  in range(len(hosts)):
        if (hosts[i].find('#') == -1 and hosts[i].find('ip6') == -1 and len(hosts[i]) > 7):
            print("\n({:0>15}) {}".format((colored((i+1), 'yellow', attrs=['bold'])),(colored(hosts[i], 'red', attrs=['blink']))))


def list():
    os.system('clear')
    messages.title(">> Virtual Hosts Listing <<")
    getListVhosts()
    input('>> Back to menu; ')

def new(hostname = "", vhost_name = "", dir_name = ""):
    if (not hostname and not vhost_name and not dir_name):
        messages.title(">> Creating Virtual Hosts <<")
        print("\n")
        hostname = str(prefill.input_with_prefill(text_hostname,"127.0.0.1"))
        dir_name = str(prefill.input_with_prefill(text_dir_name,"/var/www/"))
        vhost_name = str(prefill.input_with_prefill((example_new_vhost + text_new_vhost),"dev."))
    if (not vhost_name or not dir_name or not hostname):
        messages.error("Inform the data correctly!")
        new()
        return 0

    server_config = vhost_name #with prefix
    vhost_name =  vhost_name.split('.')
    del vhost_name[0]
    vhost_name = str.join('.', vhost_name); # less prefixo

    messages.process("Generating settings file...")
    config_vhost = """<VirtualHost *:80>
   ServerAdmin webmaster@localhost
   ServerName """+server_config+"""
   ServerAlias """+vhost_name+"""
   DocumentRoot """+dir_name+"""
   <Directory """+dir_name+""">
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Order allow,deny
        Allow from all
    </Directory>
</VirtualHost>"""

    messages.success("Created a archive with following lines in "+env.CONFIG_DIR+":\n\n" + config_vhost)


    arq = open((env.CONFIG_DIR + vhost_name + ".conf"), 'w+')
    arq.writelines(config_vhost)
    arq.close()

    messages.process(("Enabling virtual host " + server_config + "..."))


    subprocess.getoutput(("a2ensite "+ vhost_name +".conf"))

    

    hosts = hostname + " " + server_config
    messages.success( "Added following lines in "+env.HOSTS_FILE+":\n\n" + hosts)
   
    messages.process(("Updating hosts file with " + server_config +" config..."))
    subprocess.getoutput(("echo '" + hosts + "' >> "+env.HOSTS_FILE+""))
    messages.process(("Restarting apache2..."))
    subprocess.getoutput("service apache2 restart")
    subprocess.getoutput("systemctl restart apache2")
    messages.success("\n\n\n\tSUCCESS!\t Virtual host created successfully! \n\n\n")
    messages.info(("See a log scrolling up.\nFor access use " + server_config +" in your browser. \n"))


    input("Tank you to use this program, git a star the project on Github!\n\nPress any key to continue... ")
    return 0

def edit():
    os.system('clear')
    messages.title(">> Edit Virtual Hosts<<")
    messages.question("\nChoose a virtual host to edit by your number: ")
    db = open(env.HOSTS_FILE, 'r', encoding="utf8")
    db = db.readlines()
    getListVhosts()
    option = input("\nEdit nº: ")
    if not option.isnumeric():
        return 0
    option = int(option)-1
    os.system('clear')

    edithost = db[option]
    messages.question("Edit Virtual Host:")
    messages.info(edithost)

    edithost = edithost.split()
    edithostname = edithost[0]
    editvhostname = edithost[1]
    if(len(edithost) > 2):
        editvhostname = edithost[2]

    editdirname = ""
    try:
        arq = open((env.CONFIG_DIR + edithost[1] + ".conf"), 'r')
        words = arq.read().split()
        editdirname = words.index("DocumentRoot")
        editdirname = words[(editdirname+1)]
        arq.close()
    except IOError:
       messages.atention("File not found: "+env.CONFIG_DIR+"" + edithost[1] + ".conf")

    hostname = str(prefill.input_with_prefill(text_hostname,edithostname))
    vhost_name = str(prefill.input_with_prefill(text_new_vhost,editvhostname))
    dir_name = str(prefill.input_with_prefill(text_dir_name,editdirname))

    messages.question("Are you sure you want to save changes? Y/n")
    op = input().strip().lower()

    if op != 'n':
        subprocess.getoutput(("rm " + env.CONFIG_DIR + edithost[1] + ".conf"))
        if SITES_ENABLED != 0:
            subprocess.getoutput(("rm " + env.SITES_ENABLED + edithost[1] + ".conf"))
        f = open(env.HOSTS_FILE, 'r', encoding="utf8")
        lines = f.readlines()
        f.close()
        f = open(env.HOSTS_FILE, 'w', encoding="utf8")
        for line in lines:
            if line!=db[option]:
                f.write(line)
        f.close()
        new(hostname,vhost_name,dir_name) # exists => 1


def delete():
    os.system('clear')

    messages.title(">> Delete Virtual Host<<")
    messages.question("\nChoose a virtual host to delete by your number: ")

    getListVhosts()

    option = input("\nDelete nº: ")
    if not option.isnumeric():
        return 0
    option = int(option)-1
    os.system('clear')

    db = open(env.HOSTS_FILE, 'r', encoding="utf8")
    db = db.readlines()
    edithost = db[option]
    messages.question("Remove Virtual Host:")
    messages.info(edithost)

    edithost = edithost.split()
    edithostname = edithost[0]
    if(len(edithost) > 1):
        editvhostname = edithost[1]
    if(len(edithost) > 2):
        editvhostname = edithost[2]

    try:
        arq = open((env.CONFIG_DIR + edithost[1] + ".conf"), 'r')
        words = arq.read().split()
        editdirname = words.index("DocumentRoot")
        editdirname = words[(editdirname+1)]
        arq.close()
    except IOError:
       messages.atention("File not found: "+env.CONFIG_DIR+ edithost[1] + ".conf \n")
    messages.question("Are you sure to delete the virtual host? Y/n")
    op = input().strip().lower()

    if op != 'n':
        subprocess.getoutput(("rm " + env.CONFIG_DIR + edithost[1] + ".conf"))
        if SITES_ENABLED != 0:
            subprocess.getoutput(("rm " + env.SITES_ENABLED + edithost[1] + ".conf"))
        f = open(env.HOSTS_FILE, 'r', encoding="utf8")
        lines = f.readlines()
        f.close()
        f = open(env.HOSTS_FILE, 'w', encoding="utf8")
        for line in lines:
            if line!=db[option]:
                f.write(line)
        f.close()
        messages.success("Virtual host removed successfully! ")
        messages.info(("You can no longer access this virtual host through the browser"))
        input("Press any key to continue... ")
        return 0
