# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_updateserviceinterfacepoint_input import TapiCommonUpdateserviceinterfacepointInput  # noqa: F401,E501
from tapi_server import util


class InlineObject32(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input=None):  # noqa: E501
        """InlineObject32 - a model defined in OpenAPI

        :param input: The input of this InlineObject32.  # noqa: E501
        :type input: TapiCommonUpdateserviceinterfacepointInput
        """
        self.openapi_types = {
            'input': TapiCommonUpdateserviceinterfacepointInput
        }

        self.attribute_map = {
            'input': 'input'
        }

        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject32':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_32 of this InlineObject32.  # noqa: E501
        :rtype: InlineObject32
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InlineObject32.


        :return: The input of this InlineObject32.
        :rtype: TapiCommonUpdateserviceinterfacepointInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InlineObject32.


        :param input: The input of this InlineObject32.
        :type input: TapiCommonUpdateserviceinterfacepointInput
        """

        self._input = input
