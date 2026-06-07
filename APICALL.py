import requests
base_url = "https://pokeapi.co/api/v2/"


def getPokeInfo(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrive : {response.status_code}")


poke_name = 'typhlosion'
Pokemon_dic = getPokeInfo(poke_name)
if Pokemon_dic:
    print(f"Name :{Pokemon_dic["name"]}")
    print(f"id :{Pokemon_dic["id"]}")
    print(f"height :{Pokemon_dic["height"]}")
    print(f"weight :{Pokemon_dic["weight"]}")
