def hdbscan_clustering(embeddings, nodes, G, min_cluster_size=20):
    """
    Perform HDBSCAN clustering on node embeddings and assign labels to graph nodes.

    Args:
        embeddings (np.ndarray): Node embedding matrix.
        nodes (list): List of node IDs (same order as embeddings).
        G (networkx.Graph or networkx.DiGraph): The graph to assign node attributes.
        min_cluster_size (int): Minimum size for a cluster in HDBSCAN.

    Returns:
        node_to_cluster (dict): Mapping of node ID to cluster label.
        cluster_labels (np.ndarray): Array of cluster labels.
    """
    print("Running HDBSCAN clustering")
    clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, metric='euclidean')
    cluster_labels = clusterer.fit_predict(embeddings)

    node_to_cluster = dict(zip(nodes, cluster_labels))

    # Add cluster label as node attribute
    for node, HDBSCAN_label in zip(nodes, cluster_labels):
        G.nodes[node]['HDBSCAN'] = HDBSCAN_label

    # Cluster statistics
    label_counts = Counter(cluster_labels)
    num_clusters = len([label for label in label_counts if label != -1])
    num_clustered_nodes = sum(count for label, count in label_counts.items() if label != -1)

    print("\n=== Clustering Summary ===")
    print(f"Total nodes: {len(nodes)}")
    print(f"Number of clusters (excluding noise): {num_clusters}")
    print(f"Number of clustered nodes (excluding noise): {num_clustered_nodes}")
    print(f"Number of noise nodes: {label_counts.get(-1, 0)}")
    print("\nCluster sizes:")
    for label, count in label_counts.items():
        label_str = f"Cluster {label}" if label != -1 else "Noise"
        print(f"{label_str}: {count} nodes")

    return node_to_cluster, cluster_labels
