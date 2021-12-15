import requests

req = requests.get("https://swapi.dev/api/people/1/")
orang = req.json()
print(f"namanya :\t\t\t{orang['name']}")
print(f"kelaminnya :\t\t\t{orang['gender']}")

print("pokonya film :")
for film in orang['films']:
    req = requests.get(film)
    film = req.json()
    print("tontonan : ", film['title'])