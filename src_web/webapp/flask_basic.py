from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# CORS: 허용
CORS(app, resources={r'*':{'origins':['http://localhost:8080']}})
# CORS(app, resources={r'/api/*':{'origins':['http://localhost:8080']}})

# 1. 문자열 반환
@app.route('/')
def index():
    return '<h1>Hello World!!!</h1>'

# 2.
@app.route('/name')
def name():
    return __name__

# 3. Escape
from markupsafe import escape
@app.route('/html')
def tag_escape():
    return escape('<h1>Hello World!!!</h1>')

# 4.
@app.route('/user/<name>')
def user_name(name):
    return f'이름: {name}'

@app.route('/user/<int:age>')
def user_age(age):
    return f'나이: {age}'

@app.route('/hello')
@app.route('/hello/message')
def hello():
    return '<h1>Hello World!!!</h1>'

# 5. url 생성
from flask import url_for
with app.test_request_context():
    # test_request_context()는 Flask 애플리케이션의 테스트 환경을 설정하는 방법.
    # 테스트 컨텍스트 내에서 Flask의 기능을 테스트할 수 있도록 해준다.
    print(url_for('index'))         # /
    print(url_for('tag_escape', page=10))   # /html/10
    print(url_for('user_name', name='홍길동'))     # /user/홍길동
    print(url_for('static', filename='css/bootstrap.min.css'))

# 6. Method
from flask import request
@app.route('/methods/<name>', methods=['GET', 'POST'])
def methods(name):
    print(request.method)
    return f'이름: {name}'

@app.route('/methods/<int:age>', methods=['GET'])
def methods_age(age):
    return f'나이: {age}'

# JSON
from flask import render_template
@app.route('/json_html')
def json_html():
    return render_template('html/basic.html')

from flask import jsonify
@app.route('/json_echo', methods=['POST'])
def json_echo():
    '''
    jsons = {'name':'홍길동', 'age': 15}
    return jsons
    '''
    if request.is_json:
        jsons=request.get_json()
    else:
        jsons = request.form.to_dict(flat=False) # flat=False => seliarlize를 막아줌
    
    print(f'{request.is_json}, {jsons}')
    
    return jsonify(jsons)

if __name__ == '__main__':
    app.run(debug=True)