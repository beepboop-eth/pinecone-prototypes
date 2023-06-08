import pinecone
import os

pinecone.init(api_key=os.environ["PINECONE_API_KEY"], environment="northamerica-northeast1-gcp")
index = pinecone.Index("quickstart2")

print(pinecone.list_indexes())
# pinecone.create_index("quickstart2", dimension=8, metric="euclidean")

# index.upsert([
#     ("A", [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]),
#     ("B", [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]),
#     ("C", [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
#     ("D", [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]),
#     ("E", [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
# ])

# print(index.describe_index_stats())
# pinecone.delete_index("quickstart2")