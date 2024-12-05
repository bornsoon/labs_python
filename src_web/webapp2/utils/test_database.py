from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../lab.db'
db = SQLAlchemy(app)

@app.route('/list')
def list():
    sql = 'select * from t_iris'
    df = pd.read_sql(sql, db.get_engine())
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)