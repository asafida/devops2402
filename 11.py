from datetime import  datetime
print(datetime.now())

import requests
response = requests.get("https://api.github.com/users/avielb/repos")
print(response.json())
for repo in response.json():
    print(repo["full _name"])

