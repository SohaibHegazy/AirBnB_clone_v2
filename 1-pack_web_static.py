#!/usr/bin/python3
'''
a Fabric script that generates a .tgz archive from
the contents of the web_static folder
'''
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    if not os.path.exists("versions"):
        os.makedirs("versions")

    now = datetime.now()
    compress_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    compress_path = "versions/{}".format(compress_name)
    c = local("tar -cvzf {} web_static".format(compress_path), capture=True)

    if c.succeeded:
        return compress_path
    else:
        return None
