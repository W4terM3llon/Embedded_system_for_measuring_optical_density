from flask import Blueprint, send_file, make_response

from app.controller.GetYeastGrowthImageHandler import HandleGetYeastGrowthImage

bp = Blueprint('GetYeastGrowthImage', __name__, url_prefix="/api/v1/")

# a simple page that says hello
@bp.route('/yeastGrowthPlot', methods=['GET'])
def GetYeastGrowthImage():
    print("GetYeastGrowthImage")
    graphAsBytes = HandleGetYeastGrowthImage()
    response = make_response(graphAsBytes)
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='eastGrowth.png')
    return response, 200