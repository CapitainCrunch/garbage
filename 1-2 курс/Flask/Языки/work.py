from flask import Flask, request, render_template
import codecs, re

app = Flask(__name__)

f = codecs.open (u'lang.txt', 'w', 'utf-8-sig')
f.close()

@app.route('/')
def index():
    return render_template ('number.html')

@app.route('/number')
def number():
    chislo = ' '
    if len(request.args) > 0:
        chislo = request.args['num']
        arr = range (int(chislo))
    return render_template ('languages.html', arr=arr)

@app.route('/languages')
def languages():
    arr = []
    s = ''
    f = codecs.open (u'lang.txt', 'w', 'utf-8-sig')
    for i in request.args.values():
        f.write (i + u'\r\n')
        arr.append (i)
    f.close()
    hellos = {}
    hellos[u'русский']=u'привет'
    hellos[u'английский']=u'hello'
    hellos[u'немецкий']=u'hallo'
    hellos[u'французский']=u'bonjour'
    hellos[u'испанский']=u'ola'
    hellos[u'итальянский']=u'ciao'
    for i in arr:
        if i in hellos:
            s = s + hellos[i] + u'<br>'
    return render_template ('hello.html', s=s)


if __name__ == '__main__':
    app.run(debug=True)
