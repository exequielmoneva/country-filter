import random
import unittest

import pytest

from app import app
from services.dataset_service import DatasetService


class MyTestCase(unittest.TestCase):
    def test_query_param_ok(self):
        with app.app_context():
            number = random.uniform(0, 176075)
            value = {'satisfaction_index': number}
            result = DatasetService().filter_service(value)
            assert result is not None
            assert result.status_code == 200

    def test_query_param_not_number(self):
        with pytest.raises(Exception) as e:
            value = {'satisfaction_index': 'broken'}
            DatasetService().filter_service(value)
            assert str(e.value) == 'satisfaction_index parameter must be a number'
            assert e is not None

    def test_query_param_smaller_than_zero(self):
        with pytest.raises(Exception) as e:
            value = {'satisfaction_index': -1}
            DatasetService().filter_service(value)
            assert str(e.value) == 'satisfaction_index parameter must be equal or greater than 0'
            assert e is not None

    def test_query_param_not_supplied(self):
        with pytest.raises(Exception) as e:
            value = {'wrong_parameter': -1}
            DatasetService().filter_service(value)
            assert str(e.value) == 'satisfaction_index parameter is required'
            assert e is not None

    def test_retrieve_list_of_countries(self):
        value = random.uniform(0, 176075)
        result = DatasetService().pd_service(value)

        assert result is not None
        assert len(result) > 0
        assert result[0]['Value'] > value
        assert result[-1]['Value'] > value

    def test_retrieve_empty_list(self):
        value = 1000000
        result = DatasetService().pd_service(value)

        assert result is not None
        assert len(result) == 0


if __name__ == '__main__':
    unittest.main()
