from flask import Flask
mud_app = Flask(__name__)

@mud_app.route('/mud')
def hello_world_lulu():
  return 'Hello World!'




if __name__ == '__main__':
  app_lulu.run(debug=True)
