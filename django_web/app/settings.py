import os

#IS_PRODUCTION = os.environ.get('IS_PRODUCTION')
IS_PRODUCTION = False

if IS_PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *