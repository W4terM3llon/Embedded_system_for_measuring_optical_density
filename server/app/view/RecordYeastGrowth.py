from flask import jsonify, Blueprint, request
from marshmallow import ValidationError, fields, Schema

from app.controller.RecordYeastGrowthHandler import HandleRecordYeastGrowth

bp = Blueprint('RecordYeastGrowthData', __name__, url_prefix="/api/v1/")


@bp.route('/hello', methods=['POST'])
def RecordYeastGrowthData():
    print("RecordYeastGrowthData")
    try:
        requestBodyData = RecordYeastGrowthSchema().load(request.get_json(force=True))
    except ValidationError as err:
        return jsonify(err.messages), 400

    HandleRecordYeastGrowth(requestBodyData["growthIntensity"], requestBodyData["dateTime"])

    return {'message': 'success'}, 200

class RecordYeastGrowthSchema(Schema):
    growthIntensity = fields.Integer(required=True)
    dateTime = fields.DateTime(required=True)
