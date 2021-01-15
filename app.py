from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint

from schemas.schemas import CountrySchema
from services.dataset_service import DatasetService

app = Flask(__name__)
preprocessing = DatasetService()
schema = CountrySchema(many=True)
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

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


@app.route('/country')
def country_filter():
    query_params = request.args.to_dict()
    return preprocessing.filter_service(query_params)


if __name__ == '__main__':
    app.run()
