import requests

response = requests.post(url='https://api.pokemonbattle.me/pokemons',
                         headers={
                                  'trainer_token':'ea90833759ce2e50db903fb2a1c90a30',
                                  'Content-Type':'application/json'
                                 },
                         json={
                               "name": "Бульб",
                               "photo": "https://dolnikov.ru/pokemons/albums/101.png"
                             },
                                timeout=5
                        )
print(f' code: {response.status_code}. message:{response.text} ')

response = requests.put(url='https://api.pokemonbattle.me/pokemons',
                         headers={
                             'trainer_token':'ea90833759ce2e50db903fb2a1c90a30',
                             'Content-Type':'application/json'
                                 },
                         json={
                              "pokemon_id": "12642",
                              "name": "New Name",
                              "photo": "https://dolnikov.ru/pokemons/albums/111.png"
                              },
                                timeout=5
                        )
print(f' code: {response.status_code}. message:{response.text} ')

response = requests.post(url='https://api.pokemonbattle.me/trainers/add_pokeball',
                         headers={
                             'trainer_token':'ea90833759ce2e50db903fb2a1c90a30',
                             'Content-Type':'application/json'
                                 },
                         json={
                               "pokemon_id": "12642"
                              },
                                timeout=5
                        )
print(f' code: {response.status_code}. message:{response.text} ')

