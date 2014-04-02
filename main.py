""" You are a hacker, looking to delve into the world's megacorporations for
fun and profit.  One day, a friend contacts you looking to gain info about IntroSys Inc.
From there, your journey is up to you."""

from flask import Flask
from flask.ext.heroku import Heroku

mud_app = Flask(__name__)
heroku = Heroku(mud_app)

@mud_app.route('/mud')
def hello_world():
  return 'Hello World!'

@mud_app.errorhandler(404)
def page_not_found(e):
  return 'You didn\'t want to go here. Go to <a href=\'/mud\'>this page</a> instead.', 404

