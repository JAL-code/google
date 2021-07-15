import requests
import json
import time

# Monitor your API requests to GitHub with this file.
# Goto the following page and update to find limit per hour
# https://api.github.com/rate_limit
# See resources -> search

url = 'https://api.github.com/search/repositories?q=language:python&sort:updated-desc&topic:tensorflow'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
limit_time = 1618250773
localtime = time.asctime( time.localtime(limit_time))
print ("Limit 10 current time :", localtime)
timerun = time.asctime( time.localtime(time.time()) )
print ("Runtime :", timerun)
print(f"Total respositories: {response_dict['total_count']}")

# Process results.
print(response_dict.keys())
readable_file = 'data/readable_python_results.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Example the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

print("\nSelected information about each repository: ")

