from flask import Flask, request, jsonify

from schemas.schemas import CountrySchema
from services.dataset_service import DatasetService

app = Flask(__name__)
preprocessing = DatasetService()
schema = CountrySchema(many=True)


@app.route('/')
def hello_world():
    return 'API is running'


@app.route('/country', methods=['POST'])
def country_filter():
    value = float(request.json.get("value"))
    countries = preprocessing.pd_service(value)
    sep = schema.dump(countries)
    return jsonify(schema.dump(countries))


if __name__ == '__main__':
    app.run()
