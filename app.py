from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def Overwatch_characters_info():
    url = "https://overfast-api.tekrop.fr/heroes"

    response = requests.get(url)
    data = response.json()
    
    return render_template('index.html', 
        name=data[0].get("name"),
        portrait=data[0].get("portrait"))

app.run(debug=True)