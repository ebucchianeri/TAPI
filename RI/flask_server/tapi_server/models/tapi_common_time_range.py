# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiCommonTimeRange(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end_time=None, start_time=None):  # noqa: E501
        """TapiCommonTimeRange - a model defined in OpenAPI

        :param end_time: The end_time of this TapiCommonTimeRange.  # noqa: E501
        :type end_time: str
        :param start_time: The start_time of this TapiCommonTimeRange.  # noqa: E501
        :type start_time: str
        """
        self.openapi_types = {
            'end_time': str,
            'start_time': str
        }

        self.attribute_map = {
            'end_time': 'end-time',
            'start_time': 'start-time'
        }

        self._end_time = end_time
        self._start_time = start_time

    @classmethod
    def from_dict(cls, dikt) -> 'TapiCommonTimeRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.common.TimeRange of this TapiCommonTimeRange.  # noqa: E501
        :rtype: TapiCommonTimeRange
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end_time(self):
        """Gets the end_time of this TapiCommonTimeRange.

        none  # noqa: E501

        :return: The end_time of this TapiCommonTimeRange.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TapiCommonTimeRange.

        none  # noqa: E501

        :param end_time: The end_time of this TapiCommonTimeRange.
        :type end_time: str
        """

        self._end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this TapiCommonTimeRange.

        none  # noqa: E501

        :return: The start_time of this TapiCommonTimeRange.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TapiCommonTimeRange.

        none  # noqa: E501

        :param start_time: The start_time of this TapiCommonTimeRange.
        :type start_time: str
        """

        self._start_time = start_time