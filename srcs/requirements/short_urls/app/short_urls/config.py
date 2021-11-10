from os import environ

SECRET_KEY = 'dev'
DATABASE_SERVER = 'mariadb'
DATABASE_USER = 'short_urls'
DATABASE_PASSWORD = environ.get('MYSQL_SHORT_URLS_PASSWORD', '')
DATABASE_DB = 'short_urls'
SQLALCHEMY_TRACK_MODIFICATIONS = False
