import flask


routes = flask.Blueprint('healthcheck', __name__)


@routes.route('/healthcheck', methods=['GET'])
def healthcheck():
    r"""A Basic Health Endpoint. Returns a 200 status."""
    return flask.Response('pong', status=200)
