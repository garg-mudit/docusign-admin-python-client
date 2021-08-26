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


class NewUserRequest(object):
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
        'accounts': 'list[NewUserRequestAccountProperties]',
        'user_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'default_account_id': 'str',
        'language_culture': 'str',
        'selected_languages': 'str',
        'access_code': 'str',
        'federated_status': 'str',
        'auto_activate_memberships': 'bool'
    }

    attribute_map = {
        'accounts': 'accounts',
        'user_name': 'user_name',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'default_account_id': 'default_account_id',
        'language_culture': 'language_culture',
        'selected_languages': 'selected_languages',
        'access_code': 'access_code',
        'federated_status': 'federated_status',
        'auto_activate_memberships': 'auto_activate_memberships'
    }

    def __init__(self, accounts=None, user_name=None, first_name=None, last_name=None, email=None, default_account_id=None, language_culture=None, selected_languages=None, access_code=None, federated_status=None, auto_activate_memberships=None):  # noqa: E501
        """NewUserRequest - a model defined in Swagger"""  # noqa: E501

        self._accounts = None
        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._default_account_id = None
        self._language_culture = None
        self._selected_languages = None
        self._access_code = None
        self._federated_status = None
        self._auto_activate_memberships = None
        self.discriminator = None

        self.accounts = accounts
        if user_name is not None:
            self.user_name = user_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        self.email = email
        if default_account_id is not None:
            self.default_account_id = default_account_id
        if language_culture is not None:
            self.language_culture = language_culture
        if selected_languages is not None:
            self.selected_languages = selected_languages
        if access_code is not None:
            self.access_code = access_code
        if federated_status is not None:
            self.federated_status = federated_status
        if auto_activate_memberships is not None:
            self.auto_activate_memberships = auto_activate_memberships

    @property
    def accounts(self):
        """Gets the accounts of this NewUserRequest.  # noqa: E501


        :return: The accounts of this NewUserRequest.  # noqa: E501
        :rtype: list[NewUserRequestAccountProperties]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this NewUserRequest.


        :param accounts: The accounts of this NewUserRequest.  # noqa: E501
        :type: list[NewUserRequestAccountProperties]
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

    @property
    def user_name(self):
        """Gets the user_name of this NewUserRequest.  # noqa: E501


        :return: The user_name of this NewUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this NewUserRequest.


        :param user_name: The user_name of this NewUserRequest.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def first_name(self):
        """Gets the first_name of this NewUserRequest.  # noqa: E501


        :return: The first_name of this NewUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this NewUserRequest.


        :param first_name: The first_name of this NewUserRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this NewUserRequest.  # noqa: E501


        :return: The last_name of this NewUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this NewUserRequest.


        :param last_name: The last_name of this NewUserRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this NewUserRequest.  # noqa: E501


        :return: The email of this NewUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this NewUserRequest.


        :param email: The email of this NewUserRequest.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def default_account_id(self):
        """Gets the default_account_id of this NewUserRequest.  # noqa: E501


        :return: The default_account_id of this NewUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._default_account_id

    @default_account_id.setter
    def default_account_id(self, default_account_id):
        """Sets the default_account_id of this NewUserRequest.


        :param default_account_id: The default_account_id of this NewUserRequest.  # noqa: E501
        :type: str
        """

        self._default_account_id = default_account_id

    @property
    def language_culture(self):
        """Gets the language_culture of this NewUserRequest.  # noqa: E501


        :return: The language_culture of this NewUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._language_culture

    @language_culture.setter
    def language_culture(self, language_culture):
        """Sets the language_culture of this NewUserRequest.


        :param language_culture: The language_culture of this NewUserRequest.  # noqa: E501
        :type: str
        """

        self._language_culture = language_culture

    @property
    def selected_languages(self):
        """Gets the selected_languages of this NewUserRequest.  # noqa: E501


        :return: The selected_languages of this NewUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._selected_languages

    @selected_languages.setter
    def selected_languages(self, selected_languages):
        """Sets the selected_languages of this NewUserRequest.


        :param selected_languages: The selected_languages of this NewUserRequest.  # noqa: E501
        :type: str
        """

        self._selected_languages = selected_languages

    @property
    def access_code(self):
        """Gets the access_code of this NewUserRequest.  # noqa: E501


        :return: The access_code of this NewUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this NewUserRequest.


        :param access_code: The access_code of this NewUserRequest.  # noqa: E501
        :type: str
        """

        self._access_code = access_code

    @property
    def federated_status(self):
        """Gets the federated_status of this NewUserRequest.  # noqa: E501


        :return: The federated_status of this NewUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._federated_status

    @federated_status.setter
    def federated_status(self, federated_status):
        """Sets the federated_status of this NewUserRequest.


        :param federated_status: The federated_status of this NewUserRequest.  # noqa: E501
        :type: str
        """

        self._federated_status = federated_status

    @property
    def auto_activate_memberships(self):
        """Gets the auto_activate_memberships of this NewUserRequest.  # noqa: E501


        :return: The auto_activate_memberships of this NewUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_activate_memberships

    @auto_activate_memberships.setter
    def auto_activate_memberships(self, auto_activate_memberships):
        """Sets the auto_activate_memberships of this NewUserRequest.


        :param auto_activate_memberships: The auto_activate_memberships of this NewUserRequest.  # noqa: E501
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
        if issubclass(NewUserRequest, dict):
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
        if not isinstance(other, NewUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
