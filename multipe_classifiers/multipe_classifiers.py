"""
multipe_classifiers.py
script

############################################
######  Written by: Mikolaj Buchwald  ######
############################################

Example of LDA, QDA, KNN and SVC and SelectKBest (feature selection)
of the Haxby's database.

Based on Alexandre Abraham's code:
    https://github.com/AlexandreAbraham/frontiers2013

Novum is splitting step (dataset divided into train and test
subsets) and classification performed on test data.
Leave-40%-samples-out cross validation has been performed to prove
the accuracy of the model (classifier - SVC)

Subject 001, data preprocessed with fsl:
    * brain extraction
    * motion correction
"""


# ### Load Haxby dataset ######################################################
import numpy as np
import nibabel

# ### Load data ###############################################################
# Path to directory with data

# data_dir = '/tmp/pymvpa-exampledata/'
data_dir = '/media/e0b555e6-cfa3-41fa-abd8-17ea6e249dc2/pymvpa-exampledata/'

func = data_dir+'bold.nii.gz'
session_target = data_dir+'attributes.txt'
brain_mask_file = data_dir+'mask.nii.gz'
conditions_target = data_dir+'attributes_literal.txt'

# fmri_data and mask are copied to break any reference to the original object
bold_img = nibabel.load(func)
fmri_data = bold_img.get_data().astype(float)
affine = bold_img.get_affine()
y, session = np.loadtxt(session_target).astype("int").T
conditions = np.recfromtxt(conditions_target)['f0']
brain_mask_img = nibabel.load(brain_mask_file)
brain_mask = brain_mask_img.get_data().astype(bool)

# After loading to python numpy:
#   * fmri_data.shape is (40, 64, 64, 1452)
#   * mask.shape is (40, 64, 64)


# ### Restrict to faces and houses ############################################
condition_mask = np.logical_or(conditions == 'face', conditions == 'house')
X = fmri_data[..., condition_mask]
y = y[condition_mask]-1

# ### Masking step ############################################################

# Mask data
X = X[brain_mask].T

# ### Sampling ################################################################
from sklearn.model_selection import train_test_split

# split original dataset into training and testing datasets
X, X_t, y, y_t = train_test_split(
    X, y, test_size=0.4, random_state=42
    )


###############################################################################
#                                                                             #
#   FAETURE REDUCTION                                                         #
#                                                                             #
###############################################################################

from sklearn.feature_selection import SelectKBest, f_classif

# ### Define the dimension reduction to be used.
# Here we use a classical univariate feature selection based on F-test,
# namely Anova. We set the number of features to be selected to 784
feature_selection = SelectKBest(f_classif, k=784)

# We fit the selector to our training dataset
feature_selection.fit(X, y)
# Transform training dataset
X = feature_selection.transform(X)
# Transform testing dataset
X_t = feature_selection.transform(X_t)


###############################################################################
#                                                                             #
#   CLASSIFIERS                                                               #
#                                                                             #
###############################################################################
# Define the estimator
from sklearn.lda import LDA
from sklearn.qda import QDA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
# regression, bayes


lda = LDA()
qda = QDA()
knn = KNeighborsClassifier(n_neighbors=5)
svc = SVC(kernel='linear', C=0.01)

models = [lda, qda, knn, svc]

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

for model in models:

    print('\n\n#############################################')
    print(model)

    # ### Fit and predict #####################################################

    # fit data, create hyperplane (model)
    model.fit(X, y)

    # prior chance level
    print('Prior chance: %0.2f \n' % (y_t.sum()/float(y_t.shape[0])))

    # predict samples' classes for TRAINING dataset (resubstitution)
    y_pred = model.predict(X)
    confusion_matrix_X = confusion_matrix(y, y_pred)

    accuracy_X = accuracy_score(y, y_pred)
    precision_X = precision_score(y, y_pred)

    print('training dataset')
    print('confusion_matrix')
    print(confusion_matrix_X)
    print('accuracy: %.2f' % accuracy_X)
    print('precision: %.2f' % precision_X)
    print('')

    # predict samples' classes for TESTING dataset
    y_pred_t = model.predict(X_t)
    confusion_matrix_X_t = confusion_matrix(y_t, y_pred_t)

    accuracy_X_t = accuracy_score(y_t, y_pred_t)
    precision_X_t = precision_score(y_t, y_pred_t)

    print('testing dataset')
    print('confusion_matrix')
    print(confusion_matrix_X_t)
    print('accuracy: %.2f' % accuracy_X_t)
    print('precision: %.2f' % precision_X_t)
    print('')
