
def register_blueprints(app, blueprints):
    r"""Registers blueprints.
    Args:
        app: flask app.
        tokens: API blueprints.
    """ 
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
