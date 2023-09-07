#!/usr/bin/python3
"""
Fabric script that generates .tgz archive from contents of the web_static 
folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function that compresses directory
    Returns archive pass on access; None on fail
    """

    # set up datetime
    now = datetime.now()
    now = strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    # Create archive
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    # Check success
    if result.succeeded:
        return archive_path
    return None
