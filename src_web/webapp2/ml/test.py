import joblib

df_clf2 = joblib.load('webapp2/ml/iris_model.pkl')
iris_names = joblib.load('webapp2/ml/iris_names.pkl')

label = df_clf2.predict([[4.4, 2.9, 1.4, 0.2]])

print(iris_names[label][0])