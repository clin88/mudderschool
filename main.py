from flask import Flask
mud_app = Flask(__name__)

@mud_app.route('/mud')
def hello_world_lulu():
  return 'Hello World!'



def main():
  app_lulu.run(debug=True)

