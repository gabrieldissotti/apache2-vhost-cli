# encoding:utf-8
#!/usr/bin/env python3
# Developed by: Gabriel Dissotti

from termcolor import colored


def process(message):
    return print(colored(message, 'red', attrs=['blink']))

def title(message):
    return print("{:=^90}".format(colored(message, 'green', attrs=['bold', 'blink'])))

def error(message):
    return print(colored(message, 'red', attrs=['blink', 'bold']))

def success(message):
    return print(colored(message, 'green', attrs=['blink']))

def info(message):
    return print(colored(message, 'blue', attrs=['blink']))

def question(message):
    return print(colored(message, 'cyan', attrs=['blink']))

def atention(message):
    return print(colored(message, 'yellow', attrs=['blink']))
