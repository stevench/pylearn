#-*- encoding:utf-8 -*-
from flask import Flask,render_template,request,session,redirect,flash,abort,jsonify
from flask_bootstrap import Bootstrap
from database import db_session
from models import User,Logger
#from nav import nav

app = Flask(__name__)

app.config["SECRET_KEY"] = 'you never guess it'

bootstrap = Bootstrap(app)

#nav.init_app(app)

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/',methods=['GET'])
@app.route('/home',methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/login',methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        user = User.query.filter(User.name==username).first()
        if user is not None and user.check_password(password):
            session['userId'] = user.id
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

@app.route('/getLog',methods=['GET'])
def getLog():
    userId = session.get('userId')
    loggers = Logger.query.filter(Logger.user==userId).all()
    logger_lst = [{'id':logger.id,'title':logger.title,'forwho':logger.forwho,'content':logger.content,'date':logger.date} for logger in loggers]
    return jsonify({'loggers':logger_lst})

@app.route('/addLog',methods=['POST'])
def addLog():
    title = request.form.get('title')
    forwho = request.form.get('forwho')
    content = request.form.get('content')
    date = request.form.get('date')
    user = session.get("userId")
    logger = Logger(title,forwho,content,date,user)
    db_session.add(logger)
    db_session.commit(logger)
    return '1'


@app.route('/picture',methods=['GET','POST'])
def picture():
    return 'picture'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)
