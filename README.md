# Fast hierarchical clustering to Arrange Data
Rohan Raj (150107048) & Lavish Maheswari (150107048)
### Abstract
Clustering is widely used in unsupervised machine learning to separate data. Hierarchical clustering
is a method which seeks to build a hierarchy of clusters in the data. However, this is a slow algorithm with a 
time complexity of O(N <sup>3</sup> ). In this project our aim is to develope a fast clustering mechanism 
for binary separation of data at nodes of decision tree.

### Introduction

Decision tree learning is a supervised machine learning approach that uses a decision tree to go from decision on observation values(branches)
to conclusion about item's target class (leaves) . Trees provides high accuracy, stability and ease of interpretation in classification problems. 
An example of a simple decision tree is shown by the following image.
<p align="center">
	<img src="image/Decision_Tree_2.png" class="img-responsive" alt=""/>
</p>
A major question that comes in mind is how does a tree decide where to split. Decision tree uses multiple algorithms to decide the split in the
decision node. Commonly used algorithm in the decision tress measures Gini index, Chi-Square, Information gain or Reduction in Variance to decide 
the split in the decision node. However all of these algorithms have high time complexity. 	In this project we would like to extend hierarchical clustering
to decision tress for fast arrangement of data.

### Related Work

In computer vision , Otsu's method does clustering using thresold on one dimentional data. This algorithm is very fast and is widely used 
for reduction of a graylevel image to a binary image . This method is approximately a 1-D discrete analog of FDA( Fisher's Discriminant Analysis). However this
method works well with 1-D data. An extesion of this method to multi dimentional data is the focus of study in this project.