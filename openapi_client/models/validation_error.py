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


class ValidationError(object):
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
        'message': 'str',
        'status_code': 'int',
        'validation_errors': 'list[ValidationErrorValidationErrors]'
    }

    attribute_map = {
        'message': 'message',
        'status_code': 'statusCode',
        'validation_errors': 'validationErrors'
    }

    def __init__(self, message=None, status_code=None, validation_errors=None):  # noqa: E501
        """ValidationError - a model defined in OpenAPI"""  # noqa: E501

        self._message = None
        self._status_code = None
        self._validation_errors = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def message(self):
        """Gets the message of this ValidationError.  # noqa: E501


        :return: The message of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationError.


        :param message: The message of this ValidationError.  # noqa: E501
        :type: str
        """
        if message is not None and len(message) > 1024:
            raise ValueError("Invalid value for `message`, length must be less than or equal to `1024`")  # noqa: E501

        self._message = message

    @property
    def status_code(self):
        """Gets the status_code of this ValidationError.  # noqa: E501

        A code identifying the message response. A code of `1` indicates success.  # noqa: E501

        :return: The status_code of this ValidationError.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ValidationError.

        A code identifying the message response. A code of `1` indicates success.  # noqa: E501

        :param status_code: The status_code of this ValidationError.  # noqa: E501
        :type: int
        """
        if status_code is not None and status_code > 9999:  # noqa: E501
            raise ValueError("Invalid value for `status_code`, must be a value less than or equal to `9999`")  # noqa: E501
        if status_code is not None and status_code < -1:  # noqa: E501
            raise ValueError("Invalid value for `status_code`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._status_code = status_code

    @property
    def validation_errors(self):
        """Gets the validation_errors of this ValidationError.  # noqa: E501


        :return: The validation_errors of this ValidationError.  # noqa: E501
        :rtype: list[ValidationErrorValidationErrors]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this ValidationError.


        :param validation_errors: The validation_errors of this ValidationError.  # noqa: E501
        :type: list[ValidationErrorValidationErrors]
        """

        self._validation_errors = validation_errors

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
        if not isinstance(other, ValidationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other