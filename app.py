from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def Overwatch_characters_info():
    url = "https://overfast-api.tekrop.fr/heroes"

    response = requests.get(url)
    data = response.json()

    return render_template('index.html', 
        heroes=data)    

@app.route('/herodata.html')
def Overwatch_characters_data():
    hero_key = request.args.get('hero')
    if not hero_key:
        return "Missing hero parameter", 400

    hero_slug = hero_key.strip().lower()
    hero_slug = hero_slug.replace(' ', '-').replace('.', '').replace("'", '').replace(':', '')
    url = f"https://overfast-api.tekrop.fr/heroes/{hero_slug}"
    response = requests.get(url)
    data = response.json()

    return render_template('herodata.html',
        hero=data,
        hero_key=hero_key,
        hero_slug=hero_slug)

app.run(debug=True)