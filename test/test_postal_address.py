# coding: utf-8

"""
    JDX reference application API

    This is a collection of schemas and endpoints for the various JDX, Concentric Sky facing REST endpoints, the schemas define an API contract of sorts between the request and response expectations of the JDX reference application. This API is to be mutually developed by Concentric Sky and BrightHive.  # noqa: E501

    The version of the OpenAPI document: 0.0.10
    Contact: engineering@brighthive.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.models.postal_address import PostalAddress  # noqa: E501
from openapi_client.rest import ApiException


class TestPostalAddress(unittest.TestCase):
    """PostalAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPostalAddress(self):
        """Test PostalAddress"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openapi_client.models.postal_address.PostalAddress()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
