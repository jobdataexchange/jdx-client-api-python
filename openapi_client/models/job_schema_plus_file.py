# coding: utf-8

"""
    JDX reference application API

    This is a collection of schemas and endpoints for the various JDX, Concentric Sky facing REST endpoints, the schemas define an API contract of sorts between the request and response expectations of the JDX reference application. This API is to be mutually developed by Concentric Sky and BrightHive.  # noqa: E501

    The version of the OpenAPI document: 0.0.14
    Contact: engineering@brighthive.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class JobSchemaPlusFile(object):
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
        'job_schema_plus_file': 'str'
    }

    attribute_map = {
        'job_schema_plus_file': 'jobSchemaPlusFile'
    }

    def __init__(self, job_schema_plus_file=None):  # noqa: E501
        """JobSchemaPlusFile - a model defined in OpenAPI"""  # noqa: E501

        self._job_schema_plus_file = None
        self.discriminator = None

        if job_schema_plus_file is not None:
            self.job_schema_plus_file = job_schema_plus_file

    @property
    def job_schema_plus_file(self):
        """Gets the job_schema_plus_file of this JobSchemaPlusFile.  # noqa: E501


        :return: The job_schema_plus_file of this JobSchemaPlusFile.  # noqa: E501
        :rtype: str
        """
        return self._job_schema_plus_file

    @job_schema_plus_file.setter
    def job_schema_plus_file(self, job_schema_plus_file):
        """Sets the job_schema_plus_file of this JobSchemaPlusFile.


        :param job_schema_plus_file: The job_schema_plus_file of this JobSchemaPlusFile.  # noqa: E501
        :type: str
        """

        self._job_schema_plus_file = job_schema_plus_file

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
        if not isinstance(other, JobSchemaPlusFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
