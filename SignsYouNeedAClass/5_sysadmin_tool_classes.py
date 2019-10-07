"""System administration tool with Classes"""

import platform
import subprocess

class CommandBackend:

    ls_command = None
    ps_command = None
    tcp_command = None
    encoding = 'utf-8'

    def run_command(self, command):
        command_map = {'l': self.ls_command, 'p': self.ps_command, 'n': self.tcp_command}
        command_list = command_map.get(command)
        if not command_list:
            print(f'Operation not supported on this OS ({platform.system()}).')
            return
        print(subprocess.check_output(command_list).decode(self.encoding))

class DarwinBackend(CommandBackend):
    ls_command = ['ls']
    ps_command = ['ps', 'aux']
    tcp_command = ['netstat', '-t']

class LinuxBackend(CommandBackend):
    ls_command = ['ls']
    ps_command = ['ps', '-e']
    tcp_command = ['ss', '-t']

class WindowsBackend(CommandBackend):
    ls_command = ['dir']
    ps_command = ['tasklist']
    tcp_command = ['netstat', '/t']
    encoding = 'ascii'

backends = {'Windows': WindowsBackend, 'Linux': LinuxBackend, 'Darwin': DarwinBackend}
backend = backends.get(platform.system(), CommandBackend)()

while True:
    print('Select an operation:')
    print('    l - list files')
    print('    p - list processes')
    print('    n - list TCP network connections')
    print('    q - quit')
    selection = input('> ')
    if selection == 'q':
        break
    else:
        backend.run_command(selection)
