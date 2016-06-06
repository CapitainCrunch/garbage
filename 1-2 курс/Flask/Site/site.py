from flask import Flask, request, render_template
import codecs, re
from datetime import *
app = Flask(__name__)
_DICT = {}
@app.route('/')
def index():
    global _DICT
    if u'name' in request.args:
        for name in request.args:
            if name == 'name':
                dn = datetime.now()
                a = str(dn)[11:16]
                h, m = a.split(':')
                _DICT[request.args[name] + ' ' + a] = None
    for outname in _DICT.keys():
        if outname in request.args:
            if request.args[outname] == u'on':
                dout = datetime.now()
                outtime = str(dout)[11:16]
                _DICT[outname] = outtime
    return render_template('form.html', _DICT=_DICT)

if __name__ == '__main__':
    app.run(debug=True)
