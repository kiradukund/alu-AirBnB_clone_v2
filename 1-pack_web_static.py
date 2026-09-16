#!/usr/bin/python3
"""Fabric script that generates a tgz archive from web_static folder."""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generate a tgz archive from the web_static folder.

    Returns:
        str: path to the archive if successful, None otherwise
    """
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
