import requests
from dotenv import load_dotenv
import os
import json
load_dotenv()


token = os.getenv("GITHUB_ACCESS_TOKEN")

url = f"https://api.github.com/repos/{os.getenv('OWNER')}/{os.getenv('REPO')}/commits"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))

else:
    print(f"Error: {response.status_code} - {response.text}")
