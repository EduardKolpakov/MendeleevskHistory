from flask import Flask, render_template, request, redirect
import sqlite3 as sql

app = Flask(__name__)


def call_red(url):
    return redirect('http://127.0.0.1:8080/main', code=302)


@app.route('/main')
def main():
    return render_template('main.html', title='История города')


@app.route('/', methods=['GET', 'POST'])
def reg():
    if request.method == 'GET':
        return render_template('registry.html', title='Опрос')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        con = sql.connect('users.sqlite')
        cur = con.cursor()
        print(name, email, city)
        cur.execute("INSERT INTO user_info(name, email, city) VALUES(?,?,?)", (name, email, city))
        con.commit()
        call_red('form')
        return redirect('http://127.0.0.1:8080/main', code=302)


@app.route('/info')
def info():
    return render_template('info.html', title='Информация')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакты')


@app.route('/maps')
def maps():
    return render_template('map.html', title="Карта")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
