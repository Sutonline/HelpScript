# ! -*- coding:utf-8 -*-
import os
import subprocess
import time
import yaml

# Load configuration from yaml file
f = open(os.path.dirname(os.path.abspath(__file__)) + '/config.yaml')
config = yaml.load(f)

# Settings
USERNAME = config['username']
PASSWORD = config['password']
HOSTNAME = config['hostname']
PORT = config['port']
BACK_DIR = config['back_dir']
FILESTAMP = time.strftime('%Y-%m-%d')


# 进入目录
def change_directory(directory):
    if directory_exists(directory) is False:
        os.makedirs(directory)
    os.chdir(directory)


# 目录是否存在
def directory_exists(directory):
    return os.path.isdir(directory)


# Create or change current directory to user's specific folder
if BACK_DIR:
    change_directory(BACK_DIR)

# Loop each selected database, dump it and upload to ftp
for database in config['databases']:
    filename = "%s/%s-%s.sql" % (BACK_DIR, database, FILESTAMP)
    subprocess.run(
        "mysqldump -h %s -P %s -u %s -p%s -B %s > %s" % (HOSTNAME, PORT, USERNAME, PASSWORD, database, filename),
        shell=True)