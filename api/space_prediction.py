import flask
import os

from flask import jsonify, request, render_template

from model.space_predictor import SpacePredictor
from config.common import app_config


# Initialize SpacePredictor instance
model = SpacePredictor(os.path.join(app_config['APP_ROOT_PATH'], 
                                    app_config['VOCABULARY_PATH']),
                       app_config['PUNCTUATION'])


routes = flask.Blueprint('predict', __name__)


@routes.route('/predict_spaces', methods=['POST'])
def predict_spaces():
    r"""Primary endpoint. Receives a request with a damaged string 
        and returns a json with reconstructed string and indexes 
        of missed spaces.
    """
    json_request = request.get_json(force=True)
    
    s = json_request['text']

    result = model.predict(s)
    
    return jsonify(result)


@routes.route('/predict_homepage', methods=['POST'])
def predict_homepage():
    r"""Updates the homepage after the user submits a string.
    """
    s = request.form['text']

    predictions = model.predict(s)

    # Prepare message with predictions
    predicted_text = predictions['text']
    space_indices = [str(index) for index in predictions['missed_spaces']]
    space_indices = ', '.join(space_indices)

    message = "Reconstructed text: \n{}\n\nMissed spaces positions: \n{}".format(predicted_text, space_indices)
    
    return render_template('home.html', message = message)
