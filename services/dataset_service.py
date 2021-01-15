import pandas as pd
from flask import make_response, jsonify

from schemas.schemas import CountrySchema

schema = CountrySchema(many=True)


class DatasetService:
    def __init__(self):
        self.dataset = pd.read_csv('countries.csv').fillna("")

    def filter_service(self, query_params):
        """
        validations over the query params before filtering
        :param query_params: dict containing the query params
        :return: final JSON response
        """
        try:
            if 'satisfaction_index' not in query_params.keys():
                return make_response(jsonify(error="satisfaction_index parameter is required"), 400)
            elif float(query_params.get('satisfaction_index')) < 0:
                return make_response(
                    jsonify(error='satisfaction_index parameter must be equal or greater than 0'), 400
                )
            countries = self.pd_service(
                float(query_params.get('satisfaction_index'))
            )
            return make_response(jsonify({"countries": schema.dump(countries)}), 200)
        except ValueError:
            return make_response(jsonify(error='satisfaction_index parameter must be a number'), 400)

    def pd_service(self, value: float) -> list:
        """
        filters all countries listed in the dataset by Value > input value
        value: Int or float value
        return: list of dictionaries
        """
        res = self.dataset.loc[
            (self.dataset.Inequality == 'Total') & (self.dataset['Value'] > value)
            ]
        return res.to_dict('records')
