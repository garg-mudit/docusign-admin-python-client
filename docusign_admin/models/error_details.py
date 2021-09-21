# coding: utf-8

"""
    DocuSign Admin API

    An API for an organization administrator to manage organizations, accounts and users  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_admin.client.configuration import Configuration


class ErrorDetails(object):
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
        'error': 'str',
        'error_description': 'str'
    }

    attribute_map = {
        'error': 'error',
        'error_description': 'error_description'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ErrorDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error = None
        self._error_description = None
        self.discriminator = None

        setattr(self, "_{}".format('error'), kwargs.get('error', None))
        setattr(self, "_{}".format('error_description'), kwargs.get('error_description', None))

    @property
    def error(self):
        """Gets the error of this ErrorDetails.  # noqa: E501


        :return: The error of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ErrorDetails.


        :param error: The error of this ErrorDetails.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_description(self):
        """Gets the error_description of this ErrorDetails.  # noqa: E501


        :return: The error_description of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this ErrorDetails.


        :param error_description: The error_description of this ErrorDetails.  # noqa: E501
        :type: str
        """

        self._error_description = error_description

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
        if issubclass(ErrorDetails, dict):
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
        if not isinstance(other, ErrorDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorDetails):
            return True

        return self.to_dict() != other.to_dict()
