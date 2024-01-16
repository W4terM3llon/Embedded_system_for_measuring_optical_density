from flask import Blueprint, make_response, request, jsonify
from marshmallow import ValidationError, fields, Schema


from app.controller.GetYeastGrowthImageHandler import HandleGetYeastGrowthImage
from app.controller.HandleGetMeasurementFileNames import HandleGetMeasurementFileNames

bp = Blueprint('GetYeastGrowthImage', __name__, url_prefix="/api/v1/")

# a simple page that says hello
@bp.route('/yeastGrowthPlot', methods=['GET'])
def GetYeastGrowthImage():
    try:
        schema = GetYeastGrowthImageSchema().load(request.args)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if schema['id'] not in HandleGetMeasurementFileNames():
        return {'error': 'File name not found.'}, 400


    print("GetYeastGrowthImage")
    graphAsBytes = HandleGetYeastGrowthImage(schema['id'])
    response = make_response(graphAsBytes)
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename=f"Yeast growth (measurement no. {schema['id']}).png")
    return response, 200

class GetYeastGrowthImageSchema(Schema):
    id = fields.String(required=True)