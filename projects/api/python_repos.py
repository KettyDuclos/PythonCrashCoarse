import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("status code:", r.status_code)

#Store API reponse in a variable.
response_dict = r.json()

#process results
print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])

#Explore information about the repositories.
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

#Examine the first repository
repo_dict = repo_dicts[0]
print('\nKeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

#Selected information about the repositories
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('ID:', repo_dict['id'])
print('Owner:', repo_dict['owner']['login'])


#Visualizing Repositories Using Pygal
#Visualization showing the relative popularity of Python projects on Github

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Make visualization.








