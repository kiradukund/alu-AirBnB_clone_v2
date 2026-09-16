#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers."""
from fabric.api import env
from datetime import datetime
import os

env.hosts = ['13.218.52.231', '3.87.7.134']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """Generate a tgz archive from the web_static folder.

    Returns:
        str: path to the archive if successful, None otherwise
    """
    from fabric.api import local
    local("mkdir -p versions")
    now = datetime.now()
    name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        now.year, str(now.month).zfill(2), str(now.day).zfill(2),
        str(now.hour).zfill(2), str(now.minute).zfill(2),
        str(now.second).zfill(2))
    result = local("tar -cvzf {} web_static".format(name))
    if result.failed:
        return None
    return name


def do_deploy(archive_path):
    """Distribute an archive to web servers.

    Args:
        archive_path (str): path to the archive to deploy

    Returns:
        bool: True if successful, False otherwise
    """
    from fabric.api import put, run
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


def deploy():
    """Create and distribute an archive to web servers.

    Returns:
        bool: True if successful, False otherwise
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
