from scipy.cluster.hierarchy import linkage, fcluster
import numpy as np
from collections import defaultdict

def ward_clustering_auto(embeddings, nodes, G):
    """
    Perform Ward hierarchical clustering and assign cluster IDs as node attributes.

    Args:
        embeddings (np.ndarray): Node embeddings.
        nodes (List): List of node IDs corresponding to the embeddings.
        G (nx.Graph or nx.DiGraph): The graph with those nodes.

    Returns:
        labels_dict (dict): {cluster_id: number of nodes in that cluster}
        n_clusters (int): Estimated number of clusters
        labels (np.ndarray): Cluster label array
    """
    print("[Ward] Performing linkage")
    Z = linkage(embeddings, method='ward')

    print("[Ward] Estimating optimal number of clusters")
    # You can tune the threshold `t` here
    labels = fcluster(Z, t=17.0, criterion='distance')

    # Count how many nodes in each cluster
    labels_dict = defaultdict(int)
    for label in labels:
        labels_dict[label] += 1

    labels_dict = dict(labels_dict)
    n_clusters = len(np.unique(labels))

    print(f"Number of clusters: {n_clusters}")
    print(f"Cluster sizes: {labels_dict}")

    #Add cluster ID as a node attribute 'ward'
    for node, Ward_label in zip(nodes, labels):
        G.nodes[node]['ward'] = Ward_label

    return labels_dict, n_clusters, labels