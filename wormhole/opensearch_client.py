from functools import cache
from opensearchpy import OpenSearch
from wormhole.config import config
from opensearchpy.exceptions import ConnectionError, TransportError

class OpenSearchClient:
    def __init__(self):
        # define auth
        auth = (config.OPENSEARCH_USERNAME, config.OPENSEARCH_PASSWORD)

        # define client
        self.opensearch_client = OpenSearch(
            hosts = [
                {
                    "host": config.OPENSEARCH_HOST,
                    "port": config.OPENSEARCH_PORT
                }
            ],
            http_auth = auth,
            use_ssl = config.USE_SSL
        )

        # raise connection error before user attempts to call the function
        if not self.opensearch_client.ping():
            raise ConnectionError("Cluster is Unreachable!!")


    def get_client_info(self):
        return self.opensearch_client.info()


    def get_cluster_health(self):
        return self.opensearch_client.cluster.health()


    def get_indices_info(self):
        # _cat/indices
        # filter all starts with dot
        return self.opensearch_client.indices.get(index="*")


@cache
def get_opensearch_client() -> OpenSearchClient:
    return OpenSearchClient()
