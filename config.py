# Database configuration
import os

basedir = os.path.abspath(os.path.dirname(__file__))

## THE ELSE STATEMENT GETS THE DB ENVIRONMENT FOR THE HEROKU ENV

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') +
                               '?check_same_thread=False')
else
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Email Configuration
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_SENDER = 'admin@sellsnapshots.com'
MAIL_SUBJECT_PREFIX = '[SELL SNAP SHOTS] '
