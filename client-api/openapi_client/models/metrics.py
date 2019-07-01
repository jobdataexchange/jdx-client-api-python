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


class Metrics(object):
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
        'user_type': 'str',
        'uuid': 'str',
        'object_type': 'str',
        'statistic_type': 'str',
        'extra_info': 'MetricsExtraInfo',
        'metric_class': 'str'
    }

    attribute_map = {
        'user_type': 'userType',
        'uuid': 'uuid',
        'object_type': 'objectType',
        'statistic_type': 'statisticType',
        'extra_info': 'extraInfo',
        'metric_class': 'metricClass'
    }

    def __init__(self, user_type=None, uuid=None, object_type=None, statistic_type=None, extra_info=None, metric_class=None):  # noqa: E501
        """Metrics - a model defined in OpenAPI"""  # noqa: E501

        self._user_type = None
        self._uuid = None
        self._object_type = None
        self._statistic_type = None
        self._extra_info = None
        self._metric_class = None
        self.discriminator = None

        if user_type is not None:
            self.user_type = user_type
        if uuid is not None:
            self.uuid = uuid
        if object_type is not None:
            self.object_type = object_type
        if statistic_type is not None:
            self.statistic_type = statistic_type
        if extra_info is not None:
            self.extra_info = extra_info
        if metric_class is not None:
            self.metric_class = metric_class

    @property
    def user_type(self):
        """Gets the user_type of this Metrics.  # noqa: E501

        the type of user the metric was derived from. For example, a count derived from a `collaborative` is the number of employers in that collaborative, whereas a count derived from `pilot user` is the number of `pilot users` at that time (e.g. using a recomemendation)  # noqa: E501

        :return: The user_type of this Metrics.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this Metrics.

        the type of user the metric was derived from. For example, a count derived from a `collaborative` is the number of employers in that collaborative, whereas a count derived from `pilot user` is the number of `pilot users` at that time (e.g. using a recomemendation)  # noqa: E501

        :param user_type: The user_type of this Metrics.  # noqa: E501
        :type: str
        """
        allowed_values = ["abstract", "user", "pilot user", "collaborative"]  # noqa: E501
        if user_type not in allowed_values:
            raise ValueError(
                "Invalid value for `user_type` ({0}), must be one of {1}"  # noqa: E501
                .format(user_type, allowed_values)
            )

        self._user_type = user_type

    @property
    def uuid(self):
        """Gets the uuid of this Metrics.  # noqa: E501

        If given, the matching uuid in the matchTable (a row in the matchTable) that this `scoredRecommendation` applies to (e.g. one of several `scoredRecommendation`s that could be assigned to a particular competency property in the json-ld file). If no uuid present and recommendation, then this applies to the entire converted job description (e.g., in general you can be recommended to include additional competencies of a certain type based on comparative measures)  # noqa: E501

        :return: The uuid of this Metrics.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Metrics.

        If given, the matching uuid in the matchTable (a row in the matchTable) that this `scoredRecommendation` applies to (e.g. one of several `scoredRecommendation`s that could be assigned to a particular competency property in the json-ld file). If no uuid present and recommendation, then this applies to the entire converted job description (e.g., in general you can be recommended to include additional competencies of a certain type based on comparative measures)  # noqa: E501

        :param uuid: The uuid of this Metrics.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def object_type(self):
        """Gets the object_type of this Metrics.  # noqa: E501

        If `score`, this object simply rates the matching uuid identified object. If `recommendation` an actual recommendation, with `recommendedContent` and other justifications, are provided.  # noqa: E501

        :return: The object_type of this Metrics.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this Metrics.

        If `score`, this object simply rates the matching uuid identified object. If `recommendation` an actual recommendation, with `recommendedContent` and other justifications, are provided.  # noqa: E501

        :param object_type: The object_type of this Metrics.  # noqa: E501
        :type: str
        """
        allowed_values = ["recommendation", "score"]  # noqa: E501
        if object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `object_type` ({0}), must be one of {1}"  # noqa: E501
                .format(object_type, allowed_values)
            )

        self._object_type = object_type

    @property
    def statistic_type(self):
        """Gets the statistic_type of this Metrics.  # noqa: E501


        :return: The statistic_type of this Metrics.  # noqa: E501
        :rtype: str
        """
        return self._statistic_type

    @statistic_type.setter
    def statistic_type(self, statistic_type):
        """Sets the statistic_type of this Metrics.


        :param statistic_type: The statistic_type of this Metrics.  # noqa: E501
        :type: str
        """
        allowed_values = ["count", "mean", "median"]  # noqa: E501
        if statistic_type not in allowed_values:
            raise ValueError(
                "Invalid value for `statistic_type` ({0}), must be one of {1}"  # noqa: E501
                .format(statistic_type, allowed_values)
            )

        self._statistic_type = statistic_type

    @property
    def extra_info(self):
        """Gets the extra_info of this Metrics.  # noqa: E501


        :return: The extra_info of this Metrics.  # noqa: E501
        :rtype: MetricsExtraInfo
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this Metrics.


        :param extra_info: The extra_info of this Metrics.  # noqa: E501
        :type: MetricsExtraInfo
        """

        self._extra_info = extra_info

    @property
    def metric_class(self):
        """Gets the metric_class of this Metrics.  # noqa: E501

        In a scoring context (e.g. `objectType: score`) this describes what kind of framework is being recommended. In a recommendation context this describes the nature of the `recommendedContent` and the area that recommendation seeks to help the user improve in. For example, a `metricClass: actionable`, with `recommendedContent: Consider using more action verbs to describe this competency. 55 out of 100 users in your collaborative have done so.`  # noqa: E501

        :return: The metric_class of this Metrics.  # noqa: E501
        :rtype: str
        """
        return self._metric_class

    @metric_class.setter
    def metric_class(self, metric_class):
        """Sets the metric_class of this Metrics.

        In a scoring context (e.g. `objectType: score`) this describes what kind of framework is being recommended. In a recommendation context this describes the nature of the `recommendedContent` and the area that recommendation seeks to help the user improve in. For example, a `metricClass: actionable`, with `recommendedContent: Consider using more action verbs to describe this competency. 55 out of 100 users in your collaborative have done so.`  # noqa: E501

        :param metric_class: The metric_class of this Metrics.  # noqa: E501
        :type: str
        """
        allowed_values = ["occupation", "industry", "competency", "observable", "actionable", "brief", "topic"]  # noqa: E501
        if metric_class not in allowed_values:
            raise ValueError(
                "Invalid value for `metric_class` ({0}), must be one of {1}"  # noqa: E501
                .format(metric_class, allowed_values)
            )

        self._metric_class = metric_class

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
        if not isinstance(other, Metrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
