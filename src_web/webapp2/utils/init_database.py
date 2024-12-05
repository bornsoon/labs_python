from sklearn.datasets import load_iris
iris = load_iris()

# print(iris)
import pandas as pd
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['label'] = iris.target
df['species'] = iris.target_names[iris.target]

print(df.head())

from sqlalchemy import create_engine
engine = create_engine('sqlite:///../../lab.db')
df.to_sql(name='t_iris', con=engine, if_exists='replace')   # (if_exists >> 'fail', 'append'), 'replace'는 집계 컬럼과 같이 업데이트 할 때

sql = 'select * from t_iris'
df = pd.read_sql(sql, engine)
print(df.head())
