from flask import jsonify, Blueprint, request
from marshmallow import ValidationError, fields, Schema

from app.controller.RecordYeastGrowthHandler import HandleRecordYeastGrowth

bp = Blueprint('RecordYeastGrowthData', __name__, url_prefix="/api/v1/")


@bp.route('/yeastGrowthReadings', methods=['POST'])
def RecordYeastGrowthData():
    print("RecordYeastGrowthData")
    try:
        requestBodyData = RecordYeastGrowthSchema().load(request.get_json(force=True))
    except ValidationError as err:
        return jsonify(err.messages), 400

    HandleRecordYeastGrowth(requestBodyData["fileName"], requestBodyData["OD600"], requestBodyData["time"])

    return {'message': 'success'}, 200

class RecordYeastGrowthSchema(Schema):
    fileName = fields.String(required=True)
    OD600 = fields.Float(required=True)
    time = fields.Integer(required=True)
