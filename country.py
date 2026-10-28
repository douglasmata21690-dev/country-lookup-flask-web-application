from dotenv import load_dotenv
from pprint import pprint
import os 
import requests 

print("FILE IS RUNNING")

load_dotenv(override=True)

AUTH = os.getenv("API_KEY")

# for working in terminal
def country_select (data):
    objects = data['data']['objects']

    if len(objects) == 1:
       selected_country = objects[0]
    else:   
       print("\nMultiple countries found:\n")   
       for i, country in enumerate(objects):
           print(f"{i + 1}. {country['names']['common']}")
       
       choice = int(input("\nWhich country do you want? Type the number."))
       selected_country = objects[choice - 1]

    return selected_country

def get_country_options(data):
    country_options = data['data']['objects']
    return country_options

def country_data (country = "canada"):
    base_url = f"https://api.restcountries.com/countries/v5/names.common?q={country}&pretty=1"
    headers= {'Authorization': f'Bearer {AUTH}'}

    country_data = requests.get(base_url, headers=headers).json()

    return country_data

# just for printing in terminal
def flag_lookup (selected_country): 
       
       print(f"Name: {selected_country['names']['common']}")
       print(f"Capital: {selected_country['capitals'][0]['name']}")
       print(f"Continent: {selected_country['continents'][0]}")
       print(f"Government type: {selected_country['government_type']}")
       print(f"They drive on the {selected_country['cars']['driving_side']} side")

       print(f"{selected_country['flag']['description']}")
       print(f"{selected_country['flag']['url_png']}")
       

if __name__ == "__main__": 
    print("country info:\n")

    country = input("What country do you want to learn about?: \n")
    data= country_data(country) 
    get_country_options(data)
    selected_country = country_select(data)

    try: 
      flag_lookup(selected_country)
    except IndexError: 
      print("Error. Information not found. Try another country. \n") 


    
    