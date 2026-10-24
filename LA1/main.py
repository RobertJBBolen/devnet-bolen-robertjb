import random
import requests

pokemon_pool = ["pikachu", "charizard", "bulbasaur", "squirtle", "eevee"]

secret_name = random.choice(pokemon_pool)

url = f"https://pokeapi.co/api/v2/pokemon/{secret_name}"

response = requests.get(url, timeout=10)
    
if response.status_code == 200:
    data = response.json()

    name = data["name"]
    height = data["height"]
    weight = data["weight"]
    ability = data["abilities"][random.randint(0,1)]["ability"]["name"]

    print("-----GUESS THAT POKEMON!!-----")
    print(f"Pokemon's Height: {height}")
    print(f"Pokemon's Weight: {weight}")
    print(f"Pokemon's Ability: {ability}")

    for attempt in range(3):
            guess = input("\nYour guess: ").lower().strip()
            
            if guess == name:
                print("Congrats You guessed that pokemon!!")
                break
            else:
                print("Wrong!!!")

    else:
        print(f"\nGame over! The correct answer was {name.capitalize()}.")

else:
    print(f"Error: Received status code {response.status_code} from PokeAPI.")