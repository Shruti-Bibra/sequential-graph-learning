import networkx as nx
import community as community_louvain  # python-louvain
from collections import Counter

def louvain_clustering(G):

    undirected_G = G.to_undirected()

    # Perform Louvain community detection
    partitions = community_louvain.best_partition(undirected_G)

    # Assign cluster labels to nodes
    for node, c in partitions.items():
        G.nodes[node]['louvain'] = c

    # Calculate the number of unique clusters
    num_clusters = len(set(partitions.values()))
    cluster_sizes = Counter(partitions.values())

    print("Number of clusters:", num_clusters)
    print("Cluster sizes:", cluster_sizes)

    return num_clusters, dict(cluster_sizes)