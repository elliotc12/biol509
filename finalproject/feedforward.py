#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Maybe do PCA first, maybe just to see if there are relevant dimensions?
# Think about what good assessment metrics are good - learning curves, ROC
# Think about how to cross-validate, how to make sure you're not over-fitting
# Think about good things to do to data - PCA, normalization, outlier removal
# Look into Sacred as a log for python
# Snakemake as an alternative to make?
# Think about if we want to use/remove no-image data, or other data to throw out
# Could we combine data in any way, or no? Pare down to the lowest number of ROIs, or would that not work
# Use docstrings to descibe different functions
# Look for public data sets, like that one Yahya site
# Look into SVD

# Use stratified K fold since we have class imbalance
# Shuffle data to destroy time dependence
# Use estimator.get_params()
# Use a better scoring metric
# Visualize data by stimulus, see if you can spot trends by eye. This would be good to have in a talk
   # maybe plot signals (transformed or otherwise) per stimuli?
# Look into the 'rifit' parameter of GridSearchCV, and also diff between non/nested search
# You need to do a train/test split BEFORE GSCV, fit the parameters using the best CV, THEN evaluate the resultant optimized model on the test data

# Set iid to false for GridSearchCV
# Also set cv=5, specify 'Stratified'
# Best estimator through GridSearchCV's .best_estimator_ member
# Get mean/cv during GSCV, compare with test set
# Output results using classification_report

# Do activity (stimulus == 0) testing as a baseline

# Do nested GSCV to get the generalization score, then do GSCV on the whole set to get best estimator, then report that using classification_report

# Vary the # of vectors to reduce dataset down to

# make sure vectors don't have stimuli in them
# transform into a lower-dimensional space
# try a couple techniques on the lower- and higher-dimensional collapsed data sets

def get_parsed_data():
    fname = "vsdata1.txt"
    df = pd.read_table(fname, sep=" ", skiprows=1)
    print(np.)

if __name__ == "__main__":
    data = get_parsed_data()
