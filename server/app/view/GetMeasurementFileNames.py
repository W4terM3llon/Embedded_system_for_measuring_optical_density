import os

from flask import Blueprint, jsonify

from app.controller.HandleGetMeasurementFileNames import HandleGetMeasurementFileNames

bp = Blueprint('GetMeasurementFileNames', __name__, url_prefix="/api/v1/")


@bp.route('/measurementFileNames', methods=['GET'])
def GetMeasurementFileNames():
    print("GetMeasurementFileNames")
    return jsonify({'measurementFileNames': HandleGetMeasurementFileNames()}), 200
