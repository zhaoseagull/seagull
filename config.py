import os
basedir=os.path.abspath(os.path.dirname(__file__))
dburi='mysql://mysql:Lufax@192.168.122.191/zw'
dbrepo=os.path.join(basedir,'db_repository')
CSRF=True
SECRTY_KEY='you-will-never-guess'


