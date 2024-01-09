from flask import Flask, url_for, redirect, request, make_response

app = Flask("Prva flask aplikacija")

temperatura = []

# 1. zadatak
@app.get('/')
def index():
    return 'Pocetna stranica'

@app.get('/login')
def login():
    return 'Stranica za prijavu'

#2. zadatak
@app.post('/login')
def check():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is not None and password is not None:
        if username == 'PURS' and password == '1234':
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    else: 
        return redirect(url_for('login'))
    
#3. zadatak
@app.post('/temperatura')
def rect():
    temp = request.json.get('temperatura')

    if temp is not None:
        global temperatura
        temperatura.append(temp)
        return 'Uspješno ste upisali', 201
    else:
        return 'Niste upisali ispravan ključ', 404

#4. zadatak
@app.get('/temperatura')
def last():
    global temperatura
    json = {
        "temperatura":temperatura[-1]
    }
    resp = make_response(json, 202)
    return resp

#5. zadatak
@app.delete('/temperatura')
def dlt():
    global temperatura

    temp_received = request.args.get('temperatura')

    if temp_received is not None:
        try:
            temp_to_delete = int(temp_received)
            if temp_to_delete in temperatura:
                # Brisanje odredene temperature
                temperatura.remove(temp_to_delete)
                return f"Uspješno ste obrisali temperaturu {temp_to_delete}", 202
            else:
                return f"Upisali ste neispravan ključ (temperatura {temp_to_delete} not found)", 404
        except ValueError:
            return "Upisali ste neispravan ključ (not an integer)", 404
    else:
        return "Nije predan URL parametar", 400
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
