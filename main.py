from wormhole.opensearch_client import get_opensearch_client

if __name__ == "__main__":
    open_search_client = get_opensearch_client()
    client_info = open_search_client.get_client_info()
    cluster_version = client_info['version']['number']
    print(f"Open Search Cluster Version: {cluster_version}")
