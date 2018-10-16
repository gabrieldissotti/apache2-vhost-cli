# encoding:utf-8
#!/usr/bin/env python3
# for: Linux(Debian distros)
# Developed by: Gabriel Dissotti
from termcolor import colored
from components import header, menu, vhost
from helpers import messages
import os
import subprocess

def main():
    os.system('clear')
    if subprocess.getoutput('whoami') != 'root':
        messages.error('\n\nThis program require super user privileges!\n\n')
        quit()
    if subprocess.getoutput('apache2 --version') == '/bin/sh: 1: apache: not found':
        messages.error('\n\nApache2 must be installed to run this program!\n\n')
        quit()
    os.system('clear')
    header.show()
    menu.show()
    option = input("Your NUMBER option: ")

    if not option.isnumeric():
        main()
    option = int(option)

    if(option == 1):
        vhost.list()
    elif(option == 2):
        vhost.new()
    elif(option == 3):
        vhost.edit()
    elif(option == 4):
        vhost.delete()
    elif(option == 6):
        quit()
    else:
        main()
    os.system('clear')
    main()
main()
