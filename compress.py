# Auxiliary script, packs distribution into a tar archive and sends it to the server

import os
import tarfile
from settings import CURRENT_VERSION
import requests

with tarfile.open("release_archives/" + CURRENT_VERSION + ".tar", "w") as tar:
    for file in os.listdir("dist/Cardes"):
        tar.add("dist/Cardes/" + file, arcname=file)
# print(tar.name.split('\\')[-1])
print(requests.post("http://192.168.0.184:6006/", files=[(tar.name.split('\\')[-1], open(tar.name, 'rb'))]).text)