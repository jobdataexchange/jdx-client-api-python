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
from openapi_client.api.default_api import DefaultApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_framework_recommendations_post(self):
        """Test case for framework_recommendations_post

        Get framework recommendations based on the uploaded job descripton and context.  # noqa: E501
        """
        pass

    def test_framework_selections_post(self):
        """Test case for framework_selections_post

        The user indicates what frameworks they selected  # noqa: E501
        """
        pass

    def test_get_scored_recommendations_post(self):
        """Test case for get_scored_recommendations_post

        [NOT IMPLEMENTED FOR 5/31 PROTOTYPE] Get a list of `scoredRecommendations` associated with the match table  # noqa: E501
        """
        pass

    def test_health_get(self):
        """Test case for health_get

        Health Check  # noqa: E501
        """
        pass

    def test_match_table_post(self):
        """Test case for match_table_post

        Get the match table associated with the provided `pipelineID`  # noqa: E501
        """
        pass

    def test_preview_post(self):
        """Test case for preview_post

        Get preview of job description with tagged matches.  # noqa: E501
        """
        pass

    def test_set_scored_recommendations_post(self):
        """Test case for set_scored_recommendations_post

        [NOT IMPLEMENTED FOR 5/31 PROTOTYPE] Obtain a recommendation for a specific user replacement  # noqa: E501
        """
        pass

    def test_upload_job_description_context_post(self):
        """Test case for upload_job_description_context_post

        Provide job description context (e.g metadata) on the job description  # noqa: E501
        """
        pass

    def test_upload_job_description_file_post(self):
        """Test case for upload_job_description_file_post

        Upload a raw job description file.  # noqa: E501
        """
        pass

    def test_user_actions_post(self):
        """Test case for user_actions_post

        Provide the user responses as a list of user actions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
