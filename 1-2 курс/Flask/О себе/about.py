from flask import Flask, request, render_template
import codecs, re
app = Flask(__name__)
arrNames = []
arrWords = []
@app.route('/form')
def index():
    global arr
    if u'name' in request.args:
        for about in request.args:
            if about == 'about':
                arrWords.append(request.args[about])
    for check in arrWords:
        m = re.search(u'(С|с)обак(а(х|ми)?|и|е|у|ой)?', check)
        if m != None:
            for name in request.args:
                if name == 'name':
                    arrNames.append(request.args[name])
            table = codecs.open('txt.txt', 'w', 'utf-8')            
            txt = map('-'.join, zip(arrNames, arrWords))
            for i in txt:
                table.write(i)
                table.write('\r\n')
        table.close()
                            
        
        
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

