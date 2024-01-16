import os

from flask import Flask
from flask_cors import CORS

web_client_url = "http://localhost:3000"

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app, resources={r"*": {"origins": web_client_url + '/*'}})

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.view import GetYeastGrowthImage, RecordYeastGrowth, GetMeasurementFileNames
    app.register_blueprint(GetYeastGrowthImage.bp)
    app.register_blueprint(RecordYeastGrowth.bp)
    app.register_blueprint(GetMeasurementFileNames.bp)

    return app

