## Topological Representations for Community Evolution Prediction

Understanding the evolution of online communities is crucial for
analyzing social dynamics on platforms during politically sensitive
periods. Using Louvain, HDBSCAN, and Ward clustering, we analyze community structures on a private X dataset collected during
an election period, and employ LLM-based labeling to assess semantic coherence, finding that Ward’s clusters are the most interpretable.
In addition, we propose TopoTemp, a novel framework combining
topological data analysis with sequential modeling to predict community evolution in temporal social networks, achieving consistent
improvements over baselines. Furthermore, we experiment on both
the X and Reddit Hyperlinks dataset to determine the impact of
snapshot-level, as well as community-level, topological features
when applied to community evolution prediction. This work highlights the importance of data granularity and feature selection in
dynamic network analysis and offers a practical foundation for
future research in community evolution prediction.

## Architecture

<img width="1918" height="474" alt="image" src="https://github.com/user-attachments/assets/c239d0bf-fc83-419c-adae-f65c60b48f43" />

## Results

the cluster labels we can clearly see that HDBSCAN has quite detailed and
inquisitive labels like "Breaking News", "Canada National News",
and "Sarcasm". While the other clustering methods are broader in
nature with labels like "Political Figures", "Religious Group", and
"LGBTQ+ Advocacy". Overall, Ward produces more intuitive and
well-separated clusters, often capturing clear distinctions such as
liberal versus conservative politics. In contrast, Louvain tends to
identify broader, less specific groupings, typically labeling clusters with high-level themes like political leader, group, or figure,
without distinguishing between ideological alignments. Furthermore, among the three algorithms, Louvain resulted in the highest
number of "unknown" clusters, while Ward’s has the fewest.

<img width="1966" height="660" alt="image" src="https://github.com/user-attachments/assets/ee4b3765-f893-4af7-b780-4e3b0467f7de" />





