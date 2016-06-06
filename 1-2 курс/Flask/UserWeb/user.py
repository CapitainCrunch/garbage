from flask import Flask, render_template
import codecs

app = Flask(__name__)
arr_names = []
user = 'Гость'

names = codecs.open(u'names.txt','r','utf-8-sig')
for line in names:
    line = line.split()
    for name in line:
        name = name.strip(u'.,!&;><\\:')
        arr_names.append(name)

@app.route('/user/<user>')
def index(user):
    if user in arr_names:
        return render_template('ban.html', user=user)        
    else:
        return render_template('not_banned.html', user=user)
names.close()

if __name__ == '__main__':
    app.run(debug=True)
