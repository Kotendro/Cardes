# Auxiliary script, requests latest root metadata file from the server to pack it with the distribution.

import requests
with open("root.json", 'wb') as root_file:
    root_file.write(requests.get(f"http://repo.aiop.su:6006/metadata/{requests.get(f'http://192.168.0.184:6006/').text}.root.json").content)