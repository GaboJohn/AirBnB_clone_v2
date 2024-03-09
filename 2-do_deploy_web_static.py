#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import env, run, put
from os.path import exists

env.hosts = ['54.88.187.237', '52.91.121.185']

def do_deploy(archive_path):
    """Deploy archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        file_x = archive_path.split("/")[-1]
        exile = file_x.split(".")[0]  # Fix the variable name
        path = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, exile))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_x, path, exile))  # Remove extra '/'
        run('rm /tmp/{}'.format(file_x))  # Remove extra '/'
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, exile))
        # Remove the web_static directory
        run('rm -rf {0}{1}/web_static'.format(path, exile))
        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link to the new version
        run('ln -s {0}{1}/ /data/web_static/current'.format(path, exile))
        print('New version deployed!')
        return True
    except:
        return False
