#!/usr/bin/python3
'''
a Fabric script that generates a .tgz archive from
the contents of the web_static folder
'''

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    '''
    function to archive the directory to tgz
    '''
    try:
        if not os.path.exists("versions"):
            local("mkdir -p versions")
        now = datetime.now()
        arch_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
        arch_path = "versions/{}".format(arch_name)
        local("tar -cvzf {} web_static".format(arch_path))
        return arch_path
    except Exception:
        return None
