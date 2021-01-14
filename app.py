from flask import Flask, request, jsonify, make_response, send_from_directory

from schemas.schemas import CountrySchema
from services.dataset_service import DatasetService
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
preprocessing = DatasetService()
schema = CountrySchema(many=True)
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml/'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "countryFilter"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/')
def index():
    return 'API is running'


@app.route('/country/<satisfaction_index>')
def country_filter(satisfaction_index):
    try:
        countries = preprocessing.pd_service(float(satisfaction_index))
        return make_response(jsonify({"countries": schema.dump(countries)}), 200)
    except ValueError as e:
        return make_response(jsonify({'error': str(e)}), 400)


if __name__ == '__main__':
    app.run()
