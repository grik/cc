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

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

scores = [accuracy_score, precision_score, recall_score]

number_of_models = len(models)
number_of_runs = np.unique(session).shape[0]
number_of_scores = len(scores)

results = np.zeros((number_of_models, number_of_runs, number_of_scores))


for model in range(number_of_models):

    print('\n\n#############################################')
    print(models[model])

    for run in range(number_of_runs):

        X_train = X[-(session == run)[condition_mask]]
        y_train = y[-(session == run)[condition_mask]]
        X_test = X[(session == run)[condition_mask]]
        y_test = y[(session == run)[condition_mask]]

        #######################################################################
        #                                                                     #
        #   FAETURE REDUCTION                                                 #
        #                                                                     #
        #######################################################################

        from sklearn.feature_selection import SelectKBest, f_classif

        # ### Define the dimension reduction to be used.
        # Here we use a classical univariate feature selection based on F-test,
        # namely Anova. We set the number of features to be selected to 784
        feature_selection = SelectKBest(f_classif, k=784)

        # We fit the selector to our training dataset
        feature_selection.fit(X_train, y_train)
        # Transform training dataset
        X_train = feature_selection.transform(X_train)
        # Transform testing dataset
        X_test = feature_selection.transform(X_test)

        # ### Fit and predict #################################################

        # fit data, create hyperplane (model)
        models[model].fit(X_train, y_train)

        # predict samples' classes for TESTING dataset
        y_pred_test = models[model].predict(X_test)

        for score in range(number_of_scores):
            results[model][run][score] = scores[score](y_test, y_pred_test)

    for score in range(number_of_scores):
        print(scores[score])
        print(results[model, ..., score].mean())
        print('')
