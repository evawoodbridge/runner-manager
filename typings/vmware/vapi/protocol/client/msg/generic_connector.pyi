"""
This type stub file was generated by pyright.
"""

from vmware.vapi.protocol.client.connector import Connector

"""
Generic client connector
"""
__author__ = ...
__copyright__ = ...
logger = ...

class GenericConnector(Connector):
    """A generic protocol connector"""

    def __init__(self, rpc_provider, api_provider, provider_filter_chain) -> None:
        """
        Generic protocol connector init

        :type  rpc_provider: :class:`vmware.vapi.protocol.client.rpc.provider
            .RpcProvider`
        :param rpc_provider: rpc provider object
        :type  api_provider: :class:`vmware.vapi.core.ApiProvider`
        :param api_provider: api provider object
        :type  provider_filter_chain: :class:`list` of
            :class:`vmware.vapi.provider.filter.ApiProviderFilter`
        :param provider_filter_chain: List of API filters in order they are to
            be chained
        """
        ...

    def connect(self):  # -> None:
        """rpc provider connect"""
        ...

    def disconnect(self):  # -> None:
        """rpc provider disconnect"""
        ...