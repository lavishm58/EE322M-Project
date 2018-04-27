# Fast clustering Using Decision Tree
Rohan Raj (150107048) & Lavish Maheswari (150122021)
### Abstract
Clustering is widely used in unsupervised machine learning to separate data.We will use a new  clustering technique, which is based on a supervised learning technique called decision tree construction.The main idea is to use a decision tree to partition the data space into cluster and sparse regions.First, new data points are introduced into the space and then a modified decision tree algorithm is applied.This method works well for large high dimensional
spaces efficiently.

### Introduction

Decision tree learning is a supervised machine learning approach that uses a decision tree to go from decision on observation values(branches) to conclusion about item's target class (leaves) . Trees provides high accuracy, stability and ease of interpretation in classification problems. 
An example of a simple decision tree is shown by the following image.
<p align="center">
	<img src="image/Decision_Tree_2.png"/>
</p>
A major question that comes in mind is how does a tree decide where to split. Decision tree uses multiple algorithms to decide the split in the
decision node. Commonly used algorithm in the decision tress measures Gini index, Chi-Square, Information gain or Reduction in Variance to decide 
the split in the decision node. However all of these algorithms have high time complexity. 	In this project we would like to extend hierarchical clustering
to decision tress for fast arrangement of data.


In this paper, we study clustering in a numerical space, where each di-mension (or attribute) has a bounded and totally ordered domain. Each data
record is basically a point in the space. Clusters in such a space are commonly
defined as connected regions in the space containing a relatively high density
of points, separated from other such regions by a region containing a relatively
low density of points

### Proposed Approach
We use an example to show the intuition behind the proposed technique.
Figure 1(A) gives a 2-dimensional space, which has 24 data (Y ) points rep-
resented by filled rectangles. Two clusters exist in the space. We then add
some uniformly distributed N points (represented by ”o”) to the data space
(Figure 1(B)). With the augmented dataset, we can run a decision tree algo-
rithm to obtain a partitioning of the space (Figure 1(B)). The two clusters
are identified.
The reason that this technique works is that if there are clusters in the
data, the data points cannot be uniformly distributed in the entire space.By adding some uniformly distributed N points, we can isolate the clusters
because within each cluster region there are more Y points than N points.
The decision tree technique is well known for this task.

1) how many N points should
we add, and (2) can the same task be performed without physically adding the
N points to the data?The
number changes as the tree grows. It is insufficient to add a fixed number of N
points to the original dataset at the beginning (see Section 2.2). The answer
to the second question is yes. Physically adding N points increases the size
of the dataset and also the running time.

The proposed CLTree technique consists of two steps:

1) Cluster tree construction: This step uses a modified decision tree algorithm
with a new purity function to construct a cluster tree to capture the
natural distribution of the data without making any prior assumptions.

2)Cluster tree pruning: After the tree is built, an interactive pruning step
is performed to simplify the tree to find meaningful/useful clusters. The
final clusters are expressed as a list of hyper-rectangular regions.

### Building Tree
The algorithm for building a decision tree typically uses the divide and
conquer strategy to recursively partition the data to produce the tree.

inf o X (D)

gain(X) = inf o(D) − inf o X (D) 

### Building 

### Dataset 

The dataset has 12 clusters and 5 dimensions.
Size of dataset is 804

### Results 



Cluster 0
Node: 
29 instances, 0 misclassified, 100% 701, 100 relative density 
Cuts {'dim3', 'dim2', 'dim4', 'dim0', 'dim1'}
dim0 max: 254.69675232465048 min: 224.20357516054443
dim1 max: 206.1862528210675 min: 5.190836527707465
dim2 max: 976.3666547354335 min: 927.5042081847703
dim3 max: 193.7491530020439 min: 136.21988447225175
dim4 max: 929.1536480603974 min: 32.46006671289536

Cluster 1
Node: 
19 instances, 0 misclassified, 100% 301, 100 relative density 
Cuts {'dim3', 'dim2', 'dim0', 'dim1'}
dim0 max: 962.1603414509655 min: 923.9130257944147
dim1 max: 172.2029640136189 min: 7.924708280993231
dim2 max: 789.992332195958 min: 771.2605895712188
dim3 max: 263.7076455927995 min: 225.51485810031943
dim4 max: 945.1674404097963 min: 41.342229783885685

Cluster 2
Node: 
22 instances, 0 misclassified, 100% 200, 100 relative density 
Cuts {'dim3', 'dim2', 'dim4', 'dim0', 'dim1'}
dim0 max: 240.628022938997 min: 17.576143658934452
dim1 max: 173.48777204911167 min: 158.64894054588657
dim2 max: 53.13910978648526 min: 35.12401685382305
dim3 max: 653.815023433192 min: 632.4151209026564
dim4 max: 573.6401199167576 min: 517.2481967409421

Cluster 3
Node: 
22 instances, 0 misclassified, 100% 200, 100 relative density 
Cuts {'dim3', 'dim2', 'dim4', 'dim0', 'dim1'}
dim0 max: 638.378329543906 min: 256.4877110888415
dim1 max: 168.34823873566162 min: 158.14171158181716
dim2 max: 54.6030055765337 min: 37.4717082761719
dim3 max: 656.3117205440806 min: 633.5320878016806
dim4 max: 578.2313339123309 min: 515.1843216285704

