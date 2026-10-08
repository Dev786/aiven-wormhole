from requests.packages import mod

from wormhole.monitoring import Monitoring
from wormhole.opensearch_client import get_opensearch_client
from wormhole.log_client import LogClient

if __name__ == "__main__":
    open_search_client = get_opensearch_client()
    client_info = open_search_client.get_client_info()
    cluster_version = client_info['version']['number']
    # print(f"Open Search Cluster Version: {cluster_version}")

    # get the cluster health
    cluster_health = open_search_client.get_cluster_health()
    # print(f"Cluster Health: {cluster_health}")

    # get the indices info
    # print("Monitoring")
    monitoring = Monitoring(open_search_client, LogClient())
    monitoring.log_cluster_health()
