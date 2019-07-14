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


class PostalAddress(object):
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
        'name': 'str',
        'street_address': 'str',
        'address_locality': 'str',
        'address_region': 'str',
        'address_country': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'street_address': 'streetAddress',
        'address_locality': 'addressLocality',
        'address_region': 'addressRegion',
        'address_country': 'addressCountry',
        'postal_code': 'postalCode'
    }

    def __init__(self, name=None, street_address=None, address_locality=None, address_region=None, address_country=None, postal_code=None):  # noqa: E501
        """PostalAddress - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._street_address = None
        self._address_locality = None
        self._address_region = None
        self._address_country = None
        self._postal_code = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if street_address is not None:
            self.street_address = street_address
        if address_locality is not None:
            self.address_locality = address_locality
        if address_region is not None:
            self.address_region = address_region
        if address_country is not None:
            self.address_country = address_country
        if postal_code is not None:
            self.postal_code = postal_code

    @property
    def name(self):
        """Gets the name of this PostalAddress.  # noqa: E501


        :return: The name of this PostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostalAddress.


        :param name: The name of this PostalAddress.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 1024:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `1024`")  # noqa: E501

        self._name = name

    @property
    def street_address(self):
        """Gets the street_address of this PostalAddress.  # noqa: E501


        :return: The street_address of this PostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this PostalAddress.


        :param street_address: The street_address of this PostalAddress.  # noqa: E501
        :type: str
        """
        if street_address is not None and len(street_address) > 1024:
            raise ValueError("Invalid value for `street_address`, length must be less than or equal to `1024`")  # noqa: E501

        self._street_address = street_address

    @property
    def address_locality(self):
        """Gets the address_locality of this PostalAddress.  # noqa: E501


        :return: The address_locality of this PostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_locality

    @address_locality.setter
    def address_locality(self, address_locality):
        """Sets the address_locality of this PostalAddress.


        :param address_locality: The address_locality of this PostalAddress.  # noqa: E501
        :type: str
        """
        if address_locality is not None and len(address_locality) > 1024:
            raise ValueError("Invalid value for `address_locality`, length must be less than or equal to `1024`")  # noqa: E501

        self._address_locality = address_locality

    @property
    def address_region(self):
        """Gets the address_region of this PostalAddress.  # noqa: E501


        :return: The address_region of this PostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_region

    @address_region.setter
    def address_region(self, address_region):
        """Sets the address_region of this PostalAddress.


        :param address_region: The address_region of this PostalAddress.  # noqa: E501
        :type: str
        """
        if address_region is not None and len(address_region) > 1024:
            raise ValueError("Invalid value for `address_region`, length must be less than or equal to `1024`")  # noqa: E501

        self._address_region = address_region

    @property
    def address_country(self):
        """Gets the address_country of this PostalAddress.  # noqa: E501


        :return: The address_country of this PostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_country

    @address_country.setter
    def address_country(self, address_country):
        """Sets the address_country of this PostalAddress.


        :param address_country: The address_country of this PostalAddress.  # noqa: E501
        :type: str
        """
        if address_country is not None and len(address_country) > 1024:
            raise ValueError("Invalid value for `address_country`, length must be less than or equal to `1024`")  # noqa: E501

        self._address_country = address_country

    @property
    def postal_code(self):
        """Gets the postal_code of this PostalAddress.  # noqa: E501


        :return: The postal_code of this PostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PostalAddress.


        :param postal_code: The postal_code of this PostalAddress.  # noqa: E501
        :type: str
        """
        if postal_code is not None and len(postal_code) > 1024:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `1024`")  # noqa: E501

        self._postal_code = postal_code

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
        if not isinstance(other, PostalAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
