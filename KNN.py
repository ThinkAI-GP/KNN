#requirements 
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set()

#we first load our dataser into dataframes
breast_cancer = load_breast_cancer()
X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
X = X[['mean area', 'mean compactness']]
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
y = pd.get_dummies(y, drop_first=True)



X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)



thinkAI_knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
thinkAI_knn.fit(X_train, y_train)



y_pred = thinkAI_knn.predict(X_test)


#we compare the prediction results with the actual ones 

sns.scatterplot(
    x='mean area',
    y='mean compactness',
    hue='benign',
    data=X_test.join(y_test, how='outer')
)




plt.scatter(
    X_test['mean area'],
    X_test['mean compactness'],
    c=y_pred,
    cmap='coolwarm',
    alpha=0.7
)


# another way to calculate precision is confusion matrix


confusion_matrix(y_test, y_pred)


# In[ ]:




