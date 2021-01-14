import unittest
import random

import pytest

from app import country_filter
from services.dataset_service import DatasetService


class MyTestCase(unittest.TestCase):
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
