import pandas as pd



class DatasetService:
    def __init__(self):
        self.dataset = pd.read_csv('countries.csv').fillna("")

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
