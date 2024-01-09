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
    user_id = session.get('id')
    id = request.args.get('id')

    if id == '1' or id is None:
        if user_id is not None:
            getTemp = render_template('getTemperature.sql')
            g.cursor.execute(getTemp, (user_id,))
            user_temps = g.cursor.fetchall()
            response = render_template('index.html', naslov='Početna stranica', username=session.get('username'), data=user_temps, tip='Temperatura')
        return response, 200
    
    if id == '2':
        if user_id is not None:
            getHmds = render_template('getHumidity.sql')
            g.cursor.execute(getHmds, (user_id,))
            user_hmds = g.cursor.fetchall()
            response = render_template('index.html', naslov='Početna stranica', username=session.get('username'), data=user_hmds, tip='Vlaga')
        return response, 200
    
@app.post('/delete_last_temp')
def delete_last_temp():
    user_id = session.get('id')

    deleteTemp = render_template('deleteLastTemperature.sql')
    g.cursor.execute(deleteTemp, (user_id,))
    g.connection.commit()

    return redirect(url_for('index'))

@app.post('/delete_last_hum')
def delete_last_hum():
    user_id = session.get('id')

    deleteHum = render_template('deleteLastHumidity.sql')
    g.cursor.execute(deleteHum, (user_id,))
    g.connection.commit()

    return redirect(url_for('index', id = 2))

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
    username = request.form.get('username')
    password = request.form.get('password')

    getUser = render_template('getUser.sql')
    g.cursor.execute(getUser, (username, password))
    user = g.cursor.fetchone()

    if user:
        session['id'] = user[0]
        session['username'] = user[1]
        print(session.get('id'), session.get('username'))
        return redirect(url_for('index'))
        
    else:
        return render_template('login.html', poruka='Uneseni su pogresni podaci')    
        
@app.post('/temperatura')
def put_temperatura():
    global put_temperatura
    response = make_response()

    if request.json.get('temperatura') is not None:
        query = render_template('writeTemperature.sql', value=request.json.get('temperatura'))
        g.cursor.execute(query)
        response.data = 'Uspješno ste postavili temperaturu'
        response.status_code = 201

    else:
        response.data = 'Niste napisali ispravan ključ'
        response.status_code = 404
        
    return response

@app.get('/temperatura')
def last_temperature():
    user_id = session.get('id')  
    
    getLastTemp = render_template('getLastTemperature.sql')
    
    g.cursor.execute(getLastTemp, (user_id,))
    last_temperature = g.cursor.fetchone()
    
    if last_temperature:
        return {"temperatura": last_temperature[0]}, 200
    else:
        return {"error": "Temp not found"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)