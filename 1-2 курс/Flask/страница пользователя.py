from flask import Flask
app = Flask(__name__)

@app.route('/user/<user>')
def index(user):
    return u'This is the page of ' + user.capitalize()

if __name__ == '__main__':
    app.run()
