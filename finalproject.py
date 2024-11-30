import csv
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'pokemon'



with open('Pokemon.csv', 'r') as f:
    rows = list(csv.reader(f))[1:]
    
    



    @app.route("/", methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            name = request.form.get('name').title()
            session['name'] = name
            return redirect(url_for("pokedex"))
        return render_template('index.html')


    

    @app.route('/pokedex', methods=['GET'])
    def pokedex():
        pokedex = {row[1]: row[3:] for row in rows}
        name = session.get('name')
        try:

            pokemon = pokedex[name]
            return render_template('pokedex.html', pokemon=pokemon, name=name)
        except KeyError:
            return render_template('fail.html')
    
app.run()
