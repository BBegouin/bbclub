# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

from BBClub.base_settings import *

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "z_=_tychz8m8k@4)kmzn(!=s9a-ao=g-@b7qutwmau@2qozlxs"
NEVERCACHE_KEY = "2f_)*3b6$*&7dpj%%^a(z8wpiq=gd&kya8@1)okiro#yv34d(d"

FRONT_DOMAIN = "localhost:5555"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "BBClub",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",   # Or an IP Address that your DB is hosted on
        "PORT": "3306",
    }
}

FACEBOOK_ADAPTER = "bbc_auth.tests.adapters.facebook_adapter"
#FACEBOOK_ADAPTER = "bbc_auth.views.adapters.facebook_adapter"


################
# APPLICATIONS #
################

INSTALLED_APPS += ('debug_toolbar',)

######################
# User Settings
######################

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
# ALLOWED_HOSTS = [""]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }
