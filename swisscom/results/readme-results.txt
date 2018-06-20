Content of results directory
----------------------------
Created: DM-2018/06/15
Goal: Describe here the creation date, the creator, the source, the goal of having this document and a brief description, by filling in the respective entries for each new document, as shown in the first document entry below.


readme-results.txt
------------------
Date: 2018/06/15
Creator: Daniel
Source: fmdsf team
Goal: Have a common understanding of the documents we work with and why we consider them to be relevant. 
Description: List and brief description of documents we use to show the relevant results of the project.

Daniel/DescriptionBasedClustering/daniel_startupch_description_based_clustering_model.pkl
-----------------------------------------------------------------------------------------
Date: 2018/06/18
Creator: Daniel
Source: fmdsf team
Goal: Use the cluster to which a startup company belongs (company category) as a predictor variable of a successful startup.
Description: Pickle file containing a dictionary with the following entries:
	- bow_vectorizer:
		the Bag Of Words (words = n-grams) model obtained by running the CountVectorizer.fit() method on the Description field of the 'startups.ch 2013 - 2018' data.
		This piece of information is used to transform() each input message into a bag of "words in the training vocabulary".
	- tfidf_transformer:
		the TF-IDF transformer obtained by running the TfidfTransfomer.fit() method on the bag of "words in the training vocabulary".
		This piece of information is used to transform() the bag of words in the input descriptions to get the TF-IDF matrix for those descriptions.
	- U:
		the matrix containing the left singular vectors of the SVD run on the TF-IDF matrix (using scipy.sparse.linalg.svds()) of the company descriptions used for training.
		This piece of infomration is used to project each input description to the SVD-reduced space (typically of 2-3 dimensions).
	- cluster_model:
		the clustering model obtained by running the KMeans.fit() method.
	- cluster_labels:
		list containing the cluster "human" labels (e.g. "2 - Medical")

Slide.key, Slide.pdf
--------------------
Date: 2018/06/20
Creator: Federica
Source: fmdsf team
Goal: The slide of the final pitch of the project.
Description: The slide of the final pitch of the project.

Trends.pdf
----------
Date: 2018/06/20
Creator: Federica
Source: fmdsf team
Goal: Show the number of winners in each sector.
Description: Show the number of winners in each sector.
