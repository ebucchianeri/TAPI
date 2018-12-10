# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiOduUasChoice(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fuas=None, bidirectional=True, nuas=None, uas=None):  # noqa: E501
        """TapiOduUasChoice - a model defined in OpenAPI

        :param fuas: The fuas of this TapiOduUasChoice.  # noqa: E501
        :type fuas: int
        :param bidirectional: The bidirectional of this TapiOduUasChoice.  # noqa: E501
        :type bidirectional: bool
        :param nuas: The nuas of this TapiOduUasChoice.  # noqa: E501
        :type nuas: int
        :param uas: The uas of this TapiOduUasChoice.  # noqa: E501
        :type uas: int
        """
        self.openapi_types = {
            'fuas': int,
            'bidirectional': bool,
            'nuas': int,
            'uas': int
        }

        self.attribute_map = {
            'fuas': 'fuas',
            'bidirectional': 'bidirectional',
            'nuas': 'nuas',
            'uas': 'uas'
        }

        self._fuas = fuas
        self._bidirectional = bidirectional
        self._nuas = nuas
        self._uas = uas

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduUasChoice':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.UasChoice of this TapiOduUasChoice.  # noqa: E501
        :rtype: TapiOduUasChoice
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fuas(self):
        """Gets the fuas of this TapiOduUasChoice.

        none  # noqa: E501

        :return: The fuas of this TapiOduUasChoice.
        :rtype: int
        """
        return self._fuas

    @fuas.setter
    def fuas(self, fuas):
        """Sets the fuas of this TapiOduUasChoice.

        none  # noqa: E501

        :param fuas: The fuas of this TapiOduUasChoice.
        :type fuas: int
        """

        self._fuas = fuas

    @property
    def bidirectional(self):
        """Gets the bidirectional of this TapiOduUasChoice.

        none  # noqa: E501

        :return: The bidirectional of this TapiOduUasChoice.
        :rtype: bool
        """
        return self._bidirectional

    @bidirectional.setter
    def bidirectional(self, bidirectional):
        """Sets the bidirectional of this TapiOduUasChoice.

        none  # noqa: E501

        :param bidirectional: The bidirectional of this TapiOduUasChoice.
        :type bidirectional: bool
        """

        self._bidirectional = bidirectional

    @property
    def nuas(self):
        """Gets the nuas of this TapiOduUasChoice.

        none  # noqa: E501

        :return: The nuas of this TapiOduUasChoice.
        :rtype: int
        """
        return self._nuas

    @nuas.setter
    def nuas(self, nuas):
        """Sets the nuas of this TapiOduUasChoice.

        none  # noqa: E501

        :param nuas: The nuas of this TapiOduUasChoice.
        :type nuas: int
        """

        self._nuas = nuas

    @property
    def uas(self):
        """Gets the uas of this TapiOduUasChoice.

        none  # noqa: E501

        :return: The uas of this TapiOduUasChoice.
        :rtype: int
        """
        return self._uas

    @uas.setter
    def uas(self, uas):
        """Sets the uas of this TapiOduUasChoice.

        none  # noqa: E501

        :param uas: The uas of this TapiOduUasChoice.
        :type uas: int
        """

        self._uas = uas