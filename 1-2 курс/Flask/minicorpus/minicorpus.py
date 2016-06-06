import os, codecs, re
from flask import Flask, url_for, request,\
     render_template, redirect

app = Flask(__name__)
user = u'guest'
adminPassword = u'123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html', user=user)

@app.route('/login')
def login():
    global user
    try:
        login = request.args['login']
        pwd = request.args['password']
        if login == u'admin' and pwd != adminPassword:
            user = u'guest'
        else:
            user = login
        return redirect(url_for('search'))
    except:
        return render_template('login.html', user=user)


@app.route('/result', methods=['GET'])
def result():
    try:
        word = request.args['word']
        if len(request.args['length']) > 0:
            length = int(request.args['length'])
        else:
            length = -1
        if 'capital' in request.args:
            capital = True
        else:
            capital = False
        
        sentences = search_corpus(word, length, capital)
        if user != u'admin' and len(sentences) > 5:
            sentences = sentences[:5]
            message = u'Только администратор может' +\
                      u' посмотреть больше пяти примеров!'
        else:
            message = None
        return render_template('result.html',\
                               user=user,\
                               sentences=sentences,\
                               message=message)
    except:
        return redirect(url_for('search'))


def search_corpus(word, length, capital):
    sentences = get_all_sentences()
    result = []
    regexWord = u'\\b' + word + u'\\b'
    for sentence in sentences:
        words = re.findall(regexWord, sentence, flags=re.U)
        if length > 0:
            words = [w for w in words if len(w) == length]
        else:
            words = [w for w in words if len(w) > 0]
        
        if capital == False:
            words = [w for w in words if w[0].lower() == w[0]]
        
        if len(words) == 0:
            continue
        for w in words:
            regexWord = u'\\b' + w + u'\\b'
            sentence = re.sub(regexWord,\
                u'<font color="blue">' + w + u'</font>',\
                sentence, flags=re.U)
        result.append(sentence)
    return result


def get_all_sentences():
    sentences = []
    for root, dirs, files in os.walk(u'./corpus'):
        for fname in files:
            if not fname.endswith(u'.txt'):
                continue
            f = codecs.open(root + u'/' + fname,
                            'r', 'utf-8-sig')
            text = f.read()
            sentences += re.findall(u'[^.?!]+[.?!]+ *',\
                                    text)
            f.close()
    return sentences

if __name__ == '__main__':
    app.run(debug=True)
