import flask

from utils.flask import register_blueprints
from config.common import app_config
from api import routes

# Application configuration
app = flask.Flask(__name__,
                  static_url_path='',
                  static_folder='static',
                  template_folder='templates')

# Register blueprints
register_blueprints(app, routes)

# Run application
if __name__ == '__main__':
    app.run(host=app_config.get('FLASK_HOST', '0.0.0.0'),
            port=app_config.get('FLASK_PORT', 5100),
            debug=app_config.get('FLASK_DEBUG', False))
