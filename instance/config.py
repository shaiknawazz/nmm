import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'p9Bv<qeqqwqwfsdgs#%$#$%T%$i01'
'''SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')'''

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')