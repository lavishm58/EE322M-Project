# Fast clustering Using Binary Tree
Rohan Raj (150107048) & Lavish Maheswari (150122021)
### Abstract
Clustering is widely used in unsupervised machine learning to separate data.We will use a new  clustering technique, which is based on a supervised learning technique called binary tree construction.The main idea is to use binary clustering as split parameter for binary tree construction.The algorigthm works very well to igive intuitive description of every splitted node, hence not only end results of clustering are available but the previous nodes of clusters also from which the end results are derived. 


### Introduction

A major question that comes in mind is how does a tree decide where to split. Decision tree uses multiple algorithms to decide the split in the decision node.The number of split is number of clusters (k) value provided.
The splitting criteria can be many like used in Hierarchical clustering, mean shift clustering, DBSCAN or any other type of criteria like otsu's algorithm. 
<p align="center">
	<img src="image/Decision_Tree_2.png"/>
</p>
 We have used a centroid comparison technique to decide label of a data point which is inspired by k-means 
 clustering splitting idea.However all of these algorithms have high time complexity. 	In this project we would like to extend clustering to binary tress for fast arrangement of data.

Although, not very much work is done on clustering using decision tree.So, this is purely a new technique to 
seperate similar data together and recursive splitting of clusters.

### Proposed Approach

The normal binary tree format is followed if k=2 for clustering.Each node splits the data after getting  optimal centroid for every cluster which splits data to 2 clusters.This splitting is continued for the output clusters obtained from root node.

The stopping criteria is decided by threshold, if a particular node contains less than 
N/20 training examples, it is considered as a leaf node which has majority of same labeled training data.

This method is very useful not only getting end results of all same labelled data clusters but also intuitive
description about clusters obtained in between leaf and root cluster, as algorithm can obtain accuracy of all
the clusters.  

### Dataset 

We have used a small dataset of size 777.
The number of attributes are 16 and labels are 5 and 6.


### Results 

The results are obtained with descriptions about the split of subset, number of
misclassifications, relative density and the features responsible for cuts.

Cluster 0
Leaf node has label 5 with accuracy 92%<br />
Cluster 1
Leaf node has label 6 with accuracy 66%<br />
Cluster 2
Leaf node has label 5 with accuracy 65%<br />
Cluster 3
Leaf node has label 6 with accuracy 62%<br />
Cluster 4
Leaf node has label 5 with accuracy 56%<br />
Cluster 5
Leaf node has label 5 with accuracy 58%<br />
Cluster 6
Leaf node has label 6 with accuracy 58%<br />
Cluster 7
Leaf node has label 5 with accuracy 70%<br />
Cluster 8
Leaf node has label 5 with accuracy 91%<br />
Cluster 9
Leaf node has label 6 with accuracy 66%<br />
Cluster 10
Leaf node has label 6 with accuracy 51%<br />
Cluster 11
Leaf node has label 5 with accuracy 84%<br />
Cluster 12
Leaf node has label 5 with accuracy 100%<br />
Cluster 13
Leaf node has label 6 with accuracy 84%<br />
Cluster 14
Leaf node has label 6 with accuracy 85%<br />
Cluster 15
Leaf node has label 6 with accuracy 64%<br />
Cluster 16
Leaf node has label 5 with accuracy 93%<br />
Cluster 17
Leaf node has label 5 with accuracy 95%<br />
Cluster 18
Leaf node has label 6 with accuracy 93%<br />
Cluster 19
Leaf node has label 6 with accuracy 96%<br />
Cluster 20
Leaf node has label 6 with accuracy 100%<br />
Cluster 21
Leaf node has label 6 with accuracy 96%<br />
Cluster 22
Leaf node has label 5 with accuracy 54%<br />
Cluster 23
Leaf node has label 5 with accuracy 81%<br />
Cluster 24
Leaf node has label 5 with accuracy 51%<br />

Average Total accuracy: 76.44%<br />

### References 

1. C. Aggarwal, C. Propiuc, J. L. Wolf, P. S. Yu, and J. S. Park (1999) A frame-
work for finding projected clusters in high dimensional spaces, SIGMOD-99
2. C. Aggarwal, and P. S. Yu (2000) Finding generalized projected clusters in high
dimensional spaces, SIGMOD-00
3. R. Agrawal, J. Gehrke, D. Gunopulos and P. Raghavan (1998) Automatic
subspace clustering for high dimensional data for data mining applications,
SIGMOD-98
4. R. Agrawal, S. Ghosh, T. Imielinski, B. Lyer, and A. Swami (1992) In interval
classifier for database mining applications, VLDB-92.
5. P. Arabie and L. J. Hubert (1996) An overview of combinatorial data analysis,
In P. Arabie, L. Hubert, and G.D. Soets, editors, Clustering and Classification,
pages 5-63
6. K. Beyer, J. Goldstein, R. Ramakrishnan and U. Shaft (1999) When is nearest
neighbor meaningful?” Proc.7th Int. Conf. on Database Theory (ICDT)
7. P. Bradley, U. Fayyad and C. Reina (1998) Scaling clustering algorithms to
large databases, KDD-98
8. C. H. Cheng, A. W. Fu and Y Zhang. ”Entropy-based subspace clustering for
mining numerical data.” KDD-99
9. R. Dubes and A. K. Jain (1976) Clustering techniques: the user’s dilemma,
Pattern Recognition, 8:247-260
10. M. Ester, H.-P. Kriegal, J. Sander and X.
