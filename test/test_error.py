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
from bikes_api.models.error import Error  # noqa: E501
from bikes_api.rest import ApiException


class TestError(unittest.TestCase):
    """Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testError(self):
        """Test Error"""
        # FIXME: construct object with mandatory attributes with example values
        # model = bikes_api.models.error.Error()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
