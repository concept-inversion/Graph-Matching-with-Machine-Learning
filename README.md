# Graph-Matching-with-Machine-Learning
This project tries to address graph similarity.

Files:
1. The file DD.mat in datasets/ folder is used to get Adjacency matrices of protiens.

2. eigen.py: It has methods to get laplacian of a matrix by getting, and ultimately eigen vectors.

3. five_node_test.ipynb: Has code to test a graph with 5 nodes and display similarities and other distance metrics.

4. seven_node_test.ipynb: Has code to test a graph with 7 nodes and display similarities and other distance metrics.

5. twelve_node_test.ipynb: Has code to test a graph with 12 nodes and display similarities and other distance metrics.

6. generate_dataset.py: Generates positive and negative adjancecy matrices given a adjacency matrix.

7. process_data.py: Has code to get the DD.mat file from datasets/ folder and get the adjacency matrix from a list of adjacency matrices based on passed index.

8. test.py: This file is used to test on real datasets, i.e. DD.mat. It has a method that tests the original matrix chosen by calling process_data.py with other positive and negative matches by generating these positive and negative matches and hence finding distance metrics.

9. similarity_algorithms.py: Has functions that can be used to calculate Euclidean, Minkowski, and Manhattan distances, given two eigen vectors.

Steps to run custom graphs with 5, 7 and 12 nodes:
1. Go to file five_node_test.ipynb or seven_node_test.ipynb or twelve_node_ipynb in your IDE like VS code.
2. Click on first cell.
3. Click on "Run cell and below".
Scroll down and see all results.

Steps to run real datasets from DD.mat:
1. Go to file test.py on your IDE.
2. Run command "python test.py" in terminal to run the code.
This file reads DD.mat's adjacency matrix of index "x" defined in code, then creates 20 positive/negative adjacency matrices based on original matrix and tests different distance metrics of original matrix with all other generated matrices. Comment/uncomment line #25/#26 to generate positive/negative matrices for comparision.
