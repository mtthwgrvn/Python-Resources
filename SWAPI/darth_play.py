import json
import requests

baseurl = 'https://swapi.co/api'
people_url = f"{baseurl}/people/"
films_url = f"{baseurl}/films/"
starships_url = f"{baseurl}/starships/"
vehicles_url = f"{baseurl}/vehicles/"
species_url = f"{baseurl}/species/"
planets_url = f"{baseurl}/planets/"

def summon_darth(baseurl, resource="", params = {}):
    response = requests.get(baseurl + resource, params=params).json()
    return response

d = requests.get(people_url)
