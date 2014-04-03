""" You are a hacker, looking to delve into the world's megacorporations for
fun and profit.  One day, a friend contacts you looking to gain info about IntroSys Inc.
From there, your journey is up to you."""

from flask import Flask, g, render_template, session, request, redirect
from flask import flash
from flask.ext.heroku import Heroku
import os
from models import validateLogin, createAccount 
import models

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

# WARNING: TURN OFF IF PRODUCTION
app.debug = True
heroku = Heroku(app)

@app.route('/mud')
def hello_world():
  if 'user' in session:
    return 'Hello {}'.format(session['user'])
  else:
    # 307 is a temporary redirect
    flash('Redirect from {}'.format(request.url, 'info'))
    return redirect('/login', 307)

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
  uname = request.form['username']
  passw = request.form['password']
  if 'createaccount' in request.form:
    result = createAccount(uname, passw)
    return "MSG: {}".format(result['message'])
  elif 'login' in request.form:
    login = validateLogin(uname, passw)
    if login['status']:
      session.user = login['user']
      return "Login successful."
    else:
      return login['message']

@app.route('/logout')
def logout():
  session.pop('user', None)
  session.sessionMessages += "Logged out.<br>"
  return redirect('/login',307)

@app.errorhandler(404)
def page_not_found(e):
  return "You didn't want to go here. Go to <a href='/mud'>this page</a> instead.", 404

@app.route('/debug')
def debug():
  g.yo = 'sup'
  return render_template('debug.html')
