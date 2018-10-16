# encoding:utf-8
#!/usr/bin/env python3
# for: Linux(Debian distros)
# Developed by: Gabriel Dissotti
from termcolor import colored
from random import choice
# Variables
ver = 'v0.1'
title = 'Virtual Hosts '
div = ' # ' * 21
div_color = choice(['red','green','yellow','blue','magenta','cyan'])

# Colors
title = colored(title , 'white', attrs=['blink', 'bold'])
div = colored(div, div_color, attrs=['blink', 'reverse'])
ver = colored(ver, 'green', attrs=['blink', 'bold'])
def show():
    # Program
    print(div)
    print("{0:^95}".format(title+ver))
    print(div)
    print("{0:^60}".format("Menu"))
    print('\n')
