from flask import Flask, request, render_template
import codecs
app = Flask(__name__)
arr = []
arrcolor = []
@app.route('/form')
def index():
    global arr
    global arrcolor
    if u'name' in request.args:
        for name in request.args:
            if name == 'name':
                arr.append(request.args[name])
        for color in request.args:
            if color == 'color':
                arrcolor.append(request.args[color])
    table = codecs.open('tables.csv', 'w', 'utf-8')
    csv = map(';'.join, zip(arr, arrcolor))
    for i in csv:
        table.write(i)
        table.write('\r\n')
    table.close()
    return render_template('form.html')


@app.route('/table')
def table_csv():
    global arr
    global arrcolor
    table = codecs.open('tables.csv', 'w', 'utf-8')
    csv = map(';'.join, zip(arr, arrcolor))
    for i in csv:
        table.write(i)
        table.write('\r\n')
    table.close()
    return render_template('form.html')

@app.route('/stats')
def stats():
    global arrcolor
    dic_count = {}
    for color in arrcolor:
        color = color.lower()
        if color in dic_count:
            dic_count[color] += 1
        else:
            dic_count[color] = 1
    insert = max(dic_count, key=lambda k: dic_count[k])
    return render_template('max.html', insert=insert)
    
if __name__ == '__main__':
    app.run(debug=True)
