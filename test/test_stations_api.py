# coding: utf-8

"""
    JCDecaux API

    JCDecaux API for retrieving dynamic data about bike stations and contracts  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: alesanchezmedina@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from lambda import bikes_api
from bikes_api.api.stations_api import StationsApi  # noqa: E501
from bikes_api.rest import ApiException


class TestStationsApi(unittest.TestCase):
    """StationsApi unit test stubs"""

    def setUp(self):
        self.api = bikes_api.api.stations_api.StationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_stations_get(self):
        """Test case for stations_get

        Gets the list of stations  # noqa: E501
        """
        pass

    def test_stations_station_number_get(self):
        """Test case for stations_station_number_get

        Gets a specific station  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
