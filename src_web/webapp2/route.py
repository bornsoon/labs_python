# from flask import Flask
from flask import render_template, url_for

# app = Flask(__name__)
from webapp2 import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('/basic/helloworld.html', msg='안녕하세요.<br>abc')

@app.route('/reqres/input')
def req_input():
    return render_template('/basic/input.html')

from flask import request
@app.route('/reqres/result', methods=['POST'])
def req_result():
    result = {}
    if request.method == 'POST':
        result['name'] = request.form['name']
        result['age'] = request.form['age']
    else:
        result['name'] = request.args.get('name')
        result['age'] = request.args.get('age')

    result['msg'] = request.args.get('msg')

    return render_template('/basic/result.html', results=result)

from flask import session
app.secret_key = b'5#030!_AxC\3c'
@app.route('/session/count')
def session_count():
    count = 0

    if 'count' in session:
        count = session['count']

    if count > 10:
        session.pop('count', 0)
        # session.clear()  # 전체 초기화
    else:
        session['count'] = count + 1

    # session.peramanent = True
    # app.permanent_session_lifetime = timedelta(minutes=5)

        return f'count: {count}'
    
from flask import flash
@app.errorhandler(404)
def page_not_found(error):
    flash('페이지를 찾을 수 없습니다,')
    return render_template('/basic/error.html', msg=error), 404

from flask import redirect
@app.route('/redirect')
def url_redirect():
    app.logger.debug('페이지 이동')
    return redirect(url_for('session_count'))

# if __name__ == '__main__':
#     app.run(debug=True)