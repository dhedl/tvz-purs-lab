from flask import Flask, url_for, redirect, request, make_response, render_template, session, g
import jinja2, MySQLdb

app = Flask("Prva flask aplikacija")

app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

@app.before_request
def before_request_func():
    g.connection = MySQLdb.connect(host="localhost", user="app", passwd="1234", db="lvj6")
    g.cursor = g.connection.cursor()

    if request.path == '/login' or request.path.startswith('/static') or request.path == '/temperatura':
        return
    
    if session.get('username') is None:
        return redirect(url_for('login'))
    
@app.after_request
def after_request_func(response):
    g.connection.commit()
    g.connection.close()
    return response

@app.get('/')
def index():   
    id = request.args.get('id')

    if id == '1' or id is None:
        g.cursor.execute(render_template('getTemperature.sql', id_korisnika=session.get('id')))
        user_temps = g.cursor.fetchall()
        response = render_template('index.html', naslov='Početna stranica', username=session.get('username'), data=user_temps, tip='Temperatura', tip_podatka = id)
        return response, 200
    
    if id == '2':   
        g.cursor.execute(render_template('getHumidity.sql', id_korisnika=session.get('id')))
        user_hmds = g.cursor.fetchall()
        response = render_template('index.html', naslov='Početna stranica', username=session.get('username'), data=user_hmds, tip='Vlaga', tip_podatka = id)
        return response, 200
    
@app.post('/delete/<int:id_stupca>')
def delete(id_stupca):
    id_podatka = request.args.get('id_podatka')

    if id_podatka == '2':
        g.cursor.execute(render_template('deleteHumidity.sql', id_hum=id_stupca))
        return redirect(url_for('index', id=id_podatka))

    else:    
        g.cursor.execute(render_template('deleteTemperature.sql', id_temp=id_stupca))  
        if id_podatka == '1':
            return redirect(url_for('index', id=id_podatka))
        else:
            return redirect(url_for('index'))

@app.get('/login')
def login():
    response = render_template('login.html', naslov='Stranica za prijavu')
    return response, 200

@app.get('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))

@app.post('/login')
def check():
    g.cursor.execute(render_template('getUser.sql', username = request.form.get('username'), password = request.form.get('password')))
    user = g.cursor.fetchone()

    if user:
        session['id'] = user[0]
        session['username'] = user[1]
        return redirect(url_for('index'))
        
    else:
        return render_template('login.html', naslov='Stranica za prijavu', poruka='Uneseni su pogresni podaci')    
        
@app.post('/temperatura')
def put_temperatura():
    global put_temperatura
    response = make_response()

    if request.json.get('temperatura') is not None:
        
        g.cursor.execute(render_template('writeTemperature.sql', value=request.json.get('temperatura')))
        response.data = 'Uspješno ste postavili temperaturu'
        response.status_code = 201

    else:
        response.data = 'Niste napisali ispravan ključ'
        response.status_code = 404
        
    return response

@app.get('/temperatura')
def last_temperature():
    g.cursor.execute(render_template('getLastTemperature.sql'))
    last_temperature = g.cursor.fetchone()
    
    if last_temperature:
        return {"temperatura": last_temperature[0]}, 200
    else:
        return {"error": "Temp not found"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)