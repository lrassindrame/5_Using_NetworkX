import networkx as nx
import matplotlib.pyplot as plt

# Create a new directed graph
G = nx.DiGraph()

# Add edges (service pairs)
pairs = [("EC2", "S3"), ("Lambda", "DynamoDB"), ("RDS", "VPC"), ("Route 53", "S3"), ("IAM", "EC2"), ("Shield", "EC2"), ("Redshift", "Glue"), ("SQS", "Lambda"), ("Step Functions", "Lambda"), ("CloudWatch", "EC2"), ("CloudTrail", "IAM")]

# Add edges to the graph
G.add_edges_from(pairs)

# Draw the network
nx.draw(G, with_labels=True, node_size=800, node_color="lightblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
plt.title("Service Network Visualization")
plt.show()
