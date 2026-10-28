from flask import Flask, render_template, request
from country import country_data, country_select, get_country_options
from waitress import serve

import os

print("SERVER FILE:", os.path.abspath(__file__))
print("CURRENT DIRECTORY:", os.getcwd())
print("TEMPLATE FOLDER:", os.path.abspath("templates"))

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index(): 
    return render_template('index.html') 

@app.route("/search")
def search():
    user_country = request.args.get('country')
    data = country_data(user_country) 
    countries = get_country_options(data)

    return render_template(
        "index.html", 
        countries = countries
    )

@app.route("/menu/countries")
def api_countries():
     user_country = request.args.get('country')
     data = country_data(user_country) 
     countries = get_country_options(data)
     return countries


@app.route("/country")
def get_flag():
    user_country = request.args.get('country')

    data = country_data(user_country) 
    selected_country = get_country_options(data)[0]

    return render_template(
        "country.html", 
        name = selected_country['names']['common'], 
        capital = selected_country['capitals'][0]['name'],
        continent = selected_country['continents'][0], 
        gov_type = selected_country['government_type'],
        driving_side = selected_country['cars']['driving_side'], 

        flag_url = selected_country['flag']['url_png'], 
        flag_description = selected_country['flag']['description'] 
    )


if __name__ == "__main__":
    print("Starting server...")
    serve(app, host="0.0.0.0", port=8000)

