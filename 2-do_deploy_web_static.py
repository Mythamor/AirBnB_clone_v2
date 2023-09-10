#!/usr/bin/python3
"""
Deploys to the server from local machine
"""

from fabric.api import env, put, run
import os

env.hosts = ['52.91.125.119', '52.86.30.214']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """
    Creates and distributes an archive to your web servers.
    """
    try:
        # Check if file path exists
        if not os.path.exists(archive_path):
            return False

        # Upload archive to tmp directory of web server
        put(archive_path, '/tmp')

        # Extract the version from the archive filename
        version = archive_path.split('/')[-1][:-4]

        # Create a directory for the new release
        release_path = '/data/web_static/releases/{}'.format(version)
        run('sudo mkdir -p {}'.format(release_path))

        # Uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(version, release_path))
        run('sudo rm /tmp/{}.tgz'.format(version))

        # Move files to web_static
        run('sudo mv {}/web_static/* {}/'.format(release_path, release_path))

        # Remove the old symbolic link
        current_path = '/data/web_static/current'
        run('sudo rm -rf {}'.format(current_path))

        # Create a new symbolic link
        run('sudo ln -s {} {}'.format(release_path, current_path))

        return True

    except Exception as e:
        print("Error:", str(e))
        return False

