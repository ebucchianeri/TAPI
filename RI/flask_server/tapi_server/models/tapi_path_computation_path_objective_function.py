# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_directive_value import TapiCommonDirectiveValue  # noqa: F401,E501
from tapi_server.models.tapi_common_local_class import TapiCommonLocalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server import util


class TapiPathComputationPathObjectiveFunction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, local_id=None, link_utilization=None, bandwidth_optimization=None, cost_optimization=None, resource_sharing=None, concurrent_paths=None):  # noqa: E501
        """TapiPathComputationPathObjectiveFunction - a model defined in OpenAPI

        :param name: The name of this TapiPathComputationPathObjectiveFunction.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param local_id: The local_id of this TapiPathComputationPathObjectiveFunction.  # noqa: E501
        :type local_id: str
        :param link_utilization: The link_utilization of this TapiPathComputationPathObjectiveFunction.  # noqa: E501
        :type link_utilization: TapiCommonDirectiveValue
        :param bandwidth_optimization: The bandwidth_optimization of this TapiPathComputationPathObjectiveFunction.  # noqa: E501
        :type bandwidth_optimization: TapiCommonDirectiveValue
        :param cost_optimization: The cost_optimization of this TapiPathComputationPathObjectiveFunction.  # noqa: E501
        :type cost_optimization: TapiCommonDirectiveValue
        :param resource_sharing: The resource_sharing of this TapiPathComputationPathObjectiveFunction.  # noqa: E501
        :type resource_sharing: TapiCommonDirectiveValue
        :param concurrent_paths: The concurrent_paths of this TapiPathComputationPathObjectiveFunction.  # noqa: E501
        :type concurrent_paths: TapiCommonDirectiveValue
        """
        self.openapi_types = {
            'name': List[TapiCommonNameAndValue],
            'local_id': str,
            'link_utilization': TapiCommonDirectiveValue,
            'bandwidth_optimization': TapiCommonDirectiveValue,
            'cost_optimization': TapiCommonDirectiveValue,
            'resource_sharing': TapiCommonDirectiveValue,
            'concurrent_paths': TapiCommonDirectiveValue
        }

        self.attribute_map = {
            'name': 'name',
            'local_id': 'local-id',
            'link_utilization': 'link-utilization',
            'bandwidth_optimization': 'bandwidth-optimization',
            'cost_optimization': 'cost-optimization',
            'resource_sharing': 'resource-sharing',
            'concurrent_paths': 'concurrent-paths'
        }

        self._name = name
        self._local_id = local_id
        self._link_utilization = link_utilization
        self._bandwidth_optimization = bandwidth_optimization
        self._cost_optimization = cost_optimization
        self._resource_sharing = resource_sharing
        self._concurrent_paths = concurrent_paths

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPathComputationPathObjectiveFunction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.path.computation.PathObjectiveFunction of this TapiPathComputationPathObjectiveFunction.  # noqa: E501
        :rtype: TapiPathComputationPathObjectiveFunction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this TapiPathComputationPathObjectiveFunction.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiPathComputationPathObjectiveFunction.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiPathComputationPathObjectiveFunction.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiPathComputationPathObjectiveFunction.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def local_id(self):
        """Gets the local_id of this TapiPathComputationPathObjectiveFunction.

        none  # noqa: E501

        :return: The local_id of this TapiPathComputationPathObjectiveFunction.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this TapiPathComputationPathObjectiveFunction.

        none  # noqa: E501

        :param local_id: The local_id of this TapiPathComputationPathObjectiveFunction.
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def link_utilization(self):
        """Gets the link_utilization of this TapiPathComputationPathObjectiveFunction.


        :return: The link_utilization of this TapiPathComputationPathObjectiveFunction.
        :rtype: TapiCommonDirectiveValue
        """
        return self._link_utilization

    @link_utilization.setter
    def link_utilization(self, link_utilization):
        """Sets the link_utilization of this TapiPathComputationPathObjectiveFunction.


        :param link_utilization: The link_utilization of this TapiPathComputationPathObjectiveFunction.
        :type link_utilization: TapiCommonDirectiveValue
        """

        self._link_utilization = link_utilization

    @property
    def bandwidth_optimization(self):
        """Gets the bandwidth_optimization of this TapiPathComputationPathObjectiveFunction.


        :return: The bandwidth_optimization of this TapiPathComputationPathObjectiveFunction.
        :rtype: TapiCommonDirectiveValue
        """
        return self._bandwidth_optimization

    @bandwidth_optimization.setter
    def bandwidth_optimization(self, bandwidth_optimization):
        """Sets the bandwidth_optimization of this TapiPathComputationPathObjectiveFunction.


        :param bandwidth_optimization: The bandwidth_optimization of this TapiPathComputationPathObjectiveFunction.
        :type bandwidth_optimization: TapiCommonDirectiveValue
        """

        self._bandwidth_optimization = bandwidth_optimization

    @property
    def cost_optimization(self):
        """Gets the cost_optimization of this TapiPathComputationPathObjectiveFunction.


        :return: The cost_optimization of this TapiPathComputationPathObjectiveFunction.
        :rtype: TapiCommonDirectiveValue
        """
        return self._cost_optimization

    @cost_optimization.setter
    def cost_optimization(self, cost_optimization):
        """Sets the cost_optimization of this TapiPathComputationPathObjectiveFunction.


        :param cost_optimization: The cost_optimization of this TapiPathComputationPathObjectiveFunction.
        :type cost_optimization: TapiCommonDirectiveValue
        """

        self._cost_optimization = cost_optimization

    @property
    def resource_sharing(self):
        """Gets the resource_sharing of this TapiPathComputationPathObjectiveFunction.


        :return: The resource_sharing of this TapiPathComputationPathObjectiveFunction.
        :rtype: TapiCommonDirectiveValue
        """
        return self._resource_sharing

    @resource_sharing.setter
    def resource_sharing(self, resource_sharing):
        """Sets the resource_sharing of this TapiPathComputationPathObjectiveFunction.


        :param resource_sharing: The resource_sharing of this TapiPathComputationPathObjectiveFunction.
        :type resource_sharing: TapiCommonDirectiveValue
        """

        self._resource_sharing = resource_sharing

    @property
    def concurrent_paths(self):
        """Gets the concurrent_paths of this TapiPathComputationPathObjectiveFunction.


        :return: The concurrent_paths of this TapiPathComputationPathObjectiveFunction.
        :rtype: TapiCommonDirectiveValue
        """
        return self._concurrent_paths

    @concurrent_paths.setter
    def concurrent_paths(self, concurrent_paths):
        """Sets the concurrent_paths of this TapiPathComputationPathObjectiveFunction.


        :param concurrent_paths: The concurrent_paths of this TapiPathComputationPathObjectiveFunction.
        :type concurrent_paths: TapiCommonDirectiveValue
        """

        self._concurrent_paths = concurrent_paths
