import os
import requests

links = ["client.py", "server.py"]

for i in ["Hristiyan"]:
    try:
        os.mkdir(i)
    except FileExistsError:
        pass

os.chdir("Hristiyan")
for j in links:
    r = requests.get("https://raw.githubusercontent.com/HristiyanPetkov/Sockets/main/" + j)
    with open(j, "wb") as f:
        for i in r.iter_content(chunk_size=8192):
            f.write(i)