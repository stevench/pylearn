#-*- encoding:utf-8 -*-
from flask import Flask,render_template,request,session,redirect,flash,abort,jsonify
from database import db_session
from models import User
#from nav import nav

app = Flask(__name__)

app.config["SECRET_KEY"] = 'you never guess it'

#nav.init_app(app)

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/',methods=['GET'])
@app.route('/home',methods=['GET'])
def home():
    return render_template("index.html",login=False)

@app.route('/login',methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        user = User.query.filter(User.name==username).first()
        if user is not None and user.check_password(password):
            session['username'] = username
            session['login'] = True
            return jsonify({'flag':1})
        else:
            return jsonify({'flag':0})
    else:
        abort(404)

@app.route('/register',methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    if username and password:
        user = User(username,password,email)
        db_session.add(user)
        db_session.commit()
        return jsonify({'flag':1})
    else:
        return jsonify({'flag': 0})

@app.route('/about',methods=['GET'])
def about():
    return 'about'

@app.route('/logger',methods=['GET','POST'])
def log():
    return 'logger'

@app.route('/picture',methods=['GET','POST'])
def picture():
    return 'picture'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)
