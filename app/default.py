import os
import re
import time
import json
import socket
import shutil
from .app import *


def check_hostname(hostname):
    return True if re.match(r'([a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+)', hostname) else False

def convert_hostnames(file_path):
    with open(file_path, 'r+') as json_file:
        data = json.loads(json_file.read())
        data_accounts = data['accounts']
        length, loop, timeout = 0, 0, 0

        for name, value in data_accounts.items():
            for i in range(len(value)):
                if check_hostname(data_accounts[name][i]['hostname']) == True:
                    length += 1

        for name, value in data_accounts.items():
            for i in range(len(value)):
                account = data_accounts[name][i]
                if check_hostname(account['hostname']) == False:
                    continue
                try:
                    if timeout == 3: break
                    log_replace('[{}/{}] Converting hostnames'.format(app_format(loop+1, align='>', width=len(str(length)), chars='0'), length), time=True, status='INFO', status_color='[Y1]')
                    host = ''
                    host = socket.gethostbyname(account['hostname'])
                    if not host:
                        raise socket.gaierror
                    elif host != account['host']:
                        log('{:.<19} [Y1]{:.<23} {}'.format((account['host'] if account['host'] else '(empty)')+' ', host+' [G1]', account['hostname']), status='INFO', status_color='[G1]')
                        data_accounts[name][i]['host'] = host
                        timeout = 0
                except socket.gaierror:
                    log('[{}/{}] Converting hostnames error ({})'.format(app_format(timeout+1, align='>', width=len(str(length)), chars='0'), app_format('3', align='>', width=len(str(length)), chars='0'), account['hostname']), status='INFO', status_color='[R1]')
                    timeout = timeout + 1
                finally:
                    loop = loop + 1

        json_file.seek(0)
        json.dump(data, json_file, indent=2)
        json_file.truncate()

    return data_accounts

def generate_accounts(data_accounts, data_authentications=None):
    data_authentications = json.loads(open(real_path('/../database/authentications.json')).read())['authentications'] if data_authentications is None else data_authentications

    accounts = []

    for i in range(len(data_authentications)):
        for name in data_accounts:
            for x in range(len(data_accounts[name])):
                account = data_accounts[name][x]
                if not account: continue
                account['hostname'] = account['hostname'].lstrip('#')
                if check_hostname(account['hostname']) == False:
                    continue
                accounts.append({
                    'name': name,
                    'host': account['host'],
                    'hostname': account['hostname'],
                    'username': account['username'].replace('{username}', data_authentications[i]['username']),
                    'password': account['password'].replace('{password}', data_authentications[i]['password'])
                })

    accounts = [dict(tuples) for tuples in {tuple(dictionaries.items()) for dictionaries in accounts}]

    return accounts

def get_file_names(value = 'all'):
    file_names = []

    if value == 'all':
        file_names = [
            'config/config.json',
            'config/proxies.txt',
            'config/payload.txt',
            'config/server-name-indication.txt',
            'database/accounts.json',
            'database/authentications.json',
            'database/servers.json'
        ]
    elif value == 'database':
        file_names = [
            'database/accounts.json',
            'database/authentications.json',
            'database/servers.json'
        ]

    return file_names

def reset_to_default_settings():
    for file_name in get_file_names('all'):
        try:
            os.remove(real_path('/../' + file_name))
        except FileNotFoundError: pass

    default_settings()

def reset_database():
    for file_name in get_file_names('database'):
        try:
            os.remove(real_path('/../' + file_name))
        except FileNotFoundError: pass

    default_settings()

def default_settings():
    for file_name in get_file_names('all'):
        try:
            open(real_path('/../' + file_name))
        except FileNotFoundError:
            shutil.copyfile(real_path('/default/' + file_name), real_path('/../' + file_name))

def json_error(file):
    value = 'Exception: {} \n\n'.format(' ' * 24)                           + \
            '   File {} Error! \n'.format(file).replace('/app/../', '/')    + \
            '   Run reset.py first or fixing by your-self. \n'              + \
            '   Good-luck! \n'

    log(value, status_color='[R1]')

def autoload():
    default_settings()

autoload()
