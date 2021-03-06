# Function to return the cluster (0 to 4) of a set of messages
# Packages needed:
# pickle
#
# Example usage:
# import pickle
# 
# List or array of messages:
# messages = ["Today less than asdfadf 12345 billion people have access to internet and clean water.\r\n", 
#             "health medical"]
# messages_clusters = description_cluster(messages, "text_based_clustering_model.pkl")
#
# Version: Python 3.6.4 Anaconda 64-bit
#
def description_cluster(messages_list_or_array, pickle_file_with_model):
    """
    messages_list_or_array:		List or array with messages to cluster.
    pickle_file_with_model:		Pickle file containing the model needed to cluster the messages.
                                It should contain a dictionary with the following attributes:
                                - 'bow_vectorizer': Bag Of Words obtained from CountVectorizer.fit() run on a set of messages
                                - 'tfidf_transformer': TF-IDF model obtained from tfidf_transformer.fit() run on a set of Bag Of Words
                                - 'U': left-eigenvector matrix of the SVD decomposition of the TF-IDF matrix
                                - 'cluster_model': k-means cluster model obtained from KMeans.fit()
                                - 'cluster_label': list with the humand-readable cluster labels
    """

    # Read model
    model = pickle.load(open(pickle_file_with_model, "rb"))
    print("Model details:")
    print(model)
    
    bow_vectorizer = model['bow_vectorizer']
    tfidf_transformer = model['tfidf_transformer']
    U = model['U']
    cluster_model = model['cluster_model']                   # This should be a K-means cluster model
    cluster_labels = model['cluster_labels']

    # 0) Normalize messages
    msg = [unicodedata.normalize('NFD', m) for m in messages_list_or_array]

    # 1) Compute the document-term frequency matrix for the message based on the learned vocabulary (n-grams)
    msg_bow = bow_vectorizer.transform(msg)

    # 2) Compute the TF-IDF matrix (used for projection)
    msg_tfidf = tfidf_transformer.transform(msg_bow)
    
    # 3) Project into SVD-reduced space and normalize
    A_new = msg_tfidf.T
    Ak_new = U.T*A_new
    Ak_new_norm = np.sqrt(np.sum(Ak_new * Ak_new, axis=0))
    Ak1_new = Ak_new / Ak_new_norm
    
    # 4) Cluster
    return([cluster_labels[c] for c in cluster_model.predict(Ak1_new.T)])
