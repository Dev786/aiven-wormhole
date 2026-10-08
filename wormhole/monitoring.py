from wormhole.opensearch_client import OpenSearchClient
from wormhole.log_client import LogClient


class Monitoring:
    def __init__(self, client: OpenSearchClient, logger: LogClient):
        self.client = client
        self.logger = logger


    def log_cluster_health(self):
        cluster_health = self.client.get_cluster_health()
        cluster_info = {
            "status": cluster_health["status"],
            "number_of_nodes": cluster_health["number_of_nodes"],
            "number_of_data_nodes": cluster_health["number_of_data_nodes"],
            "active_primary_shards": cluster_health["active_primary_shards"],
            "active_shards": cluster_health["active_shards"],
        }

        # get the indices info
        indices_info = self.client.get_indices_info()

        user_created_indices = []
        for index, info in indices_info.items():
            '''
                "settings": {
                    "index": {
                    "replication": {
                        "type": "DOCUMENT"
                    },
                    "number_of_shards": "1",
                    "provided_name": "metrics-system",
                    "creation_date": "1790758141192",
                    "number_of_replicas": "0",
                    "uuid": "UOb4wZeySqi1w2rDd6wEzg",
                    "version": {
                        "created": "137277827"
                    }
                    }
                }
            '''

            if not index.startswith("."):
                index_info = {
                    "name": index,
                    "replication_strategy": info["settings"]["index"]["replication"]["type"],
                    "number_of_shards": info["settings"]["index"]["number_of_shards"],
                    "number_of_replicas": info["settings"]["index"]["number_of_replicas"],
                    "created_at": info["settings"]["index"]["creation_date"],
                }
                user_created_indices.append(index_info)

        self.logger.send({
            "cluster_info": cluster_info,
            "user_created_indices_info": user_created_indices,
        })
