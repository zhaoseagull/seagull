#--coding:utf-8
from migrate.versioning import api
from config import dbrepo
from config import dburi


from app import db

import os.path

db.create_all()

if not os.path.exists(dbrepo):
    api.create(dbrepo,'database repository')
    api.version_control(dburi,dbrepo)
else:
    api.version_control(dburi,dbrepo,api.version(dbrepo))
