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


@cache
def get_opensearch_client() -> OpenSearchClient:
    return OpenSearchClient()
