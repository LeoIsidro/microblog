import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'postgresql://postgres:Princesa4@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False