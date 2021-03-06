# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiTopologyLayerProtocolTransitionPac(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, transitioned_layer_protocol_name=None):  # noqa: E501
        """TapiTopologyLayerProtocolTransitionPac - a model defined in OpenAPI

        :param transitioned_layer_protocol_name: The transitioned_layer_protocol_name of this TapiTopologyLayerProtocolTransitionPac.  # noqa: E501
        :type transitioned_layer_protocol_name: List[str]
        """
        self.openapi_types = {
            'transitioned_layer_protocol_name': List[str]
        }

        self.attribute_map = {
            'transitioned_layer_protocol_name': 'transitioned-layer-protocol-name'
        }

        self._transitioned_layer_protocol_name = transitioned_layer_protocol_name

    @classmethod
    def from_dict(cls, dikt) -> 'TapiTopologyLayerProtocolTransitionPac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.topology.LayerProtocolTransitionPac of this TapiTopologyLayerProtocolTransitionPac.  # noqa: E501
        :rtype: TapiTopologyLayerProtocolTransitionPac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transitioned_layer_protocol_name(self):
        """Gets the transitioned_layer_protocol_name of this TapiTopologyLayerProtocolTransitionPac.

        Provides the ordered structure of layer protocol transitions encapsulated in the TopologicalEntity. The ordering relates to the LinkPort role.  # noqa: E501

        :return: The transitioned_layer_protocol_name of this TapiTopologyLayerProtocolTransitionPac.
        :rtype: List[str]
        """
        return self._transitioned_layer_protocol_name

    @transitioned_layer_protocol_name.setter
    def transitioned_layer_protocol_name(self, transitioned_layer_protocol_name):
        """Sets the transitioned_layer_protocol_name of this TapiTopologyLayerProtocolTransitionPac.

        Provides the ordered structure of layer protocol transitions encapsulated in the TopologicalEntity. The ordering relates to the LinkPort role.  # noqa: E501

        :param transitioned_layer_protocol_name: The transitioned_layer_protocol_name of this TapiTopologyLayerProtocolTransitionPac.
        :type transitioned_layer_protocol_name: List[str]
        """

        self._transitioned_layer_protocol_name = transitioned_layer_protocol_name
