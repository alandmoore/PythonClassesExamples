"""System administration tool without Classes"""

import platform
import subprocess

operating_system = platform.system()

def list_files():
    if operating_system in ('Linux', 'Darwin'):
        print(subprocess.check_output(['ls']).decode('utf-8'))
    elif operating_system == 'Windows':
        print(subprocess.check_output(['dir']).decode('ascii'))
    else:
        print('Unknown OS; operation not supported.')

def list_processes():
    if operating_system == 'Linux':
        print(subprocess.check_output(['ps', '-e']).decode('utf-8'))
    elif operating_system == 'Darwin':
        print(subprocess.check_output(['ps', 'aux']).decode('utf-8'))
    elif operating_system == 'Windows':
        print(subprocess.check_output(['tasklist']).decode('ascii'))
    else:
        print('Unknown OS; operation not supported')

def list_tcp_network():
    if operating_system == 'Linux':
        print(subprocess.check_output(['ss', '-t']).decode('utf-8'))
    elif operating_system == 'Darwin':
        print(subprocess.check_output(['netstat', '-t']).decode('utf-8'))
    elif operating_system == 'Windows':
        print(subprocess.check_output(['netstat', '/t']).decode('ascii'))
    else:
        print('Unknown OS; operation not supported')

callbacks = {'l': list_files, 'p': list_processes, 'n': list_tcp_network}

while True:
    print('Select an operation:')
    print('    l - list files')
    print('    p - list processes')
    print('    n - list TCP network connections')
    print('    q - quit')
    selection = input('> ')
    if selection == 'q':
        break
    callback = callbacks.get(selection)
    if callback:
        callback()
    else:
        print('Invalid operation')
