#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to your web servers, using the
functions do_pack and do_deploy
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists

env.hosts = ['54.88.187.237', '52.91.121.185']


def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder"""
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    return 'versions/{}'.format(archive) if create.succeeded else None


def do_deploy(archive_path):
    """Deploy the web_static archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_x = archive_path.split("/")[-1]
        exile = file_x.split(".")[0]
        path = '/data/web_static/releases/'
        # Upload the archive
        put(archive_path, '/tmp/')
        # Create the directory to extract the contents
        run('mkdir -p {}{}/'.format(path, exile))
        # Extract the contents of the archive
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_x, path, exile))
        # Remove the temporary archive
        run('rm /tmp/{}'.format(file_x))
        # Move the contents to the release directory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, exile))
        # Remove the web_static directory
        run('rm -rf {}/web_static'.format(path, exile))
        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link to the new version
        run('ln -s {}{}/ /data/web_static/current'.format(path, exile))

        print('New version deployed!')
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """Deploy the web_static content to the web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
