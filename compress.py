# Auxiliary script, downloads latest root file from the repository, writes it to the distribution,
# then packs distribution into a tar archive and sends it to the repository

import os
import tarfile
from settings import CURRENT_VERSION
import requests

import requests

with open("dist/Cardes/root.json", 'wb') as root_file:
    root_file.write(requests.get(
        f"http://repo.aiop.su:6006/metadata/{requests.get(f'http://192.168.0.184:6006/').text}.root.json").content)
with tarfile.open("release_archives/" + CURRENT_VERSION + ".tar", "w") as tar:
    for file in os.listdir("dist/Cardes"):
        tar.add("dist/Cardes/" + file, arcname=file)
print(requests.post("http://192.168.0.184:6006/", files=[(tar.name.split('\\')[-1], open(tar.name, 'rb'))]).text)
