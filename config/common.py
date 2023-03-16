
import os

"""
Basic configuration.
"""
app_config = {
    # Common
    'TIMEZONE': 'UTC',
    'APP_ROOT_PATH': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),

    # Flask config
    'FLASK_HOST': '0.0.0.0',
    'FLASK_PORT': 5100,
    'FLASK_DEBUG': False,

    # Model config
    'VOCABULARY_PATH': "static/vocabulary/vocabulary_126k.txt.gz",
    'PUNCTUATION': {'.', ',', ':', ';', '!', '?'},   
}
