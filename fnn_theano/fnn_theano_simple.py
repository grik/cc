"""
fnn_theano_simple.py
script

############################################
######  Written by: Mikolaj Buchwald  ######
############################################

Example of FNN (Feedforward Neural Network) and
SelectKBest (feature selection) of the Haxby's database.

Based strongly on Alexandre Abraham's code:
    https://github.com/AlexandreAbraham/frontiers2013

Novum is sampling step (split original dataset train and test
subsets) and classification performed on test data.
Leave-40%-samples-out cross validation has been performed to prove
the accuracy of the model (classifier - FNN)

Subject 001, data preprocessed with fsl:
    * brain extraction
    * motion correction
"""


# ### Load Haxby dataset ######################################################
import numpy as np
import nibabel
from sklearn.datasets.base import Bunch

from os.path import expanduser

# ### Load data ###############################################################
# Path to direcotry with data
# data_dir = expanduser('~') + '/workshops/aiml/data/pymvpa-exampledata/'
data_dir = expanduser('~') + '/downloads/pymvpa-exampledata/'

# create sklearn's Bunch of data
dataset_files = Bunch(
    func=data_dir+'bold.nii.gz',
    session_target=data_dir+'attributes.txt',
    mask=data_dir+'mask.nii.gz',
    conditions_target=data_dir+'attributes_literal.txt'
    )

# fmri_data and mask are copied to break any reference to the original object
bold_img = nibabel.load(dataset_files.func)
fmri_data = bold_img.get_data().astype(float)
affine = bold_img.get_affine()
y, session = np.loadtxt(dataset_files.session_target).astype("int").T
conditions = np.recfromtxt(dataset_files.conditions_target)['f0']
mask = dataset_files.mask

# After loading to python numpy:
#   * fmri_data.shape is (40, 64, 64, 1452)
#   * mask.shape is (40, 64, 64)


# ### Restrict to faces and houses ############################################
condition_mask = np.logical_or(conditions == 'face', conditions == 'house')
X = fmri_data[..., condition_mask]
y = y[condition_mask]
y -= 1

# ### Masking step ############################################################
from pymri.utils import masking
from nibabel import Nifti1Image

# Mask data
X_img = Nifti1Image(X, affine)
X = masking.apply_mask(X_img, mask, smoothing_fwhm=4)
# X = signal.clean(X, standardize=True, detrend=False)

# ### Sampling ################################################################
from sklearn.model_selection import train_test_split

# split original dataset into training and testing datasets
X, X_t, y, y_t = train_test_split(
    X, y, test_size=0.4, random_state=42
    )

###############################################################################
#                                                                             #
#   FNN                                                                       #
#                                                                             #
###############################################################################
# Define the estimator
from pymri.model.ann.theano_script import Network
from pymri.model.ann.theano_script import ConvPoolLayer
from pymri.model.ann.theano_script import FullyConnectedLayer
from pymri.model.ann.theano_script import SoftmaxLayer
mini_batch_size = 20

net = Network([
    FullyConnectedLayer(n_in=300, n_out=600),
    SoftmaxLayer(n_in=600, n_out=2)],
    mini_batch_size
    )


# ### Dimensionality reduction ################################################

from sklearn.feature_selection import SelectKBest, f_classif

# ### Define the dimension reduction to be used.
# Here we use a classical univariate feature selection based on F-test,
# namely Anova. We set the number of features to be selected to 784
feature_selection = SelectKBest(f_classif, k=300)

# We fit the selector to our tr6ining dataset
feature_selection.fit(X, y)
# Transform training dataset
X = feature_selection.transform(X)
# Transform testing dataset
X_t = feature_selection.transform(X_t)


# ### Train and test classifier ###############################################

# prior chance level
print('Prior chance: %0.2f' % (y_t.sum()/float(y_t.shape[0])))

# prepare data in the format acceptable by theano scripts
from pymri.model.ann.theano_script import share_data
training_data, test_data = share_data((X, y), (X_t, y_t))

net.SGD(training_data, 500, mini_batch_size, 3., test_data, verbose=1)


# from sklearn.metrics import confusion_matrix
