# -*- coding:utf8 -*-
from flask_script import Manager

from chungoba import create_app, db
from chungoba.models import *

app = create_app('ProductionConfig')

manager = Manager(app)

@manager.command
def runserver():
    """Run Test Server"""
    app.run(host='0.0.0.0')

@manager.command
def debug():
    app.config.from_object('chungoba.config.DevelopmentConfig')
    app.run(host='0.0.0.0')

@manager.command
def init_db():
    """Create Database Tables"""
    db.create_all()

@manager.command
def recreate_db():
    """Drop Database Tables and Create Database Tables"""
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    manager.run()