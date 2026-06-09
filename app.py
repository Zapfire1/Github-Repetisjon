from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def Overwatch_characters_info():
    url = "https://overfast-api.tekrop.fr/heroes"

    response = requests.get(url)
    data = response.json()
    
    return render_template('index.html', 
        heroes=data)

app.run(debug=True)