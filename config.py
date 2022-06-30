import os
_basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
try:
    from local_config import *
except ImportError:
    pass
