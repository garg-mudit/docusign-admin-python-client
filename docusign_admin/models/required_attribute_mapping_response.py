# coding: utf-8

"""
    DocuSign Admin API

    An API for an organization administrator to manage organizations, accounts and users  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RequiredAttributeMappingResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'required_attribute_id': 'int',
        'required_attribute_name': 'str',
        'required_attribute_friendly_name': 'str',
        'substitute_attribute_name': 'str'
    }

    attribute_map = {
        'required_attribute_id': 'required_attribute_id',
        'required_attribute_name': 'required_attribute_name',
        'required_attribute_friendly_name': 'required_attribute_friendly_name',
        'substitute_attribute_name': 'substitute_attribute_name'
    }

    def __init__(self, required_attribute_id=None, required_attribute_name=None, required_attribute_friendly_name=None, substitute_attribute_name=None):  # noqa: E501
        """RequiredAttributeMappingResponse - a model defined in Swagger"""  # noqa: E501

        self._required_attribute_id = None
        self._required_attribute_name = None
        self._required_attribute_friendly_name = None
        self._substitute_attribute_name = None
        self.discriminator = None

        if required_attribute_id is not None:
            self.required_attribute_id = required_attribute_id
        if required_attribute_name is not None:
            self.required_attribute_name = required_attribute_name
        if required_attribute_friendly_name is not None:
            self.required_attribute_friendly_name = required_attribute_friendly_name
        if substitute_attribute_name is not None:
            self.substitute_attribute_name = substitute_attribute_name

    @property
    def required_attribute_id(self):
        """Gets the required_attribute_id of this RequiredAttributeMappingResponse.  # noqa: E501


        :return: The required_attribute_id of this RequiredAttributeMappingResponse.  # noqa: E501
        :rtype: int
        """
        return self._required_attribute_id

    @required_attribute_id.setter
    def required_attribute_id(self, required_attribute_id):
        """Sets the required_attribute_id of this RequiredAttributeMappingResponse.


        :param required_attribute_id: The required_attribute_id of this RequiredAttributeMappingResponse.  # noqa: E501
        :type: int
        """

        self._required_attribute_id = required_attribute_id

    @property
    def required_attribute_name(self):
        """Gets the required_attribute_name of this RequiredAttributeMappingResponse.  # noqa: E501


        :return: The required_attribute_name of this RequiredAttributeMappingResponse.  # noqa: E501
        :rtype: str
        """
        return self._required_attribute_name

    @required_attribute_name.setter
    def required_attribute_name(self, required_attribute_name):
        """Sets the required_attribute_name of this RequiredAttributeMappingResponse.


        :param required_attribute_name: The required_attribute_name of this RequiredAttributeMappingResponse.  # noqa: E501
        :type: str
        """

        self._required_attribute_name = required_attribute_name

    @property
    def required_attribute_friendly_name(self):
        """Gets the required_attribute_friendly_name of this RequiredAttributeMappingResponse.  # noqa: E501


        :return: The required_attribute_friendly_name of this RequiredAttributeMappingResponse.  # noqa: E501
        :rtype: str
        """
        return self._required_attribute_friendly_name

    @required_attribute_friendly_name.setter
    def required_attribute_friendly_name(self, required_attribute_friendly_name):
        """Sets the required_attribute_friendly_name of this RequiredAttributeMappingResponse.


        :param required_attribute_friendly_name: The required_attribute_friendly_name of this RequiredAttributeMappingResponse.  # noqa: E501
        :type: str
        """

        self._required_attribute_friendly_name = required_attribute_friendly_name

    @property
    def substitute_attribute_name(self):
        """Gets the substitute_attribute_name of this RequiredAttributeMappingResponse.  # noqa: E501


        :return: The substitute_attribute_name of this RequiredAttributeMappingResponse.  # noqa: E501
        :rtype: str
        """
        return self._substitute_attribute_name

    @substitute_attribute_name.setter
    def substitute_attribute_name(self, substitute_attribute_name):
        """Sets the substitute_attribute_name of this RequiredAttributeMappingResponse.


        :param substitute_attribute_name: The substitute_attribute_name of this RequiredAttributeMappingResponse.  # noqa: E501
        :type: str
        """

        self._substitute_attribute_name = substitute_attribute_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(RequiredAttributeMappingResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequiredAttributeMappingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
