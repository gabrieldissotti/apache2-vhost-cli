# encoding:utf-8
#!/usr/bin/env python3
# for: Linux(Debian distros)
# Developed by: Gabriel Dissotti
from termcolor import colored
# Variables
text = """ 1 - List Virtual Hosts \t4 - Delete a Virtual Host
 2 - New Virtual Host   \t6 - Exit
 3 - Edit a Virtual Host"""
div = '-=-' * 21

# Colors
text = colored(text , 'white', attrs=['blink'])
div = colored(div, 'yellow', attrs=['blink'])

def show():
    print(text)
    print(div)
