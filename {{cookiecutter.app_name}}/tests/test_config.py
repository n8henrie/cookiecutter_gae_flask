import sys

sys.path.append('/path/to/gae_pathfix/dir/')
import gae_pathfix

from {{cookiecutter.app_name}} import app
print(app.config['ALLOWED_EXTENSIONS'])
