from django.http import JsonResponse
import os 
import requests
import dotenv
import socket
import json

def pokemon_show(request, pk):
    api_url = f"http://pokeapi.co/api/v2/pokemon/{pk}/"
    res = requests.get(api_url)
    body = json.loads(res.content)
    pokemon_name  = body["name"]
    pokemon_id = body["id"]
    pokemon_type = body["types"][0]["type"]["name"]

    key = os.environ.get("GIPHY_KEY")
    root = 'https://api.giphy.com'
    path = '/v1/gifs/search'
    pokemon_query = pokemon_name
    limit = 1
    offset = 0

    url = (f"{root}{path}?api_key={key}&q={pokemon_query}&limit=(int{limit})&offset=(int{offset})")
    giphy_res = requests.get(url)
    body = json.loads(giphy_res.content)
    gif_url = body['data'][0]['url']

    response = requests.get(url)
    gif_body = json.loads(response.content)
    gif = gif_body['data'][0]['images']['fixed_height_still']['url']
    
    
    return JsonResponse({ "id": pokemon_id, "name": pokemon_name, "types": pokemon_type, "gif": gif})

    
    