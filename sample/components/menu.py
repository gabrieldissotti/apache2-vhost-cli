# encoding:utf-8
#!/usr/bin/env python3
# for: Linux(Debian distros)
# Developed by: Gabriel Dissotti
from termcolor import colored
# Variables
text = """ 1 - List \t\t\t\t\t    4 - Delete
 
 2 - New

 3 - Edit \t\t\t\t\t      6 - Exit
 """
div = '-=-' * 21

# Colors
text = colored(text , 'white', attrs=['blink'])
div = colored(div, 'yellow', attrs=['blink'])

def show():
    print(text)
    print(div)
