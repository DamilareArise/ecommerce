import requests

def get_countries():
    
    url = "https://country-state-city-search-rest-api.p.rapidapi.com/allcountries"

    headers = {
        "x-rapidapi-key": "d5c5fe5c5dmshf006ed9f1ab63d6p1c8a6djsn1caa7867a7e8",
        "x-rapidapi-host": "country-state-city-search-rest-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    info = response.json()
    countries = []
    for i in info:
        country = i['name']
        countries.append((country, country))
        
        
    return countries
    
