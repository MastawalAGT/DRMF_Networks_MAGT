# DRMF_Networks_MAGT

This repository contains code for analysis and graphing for the paper of tenative title "Local and Global Electrical Transport in Variably Uniform Networks" in Daniels, Newhall, Rock et al.

Entropy_Metrics.py is a file containg python analysis code used in EntropyMetrics.ipynb

EntropyMetrics.ipynb can, from raw data in the oit-rs golubs drive on the Daniels lab ENO computer, execute analysis and make graphs. It also exports the data Jsons degree_entropy_examples, edge_entropy_examples, and resistance_entropy_lloyds_trends. These data sets are used by graphing_script.ipynb to produce the graphs for the paper. 

degree_entropy_examples contains the average degree entropy per lloyds itteration for the graphs and the std of the average for use in graphing, edge_entropy_examples is the same thing but for degree entropy 
