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


class FrameworkRecommendations(object):
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
        'value': 'float',
        'valid_until': 'datetime',
        'framework_data': 'FrameworkData'
    }

    attribute_map = {
        'value': 'value',
        'valid_until': 'validUntil',
        'framework_data': 'frameworkData'
    }

    def __init__(self, value=None, valid_until=None, framework_data=None):  # noqa: E501
        """FrameworkRecommendations - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._valid_until = None
        self._framework_data = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if valid_until is not None:
            self.valid_until = valid_until
        if framework_data is not None:
            self.framework_data = framework_data

    @property
    def value(self):
        """Gets the value of this FrameworkRecommendations.  # noqa: E501

        numeric score, higher is better  # noqa: E501

        :return: The value of this FrameworkRecommendations.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FrameworkRecommendations.

        numeric score, higher is better  # noqa: E501

        :param value: The value of this FrameworkRecommendations.  # noqa: E501
        :type: float
        """
        if value is not None and value < 0:  # noqa: E501
            raise ValueError("Invalid value for `value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._value = value

    @property
    def valid_until(self):
        """Gets the valid_until of this FrameworkRecommendations.  # noqa: E501

        A timestamp of the time up until this is valid  # noqa: E501

        :return: The valid_until of this FrameworkRecommendations.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this FrameworkRecommendations.

        A timestamp of the time up until this is valid  # noqa: E501

        :param valid_until: The valid_until of this FrameworkRecommendations.  # noqa: E501
        :type: datetime
        """

        self._valid_until = valid_until

    @property
    def framework_data(self):
        """Gets the framework_data of this FrameworkRecommendations.  # noqa: E501


        :return: The framework_data of this FrameworkRecommendations.  # noqa: E501
        :rtype: FrameworkData
        """
        return self._framework_data

    @framework_data.setter
    def framework_data(self, framework_data):
        """Sets the framework_data of this FrameworkRecommendations.


        :param framework_data: The framework_data of this FrameworkRecommendations.  # noqa: E501
        :type: FrameworkData
        """

        self._framework_data = framework_data

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
        if not isinstance(other, FrameworkRecommendations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
