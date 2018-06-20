Content of code directory
-------------------------
Created: DM-2018/06/15
Goal: Describe here the creation date, the creator, the source, the goal of having the code/file and a brief description, by filling in the respective entries for each new code/file, as shown in the first file entry below.


readme-code.txt
---------------
Date: 2018/06/15
Creator: Daniel
Source: fmdsf team
Goal: Have a common understanding of the code/notebooks we work with and why we have created them.
Description: List and brief description of code/notebooks/etc. we use during the project development.

Daniel - startup.ch - Text Mining - Cluster Description.ipynb
-------------------------------------------------------------
Date: 2018/06/18
Creator: Daniel
Source: fmdsf team
Goal: Cluster the startup companies into a few categories (clusters) based on their description.
Description: An SVD is run on the TF-IDF (Term Frequency - Inverse Document Frequency) matrix constructed on the Description field of the 667 companies in the 'startup.ch 2013 - 2018' dataset. A K-means cluster algorithm is run on the top singular vectors (typically 3) classifying the companies into e.g. 5 clusters.

Federica.ipynb
-------------------------------------------------------------
Date: 2018/06/20
Creator: Federica
Source: fmdsf team
Goal: Clean and preprocess data, identify and fix data quality issues, inspect startup location and description, add information corresponding to how many times a startup won in the past, train and apply a SVM classifier for one-class classification (winners only).
Description: Get data corresponding to winners of 2011-2017 and eligible of 2018 from Excel files. Deal with missing values and inconsistency in the data format. Add information corresponding to how many times a startup won in the past, since this might be an indication of how good the startup is. Use folium and geocoder to assign latitude and longitude to each startup and to display the startup location in Switzerland. Fix issue related to multiple locations with the same name. Use the latitude and longitude as features of the SVM classifier. The other features are the number of previously won competitions, the foundation year, and a score ("unique_score") corresponding to the number of matches between the keywords in the description of the startup and the keywords of the winners of 2011-2017. The latter can be replaced with other numerical features linked to textual information. The SVM classifier is trained and tested on the winners of 2011-2017 using cross-validation. See precision, recall, and accuracy. The output of the SVM classifier is 1 or -1, so no ranking information is available. To be replaced with another model that returns a ranking (first 100). Ideas for the future: add sentiment analysis from Twitter, score corresponding to positive, negative, neutral. 

get_clean_data.py
-------------------------------------------------------------
Date: 2018/06/20
Creator: Federica
Source: fmdsf team
Goal: Clean data.
Description: Similar to the get_clean_data() function in Federica.ipynb.
