"""Endpoints to configure and interact with high availability clusters."""

from dataclasses import dataclass
from typing import Any, Awaitable

from requests import Response

from .base import APIEndpoint, _ret_json


@dataclass
class Cluster(APIEndpoint):
    """Class defining the Cluster API endpoint.

    Attributes
    ----------
    endpoint : str, default='cluster'
        The endpoint path.

    Methods
    -------
    get_cluster_status()
        Get cluster status.

    """

    endpoint: str = "cluster"

    @_ret_json
    def get_cluster_status(self) -> Any | Response | Awaitable[Any | Response]:
        """Get cluster status.

        Get a set of information for each node in the cluster, useful for
        checking the status and health of each node.

        Returns
        -------
        Any or Coroutine(...) -> Any
        or requests.Response or Coroutine(...) -> requests.Response

        """
        return self.client.get(f"{self.endpoint}/status")
