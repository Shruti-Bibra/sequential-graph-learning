import networkx as nx
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np
import json

def visualize_clusters_tsne_labeled2(G, embeddings, cluster_label_file, cluster_attr, title="t-SNE Clustering Visualization"):
    """
    Visualize t-SNE plot with clusters labeled using string descriptions from a file.

    Args:
        G (nx.Graph): Graph with nodes containing cluster IDs under `cluster_attr`.
        embeddings (np.ndarray): Node embeddings aligned with list(G.nodes()).
        cluster_label_file (str): Path to .txt/.json file mapping 'Cluster N' → Label string.
        cluster_attr (str): Node attribute containing cluster ID (e.g., 'louvain').
        title (str): Title for the plot.
    """
    # Load cluster label mapping from file
    with open(cluster_label_file, 'r') as f:
        cluster_map_raw = json.load(f)

    # Convert "Cluster N" to int → label mapping
    cluster_map = {int(k.replace("Cluster ", "")): v for k, v in cluster_map_raw.items()}

    # Prepare cluster labels for nodes
    node_list = list(G.nodes())
    cluster_ids = [G.nodes[node].get(cluster_attr, -1) for node in node_list]
    cluster_labels = [cluster_map.get(cid, "Unknown") for cid in cluster_ids]
    #cluster_labels = [cluster_map[cid] for cid in cluster_ids]

    filtered_data = [
        (node, emb, label)
        for node, emb, label in zip(node_list, embeddings, cluster_labels)
        if label != "Unknown"
    ]

    if not filtered_data:
        print("[Warning] No nodes with known cluster labels to plot.")
        return

    filtered_nodes, filtered_embeddings, filtered_labels = zip(*filtered_data)
    filtered_embeddings = np.array(filtered_embeddings)

    # Reduce dimensions using t-SNE
    print("[t-SNE] Reducing dimensions for visualization...")
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    reduced = tsne.fit_transform(filtered_embeddings)

    # Plot
    plt.figure(figsize=(10, 7))
    unique_labels = sorted(set(cluster_labels))
    color_map = {label: idx for idx, label in enumerate(unique_labels)}
    #numeric_labels = [color_map[label] for cid in cluster_ids]
    #numeric_labels = [color_map[cluster_labels[i]] for i in range(len(cluster_ids))]
    numeric_labels = [color_map[label] for label in filtered_labels]


    scatter = plt.scatter(reduced[:, 0], reduced[:, 1], c=numeric_labels, cmap='tab10', s=10)

    label_counts = Counter(filtered_labels)
    top_10_labels = [label for label, _ in label_counts.most_common(10)]

    # Create a legend with readable labels
    handles = [
        plt.Line2D([], [], marker='o', linestyle='', color=scatter.cmap(color_map[label] / len(unique_labels)),
                   label=label)
        for label in top_10_labels
    ]
    plt.legend(handles=handles, title="Cluster Label",loc='upper left', bbox_to_anchor=(1, 1))

    plt.title(title)
    plt.xlabel("t-SNE 1")
    plt.ylabel("t-SNE 2")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
