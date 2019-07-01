# coding: utf-8

"""
    JDX reference application API

    This is a collection of schemas and endpoints for the various JDX, Concentric Sky facing REST endpoints, the schemas define an API contract of sorts between the request and response expectations of the JDX reference application. This API is to be mutually developed by Concentric Sky and BrightHive.  # noqa: E501

    The version of the OpenAPI document: 0.0.9
    Contact: engineering@brighthive.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class JobDescriptionContextRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pipeline_id': 'str',
        'primary_economic_activity': 'str',
        'job_location': 'Place',
        'occupation_category': 'AnnotatedDefinedTerm',
        'industry_category': 'AnnotatedDefinedTerm'
    }

    attribute_map = {
        'pipeline_id': 'pipelineID',
        'primary_economic_activity': 'primaryEconomicActivity',
        'job_location': 'jobLocation',
        'occupation_category': 'occupationCategory',
        'industry_category': 'industryCategory'
    }

    def __init__(self, pipeline_id=None, primary_economic_activity=None, job_location=None, occupation_category=None, industry_category=None):  # noqa: E501
        """JobDescriptionContextRequest - a model defined in OpenAPI"""  # noqa: E501

        self._pipeline_id = None
        self._primary_economic_activity = None
        self._job_location = None
        self._occupation_category = None
        self._industry_category = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if primary_economic_activity is not None:
            self.primary_economic_activity = primary_economic_activity
        if job_location is not None:
            self.job_location = job_location
        if occupation_category is not None:
            self.occupation_category = occupation_category
        if industry_category is not None:
            self.industry_category = industry_category

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this JobDescriptionContextRequest.  # noqa: E501

        An identifier for this jdx reference application _session_ of converting a raw job description. On first request this is ignored.  # noqa: E501

        :return: The pipeline_id of this JobDescriptionContextRequest.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this JobDescriptionContextRequest.

        An identifier for this jdx reference application _session_ of converting a raw job description. On first request this is ignored.  # noqa: E501

        :param pipeline_id: The pipeline_id of this JobDescriptionContextRequest.  # noqa: E501
        :type: str
        """

        self._pipeline_id = pipeline_id

    @property
    def primary_economic_activity(self):
        """Gets the primary_economic_activity of this JobDescriptionContextRequest.  # noqa: E501


        :return: The primary_economic_activity of this JobDescriptionContextRequest.  # noqa: E501
        :rtype: str
        """
        return self._primary_economic_activity

    @primary_economic_activity.setter
    def primary_economic_activity(self, primary_economic_activity):
        """Sets the primary_economic_activity of this JobDescriptionContextRequest.


        :param primary_economic_activity: The primary_economic_activity of this JobDescriptionContextRequest.  # noqa: E501
        :type: str
        """
        if primary_economic_activity is not None and len(primary_economic_activity) > 1024:
            raise ValueError("Invalid value for `primary_economic_activity`, length must be less than or equal to `1024`")  # noqa: E501

        self._primary_economic_activity = primary_economic_activity

    @property
    def job_location(self):
        """Gets the job_location of this JobDescriptionContextRequest.  # noqa: E501


        :return: The job_location of this JobDescriptionContextRequest.  # noqa: E501
        :rtype: Place
        """
        return self._job_location

    @job_location.setter
    def job_location(self, job_location):
        """Sets the job_location of this JobDescriptionContextRequest.


        :param job_location: The job_location of this JobDescriptionContextRequest.  # noqa: E501
        :type: Place
        """

        self._job_location = job_location

    @property
    def occupation_category(self):
        """Gets the occupation_category of this JobDescriptionContextRequest.  # noqa: E501


        :return: The occupation_category of this JobDescriptionContextRequest.  # noqa: E501
        :rtype: AnnotatedDefinedTerm
        """
        return self._occupation_category

    @occupation_category.setter
    def occupation_category(self, occupation_category):
        """Sets the occupation_category of this JobDescriptionContextRequest.


        :param occupation_category: The occupation_category of this JobDescriptionContextRequest.  # noqa: E501
        :type: AnnotatedDefinedTerm
        """

        self._occupation_category = occupation_category

    @property
    def industry_category(self):
        """Gets the industry_category of this JobDescriptionContextRequest.  # noqa: E501


        :return: The industry_category of this JobDescriptionContextRequest.  # noqa: E501
        :rtype: AnnotatedDefinedTerm
        """
        return self._industry_category

    @industry_category.setter
    def industry_category(self, industry_category):
        """Sets the industry_category of this JobDescriptionContextRequest.


        :param industry_category: The industry_category of this JobDescriptionContextRequest.  # noqa: E501
        :type: AnnotatedDefinedTerm
        """

        self._industry_category = industry_category

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobDescriptionContextRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
