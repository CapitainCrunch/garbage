from flask import Flask, request
import codecs
app = Flask(__name__)
arr = []

@app.route('/')
def index():
    global arr
    f = 1
    if u'name' in request.args:
        s = request.args['name'] + u';'
        if u'swahili' in request.args:
            if request.args['swahili'] == u'on':
                s = s + u'+;'
        else:
            s = s + u' ;'
        if u'signlang' in request.args:
            if request.args['signlang'] == u'on':
                s = s + u'+;'
        else:
            s = s + u' ;'
        if u'neuro' in request.args:
            if request.args['neuro'] == u'on':
                s = s + u'+'
        else:
            s = s + u' '
        for i in range(len(arr)):
            if arr[i].startswith(request.args['name']):
                arr[i] = s + u'\n'                  
            else:
                f = 0
        if f == 0:
            s = s + u'\n'
            arr.append(s)
    for i in arr:
        print i
    
    return u'<html><head><title>Курсы по выбору</title>' +\
           u'</head><body>' +\
           u'<form>Фамилия, Имя: <input type="text" name="name"><br>' +\
           u'<input type="checkbox" name="swahili">Суахили<br>' +\
           u'<input type="checkbox" name="signlang">Язык жестов<br>' +\
           u'<input type="checkbox" name="neuro">Нейролингвистика<br>' +\
           u'<input type="submit" value="Отправить">' +\
           u'</form>' +\
           u'<a href="/table">Внести данные в CSV таблицу</a>' +\
           u'</body></html>'
    

@app.route('/table')
def table_csv():
    global arr
    table = codecs.open('table.csv','w','utf-8')
    s1 = u'Имя;Суахили;Язык жестов;Нейролингвистика' + u'\n'
    table.write(s1)   
    for i in arr:
        table.write(i)
    table.close()
    return u''

    
    
if __name__ == '__main__':
    app.run(debug=True)
