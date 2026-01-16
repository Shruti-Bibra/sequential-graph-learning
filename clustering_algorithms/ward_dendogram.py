from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

Z = linkage(embeddings_pvt, method='ward')

# Plot the dendrogram to find natural cut-off points
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title("Dendrogram for Ward Clustering")
plt.xlabel("Samples")
plt.ylabel("Merge Distance")
plt.show()