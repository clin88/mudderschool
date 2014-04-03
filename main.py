""" You are a hacker, looking to delve into the world's megacorporations for
fun and profit.  One day, a friend contacts you looking to gain info about IntroSys Inc.
From there, your journey is up to you."""

from flask import Flask, g, render_template
from flask.ext.heroku import Heroku

app = Flask(__name__)

# WARNING: TURN OFF IF PRODUCTION
# app.debug = True
heroku = Heroku(app)

@app.route('/mud')
def hello_world():
  return 'Hello World!'

@app.errorhandler(404)
def page_not_found(e):
  return 'You didn\'t want to go here. Go to <a href=\'/mud\'>this page</a> instead.', 404

@app.route('/debug')
def debug():
  g.yo = 'sup'
  return render_template('debug.html')
