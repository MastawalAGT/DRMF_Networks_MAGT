# DRMF_Networks_MAGT

This repository contains code for analysis and graphing for the paper of tenative title "Local and Global Electrical Transport in Variably Uniform Networks" in Daniels, Newhall, Rock et al.

Entropy_Metrics.py is a file containg python analysis code used in EntropyMetrics.ipynb

EntropyMetrics.ipynb can, from raw data in the oit-rs golubs drive on the Daniels lab ENO computer, execute analysis and make graphs. It also exports the data Jsons degree_entropy_examples, edge_entropy_examples, and resistance_entropy_lloyds_trends. These data sets are used by graphing_script.ipynb to produce the graphs for the paper. 

resistance_entropy_lloyds trends contains the average degree and entropy and average resistance per lloyds itteration for the networks and the std of the averages for network ensembles of N = 100, 200, 300 for use in graphing. 

degree_entropy_examples contains the degrees and edge weights of network ensemble PC10041 at lloyds itteration 0, 10, and 101 for use in graphing its edge and node distrobution at these different lloyds itterations.
