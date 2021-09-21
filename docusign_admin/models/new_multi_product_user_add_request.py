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


class NewMultiProductUserAddRequest(object):
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
        'product_permission_profiles': 'list[ProductPermissionProfileRequest]',
        'ds_groups': 'list[DSGroupRequest]',
        'user_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'default_account_id': 'str',
        'language_culture': 'str',
        'access_code': 'str',
        'federated_status': 'str',
        'auto_activate_memberships': 'bool'
    }

    attribute_map = {
        'product_permission_profiles': 'product_permission_profiles',
        'ds_groups': 'ds_groups',
        'user_name': 'user_name',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'default_account_id': 'default_account_id',
        'language_culture': 'language_culture',
        'access_code': 'access_code',
        'federated_status': 'federated_status',
        'auto_activate_memberships': 'auto_activate_memberships'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """NewMultiProductUserAddRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_permission_profiles = None
        self._ds_groups = None
        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._default_account_id = None
        self._language_culture = None
        self._access_code = None
        self._federated_status = None
        self._auto_activate_memberships = None
        self.discriminator = None

        setattr(self, "_{}".format('product_permission_profiles'), kwargs.get('product_permission_profiles', None))
        setattr(self, "_{}".format('ds_groups'), kwargs.get('ds_groups', None))
        setattr(self, "_{}".format('user_name'), kwargs.get('user_name', None))
        setattr(self, "_{}".format('first_name'), kwargs.get('first_name', None))
        setattr(self, "_{}".format('last_name'), kwargs.get('last_name', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('default_account_id'), kwargs.get('default_account_id', None))
        setattr(self, "_{}".format('language_culture'), kwargs.get('language_culture', None))
        setattr(self, "_{}".format('access_code'), kwargs.get('access_code', None))
        setattr(self, "_{}".format('federated_status'), kwargs.get('federated_status', None))
        setattr(self, "_{}".format('auto_activate_memberships'), kwargs.get('auto_activate_memberships', None))

    @property
    def product_permission_profiles(self):
        """Gets the product_permission_profiles of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The product_permission_profiles of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: list[ProductPermissionProfileRequest]
        """
        return self._product_permission_profiles

    @product_permission_profiles.setter
    def product_permission_profiles(self, product_permission_profiles):
        """Sets the product_permission_profiles of this NewMultiProductUserAddRequest.


        :param product_permission_profiles: The product_permission_profiles of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: list[ProductPermissionProfileRequest]
        """
        if self._configuration.client_side_validation and product_permission_profiles is None:
            raise ValueError("Invalid value for `product_permission_profiles`, must not be `None`")  # noqa: E501

        self._product_permission_profiles = product_permission_profiles

    @property
    def ds_groups(self):
        """Gets the ds_groups of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The ds_groups of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: list[DSGroupRequest]
        """
        return self._ds_groups

    @ds_groups.setter
    def ds_groups(self, ds_groups):
        """Sets the ds_groups of this NewMultiProductUserAddRequest.


        :param ds_groups: The ds_groups of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: list[DSGroupRequest]
        """

        self._ds_groups = ds_groups

    @property
    def user_name(self):
        """Gets the user_name of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The user_name of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this NewMultiProductUserAddRequest.


        :param user_name: The user_name of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def first_name(self):
        """Gets the first_name of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The first_name of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this NewMultiProductUserAddRequest.


        :param first_name: The first_name of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The last_name of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this NewMultiProductUserAddRequest.


        :param last_name: The last_name of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The email of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this NewMultiProductUserAddRequest.


        :param email: The email of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def default_account_id(self):
        """Gets the default_account_id of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The default_account_id of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._default_account_id

    @default_account_id.setter
    def default_account_id(self, default_account_id):
        """Sets the default_account_id of this NewMultiProductUserAddRequest.


        :param default_account_id: The default_account_id of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: str
        """

        self._default_account_id = default_account_id

    @property
    def language_culture(self):
        """Gets the language_culture of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The language_culture of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._language_culture

    @language_culture.setter
    def language_culture(self, language_culture):
        """Sets the language_culture of this NewMultiProductUserAddRequest.


        :param language_culture: The language_culture of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: str
        """

        self._language_culture = language_culture

    @property
    def access_code(self):
        """Gets the access_code of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The access_code of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this NewMultiProductUserAddRequest.


        :param access_code: The access_code of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: str
        """

        self._access_code = access_code

    @property
    def federated_status(self):
        """Gets the federated_status of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The federated_status of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._federated_status

    @federated_status.setter
    def federated_status(self, federated_status):
        """Sets the federated_status of this NewMultiProductUserAddRequest.


        :param federated_status: The federated_status of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: str
        """

        self._federated_status = federated_status

    @property
    def auto_activate_memberships(self):
        """Gets the auto_activate_memberships of this NewMultiProductUserAddRequest.  # noqa: E501


        :return: The auto_activate_memberships of this NewMultiProductUserAddRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_activate_memberships

    @auto_activate_memberships.setter
    def auto_activate_memberships(self, auto_activate_memberships):
        """Sets the auto_activate_memberships of this NewMultiProductUserAddRequest.


        :param auto_activate_memberships: The auto_activate_memberships of this NewMultiProductUserAddRequest.  # noqa: E501
        :type: bool
        """

        self._auto_activate_memberships = auto_activate_memberships

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
        if issubclass(NewMultiProductUserAddRequest, dict):
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
        if not isinstance(other, NewMultiProductUserAddRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewMultiProductUserAddRequest):
            return True

        return self.to_dict() != other.to_dict()
