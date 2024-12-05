import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import io

from matplotlib.backends.backend_svg import FigureCanvasSVG

from flask import render_template, request, Response
from flask_sqlalchemy import SQLAlchemy

from webapp2 import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../lab.db'
db = SQLAlchemy(app)

@app.route('/iris/test')
def isis_test():
    sql = 'select * from t_iris'
    df = pd.read_sql(sql, db.get_engine())
    return df.to_json(orient='records')

@app.route('/iris/list')
def iris_list():
    return render_template('iris/list.html')

@app.route('/iris/ajax/list', methods=['POST'])
def iris_ajax_list():
    sql = 'select * from t_iris'
    df = pd.read_sql(sql, db.get_engine())

    return '{"data":' + df.to_json(orient='values') + '}'

@app.route('/iris/ajax/model', methods=['POST'])
def iris_ajax_model():
    sl = request.form['sl']
    sw = request.form['sw']
    pl = request.form['pl']
    pw = request.form['pw']

    df_clf = joblib.load('ml/iris_model.pkl')
    iris_names = joblib.load('ml/iris_names.pkl')

    label = df_clf.predict([[sl, sw, pl, pw]])
    return {'result': iris_names[label][0]}

@app.route('/iris/chart')
def iris_chart():
    return render_template('/iris/chart.html')

@app.route('/iris/chart/pie.png')
def iris_chart_pie():
    sql = 'select * from t_iris'
    df = pd.read_sql(sql, db.get_engine())

    species = df['species'].value_counts()
    keys = species.index
    data = species.values
    palette_color = sns.color_palette('bright')

    plt.rcParams['font.size'] = '20'

    fig = plt.figure()
    plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')
    plt.tight_layout()
    output = io.BytesIO()

    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")

@app.route('/iris/chart/datas', methods=['POST'])
def iris_chart_datas():
    result = {
        'labels': [n for n in range(2000, 2010)],
        'datas': np.random.randint(2000, 10000, size=10).tolist()
    }

    return result