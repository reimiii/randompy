# import requests

# req = requests.get("https://reimi.my.id")
# print(req.status_code)

import requests
import time
while True:
    req = requests.get("https://blog-mi.reimi.my.id")
    print(req.status_code)
    if req.status_code != 200:
        pass
    time.sleep(3)