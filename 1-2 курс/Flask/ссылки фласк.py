from flask import Flask, url_for

app = Flask (__name__)

@app.route('/g')
def index():
    return u'<html><body><p>Это гоша и он жираф!</p><a href="http://127.0.0.1:5000/P">панда</a></body></html>'

@app.route('/P')
def inde():
    return u'<html><body><p>Это панда и это панда!</p><a href="http://127.0.0.1:5000/g">гоша</a></body></html>'

if __name__ == '__main__':
    app.run()
