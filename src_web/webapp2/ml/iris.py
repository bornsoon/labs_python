from sklearn.datasets import load_iris
iris = load_iris()

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=15)

df_clf = DecisionTreeClassifier(random_state=15)

df_clf.fit(X_train, y_train)
y_pred = df_clf.predict(X_test)

import joblib
joblib.dump(df_clf, 'webapp2/ml/iris_model.pkl')
joblib.dump(iris.target_names, 'webapp2/ml/iris_names.pkl')

df_clf2 = joblib.load('webapp2/ml/iris_model.pkl')
label = df_clf2.predict([[4.4, 2.9, 1.4, 0.2]])

print(iris.target_names[label])