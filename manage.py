#!/usr/bin/env python
# coding: utf-8

from flask_script import Manager
import os
from app import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()