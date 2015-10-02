"""
svc_pca.py
script

############################################
######  Written by: Mikolaj Buchwald  ######
############################################

Example of PCA (Principal Component Analysis - feature extraction method
and SVC (Support Vector Classification) of the Haxby's database.

Based strongly on Alexandre Abraham's code:
    https://github.com/AlexandreAbraham/frontiers2013

Novum in this example is:
    * use of PCA instead of SelectKBest as dimensionality reduction method,
    * sampling step (split original dataset train and test subsets) and
    classification performed on test data.

Subject 001, data preprocessed with fsl:
    * brain extraction
    * motion correction
"""

# ### Load Haxby dataset ######################################################
import numpy as np
import nibabel
from sklearn.datasets.base import Bunch

from os.path import expanduser
from pymri.model.visualisation import plot_haxby

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

# fmri_data.shape is (40, 64, 64, 1452)
# and mask.shape is (40, 64, 64)

# ### Preprocess data
# Build the mean image because we have no anatomic data
mean_img = fmri_data.mean(axis=-1)


# ### Restrict to faces and houses
condition_mask = np.logical_or(conditions == 'face', conditions == 'house')
X = fmri_data[..., condition_mask]
y = y[condition_mask]
# session = session[condition_mask]
# conditions = conditions[condition_mask]

# ### Masking step
# from utils import masking, signal
from pymri.utils import masking
from nibabel import Nifti1Image

# Mask data
X_img = Nifti1Image(X, affine)
X = masking.apply_mask(X_img, mask, smoothing_fwhm=4)
# X = signal.clean(X, standardize=True, detrend=False)


# ### Sampling ################################################################
from sklearn.cross_validation import train_test_split

# split original dataset into training and testing datasets
X, X_t, y, y_t = train_test_split(
    X, y, test_size=0.4, random_state=42
    )

###############################################################################
#                                                                             #
#   SVC                                                                       #
#                                                                             #
###############################################################################
# Define the estimator
from sklearn.svm import SVC
clf = SVC(kernel='linear', C=0.01)

# ### Dimension reduction #####################################################

from sklearn.decomposition import PCA

# PCA model creation, number of components
# feature extraction method. Used here (after sampling) because we are
# creating an universal model and not this_dataset-specific.
feature_extraction = PCA(n_components=500)

# We have our classifier (SVC), our feature extraction (PCA), and now,
# we can plug them together in a *pipeline* that performs the two operations
# successively:
from sklearn.pipeline import Pipeline
pca_svc = Pipeline([('pca', feature_extraction), ('svc', clf)])

# ### Fit and predict #########################################################
from sklearn.metrics import precision_score

# fit data, create new feature space transformation (model)
pca_svc.fit(X, y)

# predict samples' classes for TRAINING dataset
y_pred = pca_svc.predict(X)
precision_X = precision_score(y, y_pred)
print('train dataset precision: %.2f' % (precision_X))

# predict samples' classes for TESTING dataset
y_pred_t = pca_svc.predict(X_t)
precision_X_t = precision_score(y_t, y_pred_t)
print('test dataset precision: %.2f' % (precision_X_t))

# ### Visualisation (SVC) #####################################################
import numpy as np

# ### Look at the discriminating weights
coef = clf.coef_
# reverse feature selection
coef = feature_extraction.inverse_transform(coef)

# reverse masking
coef = masking.unmask(coef[0], mask)

# # We use a masked array so that the voxels at '-1' are displayed
# # transparently
act = np.ma.masked_array(coef, coef == 0)


plot_haxby(act, mean_img, 'PCA')

# save statistical map as nifti image
img = nibabel.Nifti1Image(act, np.eye(4))
img.to_filename('output_stats.nii.gz')

# ### Visualisation (PCA) #####################################################

Z = feature_extraction.transform(X)
C = feature_extraction.transform(X_t)

# plot data in 2D (i.e. plot two main components)
import matplotlib.pyplot as plt
for i in range(len(Z)):
    if y[i] == 1:
        marker = '^'
        col = 'b'
    else:
        marker = 'o'
        col = 'r'
    plt.scatter(Z[i][0], Z[i][1], c=col, marker=marker, s=100)
for i in range(len(C)):
    if y_t[i] == 1:
        marker = '^'
        col = 'g'
    else:
        marker = 'o'
        col = 'y'
    plt.scatter(C[i][0], C[i][1], c=col, marker=marker, s=100)

plt.show()
