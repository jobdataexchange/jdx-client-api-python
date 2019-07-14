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


class PreviewFields(object):
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
        'field': 'str',
        'paragraph_number': 'int'
    }

    attribute_map = {
        'field': 'field',
        'paragraph_number': 'paragraph_number'
    }

    def __init__(self, field=None, paragraph_number=None):  # noqa: E501
        """PreviewFields - a model defined in OpenAPI"""  # noqa: E501

        self._field = None
        self._paragraph_number = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if paragraph_number is not None:
            self.paragraph_number = paragraph_number

    @property
    def field(self):
        """Gets the field of this PreviewFields.  # noqa: E501


        :return: The field of this PreviewFields.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this PreviewFields.


        :param field: The field of this PreviewFields.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def paragraph_number(self):
        """Gets the paragraph_number of this PreviewFields.  # noqa: E501


        :return: The paragraph_number of this PreviewFields.  # noqa: E501
        :rtype: int
        """
        return self._paragraph_number

    @paragraph_number.setter
    def paragraph_number(self, paragraph_number):
        """Sets the paragraph_number of this PreviewFields.


        :param paragraph_number: The paragraph_number of this PreviewFields.  # noqa: E501
        :type: int
        """

        self._paragraph_number = paragraph_number

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
        if not isinstance(other, PreviewFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
