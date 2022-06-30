#!/usr/bin/env python
# coding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
import sys
from app import app, db
from app.models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()