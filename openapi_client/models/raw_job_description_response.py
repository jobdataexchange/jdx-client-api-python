# coding: utf-8

"""
    JDX reference application API

    This is a collection of schemas and endpoints for the various JDX, Concentric Sky facing REST endpoints, the schemas define an API contract of sorts between the request and response expectations of the JDX reference application. This API is to be mutually developed by Concentric Sky and BrightHive.  # noqa: E501

    The version of the OpenAPI document: 0.0.10
    Contact: engineering@brighthive.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RawJobDescriptionResponse(object):
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
        'timestamp': 'datetime',
        'file_text': 'str',
        'converted_length': 'int'
    }

    attribute_map = {
        'pipeline_id': 'pipelineID',
        'timestamp': 'timestamp',
        'file_text': 'fileText',
        'converted_length': 'convertedLength'
    }

    def __init__(self, pipeline_id=None, timestamp=None, file_text=None, converted_length=None):  # noqa: E501
        """RawJobDescriptionResponse - a model defined in OpenAPI"""  # noqa: E501

        self._pipeline_id = None
        self._timestamp = None
        self._file_text = None
        self._converted_length = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if timestamp is not None:
            self.timestamp = timestamp
        if file_text is not None:
            self.file_text = file_text
        if converted_length is not None:
            self.converted_length = converted_length

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this RawJobDescriptionResponse.  # noqa: E501

        An identifier for this jdx reference application session of converting a raw job description  # noqa: E501

        :return: The pipeline_id of this RawJobDescriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this RawJobDescriptionResponse.

        An identifier for this jdx reference application session of converting a raw job description  # noqa: E501

        :param pipeline_id: The pipeline_id of this RawJobDescriptionResponse.  # noqa: E501
        :type: str
        """

        self._pipeline_id = pipeline_id

    @property
    def timestamp(self):
        """Gets the timestamp of this RawJobDescriptionResponse.  # noqa: E501

        A timestamp of when this response was generated  # noqa: E501

        :return: The timestamp of this RawJobDescriptionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this RawJobDescriptionResponse.

        A timestamp of when this response was generated  # noqa: E501

        :param timestamp: The timestamp of this RawJobDescriptionResponse.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def file_text(self):
        """Gets the file_text of this RawJobDescriptionResponse.  # noqa: E501

        number of words in the converted job description  # noqa: E501

        :return: The file_text of this RawJobDescriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_text

    @file_text.setter
    def file_text(self, file_text):
        """Sets the file_text of this RawJobDescriptionResponse.

        number of words in the converted job description  # noqa: E501

        :param file_text: The file_text of this RawJobDescriptionResponse.  # noqa: E501
        :type: str
        """

        self._file_text = file_text

    @property
    def converted_length(self):
        """Gets the converted_length of this RawJobDescriptionResponse.  # noqa: E501

        number of words in the converted job description  # noqa: E501

        :return: The converted_length of this RawJobDescriptionResponse.  # noqa: E501
        :rtype: int
        """
        return self._converted_length

    @converted_length.setter
    def converted_length(self, converted_length):
        """Sets the converted_length of this RawJobDescriptionResponse.

        number of words in the converted job description  # noqa: E501

        :param converted_length: The converted_length of this RawJobDescriptionResponse.  # noqa: E501
        :type: int
        """
        if converted_length is not None and converted_length > 999999:  # noqa: E501
            raise ValueError("Invalid value for `converted_length`, must be a value less than or equal to `999999`")  # noqa: E501
        if converted_length is not None and converted_length < 0:  # noqa: E501
            raise ValueError("Invalid value for `converted_length`, must be a value greater than or equal to `0`")  # noqa: E501

        self._converted_length = converted_length

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
        if not isinstance(other, RawJobDescriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
