#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers."""
from fabric.api import env, put, run
import os

env.hosts = ['13.218.52.231', '3.87.7.134']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Distribute an archive to web servers.

    Args:
        archive_path (str): path to the archive to deploy

    Returns:
        bool: True if successful, False otherwise
    """
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split('/')[-1]
        name = filename.split('.')[0]
        release = "/data/web_static/releases/{}/".format(name)

        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(release))
        run("tar -xzf /tmp/{} -C {}".format(filename, release))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(release, release))
        run("rm -rf {}web_static".format(release))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release))
        print("New version deployed!")
        return True
    except Exception:
        return False