Cluster 4
Node: 
19 instances, 0 misclassified, 100% 201, 32 relative density 
Cuts {'dim3', 'dim2', 'dim0', 'dim1'}
dim0 max: 975.398342102654 min: 23.38914272448589
dim1 max: 202.07864786650325 min: 190.39055002282907
dim2 max: 82.02025043651503 min: 60.20360830755551
dim3 max: 681.8416394882013 min: 651.3308749908896
dim4 max: 922.2060321505132 min: 19.35700277640273

Cluster 5
Node: 
19 instances, 0 misclassified, 100% 201, 59 relative density 
Cuts {'dim3', 'dim2', 'dim0', 'dim1'}
dim0 max: 968.3111630088113 min: 76.63219248200426
dim1 max: 199.88770453859857 min: 166.12914315012637
dim2 max: 79.45090749199282 min: 45.52207050855784
dim3 max: 691.9622273888685 min: 684.7247841915693
dim4 max: 989.9965089956665 min: 30.463559787844208

Cluster 6
Node: 
17 instances, 1 misclassified, 94% 701, 100 relative density 
Cuts {'dim0', 'dim4', 'dim2', 'dim3', 'dim1'}
dim0 max: 464.2953481675183 min: 227.75011270426435
dim1 max: 575.1720657217475 min: 444.1795859968598
dim2 max: 967.7152556826785 min: 930.8588271871524
dim3 max: 398.95258476770965 min: 134.0370600108329
dim4 max: 965.038266772788 min: 26.471606209095057

Cluster 7
Node: 
273 instances, 117 misclassified, 57% 100, 100 relative density 
Cuts {'dim3', 'dim4', 'dim0', 'dim1'}
dim0 max: 62.76544442749074 min: 15.651128853954408
dim1 max: 687.2831777713362 min: 629.9993779936235
dim2 max: 991.9719862461911 min: 5.372973284257121
dim3 max: 820.6255601096218 min: 32.90036706886546
dim4 max: 307.0625969210362 min: 237.70092012230538

Cluster 8
Node: 
151 instances, 0 misclassified, 100% 501, 100 relative density 
Cuts {'dim3', 'dim4', 'dim0', 'dim1'}
dim0 max: 478.08590718216834 min: 434.10573363360714
dim1 max: 866.248944302787 min: 820.4991233464903
dim2 max: 995.4631948659544 min: 10.235848871282482
dim3 max: 358.45057009237746 min: 316.6044032961324
dim4 max: 902.847190279711 min: 840.8536859747837

Cluster 9
Node: 
27 instances, 0 misclassified, 100% 601, 100 relative density 
Cuts {'dim3', 'dim2', 'dim4', 'dim0', 'dim1'}
dim0 max: 561.9225714412245 min: 538.3610207796331
dim1 max: 752.5094213122288 min: 732.8657839831341
dim2 max: 800.5868929387598 min: 15.137502833868165
dim3 max: 749.2076388139174 min: 734.3316487604263
dim4 max: 955.2602009342439 min: 937.2278023222284

Cluster 10
Node: 
33 instances, 16 misclassified, 51% 302, 13 relative density 
Cuts {'dim3', 'dim4', 'dim0', 'dim1'}
dim0 max: 911.916180121605 min: 662.5745772116724
dim1 max: 986.3003371483435 min: 294.1497198278628
dim2 max: 877.3152637339153 min: 8.232561853376508
dim3 max: 803.6595342040058 min: 82.77917190687256
dim4 max: 816.2424118908528 min: 89.89562034279753

Cluster 11
Node: 
24 instances, 0 misclassified, 100% 301, 63 relative density 
Cuts {'dim3', 'dim2', 'dim4', 'dim0', 'dim1'}
dim0 max: 967.9342421631413 min: 912.5520078043219
dim1 max: 999.4763230788816 min: 777.4652541976975
dim2 max: 788.203606970544 min: 761.0532258809538
dim3 max: 261.863859544531 min: 222.0571453153609
dim4 max: 973.7348449554071 min: 77.86448951801151

Cluster 12
Node: 
149 instances, 1 misclassified, 99% 401, 100 relative density 
Cuts {'dim3', 'dim4', 'dim0'}
dim0 max: 173.04114019485687 min: 21.588530110535963
dim1 max: 996.1926077111222 min: 2.6515474910964176
dim2 max: 371.4783351842746 min: 256.6000878954098
dim3 max: 997.5775264212 min: 935.2868246831398
dim4 max: 785.2095547030349 min: 621.5252628692459

### Related Work

In computer vision , Otsu's method does clustering using thresold on one dimentional data. This algorithm is very fast and is widely used 
for reduction of a graylevel image to a binary image . This method is approximately a 1-D discrete analog of FDA( Fisher's Discriminant Analysis). However this
method works well with 1-D data. An extesion of this method to multi dimentional data is the focus of study in this project.