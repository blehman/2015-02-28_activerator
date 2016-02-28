
#!/usr/bin/env python

#inside ipython:
#%matplotlib inline
#sqlContext = SQLContext(sc)
#from imports import *


# general tools
import ujson as json
import itertools
import pickle
import gzip
import operator
import os
import sys
from time import time
import pprint as pp
import collections
import ConfigParser
import copy
from datetime import datetime

# numpy and pandas
import numpy as np
import pandas as pd

# scipy
import scipy.sparse as sps

# sklearn
#from sklearn.pipeline import make_pipeline
#from sklearn.preprocessing import Normalizer
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.decomposition import TruncatedSVD
#from sklearn.cross_validation import train_test_split
#from sklearn.cluster import KMeans, MiniBatchKMeans
#from sklearn.externals import joblib
#from sklearn.linear_model import SGDClassifier
#from sklearn.ensemble import AdaBoostClassifier
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.decomposition import PCA
#from sklearn.cluster import KMeans as sklearn_kmeans
#from sklearn import metrics
#from sklearn.ensemble import GradientBoostingClassifier
#from sklearn.neighbors.nearest_centroid import NearestCentroid
#from sklearn.ensemble import BaggingClassifier

# pyspark
#from pyspark.mllib.linalg.distributed import RowMatrix
#from pyspark.mllib.linalg import Matrices
#from pyspark.sql import Row
#from pyspark.mllib.linalg import Vectors
#from pyspark.ml.feature import RegexTokenizer
#from pyspark.ml.feature import Bucketizer
#from pyspark.ml.feature import NGram
#from pyspark.ml.clustering import KMeans
#
# needed?
#from pyspark.mllib.linalg import SparseVector
#from pyspark.mllib.regression import LabeledPoint
#from pyspark.mllib.classification import LogisticRegressionWithSGD
#from pyspark.mllib.classification import LogisticRegressionWithLBFGS

# sqlcontext
#from pyspark.sql import SQLContext

# bokeh
import bokeh.plotting as bkplt
from bokeh.io import output_notebook

# matplotlib
import matplotlib.pyplot as plt

# ipynb display
from IPython.display import Image
from IPython.display import display
