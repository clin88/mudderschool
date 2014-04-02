from flask import Flask
mud_app = Flask(__name__)

@mud_app.route('/mud')
def hello_world():
  return 'Hello World!'

@mud_app.errorhandler(404)
def page_not_found(e):
  return 'You didn\'t want to go here. Go to <a href=\'/mud\'>this page</a> instead.', 404

